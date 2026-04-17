# Constraints da Plataforma — Dev Web Senior
Data: 2026-04-13
Fontes:
- https://vercel.com/docs/limits (Vercel oficial)
- https://vercel.com/docs/functions/runtimes/edge (Vercel oficial)
- https://uibakery.io/blog/supabase-pricing (compilação 2026)
- https://developers.cloudflare.com/workers/platform/limits/ (Cloudflare oficial)
- https://developers.cloudflare.com/kv/platform/limits/ (Cloudflare KV oficial)
- https://developers.cloudflare.com/d1/platform/limits/ (Cloudflare D1 oficial)
- https://nextjs.org/docs/app/api-reference/edge (Next.js oficial)

---

## Vercel

### Limites por Tier

| Constraint | Valor | Tier | Fonte |
|-----------|-------|------|-------|
| Bandwidth (Fast Data Transfer) | **100 GB/mês** | Hobby (Free) | vercel.com/docs/limits |
| Bandwidth | 1 TB/mês | Pro | vercel.com/docs/limits |
| Function Invocations (Serverless + Edge) | **1 milhão/mês** | Hobby | vercel.com/docs/limits |
| Build Execution | **6.000 min/mês** | Hobby | vercel.com/docs/limits |
| Deployments por dia | **100/dia** | Hobby | vercel.com/docs/limits |
| Deployments por hora | **100/hora** (rate limit) | Hobby | vercel.com/docs/limits |
| Concurrent Builds | **1** | Hobby | vercel.com/docs/limits |
| Concurrent Builds | 12 | Pro | vercel.com/docs/limits |
| Build time por deployment | **45 min** | Todos | vercel.com/docs/limits |
| Static File upload limit | **100 MB** | Hobby | vercel.com/docs/limits |
| Static File upload limit | 1 GB | Pro | vercel.com/docs/limits |
| Função Serverless — duração padrão | **10s** | Hobby | vercel.com/docs/limits |
| Função Serverless — duração máxima | **60s** | Hobby | vercel.com/docs/limits |
| Função Serverless — duração máxima | 300s (5 min) | Pro | vercel.com/docs/limits |
| Edge Function — bundle size máximo | **1 MB** (após gzip) | Hobby | vercel.com/docs/functions/runtimes/edge |
| Edge Function — bundle size máximo | 2 MB (após gzip) | Pro | vercel.com/docs/functions/runtimes/edge |
| Edge Function — duração máxima | **25s** para iniciar response | Todos | vercel.com/docs/functions/runtimes/edge |
| Edge Function — streaming máximo | 300s | Todos | vercel.com/docs/functions/runtimes/edge |
| Runtime Logs retidos | **1 hora** | Hobby | vercel.com/docs/limits |
| Runtime Logs retidos | 1 dia | Pro | vercel.com/docs/limits |
| Projects | 200 | Hobby | vercel.com/docs/limits |
| Git org repository connect | **Não permitido** | Hobby | vercel.com/docs/limits |
| Web Analytics Events | 100.000/mês | Hobby | vercel.com/docs/limits |
| Speed Insights Data Points | 10.000/mês | Hobby | vercel.com/docs/limits |

### Constraints mais críticos para o workflow da agência

1. **1 concurrent build no Hobby** — para agência com vários clientes em um único Vercel team, builds ficam na fila. Considerar Pro ($20/mês) a partir do 3º cliente ativo.
2. **100 deployments/dia no Hobby** — suficiente para desenvolvimento, mas facilmente atingível com preview por PR em projetos ativos.
3. **60s de função máxima no Hobby** — LPs simples não atingem esse limite, mas processamento de formulários pesados (ex: geração de PDF, envio de e-mail em batch) pode precisar Pro.
4. **1 MB bundle Edge** — para middleware simples (auth check, A/B, redirects), ok. Para lógica mais complexa, risco de estouro.
5. **Runtime Logs por apenas 1 hora no Hobby** — para debug de prod é insuficiente. Sentry compensa este gap.
6. **Hobby não conecta a repositórios de Git organizations** — agência precisa de repositórios pessoais ou Pro para orgs.

---

## Supabase

### Limites do Free Tier (2026)

| Constraint | Valor | Tier | Fonte |
|-----------|-------|------|-------|
| Database size | **500 MB** | Free | supabase.com/pricing |
| File Storage | **1 GB** | Free | supabase.com/pricing |
| Database Egress (bandwidth) | **5 GB/mês** | Free | supabase.com/pricing |
| Storage Egress (cached) | **5 GB/mês** | Free | supabase.com/pricing |
| Monthly Active Users (Auth) | **50.000 MAUs** | Free | supabase.com/pricing |
| Active Projects | **2 projetos** | Free | supabase.com/pricing |
| Inactivity Pausing | **Pausa após 1 semana** sem acesso | Free | supabase.com/pricing |
| Backups / PITR | **Nenhum** | Free | supabase.com/pricing |
| Edge Functions | Incluído (compute limitado) | Free | supabase.com/pricing |
| Realtime Connections | Básico (sem garantia de SLA) | Free | supabase.com/pricing |
| Support | Comunidade apenas | Free | supabase.com/pricing |
| Supabase CLI mínimo para gen types | **v1.8.1** | — | supabase.com/docs |
| supabase-js para JSON type inference | **v2.48.0+** | — | supabase.com/docs |

### Constraints mais críticos para o workflow da agência

1. **Pausa após 1 semana de inatividade (Free)** — crítico para LPs de clientes com baixo tráfego. O primeiro request após pausa tem cold start de ~5-10s visível para o usuário. Solução: Pro ($25/mês) por projeto, ou wake-up ping agendado.
2. **2 projetos no Free** — a agência com 3+ clientes ativos no mesmo Supabase org precisa de Pro ou projetos distribuídos em contas diferentes.
3. **500 MB de banco** — suficiente para LPs (dados de leads, formulários, análises simples). Risco apenas com uploads de imagens no banco (evitar — usar Supabase Storage ou R2).
4. **50.000 MAUs no Auth** — generoso para LPs de conversão. Problema apenas se a LP tiver área de membros/login recorrente com muitos usuários.
5. **Sem PITR (backups) no Free** — para clientes que pagam pela LP, recomendar Pro para ter backup diário.

---

## Cloudflare Workers

### Limites por Tier

| Constraint | Valor | Tier | Fonte |
|-----------|-------|------|-------|
| Requests | **100.000/dia** | Free | developers.cloudflare.com/workers/platform/limits |
| CPU time por request | **10ms** | Free | developers.cloudflare.com/workers/platform/limits |
| CPU time por request | 5 min (padrão 30s) | Paid | developers.cloudflare.com/workers/platform/limits |
| Memória por isolate | **128 MB** | Free + Paid | developers.cloudflare.com/workers/platform/limits |
| Worker bundle size (após gzip) | **3 MB** | Free | developers.cloudflare.com/workers/platform/limits |
| Worker bundle size (após gzip) | 10 MB | Paid | developers.cloudflare.com/workers/platform/limits |
| Subrequests por invocação | **50** | Free | developers.cloudflare.com/workers/platform/limits |
| Subrequests por invocação | 10.000 | Paid | developers.cloudflare.com/workers/platform/limits |
| Workers por conta | **100** | Free | developers.cloudflare.com/workers/platform/limits |
| Cron Triggers por conta | **5** | Free | developers.cloudflare.com/workers/platform/limits |
| KV Reads | **100.000/dia** | Free | developers.cloudflare.com/kv/platform/limits |
| KV Writes | **1.000/dia** (chaves diferentes) | Free | developers.cloudflare.com/kv/platform/limits |
| KV Storage | **1 GB por conta** | Free | developers.cloudflare.com/kv/platform/limits |
| KV Write para mesma chave | **1/segundo** | Free | developers.cloudflare.com/kv/platform/limits |
| D1 Databases | **10 databases** | Free | developers.cloudflare.com/d1/platform/limits |
| D1 Storage por database | **500 MB** | Free | developers.cloudflare.com/d1/platform/limits |
| D1 Storage total | **5 GB** | Free | developers.cloudflare.com/d1/platform/limits |
| D1 Queries por Worker invocation | **50** | Free | developers.cloudflare.com/d1/platform/limits |
| D1 Time Travel (PITR) | **7 dias** | Free | developers.cloudflare.com/d1/platform/limits |

### Constraints mais críticos para o workflow da agência

1. **10ms CPU no Free** — suficiente para lógica simples de routing, headers, auth token validation. Para qualquer processamento mais pesado (parsing, transformações), o Free travar. Usar Paid ($5/mês).
2. **100.000 requests/dia no Free** — para LPs de clientes locais (barbearia, salão), suficiente. Para campanhas de tráfego pago com alto volume, pode estourar.
3. **50 subrequests por invocação no Free** — se o Worker chama vários endpoints (Supabase + APIs externas), fácil atingir. Paid aumenta para 10.000.
4. **10ms CPU é a restrição mais severa** — o dado do scan-estrategico sobre Edge para A/B testing é válido para Vercel Edge Middleware (não tem esse limite), mas para Cloudflare Workers puros é necessário Paid.

---

## Next.js Edge Runtime

### O que NÃO funciona no Edge Runtime

| Constraint | Detalhes | Fonte |
|-----------|----------|-------|
| Filesystem access | `fs`, `path`, leitura/escrita de arquivos | nextjs.org/docs/app/api-reference/edge |
| Node.js APIs nativas | `net`, `crypto` nativo, `child_process`, `os`, `http` nativo | nextjs.org/docs/app/api-reference/edge |
| `require()` | Não permitido — usar apenas `import` (ES Modules) | nextjs.org/docs/app/api-reference/edge |
| `eval()` | Proibido por segurança | nextjs.org/docs/app/api-reference/edge |
| `new Function(string)` | Proibido — execução dinâmica de código | nextjs.org/docs/app/api-reference/edge |
| `WebAssembly.compile` | Proibido — compilação de Wasm em runtime | nextjs.org/docs/app/api-reference/edge |
| `WebAssembly.instantiate` com buffer | Proibido — somente via import estático | nextjs.org/docs/app/api-reference/edge |
| ISR (Incremental Static Regeneration) | **Não suportado** no Edge Runtime | nextjs.org/docs/app/api-reference/edge |
| Conexão direta com PostgreSQL | Sem suporte nativo — usar fetch para API | vercel.com/docs (recomendação arquitetural) |
| `node_modules` com APIs nativas | Quebra silenciosamente — depende da lib | nextjs.org/docs/app/api-reference/edge |
| `NextRequest.geo` e `.ip` | **Removidos no Next.js 15** — usar `@vercel/functions` | nextjs.org/docs/app/guides/upgrading/version-15 |

### Node.js módulos compatíveis com Edge Runtime

| Módulo | Suporte |
|--------|---------|
| `async_hooks` (AsyncLocalStorage) | Parcial (WinterCG subset) |
| `events` | Completo |
| `buffer` | Completo |
| `assert` | Completo |
| `util` (promisify, callbackify, types) | Parcial |
| `Buffer` (global) | Disponível |

### Bundle size limits (Edge Runtime)

| Plan | Limite (após gzip) |
|------|--------------------|
| Hobby | **1 MB** |
| Pro | **2 MB** |
| Enterprise | **4 MB** |

Inclui: código JS + bibliotecas importadas + arquivos (fontes, assets).

---

## Deprecations Relevantes

| O que mudou | Versão | Impacto | Ação |
|-------------|--------|---------|------|
| `NextRequest.geo` e `NextRequest.ip` removidos | Next.js 15 | CRÍTICO — A/B com geolocation quebra | Migrar para `geolocation()` e `ipAddress()` de `@vercel/functions` |
| `cookies()`, `headers()`, `draftMode()` agora async | Next.js 15 | CRÍTICO — quebra silenciosamente em prod | Adicionar `await` em todos os usos |
| `params` e `searchParams` agora async | Next.js 15 | CRÍTICO — afeta todos os layouts/pages | Adicionar `await` ou usar `use()` em client components |
| `fetch` não faz cache por padrão | Next.js 15 | ALTO — pode causar lentidão inesperada | Adicionar `{ cache: 'force-cache' }` onde necessário |
| `GET` em Route Handlers não cacheia por padrão | Next.js 15 | MÉDIO — afeta endpoints de leitura | Usar `export const dynamic = 'force-static'` para optar por cache |
| `runtime: 'experimental-edge'` removido | Next.js 15 | BAIXO — erro de build claro | Mudar para `'edge'` |
| `@next/font` removido | Next.js 15 | BAIXO — erro de import claro | Usar `next/font/google` nativo |
| `useFormState` depreciado | React 19 + Next.js 15 | MÉDIO — ainda funciona mas com warning | Migrar para `useActionState` |
| Auto instrumentation de Speed Insights removida | Next.js 15 | MÉDIO — métricas param de coletar | Instalar `@vercel/speed-insights` manualmente |
| `FID` (First Input Delay) removido do CWV | Plataforma Google 2024 | BAIXO — FID é histórico | Usar INP (já no scan-estrategico) |
| Edge Runtime recomendado → Node.js | Vercel 2025/2026 | MÉDIO — decisão arquitetural | Usar Edge apenas para middleware (auth, A/B, redirects) |
