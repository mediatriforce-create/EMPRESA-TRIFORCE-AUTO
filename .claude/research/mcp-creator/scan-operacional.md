# Scan Operacional — Criador de MCP Servers Senior

**Data:** 2026-05-06
**Responsavel:** Gabriela (RH)
**Objetivo:** Skills externas, frameworks reutilizaveis e ferramentas operacionais para o cargo

---

## 1. SKILLS EXTERNAS ENCONTRADAS

### 1.1 MCP Builder (ComposioHQ/awesome-claude-skills)
- **URL:** https://github.com/ComposioHQ/awesome-claude-skills/blob/master/mcp-builder/SKILL.md
- **Autor:** ComposioHQ (reconhecido, curadoria de skills)
- **Qualidade:** ALTA — 4 fases estruturadas, reference/ com docs detalhados
- **O que cobre:**
  - Processo completo de 4 fases: Research & Planning > Implementation > Review & Refine > Evaluations
  - Design agent-centric (workflow tools, nao API wrappers)
  - Validacao com Pydantic v2 (Python) e Zod (TypeScript)
  - Tool annotations (readOnlyHint, destructiveHint, idempotentHint, openWorldHint)
  - Patterns de erro educativos para agents
  - Framework de avaliacao com 10 questoes complexas
  - References locais: mcp_best_practices.md, python_mcp_server.md, node_mcp_server.md, evaluation.md
- **Gaps que cobre:** 2 (MCPs customizados), 5 (Zod), 7 (documentacao)
- **Relevancia Triforce:** ALTA — cobre exatamente o gap de MCPs customizados do zero

### 1.2 Skill Creator (daymade/claude-code-skills)
- **URL:** https://github.com/daymade/claude-code-skills
- **Autor:** daymade (marketplace independente, 51+ skills)
- **Qualidade:** MEDIA — meta-skill para criar skills, nao especifico MCP
- **O que cobre:** Criacao, validacao e empacotamento de Claude Code skills
- **Relevancia Triforce:** BAIXA — complemento generico, nao foca MCP

### 1.3 Supabase Automation Skill
- **URL:** https://github.com/ComposioHQ/awesome-claude-skills/blob/master/supabase-automation
- **Qualidade:** MEDIA — automacao via Composio, nao construcao de MCPs
- **O que cobre:** SQL queries, table schemas, edge functions, storage
- **Gaps que cobre:** 3 (stack Supabase) — parcial
- **Relevancia Triforce:** MEDIA — referencia para integracao Supabase

### 1.4 Airtable Automation Skill
- **URL:** https://github.com/ComposioHQ/awesome-claude-skills/blob/master/airtable-automation
- **Qualidade:** MEDIA — automacao via Composio
- **O que cobre:** Records, tables, bases, views, field management
- **Gaps que cobre:** 3 (stack Airtable) — parcial
- **Relevancia Triforce:** MEDIA — referencia para integracao Airtable

### 1.5 Connect/OpenWeb (ComposioHQ)
- **URL:** https://github.com/openweb-org/openweb
- **Qualidade:** ALTA — 500+ apps, auth automatico (cookies, JWT, CSRF)
- **O que cobre:** Integracao agent-native com websites (JSON in/out), 90+ sites built-in
- **Relevancia Triforce:** MEDIA — referencia de patterns de auth para MCPs

---

## 2. FRAMEWORKS E FERRAMENTAS ENCONTRADOS

### 2.1 SDKs Oficiais

#### @modelcontextprotocol/sdk (TypeScript) — PRINCIPAL
- **URL:** https://github.com/modelcontextprotocol/typescript-sdk
- **NPM:** https://www.npmjs.com/package/@modelcontextprotocol/sdk
- **Versao:** 1.17.4 (v1.x estavel) | v2 pre-alpha em dev
- **Downloads:** 11.484+ projetos dependentes no npm
- **Docs:** https://ts.sdk.modelcontextprotocol.io
- **O que faz:** SDK oficial para criar MCP servers e clients em TypeScript
- **Features:**
  - McpServer class com registro de tools/resources/prompts
  - Transports: stdio, Streamable HTTP, SSE (legacy)
  - Standard Schema (Zod v4, Valibot, ArkType)
  - Middleware packages (Express, Hono, Node.js HTTP)
  - Runtimes: Node.js, Bun, Deno
- **Seguranca:** OAuth 2.1 resource server pattern, Bearer tokens
- **Gaps que cobre:** 1 (TS SDK), 4 (protocolo profundo), 5 (Zod)
- **Relevancia Triforce:** CRITICA — base obrigatoria

#### modelcontextprotocol/python-sdk
- **URL:** https://github.com/modelcontextprotocol/python-sdk
- **O que faz:** SDK oficial Python com FastMCP integrado
- **Relevancia Triforce:** BAIXA — stack e TypeScript, mas bom para referencia

### 2.2 Frameworks de Alto Nivel

#### FastMCP (TypeScript) — punkpeye/fastmcp
- **URL:** https://github.com/punkpeye/fastmcp
- **Stars:** 3.100+ | Forks: 264
- **NPM:** fastmcp | JSR: @glama/fastmcp
- **Docs:** https://punkpeye-fastmcp.mintlify.app
- **O que faz:** Framework de alto nivel sobre o SDK oficial, elimina boilerplate
- **Features:**
  - API simples com Zod nativo: `server.addTool({ parameters: z.object({...}), execute: async (args) => ... })`
  - Auth/OAuth built-in, session management (stateful/stateless)
  - Transports: stdio, HTTP Streaming, SSE
  - EdgeFastMCP para Cloudflare Workers/Deno Deploy
  - Custom HTTP routes (REST, webhooks, admin)
  - HTTPS, CORS, health-check, progress notifications
  - Image/audio content, streaming output
  - CLI: `npx fastmcp dev` para teste
- **Seguranca:** OAuth, CORS, HTTPS nativo
- **Gaps que cobre:** 1 (TS), 2 (customizados), 5 (Zod), 6 (Edge/Deno), 8 (seguranca)
- **Relevancia Triforce:** ALTA — alternativa produtiva ao SDK puro

#### MCP Framework — QuantGeekDev/mcp-framework
- **URL:** https://github.com/QuantGeekDev/mcp-framework
- **Site:** https://mcp-framework.com
- **O que faz:** Framework class-based com CLI e auto-discovery
- **Features:**
  - CLI: `mcp create`, `mcp add tool/prompt/resource`
  - Auto-discovery de tools/resources/prompts por diretorio
  - Class-based: extends MCPTool com Zod schemas
  - Transports: stdio, SSE, HTTP (experimental)
  - Auth SSE: OAuth 2.1, JWT, API Key
  - Validacao de schema descriptions em build-time
- **Gaps que cobre:** 1 (TS), 2 (customizados), 5 (Zod)
- **Relevancia Triforce:** MEDIA — bom para scaffolding rapido, menos maduro que FastMCP

### 2.3 Geradores Spec-Driven

#### Speakeasy — OpenAPI-to-MCP
- **URL:** https://www.speakeasy.com/blog/release-model-context-protocol
- **URL gerador:** https://www.speakeasy.com/blog/generate-mcp-from-openapi
- **O que faz:** Gera MCP servers TypeScript a partir de specs OpenAPI automaticamente
- **Features:**
  - Cada metodo SDK vira tool MCP automaticamente
  - x-speakeasy-mcp extension para customizar nomes/descricoes
  - Scoping system: "read", "write", "destructive" com --scope CLI
  - Tools composiveis — importaveis em MCP servers customizados
  - PRs automaticos para SDKs existentes
- **Gaps que cobre:** 2 (customizados — parcial, foco em API specs)
- **Relevancia Triforce:** ALTA — pipeline spec-driven para integrações (Hotmart, WhatsApp)

#### Gram — speakeasy-api/gram
- **URL:** https://github.com/speakeasy-api/gram
- **O que faz:** Plataforma de criacao, curadoria e hosting de MCP servers
- **Features:**
  - Framework TypeScript de alto nivel
  - OpenAPI 3.0.x e 3.1.x first-class
  - Tool composition (higher-order tools via chaining)
  - OAuth + DCR built-in
  - Hosting em dominio custom (mcp.empresa.com)
  - Control plane organizacional para agents/MCP/skills
- **Gaps que cobre:** 2 (customizados), 8 (seguranca, governance)
- **Relevancia Triforce:** MEDIA — mais enterprise, avaliar custo

### 2.4 Plataformas de Deploy

#### Cloudflare Workers + Agents SDK
- **URL:** https://developers.cloudflare.com/agents/guides/remote-mcp-server/
- **URL workers-mcp:** https://github.com/cloudflare/workers-mcp
- **O que faz:** Deploy de MCP servers remotos na edge Cloudflare
- **Patterns:**
  - `createMcpHandler()` — stateless, sem Durable Objects
  - `McpAgent` — stateful com Durable Objects
  - Raw WebStandardStreamableHTTPServerTransport — controle total
- **Auth:** Cloudflare Access (IdPs), GitHub OAuth, Auth0, Stytch, WorkOS
- **Deploy:** `npm create cloudflare@latest -- my-server --template=cloudflare/ai/demos/remote-mcp-authless`
- **Code Mode:** 2.500+ endpoints colapsados em 2 tools (~1.000 tokens)
- **Gaps que cobre:** 3 (stack Cloudflare), 4 (transports), 6 (Edge), 8 (seguranca)
- **Relevancia Triforce:** ALTA — Cloudflare esta na stack

#### Vercel MCP Adapter (@vercel/mcp-adapter)
- **URL:** https://github.com/vercel/mcp-adapter
- **NPM:** @vercel/mcp-adapter
- **Template:** https://vercel.com/templates/next.js/model-context-protocol-mcp-with-next-js
- **O que faz:** Wraps MCP servers em Next.js API routes
- **Features:**
  - Streamable HTTP com cold start handling
  - OAuth 2.1 built-in
  - Deploy zero-ops na Vercel
  - Suporte Next.js, Nuxt, Svelte
- **Gaps que cobre:** 3 (stack Vercel), 4 (transports), 8 (seguranca)
- **Relevancia Triforce:** ALTA — Vercel esta na stack, Next.js 15

#### Supabase Edge Functions
- **URL deploy:** https://supabase.com/docs/guides/getting-started/byo-mcp
- **URL mcp-lite:** https://blog.fiberplane.com/blog/mcp-lite-supabase-edge-functions/
- **URL handler:** https://jsr.io/@rodriguespn/supabase-mcp-handler
- **O que faz:** Deploy de MCP servers em Edge Functions Deno
- **Opcoes:**
  - SDK oficial + WebStandardStreamableHTTPServerTransport + Hono
  - mcp-lite (zero-dependency, Zod, Hono) — mais leve
  - @rodriguespn/supabase-mcp-handler — turnkey com createEdgeMCPServer()
- **Deploy:** `supabase functions deploy --no-verify-jwt mcp`
- **Endpoint:** `https://<ref>.supabase.co/functions/v1/mcp`
- **Gaps que cobre:** 3 (stack Supabase), 6 (Edge/Deno 2.1)
- **Relevancia Triforce:** ALTA — Supabase esta na stack

### 2.5 MCP Servers Pre-Construidos (Stack Triforce)

#### Supabase MCP Server (oficial)
- **URL:** https://github.com/supabase-community/supabase-mcp
- **Blog:** https://supabase.com/blog/mcp-server
- **Remote:** https://supabase.com/blog/remote-mcp-server
- **O que faz:** Conecta AI tools ao Supabase — SQL, schemas, edge functions, auth, storage
- **Features:** Claude connector oficial, OAuth2 (MCP auth), local + remote
- **Relevancia Triforce:** JA INSTALADO no Claude Code (verificar config)

#### Airtable MCP Server (oficial)
- **URL oficial:** https://support.airtable.com/docs/using-the-airtable-mcp-server
- **URL domdomegg:** https://github.com/domdomegg/airtable-mcp-server
- **URL felores:** https://github.com/felores/airtable-mcp
- **Docker:** mcp/airtable-mcp-server
- **O que faz:** Leitura/escrita em Airtable bases via MCP
- **Relevancia Triforce:** JA DISPONIVEL — Gabriel quer encapsular rate limiting em cima

#### Cloudflare MCP Servers (oficiais)
- **URL:** https://developers.cloudflare.com/agents/model-context-protocol/mcp-servers-for-cloudflare/
- **O que faz:** Gerenciamento de Workers, D1, KV, R2, Hyperdrive via MCP
- **Relevancia Triforce:** JA INSTALADO no Claude Code

### 2.6 Ferramentas de Teste e Debug

#### MCP Inspector
- **Comando:** `npx -y @modelcontextprotocol/inspector`
- **O que faz:** Debug visual interativo de qualquer MCP server
- **Relevancia:** CRITICA para desenvolvimento

#### mcp-proxy
- **URL:** https://github.com/sparfenyuk/mcp-proxy
- **O que faz:** Bridge entre Streamable HTTP e stdio — compatibilidade com clients antigos
- **Relevancia:** UTIL para deploy hibrido

### 2.7 Recursos de Referencia

#### MCP Spec 2025-06-18
- **URL:** https://modelcontextprotocol.io/specification/2025-06-18
- **Transports:** https://modelcontextprotocol.io/specification/2025-06-18/basic/transports
- **Lifecycle:** https://modelcontextprotocol.io/specification/2025-03-26/basic/lifecycle
- **Security:** https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices

#### MCP Cheat Sheet 2026
- **URL:** https://www.webfuse.com/mcp-cheat-sheet
- **O que cobre:** Arquitetura, primitives, transports, SDK quick starts, seguranca, ecossistema

#### MCP Server Dev Guide (cyanheads)
- **URL:** https://github.com/cyanheads/model-context-protocol-resources/blob/main/guides/mcp-server-development-guide.md
- **O que cobre:** Project structure, testing, error handling, security, deployment checklist completo

#### Guides de Construcao
- **FreeCodeCamp:** https://www.freecodecamp.org/news/how-to-build-a-custom-mcp-server-with-typescript-a-handbook-for-developers/
- **Noqta 2026:** https://noqta.tn/en/tutorials/build-mcp-server-typescript-2026
- **Thomas Wiegold:** https://thomas-wiegold.com/blog/how-to-build-mcp-server/
- **Agentailor (completo):** https://blog.agentailor.com/posts/mcp-typescript-sdk-complete-guide
- **Context Studios 2026:** https://www.contextstudios.ai/it/guides/mcp-integration-development-guide-2026

#### MCP Protocol Deep (llms.txt)
- **URL:** https://modelcontextprotocol.io/llms-full.txt

---

## 3. MAPA: COMPETENCIA / GAP -> COBERTURA

| # | Gap Identificado | Cobertura | Fonte Principal | Status |
|---|-----------------|-----------|-----------------|--------|
| 1 | MCP servers em TypeScript (SDK oficial) | COBERTO | @modelcontextprotocol/sdk + FastMCP + MCP Framework | Skill local cobre ~40%, SDK + FastMCP completam |
| 2 | MCPs customizados do zero | COBERTO | MCP Builder skill (ComposioHQ) + FastMCP + cyanheads guide | 4 fases estruturadas, patterns agent-centric |
| 3 | Stack Triforce (Supabase, Airtable, Vercel, Cloudflare) | COBERTO | MCP servers oficiais + deploy guides por plataforma | Supabase Edge, Vercel Adapter, CF Workers |
| 4 | Protocolo MCP profundo (transports, lifecycle, JSON-RPC) | COBERTO | MCP Spec 2025-06-18 + Cheat Sheet + cyanheads guide | Transports comparados, lifecycle state machine |
| 5 | Integracao Zod (schemas tipados) | COBERTO | SDK oficial (Standard Schema) + FastMCP + MCP Builder | Zod v4 nativo em todos os frameworks |
| 6 | Edge Functions Deno 2.1 | COBERTO | Supabase BYO-MCP + mcp-lite + supabase-mcp-handler | 3 opcoes de deploy Edge |
| 7 | Padroes de documentacao (changelog, schema docs) | PARCIAL | MCP Builder (evaluations) + cyanheads (checklist) | Falta template de changelog/versioning especifico |
| 8 | Seguranca (auth, sandboxing, rate limiting) | COBERTO | MCP Spec security + OAuth 2.1 guides + Gram + CF Access | OAuth 2.1, PKCE, rate limiting, sandboxing |

### Gaps Adicionais Detectados na Pesquisa

| # | Gap Novo | Status | Fonte |
|---|----------|--------|-------|
| 9 | Hotmart API MCP Server | SEM COBERTURA | Nenhum MCP server existe — construir do zero via webhook/API |
| 10 | WhatsApp Cloud API MCP Server | SEM COBERTURA | Nenhum MCP server oficial — construir do zero |
| 11 | Rate limiting Airtable + fila + retry/idempotencia | PARCIAL | Patterns genericos existem, MCP especifico nao |
| 12 | MCP Gateway / control plane organizacional | PARCIAL | Gram (Speakeasy) cobre, avaliar custo vs build proprio |

---

## 4. INTEGRAÇÕES ESPECIFICAS TRIFORCE (sem MCP existente)

### 4.1 Hotmart
- **API:** REST, webhook postback para eventos de transacao
- **Docs:** https://help.hotmart.com/pt-br/article/360001491352
- **Status MCP:** INEXISTENTE — sera o primeiro MCP server customizado a criar
- **Approach:** Usar Speakeasy (se OpenAPI spec disponivel) ou FastMCP do zero
- **Webhooks:** Eventos de compra, cancelamento, reembolso, assinatura

### 4.2 WhatsApp Cloud API (Meta)
- **API:** REST + Webhooks
- **Docs:** https://developers.facebook.com/docs/whatsapp/cloud-api
- **Status MCP:** INEXISTENTE publicamente
- **Approach:** FastMCP + Zod schemas, deploy em Supabase Edge ou CF Workers
- **Webhooks:** Messages, status updates, templates

### 4.3 Rate Limiting Airtable (demanda Gabriel)
- **Problema:** Airtable rate limit 5 req/s, precisa fila + retry + idempotencia
- **Patterns encontrados:**
  - Token bucket / sliding window keyed por tool + token
  - Exponential backoff com jitter
  - Idempotency keys por request
  - Dead-letter queue para falhas
- **Approach:** Encapsular no MCP server Airtable customizado sobre o oficial

---

## 5. PATTERNS EXTRAIDOS (frameworks reutilizaveis)

### 5.1 Arquitetura Padrao de MCP Server

```
project/
  src/
    server.ts          # McpServer instance + tool/resource/prompt registration
    tools/
      toolA.ts         # Tool handler + Zod schema
      toolB.ts
    resources/
      resourceA.ts
    prompts/
      promptA.ts
    lib/
      api-client.ts    # HTTP client com retry/rate-limit
      auth.ts          # OAuth 2.1 validation
      errors.ts        # Error formatting
      schemas.ts       # Shared Zod schemas
  transports/
    stdio.ts           # Entry point stdio
    http.ts            # Entry point Streamable HTTP
  tests/
    tools.test.ts
    evaluations.xml    # 10 questoes de avaliacao
  package.json
  tsconfig.json
```

### 5.2 Pattern: Tool Registration (SDK Oficial + Zod)

```typescript
import { McpServer } from '@modelcontextprotocol/sdk/server/mcp.js';
import { z } from 'zod';

const server = new McpServer({ name: 'triforce-mcp', version: '1.0.0' });

const InputSchema = z.object({
  query: z.string().min(1).max(10_000).describe('Search query'),
  limit: z.number().int().min(1).max(100).default(10).describe('Max results'),
});

server.registerTool('search', {
  title: 'Search Records',
  description: 'Search records in the database',
  inputSchema: InputSchema,
  annotations: { readOnlyHint: true, openWorldHint: false },
}, async (input) => {
  const parsed = InputSchema.parse(input);
  const results = await apiClient.search(parsed.query, parsed.limit);
  return {
    content: [{ type: 'text', text: JSON.stringify(results) }],
  };
});
```

### 5.3 Pattern: Rate Limiting Wrapper

```typescript
class RateLimiter {
  private queue: Array<() => Promise<void>> = [];
  private running = 0;
  private readonly maxConcurrent: number;
  private readonly intervalMs: number;

  async execute<T>(fn: () => Promise<T>): Promise<T> {
    // Token bucket + exponential backoff com jitter
    // Idempotency key por request
    // Dead-letter apos N retries
  }
}
```

### 5.4 Pattern: Deploy Multi-Plataforma

| Plataforma | Transport | Auth | Comando Deploy |
|-----------|-----------|------|----------------|
| Local/CLI | stdio | N/A | `node dist/stdio.js` |
| Vercel | Streamable HTTP | OAuth 2.1 | `vercel deploy` + @vercel/mcp-adapter |
| Cloudflare | Streamable HTTP | CF Access / OAuth | `wrangler deploy` |
| Supabase Edge | Streamable HTTP | JWT (futuro OAuth) | `supabase functions deploy` |

### 5.5 Pattern: Lifecycle Correto

```
1. Client -> initialize request (protocolVersion, capabilities, clientInfo)
2. Server -> initialize response (protocolVersion, capabilities, serverInfo)
3. Client -> initialized notification
4. [Operation phase - tools/resources/prompts calls]
5. Shutdown: stdio=close stdin+SIGTERM | HTTP=DELETE session
```

Regras:
- Rejeitar tudo exceto `initialize` antes de `initialized`
- `initialize` NAO pode estar em batch JSON-RPC
- Manter state machine: pendingInit > ready > closed

---

## 6. SEGURANCA — CHECKLIST CONSOLIDADO

- [ ] HTTPS obrigatorio para endpoints remotos (exceto loopback dev)
- [ ] OAuth 2.1 com PKCE para clients publicos
- [ ] Bearer token validation em cada request (issuer, audience, expiry, scopes)
- [ ] MCP-specific scopes (ex: mcp:read:crm, mcp:write:tickets)
- [ ] Rate limiting por tenant + tool (sliding window ou token bucket)
- [ ] Input validation Zod em TODOS os parametros (nunca confiar em params)
- [ ] Bloqueio de IPs privados/reservados (anti-SSRF)
- [ ] Secrets via env vars ou vault (nunca em parametros de tool)
- [ ] Container/edge sandbox com filesystem minimo
- [ ] DNS rebinding protection para servers locais
- [ ] Refresh token rotation para clients publicos
- [ ] Logging de seguranca sem exposicao de dados sensiveis

---

## 7. DECISOES RECOMENDADAS PARA O CARGO

### Stack de Desenvolvimento MCP
1. **SDK base:** @modelcontextprotocol/sdk (TypeScript) — obrigatorio
2. **Framework produtivo:** FastMCP (punkpeye) — para MCPs simples/medios
3. **Scaffold:** MCP Framework CLI (`mcp create`) — para projetos novos
4. **Spec-driven:** Speakeasy — para APIs com OpenAPI spec (Hotmart se tiver)
5. **Schemas:** Zod v4 — em todos os servers
6. **Teste:** MCP Inspector + evaluations XML

### Deploy por Contexto
- **Interno/dev:** stdio
- **Producao Vercel:** @vercel/mcp-adapter + Next.js route
- **Producao Supabase:** Edge Functions + mcp-lite ou SDK oficial
- **Producao Cloudflare:** Workers + McpAgent (stateful) ou createMcpHandler (stateless)

### Prioridade de Construcao (primeiros MCPs)
1. Airtable customizado (rate limiting + fila + retry) — demanda Gabriel
2. Hotmart MCP Server — demanda Felipe, sem solucao existente
3. WhatsApp Cloud API MCP Server — demanda Felipe, sem solucao existente
4. MCPs internos Triforce (workflows customizados) — demanda Andre

---

## 8. FONTES E MARKETPLACES

### Marketplaces de Skills
- https://claudeskills.info/skills/
- https://claudemarketplaces.com
- https://github.com/ComposioHQ/awesome-claude-skills
- https://github.com/daymade/claude-code-skills
- https://mcpmarket.com

### Marketplaces de MCP Servers
- https://mcpmarket.com
- https://www.pulsemcp.com
- https://mcp.directory
- https://lobehub.com/mcp
- https://hub.docker.com (mcp/ namespace)

### Documentacao Oficial
- Spec: https://modelcontextprotocol.io/specification/2025-06-18
- TS SDK Docs: https://ts.sdk.modelcontextprotocol.io
- Security: https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices
- Protocol full (llms.txt): https://modelcontextprotocol.io/llms-full.txt
- Anthropic guide: https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf
