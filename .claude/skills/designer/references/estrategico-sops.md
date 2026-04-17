# SOPs Operacionais — Designer
**Versão:** 2026-04-13

---

## SOP 1 — Brand Sprint (1–2h para novo cliente)

**Objetivo:** Definir identidade básica antes de abrir o Figma.

### Inputs necessários
- Brief do cliente (via Joaquim)
- Referências visuais do cliente (imagens, URLs, exemplos que ele gosta/não gosta)
- Copy inicial (se disponível) — headline, serviços, proposta de valor

### Passo a passo

**STEP 1 — Leitura de contexto (10min)**
```
Ler .claude/brand/:
  - voice.md → tom da marca do cliente
  - audience.md → público-alvo real
  - products.md → serviços e proposta de valor
```

**STEP 2 — Extração de paleta (15min)**
```
Se o cliente enviou referências visuais:
  → Chamar image-analysis em cada imagem
  → Extrair paleta dominante + paleta de acento
  → Anotar: quais cores evocam os adjetivos da marca?
```

**STEP 3 — Posicionamento (20min)**
```
Definir:
  1. Público-alvo (quem vem até o negócio)
  2. Conceito visual (1 palavra): vintage | moderno | premium | jovem | artesanal | urbano
  3. Pergunta diagnóstica: "se a marca fosse uma pessoa, como se vestiria?"
  4. Teste only-we: o que só este negócio pode afirmar com honestidade?
```

**STEP 4 — Sistema visual (30–40min)**
```
No Figma:
  1. use_figma → criar arquivo do cliente
  2. use_figma → criar coleção de Variables:
     - Colors: primary, secondary, accent, bg, bg-surface, text, text-muted
     - Typography: font-family-heading, font-family-body, sizes (h1–h4, body, small)
     - Spacing: 4, 8, 12, 16, 24, 32, 48, 64, 96 (base 4px)
     - Radii: none, sm(4), md(8), lg(16), full(9999)
  3. Testar paleta: fundo + texto principal + CTA — verificar contraste WCAG AA
```

**STEP 5 — Mini brand guide (20min)**
```
Criar frame "Brand Guide" no Figma com:
  - Logo + variações
  - Paleta com nome de cada cor e valor HEX
  - Tipografia: fontes + hierarquia visual
  - Tom em 3 adjetivos
  - Exemplos de uso correto/incorreto do logo
```

**OUTPUT:** Arquivo Figma com design system pronto + `DESIGN_SYSTEM.md` com tokens para Felipe

---

## SOP 2 — Setup de Projeto Figma

**Objetivo:** Criar estrutura consistente para qualquer projeto de cliente.

### Estrutura de páginas

```
[Nome do Cliente — LP]
├── 🎨 Design System
│   ├── Variables (Colors, Typography, Spacing, Radii)
│   ├── Components
│   │   ├── Buttons (Primary, Secondary, Ghost — 3 variantes × 4 estados)
│   │   ├── Cards (Serviço, Depoimento, Equipe)
│   │   ├── Forms (Input, Select, Textarea — Default, Focus, Error, Filled)
│   │   ├── Navigation (Header mobile + desktop)
│   │   └── Footer
│   └── Styles (Shadows, Gradients, Icons)
├── 📱 Mobile (390px)
│   └── [1 frame por seção — nomeados]
├── 🖥️ Desktop (1440px)
│   └── [1 frame por seção — nomeados]
└── 📋 Handoff
    └── Annotations e specs para Felipe
```

### Naming conventions obrigatórias

| Elemento | Formato | Exemplo |
|----------|---------|---------|
| Arquivo | `[cliente]-lp` | `barbeiro-joao-lp` |
| Frame de seção | `[cliente]-[secao]-[device]` | `barbeiro-joao-hero-mobile` |
| Componente | `[Categoria]/[Nome]/[Variant]` | `Button/Primary/Hover` |
| Variable | `[Categoria]/[Nome]` | `Colors/Primary` |
| Camada | kebab-case sem caracteres especiais | `hero-background` |

### Configurações obrigatórias

```
- Grid: 12 colunas, gutter 24px (desktop) / 16px (mobile)
- Auto-layout em todos os frames de seção (facilita responsive)
- Library publicada antes de começar o design
- Todas as cores como Variables (nunca hardcoded em camadas)
```

---

## SOP 3 — Handoff para Felipe

**Objetivo:** Garantir que Felipe tem tudo o que precisa para implementar sem volta.

### O que o DESIGN_SYSTEM.md deve conter

```markdown
# Design System — [Nome do Cliente]
**Versão:** X.X | **Data:** YYYY-MM-DD | **Link Figma:** [URL]

## 1. Tokens

### Cores
| Token Figma | CSS Variable | Tailwind | Valor |
|-------------|-------------|----------|-------|
| Colors/Primary | --color-primary | text-primary, bg-primary | #c8860a |
| Colors/BG | --color-bg | bg-background | #1a1a1a |

### Tipografia
| Token Figma | CSS Variable | Tailwind | Valor |
|-------------|-------------|----------|-------|
| Typography/Heading-1 | --font-size-h1 | text-5xl | 48px |

### Espaçamento
[Tabela de spacing tokens]

## 2. Mapeamento de Componentes

| Componente Figma | Componente React | Arquivo | Props mapeadas |
|-----------------|-----------------|---------|----------------|
| Button/Primary | `<Button variant="primary">` | src/components/Button.tsx | variant, size, children, icon?, disabled? |

## 3. Estados por Componente

| Componente | Variants no Figma | Estados a implementar |
|------------|------------------|-----------------------|
| Button | Default, Hover, Loading, Disabled | className dinâmico + aria-disabled |

## 4. Imagens — Dimensões Obrigatórias

| Imagem | Width | Height | Loading | Observação |
|--------|-------|--------|---------|-----------|
| Hero bg | 1440px | 800px | eager | LCP — prioridade máxima |
| Foto equipe | 400px | 500px | lazy | aspect-ratio: 4/5 |

## 5. Specs de Animação

[Se houver — referenciar ui-animation-specs.md]

## 6. Breakpoints

| Breakpoint | Width | Uso |
|-----------|-------|-----|
| mobile | 390px | Frame Figma principal mobile |
| tablet | 768px | Interpolação — sem frame dedicado |
| desktop | 1440px | Frame Figma principal desktop |
```

### Checklist antes de entregar handoff

- [ ] get_design_context chamado por seção (não por página inteira)
- [ ] get_screenshot feito para cada seção — validar fidelidade visual
- [ ] Todos os valores hardcoded mapeados para tokens do projeto
- [ ] Dimensões explícitas em TODAS as imagens (width + height)
- [ ] Variants criadas para todos os estados de cada componente
- [ ] DESIGN_SYSTEM.md escrito e revisado
- [ ] Anti-AI checklist passado (5 perguntas)
- [ ] Link do Figma compartilhado com Felipe (can view)

---

## SOP 4 — Auditoria CRO Visual (Pré-Entrega)

**Objetivo:** Garantir que o design converte antes de passar para o Felipe.

### Rodar em ordem

**1. CTA e hierarquia visual**
- [ ] CTA WhatsApp visível acima da dobra no mobile (viewport 375px)
- [ ] Sticky CTA ativo — acompanha o scroll
- [ ] CTA após cada bloco de prova social
- [ ] Botão CTA tem contraste suficiente (WCAG AA: ≥4.5:1)
- [ ] Hierarquia de chamadas: 1 CTA primário dominante por tela

**2. Prova social**
- [ ] Depoimentos com nome + cidade/bairro + foto
- [ ] Badge de avaliação Google acima da dobra ou próximo ao hero
- [ ] Fotos reais de trabalhos realizados (não ilustrações ou stock)

**3. Formulário (se houver)**
- [ ] Máximo 4 campos visíveis
- [ ] Label acima do campo (não placeholder como label)
- [ ] Estado de erro visível em variants

**4. Preço e oferta**
- [ ] Preço ou faixa visível na seção de serviços
- [ ] Sem objeções óbvias sem resposta (FAQ cobre as principais?)

**5. Localização e contato (negócio presencial)**
- [ ] Endereço com bairro visível
- [ ] Google Maps embed
- [ ] Horários com destaque para diferencial

**6. Performance visual**
- [ ] Nenhuma imagem sem width + height documentados
- [ ] Hero sem carousel/slider
- [ ] Fontes web carregáveis (Google Fonts ou font-face com fallback)

---

## SOP 5 — Manutenção do Design System

**Objetivo:** Manter Figma e codebase em sincronia quando Felipe adiciona componentes.

### Trigger: Felipe adicionou componente novo ao codebase

```
1. Felipe informa: novo componente criado (nome + props + estados)
2. Camila cria componente correspondente no Figma:
   use_figma → criar componente com mesmas variants e states
3. Atualizar DESIGN_SYSTEM.md:
   - Adicionar linha na tabela de mapeamento de componentes
   - Documentar props e estados
4. Publicar library atualizada
5. Confirmar com Felipe que o mapeamento está correto
```

### Trigger: Camila mudou token no Figma (cor, tipografia, espaçamento)

```
1. Identificar o token modificado (get_variable_defs para confirmar)
2. Re-exportar via Plugin Token Exporter → novo tailwind.config.js
3. Informar Felipe: qual token mudou + novo valor
4. Felipe atualiza tailwind.config.js e testa responsividade
5. Atualizar DESIGN_SYSTEM.md com novo valor do token
```

### Trigger: Mudança de escopo (nova seção adicionada)

```
1. Criar frame da nova seção no Figma (mobile + desktop)
2. Anti-AI review na nova seção antes de avançar
3. get_design_context da nova seção
4. Atualizar DESIGN_SYSTEM.md com componentes e imagens da nova seção
5. Entregar handoff incremental ao Felipe
```

### Cadência recomendada de revisão

- **Por projeto:** Revisão de DS ao finalizar cada LP (componentes reutilizáveis para próximas)
- **Mensal:** Verificar se Felipe tem componentes novos não mapeados no Figma
- **A cada novo nicho:** Criar kit de seções específico no Figma (barbearia, salão, personal)
