# Validação Estratégica — Dev Web Senior
Data: 2026-04-13
Fontes consultadas:
- https://web.dev/articles/vitals (Google oficial, última atualização 2024-10-31)
- https://nextjs.org/docs/app/building-your-application/upgrading/version-15 (Next.js oficial, última atualização 2026-04-10, versão 16.2.3)
- https://nextjs.org/docs/app/api-reference/edge (Next.js oficial, 2026-04-10)
- https://vercel.com/docs/functions/runtimes/edge (Vercel oficial)
- https://supabase.com/docs/guides/api/rest/generating-types (Supabase oficial)
- https://docs.sentry.io/platforms/javascript/guides/nextjs/ (Sentry oficial)
- https://www.openstatus.dev/blog/monitoring-latency-vercel-edge-vs-serverless (benchmark independente, mar/2024)

---

## Status dos Frameworks

| Framework | Status | Fonte | Notas |
|-----------|--------|-------|-------|
| Edge cold start < 5ms | ATUALIZAR | openstatus.dev (mar/2024) + Vercel docs | O dado "< 5ms" do scan-estrategico está impreciso. O benchmark real: Edge cold start = **106ms P50** vs Serverless cold start = **859ms P50**. Edge é ~9x mais rápido no cold start, mas não é < 5ms. A vantagem é real e expressiva, porém o número absoluto precisa ser corrigido. |
| Core Web Vitals thresholds | VALIDADO | web.dev (Google, 2024-10-31) — métricas Stable | LCP ≤ 2.5s, INP ≤ 200ms, CLS ≤ 0.1 confirmados e estáveis. Medir no P75 de page loads. INP substituiu FID (já removido). |
| Supabase gen types | VALIDADO com adendo | supabase.com/docs (oficial) | Comando correto: `npx supabase gen types typescript --project-id "$PROJECT_REF" --schema public > database.types.ts`. CLI mínimo: v1.8.1. Adendo: desde supabase-js **v2.48.0**, JSON/JSONB fields têm inferência de tipo aprimorada. |
| Next.js 15 async APIs | VALIDADO — é breaking change | nextjs.org/docs (oficial, 2026-04-10) | `cookies()`, `headers()`, `draftMode()` e `params`/`searchParams` são agora **async** (await obrigatório). Codemod disponível: `npx @next/codemod@canary upgrade latest`. `fetch` não faz cache por padrão (era o oposto). `runtime: 'experimental-edge'` foi removido — usar `'edge'`. `NextRequest.geo` e `.ip` foram removidos — usar `@vercel/functions`. |
| Sentry Next.js | VALIDADO | docs.sentry.io (oficial) | Compatível com Next.js App Router (15+). Wizard: `npx @sentry/wizard@latest -i nextjs`. Cria automaticamente: `instrumentation-client.ts`, `sentry.server.config.ts`, `sentry.edge.config.ts`, `instrumentation.ts`, `app/global-error.tsx`. Nenhuma limitação reportada para Next.js 15. |

---

## Detalhamento por Framework

### 1. Edge vs Serverless — Benchmark Real (ATUALIZAR no scan-estrategico)

O scan-estrategico reportava "Edge cold start: < 5ms" — este dado está incorreto.

**Números reais validados (benchmark OpenStatus, março 2024, 6 regiões globais):**

| Métrica | Edge | Serverless Node.js |
|---------|------|-------------------|
| Cold start (P50) | **106ms** | **859ms** |
| Warm execution (P50) | **106ms** | **246ms** |
| Diferença cold start | — | 9x mais lento |
| Diferença warm | — | 2x mais lento |

**Aviso crítico da Vercel (2025/2026):** A própria Vercel recomenda **migrar de Edge para Node.js** para melhor performance e confiabilidade, agora que ambos rodam em Fluid Compute com Active CPU pricing. A vantagem de cold start do Edge ainda existe, mas Node.js com Fluid Compute reduziu o gap significativamente.

**O framework de decisão do scan-estrategico permanece válido**, mas o dado "< 5ms" precisa ser substituído por "~106ms P50" e a nota sobre migração para Node.js precisa ser incluída.

---

### 2. Core Web Vitals — VALIDADO (sem mudanças)

Thresholds confirmados pelo Google (estado Stable desde 2024-10-31):
- **LCP (Largest Contentful Paint):** ≤ 2.5s = Bom | > 4.0s = Ruim
- **INP (Interaction to Next Paint):** ≤ 200ms = Bom | > 500ms = Ruim
- **CLS (Cumulative Layout Shift):** ≤ 0.1 = Bom | > 0.25 = Ruim

Medir sempre no **P75** de page loads.

**Nota:** INP substituiu FID permanentemente. Se houver menção a FID em qualquer código ou doc, pode ser removida.

---

### 3. Supabase TypeScript Type Generation — VALIDADO com adendo

Comando confirmado e atual:
```bash
# Remoto (produção)
npx supabase gen types typescript --project-id "$PROJECT_REF" --schema public > src/types/database.types.ts

# Local (dev)
npx supabase gen types typescript --local > src/types/database.types.ts

# Self-hosted
npx supabase gen types typescript --db-url postgres://... --schema public > src/types/database.types.ts
```

**Novidade (supabase-js v2.48.0+):** Inferência de tipo aprimorada para JSON/JSONB columns. O workaround com `MergeDeep` da lib `type-fest` (mencionado no scan-estrategico) pode ser desnecessário para projetos novos em v2.48.0+.

---

### 4. Next.js 15 Async APIs — VALIDADO (breaking changes confirmados)

**Breaking changes críticos confirmados pela documentação oficial (versão 16.2.3, 2026-04-10):**

| API | Antes (sync) | Depois (async) |
|-----|-------------|----------------|
| `cookies()` | `const store = cookies()` | `const store = await cookies()` |
| `headers()` | `const h = headers()` | `const h = await headers()` |
| `draftMode()` | `const { isEnabled } = draftMode()` | `const { isEnabled } = await draftMode()` |
| `params` em layouts/pages | `const { slug } = params` | `const { slug } = await params` |
| `searchParams` em pages | `const { q } = searchParams` | `const { q } = await searchParams` |
| `params` em Route Handlers | `const params = segmentData.params` | `const params = await segmentData.params` |

**Outras mudanças relevantes:**
- `fetch` sem opção de cache = **não cacheia** por padrão (era o oposto no Next.js 14)
- `GET` em Route Handlers não cacheia por padrão — usar `export const dynamic = 'force-static'` para optar por cache
- `runtime: 'experimental-edge'` removido — usar `'edge'`
- `NextRequest.geo` e `NextRequest.ip` removidos — usar `geolocation()` e `ipAddress()` de `@vercel/functions`
- `@next/font` removido — usar `next/font` nativo

---

### 5. Sentry + Next.js 15 — VALIDADO

Integração oficial confirmada:
```bash
npx @sentry/wizard@latest -i nextjs
```

Arquivos criados automaticamente pelo wizard:
- `instrumentation-client.ts` — erros no browser
- `sentry.server.config.ts` — erros no Node.js server
- `sentry.edge.config.ts` — erros no Edge Runtime
- `instrumentation.ts` — registra configs de server e edge
- `next.config.ts` — wrapped com `withSentryConfig`
- `app/global-error.tsx` — captura erros de rendering React

**Sem issues conhecidos com Next.js 15 App Router.** SDK detecta automaticamente qual router está em uso.

---

## Novas Práticas Descobertas na Validação

### 1. Vercel recomenda migrar Edge → Node.js (2025/2026)
A documentação oficial da Vercel agora contém o aviso: *"We recommend migrating from edge to Node.js for improved performance and reliability."* Isso ocorreu porque Fluid Compute eliminou a maior vantagem do Edge (cold starts rápidos) para casos de uso com banco de dados. O scan-estrategico deve ser atualizado: Edge ainda é indicado para middleware (auth check, A/B, redirects), mas não como solução geral.

### 2. `NextRequest.geo` foi removido no Next.js 15
O padrão de geolocalização do scan-estrategico usa `req.geo?.country` — isso não funciona mais no Next.js 15. O correto é:
```typescript
import { geolocation } from '@vercel/functions'
const { city, country } = geolocation(request)
```

### 3. fetch caching invertido no Next.js 15
O scan-estrategico não menciona essa mudança. Qualquer `fetch()` sem opção explícita **não faz cache** no Next.js 15 (era o oposto no 14). Para o workflow de LP, isso afeta qualquer fetch em RSC que busque dados externos. Adicionar `{ cache: 'force-cache' }` onde cache for desejado.

### 4. Supabase type generation via MCP disponível
O Supabase MCP já instalado tem a ferramenta `generate_typescript_types` — o dev pode gerar tipos diretamente via Claude sem CLI local, o que simplifica o setup inicial.
