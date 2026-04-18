# IA para Geracao de Imagem — Covers Editoriais

> Material de treinamento — Vitoria, Designer Instagram Triforce Auto
> Canal: curadoria de IA | Paleta: #FF6B00 / #0A0A0A / #F5F0EB | Referencia: @hollyfield.ia

---

## Logica de uso no canal

Imagens de IA no canal de curadoria de IA nao sao decoracao — sao o argumento visual do post.

O cover precisa criar tensao em 0,5 segundo. A foto de banco nao cria — e generico demais. A imagem de IA certa cria porque e unica, alinhada ao tema, e visualmente improvavel.

Regras antes de gerar qualquer imagem:
1. Saiba qual e a headline do post
2. Saiba qual e a tensao visual que o cover precisa criar
3. Escreva o prompt com base na tensao — nao na descricao literal do tema

---

## 1. Midjourney V7 — fundamentos

### O que mudou no V7 (lancado abril 2025):

- Prompt accuracy muito superior — textos longos com multiplas instrucoes funcionam melhor
- Texturas mais ricas e coerencia de cena melhorada (maos, objetos complexos)
- Novos parametros: `--p` (personagem consistente em cenas diferentes), `--oref` (Omni Reference)
- Resolucao e sharpness por padrao mais altos

### Parametros essenciais para o canal editorial:

| Parametro | Funcao | Valor recomendado |
|---|---|---|
| `--ar` | Aspect ratio | `--ar 1:1` (feed) / `--ar 4:5` (portrait) / `--ar 9:16` (reels cover) |
| `--s` | Stylize — quanto o MJ interpreta artisticamente | `--s 200` a `--s 400` para editorial |
| `--q` | Quality — quanto tempo gasta renderizando | `--q 2` para finalizacao |
| `--v 7` | Usa o modelo V7 | Sempre explicito |
| `--no` | Elementos a excluir | `--no text, watermark, logo, signature` |
| `--sref [URL]` | Style Reference — aplica o estilo visual de uma imagem de referencia | Ver secao 3 |
| `--sw` | Style Weight — quao forte o `--sref` influencia | `--sw 500` a `--sw 800` |
| `--seed` | Semente para reproducao exata | Anote o seed de imagens que aprovadas |

---

## 2. Anatomia do prompt para covers editoriais dark

### Formula basica:

```
[SUJEITO] + [CONTEXTO/CENA] + [ESTILO VISUAL] + [ILUMINACAO] + [PALETA] + [MOOD] + [PARAMETROS]
```

### Vocabulario que funciona para o estilo Triforce Auto:

**Sujeito (o que aparece):**
- `abstract neural network visualization`
- `glowing circuit board macro`
- `robotic hand reaching toward light`
- `data streams dissolving into particles`
- `dark server room with orange ambient light`
- `AI brain made of light filaments`
- `person in silhouette against digital horizon`

**Estilo visual:**
- `editorial magazine photography`
- `cinematic still`
- `high-end tech editorial`
- `dark minimalist composition`
- `deconstructed digital art`

**Iluminacao:**
- `single source dramatic backlight`
- `orange rim light from the right`
- `neon glow reflecting off dark surface`
- `chiaroscuro, deep shadows`
- `low-key studio lighting`

**Paleta:**
- `deep black background #0A0A0A`
- `warm orange accents #FF6B00`
- `monochromatic dark palette with single warm highlight`
- `noir with amber highlights`

**Mood:**
- `mysterious, intelligent, minimal`
- `tension between human and machine`
- `quiet power, technological depth`

---

## 3. Style Reference (--sref) — consistencia visual entre posts

O `--sref` e o parametro que garante que todos os covers do canal tenham o mesmo DNA visual — mesmo gerados em dias diferentes.

### Como usar `--sref`:

1. Gere uma imagem que seja o cover perfeito do canal (ou use um cover aprovado existente)
2. Copie a URL da imagem (no Discord do MJ: clique na imagem, botao direito, "Copiar link de imagem")
3. Em todos os prompts subsequentes, adicione: `--sref [URL_DO_COVER_APROVADO]`
4. Ajuste a forca com `--sw 600` (600 e equilibrio entre manter o estilo e aceitar o novo sujeito)

### Criando um "moodboard de referencia" para o canal:

Voce pode usar multiplas URLs de referencia:
```
--sref URL1 URL2 URL3
```
Midjourney vai interpolar o estilo das tres imagens. Ideal para quando o canal tiver 5-10 covers aprovados — use todos como referencia.

### Guardando e organizando referencias:

Crie uma pasta no Google Drive: `TriforceAuto / IA Referencias / Covers Aprovados`
Para cada cover aprovado: salve a imagem + anote o seed + anote os parametros usados.

---

## 4. Prompts prontos para o canal Triforce Auto

### Prompt 01 — Cover para post sobre "Ferramentas de IA":

```
editorial magazine cover, abstract visualization of AI tools as floating geometric objects,
warm orange light sources, deep black background, minimal composition,
professional tech magazine aesthetic, dramatic shadows, single point perspective,
high contrast, cinematic quality --ar 4:5 --s 300 --q 2 --v 7 --no text logo watermark
```

### Prompt 02 — Cover para post sobre "ChatGPT / LLMs":

```
glowing neural network nodes dissolving into light particles, orange and amber light,
pitch black void background, macro photography style, mathematical precision,
hyper-detailed, editorial dark aesthetic, chiaroscuro lighting --ar 1:1 --s 350 --q 2 --v 7 --no text
```

### Prompt 03 — Cover para post sobre "Automacao / Produtividade":

```
robotic hand and human hand reaching toward each other, near-touching, dramatic orange backlight,
smoke and light particles, deep dark background, cinematic still, Michelangelo inspired composition,
tech editorial magazine --ar 4:5 --s 400 --q 2 --v 7 --no text watermark
```

### Prompt 04 — Cover para post sobre "Dados e Analytics":

```
abstract data visualization, thousands of glowing data points forming a face profile,
warm orange and white glow against void black, motion blur on edges,
editorial tech photography, minimal negative space --ar 1:1 --s 300 --q 2 --v 7 --no text
```

### Prompt 05 — Cover para post de "Top 5 / Lista":

```
five abstract geometric objects floating in dark space, single orange light source below,
editorial still life, luxury tech magazine aesthetic, ultra-sharp focus, subtle depth of field,
dark minimalist composition --ar 4:5 --s 250 --q 2 --v 7 --no text logo
```

### Prompt 06 — Reels Cover (9:16):

```
vertical editorial composition, AI brain network made of light filaments,
full height dark frame, orange glow from center, dramatic vignette edges,
magazine cover vertical format, cinematic, intelligent, mysterious --ar 9:16 --s 350 --q 2 --v 7 --no text
```

---

## 5. Leonardo AI — quando usar como alternativa

### Vantagens do Leonardo AI sobre Midjourney para este canal:

- Interface web (sem Discord — mais acessivel)
- Modelos especializados: Phoenix, Kino XL (cinematico), Flux Dev
- Canvas de edicao inpainting e outpainting diretamente no browser
- Controle de paleta de cores mais direto
- Plano gratuito com creditos diarios

### Configuracao recomendada no Leonardo:

- Modelo: **Phoenix** (melhor para editorial realista)
- Guidance Scale: 7-9 (equilibrio entre fidelidade ao prompt e criatividade)
- Image Dimensions: 1024x1024 (square) ou 832x1216 (portrait 4:5)
- Number of images: 4 (gera 4 opcoes por vez para selecionar o melhor)

### Prompt equivalente no Leonardo (nao usa `--ar`, usa o campo de dimensoes):

```
editorial magazine photography, abstract AI neural network visualization,
dramatic orange rim lighting, deep black background, cinematic still,
high contrast, tech editorial dark aesthetic, professional photography quality,
negative prompt: text, watermark, logo, people, face, hands
```

### Quando escolher Leonardo vs Midjourney:

| Situacao | Ferramenta |
|---|---|
| Volume alto de geracao (5+ imagens por sessao) | Midjourney (mais rapido) |
| Precisao de paleta de cor especifica | Leonardo (controle de cor melhor) |
| Edicao inpainting (alterar parte da imagem) | Leonardo (canvas embutido) |
| Consistencia de estilo entre posts (sref) | Midjourney |
| Sem acesso ao Discord | Leonardo |

---

## 6. Workflow de geracao para batch semanal

### Sessao de geracao semanal (estimativa: 30-45 min para 7 covers):

**Etapa 1 — Pre-producao (5 min):**
- Leia os titulos dos 7 posts da semana (do calendario editorial)
- Identifique o tema visual de cada um (conceito abstrato, ferramenta, pessoa, dado)
- Escreva os prompts em um doc de texto (mais rapido que digitar no Discord)

**Etapa 2 — Geracao no Midjourney (15 min):**
- Submeta todos os prompts em sequencia
- Para cada resultado: selecione U1-U4 (upscale da melhor opcao) ou V1-V4 (variacao)
- Anote o seed das que aprovarem (botao "..." > "Copy Job ID" no Discord)

**Etapa 3 — Download e triagem (5 min):**
- Baixe todas as imagens aprovadas
- Nomeie imediatamente: `raw_cover_[slug-do-post]_v1.png`
- Mova para pasta `raw/semana-XX/covers-ia/`

**Etapa 4 — Tratamento no Photoshop (10 min):**
- Aplique a Action `editorial_dark_batch` (color grade padrao)
- Adicione noise overlay se necessario
- Exporte PNG final em 1080x1080 ou 1080x1350

**Etapa 5 — Composicao no Figma (5-10 min):**
- Coloque a imagem tratada no componente Cover
- Adicione headline
- Confira: laranja, preto, branco na proporcao certa
- Exporte o frame final

---

## 7. Parametros avancados para controle de output

### Controlando o que NAO deve aparecer (`--no`):

Sempre use em posts do canal editorial:
```
--no text, watermark, logo, signature, people smiling, cartoon, illustration style,
colorful background, neon rainbow, lens flare excessive
```

### Seed para reproducao exata:

Quando uma imagem sai perfeita mas voce quer uma variacao minima:
1. Clique em "..." na imagem no Discord
2. "Copy Job ID" — e o seed
3. No proximo prompt: `--seed [numero]`
4. Resultado: imagem muito similar com as alteracoes do prompt

### Chaos (`--chaos`) para explorar variacao:

Quando voce quer opcoes radicalmente diferentes:
```
--chaos 30
```
Gera 4 imagens muito distintas entre si. Util no inicio de um novo tema visual para explorar direcoes.

### Tile para texturas de fundo (`--tile`):

Para criar texturas que se repetem sem emendas (util como fundo de slide interno):
```
abstract circuit board pattern, minimal, monochrome, dark --tile --ar 1:1 --s 200
```

---

## 8. Biblioteca de prompts — organizacao

Mantenha um arquivo `prompts-biblioteca.md` com:

```markdown
## Template Cover — Ferramentas IA
Data: YYYY-MM-DD
Prompt: [prompt completo]
Seed: [numero]
Resultado: [nome do arquivo gerado]
Aprovado: sim/nao
Observacoes: [o que funcionou / o que nao funcionou]
```

Isso cria um historico que acelera a producao — prompts aprovados sao reutilizados com pequenas adaptacoes, nao reescritos do zero.

---

## Checklist IA antes de entregar o cover

- [ ] Imagem gerada com parametros corretos (ar, s, q, v7)
- [ ] `--no text` aplicado (nenhum texto aleatorio na imagem)
- [ ] Paleta coerente com o canal (escuro, laranja, sem cores saturadas estranhas)
- [ ] Seed anotado no arquivo de biblioteca de prompts
- [ ] Imagem tratada no Photoshop (color grade editorial)
- [ ] PNG final em resolucao correta (1080x1080 ou 1080x1350)
- [ ] Cover passa no teste 0,5 segundo (mostra para alguem sem contexto — ele para o scroll?)
