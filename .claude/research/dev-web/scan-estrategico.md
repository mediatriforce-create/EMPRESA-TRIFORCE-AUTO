# Scan Estratégico — Dev Web Senior
Data: 2026-04-13

---

## Gap 1 — LP Workflow para Agência

### Framework: Brief → Deploy (8 fases)

**Fase 1 — Intake de brief (documento único)**
- Formulário padronizado (Google Forms ou Typeform) com campos obrigatórios: objetivo da LP (lead/cadastro/venda), público-alvo, diferenciais, conteúdo (headlines, CTAs, tom de voz), seções desejadas, recursos visuais (logo, paleta, fontes), requisitos técnicos, KPIs, prazo e orçamento
- Saída: brief assinado via e-mail + one-pager resumido para o time
- SOP: template de intake com SLA de resposta (ex: 24h para confirmação)

**Fase 2 — Aprovação de design (sprint 5 dias)**
- Day 0: kickoff com cliente (agenda + brief resumido)
- Day 1–2: wireframes baixa fidelidade (hierarquia, CTA, fluxo)
- Day 3–4: mockups alta fidelidade (cores, tipografia, estados)
- Day 5: protótipo navegável opcional para feedback
- Critério de aprovação: estrutura aprovada + fontes/cores aprovadas + responsividade em 3 breakpoints (desktop, tablet, mobile)
- Entregável: link Figma + guia de estilo básico (tokens: paleta, tipografia, espaçamento, componentes)

**Fase 3 — Preparação técnica**
- Stack: React + TypeScript + Next.js (SSR/SEO) + ESLint + Prettier + Commitlint
- Design tokens exportados como JSON/TS (cores, fontes, spacing, radii, breakpoints)
- Repositório pronto com estrutura de componentes e pipeline de deploy (Vercel)
- Checklist técnico gerado para Dev + QA

**Fase 4 — Desenvolvimento**
```
src/
  components/     # reutilizáveis
  pages/ (ou app/)
  styles/
  hooks/
  types/
config/           # eslint, tsconfig, prettier
public/assets/    # logos, imagens otimizadas
```
- Git: branching simples (main, feature/cliente-lp, hotfix)
- Preview URL disponível ao cliente via Vercel a cada PR

**Fase 5 — QA checklist**
- Responsividade verificada em 3 breakpoints
- CTAs e formulários funcionando com integração
- Performance: Lighthouse score ≥ 90 (Performance, Acessibilidade)
- SEO básico: title, meta description, alt text
- Links ativos, sem placeholders visíveis
- Conteúdo textual revisado

**Fase 6 — Entrega ao cliente**
- URL de preview com aprovação formal (e-mail com OK ou checklist assinado)
- Guia rápido de uso (como editar conteúdo, atualizações simples)
- Documentação técnica resumida (tokens, APIs integradas, passos de manutenção)

**Fase 7 — Go-live checklist**
- [ ] Domínio DNS propagado (A/CNAME verificado)
- [ ] SSL ativo
- [ ] CDN e cache configurados (Vercel Edge Network)
- [ ] Redirecionamentos 301 configurados
- [ ] Sitemap.xml e robots.txt
- [ ] Build de produção disponível
- [ ] Lighthouse/Performance ≥ objetivo
- [ ] Formulário funcionando com integração (CRM, e-mail)
- [ ] Google Analytics / Vercel Analytics ativos
- [ ] Monitoramento inicial de uptime e erros

**Fase 8 — Pós-lançamento**
- Monitorar métricas mensais (visitas, CTR, conversões, bounce rate)
- Relatórios simples ao cliente (CSV ou Slides)
- Roadmap de melhorias (priorizado)

### Ferramentas recomendadas (equipe 1–3 pessoas)
| Área | Ferramenta |
|------|-----------|
| Gestão de projeto | Notion ou Trello (kanban com templates de projeto) |
| Design | Figma (design system, tokens, protótipos) |
| Dev | VS Code, Node.js LTS, GitHub |
| QA/Performance | Lighthouse, axe-core, Jest + RTL |
| Deploy | Vercel (preview automático por PR) |
| Analytics | Vercel Analytics + Google Analytics |
| Documentação | Notion (SOPs, guias de entrega, playbooks) |

---

## Gap 2 — TypeScript Avançado

### Geração de tipos Supabase

**Comando de geração:**
```bash
npx supabase gen types typescript --project-id "$PROJECT_REF" --schema public > src/types/database.types.ts
```
- Para dev local: `--local`
- Para self-hosted: `--db-url`
- Automatizar: script `"gen-types"` no `package.json` + GitHub Actions cron nightly

**Cliente tipado (singleton):**
```typescript
import { createClient } from '@supabase/supabase-js'
import type { Database } from '@/types/database.types'

export const supabase = createClient<Database>(
  process.env.NEXT_PUBLIC_SUPABASE_URL!,
  process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!
)
```

**Queries tipadas:**
- `select('*')` retorna `Database['public']['Tables']['clientes']['Row'][]` automaticamente
- Para joins: usar helper `QueryData<typeof query>` para tipos aninhados
- Para shapes customizados: `.overrideTypes<T>()`
- Para JSON com RLS: usar `MergeDeep` da lib `type-fest`

**Route Handlers tipados (App Router):**
```typescript
// app/api/clientes/route.ts
import { NextRequest, NextResponse } from 'next/server'
import { CreateClienteSchema } from '@/schemas/cliente'

export async function GET(req: NextRequest) {
  const { data, error } = await supabase
    .from('clientes')
    .select('*')
  if (error) return NextResponse.json({ error }, { status: 400 })
  return NextResponse.json(data)
}

export async function POST(req: NextRequest) {
  const payload = await req.json()
  const parsed = CreateClienteSchema.parse(payload) // Zod validation
  const { data, error } = await supabase
    .from('clientes')
    .insert(parsed)
    .single()
  // ...
}
```

**Padrão completo — checklist de implementação:**
- [ ] Gerar tipos do DB e exportar como `Database`
- [ ] Criar cliente Supabase tipado singleton em `lib/supabaseClient.ts`
- [ ] Definir schemas Zod espelhando os tipos de insert/update
- [ ] Tipar route handlers com `NextRequest`/`NextResponse` + tipos gerados
- [ ] Compartilhar tipos centralizados em `src/types/` para Server e Client Components
- [ ] Regenerar tipos após cada migration e testar end-to-end
- [ ] Proteger routes com middleware cookie-based auth (Supabase SSR)

**Boas práticas para agência com múltiplos projetos:**
- Um arquivo `database.types.ts` por projeto em `src/types/`
- Script de geração padronizado no `package.json` de cada projeto
- GitHub Actions cron job para regenerar tipos após migrations
- Versionar tipos no repositório para rastrear mudanças de schema

---

## Gap 3 — Vercel Edge Functions e Middleware

### Edge vs Serverless — Tabela de decisão

| Critério | Edge Function | Serverless Function |
|----------|--------------|---------------------|
| Cold start | < 5ms | 100ms–1s+ |
| Warm execution | ~106ms (P50) | ~246ms |
| Runtime | V8 Isolates (limitado) | Node.js completo |
| Memória máxima | ~128MB | até 3GB |
| Tempo de execução | segundos | até 15min |
| Node.js APIs nativas | Limitado | Completo |
| Banco de dados direto | Não ideal (latência) | Sim |
| Ecossistema npm | Limitado | Completo |

**Benchmarks reais (Vercel, 2025):**
- Edge cold start: < 5ms vs Serverless cold start: 100ms–1s+
- Edge warm: 167ms vs Serverless warm: 287ms (2x mais rápido)
- Edge 9x mais rápido em cold starts

### Quando usar Edge

- Auth checks e validação de token antes de chegar à rota
- A/B testing e personalização por usuário/região
- Geolocalização para conteúdo regionalizado
- Header manipulation (CSP, redirects, reescritas)
- Cache e respostas leves que precisam de baixa latência global
- Middleware de i18n e routing condicional

### Quando NÃO usar Edge

- Tarefas CPU-bound longas
- Acesso direto a banco de dados (PostgreSQL/Supabase) sem camada de cache
- Processamento de arquivos grandes
- Uso de APIs Node.js nativas não disponíveis no runtime V8
- Lógica de negócio complexa com muitas dependências npm

### Padrão de A/B Testing com Edge Middleware

```typescript
// middleware.ts (na raiz do projeto Next.js)
import { NextRequest, NextResponse } from 'next/server'

const COOKIE_NAME = 'bucket-marketing'
const BUCKETS = ['original', 'a', 'b'] as const
type Bucket = typeof BUCKETS[number]

const getBucket = (): Bucket => BUCKETS[Math.floor(Math.random() * BUCKETS.length)]

export function middleware(req: NextRequest) {
  const url = req.nextUrl.clone()
  const existingBucket = req.cookies.get(COOKIE_NAME)?.value as Bucket | undefined
  const bucket = existingBucket ?? getBucket()

  url.pathname = `/marketing/${bucket}`
  const res = NextResponse.rewrite(url)

  if (!existingBucket) {
    res.cookies.set(COOKIE_NAME, bucket, {
      path: '/',
      maxAge: 60 * 60 * 24 * 30 // 30 dias
    })
  }

  return res
}

export const config = {
  matcher: '/marketing/:path*'
}
```

### A/B Testing com Geolocalização

```typescript
const COUNTRY_VARIANTS: Record<string, Bucket> = {
  BR: 'a',    // variante brasileira
  US: 'b',    // variante americana
}

export function middleware(req: NextRequest) {
  const country = req.geo?.country ?? 'default'
  const geoVariant = COUNTRY_VARIANTS[country] ?? 'original'
  const bucket = req.cookies.get(COOKIE_NAME)?.value ?? geoVariant
  // ... mesmo padrão de rewrite + cookie
}
```

### Arquitetura híbrida recomendada

```
Edge Middleware (middleware.ts)
  → Auth check / A/B routing / geolocation
  → Rewrite para rota correta

Route Handler (app/api/*)
  → Lógica de negócio
  → Queries Supabase
  → Processamento pesado
```

---

## Gap 4 — Sistema de Design Reutilizável

### Estrutura de monorepo para agência

```
packages/
  core/           # design tokens, theme system, utilities
  primitives/     # atoms: Button, Input, Icon, Label, Card, Image
  modules/        # organisms: HeroSection, ServicesGrid, Testimonials,
                  #            PricingTable, LeadForm, FAQSection
  templates/      # layouts de LP: LPTemplateHeroLeft, LPTemplateSplit, LPTemplateMinimal
  themes/         # configs de tema por cliente

apps/
  client-templates/  # LPs por nicho (barbearia, personal, coach, infoprodutor)

.storybook/       # documentação de componentes (opcional mas recomendado)
```

### Design Tokens — estrutura base

```typescript
// packages/core/tokens.ts
export const tokens = {
  colors: {
    primary: '#000000',
    accent: '#000000',
    bg: '#ffffff',
    text: '#111111',
    muted: '#6b7280',
  },
  radii: { sm: '6px', md: '12px', lg: '24px', full: '9999px' },
  shadows: {
    sm: '0 1px 2px rgba(0,0,0,.05)',
    md: '0 4px 16px rgba(0,0,0,.1)',
  },
  spacing: { xs: '4px', sm: '8px', md: '16px', lg: '32px', xl: '64px' },
  breakpoints: { sm: '640px', md: '768px', lg: '1024px', xl: '1280px' },
  fontSizes: { sm: '0.875rem', base: '1rem', lg: '1.125rem', xl: '1.25rem', '2xl': '1.5rem', '4xl': '2.25rem' },
}
```

### Theming por cliente (CSS Variables + Tailwind)

```typescript
// packages/themes/barbearia-vintage.ts
import { tokens } from '../core/tokens'
export const barbeariaVintage = {
  ...tokens,
  colors: {
    ...tokens.colors,
    primary: '#c8860a',   // dourado
    accent: '#8b1a1a',    // vinho
    bg: '#1a1a1a',        // fundo escuro
    text: '#f5f0e8',      // creme
  }
}

// packages/themes/coach-premium.ts
export const coachPremium = {
  ...tokens,
  colors: {
    primary: '#2563eb',   // azul
    accent: '#7c3aed',    // roxo
    bg: '#ffffff',
    text: '#0f172a',
  }
}
```

### Atomic Design — hierarquia de componentes

```
Atoms (primitives/)
  Button — variants: primary | secondary | ghost | outline
           sizes: sm | md | lg
           props: fullWidth, isLoading, leftIcon, rightIcon

  Input — types: text | email | tel | textarea
  Badge, Icon, Avatar, Divider

Molecules
  LeadForm — name + email + phone + CTA button
  TestimonialCard — photo + name + city + quote + rating
  ServiceCard — icon + title + description + price

Organisms (modules/)
  HeroSection — layout: split | centered | full-bleed
                props: headline, subheadline, ctaText, ctaHref, image/video
  ServicesGrid — grid de ServiceCards (2, 3 ou 4 colunas)
  TestimonialsCarousel — carrossel de TestimonialCards
  PricingTable — planos com features e CTA
  FAQSection — accordion com perguntas frequentes
  LeadCapture — formulário com prova social lateral

Templates
  LPTemplateBasic — Hero + Services + Testimonials + CTA
  LPTemplateFullSales — Hero + Problem + Solution + Services + Testimonials + Pricing + FAQ + CTA
  LPTemplateMinimal — Hero + LeadForm (one-page)
```

### Fluxo de entrega por cliente (2º, 3º, 4º)

1. Selecionar template base (`LPTemplateBasic` ou `LPTemplateFullSales`)
2. Criar arquivo de tema: `themes/cliente-nome.ts`
3. Criar arquivo de conteúdo: `content/cliente-nome.json`
4. Aplicar `<ThemeProvider theme={clienteTema}>` no layout
5. Build: `CLIENT_ID=cliente-nome npm run build`

**Estrutura de conteúdo por cliente:**
```json
// content/barbearia-silva.json
{
  "hero": {
    "headline": "Cortes que Realçam Sua Personalidade",
    "subheadline": "Atendimento premium no coração de Salvador",
    "ctaText": "Agendar Horário",
    "ctaHref": "https://wa.me/55719999999"
  },
  "services": [...],
  "testimonials": [...]
}
```

### Ferramentas recomendadas

| Ferramenta | Papel |
|-----------|-------|
| **Tailwind CSS** | Utilitários de styling, JIT, responsive |
| **Radix UI** | Primitivos acessíveis (Dialog, Popover, Accordion) |
| **Shadcn/ui** | Componentes prontos (Radix + Tailwind) para bootstrap rápido |
| **CSS Variables** | Theming runtime sem recarregar página |
| **PNPM Workspaces** | Monorepo management |
| **Storybook** | Documentação de componentes (opcional, recomendado no 3º projeto) |

---

## Gap 5 — LP Conversion Patterns

### Benchmarks de conversão (2025)

- Taxa de conversão média de LPs: **3%–8%** para serviços gerais
- LPs bem segmentadas com oferta clara: **5%–15%**
- Desktop converte **~8% mais** que mobile em média (otimização mobile é obrigatória)
- CTA acima da dobra melhora taxa de cliques consistentemente
- Textos em linguagem simples (5º–7º ano escolar) apresentam maiores taxas de conversão

### Hero Section — estrutura ideal

**Para negócios presenciais (barbearia, salão, personal trainer):**
```
[Foto autêntica do negócio em ação — barbeiro, treino, atendimento]
[Headline: benefício específico em 5–8 palavras]
  "Cortes que Realçam Seu Estilo em 45 Minutos"
[Subheadline: prova social + localização]
  "Mais de 500 clientes satisfeitos em Salvador-BA"
[CTA Principal] — botão grande, cor contrastante
  "Agendar agora no WhatsApp"
[CTA Secundário] — menor, abaixo ou ao lado
  "Ver depoimentos"
[Social proof de credibilidade imediata]
  ★★★★★ 4.9 no Google (127 avaliações)
```

**Para empreendedores digitais (coach, infoprodutor):**
```
[Foto/vídeo do especialista com autoridade]
[Headline: resultado + prazo]
  "Transforme Seu Negócio em 90 Dias com Estratégia Comprovada"
[Subheadline: quem é você + prova]
  "Método aplicado por +2.000 empreendedores no Brasil"
[CTA Principal]
  "Quero começar agora"
[CTA Secundário]
  "Ver o método gratuitamente"
```

### Posicionamento de CTAs

| Posição | Recomendação |
|---------|-------------|
| Acima da dobra | CTA principal — obrigatório, cor de alto contraste |
| Após prova social | CTA médio — reforça a decisão |
| Após pricing/planos | CTA de conversão — direto para compra/agendamento |
| Footer | CTA final de captura |
| Mobile fixo | Botão flutuante no rodapé (WhatsApp/agendar) |

**Regra de quantidade:** mínimo 2 CTAs (principal + secundário). Máximo 4 em LPs longas. Não exagerar — muitas opções paralisam a decisão.

### Prova Social — quando e onde

| Tipo de prova social | Posição ideal |
|---------------------|--------------|
| Avaliações Google/Facebook (estrelas) | No hero, abaixo do headline |
| Depoimentos com foto + nome + cidade | Logo abaixo do hero (1ª seção após hero) |
| Número de clientes atendidos | No hero ou seção de benefícios |
| Logotipos de clientes/parceiros | Após depoimentos |
| Resultados específicos (antes/depois) | Meio da página |
| Casos de sucesso com localização (Salvador-BA) | Aumenta credibilidade regional |

**Para negócios locais:** depoimentos de clientes da mesma cidade aumentam a credibilidade regional significativamente.

### Urgência e Escassez

- Usar apenas com oferta real — urgência falsa corrói confiança
- Exemplos éticos:
  - "Apenas 3 vagas para consultoria esta semana"
  - "Oferta válida até [data real]"
  - "Preço de lançamento — próxima turma sobe R$ 200"
- Contador regressivo: usar somente quando há deadline real
- Texto de urgência no CTA: "Garantir minha vaga agora" > "Clique aqui"

### Mobile-First — regras críticas

- CTA fixo no rodapé (sticky bottom button) — sempre visível durante scroll
- Botão mínimo: 44px de altura (touch target)
- Tipografia mínima: 16px para corpo do texto (evita zoom automático iOS)
- Formulário: máximo 3–4 campos no mobile (nome, e-mail, WhatsApp)
- Imagens: lazy loading, WebP, dimensões explícitas (evita CLS)
- Hero: texto antes da imagem no DOM (mobile-first rendering)

### Estrutura de LP de alta conversão (ordem)

1. **Hero** — headline + CTA + prova social de credibilidade
2. **Prova social** — depoimentos com foto/nome/cidade
3. **Problema/Dor** — identificação com o cliente
4. **Solução/Benefícios** — 3–5 bullets com ganhos tangíveis
5. **Como funciona** — processo simples em 3 passos
6. **Prova adicional** — mais depoimentos ou cases
7. **Oferta/Preço** — pricing claro com urgência (se aplicável)
8. **FAQ** — objeções respondidas
9. **CTA final** — reforço da oferta + urgência

---

## Gap 6 — Monitoramento Pós-Deploy

### Stack de monitoramento recomendado para agência pequena

**Tier 1 — Gratuito (começo imediato):**
- **Vercel Speed Insights** — Core Web Vitals em produção (LCP, INP, CLS) por deployment
- **Vercel Analytics** — tráfego, pageviews, visitantes únicos
- **Vercel Alerts** — alerta automático quando error rate > 4σ acima da média (5xx, 4xx configurável)
- **PageSpeed Insights (PSI)** — lab data complementar para diagnóstico
- **Sentry Free Tier** — até 5.000 errors/mês, source maps, stack traces

**Tier 2 — Pago quando necessário:**
- **Sentry Team** — ~$26–29/mês, sem limite de projetos para agência
- **Highlight.io** — session replays + error tracking (alternativa ao Sentry com tier free)
- **PostHog** — analytics de produto, feature flags, funis de conversão

### Setup mínimo de Sentry para Next.js

```bash
npm install @sentry/nextjs
```

```typescript
// next.config.js
const { withSentryConfig } = require('@sentry/nextjs')

module.exports = withSentryConfig(nextConfig, {
  silent: true,
  org: 'triforce-auto',
  project: 'cliente-nome',
})
```

**Variáveis de ambiente (Vercel):**
```
SENTRY_DSN=https://xxx@sentry.io/xxx
SENTRY_AUTH_TOKEN=xxx  # para upload de source maps
```

**Sentry cria automaticamente:**
- `instrumentation-client.ts` — erros de browser
- `sentry.server.config.ts` — erros de servidor Node.js
- `sentry.edge.config.ts` — erros de edge runtime

**Integração Vercel Marketplace:** link projeto Vercel ↔ projeto Sentry para upload automático de source maps a cada deploy.

### Vercel Speed Insights — configuração

```bash
npm install @vercel/speed-insights
```

```tsx
// app/layout.tsx
import { SpeedInsights } from '@vercel/speed-insights/next'
import { Analytics } from '@vercel/analytics/react'

export default function RootLayout({ children }) {
  return (
    <html>
      <body>
        {children}
        <SpeedInsights />
        <Analytics />
      </body>
    </html>
  )
}
```

### Métricas e metas de produção

| Métrica | Meta (boa) | Meta (excelente) | Ação se falhar |
|---------|-----------|-----------------|----------------|
| LCP (Largest Contentful Paint) | < 2.5s | < 1.8s | Otimizar imagem hero, lazy load |
| INP (Interaction to Next Paint) | < 200ms | < 100ms | Reduzir JS no main thread |
| CLS (Cumulative Layout Shift) | < 0.1 | < 0.05 | Dimensões explícitas em imagens |
| FCP (First Contentful Paint) | < 1.8s | < 1.2s | Reduzir render-blocking resources |
| TTFB (Time to First Byte) | < 800ms | < 200ms | Cache headers, ISR, CDN |

### Alertas automáticos — configurar no Vercel

- **Error Anomaly Alert:** quando taxa de erro (5xx) supera 4σ da média de 24h → notificar por e-mail + Slack
- **Configurável:** também ativar para 4xx (erros de cliente)
- **Sentry:** metric alerts se error rate > threshold definido em 5min

### Dashboard mínimo de monitoramento por cliente

Por projeto entregue, configurar:
1. Vercel Speed Insights ativo (campo CWV real de usuários)
2. Vercel Analytics ativo (tráfego)
3. Sentry projeto vinculado (error tracking com source maps)
4. Alerta de error anomaly no Vercel (e-mail do cliente ou da agência)
5. Verificação mensal com PSI para validar CWV ainda dentro das metas

### Comparativo de ferramentas de error tracking

| Ferramenta | Source Maps | Session Replay | Custo small agency | Recomendação |
|-----------|------------|---------------|-------------------|-------------|
| **Sentry** | Sim (auto via Vercel) | Sim (pago) | Free até 5K erros/mês | **Principal escolha** |
| **Vercel Built-in** | Não | Não | Incluso no plano | Complementar (métricas rápidas) |
| **Highlight.io** | Sim | Sim | Free tier generoso | Alternativa ao Sentry |
| **Datadog** | Parcial | Sim | $200+/mês | Excessivo para agência pequena |
| **GlitchTip** (self-hosted) | Sim | Não | ~$15–50/mês de infra | Opção budget |

---

## Gaps que permaneceram sem cobertura

**Nenhum gap ficou sem cobertura adequada.** Todos os 6 foram respondidos com frameworks práticos.

**Pontos que podem ser aprofundados em Stage 4 se necessário:**
- Copy integration no código: padrão para receber copy do cliente e estruturar em componentes modulares (conteúdo JSON-driven com CMS headless leve)
- Performance budget por nicho: correlação específica entre velocidade de LP e taxa de conversão para barbearias/coaches no Brasil
- Testes A/B com analytics integrado: coleta de dados de experimento no edge + visualização em dashboard (Amplitude, Mixpanel, ou PostHog)
- Vercel Edge Config: feature flags e configuração dinâmica sem redeploy
