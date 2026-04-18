# Photoshop para Social Media Editorial

> Material de treinamento — Vitoria, Designer Instagram Triforce Auto
> Canal: curadoria de IA | Paleta: #FF6B00 / #0A0A0A / #F5F0EB | Referencia: @hollyfield.ia

---

## Quando usar Photoshop (e nao Figma)

Photoshop entra no fluxo quando o post exige:
- Tratamento fotografico real (correcao de cor, retoques, compositing)
- Remocao de fundo com precisao em cabelo, objetos complexos
- Composicao de multiplas imagens em uma cena coesa
- Geracao de textura/noise organico para covers dark
- Batch de imagens de banco (ex: 10 fotos com o mesmo tratamento editorial)

Para layout, tipografia e sistema — use Figma. Para imagem bruta — use Photoshop.

---

## 1. Configuracao de documento para Instagram

### Tamanhos corretos (sempre 72 dpi nao importa, salve em 300 para arquivo):

| Formato | Pixels | Uso |
|---|---|---|
| Feed quadrado | 1080 x 1080 | Card unico, carrossel |
| Feed portrait | 1080 x 1350 | Card 4:5, maior visibilidade |
| Story / Reels Cover | 1080 x 1920 | Thumbnail de reel |
| Cover editorial horizontal | 1080 x 608 | Nao recomendado para feed |

**Configuracao de novo documento:**
- Pixels como unidade (sempre)
- Color mode: RGB 8-bit
- Background: preto (#0A0A0A) para covers dark

---

## 2. Smart Objects — a base dos templates em escala

Smart Objects sao o equivalente Photoshop dos componentes Figma. Editou o master, atualizou todas as instancias.

### Como criar um template com Smart Objects:

1. Abra o arquivo do template (ex: `template_cover_dark.psd`)
2. O placeholder de imagem e um Smart Object — identifique pelo icone de Smart Object na camada
3. Duplo clique na camada Smart Object — abre em aba separada (`placeholder.psb`)
4. Cole a nova imagem dentro, ajuste o enquadramento, salve (Ctrl+S)
5. Feche a aba — o template principal atualiza automaticamente com a nova imagem
6. Exporte via `File > Export > Export As` em PNG

### Estrutura de template cover editorial:

```
cover_template_dark.psd
  |-- [Grupo] BRANDING
  |     |-- logo (Smart Object linked)
  |     |-- badge-ia (texto + shape)
  |-- [Grupo] TEXTO
  |     |-- headline (texto editavel)
  |     |-- subline (texto editavel, opcional)
  |-- [Grupo] OVERLAY
  |     |-- gradiente preto 0-80% (modo Multiply)
  |     |-- noise texture (modo Overlay, 8% opacidade)
  |-- [Smart Object] IMAGEM_PRINCIPAL
  |-- [Layer] FUNDO_SOLIDO (#0A0A0A)
```

### Template de slide interno:

```
slide_interno_template.psd
  |-- [Grupo] CONTEUDO
  |     |-- numerador (texto — altere apenas o numero)
  |     |-- headline (texto editavel)
  |     |-- corpo (texto editavel)
  |-- [Grupo] BRANDING
  |     |-- logo (Smart Object linked)
  |-- [Layer] FUNDO (#F5F0EB ou #FFFFFF)
```

---

## 3. Remocao de fundo com IA (Firefly + Select Subject)

### Metodo rapido (Firefly AI — Photoshop 2025):

1. Abra a imagem
2. Va em `Select > Subject` — Photoshop seleciona o sujeito automaticamente com IA
3. Se precisar refinar: ative `Select and Mask` (no topo quando a selecao esta ativa)
4. Em Select and Mask: use "Refine Edge Brush" nas areas de cabelo/pelos
5. Output: `New Layer with Mask`
6. Resultado: camada com mascara limpa, fundo transparente

### Para remocao com um clique (objetos simples):

1. Selecione a camada da imagem
2. Va em `Image > Remove Background`
3. Photoshop 2025 usa Firefly para remover automaticamente
4. Confira as bordas — pode precisar de refinamento manual em bordas complexas

### Para batch de multiplas imagens com remoção de fundo:

Use o metodo de Actions (ver secao 5) — grave a acao de remoção de fundo e aplique a pasta inteira.

---

## 4. Compositing editorial dark — tecnica para covers

O estilo editorial dark do canal (@hollyfield.ia) e construido em camadas:

### Stack de camadas para cover editorial:

**Camada 1 — Base:**
Imagem principal (foto ou render de IA), ajustada com Smart Object

**Camada 2 — Color Grade:**
Camada de ajuste `Hue/Saturation`: saturacao -30 a -50 (dessatura parcialmente)
Camada de ajuste `Curves`: escurece midtones, eleva levemente os brancos

**Camada 3 — Overlay textural:**
Imagem de noise/granulacao em modo `Overlay`, opacidade 10-15%
Deixa o fundo menos plastificado, mais editorial/analogico

**Camada 4 — Gradiente de integracao:**
Gradiente preto → transparente, de baixo para cima
Modo `Normal`, opacidade 70-85%
Funcao: criar area escura para o texto respirar sem conflitar com a imagem

**Camada 5 — Color toning:**
Camada de ajuste `Color Balance` ou `Gradient Map`
Para o canal: toning levemente laranja-avermelhado nos midtones
Hex de referencia para midtone warm: #1A0A00 (quase preto, com calor)

**Camada 6 — Texto (headline):**
Sempre em branco #FFFFFF ou laranja #FF6B00
Bold, uppercase ou sentence case — nao use lowercase no cover
Sombra de texto: preto, opacidade 40%, blur 8px, distancia 0 (sombra difusa, nao direcional)

### Resultado esperado:
Cover com profundidade visual, sem parecer foto generica de banco. A imagem existe para criar tensao visual — nao para ilustrar literalmente o tema.

---

## 5. Actions — automacao de batch

Actions gravam sequencias de passos e as executam automaticamente em quantos arquivos voce quiser.

### Criando uma Action de tratamento editorial:

1. `Window > Actions` para abrir o painel
2. Clique em "New Action", nomeie: `editorial_dark_batch`
3. Clique em Record (circulo vermelho) — TUDO que voce fizer agora sera gravado
4. Execute os passos do tratamento (color grade, noise overlay, etc.)
5. Clique Stop (quadrado) para parar a gravacao

### Executando a Action em batch:

1. `File > Automate > Batch`
2. Set: escolha o conjunto onde sua action esta
3. Action: `editorial_dark_batch`
4. Source: Folder → selecione a pasta com as imagens brutas
5. Destination: Folder → selecione pasta de saida
6. File Naming: configure o padrao de nomenclatura (ex: `cover_[nome-original]_v1`)
7. OK — Photoshop processa todos os arquivos automaticamente

### Actions recomendadas para criar no sistema Triforce Auto:

| Action | Funcao |
|---|---|
| `editorial_dark_batch` | Color grade completo para covers dark |
| `remove_bg_batch` | Remocao de fundo em lote |
| `resize_feed_square` | Redimensiona para 1080x1080 com crop inteligente |
| `resize_feed_portrait` | Redimensiona para 1080x1350 |
| `export_png_web` | Exporta PNG otimizado para web (salva em pasta de saida) |
| `noise_overlay_apply` | Adiciona camada de noise editorial padronizada |

---

## 6. Exportacao em lote (Firefly Creative Production)

O Photoshop 2025 tem o Firefly Creative Production — solucao de batch editing sem codigo que processa centenas de imagens:

1. `File > Automate > Firefly Creative Production` (disponivel no CC 2025+)
2. Upload de imagens brutas
3. Configure: remocao de fundo + color grading + crop + nomenclatura
4. Execute — processa em nuvem e devolve os arquivos prontos

Para volumes menores (5-30 posts/semana), o metodo de Actions acima e mais rapido e controlavel.

---

## 7. Fluxo pratico de producao semanal no Photoshop

### Sessao semanal de tratamento de imagem (estimativa: 45-60 min para 7 posts):

**Etapa 1 — Preparacao (10 min):**
- Separe as imagens brutas na pasta `raw/semana-XX/`
- Identifique quais precisam de remoção de fundo e quais sao fundos completos
- Crie pasta de saida: `treated/semana-XX/`

**Etapa 2 — Batch de remoção de fundo (5 min):**
- Execute Action `remove_bg_batch` na subpasta de imagens que precisam de corte
- Confira resultados, corrija manualmente os 1-2 que errarem nas bordas

**Etapa 3 — Batch de color grade (10 min):**
- Execute Action `editorial_dark_batch` em todas as imagens
- Revise rapidamente — 1 minuto por imagem para ajuste fino se necessario

**Etapa 4 — Compositing no template (20 min):**
- Abra `cover_template_dark.psd`
- Troque o Smart Object de imagem para cada post (duplo clique, cole nova imagem)
- Atualize o texto da headline
- Export As PNG para pasta de saida

**Etapa 5 — Exportacao e nomenclatura (5 min):**
- Confirme nomes dos arquivos seguindo a convencao: `cover_[slug]_v1.png`
- Mova para pasta compartilhada ou entregue via link

---

## 8. Paleta de ajustes para o estilo editorial Triforce Auto

### Curves — perfil editorial dark:

```
Canal RGB:
  Ponto de entrada (shadows): Input 0, Output 10 (eleva levemente o preto — evita preto absoluto)
  Ponto medio (midtones): Input 128, Output 110 (escurece o meio)
  Ponto de saida (highlights): Input 255, Output 245 (suaviza o branco)

Canal Red:
  Midtones: Input 128, Output 135 (adiciona warm no meio)

Canal Blue:
  Midtones: Input 128, Output 120 (retira frio do meio — mais quente/editorial)
```

Esses valores criam o color grade characteristic de canais de curadoria tech — escuro, quente, com profundidade.

### Hue/Saturation para integracao de imagens de banco:

Quando a imagem vem de banco e parece "colorida demais" para o estilo dark:
- Saturation: -35 a -45
- Lightness: -10 a -15
- Resultado: imagem se integra ao fundo escuro sem conflitar

---

## Checklist Photoshop antes de entregar

- [ ] Smart Objects nao rasterizados (mantem editabilidade)
- [ ] Arquivo .psd salvo com layers organizados e nomeados
- [ ] PNG exportado em 1080x1080 ou 1080x1350 sem artifacts de compressao
- [ ] Texto embutido ou convertido em forma (sem font missing no arquivo)
- [ ] Nomenclatura: `cover_[slug]_v1.png`
- [ ] Nenhuma camada com nome "Layer 1", "Layer 2" (nomenclatura descritiva obrigatoria)
