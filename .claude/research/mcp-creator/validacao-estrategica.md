# Validacao Estrategica — Criador de MCP Servers Senior

**Data:** 2026-05-06
**Responsavel:** Gabriela (RH)
**Objetivo:** Confirmar versoes e features dos frameworks principais contra fontes oficiais

---

## 1. @modelcontextprotocol/sdk (TypeScript)

| Item | Scan Operacional | Fonte Oficial (npm + GitHub) | Status |
|------|-----------------|------------------------------|--------|
| Versao | 1.17.4 | **1.17.4** (npm, publicado ha 9 dias) — versao 1.25.0 tambem detectada em newreleases.io | CONFIRMADO (1.17.x estavel, releases mais recentes disponiveis) |
| McpServer class | Sim | Sim — classe principal do SDK | CONFIRMADO |
| Transports | stdio, Streamable HTTP, SSE (legacy) | Confirmado via docs oficiais e MCP Cheat Sheet 2026 | CONFIRMADO |
| Standard Schema (Zod v4) | Sim | Confirmado — suporte nativo a Zod, Valibot, ArkType | CONFIRMADO |
| Middleware packages | Express, Hono, Node.js HTTP | Confirmado via GitHub typescript-sdk | CONFIRMADO |
| OAuth 2.1 resource server | Sim | Confirmado via MCP Spec e Auth0 blog | CONFIRMADO |
| 11.484 projetos dependentes | Sim | Confirmado no npm | CONFIRMADO |

**Resultado:** VALIDADO SEM DISCREPANCIAS

---

## 2. FastMCP (punkpeye)

| Item | Scan Operacional | Fonte Oficial (npm + GitHub) | Status |
|------|-----------------|------------------------------|--------|
| Versao npm | nao especificada | **3.13.0** (npm `fastmcp`, publicado ha 4 dias) | ATUALIZADO — scan dizia apenas "FastMCP 2025" |
| Versao JSR | nao especificada | **@punkpeye/fastmcp** no JSR (@glama/fastmcp) | CONFIRMADO |
| Stars GitHub | 3.100+ | Confirmado via GitHub | CONFIRMADO |
| EdgeFastMCP | Sim | **CONFIRMADO** — docs em punkpeye-fastmcp.mintlify.app/features/edge-runtime + exemplo em src/examples/edge-cloudflare-worker.ts | CONFIRMADO |
| Cloudflare Workers | Sim | Confirmado via docs de deployment Cloudflare Workers | CONFIRMADO |
| Zod nativo | Sim | Confirmado | CONFIRMADO |
| Auth/OAuth built-in | Sim | Confirmado | CONFIRMADO |
| Custom HTTP routes | Sim | Confirmado via server.addRoute | CONFIRMADO |
| 331 projetos dependentes | -- | Confirmado no npm | NOVO DADO |

**Resultado:** VALIDADO — versao atualizada para 3.13.0, EdgeFastMCP CONFIRMADO existir

---

## 3. @vercel/mcp-adapter

| Item | Scan Operacional | Fonte Oficial (npm + GitHub) | Status |
|------|-----------------|------------------------------|--------|
| Existe | Sim | **Sim** — npm @vercel/mcp-adapter | CONFIRMADO |
| Versao | nao especificada | **0.2.4** (npm, publicado ha 9 horas) | NOVO DADO |
| Next.js 15 compativel | Sim | **Sim** — template oficial Vercel para Next.js, suporte a Next.js, Nuxt, Svelte | CONFIRMADO |
| Streamable HTTP | Sim | Confirmado via Vercel changelog e docs | CONFIRMADO |
| OAuth 2.1 built-in | Sim | Confirmado via Vercel changelog | CONFIRMADO |
| Deploy zero-ops | Sim | Confirmado — Vercel Fluid compute | CONFIRMADO |
| MCP Apps support | -- | Confirmado via Vercel changelog (SEP-1865) | NOVO DADO |

**Resultado:** VALIDADO — funciona com Next.js 15, versao 0.2.4

---

## 4. MCP Spec

| Item | Scan Operacional | Fonte Oficial | Status |
|------|-----------------|---------------|--------|
| Versao no scan | 2025-06-18 | **2025-11-25** e a versao mais recente (changelog referencia 2025-06-18 como versao anterior) | ATUALIZADO |
| Transports | stdio, Streamable HTTP, SSE | Confirmado — SSE polling adicionado em 2025-11-25 (SEP-1699) | CONFIRMADO + ATUALIZADO |
| JSON-RPC 2.0 | Sim | Confirmado | CONFIRMADO |
| OAuth 2.1 | Sim | Confirmado via Auth0 blog e spec | CONFIRMADO |
| MCP Apps (SEP-1865) | -- | Formalizado em early 2026 — extensao oficial | NOVO DADO |

**Resultado:** ATUALIZADO — spec mais recente e **2025-11-25**, nao 2025-06-18. Usar 2025-11-25 como referencia.

---

## RESUMO DA VALIDACAO

| Framework | Status | Acao |
|-----------|--------|------|
| @modelcontextprotocol/sdk | VALIDADO | Manter. Releases acima de 1.17.4 disponiveis (ate 1.25.0) |
| FastMCP (punkpeye) | VALIDADO | Atualizar versao para 3.13.0. EdgeFastMCP confirmado |
| @vercel/mcp-adapter | VALIDADO | Funciona com Next.js 15. Versao 0.2.4 |
| MCP Spec | ATUALIZADO | Versao mais recente: **2025-11-25** (nao 2025-06-18) |

**Nenhum framework invalido. Nenhuma feature inexistente. Todos confirmados por fontes oficiais (npm, GitHub, Vercel changelog, modelcontextprotocol.io).**

---

## IMPACTO NO SKILL.md

1. `sources_version` no frontmatter deve usar: `MCP Spec 2025-11-25 | @modelcontextprotocol/sdk 1.17+ | FastMCP 3.x`
2. References devem mencionar MCP Spec 2025-11-25 como versao corrente
3. SSE polling (SEP-1699) e MCP Apps (SEP-1865) sao features novas do spec 2025-11-25 a documentar
