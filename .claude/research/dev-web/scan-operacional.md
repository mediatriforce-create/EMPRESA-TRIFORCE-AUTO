# Scan Operacional — Dev Web Senior
Data: 2026-04-13

---

## Skills encontradas com avaliação

### Fonte: officialskills.sh (Vercel Labs / OpenAI / Cloudflare / outros)
Total encontradas no índice awesome-agent-skills: 30+
Filtradas para o contexto Triforce Auto: **13 skills aprovadas**

| # | Skill | Mantenedor | URL | Antigravity | Relevância |
|---|-------|------------|-----|-------------|-----------|
| 1 | react-best-practices | vercel-labs | https://officialskills.sh/vercel-labs/skills/react-best-practices | N/D | ALTA — 64 regras React/Next.js App Router |
| 2 | next-best-practices | vercel-labs | https://officialskills.sh/vercel-labs/skills/next-best-practices | N/D | ALTA — File conventions, RSC, async Next.js 15+ |
| 3 | next-cache-components | vercel-labs | https://officialskills.sh/vercel-labs/skills/next-cache-components | N/D | ALTA — PPR, use cache directive, ISR patterns |
| 4 | web-design-guidelines | vercel-labs | https://officialskills.sh/vercel-labs/skills/web-design-guidelines | N/D | MEDIA — Audit de acessibilidade e UX anti-patterns |
| 5 | frontend-skill | openai | https://officialskills.sh/openai/skills/frontend-skill | N/D | ALTA — LP com hero imagery, hierarquia visual, motion |
| 6 | vercel-deploy | openai | https://officialskills.sh/openai/skills/vercel-deploy | N/D | ALTA — Deploy automático, preview URLs, fallback API |
| 7 | web-perf | cloudflare | https://officialskills.sh/cloudflare/skills/web-perf | N/D | ALTA — Audit Core Web Vitals, LCP, CLS, render-blocking |
| 8 | wrangler | cloudflare | https://officialskills.sh/cloudflare/skills/wrangler | N/D | MEDIA — Workers/KV/R2/D1 via CLI (não é core do produto) |
| 9 | seo-aeo-best-practices | sanity-io | https://officialskills.sh/sanity-io/skills/seo-aeo-best-practices | N/D | ALTA — SEO + AEO para LPs: meta tags, JSON-LD, OG |
| 10 | github (workflow) | callstackincubator | https://officialskills.sh/callstackincubator/skills/github | N/D | ALTA — PR workflow, stacked PRs, squash merge, gh CLI |
| 11 | yeet | openai | https://officialskills.sh/openai/skills/yeet | N/D | MEDIA — Stage→commit→push→PR em um comando |
| 12 | gh-fix-ci | openai | https://officialskills.sh/openai/skills/gh-fix-ci | N/D | MEDIA — Debug GitHub Actions failures via gh CLI |
| 13 | cloudflare-worker-base | jezweb/antigravity | https://antigravity.codes/agent-skills/backend/cloudflare-worker-base | SIM | MEDIA — Workers + Hono + Vite, evita 10 erros documentados |

**Nota antigravity:** gh não estava disponível no ambiente. Skills verificadas via WebFetch direto nos URLs de antigravity.codes.

### Skills encontradas mas DESCARTADAS

| Skill | Motivo do descarte |
|-------|-------------------|
| zustand-store-ts (microsoft) | State management complexo — não é padrão da stack |
| react-flow-node-ts (microsoft) | Diagramas de flow — fora do escopo LP |
| netlify-* (todas) | Empresa usa Vercel, não Netlify |
| cloudflare-agents-sdk | Para AI agents/Durable Objects — fora do produto |
| cloudflare-mcp-server (antigravity) | Para construir servidores MCP — fora do escopo |
| senior-fullstack (alirezarezvani) | Genérico demais, inclui Django/MERN/Docker/K8s |
| fullstack-developer (404kidwiz) | Genérico, inclui Vue/Go/Kubernetes — não alinhado |
| neondatabase/neon-postgres | Empresa usa Supabase, não Neon |
| azure-postgres-ts (microsoft) | Empresa usa Supabase, não Azure |
| app-builder / agentscale | LP builders genéricos sem contexto de qualidade |
| awwwards-design | Foco em animações award-winning — overkill para nicho |
| anti-slop-design | Interessante mas redundante com frontend-skill |
| openai/playwright | Testing — não é prioridade no Stage 2 |
| anthropics/webapp-testing | Idem |

---

## Plano de extração por skill

### 1. react-best-practices (vercel-labs) — INSTALAR
**Extrair:**
- Regras contra data fetching waterfalls em Server Components
- Bundle size: barrel files → direct imports
- Patterns de Suspense boundaries para streaming
- Re-render prevention patterns
- Comparativo SWR vs React.cache() vs LRU cache
- Before/after examples com App Router

**Descartar:** Regras para SPAs client-only sem SSR

**Instalar com:**
```bash
npx skills add https://github.com/vercel-labs/react-best-practices --skill react-best-practices
```

---

### 2. next-best-practices (vercel-labs) — INSTALAR
**Extrair:**
- File conventions e estrutura de projeto Next.js
- RSC (React Server Components) boundaries corretos
- Async API do Next.js 15+ (params, cookies)
- Image/font optimization
- Metadata e OG image generation
- Route handlers pattern
- Hydration error prevention
- Code splitting e bundling

**Descartar:** Upgrade guides para versões antigas (next-upgrade skill separado)

**Instalar com:**
```bash
npx skills add https://github.com/vercel-labs/next-best-practices --skill next-best-practices
```

---

### 3. next-cache-components (vercel-labs) — INSTALAR
**Extrair:**
- `use cache` directive (Next.js 16/PPR)
- Partial Prerendering para LPs com partes dinâmicas
- Tag-based invalidation para dados de clientes
- Session management + cache estável
- Migration de unstable_cache

**Descartar:** Casos de uso SaaS complexo com múltiplos tenants

**Instalar com:**
```bash
npx skills add https://github.com/vercel-labs/next-cache-components --skill next-cache-components
```

---

### 4. frontend-skill (openai) — INSTALAR
**Extrair:**
- Full-bleed hero como âncora visual da LP
- Brand-first hierarchy (nome da marca > lista de features)
- Cardless layout — substituir card grids por composição
- Scroll-linked motion e hover effects
- Combate ao padrão SaaS genérico que Claude tende a gerar

**Descartar:** Game UI prototyping, dashboard redesign enterprise

**Instalar com:**
```bash
npx skills add https://github.com/openai/frontend-skill --skill frontend-skill
```

---

### 5. vercel-deploy (openai) — INSTALAR
**Extrair:**
- CLI auth handling automático
- Framework detection (40+ frameworks)
- Preview por padrão → URL para cliente revisar antes de produção
- Fallback via API quando CLI indisponível
- Deploy de subdirectories
- Build timeout handling

**Descartar:** Deploy de static sites genéricos (foco em Next.js)

**Instalar com:**
```bash
npx skills add https://github.com/openai/vercel-deploy --skill vercel-deploy
```

---

### 6. web-perf (cloudflare) — INSTALAR
**Extrair:**
- Audit Core Web Vitals via Chrome DevTools MCP: FCP, LCP, TBT, CLS, Speed Index
- Render-blocking resources: identificar CSS/JS bloqueantes
- Missing image dimensions → CLS fix
- Bundle analysis: unused code, oversized polyfills
- Cache headers e compression de assets
- Audit de acessibilidade incluso no mesmo pass

**Descartar:** Diagnósticos para apps Vite puros (foco em Next.js/LP)

**Instalar com:**
```bash
npx skills add https://github.com/cloudflare/web-perf --skill web-perf
```

---

### 7. seo-aeo-best-practices (sanity-io) — INSTALAR
**Extrair:**
- Meta tags e Open Graph para LPs de conversão
- JSON-LD: Article, FAQ, LocalBusiness schemas (barbearia, salão, personal)
- Sitemaps e robots.txt
- EEAT para credibilidade de infoprodutores/coaches
- AI crawler directives (ChatGPT/Perplexity indexing)
- FAQ schema para Google AI Overviews

**Descartar:** Hreflang multilingual (empresa opera em PT-BR only)

**Instalar com:**
```bash
npx skills add https://github.com/sanity-io/seo-aeo-best-practices --skill seo-aeo-best-practices
```

---

### 8. github workflow (callstackincubator) — INSTALAR
**Extrair:**
- PR creation pattern com formatação consistente via gh CLI
- Stacked PRs para feature branches dependentes
- Squash merge sequencial
- Monitorar CI/PR status sem sair do terminal
- Update de base branches

**Descartar:** Workflows enterprise com múltiplos times

**Instalar com:**
```bash
npx skills add https://github.com/callstackincubator/github --skill github
```

---

### 9. gh-fix-ci (openai) — INSTALAR (baixa prioridade)
**Extrair:**
- Fetch de logs do GitHub Actions via gh CLI
- Diagnóstico de falhas de lint/test em PRs
- Recuperação de snippets exatos sem abrir browser

**Descartar:** Integração com CI providers externos (Buildkite, CircleCI)

**Instalar com:**
```bash
npx skills add https://github.com/openai/gh-fix-ci --skill gh-fix-ci
```

---

### 10. web-design-guidelines (vercel-labs) — INSTALAR (complemento)
**Extrair:**
- Audit de acessibilidade em componentes TSX
- Detecção de UX anti-patterns em LPs
- Pre-merge compliance check

**Descartar:** Guidelines genéricas sem contexto de LP

**Instalar com:**
```bash
npx skills add https://github.com/vercel-labs/web-design-guidelines --skill web-design-guidelines
```

---

## Ferramentas identificadas (MCPs e integrações)

### MCPs OFICIAIS — Alta prioridade

#### 1. Vercel MCP (OFICIAL)
- **URL:** `https://mcp.vercel.com`
- **O que faz:** Gerencia projetos, deployments, logs, busca docs Vercel — diretamente do Claude Code
- **Tipo:** Remote MCP com OAuth
- **Acesso:** Read + Write (gerencia deployments reais — exige confirmação humana)
- **Segurança:** OAuth com proteção contra confused deputy attacks
- **Gap cobre:** Deploy/gerenciamento Vercel, debug de build failures, log inspection
- **Instalar no Claude Code:**
  ```bash
  claude mcp add --transport http vercel https://mcp.vercel.com
  # Depois: /mcp para autenticar
  ```

#### 2. Cloudflare Developer Platform MCP (JA INSTALADO)
- **Status:** JA DISPONIVEL — ferramentas `mcp__claude_ai_Cloudflare_Developer_Platform__*` já estão ativas nesta sessão
- **O que faz:** Gerencia Workers, D1, KV, R2, Hyperdrive, busca docs Cloudflare
- **Tipo:** MCP remoto oficial Cloudflare
- **Acesso:** Read + Write
- **Gap cobre:** Cloudflare Workers/CDN config, D1 queries, KV namespaces, R2 buckets

#### 3. Supabase MCP (JA INSTALADO)
- **Status:** JA DISPONIVEL — ferramentas `mcp__claude_ai_Supabase__*` já ativas
- **O que faz:** Execute SQL, apply migrations, deploy Edge Functions, generate TypeScript types, get logs, manage branches
- **Tipo:** MCP remoto oficial Supabase
- **Acesso:** Read + Write
- **Gap cobre:** Supabase além do auth — migrations, Edge Functions, type generation, performance advisors

#### 4. Figma MCP (JA INSTALADO)
- **Status:** JA DISPONIVEL — ferramentas `mcp__claude_ai_Figma__*` já ativas
- **O que faz:** Lê designs do Figma e gera código React/Tailwind correspondente; Code Connect para mapear componentes
- **Tipo:** MCP remoto oficial Figma
- **Acesso:** Read (design) + Write (design back)
- **Gap cobre:** Brief → LP workflow — do design ao código sem retrabalho manual

### MCPs de SUPORTE — Média prioridade

#### 5. GitHub MCP (oficial @modelcontextprotocol)
- **O que faz:** Lê issues, revisa PRs, gerencia branches, cria arquivos, check CI
- **Tipo:** MCP local via npx
- **Acesso:** Read + Write (com personal access token)
- **Gap cobre:** CI/CD workflow, code review, branch management
- **Instalar:**
  ```bash
  claude mcp add github --scope user -- npx -y @modelcontextprotocol/server-github
  export GITHUB_PERSONAL_ACCESS_TOKEN=ghp_seu_token
  ```

#### 6. Context7 MCP
- **O que faz:** Injeta docs atualizadas e versionadas de bibliotecas no contexto (Next.js, React, Supabase, Tailwind)
- **Tipo:** Read-only, npx
- **Gap cobre:** Evita erros de API deprecated, garante código correto para versão atual do framework
- **Instalar:**
  ```bash
  claude mcp add context7 -- npx -y @upstash/context7-mcp@latest
  ```

#### 7. Puppeteer MCP
- **O que faz:** Controla Chrome headless — navegação, screenshots, testes visuais, formulários
- **Tipo:** Read/Execute, npx
- **Gap cobre:** Smoke testing de LPs deployadas, visual regression, debug de responsive
- **Instalar:**
  ```bash
  claude mcp add puppeteer -s user -- npx -y @modelcontextprotocol/server-puppeteer
  ```

### Skills extras de CI/CD identificadas

#### 8. yeet (openai skill)
- Deploy: stage → commit → push → draft PR em um comando
- Útil para velocity alta de deploys de LPs
- Complementa o github skill

---

## Mapa de cobertura

| Competência | Ferramenta/Skill | Status |
|-------------|-----------------|--------|
| React patterns para LP (App Router, RSC, bundles) | react-best-practices | Instalar |
| Next.js conventions, async API, metadata, OG | next-best-practices | Instalar |
| Caching (PPR, use cache, ISR) | next-cache-components | Instalar |
| LP visual design (hero, hierarquia, motion) | frontend-skill | Instalar |
| Core Web Vitals audit (LCP, CLS, FID) | web-perf | Instalar |
| SEO/AEO: meta, JSON-LD, OG para nicho local+digital | seo-aeo-best-practices | Instalar |
| Deploy Vercel (CLI, preview, produção) | vercel-deploy (skill) + Vercel MCP | Instalar |
| UX audit, acessibilidade, anti-patterns | web-design-guidelines | Instalar |
| Git workflow (PRs, squash, stacked branches) | github (skill) | Instalar |
| CI/CD debug (GitHub Actions) | gh-fix-ci | Instalar |
| Cloudflare Workers/KV/R2/D1 | wrangler (skill) + Cloudflare MCP | Disponível |
| Supabase além de auth (migrations, Edge Fn, types) | Supabase MCP | JA ATIVO |
| Figma → código (brief to LP) | Figma MCP | JA ATIVO |
| Auth Supabase + Next.js | nextjs-supabase-auth | JA ATIVO (Stage 1) |
| Postgres/RLS | supabase-postgres-best-practices | JA ATIVO (Stage 1) |
| CSS utilities (Tailwind) | tailwind-css | JA ATIVO (Stage 1) |
| Docs atualizadas de libs (Next, React, Supabase) | Context7 MCP | Instalar |
| Visual testing / smoke test LPs | Puppeteer MCP | Instalar (baixa prioridade) |
| GitHub repo management, CI integration | GitHub MCP | Instalar |

---

## Gaps sem cobertura após Stage 2

### Gaps parcialmente cobertos (precisam de Stage 3 — pesquisa profunda)

1. **LP building workflow completo (brief → deploy)**
   - Cobertura atual: skills isoladas (design, dev, deploy) mas sem workflow integrado passo a passo
   - Falta: processo documentado de como a agência vai do brief do cliente à LP no ar, incluindo handoff Figma, copy integration, aprovação de cliente, go-live checklist
   - Ação Stage 3: pesquisar "agency workflow landing page development process brief to deploy checklist"

2. **TypeScript avançado para LP (types, generics, patterns)**
   - Cobertura atual: Next.js best practices cobre TypeScript superficialmente
   - Falta: TS patterns específicos — typed API routes, typed Supabase queries, component prop types para LP reutilizável
   - Ação Stage 3: verificar se existe skill "typescript-patterns" ou equivalente, ou pesquisar diretamente

3. **Copy/design integration no código**
   - Cobertura atual: Figma MCP cobre design → código, mas não integração de copy (headline, CTA, benefícios)
   - Falta: padrão para receber copy do cliente e estruturar em componentes de LP de forma modular e reutilizável
   - Ação Stage 3: pesquisar patterns de content-driven LP architecture

4. **Vercel Edge Functions patterns**
   - Cobertura atual: next-best-practices toca em route handlers mas não Edge Functions especificamente
   - Falta: quando usar Edge vs Serverless Function, middleware patterns, geolocation, A/B testing em edge
   - Ação Stage 3: verificar skill vercel-labs/edge-functions ou pesquisar documentação

5. **Performance budget e métricas de negócio**
   - Cobertura atual: web-perf cobre diagnóstico técnico
   - Falta: definição de performance budget para LPs (LCP < 2.5s como meta de negócio), correlação performance → conversão
   - Ação Stage 3: pesquisar "landing page performance budget conversion rate correlation"

6. **Monitoramento pós-deploy (analytics, errors, uptime)**
   - Cobertura atual: Vercel MCP cobre logs de build/deploy
   - Falta: integração de error tracking (Sentry?), analytics de conversão, Core Web Vitals em produção
   - Ação Stage 3: pesquisar MCPs ou skills para Sentry, Plausible/Vercel Analytics

### Gaps não cobertos (Stage 3 prioritário)

7. **Padrão de sistema de design reutilizável para agência**
   - Sem cobertura atual
   - Falta: como estruturar um design system de componentes de LP que acelera a entrega do 2º, 3º, 4º cliente
   - Alta importância para escalar a agência

8. **Pricing page e CTA patterns de alta conversão**
   - Sem cobertura atual (frontend-skill é genérico em design, não em conversão)
   - Falta: patterns específicos de LP de conversão: above the fold, CTA placement, social proof, urgência
   - Ação Stage 3: skill ou research específico em LP conversion optimization

---

## Comandos de instalação (ordem recomendada)

```bash
# Tier 1 — Instalar primeiro (core do workflow)
npx skills add https://github.com/vercel-labs/react-best-practices --skill react-best-practices
npx skills add https://github.com/vercel-labs/next-best-practices --skill next-best-practices
npx skills add https://github.com/openai/frontend-skill --skill frontend-skill
npx skills add https://github.com/cloudflare/web-perf --skill web-perf

# Tier 2 — Instalar a seguir (deploy + SEO + performance)
npx skills add https://github.com/openai/vercel-deploy --skill vercel-deploy
npx skills add https://github.com/sanity-io/seo-aeo-best-practices --skill seo-aeo-best-practices
npx skills add https://github.com/vercel-labs/next-cache-components --skill next-cache-components

# Tier 3 — Git/CI workflow
npx skills add https://github.com/callstackincubator/github --skill github
npx skills add https://github.com/openai/gh-fix-ci --skill gh-fix-ci
npx skills add https://github.com/vercel-labs/web-design-guidelines --skill web-design-guidelines

# MCPs — Instalar separadamente
claude mcp add --transport http vercel https://mcp.vercel.com
claude mcp add context7 -- npx -y @upstash/context7-mcp@latest
claude mcp add github --scope user -- npx -y @modelcontextprotocol/server-github
```
