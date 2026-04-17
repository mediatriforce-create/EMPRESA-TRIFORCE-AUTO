# Scan Operacional — Skills de Copywriting
**Data:** 2026-04-13
**Responsável:** Gabriela (RH) — pesquisa para contratação Copywriter Senior (Fecchio)

---

## 1. Fontes Vasculhadas

### Repos principais
- `coreyhaines31/marketingskills` — repo oficial com 40+ skills de marketing (estrutura em `/skills/`)
- `VoltAgent/awesome-agent-skills` — README com curadoria de skills por categoria
- `agentskillsrepo.com` — diretório de skills (site instável, inacessível durante scan)
- `playbooks.com/skills` — skills instaláveis, fonte confirmada
- `mcpmarket.com` — marketplace de skills MCP

### Skills localizadas no sistema atual (já instaladas)
- `direct-response-copy` — copy de resposta direta / landing pages (já no harness)

---

## 2. Skills Encontradas e Filtro de Qualidade

### APROVADAS (conteúdo verificado)

#### A. `copywriting` — coreyhaines31/marketingskills
**Repo:** `https://github.com/coreyhaines31/marketingskills`
**Instalação:** `/skills/copywriting/SKILL.md`
**Status:** APROVADA

**O que cobre:**
- Copy para homepages, landing pages, pricing pages, feature pages, about pages, product pages
- Framework de página: above-the-fold (headline + subheadline + CTA primário) + seções core
- Seções core: social proof, identificação do problema, solução/benefícios, como funciona, objeções, CTA final
- Princípios: clareza > criatividade, específico > vago, linguagem do cliente > jargão, benefícios > features
- CTAs: verbo de ação + resultado específico ("Start Free Trial", "Get the Complete Checklist")
- Output estruturado por seção com anotações estratégicas + 2-3 alternativas de headline/CTA

**Gaps cobertos:** Copy de LP (parcial), estrutura de página, CTAs
**Gaps NÃO cobertos:** Copy local BR, microcopy, handoff dev/designer, copy sem prova social, SEO local

---

#### B. `copy-editing` — coreyhaines31/marketingskills
**Repo:** `https://github.com/coreyhaines31/marketingskills`
**Instalação:** `/skills/copy-editing/SKILL.md`
**Status:** APROVADA

**O que cobre — Framework "Seven Sweeps":**
1. **Clarity** — o leitor entende a mensagem?
2. **Voice and Tone** — personalidade de marca consistente
3. **So What** — feature conectada a benefício real
4. **Prove It** — substantia claims com evidência
5. **Specificity** — concreto no lugar de vago
6. **Heightened Emotion** — adiciona ressonância emocional
7. **Zero Risk** — remove barreiras à ação

**Extras:** Expert Panel Scoring, Quick-Pass Checks, Content Refresh Framework, Common Problems & Fixes
**Princípio central:** "Good copy editing isn't about rewriting — it's about enhancing."

**Gaps cobertos:** Revisão e edição de copy existente, sweep de objeções, revisão de prova
**Gaps NÃO cobertos:** Copy local BR, microcopy, handoff, SEO local

---

#### C. `page-cro` — coreyhaines31/marketingskills
**Repo:** `https://github.com/coreyhaines31/marketingskills`
**Instalação:** `/skills/page-cro/SKILL.md`
**Status:** APROVADA

**O que cobre — CRO Analysis Framework (ordem de prioridade):**
1. Value Proposition Clarity (5-second test)
2. Headline Effectiveness (specificity + message match)
3. CTA Placement, Copy, and Hierarchy
4. Visual Hierarchy and Scannability
5. Trust Signals and Social Proof (logos, depoimentos com atribuição, métricas, review scores, badges)
6. Objection Handling (preço, fit, implementação, risco)
7. Friction Points (formulários, navegação, mobile, performance)

**Output:** Quick Wins / High-Impact Changes / Test Ideas / Copy Alternatives

**Gaps cobertos:** Análise de LP, trust signals, objeções, friction
**Gaps NÃO cobertos:** Especificidades de negócio local, SEO local, microcopy de interface

---

#### D. `ux-writing` — petekp/claude-code-setup (via playbooks.com)
**URL:** `https://playbooks.com/skills/petekp/claude-code-setup/ux-writing`
**Status:** APROVADA

**O que cobre:**
- Botões e CTAs: ação específica ("Save changes" > "Save", "Delete project" > "OK")
- Labels: sentence case, sempre visíveis, concisas
- Placeholders: suporte, não substituto de label
- Mensagens de erro: estrutura 3 partes — o que aconteceu + por que + como corrigir
- Empty states: o que pertence aqui + por que está vazio + CTA
- Onboarding flows: mostrar valor antes do esforço, progresso explícito ("Step 2 of 4")
- Success/loading states
- Tooltips e confirmações
- Voice & tone guidelines
- Acessibilidade em copy

**Metodologia:**
- Clareza > criatividade
- Brevidade com propósito (cortar até perder significado)
- Linguagem do usuário (sem jargão técnico)
- Consistência: mesma ação = mesmas palavras sempre
- Voice constante + tone adaptável por contexto

**Estrutura de análise:** Voice Check / Issues / Patterns / Quick Wins
**Testes recomendados:** readback, screenshot, stress, translation, truncation

**Gaps cobertos:** GAP 2 (Microcopy) — cobertura COMPLETA
**Gaps NÃO cobertos:** Copy persuasivo de venda, SEO, handoff formal

---

### SKILLS MAPEADAS (não verificadas individualmente, mas listadas no awesome-agent-skills)

| Skill | Repo | Relevância |
|-------|------|-----------|
| `ad-creative` | coreyhaines31/marketingskills | Criativo de anúncios — relevante para campanhas |
| `cold-email` | coreyhaines31/marketingskills | B2B outreach — baixa prioridade |
| `social-content` | coreyhaines31/marketingskills | Posts social — média prioridade |
| `form-cro` | coreyhaines31/marketingskills | CRO de formulários — relevante para LP |
| `headline-matrix` | realkimbarrett/advertising-skills | Variações de headline — alta relevância |
| `objection-crusher` | realkimbarrett/advertising-skills | Neutralizar objeções — alta relevância |
| `scroll-stopping-creative` | realkimbarrett/advertising-skills | Criativo que para scroll — relevante |
| `value-prop-statements` | phuryn/pm-skills | Value props — relevante |

---

## 3. Skills Já Instaladas no Harness (checar sobreposição)

- `direct-response-copy` — cover: copy persuasivo de venda, resposta direta, landing pages
  - Sobreposição com `copywriting` (coreyhaines31): parcial. `direct-response-copy` foca em venda; `copywriting` foca em estrutura de página web.
  - Recomendação: MANTER AMBOS — escopos complementares

---

## 4. Plano de Extração (Próxima Fase)

### Prioridade ALTA — instalar imediatamente
1. `copywriting` (coreyhaines31) — estrutura de LP, frameworks de página web
2. `copy-editing` (coreyhaines31) — Seven Sweeps para revisão
3. `page-cro` (coreyhaines31) — análise CRO de LP
4. `ux-writing` (petekp) — microcopy completo

### Prioridade MÉDIA — instalar na sequência
5. `headline-matrix` (realkimbarrett) — variações de headline
6. `objection-crusher` (realkimbarrett) — objeções
7. `form-cro` (coreyhaines31) — formulários de LP

### Instalação
```bash
# coreyhaines31/marketingskills
claude-code skill install coreyhaines31/marketingskills/copywriting
claude-code skill install coreyhaines31/marketingskills/copy-editing
claude-code skill install coreyhaines31/marketingskills/page-cro
```

---

## 5. Gaps Ainda SEM Cobertura de Skill

| Gap | Status |
|-----|--------|
| Copy para negócio presencial local BR | SEM SKILL — cobrir via conhecimento estratégico |
| Microcopy web | COBERTO (ux-writing) |
| Handoff copy para dev/designer | SEM SKILL — cobrir via template manual |
| Copy sem prova social / pré-receita | SEM SKILL — cobrir via conhecimento estratégico |
| SEO copy local | SEM SKILL — cobrir via conhecimento estratégico + schema-markup skill |
