# Senior Frontend Developer — Skill Reference

> Practical implementation guide. TypeScript/TSX throughout. No theory padding.

---

## Topic 1: Core Web Vitals — Next.js 15 App Router

### 1.1 LCP (Largest Contentful Paint)

**Root causes in App Router:**
- Hero/banner image loaded without `priority` (fetched after JS hydration)
- Font not preloaded — text renders late causing LCP to fire on text node
- Large uncompressed images served without responsive `sizes`

**Fix: Above-the-fold image with priority**

```tsx
// app/components/Hero.tsx
import Image from 'next/image'

export function Hero() {
  return (
    // fill mode requires a positioned parent
    <div style={{ position: 'relative', width: '100%', aspectRatio: '16/9' }}>
      <Image
        src="/hero.jpg"
        alt="Dashboard overview"
        fill
        priority              // injects <link rel="preload"> in <head>
        fetchPriority="high"  // HTTP priority hint
        sizes="(max-width: 768px) 100vw, 50vw"
        style={{ objectFit: 'cover' }}
      />
    </div>
  )
}
```

**Fix: Static image with known dimensions**

```tsx
<Image
  src="/product.jpg"
  width={1200}
  height={630}
  priority
  quality={85}
  sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw"
  alt="Product screenshot"
/>
```

**Rule:** Only the single above-the-fold image should carry `priority`. Every other image omits it to avoid competing preloads.

---

### 1.2 CLS (Cumulative Layout Shift)

**Root causes:**
- `<img>` without explicit `width`/`height` — browser reserves no space
- Font swap causing text reflow (`font-display: block` or missing swap)
- Dynamic content injected above existing content (banners, cookie bars)

**Fix: Always declare image dimensions**

```tsx
// Explicit dimensions — browser reserves space before load
<Image src="/avatar.png" width={64} height={64} alt="User avatar" />

// Dynamic-URL image with unknown dimensions — use fill + aspect ratio wrapper
<div style={{ position: 'relative', width: '100%', aspectRatio: '4/3' }}>
  <Image src={dynamicUrl} fill style={{ objectFit: 'cover' }} alt="" />
</div>

// Video — always include width/height
<video width="1280" height="720" poster="/poster.jpg" controls>
  <source src="/video.mp4" type="video/mp4" />
</video>
```

**Fix: CSS-only responsive layouts (avoid JS-driven shifts)**

```tsx
// Show/hide with CSS, not conditional rendering that causes reflow
export function ResponsiveNav() {
  return (
    <>
      <nav className="md:hidden"><MobileNav /></nav>
      <nav className="hidden md:block"><DesktopNav /></nav>
    </>
  )
}
```

---

### 1.3 INP (Interaction to Next Paint) — replaces FID

**Root causes:**
- Long synchronous tasks on the main thread during user interaction
- Expensive state updates blocking the browser paint cycle
- Over-use of React Context (every consumer re-renders on value change)

**Fix: `useTransition` for non-urgent updates**

```tsx
'use client'
import { useState, useTransition } from 'react'

export function SearchResults() {
  const [query, setQuery] = useState('')
  const [results, setResults] = useState<Item[]>([])
  const [isPending, startTransition] = useTransition()

  function handleSearch(value: string) {
    setQuery(value)                  // urgent: update input immediately
    startTransition(() => {          // non-urgent: heavy filter deferred
      setResults(expensiveFilter(value))
    })
  }

  return (
    <div>
      <input value={query} onChange={e => handleSearch(e.target.value)} />
      {isPending && <span aria-live="polite">Filtering...</span>}
      <ul>{results.map(r => <li key={r.id}>{r.name}</li>)}</ul>
    </div>
  )
}
```

**Fix: `useDeferredValue` for rendering-heavy lists**

```tsx
'use client'
import { useDeferredValue } from 'react'

export function ProductList({ items }: { items: Product[] }) {
  const deferred = useDeferredValue(items)
  const isStale = deferred !== items

  return (
    <ul style={{ opacity: isStale ? 0.5 : 1 }}>
      {deferred.map(item => <li key={item.id}>{item.name}</li>)}
    </ul>
  )
}
```

**Fix: Break long tasks with scheduler yield**

```ts
async function processChunked(data: Item[]): Promise<Result[]> {
  const results: Result[] = []
  const CHUNK = 50

  for (let i = 0; i < data.length; i += CHUNK) {
    results.push(...data.slice(i, i + CHUNK).map(heavyCalc))
    await new Promise(resolve => setTimeout(resolve, 0)) // yield to browser
  }
  return results
}
```

---

### 1.4 Bundle Size — Dynamic Imports & Tree Shaking

**Fix: `next/dynamic` for below-the-fold / client-only components**

```tsx
import dynamic from 'next/dynamic'

// Heavy chart — lazy, with skeleton fallback
const Chart = dynamic(() => import('@/components/Chart'), {
  loading: () => <div className="h-64 animate-pulse bg-muted rounded" />,
  ssr: false,  // disable SSR for client-only libs (e.g. canvas-based)
})

// Modal — only load when triggered
const SettingsModal = dynamic(() => import('@/components/SettingsModal'))

export function Dashboard() {
  return (
    <>
      <Chart />
      <SettingsModal />
    </>
  )
}
```

**Fix: Named exports for tree shaking**

```ts
// lib/utils.ts — named exports; bundler drops unused ones
export function formatCurrency(n: number) { ... }
export function formatDate(d: Date) { ... }

// ✓ Only formatCurrency ends up in the bundle
import { formatCurrency } from '@/lib/utils'
```

**Fix: Bundle analyzer**

```bash
npm install @next/bundle-analyzer
```

```js
// next.config.js
const withBundleAnalyzer = require('@next/bundle-analyzer')({
  enabled: process.env.ANALYZE === 'true',
})
module.exports = withBundleAnalyzer({})
```

```bash
ANALYZE=true next build
```

**Fix: Third-party scripts — defer non-critical**

```tsx
import Script from 'next/script'

// In root layout
<Script src="https://www.googletagmanager.com/gtag/js?id=GA_ID" strategy="lazyOnload" />
<Script id="ga-init" strategy="lazyOnload">{`
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_ID');
`}</Script>
```

Strategies: `beforeInteractive` (critical only) | `afterInteractive` (default) | `lazyOnload` (analytics/chat) | `worker` (experimental, off main thread).

---

### 1.5 `next/image` — sizes, priority, fill mode

| Scenario | Pattern |
|---|---|
| LCP hero, known dimensions | `width` + `height` + `priority` + `sizes` |
| LCP hero, fluid container | `fill` + positioned parent + `priority` + `sizes` |
| Below-fold product grid | `width` + `height` + `sizes` (no priority) |
| Avatar / icon | `width` + `height`, omit `sizes` |
| CMS-driven unknown dimensions | `fill` + aspect-ratio wrapper |

**The `sizes` prop is critical for avoiding oversized images on mobile:**

```tsx
// Tells the browser what CSS width the image will occupy at each breakpoint
// Next.js uses this to serve the right srcset candidate
<Image
  src="/banner.jpg"
  width={1200}
  height={400}
  sizes="(max-width: 640px) 100vw, (max-width: 1024px) 75vw, 50vw"
  alt="Banner"
/>
```

Omitting `sizes` defaults to `100vw` — the browser fetches the full-size image on every viewport.

---

### 1.6 Font Optimization — `next/font` with Variable Fonts

**Variable Google font — recommended pattern**

```tsx
// app/fonts.ts  (single shared module — prevents duplicate instances)
import { Inter, Roboto_Mono } from 'next/font/google'

// Variable font: no weight array needed
export const inter = Inter({
  subsets: ['latin'],
  display: 'swap',
  variable: '--font-inter',         // exposes CSS custom property
  adjustFontFallback: true,         // auto-generates metric-matched fallback -> zero CLS
})

export const roboto_mono = Roboto_Mono({
  subsets: ['latin'],
  display: 'swap',
  variable: '--font-roboto-mono',
})
```

```tsx
// app/layout.tsx
import { inter, roboto_mono } from './fonts'

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" className={`${inter.variable} ${roboto_mono.variable} antialiased`}>
      <body>{children}</body>
    </html>
  )
}
```

```css
/* app/globals.css — Tailwind v4 */
@import 'tailwindcss';

@theme inline {
  --font-sans: var(--font-inter);
  --font-mono: var(--font-roboto-mono);
}
```

```js
// tailwind.config.js — Tailwind v3
module.exports = {
  theme: {
    extend: {
      fontFamily: {
        sans: ['var(--font-inter)'],
        mono: ['var(--font-roboto-mono)'],
      },
    },
  },
}
```

**Variable font with extra axes (e.g. slant)**

```tsx
import { Inter } from 'next/font/google'

const inter = Inter({
  subsets: ['latin'],
  axes: ['slnt'],       // enables slant axis in addition to wght
  display: 'swap',
})
```

**Local variable font**

```tsx
import localFont from 'next/font/local'

const brandFont = localFont({
  src: './BrandFont-Variable.woff2',
  display: 'swap',
  variable: '--font-brand',
  fallback: ['system-ui', 'sans-serif'],
  adjustFontFallback: 'Arial',
})
```

**Local non-variable font (multiple weights)**

```tsx
const roboto = localFont({
  src: [
    { path: './Roboto-Regular.woff2',    weight: '400', style: 'normal' },
    { path: './Roboto-Italic.woff2',     weight: '400', style: 'italic' },
    { path: './Roboto-Bold.woff2',       weight: '700', style: 'normal' },
    { path: './Roboto-BoldItalic.woff2', weight: '700', style: 'italic' },
  ],
  display: 'swap',
})
```

**Key behaviors:**
- Fonts are downloaded at build time and self-hosted — zero Google DNS lookup at runtime
- `adjustFontFallback: true` generates a `@font-face` fallback with CSS `size-adjust`/`ascent-override` tuned to match the web font metrics — eliminates CLS from font swap
- `display: 'optional'` is stricter: if font doesn't load within the first render, it is not shown at all (no swap) — best for decorative fonts where stability matters more than brand

---

## Topic 2: shadcn/ui DataTable with TanStack Table v8

### 2.1 Installation

```bash
pnpm dlx shadcn@latest add table checkbox button input dropdown-menu
pnpm add @tanstack/react-table
pnpm add @tanstack/react-query  # for server-side pattern
```

### 2.2 Column Definitions

```tsx
// features/payments/columns.tsx
'use client'

import { ColumnDef } from '@tanstack/react-table'
import { Checkbox } from '@/components/ui/checkbox'
import { Button } from '@/components/ui/button'
import { ArrowUpDown } from 'lucide-react'

export type Payment = {
  id: string
  amount: number
  status: 'pending' | 'processing' | 'success' | 'failed'
  email: string
}

export const columns: ColumnDef<Payment>[] = [
  // Row selection column
  {
    id: 'select',
    header: ({ table }) => (
      <Checkbox
        checked={
          table.getIsAllPageRowsSelected() ||
          (table.getIsSomePageRowsSelected() && 'indeterminate')
        }
        onCheckedChange={v => table.toggleAllPageRowsSelected(!!v)}
        aria-label="Select all"
      />
    ),
    cell: ({ row }) => (
      <Checkbox
        checked={row.getIsSelected()}
        onCheckedChange={v => row.toggleSelected(!!v)}
        aria-label="Select row"
      />
    ),
    enableSorting: false,
    enableHiding: false,
  },
  // Sortable column
  {
    accessorKey: 'email',
    header: ({ column }) => (
      <Button
        variant="ghost"
        onClick={() => column.toggleSorting(column.getIsSorted() === 'asc')}
      >
        Email
        <ArrowUpDown className="ml-2 h-4 w-4" />
      </Button>
    ),
  },
  {
    accessorKey: 'status',
    header: 'Status',
  },
  {
    accessorKey: 'amount',
    header: () => <div className="text-right">Amount</div>,
    cell: ({ row }) => {
      const formatted = new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD',
      }).format(row.getValue<number>('amount'))
      return <div className="text-right font-medium">{formatted}</div>
    },
  },
]
```

### 2.3 Core DataTable Component (client-side sort/filter/paginate)

```tsx
// components/data-table.tsx
'use client'

import * as React from 'react'
import {
  ColumnDef,
  ColumnFiltersState,
  SortingState,
  VisibilityState,
  flexRender,
  getCoreRowModel,
  getFilteredRowModel,
  getPaginationRowModel,
  getSortedRowModel,
  useReactTable,
} from '@tanstack/react-table'
import {
  Table, TableBody, TableCell,
  TableHead, TableHeader, TableRow,
} from '@/components/ui/table'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import {
  DropdownMenu, DropdownMenuCheckboxItem,
  DropdownMenuContent, DropdownMenuTrigger,
} from '@/components/ui/dropdown-menu'

interface DataTableProps<TData, TValue> {
  columns: ColumnDef<TData, TValue>[]
  data: TData[]
}

export function DataTable<TData, TValue>({
  columns,
  data,
}: DataTableProps<TData, TValue>) {
  const [sorting, setSorting]               = React.useState<SortingState>([])
  const [columnFilters, setColumnFilters]   = React.useState<ColumnFiltersState>([])
  const [columnVisibility, setColumnVisibility] = React.useState<VisibilityState>({})
  const [rowSelection, setRowSelection]     = React.useState({})

  const table = useReactTable({
    data,
    columns,
    getCoreRowModel:        getCoreRowModel(),
    getPaginationRowModel:  getPaginationRowModel(),
    getSortedRowModel:      getSortedRowModel(),
    getFilteredRowModel:    getFilteredRowModel(),
    onSortingChange:        setSorting,
    onColumnFiltersChange:  setColumnFilters,
    onColumnVisibilityChange: setColumnVisibility,
    onRowSelectionChange:   setRowSelection,
    state: { sorting, columnFilters, columnVisibility, rowSelection },
  })

  const selectedCount = table.getFilteredSelectedRowModel().rows.length

  return (
    <div className="space-y-4">
      {/* Toolbar */}
      <div className="flex items-center gap-2">
        <Input
          placeholder="Filter by email..."
          value={(table.getColumn('email')?.getFilterValue() as string) ?? ''}
          onChange={e => table.getColumn('email')?.setFilterValue(e.target.value)}
          className="max-w-sm"
        />

        {/* Column visibility */}
        <DropdownMenu>
          <DropdownMenuTrigger asChild>
            <Button variant="outline" className="ml-auto">Columns</Button>
          </DropdownMenuTrigger>
          <DropdownMenuContent align="end">
            {table.getAllColumns()
              .filter(col => col.getCanHide())
              .map(col => (
                <DropdownMenuCheckboxItem
                  key={col.id}
                  className="capitalize"
                  checked={col.getIsVisible()}
                  onCheckedChange={v => col.toggleVisibility(!!v)}
                >
                  {col.id}
                </DropdownMenuCheckboxItem>
              ))}
          </DropdownMenuContent>
        </DropdownMenu>
      </div>

      {/* Bulk action bar — only visible when rows selected */}
      {selectedCount > 0 && (
        <div className="flex items-center gap-2 rounded-md border bg-muted px-4 py-2">
          <span className="text-sm text-muted-foreground">
            {selectedCount} row(s) selected
          </span>
          <Button
            variant="destructive"
            size="sm"
            onClick={() => {
              const ids = table
                .getFilteredSelectedRowModel()
                .rows.map(r => (r.original as Payment).id)
              // call your delete mutation here
              console.log('delete', ids)
              table.resetRowSelection()
            }}
          >
            Delete selected
          </Button>
        </div>
      )}

      {/* Table */}
      <div className="overflow-hidden rounded-md border">
        <Table>
          <TableHeader>
            {table.getHeaderGroups().map(hg => (
              <TableRow key={hg.id}>
                {hg.headers.map(header => (
                  <TableHead key={header.id}>
                    {header.isPlaceholder
                      ? null
                      : flexRender(header.column.columnDef.header, header.getContext())}
                  </TableHead>
                ))}
              </TableRow>
            ))}
          </TableHeader>
          <TableBody>
            {table.getRowModel().rows.length ? (
              table.getRowModel().rows.map(row => (
                <TableRow key={row.id} data-state={row.getIsSelected() && 'selected'}>
                  {row.getVisibleCells().map(cell => (
                    <TableCell key={cell.id}>
                      {flexRender(cell.column.columnDef.cell, cell.getContext())}
                    </TableCell>
                  ))}
                </TableRow>
              ))
            ) : (
              <TableRow>
                <TableCell colSpan={columns.length} className="h-24 text-center">
                  No results.
                </TableCell>
              </TableRow>
            )}
          </TableBody>
        </Table>
      </div>

      {/* Pagination */}
      <div className="flex items-center justify-between">
        <span className="text-sm text-muted-foreground">
          Page {table.getState().pagination.pageIndex + 1} of {table.getPageCount()}
        </span>
        <div className="flex gap-2">
          <Button variant="outline" size="sm" onClick={() => table.previousPage()} disabled={!table.getCanPreviousPage()}>
            Previous
          </Button>
          <Button variant="outline" size="sm" onClick={() => table.nextPage()} disabled={!table.getCanNextPage()}>
            Next
          </Button>
        </div>
      </div>
    </div>
  )
}
```

---

### 2.4 Server-Side Sorting, Filtering, Pagination

**Decision rule:**
- Less than ~1 000 rows with fast response: client-side (simpler, instant UX)
- Large datasets, expensive queries, or URL-shareable state: server-side

**Server-side setup with `manualPagination: true`**

```tsx
// components/data-table-server.tsx
'use client'

import { useReactTable, getCoreRowModel, ColumnDef, SortingState, PaginationState, ColumnFiltersState } from '@tanstack/react-table'
import { useState, useMemo } from 'react'
import { useQuery } from '@tanstack/react-query'
import { useRouter, useSearchParams, usePathname } from 'next/navigation'
import { startTransition } from 'react'

interface ServerDataTableProps<TData, TValue> {
  columns: ColumnDef<TData, TValue>[]
  fetchData: (params: { page: number; pageSize: number; sort: SortingState; filters: ColumnFiltersState }) => Promise<{ rows: TData[]; total: number }>
}

export function ServerDataTable<TData, TValue>({ columns, fetchData }: ServerDataTableProps<TData, TValue>) {
  const router     = useRouter()
  const pathname   = usePathname()
  const sp         = useSearchParams()

  const [sorting, setSorting]             = useState<SortingState>([])
  const [columnFilters, setColumnFilters] = useState<ColumnFiltersState>([])
  const [pagination, setPagination]       = useState<PaginationState>({
    pageIndex: Number(sp.get('page') ?? 0),
    pageSize:  Number(sp.get('size') ?? 10),
  })

  // Auto-refetch whenever sort/filter/page changes
  const { data, isFetching } = useQuery({
    queryKey: ['table-data', pagination, sorting, columnFilters],
    queryFn:  () => fetchData({ page: pagination.pageIndex, pageSize: pagination.pageSize, sort: sorting, filters: columnFilters }),
    placeholderData: prev => prev,  // keep stale data visible during refetch
  })

  // Sync state to URL search params
  function updateUrl(page: number, size: number) {
    const params = new URLSearchParams(sp.toString())
    params.set('page', String(page))
    params.set('size', String(size))
    startTransition(() => { router.replace(`${pathname}?${params}`) })
  }

  const memoColumns = useMemo(() => columns, [columns])

  const table = useReactTable({
    data:          data?.rows ?? [],
    columns:       memoColumns,
    rowCount:      data?.total ?? 0,   // TanStack calculates pageCount from this
    getCoreRowModel: getCoreRowModel(),
    manualPagination: true,
    manualSorting:    true,
    manualFiltering:  true,
    state:    { pagination, sorting, columnFilters },
    onPaginationChange: updater => {
      const next = typeof updater === 'function' ? updater(pagination) : updater
      setPagination(next)
      updateUrl(next.pageIndex, next.pageSize)
    },
    onSortingChange:      setSorting,
    onColumnFiltersChange: newFilters => {
      setColumnFilters(newFilters)
      setPagination(p => ({ ...p, pageIndex: 0 }))  // reset to page 1 on filter
    },
  })

  return (
    <div style={{ opacity: isFetching ? 0.7 : 1, transition: 'opacity 150ms' }}>
      {/* reuse same Table/toolbar rendering as client-side component */}
    </div>
  )
}
```

**Key flags:**
- `manualPagination: true` — table does not slice data itself; assumes `data` is already the current page
- `manualSorting: true` — table does not sort locally; you pass sorted data from the server
- `rowCount` — lets TanStack derive `pageCount` without you computing it

---

### 2.5 Column Visibility Toggle

Already included in the full `DataTable` component above. The pattern:

```tsx
table.getAllColumns()
  .filter(col => col.getCanHide())  // respects enableHiding: false on columns
  .map(col => (
    <DropdownMenuCheckboxItem
      checked={col.getIsVisible()}
      onCheckedChange={v => col.toggleVisibility(!!v)}
    >
      {col.id}
    </DropdownMenuCheckboxItem>
  ))
```

To hide a column by default on mount:

```tsx
const [columnVisibility, setColumnVisibility] = useState<VisibilityState>({
  id: false,      // hidden by default
  createdAt: false,
})
```

---

### 2.6 Row Selection + Bulk Actions

The selection column and bulk action bar are in section 2.3. Key points:

- `table.getFilteredSelectedRowModel().rows` — selected rows matching current filter
- `table.toggleAllPageRowsSelected(!!v)` — select/deselect current page
- `table.resetRowSelection()` — clear after bulk action completes
- For "select all pages" (not just current page), track a separate `selectAll` boolean and send it to your API

---

### 2.7 TanStack Query Integration Summary

```tsx
// The queryKey must include all server-side state so refetches fire automatically
const { data, isFetching, isError } = useQuery({
  queryKey: ['payments', { page: pagination.pageIndex, pageSize: pagination.pageSize, sorting, columnFilters }],
  queryFn: () => api.getPayments({ ... }),
  placeholderData: keepPreviousData,  // v5 alias for the old keepPreviousData option
  staleTime: 30_000,  // 30s cache before background refetch
})
```

Changing any key element (filter, sort, page) triggers an automatic refetch. No `useEffect` required.

---

## Topic 3: Accessibility (a11y) for Internal Dashboards

### 3.1 Skip Navigation Link

Put this as the very first element in the `<body>`. It is visually hidden but visible on focus.

```tsx
// app/layout.tsx
export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        {/* Skip link — visible only on keyboard focus */}
        <a
          href="#main-content"
          className="sr-only focus:not-sr-only focus:fixed focus:left-4 focus:top-4 focus:z-50 focus:rounded focus:bg-background focus:px-4 focus:py-2 focus:text-foreground focus:shadow-md"
        >
          Skip to main content
        </a>

        <SidebarNav />

        <main id="main-content" tabIndex={-1}>
          {children}
        </main>
      </body>
    </html>
  )
}
```

`tabIndex={-1}` on `<main>` allows it to receive programmatic focus without appearing in the tab order.

---

### 3.2 Focus Management After Route Changes (App Router)

Next.js App Router does not reset focus on navigation. Build a `FocusManager` client component and place it in the root layout.

```tsx
// components/focus-manager.tsx
'use client'

import { useEffect, useRef } from 'react'
import { usePathname } from 'next/navigation'

export function FocusManager() {
  const mainRef  = useRef<HTMLElement | null>(null)
  const pathname = usePathname()

  useEffect(() => {
    // Point at the same <main id="main-content"> used by the skip link
    mainRef.current = document.getElementById('main-content')
    mainRef.current?.focus()
  }, [pathname])

  return null
}
```

```tsx
// Pair with a route announcer for screen readers
'use client'

import { usePathname } from 'next/navigation'
import { useEffect, useState } from 'react'

export function RouteAnnouncer() {
  const pathname = usePathname()
  const [message, setMessage] = useState('')

  useEffect(() => {
    // Use the document title if set, otherwise fall back to the path
    const title = document.title || `Page: ${pathname}`
    setMessage(title)
  }, [pathname])

  return (
    <div
      role="status"
      aria-live="polite"
      aria-atomic="true"
      className="sr-only"
    >
      {message}
    </div>
  )
}
```

```tsx
// app/layout.tsx — add both
import { FocusManager } from '@/components/focus-manager'
import { RouteAnnouncer } from '@/components/route-announcer'

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        <FocusManager />
        <RouteAnnouncer />
        {/* ... rest of layout */}
      </body>
    </html>
  )
}
```

**Note:** As of 2025 Next.js tracks this as an open issue (#49386). The pattern above is the established community workaround. Next.js does emit a built-in `RouteAnnouncer` for the Pages Router; App Router does not yet have the equivalent baked in.

---

### 3.3 `aria-live` Regions for Async Data Updates

```tsx
// components/async-status.tsx
'use client'

interface AsyncStatusProps {
  isLoading: boolean
  isError:   boolean
  count?:    number
}

export function AsyncStatus({ isLoading, isError, count }: AsyncStatusProps) {
  return (
    <>
      {/* polite: waits for user to be idle before reading */}
      <div aria-live="polite" aria-atomic="true" className="sr-only">
        {isLoading && 'Loading data, please wait.'}
        {!isLoading && !isError && count !== undefined && `${count} results loaded.`}
      </div>

      {/* assertive: interrupts immediately — for errors only */}
      <div role="alert" aria-live="assertive" aria-atomic="true" className="sr-only">
        {isError && 'Error loading data. Please try again.'}
      </div>
    </>
  )
}
```

**Rules:**
- `aria-live="polite"` for loading states and success messages
- `role="alert"` (implicit `aria-live="assertive"`) for errors — interrupts the screen reader immediately
- `aria-atomic="true"` ensures the full region content is read, not just the changed portion
- Keep live regions in the DOM at all times — toggling them in/out can suppress announcements in some screen readers

---

### 3.4 Keyboard Navigation for Data Tables

**ARIA roles for a navigable grid:**

```tsx
// Use role="grid" for interactive tables (sortable, selectable)
// Use role="table" for read-only display tables

<table role="grid" aria-label="Payments" aria-rowcount={totalRows}>
  <thead>
    <tr role="row">
      <th role="columnheader" aria-sort="ascending" scope="col">
        <button onClick={toggleSort}>Email</button>
      </th>
      <th role="columnheader" aria-sort="none" scope="col">Status</th>
      <th role="columnheader" aria-sort="none" scope="col">Amount</th>
    </tr>
  </thead>
  <tbody>
    {rows.map((row, ri) => (
      <tr role="row" key={row.id} aria-rowindex={ri + 2}>
        <td role="gridcell">{row.email}</td>
        <td role="gridcell">{row.status}</td>
        <td role="gridcell">{row.amount}</td>
      </tr>
    ))}
  </tbody>
</table>
```

**`aria-sort` values:** `ascending` | `descending` | `none` | `other`

**WAI-ARIA Grid keyboard contract:**

| Key | Behavior |
|---|---|
| `Tab` | Move focus into the grid; subsequent Tab moves past the grid |
| Arrow keys | Move focus one cell in the direction pressed |
| `Home` / `End` | First / last cell in current row |
| `Ctrl+Home` / `Ctrl+End` | First / last cell in the grid |
| `Space` | Toggle row selection (with `aria-selected`) |
| `Shift+Space` | Select the entire row |
| `Ctrl+A` | Select all cells |
| `Enter` / `F2` | Enter cell edit mode |
| `Escape` | Exit edit mode, restore grid navigation |

**Implementation note:** shadcn/ui's `<Table>` renders a real `<table>` element. TanStack Table is purely headless — it does not add ARIA roles. You must add `role`, `aria-sort`, and `aria-selected` attributes yourself, or use a wrapper that does it.

**Keyboard-accessible sort button pattern:**

```tsx
// In your column header renderer
header: ({ column }) => {
  const sorted = column.getIsSorted()
  return (
    <button
      onClick={() => column.toggleSorting(sorted === 'asc')}
      aria-label={`Sort by email ${sorted === 'asc' ? 'descending' : 'ascending'}`}
      className="flex items-center gap-1"
    >
      Email
      {sorted === 'asc' && <span aria-hidden="true">↑</span>}
      {sorted === 'desc' && <span aria-hidden="true">↓</span>}
    </button>
  )
}
```

---

### 3.5 Color Contrast — WCAG AA Requirements

| Text type | Minimum ratio |
|---|---|
| Normal text (< 18pt / < 14pt bold) | 4.5 : 1 |
| Large text (>= 18pt or >= 14pt bold) | 3 : 1 |
| UI components and graphical objects | 3 : 1 |
| Placeholder text | 4.5 : 1 (treat as normal text) |
| Disabled elements | No requirement (but aim for 3:1) |

**Practical shadcn/ui notes:**
- The default shadcn/ui theme passes AA in light mode; always verify after customizing brand colors
- `text-muted-foreground` (HSL 215 16% 47%) on white background is approximately 4.6:1 — just passes AA
- Badge and status chip text colors are common failure points — check with a contrast checker before shipping
- Use `prefers-color-scheme` dark mode tokens — light-mode-passing colors often fail in dark mode

**Tooling:**
```bash
# axe-core for dev-time violations
pnpm add -D @axe-core/react

# In _app or layout — dev only
if (typeof window !== 'undefined' && process.env.NODE_ENV !== 'production') {
  import('@axe-core/react').then(({ default: axe }) => {
    axe(React, ReactDOM, 1000)
  })
}
```

---

### 3.6 Focus Trap in Modals (shadcn/ui handles this)

shadcn/ui Dialog, Sheet, and Popover are built on Radix UI primitives, which include:
- Focus trap (Tab cycles within the open dialog)
- Focus restoration on close (returns focus to the trigger element)
- Escape key dismissal
- `aria-modal="true"` and `role="dialog"`

Do not reimplement these from scratch. If building a custom modal:

```tsx
'use client'

import { useRef, useEffect } from 'react'

function Modal({ isOpen, onClose, children }: { isOpen: boolean; onClose: () => void; children: React.ReactNode }) {
  const closeRef = useRef<HTMLButtonElement>(null)

  useEffect(() => {
    if (isOpen) closeRef.current?.focus()  // move focus in on open
  }, [isOpen])

  return (
    <div role="dialog" aria-modal="true" aria-labelledby="modal-title">
      <h2 id="modal-title">Dialog title</h2>
      <button ref={closeRef} onClick={onClose}>Close</button>
      {children}
    </div>
  )
}
```

Always return focus to the element that triggered the modal on close — shadcn/ui does this automatically.

---

### 3.7 Reduced Motion

```css
/* globals.css */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

Or in Tailwind with `motion-safe:` / `motion-reduce:` variants:

```tsx
<div className="transition-opacity duration-300 motion-reduce:transition-none">
  {content}
</div>
```

---

## Quick Reference Checklist

### Core Web Vitals
- [ ] LCP image has `priority` and meaningful `sizes` prop
- [ ] All images have `width`/`height` or fill-with-aspect-ratio wrapper
- [ ] `next/font` used for all fonts — no `<link>` to Google Fonts
- [ ] `display: 'swap'` + `adjustFontFallback: true` on every font
- [ ] Heavy components lazy-loaded with `next/dynamic`
- [ ] Third-party scripts use `strategy="lazyOnload"`
- [ ] `startTransition` wraps expensive filter/sort state updates

### DataTable
- [ ] Columns defined with `ColumnDef<T>[]` — fully typed
- [ ] Server-side: `manualPagination/Sorting/Filtering: true` + `rowCount`
- [ ] TanStack Query `queryKey` includes all table state
- [ ] `placeholderData: keepPreviousData` to avoid flash during page change
- [ ] Bulk action bar conditionally rendered on `rowSelection` state

### Accessibility
- [ ] Skip nav link as first body element targeting `#main-content`
- [ ] `FocusManager` + `RouteAnnouncer` in root layout
- [ ] `aria-live="polite"` for loading/success, `role="alert"` for errors
- [ ] Sortable table headers have `aria-sort` attribute
- [ ] All interactive elements reachable and operable by keyboard
- [ ] Color contrast 4.5:1 for normal text verified after theming
- [ ] `prefers-reduced-motion` respected in animations
