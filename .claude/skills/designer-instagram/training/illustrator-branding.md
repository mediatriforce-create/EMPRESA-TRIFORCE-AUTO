# Illustrator para Branding Social Media

> Material de treinamento — Vitoria, Designer Instagram Triforce Auto
> Canal: curadoria de IA | Paleta: #FF6B00 / #0A0A0A / #F5F0EB | Referencia: @hollyfield.ia

---

## Quando usar Illustrator (e nao Figma ou Photoshop)

Illustrator e a ferramenta certa quando o trabalho e **vetorial e precisa escalar**:
- Criacao e ajuste do logo Triforce Auto (qualquer tamanho sem perda)
- Icones originais do sistema visual do canal
- Elementos graficos reutilizaveis: divisores, badges, molduras minimalistas
- Tipografia custom (lettering, variacao de fonte para titulos especiais)
- Ilustracoes de fundo para covers (grafismos geometricos, linhas tech)

Regra pratica: se o elemento vai aparecer em tamanhos diferentes (post, story, capa, thumbnail), ele tem que ser vetor — Illustrator.

---

## 1. Configuracao de documento para social media

### Setup correto:

1. `File > New`
2. Profile: Web (nao Print — garante RGB e pixel-based)
3. Unidade: Pixels
4. Tamanho: 1080x1080 (ou o formato desejado)
5. Color mode: RGB
6. Raster Effects: High (300 ppi) — para exportacao de alta qualidade

**Atencao:** Illustrator opera em vetores mas exporta para raster. O "300 ppi" no documento afeta apenas os efeitos raster (sombras, blurs) — o vetor em si e sempre escalavel.

---

## 2. Sistema de cores globais — a fundacao do branding

### Por que usar cores globais (nao cores normais):

Cor global = alterou uma vez, atualiza em todos os lugares onde ela foi usada no documento. Identico a variables no Figma.

### Como criar a paleta global da Triforce Auto:

1. Abra o painel `Window > Swatches`
2. Para cada cor da paleta:
   - Crie um retangulo com a cor desejada
   - Selecione o retangulo e arraste para o painel Swatches
   - Duplo clique no swatch criado
   - **ATIVE "Global"** (checkbox obrigatorio)
   - Nomeie: `triforce/primary`, `triforce/dark`, `triforce/light`
3. Salve o arquivo como biblioteca: `Window > Libraries` > salvar swatches como biblioteca CC

### Paleta Triforce Auto em Illustrator:

| Nome | Hex | Uso |
|---|---|---|
| `triforce/primary` | #FF6B00 | Laranja — CTA, destaque, dado em evidencia |
| `triforce/dark` | #0A0A0A | Preto editorial — fundo de cover |
| `triforce/light` | #F5F0EB | Bege — fundo de slide interno |
| `triforce/white` | #FFFFFF | Branco — texto sobre fundo escuro |
| `triforce/dark-60` | #0A0A0A 60% opacidade | Overlay suave |

---

## 3. Criando icones para o sistema visual do canal

### Principios para icones do canal de curadoria de IA:

- **Stroke icons** (apenas linha, sem preenchimento) — mais limpos, estilo tech
- Peso de linha: 1.5px ou 2px consistente em todos os icones
- Corner radius nos cantos: 2px (suaviza sem ficar arredondado demais)
- Tamanho de producao: 64x64px (escala para qualquer uso)
- Estilo: geometrico, minimalista — sem ornamentos decorativos

### Tecnica para criar icone de "chip / IA":

1. Retangulo central: 32x32px, stroke 2px, fill nenhum, corner radius 4px
2. Linhas saindo dos lados: 8 linhas de 8px, espacadas regularmente
3. Use `Object > Path > Offset Path` para criar variante preenchida se necessario
4. Group tudo, renomeie: `icon/chip`
5. Converta em Symbol (ver secao 5)

### Biblioteca de icones recomendada para o canal:

Icones a criar/adaptar no sistema Triforce Auto:

| Icone | Descricao |
|---|---|
| `icon/chip` | Chip de processador — IA/tech |
| `icon/network` | Nos conectados — redes neurais |
| `icon/spark` | Raio/spark — novidade, destaque |
| `icon/eye` | Olho — "curadoria, observacao" |
| `icon/arrow-right` | Seta — CTA, "saiba mais" |
| `icon/bookmark` | Marcador — "salve este post" |
| `icon/clock` | Relogio — "tendencia da semana" |

---

## 4. Estilos graficos para consistencia editorial

### Graphic Styles — guardar aparencias complexas:

Graphic Styles salvam combinacoes de: fill + stroke + efeitos + opacidade. Um clique aplica tudo junto.

### Estilos a criar para o sistema Triforce Auto:

**Style: `badge-ia`**
- Fill: #FF6B00
- Stroke: nenhum
- Corner radius: 4px
- Opacity: 100%
- Typography: 10px, Bold, #FFFFFF, uppercase, tracking 0.1em

**Style: `headline-dark`**
- Fill: #FFFFFF
- Stroke: nenhum
- Typography: Bold, uppercase, linha ajustada

**Style: `divider-line`**
- Fill: nenhum
- Stroke: 1px, #FF6B00, opacidade 60%

### Como criar um Graphic Style:

1. Crie o elemento com as propriedades desejadas
2. Selecione o elemento
3. `Window > Graphic Styles`
4. Arraste o elemento para o painel — estilo salvo
5. Nomear: duplo clique no estilo

---

## 5. Symbols — reutilizacao de elementos em escala

Symbols em Illustrator funcionam como Componentes no Figma: uma instancia do symbol e atualizada automaticamente quando voce edita o master.

### Como transformar o logo em Symbol:

1. Abra o arquivo do logo da Triforce Auto
2. Selecione todos os elementos do logo
3. `Object > Symbols > New Symbol` (ou arraste para `Window > Symbols`)
4. Nomeie: `logo/horizontal` ou `logo/symbol`
5. Ative "Dynamic Symbol" (permite alterar cor por instancia sem deslinkar)
6. Confirme

### Usando Dynamic Symbols para variantes de cor:

Com Dynamic Symbols ativado:
- Instancia 1: logo branco (sobre fundo escuro)
- Instancia 2: logo laranja (para contextos neutros)
- Ambas apontam para o mesmo master — formato nunca se distorce

Para alterar a cor de uma instancia sem afetar as outras:
1. Selecione a instancia
2. `Object > Symbols > Edit Symbol`
3. Use o Direct Selection Tool para selecionar o elemento interno
4. Altere a cor — apenas aquela instancia e afetada

---

## 6. Elementos graficos para o estilo editorial tech

### Grafismos de fundo para covers (estilo @hollyfield.ia):

**Grade de pontos (dot grid):**
1. Crie um circulo 2x2px, fill laranja #FF6B00, opacidade 30%
2. `Object > Transform > Move` → Horizontal: 24px, clique "Copy"
3. `Ctrl+D` para repetir 12x (cria linha de 12 pontos)
4. Selecione a linha, `Move` → Vertical: 24px, "Copy"
5. Repita ate criar grade 12x12
6. Group tudo, reduza opacidade para 15-20%
7. Use como textura de fundo em covers

**Linhas diagonais tech:**
1. Linha de 400px com stroke 1px, cor `triforce/primary`, opacidade 20%
2. Duplique com espacamento de 16px
3. Rotacione 45 graus o grupo
4. Use como elemento de profundidade no cover

**Formas geometricas de acento:**
- Circulo com stroke 1px, fill nenhum, cor laranja — posicione atras da headline
- Retangulo preenchido em laranja, altura 4px — como underline de titulo especial
- Triangulo pequeno (8px) em laranja — como marcador de item em listas

---

## 7. Character Styles e Paragraph Styles

### Por que configurar estilos tipograficos no Illustrator:

Quando voce cria varios posts no mesmo arquivo .ai, estilos garantem que todos os textos sigam o mesmo padrao — sem precisar verificar fonte, tamanho e espacamento manualmente.

### Character Styles para o sistema Triforce Auto:

| Style | Font | Size | Weight | Color | Tracking |
|---|---|---|---|---|---|
| `headline-cover` | Inter ou Sora | 64px | Black (900) | #FFFFFF | -0.02em |
| `headline-slide` | Inter ou Sora | 36px | Bold (700) | #0A0A0A | -0.01em |
| `body-slide` | Inter | 16px | Regular (400) | #0A0A0A | 0 |
| `label-badge` | Inter | 10px | Bold (700) | #FFFFFF | 0.1em (uppercase) |
| `cta-text` | Inter | 14px | SemiBold (600) | #FF6B00 | 0.05em |

### Como criar Character Style:

1. Formate o texto com as propriedades desejadas
2. `Window > Type > Character Styles`
3. Clique em "New Character Style"
4. Nomeie conforme a tabela
5. Para aplicar: selecione qualquer texto e clique no style

---

## 8. Fluxo de exportacao vetorial para Instagram

### Exportando PNG de alta qualidade do Illustrator:

1. `File > Export > Export As`
2. Formato: PNG
3. Desmarque "Use Artboards" se quiser exportar selecao especifica
4. Resolution: High (300 ppi) — mesmo para web, garante qualidade maxima
5. Anti-aliasing: Art Optimized

### Exportando SVG (para uso em Figma):

1. Selecione o elemento (icone, grafismo)
2. `File > Export Selection`
3. Formato: SVG
4. SVG Options: Responsive, Decimal: 2, CSS Properties: Style Attributes
5. Importe no Figma: `File > Place Image` ou arraste o .svg direto no canvas

### Exportando para uso como Smart Object no Photoshop:

1. `File > Export > Export As` > PNG em alta resolucao
2. Ou: salve como PDF e coloque como Smart Object no Photoshop (mantem vetorial)

---

## 9. Fluxo pratico — criando um icone e integrando ao sistema

### Do Illustrator ao post final (20 minutos):

1. **Illustrator (8 min):** Crie o icone em 64x64px, salve como Symbol, exporte SVG
2. **Figma (5 min):** Importe o SVG, converta em componente, aplique color variable
3. **Post (7 min):** Instancie o componente no template de slide interno, ajuste posicao

### Convencao de arquivos Illustrator:

```
assets/
  icons/
    icon_chip.ai
    icon_network.ai
    icon_spark.ai
  graphics/
    bg_dot-grid.ai
    bg_diagonal-lines.ai
    divider_line.ai
  branding/
    logo_horizontal.ai
    logo_symbol.ai
    logo_dark-version.ai
```

---

## Checklist Illustrator antes de entregar

- [ ] Todas as cores usando swatches globais (nao hex solto)
- [ ] Elementos reutilizaveis convertidos em Symbols
- [ ] Nenhum stroke sem expandir em exportacoes finais (a nao ser que seja intencional)
- [ ] Character Styles aplicados em todos os textos
- [ ] Arquivo .ai salvo com layers nomeados
- [ ] SVGs exportados testados no Figma (sem erros de importacao)
- [ ] Nomenclatura: `icon_[nome].ai`, `logo_[variante].ai`
