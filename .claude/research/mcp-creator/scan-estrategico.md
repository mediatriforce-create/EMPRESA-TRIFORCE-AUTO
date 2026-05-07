# Scan Estratégico - Criador de MCP Servers Senior

**Data:** 2026-05-06
**Responsável:** Gabriela (RH)
**Objetivo:** Conhecimento estratégico para os 5 gaps remanescentes do scan operacional

---

## GAPS PESQUISADOS

| # | Gap | Status Final |
|---|-----|-------------|
| 1 | Template de changelog/versioning para MCP Servers | COBERTO |
| 2 | Hotmart API (endpoints, webhooks, auth, rate limits) | COBERTO |
| 3 | WhatsApp Cloud API (endpoints, webhooks, auth, rate limits) | COBERTO |
| 4 | Rate limiting Airtable encapsulado em MCP (fila, retry, idempotência, dead-letter) | COBERTO |
| 5 | MCP server lifecycle management em produção (monitoring, versioning, deprecation) | COBERTO |

---

## 1. TEMPLATE DE CHANGELOG/VERSIONING PARA MCP SERVERS

### 1.1 Semver para MCP Servers

- **Padrão:** MAJOR.MINOR.PATCH (Semantic Versioning standard)
- **MAJOR:** breaking changes em tool schemas, alteração de auth model, remoção de tools
- **MINOR:** novos tools adicionados, campos opcionais em schemas existentes, features aditivas
- **PATCH:** bug fixes, melhorias de performance, ajustes de descrições
- **Alinhamento:** versão do server deve alinhar com versão do package no `server.json`
- **URL:** https://modelcontextprotocol.io/registry/versioning

### 1.2 Handling Breaking Changes em Tool Schemas

| Regra | Descrição |
|-------|-----------|
| Nunca renomear tool existente | Criar novo tool ID (ex: `process_data_v2`) |
| Nunca modificar parâmetros required in-place | Adicionar novo tool com schema atualizado |
| Test fixtures de regressão | Manter replay de chamadas com schemas de versões anteriores |
| Version negotiation | Permitir clients negociarem versão compatível (nunca rejeitar outright) |

### 1.3 Workflow de Deprecação de Tools

```
Passo 1: Atualizar description do tool deprecated
         → Instruir o LLM a usar o novo tool na description
Passo 2: Manter tool legado funcional (período de transição)
Passo 3: Documentar migration path explícito
Passo 4: Remover tool + emitir notifications/tools/list_changed
         → Clients reconectam automaticamente sem restart
```

### 1.4 Template de Changelog Recomendado

**Formato:** Keep a Changelog + Conventional Commits
**Automação:** `semantic-release` ou `git-cliff` no CI/CD

```markdown
# Changelog - [nome-do-mcp-server]

## [2.0.0] - 2026-05-06

### Breaking Changes
- **REMOVED** `search_records` tool (use `query_records_v2`)
- **CHANGED** `create_record` now requires `idempotency_key` parameter

### Tool Contracts
- **ADDED** `query_records_v2` — novo tool com paginação cursor-based
- **DEPRECATED** `search_records` — será removido em v3.0.0
- **SCHEMA** `update_record`: campo `metadata` agora aceita nested objects

### Protocol
- Atualizado para MCP spec 2025-11-25 (Streamable HTTP obrigatório)

### Fixes
- Corrigido timeout em chamadas com payload > 1MB

## [1.2.0] - 2026-04-15

### Added
- **NEW TOOL** `batch_update` — atualização em lote com idempotência
- **NEW RESOURCE** `schema://tables` — lista schemas disponíveis

### Changed
- `list_records`: adicionado parâmetro opcional `cursor` para paginação
```

### 1.5 Frameworks/Ferramentas para Automação

| Ferramenta | URL | O que faz |
|-----------|-----|-----------|
| semantic-release | https://github.com/semantic-release/semantic-release | Automação de versioning + changelog via Conventional Commits |
| git-cliff | https://github.com/orhun/git-cliff | Gerador de changelog customizável |
| Changelog Automation Skill | https://mcpmarket.com/tools/skills/changelog-release-automation-3 | Skill Claude Code para automação de releases |
| Changerawr MCP Server | https://mcpservers.org/servers/Changerawr/mcp-server | MCP server dedicado a gestão de changelogs |
| Keep a Changelog spec | https://keepachangelog.com | Formato padrão de changelog |

### 1.6 Referências Adicionais

- **MCP Versioning Guide:** https://www.byteplus.com/en/topic/542091
- **MCP Backward Compatibility:** https://chatforest.com/guides/mcp-versioning-backward-compatibility/
- **Breaking Changes Case Study:** https://scottefein.github.io/mcp-versioning/
- **Tool Versioning Discussion (spec):** https://github.com/modelcontextprotocol/modelcontextprotocol/issues/1039
- **MCP Best Practices (lirantal):** https://github.com/lirantal/awesome-mcp-best-practices

### Adaptável ao contexto Triforce?
**SIM** - Aplicação direta. O template de changelog cobre exatamente o gap 7 (parcial) do scan operacional. Recomendação: adotar Conventional Commits + semantic-release no pipeline GitHub Actions de cada MCP server.

---

## 2. HOTMART API - REFERÊNCIA COMPLETA PARA CONSTRUÇÃO DE MCP

### 2.1 Visão Geral

| Item | Valor |
|------|-------|
| Base URL | `https://developers.hotmart.com/` |
| Auth | OAuth 2.0 `client_credentials` |
| Rate Limit | **500 requests/minuto** (leitura + escrita combinados) |
| Sandbox | Disponível com credenciais dedicadas |
| Docs Portal | https://developers.hotmart.com/docs/en/ |
| Changelog | https://developers.hotmart.com/docs/en/changelog |

### 2.2 Autenticação

```
POST https://developers.hotmart.com/security/oauth/token
Headers:
  Authorization: Basic <base64(client_id:client_secret)>
  Content-Type: application/json
Body:
  grant_type=client_credentials
Response:
  { "access_token": "...", "token_type": "bearer", "expires_in": 3600 }
```

- Grant type: `client_credentials` (server-to-server)
- Token expira em ~1h, requer refresh automático
- Para apps multi-produtor: usar `user_auth` flow (OAuth Authorization Code)
- Docs auth: https://developers.hotmart.com/docs/en/start/app-auth/
- Docs user auth: https://developers.hotmart.com/docs/pt-BR/start/user-auth/

### 2.3 REST API Endpoints

| Módulo | Endpoints Principais | Dados |
|--------|---------------------|-------|
| **Sales API** | `/sales/history`, `/sales/users`, `/sales/price-details`, `/sales/commissions` | Histórico de vendas, participantes (buyer, affiliate, creator, co-creator), breakdown de preço, comissões, impostos |
| **Subscriptions API** | `/subscriptions/purchases`, `/subscriptions/cancel`, `/subscriptions/reactivate`, `/subscriptions/change-billing-date` | Gerenciamento de assinaturas, cancelamento, reativação, alteração de data de cobrança |
| **Members Area API** | `/club/modules`, `/club/pages`, `/club/students`, `/club/progress` | Módulos de curso, páginas, alunos matriculados, progresso do aluno |
| **Product API** | `/product/plans` | Planos de produto (preço, periodicidade, opções de pagamento, parcelamento) |

**Docs endpoints:**
- Sales History: https://developers.hotmart.com/docs/en/v1/sales/sales-history/
- Sales Participants: https://developers.hotmart.com/docs/en/v1/sales/sales-users/
- Price Breakdown: https://developers.hotmart.com/docs/en/v1/sales/sales-price-details/
- Product Plans: https://developers.hotmart.com/docs/en/v1/product/product-plans
- Best Practices: https://developers.hotmart.com/docs/en/tutorials/learn-good-usage-practices/

### 2.4 Rate Limits

| Limite | Valor |
|--------|-------|
| Requests/minuto | 500 (leitura + escrita combinados) |
| Histórico | Era 100/min, aumentado 5x em 2025 |
| Recomendação | Usar filtros de data + paginação para otimizar |
| Docs | https://developers.hotmart.com/docs/en/start/rate-limit/ |

### 2.5 Webhook Postback Events

| Evento | Descrição |
|--------|-----------|
| `PURCHASE_APPROVED` | Compra aprovada |
| `PURCHASE_COMPLETE` | Compra completada |
| `PURCHASE_REFUNDED` | Compra reembolsada |
| `PURCHASE_CANCELED` | Compra cancelada |
| `PURCHASE_OVERDUE` | Pagamento vencido |
| `AWAITING_PAYMENT` | Aguardando pagamento |
| `PURCHASE_CHARGEBACK` | Chargeback |
| `REFUND_REQUEST` | Solicitação de reembolso |
| `SUBSCRIPTION_CANCELLATION` | Cancelamento de assinatura |
| `PLAN_CHANGE` | Mudança de plano |
| `CART_ABANDONMENT` | Carrinho abandonado |

**Configuração:** Hotmart Tools > Webhooks > URL + Token (hottok)
**Versão webhook:** 2.0.0 (recomendada)
**Docs:** https://help.hotmart.com/pt-br/article/360001491352

### 2.6 Design do MCP Server Hotmart (Recomendação)

```
Tools recomendados:
  - hotmart_get_sales_history    (readOnly, paginado)
  - hotmart_get_sale_details     (readOnly)
  - hotmart_get_sale_participants (readOnly)
  - hotmart_get_subscriptions    (readOnly)
  - hotmart_cancel_subscription  (destructive)
  - hotmart_get_students         (readOnly)
  - hotmart_get_student_progress (readOnly)
  - hotmart_get_product_plans    (readOnly)

Resources recomendados:
  - hotmart://webhook-events     (lista de eventos disponíveis)
  - hotmart://rate-limits        (status atual de rate limit)

Framework: FastMCP + Zod
Deploy: Supabase Edge Functions ou Cloudflare Workers
Rate limit interno: 8 req/s (buffer de segurança para 500/min = ~8.3/s)
Auth: OAuth 2.0 client_credentials com refresh automático
```

### 2.7 Referências Adicionais

- **Rollout Integration Guide:** https://rollout.com/integration-guides/hotmart
- **Pipedream Hotmart:** https://pipedream.com/apps/hotmart
- **Make Hotmart App:** https://apps.make.com/hotmart
- **Python SDK (referência):** https://pypi.org/project/hotmart-python/
- **Postman collection (community):** https://github.com/adrianomigani/hotmart_api

### Adaptável ao contexto Triforce?
**SIM** - Demanda direta do Felipe. Nenhum MCP server Hotmart existe no mercado. A API é REST simples com OAuth 2.0, perfeita para FastMCP + Zod. Rate limit de 500/min é generoso. Prioridade alta de construção.

---

## 3. WHATSAPP CLOUD API - REFERÊNCIA COMPLETA PARA CONSTRUÇÃO DE MCP

### 3.1 Visão Geral

| Item | Valor |
|------|-------|
| Base URL | `https://graph.facebook.com/v{VERSION}/` (ex: v21.0) |
| Auth | System User Access Token (permanente) |
| Throughput | ~80 msgs/s por número (upgradeable até 1.000 mps) |
| Messaging Limits | Tiers: 250 → 1K → 10K → 100K → Unlimited (24h rolling) |
| Docs Portal | https://developers.facebook.com/documentation/business-messaging/whatsapp/ |

### 3.2 Autenticação

```
1. Criar System User (Admin) em Business Settings
2. Gerar Permanent Access Token para o System User
3. Atribuir assets (App, WABA, Phone Number)
4. Permissions necessárias:
   - whatsapp_business_messaging
   - whatsapp_business_management
   - business_management (opcional)

Header em todas as requests:
  Authorization: Bearer <PERMANENT_ACCESS_TOKEN>
```

**Docs:** https://developers.facebook.com/documentation/business-messaging/whatsapp/get-started

### 3.3 REST API Endpoints

| Endpoint | Método | Função |
|----------|--------|--------|
| `/{PHONE_NUMBER_ID}/messages` | POST | Enviar texto, mídia, localização, contatos, interativos, templates |
| `/{PHONE_NUMBER_ID}/messages` | POST | Marcar mensagem como lida (status: read) |
| `/{PHONE_NUMBER_ID}/media` | POST | Upload de mídia para envio posterior |
| `/{MEDIA_ID}` | GET | Download de mídia recebida |
| `/{PHONE_NUMBER_ID}` | GET | Info do número de telefone |
| `/{WABA_ID}/message_templates` | GET | Listar templates aprovados |
| `/{WABA_ID}/message_templates` | POST | Criar template para aprovação |
| `/{PHONE_NUMBER_ID}/whatsapp_business_profile` | GET/PATCH | Ler/atualizar perfil comercial |
| `/{WABA_ID}/phone_numbers` | GET | Listar números vinculados à WABA |
| `/{PHONE_NUMBER_ID}/register` | POST | Registrar número (messaging_product + PIN 2FA) |

### 3.4 Webhook Events

**Setup:** GET (verification handshake com hub.challenge) + POST (event delivery)
**Validação:** `X-Hub-Signature-256` (HMAC SHA-256)
**Resposta:** HTTP 200 rápido (evitar timeout)

| Evento | Dados |
|--------|-------|
| `messages` | Mensagens recebidas (text, image, audio, video, document, location, contacts, interactive) |
| `statuses` (dentro de messages) | Status: `sent`, `delivered`, `read`, `failed` + conversation/pricing metadata |
| `message_template_status_update` | Status do template: `APPROVED`, `REJECTED`, `PENDING`, `DISABLED`, `PAUSED`, `LIMIT_EXCEEDED` |

**Docs webhooks:** https://hookdeck.com/webhooks/platforms/guide-to-whatsapp-webhooks-features-and-best-practices

### 3.5 Message Templates

| Categoria | Uso |
|-----------|-----|
| **Marketing** | Promoções, ofertas, newsletters |
| **Utility** | Confirmações de pedido, atualizações de entrega, notificações |
| **Authentication** | OTP, verificação de conta |

**Regra:** Fora da janela de 24h, apenas templates aprovados podem ser enviados.
**Dentro da janela de 24h:** mensagens livres (session messages) incluindo interativos.

### 3.6 Mensagens Interativas

| Tipo | Limite |
|------|--------|
| Reply Buttons | Até 3 botões |
| Lists | Até 10 itens selecionáveis (com seções) |
| Catalog Message | Catálogo de produtos |
| Product | Produto individual |
| Product List | Lista de produtos |
| Flow | WhatsApp Flows (formulários interativos) |

### 3.7 Rate Limits e Tiers

| Tier | Limite de Conversas (24h rolling) | Requisito |
|------|----------------------------------|-----------|
| Tier 0 | ~250 conversas únicas | Número novo/não verificado |
| Tier 1 | 1.000 | Negócio verificado |
| Tier 2 | 10.000 | Quality rating + volume |
| Tier 3 | 100.000 | Quality rating + volume |
| Unlimited | Sem limite | Quality rating + volume consistente |

| Throughput | Valor |
|-----------|-------|
| Default | ~80 msgs/s por número |
| Upgrade | Até 1.000 mps (contas elegíveis) |

### 3.8 Design do MCP Server WhatsApp (Recomendação)

```
Tools recomendados:
  - whatsapp_send_text          (não-destrutivo, idempotente)
  - whatsapp_send_template      (não-destrutivo)
  - whatsapp_send_media         (não-destrutivo)
  - whatsapp_send_interactive   (não-destrutivo — buttons, lists)
  - whatsapp_mark_as_read       (não-destrutivo, idempotente)
  - whatsapp_upload_media       (não-destrutivo)
  - whatsapp_download_media     (readOnly)
  - whatsapp_list_templates     (readOnly)
  - whatsapp_create_template    (não-destrutivo)
  - whatsapp_get_business_profile (readOnly)
  - whatsapp_update_business_profile (não-destrutivo)

Resources recomendados:
  - whatsapp://phone-numbers    (números vinculados)
  - whatsapp://messaging-limits (tier atual + throughput)
  - whatsapp://template-status  (status dos templates)

Framework: FastMCP + Zod
Deploy: Supabase Edge Functions ou Cloudflare Workers
Auth: Bearer token permanente (System User)
Webhook receiver: endpoint separado para receber eventos
```

### 3.9 Referências Adicionais

- **Meta Official Docs:** https://developers.facebook.com/documentation/business-messaging/whatsapp/
- **Postman Collection:** https://www.postman.com/meta/whatsapp-business-platform/collection/wlk6lh4/whatsapp-cloud-api
- **Node.js SDK (Meta):** https://whatsapp.github.io/WhatsApp-Nodejs-SDK/
- **DevOpsSchool Guide:** https://www.devopsschool.com/blog/whatsapp-cloud-api-direct-integration-with-meta/
- **GuruSup Guide 2026:** https://gurusup.com/blog/whatsapp-cloud-api
- **Hookdeck Webhooks Guide:** https://hookdeck.com/webhooks/platforms/guide-to-whatsapp-webhooks-features-and-best-practices

### Adaptável ao contexto Triforce?
**SIM** - Demanda direta do Felipe. Nenhum MCP server WhatsApp Cloud API oficial existe. A API é REST no Graph API da Meta com bearer token permanente. Templates são essenciais para outbound marketing dos clientes da agência. Prioridade alta de construção.

---

## 4. RATE LIMITING AIRTABLE ENCAPSULADO EM MCP

### 4.1 Contexto do Problema

- Airtable impõe **5 requests/segundo por base**
- Exceder retorna HTTP 429 com exigência de **30 segundos de cooldown**
- Gabriel (fundador) pediu: fila + retry + idempotência + dead-letter encapsulados no MCP

### 4.2 Implementação Recomendada (TypeScript)

**Dependência principal:** `bottleneck` (npm)
- URL: https://www.npmjs.com/package/bottleneck
- Fork mantido: https://www.npmjs.com/package/@sderrow/bottleneck (v3, distributed)

```typescript
import Bottleneck from "bottleneck";

// === 1. RATE LIMITER (Token Bucket) ===
// Airtable: 5 req/s. Usar 250ms (4 req/s) como buffer de segurança.
const limiter = new Bottleneck({
  minTime: 250,      // 1 request a cada 250ms = 4 req/s
  maxConcurrent: 1,  // serializar requests para garantir ordem
});

// === 2. DEAD-LETTER QUEUE ===
interface DeadLetterEntry {
  idempotencyKey: string;
  error: string;
  payload?: unknown;
  timestamp: number;
  retryCount: number;
}
const deadLetterQueue: DeadLetterEntry[] = [];

// === 3. RETRY COM EXPONENTIAL BACKOFF ===
limiter.on("failed", async (error: any, jobInfo) => {
  const maxRetries = 3;
  const { retryCount, options } = jobInfo;

  if (retryCount < maxRetries) {
    // Airtable 429: wait obrigatório de 30s
    if (error.status === 429) {
      console.warn(`[429] Rate limit hit. Backing off 30s. Job: ${options.id}`);
      return 30_000;
    }
    // 5xx/network errors: exponential backoff (2s, 4s, 8s)
    const backoff = Math.pow(2, retryCount) * 2000;
    const jitter = Math.random() * 1000;
    return backoff + jitter;
  }

  // === 4. DLQ ROUTING ===
  deadLetterQueue.push({
    idempotencyKey: options.id ?? "unknown",
    error: error.message || "Max retries exceeded",
    timestamp: Date.now(),
    retryCount: maxRetries,
  });

  return null; // parar de tentar
});

// === 5. IDEMPOTENCY STORE ===
// Em produção: usar Redis/Supabase em vez de Set in-memory
const processedKeys = new Map<string, { result: unknown; timestamp: number }>();
const IDEMPOTENCY_TTL_MS = 24 * 60 * 60 * 1000; // 24h

// === 6. EXECUTOR PRINCIPAL ===
export async function executeAirtableRequest<T>(
  idempotencyKey: string,
  requestFn: () => Promise<T>,
): Promise<T | { status: "skipped"; reason: "idempotency_hit" }> {

  // Check idempotency
  const cached = processedKeys.get(idempotencyKey);
  if (cached && Date.now() - cached.timestamp < IDEMPOTENCY_TTL_MS) {
    return { status: "skipped", reason: "idempotency_hit" };
  }

  return limiter.schedule({ id: idempotencyKey }, async () => {
    const result = await requestFn();
    processedKeys.set(idempotencyKey, { result, timestamp: Date.now() });
    return result;
  });
}

// === 7. DLQ TOOLS (expor via MCP) ===
export function getDeadLetterQueue(): DeadLetterEntry[] {
  return [...deadLetterQueue];
}

export function retryDeadLetterEntry(idempotencyKey: string): boolean {
  const index = deadLetterQueue.findIndex(e => e.idempotencyKey === idempotencyKey);
  if (index !== -1) {
    deadLetterQueue.splice(index, 1);
    return true;
  }
  return false;
}
```

### 4.3 Pattern Breakdown

| Pattern | Implementação | Justificativa |
|---------|--------------|---------------|
| Token Bucket / Queue | `Bottleneck` com `minTime: 250ms` | Previne ultrapassar 5 req/s antes de atingir a rede |
| Exponential Backoff | `.on("failed")` com `Math.pow(2, retryCount) * 2000` + jitter | Evita thundering herd em retries simultâneos |
| 429 Handling | Override para 30.000ms fixo no 429 | Airtable exige 30s de cooldown documentado |
| Idempotency | `Map<key, {result, timestamp}>` com TTL 24h | Previne double-execution de creates/updates |
| Dead-Letter Queue | Array com metadata (key, error, timestamp, retryCount) | Jobs exauridos vão para DLQ sem bloquear a fila |

### 4.4 Tools MCP para Exposição

```
Tools do MCP Airtable customizado:
  - airtable_list_records       (readOnly, paginado, rate-limited)
  - airtable_get_record         (readOnly, rate-limited)
  - airtable_create_record      (idempotent via key, rate-limited)
  - airtable_update_record      (idempotent via key, rate-limited)
  - airtable_delete_record      (destructive, rate-limited)
  - airtable_batch_create       (idempotent, rate-limited, max 10 por batch)
  - airtable_batch_update       (idempotent, rate-limited, max 10 por batch)
  - airtable_get_dead_letter    (readOnly — inspecionar DLQ)
  - airtable_retry_dead_letter  (retry entry específica da DLQ)
  - airtable_get_rate_status    (readOnly — jobs pendentes, DLQ size)
```

### 4.5 Considerações para Produção Distribuída

- **In-memory funciona para:** stdio transport, single-instance
- **Para serverless/Edge:** usar Redis (Upstash) para idempotency store + DLQ
- **Bottleneck v3 (@sderrow/bottleneck):** suporte a Redis clustering nativo
- **Alternativa a Bottleneck:** `p-queue` (npm) para filas simples sem Redis

### 4.6 Referências

- **Airtable Rate Limits Docs:** https://support.airtable.com/docs/managing-api-call-limits-in-airtable
- **Airtable 429 Fix Guide:** https://errormedic.com/api/airtable-api/fixing-airtable-api-error-429-too-many-requests-a-complete-guide-to-rate-limits
- **Bottleneck TS Guide:** https://michaelcohen.space/blog/dealing-with-rate-limits-in-typescript/
- **Airtable MCP (lobeHub):** https://lobehub.com/mcp/bernard0omnisend-airtable_mcp

### Adaptável ao contexto Triforce?
**SIM** - Demanda direta do Gabriel (fundador). O pattern Bottleneck + DLQ encapsula perfeitamente o rate limiting sobre o MCP Airtable oficial. Para deploy em Edge Functions (Supabase), considerar Upstash Redis para estado distribuído.

---

## 5. MCP SERVER LIFECYCLE MANAGEMENT EM PRODUÇÃO

### 5.1 Observability Stack Recomendado

| Camada | Ferramenta | Função |
|--------|-----------|--------|
| Tracing | OpenTelemetry (`@opentelemetry/sdk-node`) | Traces distribuídos por tool call |
| Collector | OpenTelemetry Collector + `spanmetrics` connector | Gerar métricas RED (Rate, Error, Duration) automaticamente a partir de traces |
| Métricas | Prometheus / Grafana | Dashboards e alertas |
| Logs | Structured JSON (pino/winston) | Logs correlacionados com trace IDs |

**Referência principal:** https://oneuptime.com/blog/post/2026-03-26-how-to-instrument-mcp-servers-with-opentelemetry/view

### 5.2 Métricas Obrigatórias para MCP Servers

| Métrica | Tipo OTel | Atributos |
|---------|-----------|-----------|
| `mcp.tool.calls` | Counter | `mcp.tool.name`, `mcp.server.name`, `mcp.transport` |
| `mcp.tool.duration` | Histogram | P50, P95, P99 de execução por tool |
| `mcp.tool.errors` | Counter | Inclui erros thrown + texto começando com "Error:" |
| `mcp.connections.active` | Gauge | Conexões ativas (HTTP/SSE/stdio) |
| `mcp.requests.queued` | Gauge | Requests na fila (se rate limiting) |

### 5.3 Alertas Recomendados

| Alerta | Condição | Ação |
|--------|----------|------|
| Error Rate Alto | `rate(mcp.tool.errors) / rate(mcp.tool.calls) > 0.05` (5%) | Investigar downstream API |
| Latência Alta | P95 duration > 1000ms | Verificar throttling em APIs externas |
| Volume Anômalo | Spike em `mcp.tool.calls` | Detectar agent stuck em retry loop infinito |
| DLQ Crescendo | `dlq.size > 10` em 5min | Investigar falhas sistêmicas |

### 5.4 Health Checks

```typescript
// Endpoint: GET /health (custom HTTP route no FastMCP)
{
  "status": "healthy",
  "version": "1.2.0",
  "uptime_seconds": 3600,
  "tools_registered": 8,
  "active_connections": 3,
  "queue_depth": 0,
  "dlq_size": 0,
  "last_error": null
}
```

### 5.5 Graceful Shutdown

```
1. Receber SIGTERM
2. Flaggar server como "shutting down" (retornar 503 para novas requests)
3. Aguardar deadline máximo (30s) para tool calls em andamento
4. Persistir estado de sessão (se stateful)
5. Force-close transports remanescentes
6. process.exit(0)
```

### 5.6 Tool Deprecation em Runtime

```typescript
// 1. Declarar capability na inicialização
const server = new McpServer({
  name: "triforce-airtable",
  version: "2.0.0",
  capabilities: {
    tools: { listChanged: true }
  }
});

// 2. Quando deprecar um tool em runtime:
server.removeTool("search_records");
// O SDK emite notifications/tools/list_changed automaticamente
// Clients re-chamam tools/list para obter lista atualizada

// 3. Alternativa: manter tool com description atualizada
server.registerTool("search_records", {
  description: "DEPRECATED: Use query_records_v2 instead. This tool will be removed in v3.0.0.",
  // ... manter implementação funcional durante transição
});
```

### 5.7 Connection Management

| Aspecto | Recomendação |
|---------|-------------|
| Transport produção | Streamable HTTP (padrão 2026, SSE é legacy) |
| Stateless design | Empurrar estado para Redis/DB externo |
| Load balancer | Stateless funciona com qualquer LB standard |
| Session affinity | Não necessário se stateless |
| Scaling | Horizontal sem restrições |

### 5.8 Referências

- **OTel para MCP (guia prático):** https://oneuptime.com/blog/post/2026-03-26-how-to-instrument-mcp-servers-with-opentelemetry/view
- **DreamFactory Observability:** https://blog.dreamfactory.com/designing-mcp-servers-for-observability
- **Grizzly Peak Logging Guide:** https://www.grizzlypeaksoftware.com/library/mcp-server-logging-and-observability-p5dkmi7d
- **MCP Manager Observability:** https://mcpmanager.ai/blog/mcp-observability/
- **Merge.dev MCP Observability:** https://www.merge.dev/blog/mcp-observability
- **MCP Best Practices (official):** https://modelcontextprotocol.info/docs/best-practices/
- **MCP Cat Best Practices:** https://mcpcat.io/blog/mcp-server-best-practices/
- **Docker MCP Best Practices:** https://www.docker.com/blog/mcp-server-best-practices/
- **Snyk 5 Best Practices:** https://snyk.io/articles/5-best-practices-for-building-mcp-servers/
- **Graceful Shutdown:** https://theneuralbase.com/mcp/qna/how-to-handle-mcp-server-updates/
- **Transport Migration 2026:** https://www.elegantsoftwaresolutions.com/blog/mcp-transport-scalability-production-migration-guide-2026
- **MCP 2026 Roadmap:** https://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap/
- **Lifecycle MCP Server:** https://mcpservers.org/servers/heffrey78/lifecycle-mcp

### Adaptável ao contexto Triforce?
**SIM** - Aplicação direta. OpenTelemetry + Prometheus/Grafana é padrão de mercado. O pattern de graceful shutdown e tool deprecation via `notifications/tools/list_changed` é nativo do SDK. Recomendação: implementar health check endpoint + OTel tracing em todos os MCP servers desde o primeiro deploy.

---

## MAPA CONSOLIDADO: GAP -> FRAMEWORK/SOP

| # | Gap | Framework/SOP que Cobre | Fonte Principal |
|---|-----|------------------------|-----------------|
| 1 | Changelog/versioning MCP | Keep a Changelog + Conventional Commits + semantic-release | MCP Registry Versioning + awesome-mcp-best-practices |
| 2 | Hotmart API para MCP | OAuth 2.0 client_credentials + REST (Sales/Subscriptions/Members/Products) + Webhook Postback | developers.hotmart.com + FastMCP para construção |
| 3 | WhatsApp Cloud API para MCP | Graph API + Bearer Token permanente + REST endpoints + Webhooks X-Hub-Signature | Meta Developers + FastMCP para construção |
| 4 | Rate limiting Airtable MCP | Bottleneck (token bucket) + exponential backoff + idempotency store + DLQ | Airtable docs + Bottleneck npm + pattern TypeScript |
| 5 | Lifecycle management produção | OpenTelemetry + health checks + graceful shutdown + notifications/tools/list_changed | oneuptime OTel guide + MCP spec + best practices guides |

## GAPS QUE PERMANECERAM SEM COBERTURA

**Nenhum.** Todos os 5 gaps foram cobertos com frameworks, SOPs e referências concretas adaptáveis ao contexto da Triforce Auto.

---

## DECISÕES RECOMENDADAS (próximos passos)

1. **Changelog:** Adotar template da seção 1.4 em todos os repos de MCP servers. Configurar `semantic-release` no GitHub Actions.

2. **Hotmart MCP:** Construir com FastMCP + Zod. OAuth 2.0 client_credentials com refresh automático. Rate limit interno de 8 req/s. Deploy em Supabase Edge Functions.

3. **WhatsApp MCP:** Construir com FastMCP + Zod. Bearer token permanente (System User). Webhook receiver separado. Deploy em Cloudflare Workers (edge performance para mensageria).

4. **Airtable MCP customizado:** Encapsular Bottleneck com `minTime: 250ms` + DLQ sobre o MCP Airtable oficial. Expor tools de inspeção de DLQ e rate status.

5. **Observability:** Implementar OpenTelemetry (`@opentelemetry/sdk-node`) + métricas `mcp.tool.calls`, `mcp.tool.duration`, `mcp.tool.errors` desde o primeiro MCP server. Health check endpoint em todos.
