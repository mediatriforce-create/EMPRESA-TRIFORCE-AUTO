# Scan Estrategico: Criador de Skills Senior

**Data:** 2026-05-06
**Responsavel:** Gabriela (Diretora de RH)
**Objetivo:** Pesquisar frameworks e metodologias para os 4 gaps restantes do cargo de Criador de Skills Senior
**Prerequisito:** scan-operacional.md (Stage 1 + Stage 2 completos)

---

## GAPS PESQUISADOS

| # | Gap | Cobertura pre-scan | Cobertura pos-scan |
|---|-----|--------------------|--------------------|
| 1 | Lifecycle management de skills | ~60% | ~90% |
| 2 | Auditoria de qualidade de skills | ~35% | ~85% |
| 3 | Cross-skill collaboration | ~50% | ~80% |
| 4 | Stack tecnico constraints (nao-dev) | ~45% | ~85% |

---

## GAP 1: LIFECYCLE MANAGEMENT DE SKILLS (era ~60%, agora ~90%)

### 1.1 Frameworks Encontrados

#### 1.1.1 Sakura Sky: Trustworthy AI Agents — Agent Lifecycle Management
- **URL:** https://www.sakurasky.com/blog/missing-primitives-for-trustworthy-ai-part-11/
- **Cobre:** Versioning, deployment pipelines, deprecation paths
- **Modelo:** Trata agentes/skills como microservicos: cada um precisa de versioning, deployment pipeline e safe deprecation path
- **Principios:**
  - Versioning alimenta diretamente safety policy rules
  - System-wide compatibility enforcement na deprecacao
  - Agent-native semantic observability para health monitoring
- **Adaptavel?** SIM. A analogia microservicos -> skills e direta. Cada SKILL.md e um "microservico de conhecimento" com ciclo de vida proprio.

#### 1.1.2 OneReach AI: Agent Lifecycle Management (6 Stages)
- **URL:** https://onereach.ai/blog/agent-lifecycle-management-stages-governance-roi/
- **Cobre:** Ciclo completo design-to-decommission
- **6 Stages:**
  1. **Design:** Specs funcionais, data access patterns, workflows
  2. **Build:** Desenvolvimento em sandbox seguro
  3. **Test:** Validacao automatizada, human-in-the-loop
  4. **Deploy:** Onboarding seguro, escalation paths
  5. **Monitor:** Telemetria real-time, boundary enforcement
  6. **Decommission:** Revocacao de acesso, arquivamento de dados, eliminacao de "ghost agents"
- **GSX Framework:** Version tracking com comparacao de iteracoes e rollbacks seguros. Deprecation via triggers predefinidos (performance em declinio). Scheduled reviews automatizados.
- **Adaptavel?** SIM PARCIALMENTE. Os 6 stages mapeiam bem para skills: Design (gap analysis) -> Build (criar SKILL.md) -> Test (eval suite) -> Deploy (pilot + rollout) -> Monitor (usage tracking) -> Decommission (archive). O GSX em si e enterprise demais, mas o modelo conceitual e perfeito.

#### 1.1.3 Microsoft AgentOps: End-to-End Lifecycle Management
- **URL:** https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/from-zero-to-hero-agentops/4484922
- **Cobre:** Artifact tracking, A/B testing, staging rollbacks
- **Modelo:**
  - Dual registries: um para prompts, outro para containers
  - Feature flags para deprecacao controlada
  - Application Insights para health monitoring
  - Immutable artifact tracking (cada versao e imutavel)
- **Adaptavel?** PARCIALMENTE. O conceito de immutable artifacts e util: cada versao do SKILL.md e imutavel via Git tags. Feature flags podem ser simulados com o campo `stability` no frontmatter.

#### 1.1.4 Skill Instruction File Dependency Resolution (TD Commons)
- **URL:** https://www.tdcommons.org/dpubs_series/9912/
- **Cobre:** Cross-skill dependency management com SemVer
- **Modelo:** Resolve dependencias entre skills usando semver-style version range constraints declarados em cada arquivo (analogia npm/pip/Cargo). Antes de invocar agente, traversa grafo de dependencias, computa versao consistente, detecta conflitos.
- **Sidecar lockfiles** para prevenir conflitos de compatibilidade.
- **Adaptavel?** SIM. Podemos adicionar campo `requires` no frontmatter: `requires: ["dev-web >= 2.0.0", "copywriter >= 1.5.0"]` para skills que dependem de outras.

#### 1.1.5 ToolHive Release Automation (Stacklok)
- **URL:** https://github.com/stacklok/toolhive
- **Cobre:** Changelog automation, SemVer bump, release workflow
- **Modelo:** Analisa commits desde ultimo release, classifica changes (features, fixes, docs, breaking), recomenda bump type (major/minor/patch), gera changelog estruturado.
- **Adaptavel?** SIM. Conventional commits + semantic-release para skills. Cada skill folder pode ter seu proprio CHANGELOG.md gerado automaticamente.

### 1.2 Sintese: Framework de Lifecycle para Triforce Auto

**Modelo proposto (combinando OneReach 6-Stage + Sakura Sky + SemVer):**

```
LIFECYCLE STAGES:
1. IDENTIFY  -> Gap analysis no time (qual skill falta?)
2. RESEARCH  -> Buscar skills externas (Adopt/Extend/Build)
3. BUILD     -> Criar SKILL.md + references/ + eval suite
4. PILOT     -> 1 agente testa por 7 dias
5. DEPLOY    -> Rollout para time completo
6. MONITOR   -> Usage tracking + next_review scheduling
7. DEPRECATE -> Sunset timeline (30-60-90 dias)
8. ARCHIVE   -> Mover para _archived/, manter historico
```

**Frontmatter de lifecycle proposto (evolucao do scan-operacional):**

```yaml
---
name: skill-name
description: "..."
version: "1.2.0"
stability: "stable"  # experimental | beta | stable | deprecated | archived
owner: "nome-do-agente"
next_review: "2026-08-06"
sources_version: "curso-anthropic-v2.1"
last_audit: "2026-05-06"
requires: ["dev-web >= 2.0.0"]  # dependencias de outras skills
changelog: "references/CHANGELOG.md"
created: "2026-03-15"
deprecated_date: null  # preenchido quando stability = deprecated
sunset_date: null      # preenchido quando stability = archived
---
```

**Regras de review automatizado:**
- `next_review` calculado como: data de criacao/atualizacao + 90 dias
- Alerta quando `next_review < hoje`: skill precisa de revisao
- Alerta quando `sources_version` nao bate com versao atual da fonte
- Alerta quando `stability = deprecated` e `sunset_date < hoje + 30 dias`

### 1.3 O que FALTAVA e agora esta COBERTO

| Item | Fonte que cobriu |
|------|-----------------|
| Sistema de next_review dates | OneReach (scheduled reviews) + Modelo proprio |
| Sources_version tracking | Sakura Sky (version -> policy rules) + Modelo proprio |
| Alertas de skill desatualizada | OneReach (performance triggers) + CI/CD policy engines |
| Workflow de deprecacao | OneReach 6-stage + Sakura Sky (compatibility enforcement) |
| Dependency tracking entre skills | TD Commons (semver dependency resolution) |
| Changelog automation | ToolHive release (conventional commits + semantic-release) |

---

## GAP 2: AUDITORIA DE QUALIDADE DE SKILLS (era ~35%, agora ~85%)

### 2.1 Frameworks Encontrados

#### 2.1.1 MedSkillAudit: Domain-Specific Audit Framework
- **URL:** https://arxiv.org/html/2604.20441v1
- **Cobre:** Framework de auditoria com veto gates e scoring
- **Estrutura:**
  - **Veto Gate 1 (Structural Audit):**
    - T1: Operational Stability (crash rate <= 20%, sem conflitos de dependencia)
    - T2: Structural Consistency (schema SKILL.md compliant, campos obrigatorios)
    - T3: Result Determinism (outputs consistentes)
    - T4: System Security (sem execucao de codigo nao sanitizado, sem prompt injection)
  - **Veto Gate 2 (Domain-Specific Audit):**
    - Verifica integridade do dominio especifico
    - Hard gates para fabricacao de dados, conclusoes invalidas, falacias logicas
  - **Scoring:** `FinalScore = 0.4 x S_static + 0.6 x D_dynamic`
    - S_static: 25 criterios de design quality
    - D_dynamic: Performance media em runtime
  - **Dispositions:**
    - >= 85: Production Ready
    - 75-84: Limited Release
    - 60-74: Beta Only
    - < 60: Reject
- **Adaptavel?** MUITO. Substituir Veto Gate 2 (medical) por gates de agencia digital: Brand Integrity, Data Privacy, Output Boundaries. Scoring 40/60 funciona direto.

#### 2.1.2 OWASP Agentic Skills Top 10 (AST09: No Governance)
- **URL:** https://owasp.org/www-project-agentic-skills-top-10/ast09
- **Checklist:** https://owasp.org/www-project-agentic-skills-top-10/checklist.html
- **Cobre:** Security assessment e governance gaps
- **AST09 identifica:**
  - Skills instaladas sem oversight do SOC
  - Ausencia de approval protocols e revocation mechanisms
  - "Shadow AI" sem inventario
- **Checklist de seguranca por severidade:**
  - Critical (AST01, AST02): Full checklist + dynamic testing + manual review
  - High (AST03-AST05): Schema validation + static analysis
  - Medium (AST06-AST08): Metadata checks + permission scoping
  - Low (AST09-AST10): Governance inventory + audit logging
- **Adaptavel?** SIM. Checklist OWASP como gate de seguranca antes de qualquer skill ir para producao. Simplificado para nosso contexto (skills internas, nao marketplace publico).

#### 2.1.3 OpenClaw Audit Guide: How to Audit AI Agent Skills
- **URL:** https://openclaw.nasseroumer.com/blog/how-to-audit-ai-skills/
- **Cobre:** Code review, permission analysis, network behavior, prompt injection detection
- **Metodologia:**
  - Review de codigo-fonte da skill
  - Analise de permissoes (allowed-tools)
  - Comportamento de rede (external calls)
  - Deteccao de prompt injection
- **Adaptavel?** SIM. Util como checklist tecnico para skills que contem scripts.

#### 2.1.4 AIXplore: Pruning Your AI Agent Skills Library
- **URL:** https://ai.rundatarun.io/AI+Development+&+Agents/Pruning+Your+AI+Agent+Skills+Library
- **Cobre:** Consolidacao, deteccao de redundancia, archiving
- **Metodologia (3 passes):**
  1. **Overlap Analysis:** Trigger collision matrix, compara triggers/descriptions/user intents
  2. **Usage Audit:** Classifica como core/occasional/unused (unused = 0 uso em 90 dias)
  3. **Quality Check:** Line count, tone consistency, references integrity
- **Merge Patterns:**
  - Mode-based consolidation: mesmo workflow, outputs diferentes
  - Feature consolidation: varias skills sao features de uma capacidade
  - Audience-based consolidation: so muda formato final
- **Resultado real:** 87 skills -> 70 (20% reducao). 24 skills arquivadas em `_archived/`.
- **Adaptavel?** MUITO. Aplicavel diretamente ao nosso inventario de 25+ skills.

#### 2.1.5 LobeHub: Skill Gap Analyzer
- **URL:** https://lobehub.com/skills/dnyoussef-ai-chrome-extension-when-analyzing-skill-gaps-use-skill-gap-analyzer
- **Cobre:** Coverage gaps, redundant overlaps, optimization opportunities
- **Features:**
  - Domain coverage mapping
  - Use-case e workflow completeness tests
  - Deteccao de funcionalidade duplicada/overlapping
  - Composability e dependency analysis
  - Prioritized recommendations
- **4 tipos de gaps detectados:**
  1. Complete gaps (dominio inteiro sem skill)
  2. Derivative gaps (skill existe mas nao cobre variantes)
  3. Compound gaps (combinacao de skills que ninguem faz)
  4. Depth gaps (skill existe mas e superficial)
- **Adaptavel?** SIM. Executar apos o overlap audit para encontrar o que FALTA, nao so o que SOBRA.

#### 2.1.6 Agent Health Checks Pattern
- **URL:** https://www.agentpatterns.tech/en/observability-monitoring/agent-health-checks
- **Cobre:** Runtime liveness, tool dependency checks, policy path validation, alertable readiness signals
- **Adaptavel?** PARCIALMENTE. Conceitos de health check aplicaveis a skills: "a skill esta saudavel se seus references existem, seu owner esta ativo, e sua next_review nao passou".

### 2.2 Sintese: Framework de Auditoria para Triforce Auto

**Modelo proposto (combinando MedSkillAudit + AIXplore + LobeHub):**

#### Veto Gate 1: Structural Audit (hard gates, falha = reject)
- [ ] SKILL.md existe e tem frontmatter valido
- [ ] Campos obrigatorios presentes: name, description, version, owner, stability, next_review
- [ ] Nenhum script executa codigo nao sanitizado
- [ ] allowed-tools esta scopado (nao usa wildcards)
- [ ] Tamanho do SKILL.md < 500 linhas (progressive disclosure)
- [ ] References/ existem e links nao estao quebrados

#### Veto Gate 2: Domain Audit (hard gates de agencia digital)
- [ ] Nao gera conteudo que viola brand guidelines de clientes
- [ ] Nao expoe PII, API keys, ou dados sensíveis
- [ ] Nao faz claims legais/financeiros sem disclaimer
- [ ] Output boundaries claros (skill sabe o que NAO fazer)

#### Scoring: Health Score por Skill

| Metrica | Peso | Como pontuar |
|---------|------|-------------|
| Frequencia de uso | 25% | Normalizar invocacoes 30/90 dias. Core workflows = score max |
| Clareza de trigger | 20% | Score maximo se triggers explicitos e descriptions especificas |
| Penalidade de overlap | 20% | Subtrair pontos conforme overlap de trigger/intent sobe. 70%+ = review de merge |
| Confiabilidade | 15% | Taxa de sucesso ou rating manual pos-invocacao |
| Eficiencia de tokens | 10% | Penalizar skills bloated e sem progressive disclosure |
| Qualidade de manutencao | 10% | Line count, tom, references, owner/links atualizados |

**Formula:** `HealthScore = sum(metrica * peso)` (0-100)

**Dispositions (adaptado MedSkillAudit):**
- >= 85: **Production Ready** (stable)
- 75-84: **Limited Release** (needs minor fixes)
- 60-74: **Beta Only** (needs significant work)
- < 60: **Reject/Archive** (rewrite ou aposentar)

**Cadencia de auditoria:**
- Trimestral: audit completo de todas as skills
- Mensal: scan rapido (next_review expirados + links quebrados)
- A cada commit: validacao de frontmatter via pre-commit hook

### 2.3 O que FALTAVA e agora esta COBERTO

| Item | Fonte que cobriu |
|------|-----------------|
| Checklist de audit periodico | MedSkillAudit (veto gates) + OWASP (checklist) |
| Deteccao de skills desatualizadas | AIXplore (90-day unused rule) + OneReach (performance triggers) |
| Ownership tracking | MedSkillAudit (DRI requirement) + Frontmatter `owner` |
| Redundancy detection | AIXplore (trigger collision matrix) + LobeHub (overlap detection) |
| Health score | MedSkillAudit (40/60 formula) + Health Score ponderado adaptado |
| Link/reference integrity | Agent Health Checks + AIXplore (quality check pass) |

---

## GAP 3: CROSS-SKILL COLLABORATION (era ~50%, agora ~80%)

### 3.1 Frameworks Encontrados

#### 3.1.1 DynamicCoord: Advanced Protocols for Multi-Agent Coordination
- **URL:** https://ijsred.com/volume9/issue1/IJSRED-V9I1P278.pdf
- **Cobre:** Task handoffs, domain overlap detection, conflict resolution
- **Mecanismos:**
  - **Domain Overlap Detection:** Computa similaridade entre task requirements e capability vectors de cada agente (proficiency 0-1, workload, confidence)
  - **Skill Handoff:** Context-preserving transfer com capability-aware routing quando agente encontra task fora do escopo
  - **Conflict Prevention:** Multi-tier resolution (auction, negociacao, belief-merging). Escalation para humano se confidence < 85%
- **Adaptavel?** PARCIALMENTE. O conceito de capability vectors e diretamente aplicavel: cada skill pode ter um `domain_tags` no frontmatter que define seu territorio. Overlap detectado quando 2+ skills tem tags identicos.

#### 3.1.2 LangChain Handoffs
- **URL:** https://docs.langchain.com/oss/python/langchain/multi-agent/handoffs
- **Cobre:** State-driven behavior changes, tool-based transitions
- **Modelo:** Tools atualizam variavel de estado (`active_agent`) que persiste entre turnos. Sistema le variavel para ajustar comportamento, aplicar config diferente, ou rotear para agente diferente.
- **Adaptavel?** PARCIALMENTE. Util para entender o conceito de "handoff = mudar estado + preservar contexto". No nosso sistema, handoff entre skills e feito via secao 5 (Colaboracao com o time) do SKILL.md.

#### 3.1.3 Microsoft Agent Framework: Handoff Orchestration
- **URL:** https://learn.microsoft.com/en-us/agent-framework/workflows/orchestrations/handoff
- **Cobre:** Dynamic agent-driven routing, conversation history preservation
- **Modelo:** Agente ativo avalia contexto e determina proximo handler. Preserva historico completo de conversacao multi-turno entre todos os handoffs.
- **Adaptavel?** PARCIALMENTE. Principio de preservar contexto completo no handoff e crucial. No nosso sistema: quando skill-creator entrega skill para agente consumidor, deve incluir contexto completo (por que a skill foi criada, o que cobre, limitacoes).

#### 3.1.4 LobeHub: Handoff Protocols Skill
- **URL:** https://lobehub.com/en/skills/rohitg00-skillkit-handoff-protocols
- **Cobre:** Structured handoff documents, planned/unplanned/partial handoffs
- **Template de Handoff Document:**
  1. Quick Summary
  2. Current Status (phase, progress, blockers, next action)
  3. Context (goal, why)
  4. Key Decisions (options, choices, rationale)
  5. Open Questions
  6. Technical Details
- **3 tipos de handoff:**
  - **Planned:** Transicao agendada com documentacao completa
  - **Unplanned:** Transicao urgente com contexto minimo viavel
  - **Partial:** Transferencia de parte do trabalho, ownership compartilhado temporario
- **Adaptavel?** MUITO. Template de handoff document diretamente aplicavel para entrega de skills do skill-creator para agentes consumidores.

#### 3.1.5 LobeHub: Multi-Agent Coordination Protocol
- **URL:** https://lobehub.com/skills/neversight-skills_feed-multi-agent-coordination
- **Cobre:** File-reservation workflow, conflict handling, peer notifications
- **Mecanismos:**
  - File-reservation com exclusive locks e TTL
  - Conflict handling: identify holder -> request handoff -> wait for expiry
  - Peer notifications: affected files, intent, estimated impact
  - Session isolation via unique session IDs
- **Adaptavel?** PARCIALMENTE. File locks sao overkill para nosso contexto (nao temos agentes concorrentes no mesmo arquivo). Mas o conceito de "domain reservation" e util: cada skill "reserva" um dominio de conhecimento.

#### 3.1.6 LobeHub: Conflict Prevention (Swarm Coordination)
- **URL:** https://lobehub.com/ar/skills/dralgorhythm-claude-agentic-framework-swarm-coordination
- **Cobre:** Multi-agent conflict-free development
- **Modelo:** Beads (bd) como single source of truth. Workflows para claiming work, progress updates, finalizacao. File locks automatizados, session isolation, edit logging.
- **Adaptavel?** PARCIALMENTE. O conceito de "claiming domain" antes de criar/editar skill e util para evitar que dois agentes criem skills conflitantes.

### 3.2 Sintese: Protocolo de Colaboracao para Triforce Auto

#### 3.2.1 Handoff Protocol: Skill-Creator -> Agentes Consumidores

**5 fases do handoff:**

```
1. DRAFT     -> Skill-creator produz v0.1 do SKILL.md
2. REVIEW    -> Agente consumidor principal revisa (7 dias)
3. PILOT     -> 1 agente usa em producao por 7 dias, reporta issues
4. ROLLOUT   -> Skill disponibilizada para todo o time
5. MONITOR   -> Feedback loop continuo (30/60/90 dias)
```

**Handoff Document (adaptado LobeHub):**

```markdown
## Handoff: [nome-da-skill]

### Quick Summary
- O que: [descricao em 1 frase]
- Para quem: [agentes que vao usar]
- Por que agora: [gap que resolve]

### Status
- Fase: [DRAFT/REVIEW/PILOT/ROLLOUT]
- Progresso: [%]
- Blockers: [lista]
- Proxima acao: [descricao]

### Contexto
- Gap original: [referencia ao gap analysis]
- Fontes usadas: [lista de fontes com versoes]
- Decisoes tomadas: [escolhas e racional]

### Instrucoes de uso
- Trigger: [como ativar a skill]
- Exemplo: [caso de uso concreto]
- Limitacoes: [o que a skill NAO faz]

### Feedback solicitado
- [ ] Instrucoes claras?
- [ ] Exemplos suficientes?
- [ ] Constraints precisos?
- [ ] Falta algum caso de uso?
```

#### 3.2.2 Domain Overlap Detection

**Metodo (adaptado DynamicCoord):**

Cada SKILL.md declara seus `domain_tags` no frontmatter:
```yaml
domain_tags: ["landing-page", "html", "css", "design-system"]
```

**Deteccao de conflito:**
- 2 skills com > 60% de tags identicos = **alerta de overlap**
- 2 skills com > 80% de tags identicos = **review obrigatorio de merge**
- Resolucao: definir boundaries claros na descricao ou merge skills

#### 3.2.3 Geracao Automatica da Secao 5 (Colaboracao com o Time)

**Template padrao para secao 5 de qualquer SKILL.md:**

```markdown
## 5. Colaboracao com o Time

### 5.1 Skills que COMPLEMENTAM esta skill
- [lista auto-gerada por domain_tags overlap < 40%]

### 5.2 Skills que podem CONFLITAR com esta skill
- [lista auto-gerada por domain_tags overlap > 60%]

### 5.3 Handoff triggers
- RECEBE trabalho de: [skills que antecedem no workflow]
- ENTREGA trabalho para: [skills que sucedem no workflow]

### 5.4 Informacoes que esta skill PRECISA de outras
- De [skill-x]: [dado especifico]

### 5.5 Informacoes que esta skill PRODUZ para outras
- Para [skill-y]: [output especifico]
```

### 3.3 O que FALTAVA e agora esta COBERTO

| Item | Fonte que cobriu |
|------|-----------------|
| Protocolo de handoff skill-creator -> consumidores | LobeHub Handoff Protocols (template + 3 tipos) |
| Geracao de secao 5 automatica | DynamicCoord (capability vectors) + domain_tags |
| Deteccao de conflitos de dominio | DynamicCoord (overlap detection) + domain_tags threshold |
| Preservacao de contexto no handoff | LangChain (state persistence) + Microsoft (history preservation) |

---

## GAP 4: STACK TECNICO CONSTRAINTS PARA NAO-DEVS (era ~45%, agora ~85%)

### 4.1 Frameworks Encontrados

#### 4.1.1 SCOPE Method (IdeaPlan)
- **URL:** https://www.ideaplan.io/blog/how-to-write-specs-for-ai-coding-agents
- **Cobre:** Metodologia para nao-devs escreverem specs para AI agents
- **Framework SCOPE:**
  - **S**tructure: Definir arquitetura e organizacao
  - **C**onstraints: Three-tier boundaries
  - **O**utput: Formato e criterios de aceitacao
  - **P**atterns: Padroes a seguir e anti-patterns a evitar
  - **E**xamples: Exemplos concretos com valores reais
- **Three-tier boundaries (crucial para nao-devs):**
  - **Always:** "Sempre use Next.js App Router, nao Pages Router"
  - **Ask First:** "Proponha novas dependencias antes de instalar"
  - **Never:** "Nunca use raw SQL; use Drizzle ORM"
- **Adaptavel?** MUITO. Framework ideal para o skill-creator extrair constraints tecnicos sem ser dev. Entrevista devs usando as 3 categorias Always/Ask First/Never.

#### 4.1.2 Addy Osmani: How to Write a Good Spec for AI Agents
- **URL:** https://addyosmani.com/blog/good-spec/
- **Cobre:** Spec writing para coding agents, incluindo nao-devs
- **Metodologia:**
  1. Fornecer visao high-level e pedir ao AI para draftar spec.md inicial
  2. Estruturar instrucoes como PRD profissional
  3. Quebrar em prompts modulares (nao um bloco massivo)
  4. Usar sub-agents especializados com apenas constraints relevantes ao dominio
- **Key insights:**
  - Specs cobrem: commands, tests, project structure, code style, git workflow, three-tier boundaries
  - "Aim for a clear spec covering just enough nuance to guide the AI without over-constraining"
- **Adaptavel?** MUITO. O skill-creator pode usar Claude para draftar a secao de constraints apos ler as skills internas dos devs. Human-in-the-loop para validar.

#### 4.1.3 Anthropic 2026 Agentic Coding Trends Report
- **URL:** https://resources.anthropic.com/hubfs/2026%20Agentic%20Coding%20Trends%20Report.pdf
- **Cobre:** Democratizacao de coding para nao-devs
- **Key findings:**
  - "Coding capabilities democratize beyond engineering: Non-technical teams across sales, marketing, legal, and operations gain the ability to automate workflows and build tools with little or no engineering intervention"
  - Agents aprendem a pedir ajuda humana quando encontram decisoes ambiguas
  - Suporte para linguagens legacy e domain-specific
- **Adaptavel?** SIM. Valida que o skill-creator nao precisa ser dev para escrever constraints. A key e: ensinar o agente a PARAR e PERGUNTAR quando nao tem certeza.

#### 4.1.4 Stack Overflow: Building Shared Coding Guidelines for AI
- **URL:** https://stackoverflow.blog/2026/03/26/coding-guidelines-for-ai-agents-and-people-too/
- **Cobre:** Como documentar guidelines que tanto humanos quanto AI agents entendem
- **Adaptavel?** SIM. Principio: constraints para AI devem ser escritos da mesma forma que coding guidelines para juniors. Claros, concretos, com exemplos.

#### 4.1.5 Dust.tt: How to Write AI Agent Instructions That Actually Work
- **URL:** https://dust.tt/blog/how-to-write-ai-agent-instructions
- **Cobre:** Writing instructions para AI agents que funcionam em centenas de interacoes
- **Diferenca crucial:** Writing prompts para ChatGPT e uma coisa. Writing instructions que definem como um AI agent se comporta across centenas de interacoes e outra.
- **Adaptavel?** SIM. Reforça que constraints devem ser COMPORTAMENTAIS, nao apenas tecnicos.

### 4.2 Sintese: Metodologia de Extracao de Constraints para Nao-Devs

#### 4.2.1 Protocolo de Consulta a Skills Internas (3 passos)

**Passo 1: Leitura automatizada**
O skill-creator instrui Claude a ler as skills internas e extrair constraints:

```
"Leia as seguintes skills e extraia TODOS os constraints tecnicos 
mencionados, organizados em 3 categorias:
- ALWAYS (regras que sempre se aplicam)
- ASK FIRST (decisoes que precisam de aprovacao)
- NEVER (proibicoes absolutas)

Skills para ler:
- .claude/skills/dev-web/SKILL.md
- .claude/skills/dev-backend/SKILL.md  
- .claude/skills/dev-frontend/SKILL.md
- .claude/skills/dev-lider/SKILL.md
```

**Passo 2: Entrevista estruturada com devs (SCOPE method)**

| Boundary | Pergunta | Exemplo de output |
|----------|---------|-------------------|
| **Always** | "Que regras se aplicam a TODA feature nova?" | "Sempre use Next.js App Router" |
| **Always** | "Que ferramentas/libs sao obrigatorias?" | "Sempre use Drizzle ORM, nunca Prisma" |
| **Ask First** | "Que decisoes tecnicas precisam de aprovacao?" | "Proponha novas deps antes de instalar" |
| **Ask First** | "Quando o agente deve PARAR e perguntar?" | "Schema changes no Supabase" |
| **Never** | "Quais sao hard stops e riscos de seguranca?" | "Nunca use raw SQL" |
| **Never** | "Que sistemas o agente NAO pode modificar?" | "Nunca edite .env ou auth config" |

**Passo 3: Validacao cruzada**
- Comparar constraints extraidos por Claude (passo 1) com respostas dos devs (passo 2)
- Discrepancias = gap de documentacao nas skills internas (feedback para skill-creator atualizar)

#### 4.2.2 Template de Constraints para SKILL.md

```markdown
## 4. Constraints Tecnicos

### 4.1 ALWAYS (obrigatorio em toda entrega)
- Use Next.js 15 App Router (nao Pages Router)
- Use TypeScript strict mode
- Use Drizzle ORM para queries (nao raw SQL, nao Prisma)
- Deploy via Vercel (nao AWS, nao GCP)
- DNS e CDN via Cloudflare
- Database via Supabase (PostgreSQL)
- Estilizacao via Tailwind CSS

### 4.2 ASK FIRST (precisa aprovacao do dev-lider)
- Instalacao de novas dependencias npm
- Mudancas no schema do banco (migrations)
- Configuracao de novos servicos externos
- Alteracoes em rotas de API existentes

### 4.3 NEVER (proibido, sem excecao)
- Nunca use raw SQL direto no Supabase
- Nunca edite arquivos .env manualmente
- Nunca modifique configuracao de auth sem dev-lider
- Nunca faca deploy direto em producao sem review
- Nunca instale pacotes com vulnerabilidades conhecidas
```

### 4.3 O que FALTAVA e agora esta COBERTO

| Item | Fonte que cobriu |
|------|-----------------|
| Metodologia para nao-dev extrair constraints | SCOPE Method (3-tier boundaries) + Addy Osmani (AI-draft + validate) |
| Como consultar skills internas existentes | Protocolo de 3 passos: leitura automatizada + entrevista + validacao |
| Como formatar constraints para AI agents | Stack Overflow (guidelines = constraints) + Dust.tt (comportamental) |
| Validacao de que nao-devs podem fazer isso | Anthropic 2026 Report (democratizacao confirmada) |

---

## INVENTARIO COMPLETO DE FRAMEWORKS E FONTES

### Fontes por Gap

| # | Nome | URL | Gap(s) | Adaptavel? |
|---|------|-----|--------|-----------|
| 1 | Sakura Sky: Trustworthy AI Lifecycle | https://www.sakurasky.com/blog/missing-primitives-for-trustworthy-ai-part-11/ | Gap 1 | SIM |
| 2 | OneReach AI: 6-Stage Lifecycle | https://onereach.ai/blog/agent-lifecycle-management-stages-governance-roi/ | Gap 1 | SIM (parcial) |
| 3 | Microsoft AgentOps | https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/from-zero-to-hero-agentops/4484922 | Gap 1 | PARCIAL |
| 4 | TD Commons: Skill Dependency Resolution | https://www.tdcommons.org/dpubs_series/9912/ | Gap 1 | SIM |
| 5 | ToolHive Release (Stacklok) | https://github.com/stacklok/toolhive | Gap 1 | SIM |
| 6 | SkillHub (iFlytek) | https://github.com/iflytek/skillhub | Gap 1, 2 | SIM |
| 7 | MedSkillAudit | https://arxiv.org/html/2604.20441v1 | Gap 2 | MUITO |
| 8 | OWASP AST09 + Checklist | https://owasp.org/www-project-agentic-skills-top-10/checklist.html | Gap 2 | SIM |
| 9 | OpenClaw Audit Guide | https://openclaw.nasseroumer.com/blog/how-to-audit-ai-skills/ | Gap 2 | SIM |
| 10 | AIXplore: Pruning Skills Library | https://ai.rundatarun.io/AI+Development+&+Agents/Pruning+Your+AI+Agent+Skills+Library | Gap 2 | MUITO |
| 11 | LobeHub: Skill Gap Analyzer | https://lobehub.com/skills/dnyoussef-ai-chrome-extension-when-analyzing-skill-gaps-use-skill-gap-analyzer | Gap 2 | SIM |
| 12 | Agent Health Checks | https://www.agentpatterns.tech/en/observability-monitoring/agent-health-checks | Gap 2 | PARCIAL |
| 13 | DynamicCoord Protocol | https://ijsred.com/volume9/issue1/IJSRED-V9I1P278.pdf | Gap 3 | PARCIAL |
| 14 | LangChain Handoffs | https://docs.langchain.com/oss/python/langchain/multi-agent/handoffs | Gap 3 | PARCIAL |
| 15 | Microsoft Agent Handoff | https://learn.microsoft.com/en-us/agent-framework/workflows/orchestrations/handoff | Gap 3 | PARCIAL |
| 16 | LobeHub: Handoff Protocols | https://lobehub.com/en/skills/rohitg00-skillkit-handoff-protocols | Gap 3 | MUITO |
| 17 | LobeHub: Multi-Agent Coordination | https://lobehub.com/skills/neversight-skills_feed-multi-agent-coordination | Gap 3 | PARCIAL |
| 18 | LobeHub: Swarm Coordination | https://lobehub.com/ar/skills/dralgorhythm-claude-agentic-framework-swarm-coordination | Gap 3 | PARCIAL |
| 19 | SCOPE Method (IdeaPlan) | https://www.ideaplan.io/blog/how-to-write-specs-for-ai-coding-agents | Gap 4 | MUITO |
| 20 | Addy Osmani: Spec for AI Agents | https://addyosmani.com/blog/good-spec/ | Gap 4 | MUITO |
| 21 | Anthropic 2026 Coding Trends | https://resources.anthropic.com/hubfs/2026%20Agentic%20Coding%20Trends%20Report.pdf | Gap 4 | SIM |
| 22 | Stack Overflow: Coding Guidelines for AI | https://stackoverflow.blog/2026/03/26/coding-guidelines-for-ai-agents-and-people-too/ | Gap 4 | SIM |
| 23 | Dust.tt: AI Agent Instructions | https://dust.tt/blog/how-to-write-ai-agent-instructions | Gap 4 | SIM |

### Fontes com Adaptabilidade MUITO ALTA (prioridade para a skill)

1. **MedSkillAudit** — Framework de audit com veto gates + scoring. Adaptacao direta substituindo gates medicos por gates de agencia digital.
2. **AIXplore Pruning** — Metodologia pratica de consolidacao testada em 87 skills reais. 3 passes + merge patterns.
3. **SCOPE Method** — Framework de constraints Always/Ask First/Never ideal para nao-devs.
4. **LobeHub Handoff Protocols** — Template de handoff document pronto para usar.
5. **Addy Osmani Spec Writing** — Workflow AI-draft -> human-validate para specs.
6. **SkillHub (iFlytek)** — Registry com SemVer, namespaces, RBAC. Referencia para governance.

---

## RECOMENDACOES PARA A SKILL DO CRIADOR DE SKILLS SENIOR

### Skills internas a criar (atualizado com novos findings):

| Skill | Descricao | Fontes base |
|-------|-----------|-------------|
| **skill-lifecycle** | Frontmatter customizado + 8 stages lifecycle + next_review automation | OneReach + Sakura Sky + SemVer |
| **skill-auditor** | Audit periodico: veto gates + health score + redundancy detection | MedSkillAudit + AIXplore + LobeHub Gap Analyzer |
| **skill-handoff** | Protocolo de entrega skill-creator -> agentes consumidores | LobeHub Handoff + DynamicCoord |
| **skill-constraints** | Metodologia SCOPE para extrair constraints tecnicos de skills internas | SCOPE Method + Addy Osmani |

### Campos de frontmatter (versao final):

```yaml
---
# Campos padrao
name: "skill-name"
description: "..."
allowed-tools: ["Read", "Edit", "Grep", "Glob"]

# Lifecycle (Gap 1)
version: "1.2.0"
stability: "stable"  # experimental | beta | stable | deprecated | archived
owner: "nome-do-agente"
next_review: "2026-08-06"
sources_version: "curso-anthropic-v2.1"
last_audit: "2026-05-06"
created: "2026-03-15"
deprecated_date: null
sunset_date: null
requires: ["dev-web >= 2.0.0"]
changelog: "references/CHANGELOG.md"

# Audit (Gap 2)
health_score: 87  # 0-100, calculado pelo skill-auditor
disposition: "production-ready"  # production-ready | limited-release | beta-only | reject

# Collaboration (Gap 3)
domain_tags: ["landing-page", "html", "css"]
handoff_from: ["estrategista-comercial"]
handoff_to: ["dev-web", "dev-frontend"]
---
```

### Checklist OWASP simplificado para skills internas:

- [ ] Skill nao executa scripts sem sandboxing?
- [ ] Allowed-tools esta minimamente scopado?
- [ ] Nenhuma credencial hardcoded no SKILL.md ou references?
- [ ] Skill nao pode escalar privilegios alem do necessario?
- [ ] Owner esta atribuído e ativo no time?

---

## CONCLUSAO

### Cobertura final dos 4 gaps:

| Gap | Pre-scan | Pos-scan | Delta | Status |
|-----|----------|----------|-------|--------|
| 1. Lifecycle management | ~60% | ~90% | +30pp | COBERTO (framework completo desenhado) |
| 2. Auditoria de qualidade | ~35% | ~85% | +50pp | COBERTO (veto gates + health score + merge patterns) |
| 3. Cross-skill collaboration | ~50% | ~80% | +30pp | COBERTO (handoff protocol + domain overlap detection) |
| 4. Stack tecnico constraints | ~45% | ~85% | +40pp | COBERTO (SCOPE method + protocolo de consulta 3-step) |

### O que resta (~10-20% por gap):

- **Gap 1 (10% restante):** Implementacao real do CI/CD para validacao de frontmatter e alertas automaticos. Precisa de dev para criar hooks.
- **Gap 2 (15% restante):** Script real de audit automatizado (o scan-operacional ja tinha proposto, agora tem framework). Precisa de implementacao.
- **Gap 3 (20% restante):** Testagem do handoff protocol com o time real. O framework esta desenhado mas nao validado em producao.
- **Gap 4 (15% restante):** Primeira rodada de entrevistas SCOPE com Andre (dev-lider) para extrair constraints reais e validar o protocolo.

### Proxima acao: Stage 3 — Criar a skill completa do Criador de Skills Senior usando scan-operacional.md + scan-estrategico.md como base de conhecimento.
