# Senior Code Reviewer Checklist

> Practical review patterns with BAD vs GOOD examples and ready-to-paste PR comments.
> Last updated: 2026-04-30

---

## TOPIC 1 — Webhook Security

### 1.1 HMAC-SHA256: `req.text()` vs `req.json()` order

**The rule:** Always read the raw body first, verify the signature against it, then parse JSON. Calling `req.json()` first consumes the stream and may silently re-serialize the payload — changing whitespace or key order — making the signature check fail or, worse, pass against a different byte sequence.

**Review comment to write:** "You're parsing JSON before verifying the signature. Call `req.text()`, verify HMAC against the raw string, then `JSON.parse()`. Signature must be validated against the exact bytes the sender signed."

```ts
// BAD — signature verified against already-parsed object
export async function POST(req: Request) {
  const body = await req.json();               // stream consumed, bytes gone
  const sig = req.headers.get('x-signature')!;
  if (!verifySignature(JSON.stringify(body), sig, SECRET)) {
    return new Response('Unauthorized', { status: 401 });
  }
  await processEvent(body);
  return new Response('OK');
}

// GOOD — raw bytes preserved for HMAC, parsed afterwards
export async function POST(req: Request) {
  const raw = await req.text();                // raw bytes intact
  const sig = req.headers.get('x-signature')!;
  if (!verifySignature(raw, sig, SECRET)) {
    return new Response('Unauthorized', { status: 401 });
  }
  const body = JSON.parse(raw);               // parse only after verification
  await processEvent(body);
  return new Response('OK');
}
```

---

### 1.2 `timingSafeEqual` — Timing Attack Prevention

**Why it matters:** A naive `===` comparison short-circuits on the first byte mismatch. An attacker can time thousands of requests to determine how many bytes of their forged signature are correct, eventually reconstructing a valid HMAC without the secret.

**What to spot in review:**
- Any HMAC result compared with `===`, `!==`, or `.includes()`
- `Buffer.from(a).toString() === Buffer.from(b).toString()`
- Missing length check before `timingSafeEqual` (it throws if lengths differ)

**Review comment:** "String equality is not constant-time. Use `crypto.timingSafeEqual` after converting both values to `Buffer`. If lengths differ, reject immediately — do not leak that information via the comparison itself."

```ts
import { createHmac, timingSafeEqual } from 'crypto';

// BAD — leaks timing information
function verifySignature(raw: string, received: string, secret: string): boolean {
  const expected = createHmac('sha256', secret).update(raw).digest('hex');
  return expected === received; // short-circuits on first mismatched byte
}

// GOOD — constant-time comparison
function verifySignature(raw: string, received: string, secret: string): boolean {
  const expected = createHmac('sha256', secret).update(raw).digest('hex');
  const a = Buffer.from(expected);
  const b = Buffer.from(received);
  if (a.length !== b.length) return false; // reject; don't pass to timingSafeEqual
  return timingSafeEqual(a, b);
}
```

---

### 1.3 Replay Protection — 5-Minute Timestamp Window

**Pattern:** Provider signs the payload with the current Unix timestamp. Receiver checks that `|now - timestamp| <= 300` (seconds). Without this, an attacker can capture a valid webhook and re-deliver it hours later.

**Review comment:** "There is no timestamp validation. Add an `X-Timestamp` header check: reject requests where `Math.abs(now - ts) > 300`. This prevents replay attacks."

```ts
// BAD — timestamp present but window never checked
function validateTimestamp(tsHeader: string | null): boolean {
  if (!tsHeader) return false;
  return true; // only checks presence, not freshness
}

// GOOD — strict 5-minute window
function validateTimestamp(tsHeader: string | null): boolean {
  if (!tsHeader) return false;
  const ts = parseInt(tsHeader, 10);
  if (isNaN(ts)) return false;
  const now = Math.floor(Date.now() / 1000);
  return Math.abs(now - ts) <= 300;
}

// GOOD — full handler combining timestamp + HMAC
export async function POST(req: Request) {
  const tsHeader = req.headers.get('x-timestamp');
  if (!validateTimestamp(tsHeader)) {
    return new Response('Request too old or missing timestamp', { status: 400 });
  }
  const raw = await req.text();
  const sig = req.headers.get('x-signature')!;
  // Signature covers both timestamp and body to prevent timestamp swapping
  const toSign = `${tsHeader}.${raw}`;
  if (!verifySignature(toSign, sig, SECRET)) {
    return new Response('Unauthorized', { status: 401 });
  }
  // ... process
}
```

---

### 1.4 Idempotency — `webhook_events` Table Pattern

**What to check in PR review:**

1. Is there a `webhook_events` (or equivalent) table with `event_id` as primary/unique key?
2. Is the check `SELECT` → `INSERT` atomic (use `INSERT ... ON CONFLICT DO NOTHING` or a transaction)?
3. Is `processed_at` / `status` updated only after the business logic succeeds?
4. Are there tests for duplicate delivery (same `event_id` delivered twice)?

**Review comment:** "This handler has no idempotency guard. A webhook provider will retry on 5xx or timeout. Without deduplication, an order could be fulfilled twice. Add a `webhook_events` insert with a unique constraint on `event_id`, and skip processing if the row already exists."

```ts
// BAD — no idempotency, double-processing on retry
export async function POST(req: Request) {
  const raw = await req.text();
  // ...verify...
  const event = JSON.parse(raw);
  await fulfillOrder(event.data.orderId); // runs again on every retry
  return new Response('OK');
}

// GOOD — idempotent handler with deduplication table
export async function POST(req: Request) {
  const raw = await req.text();
  // ...verify signature + timestamp...
  const event = JSON.parse(raw) as WebhookEvent;

  // Atomic deduplication: fails silently if event_id already exists
  const { rowCount } = await db.query(
    `INSERT INTO webhook_events (event_id, event_type, received_at, status)
     VALUES ($1, $2, NOW(), 'processing')
     ON CONFLICT (event_id) DO NOTHING`,
    [event.id, event.type]
  );

  if (rowCount === 0) {
    // Already processed — return 200 so provider stops retrying
    return new Response('OK');
  }

  try {
    await fulfillOrder(event.data.orderId);
    await db.query(
      `UPDATE webhook_events SET status = 'done', processed_at = NOW() WHERE event_id = $1`,
      [event.id]
    );
  } catch (err) {
    await db.query(
      `UPDATE webhook_events SET status = 'failed' WHERE event_id = $1`,
      [event.id]
    );
    throw err; // return 500 so provider retries
  }

  return new Response('OK');
}
```

**PR checklist for this pattern:**
- [ ] `webhook_events` table has `UNIQUE` or `PRIMARY KEY` on `event_id`
- [ ] Index on `(event_id, status)` for fast lookups
- [ ] Migration file included
- [ ] Test for duplicate `event_id` returns 200 without re-running business logic
- [ ] Test for failed processing sets `status = 'failed'` and returns 500

---

### 1.5 `waitUntil()` from `@vercel/functions`

**When required:** Vercel Serverless Functions terminate immediately after the `Response` is returned. Any `await` that happens after the return is silently dropped. Use `waitUntil()` to register promises that must complete (logging, audit writes, cache updates) without blocking the response.

**What breaks without it:**
- Audit log writes after `return new Response(...)` are never executed
- Background deduplication table updates are dropped
- Analytics/observability calls never fire

**Review comment:** "You're `await`-ing an audit write after sending the response. On Vercel this will be dropped. Wrap it in `waitUntil()` or move it before the return."

```ts
import { waitUntil } from '@vercel/functions';

// BAD — audit write after return; silently dropped on Vercel
export async function POST(req: Request) {
  const raw = await req.text();
  // ...verify + process...
  const response = new Response('OK');
  await writeAuditLog(event); // never executes — function already terminated
  return response;
}

// GOOD — non-critical work registered with waitUntil
export async function POST(req: Request) {
  const raw = await req.text();
  // ...verify + process...
  waitUntil(writeAuditLog(event)); // Vercel keeps function alive until this resolves
  return new Response('OK');      // response sent immediately
}
```

---

## TOPIC 2 — Next.js 15 App Router Frontend Review

### 2.1 `'use client'` Placement — Identifying Unnecessary Client Components

**The rule:** `'use client'` propagates down the component tree. A single misplaced directive forces everything below it to be client-rendered, losing RSC streaming benefits.

**What to look for in review:**
- Component uses no hooks, no event handlers, no browser APIs — but has `'use client'` anyway
- A large layout or page file is marked `'use client'` because one small interactive child needed it
- `'use client'` placed inside a function body or condition (invalid; it must be the first line)

**Review comment:** "This component only renders static markup and fetches server-side data. Remove `'use client'` — it's unnecessarily forcing client-side rendering for the entire subtree. Extract the interactive part into a small dedicated client component."

```tsx
// BAD — entire page is client component because of one button
'use client';

export default async function ProductPage({ params }: { params: { id: string } }) {
  const product = await fetchProduct(params.id); // works, but loses RSC benefits
  return (
    <main>
      <h1>{product.name}</h1>
      <p>{product.description}</p>
      <button onClick={() => addToCart(product.id)}>Add to cart</button>
    </main>
  );
}

// GOOD — server component with isolated client component
// app/products/[id]/page.tsx (Server Component — no directive)
export default async function ProductPage({ params }: { params: { id: string } }) {
  const product = await fetchProduct(params.id);
  return (
    <main>
      <h1>{product.name}</h1>
      <p>{product.description}</p>
      <AddToCartButton productId={product.id} /> {/* only this is client */}
    </main>
  );
}

// components/AddToCartButton.tsx
'use client';
export function AddToCartButton({ productId }: { productId: string }) {
  return <button onClick={() => addToCart(productId)}>Add to cart</button>;
}
```

---

### 2.2 Hydration Safety — Patterns That Cause Mismatch

**Root cause:** Server renders HTML with one value; client renders with a different value; React sees a mismatch and either crashes or silently re-renders, causing a flash.

**Danger patterns:** `window`, `localStorage`, `Date.now()`, `Math.random()`, `new Date()` called directly in render outside `useEffect`.

**Review comment:** "Calling `Date.now()` directly in render will produce a different value on server vs client, causing a hydration mismatch. Move it into a `useEffect` or derive it from a server-provided prop."

```tsx
// BAD — Date.now() in render causes server/client mismatch
'use client';
export function LastSeen() {
  const ts = Date.now(); // server: 1000, client: 1001 -> MISMATCH
  return <span>Last seen: {new Date(ts).toLocaleTimeString()}</span>;
}

// BAD — localStorage in render (throws on server, mismatches on client)
'use client';
export function Theme() {
  const theme = localStorage.getItem('theme') ?? 'light'; // ReferenceError on server
  return <div className={theme}>...</div>;
}

// GOOD — deferred to useEffect, safe initial state
'use client';
import { useState, useEffect } from 'react';

export function LastSeen() {
  const [ts, setTs] = useState<number | null>(null);
  useEffect(() => { setTs(Date.now()); }, []);
  if (!ts) return null; // or skeleton
  return <span>Last seen: {new Date(ts).toLocaleTimeString()}</span>;
}

export function Theme() {
  const [theme, setTheme] = useState('light'); // safe default matches server
  useEffect(() => {
    setTheme(localStorage.getItem('theme') ?? 'light');
  }, []);
  return <div className={theme}>...</div>;
}
```

---

### 2.3 TanStack Query v5 — Cache Invalidation After Mutations

**Common missed patterns in review:**
- Mutation has no `onSuccess` — stale data shown after create/update/delete
- `invalidateQueries` called with wrong or over-broad key
- Invalidation placed in component logic after `mutateAsync` instead of in mutation config (doesn't run on error paths)
- Using `refetchQueries` when `invalidateQueries` is appropriate (forces immediate network hit)

**Review comment:** "This mutation has no `onSuccess`. After creating a record the list will stay stale until manual refresh. Add `onSuccess: () => queryClient.invalidateQueries({ queryKey: ['todos'] })` to the mutation options."

```ts
// BAD — no cache invalidation after mutation
function useCreateTodo() {
  return useMutation({
    mutationFn: (data: NewTodo) => api.createTodo(data),
    // no onSuccess — list stays stale indefinitely
  });
}

// BAD — invalidation placed outside mutation config, skipped on error
async function handleSubmit(data: NewTodo) {
  await createMutation.mutateAsync(data);
  queryClient.invalidateQueries({ queryKey: ['todos'] }); // not called if mutateAsync throws
}

// GOOD — invalidation inside mutation config, always runs
function useCreateTodo() {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: (data: NewTodo) => api.createTodo(data),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['todos'] });
    },
  });
}

// GOOD — scoped invalidation for detail + list
function useUpdateTodo() {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: ({ id, ...data }: UpdateTodo) => api.updateTodo(id, data),
    onSuccess: (_, { id }) => {
      queryClient.invalidateQueries({ queryKey: ['todos'] });           // list
      queryClient.invalidateQueries({ queryKey: ['todo', id] });        // detail
    },
  });
}
```

---

### 2.4 Zustand in App Router — Server Data Anti-Pattern

**The anti-pattern:** Storing server-fetched data in a Zustand store inside a Server Component, or initializing a store with data that should live in RSC/fetch cache. Server Components and Zustand operate in different environments — the store is client-only.

**Review comment:** "Server Components cannot read from or write to Zustand stores. This data should be fetched in the Server Component via `fetch`/ORM and passed as props. Zustand is appropriate only for ephemeral client UI state (modals, selections, local preferences)."

```tsx
// BAD — server component trying to use Zustand
// app/dashboard/page.tsx (Server Component)
import { useProductStore } from '@/store/products';

export default async function DashboardPage() {
  const products = useProductStore((s) => s.products); // WRONG: hooks can't run in RSC
  return <ProductList products={products} />;
}

// BAD — fetching data in client component and dumping into Zustand
'use client';
export function ProductsProvider() {
  const setProducts = useProductStore((s) => s.setProducts);
  useEffect(() => {
    fetch('/api/products').then(r => r.json()).then(setProducts); // bypasses RSC cache
  }, []);
  return null;
}

// GOOD — server data flows through props; Zustand owns only UI state
// app/dashboard/page.tsx (Server Component)
export default async function DashboardPage() {
  const products = await db.product.findMany(); // server-side fetch, cached by Next.js
  return <ProductList initialProducts={products} />;
}

// components/ProductList.tsx
'use client';
export function ProductList({ initialProducts }: { initialProducts: Product[] }) {
  // Zustand only for selection state, not the product data itself
  const [selected, setSelected] = useProductStore((s) => [s.selected, s.setSelected]);
  return (
    <ul>
      {initialProducts.map(p => (
        <li key={p.id} onClick={() => setSelected(p.id)}>{p.name}</li>
      ))}
    </ul>
  );
}
```

---

### 2.5 `useEffect` Anti-Patterns — Derived State

**The rule:** If a value can be computed from existing state or props during render, it should not live in `useState` + `useEffect`. Effects for derived state introduce an extra render cycle, bugs on stale closures, and unnecessary complexity.

**Review comment:** "This `useEffect` is computing derived state — `fullName` is just `${first} ${last}`. Compute it inline or with `useMemo`. Effects should model synchronization with external systems, not state derivation."

```tsx
// BAD — effect used to derive state
'use client';
import { useState, useEffect } from 'react';

function UserDisplay({ first, last }: { first: string; last: string }) {
  const [fullName, setFullName] = useState('');
  useEffect(() => {
    setFullName(`${first} ${last}`); // extra render cycle, unnecessary state
  }, [first, last]);
  return <p>{fullName}</p>;
}

// BAD — filtering a list with effect instead of memo
function FilteredList({ items, query }: { items: Item[]; query: string }) {
  const [filtered, setFiltered] = useState(items);
  useEffect(() => {
    setFiltered(items.filter(i => i.name.includes(query)));
  }, [items, query]);
  return <ul>{filtered.map(i => <li key={i.id}>{i.name}</li>)}</ul>;
}

// GOOD — derived value computed inline
function UserDisplay({ first, last }: { first: string; last: string }) {
  const fullName = `${first} ${last}`; // computed on every render, zero overhead
  return <p>{fullName}</p>;
}

// GOOD — useMemo for expensive derivations
function FilteredList({ items, query }: { items: Item[]; query: string }) {
  const filtered = useMemo(
    () => items.filter(i => i.name.includes(query)),
    [items, query]
  );
  return <ul>{filtered.map(i => <li key={i.id}>{i.name}</li>)}</ul>;
}
```

---

## TOPIC 3 — TypeScript Code Review Patterns

### 3.1 `any` Usage — When to Flag vs When to Accept

**Flag when:**
- `any` flows through business logic or multiple layers without validation
- `any` is used on a public function signature (API route, server action, exported utility)
- `any` is used as a lazy escape hatch with no `// TODO` or justification
- Return type is `any` on a function called by other modules

**Accept when:**
- Thin adapter wrapping a poorly-typed third-party library, with a proper type at the exit point
- Explicitly temporary scaffolding, marked `// TODO: type this after API is stable`
- Inside a type utility that intentionally operates on arbitrary shapes (e.g., a deep-clone helper)

**Review comment:** "This function accepts and returns `any` on a core business path. Any shape mismatch becomes a runtime error with no compile-time warning. Define a concrete type or use `unknown` with a type guard."

```ts
// BAD — any propagates through business logic unguarded
function processPayment(data: any): any {
  return data.amount * 1.1;
}

// BAD — any on exported function hides contract from consumers
export async function getUser(id: string): Promise<any> {
  return db.query(`SELECT * FROM users WHERE id = $1`, [id]);
}

// GOOD — concrete type, safe at compile time
type PaymentData = { amount: number; currency: string };
type PaymentResult = { total: number; currency: string };

function processPayment(data: PaymentData): PaymentResult {
  return { total: data.amount * 1.1, currency: data.currency };
}

// GOOD — typed return value
export async function getUser(id: string): Promise<User | null> {
  const row = await db.query(`SELECT * FROM users WHERE id = $1`, [id]);
  return row ?? null;
}

// ACCEPTABLE — adapter for badly-typed library, typed at exit
function adaptLegacyResponse(raw: any): AdaptedResponse {
  return AdaptedResponseSchema.parse(raw); // Zod validates at runtime
}
```

---

### 3.2 Type Assertions (`as SomeType`) — When to Flag as Dangerous

**Flag when:**
- `as ComplexType` is used on data from an external source (API response, `JSON.parse`, form input)
- Double assertion `as unknown as SomeType` is used to bypass TypeScript entirely
- The asserted type has required fields that the source may not have at runtime

**Safe uses:**
- `as const` for literal inference
- `as HTMLInputElement` after a null check when accessing DOM-specific properties
- Casting between compatible types within a controlled internal boundary

**Review comment:** "Casting the API response directly to `User` is unsafe. The runtime shape is not guaranteed to match. Use Zod to parse and validate — you'll get both runtime safety and a correctly-typed value."

```ts
// BAD — unchecked cast from external data
const user = await fetch('/api/user').then(r => r.json()) as User;
console.log(user.email.toUpperCase()); // runtime crash if email is undefined

// BAD — double assertion to silence compiler
const config = (window as any).__APP_CONFIG__ as AppConfig;

// GOOD — Zod validation, typed result, no assertion needed
import { z } from 'zod';
const UserSchema = z.object({
  id: z.string(),
  name: z.string(),
  email: z.string().email(),
});
type User = z.infer<typeof UserSchema>;

const raw = await fetch('/api/user').then(r => r.json());
const user = UserSchema.parse(raw); // throws on invalid shape, types correctly on success

// ACCEPTABLE — DOM assertion after null guard
const input = document.getElementById('search');
if (input instanceof HTMLInputElement) {
  console.log(input.value); // no assertion needed — instanceof is a type guard
}

// ACCEPTABLE — as const
const DIRECTION = 'north' as const; // type: "north", not string
```

---

### 3.3 Return Type Annotations on Server Actions and API Route Handlers

**Why critical:**
- Without explicit return types, refactoring a server action silently changes the client contract
- TypeScript infers return types from implementation — any change to internal logic silently changes the public type
- Discriminated union return types (`{ ok: true; data: T } | { ok: false; error: string }`) enable exhaustive handling on the client

**Review comment:** "This Server Action has no return type annotation. If the implementation changes, the client's inferred type will silently shift. Add an explicit `Promise<ActionResult>` return type with a discriminated union for success/error."

```ts
// BAD — inferred return type, no explicit contract
export async function createOrder(formData: FormData) {
  const data = Object.fromEntries(formData);
  // return type inferred as Promise<{ id: string } | undefined | Error>
  // if implementation changes, client breaks silently
  return await db.order.create({ data });
}

// BAD — API route with any return
export async function GET(req: Request): Promise<any> {
  return Response.json(await db.user.findMany());
}

// GOOD — explicit discriminated union return type on Server Action
type ActionResult<T> =
  | { ok: true; data: T }
  | { ok: false; error: string };

export async function createOrder(
  formData: FormData
): Promise<ActionResult<{ orderId: string }>> {
  const parsed = OrderSchema.safeParse(Object.fromEntries(formData));
  if (!parsed.success) {
    return { ok: false, error: parsed.error.message };
  }
  const order = await db.order.create({ data: parsed.data });
  return { ok: true, data: { orderId: order.id } };
}

// GOOD — typed API route handler
type UserListResponse = { users: User[] };

export async function GET(req: Request): Promise<Response> {
  const users = await db.user.findMany();
  return Response.json({ users } satisfies UserListResponse);
}
```

---

### 3.4 Zod Schema → TypeScript Type Alignment

**What to check in PRs:**
- Is the TypeScript type derived from the Zod schema via `z.infer`, or manually duplicated?
- Is the schema used for runtime validation at the boundary (HTTP request body, server action, external API response)?
- Are optional/nullable fields consistent between schema and DB/API spec?
- Does the schema validate before business logic runs, or after?

**Review comment:** "You've defined `type User` separately from `UserSchema`. These will drift. Replace the manual type with `type User = z.infer<typeof UserSchema>` — the schema becomes the single source of truth."

```ts
// BAD — manual type duplicates schema; they will drift
const UserSchema = z.object({
  id: z.string(),
  name: z.string(),
  email: z.string().email(),
});

type User = {  // duplicated, manual — will drift from schema
  id: string;
  name: string;
  email: string;
  role?: string; // schema doesn't have this — already drifted
};

// BAD — schema exists but validation skipped; cast used instead
export async function POST(req: Request) {
  const body = await req.json() as User; // assertion, no runtime validation
  await createUser(body);
  return Response.json({ ok: true });
}

// GOOD — single source of truth; infer type from schema
const UserSchema = z.object({
  id: z.string(),
  name: z.string(),
  email: z.string().email(),
  role: z.enum(['admin', 'member']).optional(),
});
type User = z.infer<typeof UserSchema>; // always in sync with schema

// GOOD — schema validates at boundary, type flows through
export async function POST(req: Request): Promise<Response> {
  const raw = await req.json();
  const result = UserSchema.safeParse(raw);
  if (!result.success) {
    return Response.json(
      { error: result.error.flatten() },
      { status: 400 }
    );
  }
  const user: User = result.data; // correctly typed after validation
  await createUser(user);
  return Response.json({ ok: true }, { status: 201 });
}
```

**PR checklist for Zod/TS alignment:**
- [ ] All TypeScript types derived from schemas via `z.infer` — no manual duplicates
- [ ] Schema validates at every trust boundary (HTTP body, query params, external API response)
- [ ] `safeParse` used for user-facing errors (not `parse` which throws uncaught)
- [ ] Optional/nullable fields match the actual API or DB column spec
- [ ] Schema and validation logic covered by unit tests with invalid inputs

---

## Quick Reference — PR Review Decision Tree

```
Incoming PR touches a webhook handler?
  -> 1.1 req.text() before req.json()?
  -> 1.2 timingSafeEqual used?
  -> 1.3 timestamp window validated?
  -> 1.4 webhook_events deduplication?
  -> 1.5 waitUntil for post-response work?

Incoming PR touches Next.js components?
  -> 2.1 use client only where hooks/events are used?
  -> 2.2 No window/localStorage/Date.now/Math.random in render?
  -> 2.3 Mutations invalidate TanStack Query cache in onSuccess?
  -> 2.4 Server data NOT stored in Zustand?
  -> 2.5 No useEffect for derived state?

Incoming PR touches TypeScript types?
  -> 3.1 No unexplained any on public/business-logic paths?
  -> 3.2 No as ComplexType on external data without Zod validation?
  -> 3.3 Server Actions and API routes have explicit return types?
  -> 3.4 TypeScript types derived from Zod schemas, not duplicated?
```
