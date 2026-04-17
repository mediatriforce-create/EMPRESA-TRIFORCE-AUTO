# Scan Operacional — Designer UI/UX Senior (Camila)
**Data:** 2026-04-13
**Responsável:** Gabriela (RH)
**Stage:** 2 — Pesquisa de skills e ferramentas

---

## 1. SKILLS ENCONTRADAS E FILTRADAS

### Universo total varrido
- **VoltAgent awesome-agent-skills README** — 23 skills com tag design/UI/visual identificadas
- **coreyhaines31/marketingskills** — sem matches nos filtros design/creative/visual (repo foca em copy e CRO textual)
- **sickn33/antigravity-awesome-skills** — sem matches nos filtros de design
- **Perplexity + GitHub search** — 8 skills adicionais identificadas via web
- **skills.sh** — 3 skills relevantes encontradas diretamente

### Skills descartadas (não se aplicam ao contexto)
| Skill | Motivo do descarte |
|-------|-------------------|
| anthropics/canvas-design | Gera PNG/PDF artístico, não LP web |
| anthropics/theme-factory | Tematização de artifacts Claude, não Figma |
| anthropics/web-artifacts-builder | React em claude.ai artifacts, não produção |
| anthropics/brand-guidelines | Aplica brand Anthropic, não cliente |
| google-labs-code/design-md | Gerencia DESIGN.md, muito genérico |
| google-labs-code/enhance-prompt | Melhora prompts, não design |
| microsoft/frontend-ui-dark-ts | Dark theme específico Microsoft, estético demais |
| figma/figma-use | Plugin API scripts, muito técnico/baixo nível |
| figma/figma-create-new-file | Cria arquivo em branco, utilitário puro |
| figma/figma-generate-library | Gera library de DS a partir de codebase — Stage 3 |
| social-media-designer | Foco em social media, não LP |

### Skills que passaram o filtro (10)
1. figma/figma-implement-design
2. figma/figma-generate-design
3. figma/figma-create-design-system-rules
4. figma/figma-code-connect-components
5. anthropics/frontend-design
6. erichowens/web-design-expert
7. vercel-labs/web-design-guidelines
8. borghei/brand-strategist
9. microsoft/frontend-design-review
10. coreyhaines31/page-cro

---

## 2. TOP SKILLS SELECIONADAS

### TIER 1 — Essenciais (instalar imediatamente)

---

#### figma/figma-implement-design
**URL de instalação:** `npx skills add https://github.com/figma/figma-implement-design --skill figma-implement-design`
**URL de referência:** https://officialskills.sh/figma/skills/figma-implement-design

**O que faz:**
Traduz designs Figma em código de produção com fidelidade pixel-perfect. Automatiza o workflow completo design-to-code: lê o arquivo Figma via MCP, extrai context, valida output contra screenshot do mesmo arquivo.

**O que extrair para Camila:**
- Workflow: selecionar frame no Figma → pedir implementação → Claude chama `get_design_context` + `get_screenshot` + `get_code_connect_map` automaticamente
- Converte URLs de componentes em React components tipados
- Extrai design tokens para substituir hardcoded styles
- Gera layouts de página completa a partir de frames
- Valida output visualmente (screenshot comparison)

**Gap que cobre:** #1 Figma MCP workflow + #5 Handoff Figma → React/Tailwind

**Por que é essencial:** Esta é a skill core do workflow da Camila. Define como Felipe recebe o código.

---

#### figma/figma-create-design-system-rules
**URL de referência:** https://officialskills.sh/figma/skills/figma-create-design-system-rules

**O que faz:**
Gera arquivo de regras do projeto (`.figma/rules/` ou `instructions/`) com as convenções de design system, componentes existentes e tech stack. O agente usa esse arquivo em todo workflow subsequente para não inventar padrões.

**O que extrair para Camila:**
- Rodar UMA VEZ por projeto para criar o arquivo de regras
- O arquivo especifica: stack (React/Tailwind), componentes disponíveis, tokens ativos, padrões de nomenclatura
- Garante consistência entre projetos diferentes de clientes
- Salvar junto ao repositório do projeto para que Felipe também use

**Gap que cobre:** #2 Design system em Figma (tokens/variables) + #5 Handoff workflow

**Por que é essencial:** Sem esse arquivo, cada sessão começa do zero. Com ele, o agente "conhece" o projeto.

---

#### figma/figma-generate-design
**URL de instalação:** `npx skills add https://github.com/figma/figma-generate-design --skill figma-generate-design`
**URL de referência:** https://officialskills.sh/figma/skills/figma-generate-design

**O que faz:**
Gera ou atualiza telas Figma a partir de código existente ou especificação textual. Usa componentes e tokens do design system já publicado — não cria do zero com primitivos hardcoded.

**O que extrair para Camila:**
- Direção inversa do figma-implement: código → Figma (útil quando Felipe muda algo no código e precisa sincronizar o Figma)
- Criar wireframes/mockups a partir de briefing textual do cliente
- Manter design system e código em sincronia (evita design drift)
- Usa `search_design_system` para reutilizar components antes de criar novos

**Gap que cobre:** #1 Figma MCP workflow + #2 Design system

---

#### figma/figma-code-connect-components
**URL de referência:** https://officialskills.sh/figma/skills/figma-code-connect-components

**O que faz:**
Conecta componentes Figma (design) aos componentes React/Tailwind correspondentes no codebase (código). Uma vez mapeado, quando Claude implementa qualquer design, ele usa o componente real do projeto — não gera código duplicado.

**O que extrair para Camila:**
- Rodar após figma-create-design-system-rules para mapear componentes
- Fluxo: `get_code_connect_suggestions` → revisar → `send_code_connect_mappings`
- Exemplos: componente "Button/Primary" no Figma → mapeia para `<Button variant="primary">` em React
- Configura UMA VEZ por projeto, depois é automático
- Sem isso: Claude gera botão novo a cada LP. Com isso: reutiliza o componente existente

**Gap que cobre:** #1 Figma MCP workflow + #5 Handoff

---

### TIER 2 — Importantes (instalar junto)

---

#### anthropics/frontend-design
**URL de referência:** https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md

**O que faz:**
Skill de design de interfaces web de produção. Aplica pensamento estético intencional: tipografia distinta, paletas coesas, composição espacial ousada, micro-interações estratégicas. Evita estéticas genéricas de IA.

**O que extrair para Camila:**
- Framework de decisão estética: propósito → audiência → tom visual → paleta → tipografia → layout
- Princípio central: cada escolha tem intenção (não decoração aleatória)
- LPs memoráveis = hierarquia visual clara + escolhas tipográficas únicas + espaço negativo generoso
- Útil para briefing com cliente: traduz "quero algo moderno" em direção estética específica
- Complementa ui-ux-pro-max local (mais focado em execução técnica)

**Gap que cobre:** #3 Identidade visual para pequenos negócios + #4 LP design focado em conversão

---

#### erichowens/web-design-expert
**URL de referência:** https://skills.sh/erichowens/some_claude_skills/web-design-expert

**O que faz:**
Especialista em sistemas visuais para web com foco em conversão. Opera em 3 etapas: contexto de negócio → direção visual (mood boards, paleta OKLCH, tipografia) → especificações técnicas.

**O que extrair para Camila:**
- Framework de descoberta pré-design: objetivo primário + público-alvo + proposição de valor
- Hero section deve ter value proposition + primary CTA acima da dobra (80% da atenção)
- Usa OKLCH em vez de hex para paleta com uniformidade perceptual e WCAG automático
- Anti-patterns para LPs de pequenos negócios: hero sliders, carousels, hamburger em desktop
- Entrega padronizada: Brand Identity Guide + Design Specifications + Component Examples
- Pergunta diagnóstica: "se a marca fosse uma pessoa, como se vestiria?" → orienta estética

**Gap que cobre:** #3 Identidade visual para pequenos negócios + #4 LP design focado em conversão

---

#### vercel-labs/web-design-guidelines
**URL de instalação:** `npx skills add https://github.com/vercel-labs/web-design-guidelines --skill web-design-guidelines`

**O que faz:**
Busca as diretrizes mais recentes de design web do Vercel Labs e audita código UI contra elas. Reporta violações de acessibilidade, UX patterns e best practices. Sempre atualizado (não documentação estática).

**O que extrair para Camila:**
- Rodar antes de entregar handoff para Felipe: valida que o design atende padrões atuais
- Audita: acessibilidade (contraste, ARIA), padrões UX, performance visual
- Particularmente útil para: verificar hierarquia de CTAs, estrutura de forms, mobile responsiveness
- Use como checklist pré-entrega ao invés de revisão manual

**Gap que cobre:** #4 LP design focado em conversão (validação objetiva)

---

#### borghei/brand-strategist
**URL de referência:** https://skills.sh/borghei/claude-skills/brand-strategist

**O que faz:**
Estrategista sênior de marca. Define posicionamento, sistema de identidade e arquitetura de mensagens. Usa framework "only-we test" (competidores não poderiam fazer a mesma afirmação).

**O que extrair para Camila:**
- Usar na fase de briefing, antes de abrir o Figma
- Pilar de identidade visual: logo + paleta de cores + tipografia como OUTPUT da estratégia, não input
- Framework de posicionamento: público-alvo + categoria + benefício chave + pontos de prova → vira a copy do hero
- Matrizes de posicionamento competitivo: diferencia barbearia/salão dos concorrentes locais
- LIMITAR USO: skill foca em estratégia. Execução visual fica com web-design-expert + Figma

**Gap que cobre:** #3 Identidade visual para pequenos negócios (fase estratégica)

---

#### coreyhaines31/page-cro
**URL de referência:** https://github.com/coreyhaines31/marketingskills/tree/main/skills/page-cro

**O que faz:**
Melhora taxas de conversão em marketing pages. Analisa hierarquia, CTAs, social proof, friction points e fluxo de atenção. Foco em resultado (conversão), não estética.

**O que extrair para Camila:**
- Cheklist de CRO para LPs de pequenos negócios: CTA acima da dobra, número de telefone visível, depoimentos com foto, urgência/escassez
- Social proof visual para negócios locais: fotos reais do espaço, antes/depois (barbearia/salão), avaliações Google
- Hierarquia de informação: Problema → Solução → Prova → CTA → Objeções → CTA final
- Elementos que destroem conversão: excesso de links de saída, form longo, sem preço visível
- Rodar APÓS design pronto como auditoria antes de entregar para Felipe

**Gap que cobre:** #4 LP design focado em conversão

---

## 3. FIGMA MCP — COMO A CAMILA DEVE USAR

### Tools disponíveis no MCP ativo

O Figma MCP (`mcp__claude_ai_Figma`) já está instalado. As tools são divididas em duas categorias:

#### Tools de LEITURA (Design → Contexto)

| Tool | O que faz | Quando usar |
|------|-----------|------------|
| `get_design_context` | Extrai contexto completo de design para geração de código. Retorna código React+Tailwind + screenshot + hints. **Tool principal do workflow.** | Sempre que Felipe precisa implementar um componente ou seção |
| `get_variable_defs` | Retorna todas as variáveis/tokens usados na seleção (cores, espaçamento, tipografia) | Ao criar design system novo: listar tokens antes de codificar |
| `get_screenshot` | Captura screenshot da seleção atual | Complementar ao get_design_context para validar fidelidade visual |
| `get_metadata` | XML com IDs, nomes, tipos, posição e tamanhos | Para frames muito grandes: mapear estrutura antes de chamar get_design_context por partes |
| `get_figjam` | Converte diagramas FigJam para XML | Para fluxos de usuário e arquitetura de informação |
| `get_code_connect_map` | Recupera mapeamentos Figma node → componente React existente | Verificar se componente já existe antes de pedir novo código |

#### Tools de ESCRITA (Código/Descrição → Figma)

| Tool | O que faz | Quando usar |
|------|-----------|------------|
| `use_figma` | Tool genérica: cria/edita/deleta qualquer objeto no canvas (frames, componentes, variáveis, estilos) | Criar frames do zero, ajustar componentes, criar coleções de variáveis |
| `search_design_system` | Busca componentes, variáveis e estilos nas libraries conectadas | Antes de criar componente novo: verificar se já existe na library |
| `create_design_system_rules` | Gera arquivo de regras do projeto para uso em todo workflow | Setup inicial de cada projeto de cliente |
| `generate_diagram` | Gera diagrama FigJam a partir de descrição natural (via Mermaid) | Mapear fluxos de usuário, sitemap de LP |
| `get_code_connect_suggestions` | Detecta e sugere mapeamentos automáticos Figma ↔ componentes | Ao iniciar Code Connect num projeto com codebase existente |
| `send_code_connect_mappings` | Confirma mapeamentos sugeridos | Após revisar get_code_connect_suggestions |
| `add_code_connect_map` | Mapeia manualmente um node Figma para componente React | Quando sugestão automática não mapeou corretamente |
| `create_new_file` | Cria novo arquivo Design ou FigJam | Iniciar projeto novo de cliente |

### Workflow recomendado por fase de projeto

#### FASE 1: Setup do projeto (uma vez)
```
1. create_new_file → criar arquivo Figma para o cliente
2. create_design_system_rules → gerar arquivo de regras (stack: React/Tailwind, tokens, padrões)
3. use_figma → criar collections de variáveis (cores, espaçamento, tipografia)
4. [se codebase já existe] get_code_connect_suggestions → send_code_connect_mappings
```

#### FASE 2: Design da LP (iterativo)
```
1. Briefing com brand-strategist → posicionamento + identidade
2. use_figma → montar frames e componentes usando design system
3. search_design_system → verificar componentes existentes antes de criar novos
4. [Camila designers no Figma normalmente]
```

#### FASE 3: Handoff para Felipe
```
1. get_design_context (por seção/componente) → gera código React+Tailwind
2. get_screenshot → valida fidelidade visual
3. get_variable_defs → confirma tokens usados
4. [Felipe recebe código já adaptado ao codebase do projeto]
5. vercel-labs/web-design-guidelines → auditoria pré-entrega
```

#### FASE 4: Sincronização (manutenção)
```
1. [Felipe muda algo no código] → figma-generate-design → atualiza Figma
2. [Camila muda algo no Figma] → get_design_context → Felipe implementa delta
```

### Limitação importante a conhecer
- `use_figma`, `search_design_system`, `create_new_file`, `generate_diagram`, `get_code_connect_suggestions` são **Remote server only** — funcionam via Figma MCP remoto (já ativo na configuração atual)
- `get_design_context` funciona melhor com seleção ativa no Figma Desktop; via remote server requer URL do node
- Free plan Figma: limite de usos mensais em algumas features. Recomendar plano Professional para Camila

---

## 4. GAPS RESTANTES PARA STAGE 3

### Gap A — Design system para nicho específico (alta prioridade)
**O que falta:** Kit de componentes Figma prontos para barbearia/salão/personal trainer. Paletas e tipografias testadas para esses nichos.
**Ação sugerida:** Pesquisar Figma Community (templates de LP para negócios locais brasileiros) + Dribbble referências de conversão para nichos locais.

### Gap B — figma/figma-generate-library (não instalada ainda)
**O que é:** Gera library de design system completa a partir do codebase React/Tailwind existente.
**Por que aguardar:** Requer codebase existente para fazer sentido. Instalar assim que Felipe tiver os primeiros componentes prontos.
**URL:** https://officialskills.sh/figma/skills/figma-generate-library

### Gap C — Tokens workflow (Figma Variables → Tailwind config)
**O que falta:** Pipeline específico de como as variáveis criadas com `use_figma`/`get_variable_defs` se transformam em `tailwind.config.js`. Não coberto pelas skills atuais de forma explícita.
**Ação sugerida:** Pesquisar Token Studio (plugin Figma) ou Style Dictionary como bridge entre Figma Variables e Tailwind CSS custom properties.

### Gap D — Auto-layout avançado e Figma components/variants
**O que falta:** Conhecimento detalhado de como estruturar componentes Figma com variants (estados: hover, active, disabled) para que `get_design_context` gere código de estados corretamente.
**Ação sugerida:** Skill ou documentação específica sobre Figma Component Properties e como elas mapeiam para props React.

### Gap E — CRO específico para mercado brasileiro/local
**O que falta:** Padrões de conversão testados para pequenos negócios locais no Brasil: quais CTAs convertem (WhatsApp vs form vs telefone), posicionamento de preço, prova social local (Google Reviews).
**Ação sugerida:** Pesquisa específica de benchmarks BR + testes A/B de LPs para barbearia/salão.

---

## RESUMO EXECUTIVO

### Skills para instalar agora (ordem de prioridade)
1. `figma/figma-implement-design` — core do handoff Figma→React
2. `figma/figma-create-design-system-rules` — setup de projeto
3. `figma/figma-code-connect-components` — mapeamento componentes
4. `figma/figma-generate-design` — sincronização bidirecional
5. `erichowens/web-design-expert` — framework de decisão visual + CRO
6. `vercel-labs/web-design-guidelines` — auditoria pré-entrega
7. `borghei/brand-strategist` — fase de briefing/estratégia
8. `coreyhaines31/page-cro` — revisão de conversão final

### Skills locais já existentes — confirmadas como suficientes
- `ui-ux-pro-max` — cobre princípios gerais de UI/UX e execução técnica (mantida)
- `ui-animation` — cobre motion design (mantida, não duplicar)
- `image-analysis` — extração de paleta (mantida)

### Figma MCP — status
O MCP já está ativo. A Camila pode usar as tools imediatamente. Prioridade: rodar `create_design_system_rules` e `get_code_connect_suggestions` no primeiro projeto com Felipe para estabelecer o pipeline.
