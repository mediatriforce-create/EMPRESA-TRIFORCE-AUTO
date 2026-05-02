# Code Review Checklist: Next.js 15 + Supabase + Drizzle ORM

> Internal senior reviewer reference. Focus: security, correctness, type safety.
> Stack: Next.js 15 App Router, Supabase (Supavisor pooler), Drizzle ORM v0.30+.

---

## TOPIC 1 — Server Action Security (Next.js 15)

### 1.1 The core rule: Server Actions are public HTTP endpoints

The App Router expiles each `'use server'` function as a POST endpoint reachable directly via `fetch`. Middleware runs on route navigation — it does NOT protect direct action calls. Every action must authenticate and authorize itself.

---

### 1.2 Authentication inside Server Actions

**BAD — trusting client state or relying only on middleware:**

```ts
// actions/delete-post.ts
'use server'

// No session check. Caller passes userId from the client.
export async function deletePost(postId: string, userId: string) {
  await db.delete(posts).where(eq(posts.id, postId))
}
```

Problems:
- Any unauthenticated caller can hit this endpoint directly with any `postId`.
- `userId` comes from the client and cannot be trusted.

**GOOD — explicit session verification at the top of every action:**

```ts
// actions/delete-post.ts
'use server'

import { verifySession } from '@/lib/dal' // Data Access Layer

export async function deletePost(postId: string) {
  // 1. Verify session — never skip this
  const session = await verifySession()
  if (!session) return { error: 'Unauthorized' }

  // 2. Verify ownership before mutation
  const post = await db.query.posts.findFirst({
    where: eq(posts.id, postId),
    columns: { userId: true },
  })

  if (!post || post.userId !== session.userId) {
    return { error: 'Forbidden' }
  }

  await db.delete(posts).where(eq(posts.id, postId))
  return { success: true }
}
```

**`verifySession` pattern (DAL — Data Access Layer):**

```ts
// lib/dal.ts
import { cookies } from 'next/headers'
import { decrypt } from '@/lib/session' // your JWT/session lib
import { cache } from 'react'

// cache() deduplicates calls within a single request
export const verifySession = cache(async () => {
  const cookie = (await cookies()).get('session')?.value
  const session = await decrypt(cookie)
  if (!session?.userId) return null
  return session
})
```

> Next.js docs use exactly this pattern (`verifySession` + `cache()`). The `cache()` wrapper avoids redundant DB/crypto calls when multiple actions run in the same request.

---

### 1.3 Authorization (RBAC) inside Server Actions

**BAD — checking only authentication, not authorization:**

```ts
'use server'

export async function publishPost(postId: string) {
  const session = await verifySession()
  if (!session) return { error: 'Unauthorized' }

  // BUG: any authenticated user can publish any post
  await db.update(posts).set({ published: true }).where(eq(posts.id, postId))
}
```

**GOOD — role + ownership check:**

```ts
'use server'

// Permissions map — keep in a central lib
const PERMISSIONS = {
  post: {
    publish: ['editor', 'admin'],
    delete: ['admin'],
  },
} as const

type Resource = keyof typeof PERMISSIONS
type Operation<R extends Resource> = keyof (typeof PERMISSIONS)[R]

function can<R extends Resource>(
  role: string,
  resource: R,
  operation: Operation<R>
): boolean {
  const allowed = PERMISSIONS[resource][operation] as readonly string[]
  return allowed.includes(role)
}

export async function publishPost(postId: string) {
  const session = await verifySession()
  if (!session) return { error: 'Unauthorized' }

  // RBAC check
  if (!can(session.role, 'post', 'publish')) {
    return { error: 'Forbidden' }
  }

  // Ownership check (belt-and-suspenders when RLS is not in play)
  const post = await db.query.posts.findFirst({
    where: eq(posts.id, postId),
    columns: { userId: true },
  })
  if (!post || post.userId !== session.userId) {
    return { error: 'Forbidden' }
  }

  await db.update(posts).set({ published: true }).where(eq(posts.id, postId))
  return { success: true }
}
```

---

### 1.4 Common patterns where auth is forgotten

| Pattern | Risk |
|---|---|
| Actions called from forms — devs assume the page guard is enough | Direct POST bypass |
| Revalidation/mutation helpers extracted into `lib/` and marked `'use server'` | Treated as internal but still exposed |
| Actions inside route handlers (`route.ts`) that proxy to Server Actions | Double exposure |
| Returning raw DB objects instead of DTOs | Leaks columns (e.g., `passwordHash`) |
| `try/catch` that swallows auth errors and returns `{}` | Silent auth failure |

**BAD — leaking internal error details:**

```ts
} catch (e) {
  return { error: (e as Error).message } // reveals DB schema, policy names
}
```

**GOOD — generic client messages, detailed server logs:**

```ts
} catch (e) {
  console.error('[deletePost]', e) // server log
  return { error: 'Something went wrong' } // generic client message
}
```

---

### 1.5 next-safe-action: does it handle auth automatically?

**No. It does not automatically verify authentication.** It provides a middleware pipeline where YOU add auth enforcement. Without an auth middleware, actions run for any caller.

**How it actually works:**

```ts
// lib/safe-action.ts
import { createSafeActionClient } from 'next-safe-action'
import { verifySession } from '@/lib/dal'

// Base client — no auth, for public actions only
export const actionClient = createSafeActionClient()

// Auth client — enforces session in middleware
export const authActionClient = createSafeActionClient().use(async ({ next }) => {
  const session = await verifySession()

  if (!session) {
    throw new Error('Unauthorized') // short-circuits the action
  }

  // Inject session into context for the action handler
  return next({ ctx: { session } })
})
```

**Using the auth client in an action:**

```ts
// actions/update-profile.ts
'use server'

import { z } from 'zod'
import { authActionClient } from '@/lib/safe-action'

const schema = z.object({ name: z.string().min(1).max(100) })

export const updateProfile = authActionClient
  .schema(schema)
  .action(async ({ parsedInput, ctx }) => {
    // ctx.session is guaranteed to exist — middleware enforced it
    const { session } = ctx

    await db
      .update(users)
      .set({ name: parsedInput.name })
      .where(eq(users.id, session.userId))

    return { success: true }
  })
```

> Review rule: any `createSafeActionClient()` without a `.use(authMiddleware)` chain is a **public** action. Confirm this is intentional.

---

## TOPIC 2 — Supabase RLS Review Patterns

### 2.1 Verifying RLS is actually effective

RLS enabled but no policies = **default-deny** (nothing accessible). RLS disabled = all rows accessible to anyone with DB credentials. Both misconfiguration states look "working" until you test edge cases.

**Review checklist:**

```sql
-- 1. Is RLS enabled on the table?
SELECT tablename, rowsecurity
FROM pg_tables
WHERE schemaname = 'public';

-- 2. Are there policies defined?
SELECT tablename, policyname, cmd, roles, qual
FROM pg_policies
WHERE schemaname = 'public'
ORDER BY tablename;

-- 3. Test as an unauthenticated user
SET LOCAL role = anon;
SELECT * FROM posts; -- should return 0 rows if policy requires auth

-- 4. Test as a different authenticated user
SET LOCAL role = authenticated;
SET LOCAL request.jwt.claims TO '{"sub":"other-user-id"}';
SELECT * FROM posts WHERE user_id = 'target-user-id'; -- should return 0 rows
```

**Common misconfiguration: policy exists but has no `USING` clause:**

```sql
-- BAD: policy defined but effectively does nothing
CREATE POLICY "allow_all" ON posts FOR SELECT
  TO authenticated
  USING (true); -- every authenticated user sees every row
```

```sql
-- GOOD: restrict to owner
CREATE POLICY "posts_select_owner" ON posts FOR SELECT
  TO authenticated
  USING (auth.uid() = user_id);
```

---

### 2.2 Common RLS bypass patterns to look for in code review

**BYPASS 1 — Using the service role key on the client:**

```ts
// BAD: service role in browser or client-side code — bypasses ALL RLS
const supabase = createClient(
  process.env.NEXT_PUBLIC_SUPABASE_URL!,
  process.env.SUPABASE_SERVICE_ROLE_KEY! // NEVER expose this to the client
)
```

```ts
// GOOD: service role only in server-side code with no client exposure
// Server Action or Route Handler only:
const adminClient = createClient(
  process.env.NEXT_PUBLIC_SUPABASE_URL!,
  process.env.SUPABASE_SERVICE_ROLE_KEY!
)
// Only use for admin operations that explicitly need to bypass RLS (e.g., webhooks)
```

**BYPASS 2 — Trusting client-provided owner IDs:**

```ts
// BAD: accepting ownership claim from client
export async function getMyPosts(userId: string) { // userId from client = untrusted
  return db.select().from(posts).where(eq(posts.userId, userId))
}
```

```ts
// GOOD: derive ownership from verified session
export async function getMyPosts() {
  const session = await verifySession()
  if (!session) return []
  return db.select().from(posts).where(eq(posts.userId, session.userId))
}
```

**BYPASS 3 — App-level filter instead of relying on RLS:**

```ts
// BAD: fetching all rows then filtering in memory — RLS never applied
const allPosts = await supabase.from('posts').select('*')
const myPosts = allPosts.data?.filter(p => p.user_id === session.userId)
```

```ts
// GOOD: let RLS filter at the DB level
const { data } = await supabase.from('posts').select('id, title, created_at')
// RLS policy ensures only the authenticated user's rows are returned
```

**BYPASS 4 — Views without `security_invoker`:**

```sql
-- BAD: view without security_invoker uses the definer's context, not the caller's
CREATE VIEW public_posts AS SELECT * FROM posts;

-- GOOD: force view to use the calling user's RLS context
CREATE VIEW public_posts WITH (security_invoker = true) AS
  SELECT id, title, published_at FROM posts;
```

---

### 2.3 `enableRLS()` vs `withRLS()` vs `crudPolicy()` in Drizzle ORM

| Function | Layer | What it does |
|---|---|---|
| `pgTable(...).enableRLS()` | Schema declaration | Emits `ALTER TABLE ... ENABLE ROW LEVEL SECURITY` in migrations |
| `crudPolicy()` | Schema declaration | Declarative helper to define SELECT/INSERT/UPDATE/DELETE policies alongside the table |
| `withRLS()` | Query execution | Wraps a query to ensure it runs under the RLS-enforced connection context |

**BAD — enabling RLS without defining any policies:**

```ts
// schema.ts
export const posts = pgTable('posts', {
  id: serial('id').primaryKey(),
  userId: uuid('user_id').notNull(),
  title: text('title').notNull(),
}).enableRLS() // RLS on, but NO policies = default-deny = nothing works
```

**GOOD — enabling RLS with explicit policies:**

```ts
// schema.ts
import { pgTable, serial, uuid, text } from 'drizzle-orm/pg-core'
import { crudPolicy, authenticatedRole, authUid } from 'drizzle-orm/neon'
// For plain Supabase (no Neon), use pgPolicy + sql tag instead

export const posts = pgTable(
  'posts',
  {
    id: serial('id').primaryKey(),
    userId: uuid('user_id').notNull(),
    title: text('title').notNull(),
    published: boolean('published').notNull().default(false),
  },
  (table) => [
    // Owner can read/write their own posts
    crudPolicy({
      role: authenticatedRole,
      read: authUid(table.userId),
      modify: authUid(table.userId),
    }),
  ]
)
```

**Plain Supabase alternative using `pgPolicy` + SQL:**

```ts
import { pgTable, pgPolicy, serial, uuid, text, boolean } from 'drizzle-orm/pg-core'
import { sql } from 'drizzle-orm'

export const posts = pgTable('posts', {
  id: serial('id').primaryKey(),
  userId: uuid('user_id').notNull(),
  title: text('title').notNull(),
})

// Separate policy declarations
export const postsSelectPolicy = pgPolicy('posts_select', {
  on: posts,
  for: 'select',
  to: 'authenticated',
  using: sql`auth.uid() = user_id`,
})

export const postsInsertPolicy = pgPolicy('posts_insert', {
  on: posts,
  for: 'insert',
  to: 'authenticated',
  withCheck: sql`auth.uid() = user_id`,
})
```

---

### 2.4 App-level auth check: redundant vs required alongside RLS

| Scenario | App-level check needed? | Why |
|---|---|---|
| Supabase client with anon key, user JWT in session | Not strictly required — RLS handles it | RLS policies use `auth.uid()` from the JWT |
| Service role client in a Server Action | **Required** — RLS bypassed | Service role ignores all policies |
| Drizzle connecting directly via connection string | **Required** — RLS not active unless JWT context is set | Drizzle uses a raw Postgres connection; `auth.uid()` is not set |
| Complex business rules (cross-table, multi-step) | **Required** | SQL policies cannot express all business logic |
| Early UX feedback (show error before DB hit) | Recommended | Avoids unnecessary DB round-trip |

**Critical: Drizzle + Supabase requires explicit JWT context injection for RLS to work:**

```ts
// BAD: Drizzle with a plain connection string — RLS auth.uid() will be NULL
const db = drizzle(pool)
const posts = await db.select().from(postsTable) // RLS USING(auth.uid() = user_id) = FALSE
```

```ts
// GOOD: set JWT claims in the DB session before querying
async function withSupabaseAuth<T>(
  session: Session,
  fn: (db: DrizzleDB) => Promise<T>
): Promise<T> {
  return db.transaction(async (tx) => {
    // Set the Supabase auth context for this transaction
    await tx.execute(sql`
      SELECT set_config('request.jwt.claims', ${JSON.stringify({
        sub: session.userId,
        role: 'authenticated',
      })}, true)
    `)
    await tx.execute(sql`SET LOCAL role = authenticated`)
    return fn(tx)
  })
}

// Usage in Server Action
const result = await withSupabaseAuth(session, (tx) =>
  tx.select().from(postsTable)
)
```

---

## TOPIC 3 — Drizzle ORM Security and Quality Patterns

### 3.1 Column selection: risks of SELECT *

**BAD — selecting all columns:**

```ts
// Returns passwordHash, stripeCustomerId, internalNotes, etc.
const user = await db.select().from(users).where(eq(users.id, userId))
return user // leaks sensitive columns to the client
```

**GOOD — explicit column projection:**

```ts
// Define a safe DTO shape
const PUBLIC_USER_FIELDS = {
  id: users.id,
  email: users.email,
  name: users.name,
  avatarUrl: users.avatarUrl,
  createdAt: users.createdAt,
  // passwordHash, stripeCustomerId OMITTED
} as const

const user = await db
  .select(PUBLIC_USER_FIELDS)
  .from(users)
  .where(eq(users.id, userId))

// TypeScript infers the exact return type — no sensitive fields possible
```

**GOOD — using `omit` pattern for relations:**

```ts
// If you need most columns but want to exclude a few:
const { passwordHash, stripeCustomerId, ...safeColumns } = getTableColumns(users)

const user = await db
  .select(safeColumns)
  .from(users)
  .where(eq(users.id, userId))
```

> Review rule: any `db.select()` without a column argument is a red flag. Require explicit column projection on tables with PII or credentials.

---

### 3.2 TypeScript errors to look for in Drizzle queries

**Issue 1 — Return type mismatch with explicit interface:**

```ts
// BAD: interface doesn't match actual query shape
interface Post { id: number; title: string; authorName: string }

const posts: Post[] = await db.select().from(postsTable)
// TS error: Property 'authorName' does not exist on type...
// OR silently wrong if types are cast with 'as'
```

```ts
// GOOD: derive type from the query itself
const postsQuery = db.select({ id: postsTable.id, title: postsTable.title }).from(postsTable)
type Post = Awaited<ReturnType<typeof postsQuery.execute>>[number]
// Post = { id: number; title: string } — always in sync
```

**Issue 2 — Using `as` to force-cast query results:**

```ts
// BAD: bypasses TS safety, hides schema drift
const result = await db.select().from(users) as { id: string; role: 'admin' | 'user' }[]
```

```ts
// GOOD: query returns typed result, validate with Zod if crossing a boundary
const UserSchema = z.object({ id: z.string().uuid(), role: z.enum(['admin', 'user']) })
const raw = await db.select({ id: users.id, role: users.role }).from(users)
const result = raw.map(row => UserSchema.parse(row))
```

**Issue 3 — Nullable join columns treated as non-null:**

```ts
// BAD: LEFT JOIN makes joined columns nullable, but code accesses them directly
const result = await db
  .select({ postTitle: posts.title, authorName: users.name }) // users.name is string | null after LEFT JOIN
  .from(posts)
  .leftJoin(users, eq(posts.userId, users.id))

result.forEach(r => r.authorName.toUpperCase()) // Runtime crash: Cannot read .toUpperCase of null
```

```ts
// GOOD: handle nullable join result
result.forEach(r => (r.authorName ?? 'Anonymous').toUpperCase())
```

---

### 3.3 `prepare: false` with Supabase pooler (port 6543)

**Context:** Supabase uses Supavisor as its connection pooler. Port `6543` operates in **Transaction Mode** — each transaction may use a different underlying Postgres connection. Prepared statements are session-scoped in Postgres; they don't survive connection switches.

**What breaks without `prepare: false`:**

```
Error: prepared statement "drizzle_s1" does not exist
-- or --
Error: prepared statement "drizzle_s1" already exists
```

This happens because:
1. Drizzle (via `postgres.js` or `pg`) creates a named prepared statement on connection A.
2. Supavisor routes the next request to connection B.
3. Connection B has no knowledge of the prepared statement created on A.

**BAD — default config with Supabase pooler:**

```ts
// db.ts
import { drizzle } from 'drizzle-orm/postgres-js'
import postgres from 'postgres'

const client = postgres(process.env.DATABASE_URL!) // pooler URL (port 6543)
// postgres.js uses prepared statements by default — will crash under Transaction Mode
export const db = drizzle(client)
```

**GOOD — disable prepared statements for pooler connection:**

```ts
// db.ts
import { drizzle } from 'drizzle-orm/postgres-js'
import postgres from 'postgres'

const isPooer = process.env.DATABASE_URL!.includes(':6543')

const client = postgres(process.env.DATABASE_URL!, {
  prepare: false, // Required for Supavisor Transaction Mode (port 6543)
  max: 1,         // Serverless: keep pool size low
})

export const db = drizzle(client, { schema })
```

**With `node-postgres` (`pg`):**

```ts
import { drizzle } from 'drizzle-orm/node-postgres'
import { Pool } from 'pg'

const pool = new Pool({
  connectionString: process.env.DATABASE_URL, // port 6543 pooler URL
  // pg does not have a `prepare: false` option at pool level;
  // use parameterized queries (never string interpolation) and
  // avoid explicit PREPARE statements in raw SQL
})

export const db = drizzle(pool, { schema })
```

> Review rule: if `DATABASE_URL` targets port `6543`, confirm `prepare: false` is set on the `postgres.js` client. Port `5432` direct connections and Session Mode pooler support prepared statements and don't need this.

**Bonus: two connection strings pattern (Next.js + Supabase):**

```ts
// Direct connection (port 5432) — for migrations and Drizzle Kit
const migrationClient = postgres(process.env.DATABASE_URL_DIRECT!, { max: 1 })

// Pooler (port 6543) — for application queries
const queryClient = postgres(process.env.DATABASE_URL!, { prepare: false })

export const db = drizzle(queryClient, { schema })
```

---

### 3.4 Common `.where()` mistakes causing incorrect filtering

**Mistake 1 — String interpolation in raw SQL (injection risk):**

```ts
// BAD: SQL injection vector
const userId = req.body.userId
const result = await db.execute(sql`SELECT * FROM posts WHERE user_id = '${userId}'`)
// If userId = "' OR '1'='1", this returns all rows
```

```ts
// GOOD: parameterized with Drizzle operators
const result = await db.select().from(posts).where(eq(posts.userId, userId))
// Drizzle generates: SELECT ... WHERE user_id = $1 — safe
```

**Mistake 2 — Dynamic filters that silently drop conditions:**

```ts
// BAD: optional filter that evaluates to `where(undefined)` — no filter applied
const status = searchParams.get('status') // could be null

const result = await db
  .select()
  .from(posts)
  .where(eq(posts.status, status)) // If status is null: WHERE status = NULL (matches nothing OR ignored depending on driver)
```

```ts
// GOOD: guard optional conditions
import { and, eq, isNull, isNotNull } from 'drizzle-orm'

const conditions = []

if (status !== null) {
  conditions.push(eq(posts.status, status))
}

const result = await db
  .select()
  .from(posts)
  .where(conditions.length > 0 ? and(...conditions) : undefined)
```

**Mistake 3 — Multiple `.where()` calls not combining as expected:**

```ts
// BAD: developers assume multiple .where() calls are OR'd or AND'd
const result = await db
  .select()
  .from(posts)
  .where(eq(posts.userId, userId))
  .where(eq(posts.published, true)) // Overwrites the first .where() — only second applies!
```

```ts
// GOOD: combine conditions explicitly with and()
import { and } from 'drizzle-orm'

const result = await db
  .select()
  .from(posts)
  .where(and(
    eq(posts.userId, userId),
    eq(posts.published, true)
  ))
```

**Mistake 4 — Forgetting null handling in nullable columns:**

```ts
// BAD: eq(col, null) does NOT generate IS NULL — generates WHERE col = NULL (always false)
const result = await db.select().from(posts).where(eq(posts.deletedAt, null))
// Returns 0 rows — this is a silent correctness bug
```

```ts
// GOOD: use isNull() / isNotNull() for nullable columns
import { isNull, isNotNull } from 'drizzle-orm'

const activePosts = await db.select().from(posts).where(isNull(posts.deletedAt))
const archivedPosts = await db.select().from(posts).where(isNotNull(posts.deletedAt))
```

**Mistake 5 — OR condition built incorrectly:**

```ts
// BAD: two separate .where() calls intended as OR
const result = await db
  .select()
  .from(posts)
  .where(eq(posts.status, 'draft'))
  .where(eq(posts.status, 'published')) // Overwrites — only 'published' applies
```

```ts
// GOOD: explicit or()
import { or } from 'drizzle-orm'

const result = await db
  .select()
  .from(posts)
  .where(or(
    eq(posts.status, 'draft'),
    eq(posts.status, 'published')
  ))
// Equivalent: WHERE status IN ('draft', 'published')
// Even cleaner:
  .where(inArray(posts.status, ['draft', 'published']))
```

---

## Quick Review Checklist

### Server Actions
- [ ] Every action calls `verifySession()` (or equivalent) as first line
- [ ] No action trusts `userId` or ownership data from client input
- [ ] RBAC check present for write/delete operations
- [ ] No `select()` without column projection on sensitive tables
- [ ] Error responses use generic messages (no schema/policy leaks)
- [ ] `next-safe-action` clients: confirm auth middleware is attached to protected action clients

### Supabase RLS
- [ ] `pg_policies` has entries for every table with user data (SELECT, INSERT, UPDATE, DELETE)
- [ ] No service role key in `NEXT_PUBLIC_` env vars or client-side code
- [ ] Views use `security_invoker = true` if they expose RLS-protected tables
- [ ] Drizzle queries that must respect RLS inject JWT context (`set_config`) before querying
- [ ] Tests cover: owner access, non-owner access, unauthenticated access

### Drizzle ORM
- [ ] No bare `db.select()` on tables with sensitive columns (use explicit projection)
- [ ] `DATABASE_URL` on port `6543` + `prepare: false` on `postgres.js` client
- [ ] No `eq(col, null)` — use `isNull()` / `isNotNull()`
- [ ] No chained `.where()` calls — use `and()` / `or()` to combine
- [ ] Dynamic filter arrays use `and(...conditions)` pattern
- [ ] No `as SomeType[]` casts on query results — derive type from query shape
