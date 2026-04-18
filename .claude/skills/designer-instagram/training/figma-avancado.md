# Figma Avancado — Design System para Instagram Editorial

> Material de treinamento — Vitoria, Designer Instagram Triforce Auto
> Canal: curadoria de IA | Paleta: #FF6B00 / #0A0A0A / #F5F0EB | Referencia: @hollyfield.ia

---

## 1. Logica de Design System antes de criar posts

Antes de abrir um frame novo, pergunte: existe componente para esse formato?

O design system da Triforce Auto tem tres camadas:
- **Tokens** — cores, tipografia, espacamento como variaveis
- **Componentes** — cover, slide interno, reels cover como components reutilizaveis
- **Templates** — combinacoes de componentes prontas para preencher (feed semanal, carrossel, card unico)

Nunca crie um post diretamente. Crie o componente, depois instancie.

---

## 2. Variables — a espinha do sistema

### Configurar a paleta como variables (nao estilos de cor)

Vantagem das variables sobre styles: voce pode criar **modos** (ex: modo dark e modo light) e trocar tudo com um clique.

**Estrutura recomendada para Triforce Auto:**

```
Collection: Brand Colors
  Mode: Default
    brand/primary     → #FF6B00
    brand/dark        → #0A0A0A
    brand/light       → #F5F0EB
    brand/white       → #FFFFFF

Collection: Typography Scale
  Mode: Default
    type/headline     → 48px, Bold
    type/subhead      → 24px, SemiBold
    type/body         → 16px, Regular
    type/label        → 12px, Medium
    type/cta          → 14px, Bold

Collection: Spacing
  Mode: Default
    space/xs          → 8
    space/sm          → 16
    space/md          → 24
    space/lg          → 48
    space/xl          → 64
```

### Como aplicar variables em componentes

1. Selecione o elemento (fundo, texto, stroke)
2. No painel de cor, clique no icone de biblioteca (quatro quadrados)
3. Escolha a variable correspondente — nunca use hex direto em componentes
4. Resultado: mudar a variable atualiza TUDO no sistema instantaneamente

---

## 3. Auto Layout — como funciona na pratica

Auto Layout e o motor que torna templates reaproveitaveis. Sem ele, voce ajusta elemento por elemento.

### Configuracoes essenciais por tipo de frame

**Cover editorial (1080x1080 ou 1080x1350):**
```
Frame principal: Fixed width/height (nao responsivo)
Container interno: Auto Layout vertical
  - Padding: 64px horizontal, 80px vertical
  - Gap entre elementos: 24px (space/md)
  - Alignment: bottom-left (texto ancorado na base)
```

**Slide interno de carrossel:**
```
Frame: Fixed 1080x1080
Container de conteudo: Auto Layout vertical
  - Padding: 64px todos os lados
  - Gap: 32px
  - Alignment: top-left
Badge numerador: Auto Layout horizontal com padding 12x6
```

**Regra de ouro:** qualquer elemento que vai mudar de tamanho com o conteudo (headline com texto variavel, badge com numero) precisa estar em Auto Layout. Elementos fixos (logo, gradiente de fundo) ficam fora.

### Grid Auto Layout (Config 2025)

O Figma lancou Grid Auto Layout em 2025 — permite definir colunas e linhas dentro de um frame automaticamente. Para o feed editorial:

```
Grid de producao semanal:
  Columns: 3
  Gap horizontal: 24px
  Gap vertical: 24px
  Padding: 0
```

Use para organizar o canvas de producao semanal (6 posts = 2 linhas de 3).

---

## 4. Component Properties — o que muda sem quebrar o sistema

Component Properties sao os controles expostos de um componente — o que voce permite que quem instancia o componente altere sem precisar entrar no master.

### Properties essenciais no componente Cover:

| Property | Tipo | Valores |
|---|---|---|
| headline | Text | Texto editavel |
| has_badge | Boolean | true/false (mostra/esconde tag "#IA") |
| image_style | Variant | dark_photo / gradient / abstract |
| logo_position | Variant | bottom_left / bottom_right |

### Properties essenciais no componente Slide Interno:

| Property | Tipo | Valores |
|---|---|---|
| number | Text | "01", "02"... |
| headline | Text | Titulo do topico |
| body | Text | Conteudo |
| has_icon | Boolean | Mostra icone ao lado do numero |
| theme | Variant | light / dark |

### Como criar uma property:

1. Selecione o master component
2. No painel direito, clique em "+" ao lado de "Component properties"
3. Escolha o tipo (Text, Boolean, Variant, Instance swap)
4. Nomeie com prefixo de categoria: `content/headline`, `style/theme`

---

## 5. Plugins essenciais para producao de social media

### Producao de conteudo

**Content Reel**
- Preenche textos e imagens com dados reais automaticamente
- Ideal para testar templates com conteudo variado antes de finalizar
- Instale de: Figma Community > Content Reel

**Batch Styler**
- Altera multiplos estilos de cor/texto de uma vez
- Uso: quando precisar atualizar a tipografia em todos os slides de um batch
- Economiza 30+ minutos em cada atualizacao de sistema

**Google Sheets Sync**
- Conecta uma planilha ao Figma
- Cada linha da planilha = um post
- Colunas: headline, corpo, numero_slide, tema, data
- Clica "Sync" e o plugin popula todos os frames com os dados

**Bulk Variables Generator**
- Importa variaveis de JSON externo
- Util quando o sistema de tokens evoluir — importa tudo de uma vez

### Organizacao e exportacao

**Similayer**
- Seleciona todas as layers com a mesma propriedade (ex: todos os textos "headline")
- Uso: encontrar e substituir elementos identicos no batch inteiro

**Export Assets / Batch Export**
- Exporta multiplos frames selecionados simultaneamente
- Configuracao: PNG 1x (se frame em pixel exato), com prefixo de nome automatico
- Sempre exportar: PNG para publicacao, PDF para arquivo

**Exacto - Social Media Frameworks**
- Configura frames nos tamanhos corretos do Instagram automaticamente
- 1080x1080, 1080x1350, 1080x1920 com um clique

### Icones e recursos

**Iconify**
- Biblioteca com 200.000+ icones vetoriais gratuitos
- Use apenas icones da familia "Lucide" ou "Phosphor" para consistencia editorial
- Sempre importar como componente (nao como imagem achatada)

---

## 6. Montando templates reaproveitaveis — passo a passo

### Estrutura de arquivo Figma recomendada para Triforce Auto

```
Arquivo: [TriforceAuto] Design System Instagram
  Page 1: Tokens & Variables
    - Paleta de cores
    - Escala tipografica
    - Espacamento
  Page 2: Components Library
    - Cover (variants: dark_photo, gradient, abstract)
    - Slide Interno (variants: light, dark)
    - Slide CTA
    - Reels Cover
    - Logo/Branding atoms
  Page 3: Templates
    - Template: Carrossel 6 slides
    - Template: Card unico 1:1
    - Template: Card unico 4:5
    - Template: Reels Cover 9:16
  Page 4: Producao [Semana XX]
    - Batch da semana em grid
```

### Como montar o componente Cover do zero:

1. Crie frame 1080x1080, fundo com variable `brand/dark`
2. Adicione layer de imagem (placeholder) — marque como "Linked" via Instance Swap property
3. Adicione overlay gradient: preto 0% → 70% de baixo para cima (opacidade 80%)
4. Container texto em Auto Layout vertical, ancorado bottom-left:
   - Label pequeno: "#IA | Triforce Auto", 12px, laranja `brand/primary`
   - Headline: 48-64px, Bold, branco `brand/white`
   - Espaco superior: auto (empurra para baixo)
5. Logo no canto inferior direito, fora do container de texto
6. Converta tudo em Component (Ctrl+Alt+K)
7. Adicione properties: headline (Text), image (Instance Swap), has_label (Boolean)

### Como produzir 5 covers em 15 minutos:

1. Arraste 5 instancias do componente Cover na pagina de Producao
2. Em cada instancia, altere apenas: headline + image
3. Selecione todos os 5 frames > Export > PNG
4. Nome automatico ja vem do frame name — configure antes: `cover_[slug-tema]_v1`

---

## 7. Nomenclatura de layers e frames (obrigatoria)

Layers nomeados corretamente = exportacao correta = sem retrabalho.

### Convencao:

```
Frames (posts finais):
  cover_ferramentas-ia-marketing_v1
  carousel_5-prompts-chatgpt_v1 / slide-01
  carousel_5-prompts-chatgpt_v1 / slide-02
  reels-cover_automacao-ia_v1

Components:
  .cover/dark_photo
  .cover/gradient
  .slide-interno/light
  .slide-cta/default

Atoms:
  logo/horizontal/dark
  logo/symbol/light
  badge/tag-ia
```

O ponto antes do nome (`.cover`) e convencao Figma para components que ficam no topo da lista e nao sao confundidos com frames de producao.

---

## 8. Exportacao em lote — fluxo final

1. Abra a pagina de Producao da semana
2. Selecione todos os frames do batch (Ctrl+A ou selecione manualmente)
3. No painel direito, desca ate "Export"
4. Configuracao: `PNG`, `1x`, ativar "Include in export"
5. Clique "Export [N] layers"
6. Figma gera um ZIP com todos os arquivos nomeados pelo nome do frame
7. Confira o ZIP antes de entregar — nenhum arquivo deve ter "Frame" no nome (indica que a nomenclatura nao foi feita)

---

## Checklist de qualidade antes de entregar o batch

- [ ] Todos os frames nomeados com a convencao (`formato_slug_v1`)
- [ ] Todos os textos usando estilos de tipografia (nao fonte avulsa)
- [ ] Todas as cores usando variables (nao hex solto)
- [ ] Cover passa no teste dos 0,5 segundos (mostra para alguem sem contexto)
- [ ] Slides internos com no maximo 3 elementos por slide
- [ ] Exportacao PNG gerada e conferida
- [ ] Sugestao de legenda escrita para cada post

---

**Proximos passos apos dominar este material:**
- Conectar Google Sheets Sync ao calendario editorial
- Explorar Figma Variables com modos (dark/light) para variantes sazonais
- Criar biblioteca de componentes compartilhada entre arquivos
