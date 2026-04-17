# Operacional Figma MCP — Guia de Uso Completo
**Versão:** Figma MCP 2025 | 2026-04-13

---

## 1. Cada Tool — Referência Completa

### get_design_context
**Quando usar:** Sempre que Felipe precisa implementar um componente ou seção. Tool principal do handoff.
**O que retorna:** Código React+Tailwind + screenshot + hints de tokens + Code Connect (se disponível)
**Parâmetros principais:**
- `nodeId` — ID do node/frame selecionado (formato `123:456`)
- `fileKey` — chave do arquivo Figma (da URL: `figma.com/design/:fileKey/...`)

**Exemplo de uso:**
```
get_design_context(fileKey: "abc123", nodeId: "45:678")
→ Retorna código de referência React + screenshot da seção
```

**Atenção:**
- Chamar por seção, não por página inteira (resultado mais preciso e dentro do rate limit)
- Servidor remoto: requer URL do node. Desktop: funciona com seleção ativa
- Revisar output: valores hardcoded e ausência de width/height em imagens são comuns

---

### use_figma
**Quando usar:** Criar/editar no canvas — frames, componentes, variables, estilos.
**Requisito:** Figma Desktop aberto com plugin ativo + acesso de edição ao arquivo.
**O que faz:** Executa qualquer operação da Plugin API do Figma via linguagem natural.

**Exemplos de uso:**
```
use_figma("Crie um frame de 390x844 para hero mobile com background #1a1a1a")
use_figma("Adicione coleção de variáveis 'Colors' com primary: #c8860a e bg: #1a1a1a")
use_figma("Crie componente Button com variants: Primary/Default, Primary/Hover, Secondary/Default")
```

---

### get_variable_defs
**Quando usar:** Ao criar design system novo — listar todos os tokens antes de codificar. Também usar para confirmar tokens usados em uma seção antes do handoff.
**Parâmetros:** `nodeId`, `fileKey`
**O que retorna:** Lista completa de variáveis/tokens: cores, espaçamento, tipografia, raios, sombras.

---

### search_design_system
**Quando usar:** ANTES de criar qualquer componente novo — verificar se já existe na library.
**O que faz:** Busca componentes, variáveis e estilos nas libraries conectadas ao arquivo.
**Parâmetros:** `query` (nome do componente ou estilo)

**Exemplo:**
```
search_design_system("Button")
→ Retorna componentes Button existentes na library + variantes disponíveis
```

---

### get_screenshot
**Quando usar:** Complementar ao `get_design_context` para validar fidelidade visual. Capturar preview de seção para revisão com o cliente ou com o Joaquim.
**Parâmetros:** `nodeId`, `fileKey`

---

### get_metadata
**Quando usar:** Para frames muito grandes — mapear a estrutura antes de chamar `get_design_context` por partes. Identifica IDs de nodes internos.
**O que retorna:** XML com IDs, nomes, tipos, posição e tamanhos de todos os nodes.

---

### create_design_system_rules
**Quando usar:** Setup inicial de cada projeto de cliente — rodar UMA VEZ.
**O que faz:** Gera arquivo de regras do projeto especificando stack, componentes existentes, tokens ativos, padrões de nomenclatura.
**Onde salvar:** No repositório do projeto (Felipe também usa o arquivo).

---

### create_new_file
**Quando usar:** Iniciar projeto novo de cliente.
**O que faz:** Cria novo arquivo Design ou FigJam.
**Parâmetros:** `name`, `type` (design ou figjam)

---

### get_code_connect_map
**Quando usar:** Verificar se componente já tem mapeamento Figma → React antes de pedir novo código.
**Disponível em:** Todos os planos (apenas leitura — não cria novos mapeamentos no Professional).

---

### generate_diagram
**Quando usar:** Mapear fluxos de usuário, sitemap de LP, arquitetura de informação.
**O que faz:** Gera diagrama FigJam a partir de descrição natural (via Mermaid).

---

## 2. Workflow por Fase de Projeto

### FASE 1 — Setup do Projeto (uma vez por cliente)

```
1. create_new_file → criar arquivo Figma para o cliente
2. use_figma → criar coleções de Variables:
   - Colors (primary, secondary, accent, bg, text, muted)
   - Typography (font-family, font-sizes, line-heights)
   - Spacing (scale 4px base: 4, 8, 12, 16, 24, 32, 48, 64, 96)
   - Radii (sm: 4px, md: 8px, lg: 16px, full: 9999px)
3. create_design_system_rules → gerar arquivo de regras (stack: React/Tailwind, tokens, padrões)
4. Plugin Token Exporter → exportar Variables como Tailwind → Felipe integra ao tailwind.config.js
```

### FASE 2 — Design da LP (iterativo)

```
1. Consultar ui-ux-pro-max → princípios de decisão visual
2. image-analysis (se houver referências visuais) → extrair paleta antes de começar
3. search_design_system → verificar componentes existentes antes de criar novos
4. use_figma → montar frames e componentes usando design system
   - Hero: frame 1440px desktop + 390px mobile (separados)
   - Nomenclatura: "LP-[cliente]-[seção]-[dispositivo]" (ex: LP-barbeiro-joao-hero-mobile)
5. get_screenshot → revisar visualmente antes de seguir
```

### FASE 3 — Handoff para Felipe

```
1. get_design_context (por seção, não por página)
   → Gera código de referência React+Tailwind
2. get_screenshot → validar fidelidade visual do código gerado
3. get_variable_defs → confirmar tokens usados e documentar no DESIGN_SYSTEM.md
4. Revisar output:
   - Mapear componentes para os do codebase do Felipe
   - Adicionar width/height em todas as imagens (previne CLS)
   - Substituir valores hardcoded por tokens do projeto
5. Entregar DESIGN_SYSTEM.md com:
   - Mapeamento componente Figma → componente React (workaround Code Connect)
   - Tokens documentados
   - Specs de animação (se houver)
   - Frames mobile + desktop com dimensões
```

### FASE 4 — Sincronização (manutenção)

```
Se Felipe mudou algo no código:
  → Ajustar no Figma via use_figma para manter sincronia

Se Camila mudou algo no Figma:
  → get_design_context da seção modificada → Felipe implementa o delta
  → Atualizar DESIGN_SYSTEM.md com a mudança
```

---

## 3. Pipeline de Tokens — Token Exporter vs Token Studio

### Token Exporter (recomendado agora)

**Quando usar:** Projetos iniciais, clientes únicos, sem necessidade de sync automático.
**Plugin:** Figma Community `figma.com/community/plugin/1345069854741911632`

**Pipeline:**
```
1. Criar coleções de Variables no Figma (Colors, Typography, Spacing)
2. Abrir plugin Figma Token Exporter
3. Selecionar coleção → exportar como formato Tailwind
4. Colar conteúdo em tailwind.config.js do projeto
5. Definir CSS custom properties em globals.css para tokens de tema
```

**Formato de output esperado:**
```js
// tailwind.config.js
theme: {
  extend: {
    colors: {
      primary: 'var(--color-primary)',
      // ...
    }
  }
}
```

### Token Studio + Style Dictionary (para escala)

**Quando usar:** Múltiplos clientes ativos simultaneamente, com sync automático via GitHub.
**Plugin:** Token Studio (tokens-studio/figma-plugin no GitHub)

**Pipeline:**
```
1. Token Studio no Figma → exportar tokens como JSON para o repositório
2. Style Dictionary (Amazon) → transformar JSON em tailwind.config.js
3. GitHub Actions → automatizar sync a cada push
```

**Referência:** `docs.tokens.studio/transform-tokens/style-dictionary`

---

## 4. Workaround Code Connect no Professional

Sem Code Connect (disponível só em Organization+), o mapeamento manual via `DESIGN_SYSTEM.md` é obrigatório.

### Estrutura do DESIGN_SYSTEM.md

```markdown
# Design System — [Nome do Cliente]

## Tokens
| Token Figma | CSS Variable | Tailwind Class |
|-------------|-------------|----------------|
| Colors/Primary | --color-primary: #c8860a | text-primary, bg-primary |
| Typography/Heading-1 | --font-size-h1: 48px | text-5xl |

## Mapeamento de Componentes
| Componente Figma | Componente React | Arquivo | Props mapeadas |
|-----------------|-----------------|---------|----------------|
| Button/Primary | `<Button variant="primary">` | src/components/Button.tsx | variant: 'primary' \| 'secondary', size: 'sm' \| 'md' \| 'lg' |
| Card/Serviço | `<ServiceCard>` | src/components/ServiceCard.tsx | title, price, image, onCta |

## Estados por Componente
| Componente | Estados em Variants | Como implementar |
|------------|--------------------|-----------------:|
| Button | Default, Hover, Loading, Disabled | className={isLoading ? 'opacity-70 cursor-wait' : ''} |

## Imagens — Dimensões Obrigatórias
| Imagem | Width | Height | Observação |
|--------|-------|--------|-----------|
| Hero background | 1440px | 800px | Prioridade LCP — `loading="eager"` |
| Foto de equipe | 400px | 500px | Lazy load OK |

## Specs de Animação
[Ver arquivo ui-animation-specs.md se houver]
```

---

## 5. Nomenclatura e Organização de Arquivos Figma

### Estrutura de páginas por projeto

```
[Nome do Cliente]
├── 🎨 Design System
│   ├── Variables (Colors, Typography, Spacing)
│   ├── Components (Button, Card, Form, Nav, Footer)
│   └── Styles (Shadows, Gradients)
├── 📱 Mobile (390px)
│   ├── Hero
│   ├── Serviços
│   ├── [demais seções]
│   └── Rodapé
├── 🖥️ Desktop (1440px)
│   ├── Hero
│   ├── Serviços
│   ├── [demais seções]
│   └── Rodapé
└── 📋 Handoff
    └── Annotations, dimensões e specs para Felipe
```

### Naming conventions

- **Frames:** `[Projeto]-[Seção]-[Device]` → `barbeiro-hero-mobile`
- **Componentes:** `[Categoria]/[Nome]/[Variant]` → `Button/Primary/Default`
- **Variables:** `[Categoria]/[Nome]` → `Colors/Primary`
- **Camadas:** sem espaços, sem caracteres especiais → `hero-background`, `cta-button`
