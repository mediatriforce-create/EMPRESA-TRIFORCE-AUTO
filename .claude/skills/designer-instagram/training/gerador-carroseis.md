---
titulo: Gerador de Carrosséis Python — Manual Completo de Produção
autor: Vitória (Designer Instagram)
fonte: produção real batch Abril 2026 — erros cometidos, corrigidos, entendidos
versao: 1.0
---

# Gerador de Carrosséis — Manual Completo

> Este documento não é teoria. É tudo que foi descoberto, quebrado, consertado e aprendido
> durante a produção real do batch de Abril 2026 — 5 carrosséis, 29 slides.
> Cada regra aqui tem uma história de erro atrás dela.

---

## O que é e como funciona

```
Python → Playwright (Chromium headless) → HTML/CSS renderizado → PNG 1080×1350px
```

O Chromium abre cada slide como uma página HTML, renderiza com fontes reais (Inter via Google Fonts) e tira um screenshot. O resultado é indistinguível de um export do Figma — mas gerado em segundos para todos os 29 slides de uma vez.

**Localização:**
```
script:   .claude/producao/gerar-carroseis.py
output:   .claude/producao/carroseis-abril-2026/png/{slug}/slide-XX.png
cache:    .claude/producao/.img-cache/
```

**Para rodar:**
```bash
cd "EMPRESA TRIFORCE AUTO/.claude/producao"
python gerar-carroseis.py
```

Na primeira execução: baixa fotos do Unsplash e logos das empresas.
Na segunda execução: tudo em cache, roda em segundos.

---

## Paleta e identidade visual

```
#0A0A0A   preto absoluto   → covers, CTAs, spotlights, slides data
#F5F0EB   bege quente      → slides de conteúdo internos
#FF6B00   laranja vibrante → destaque, dado forte, primeira linha de spotlight
```

**Fonte:** Inter (900/800/700/600/500/400) — carregada do Google Fonts pelo Chromium.

**Regra do laranja:** é reserva de atenção. Um elemento laranja por slide. Se tudo está laranja, nada chama atenção. Use para: o número mais importante, a palavra mais forte, a primeira linha do spotlight, o CTA.

---

## Os 4 tipos de slide de conteúdo

### `layout="standard"` — abertura com impacto visual
Estrutura: título (56px, peso 900) + corpo (27px, linha 1.62) + **foto flex:1**

A foto preenche todo o espaço restante abaixo do texto. Se o corpo tem 1–2 frases, a foto ocupa 60–65% do slide. Esse é o layout de entrada — texto curto, imagem domina, impacto imediato.

```python
("content", {
    "num": 2,
    "layout": "standard",
    "photo_query": "chave-do-SLIDE_PHOTO_IDS",
    "title": "Título do slide",
    "body": "Uma frase direta com <strong>destaque inline</strong>."
})
```

---

### `layout="heavy"` — desenvolvimento, texto longo
Estrutura: título menor (46px) + corpo maior (24px, linha 1.72) + foto com altura proporcional ao texto

Quando há 3–5 frases de explicação, use heavy. O título é menor para dar espaço ao texto. A foto aparece abaixo do texto com altura que complementa — não deve deixar espaço vazio.

**REGRA CRÍTICA sobre altura de foto no layout heavy:**
A função `_img_box()` aceita `height="flex"` ou `height="NNNpx"`.

- `height="flex"` → foto preenche todo o espaço restante (flex:1)
- `height="300px"` → foto ocupa exatamente 300px, texto ocupa o resto

Se o texto for longo e a foto estiver com height fixa pequena, pode sobrar espaço vazio entre a foto e o footer. Ajustar: aumentar a height ou mudar para flex.

```python
("content", {
    "num": 4,
    "layout": "heavy",
    "photo_query": "chave-relevante",
    "photo_height": "320px",   # use flex se quiser que preencha tudo
    "title": "Desenvolvimento do argumento",
    "body": "Parágrafo 1 com <strong>destaque</strong>.<br><br>Parágrafo 2. Mais explicação. <strong>Conclusão forte.</strong>"
})
```

---

### `layout="spotlight"` — virada, frase de impacto máximo
Estrutura: fundo escuro (#0A0A0A) + tag (@triforceauto) no topo + frase grande + sub-texto + footer

Sem foto. Sem bege. Slide completamente escuro — é uma pausa visual dentro do carrossel.

A frase vem no campo `accent`, com `\n` separando as linhas:
```python
"accent": "Linha em laranja.\nLinhas em branco.\nUma ideia por linha."
```

**REGRA ABSOLUTA sobre cor:**
- Primeira linha → `#FF6B00` (laranja)
- Todas as outras linhas → `#FFFFFF` peso 900 (branco pesado)

❌ **NUNCA laranja em todas as linhas.** Fica horrível — parece alerta de trânsito, não design editorial.

O sub-texto (campo `body`) aparece abaixo da frase principal, em cinza, com borda laranja vertical à esquerda.

```python
("content", {
    "num": 5,
    "layout": "spotlight",
    "accent": "Não precisa de\ntech.\nPrecisa de\nprocesso.",
    "body": "Sabe como você atende hoje? Isso é tudo que precisa. A gente pega esse processo e coloca pra rodar sozinho."
})
```

---

### `layout="data"` — comparação com dado numérico
Slide escuro completo (#0A0A0A) — template próprio, sem header/footer bege.

Estrutura:
- Tag (@triforceauto) + título + subtítulo → topo
- **Dois blocos full-width** (flex:1 cada) → corpo
- Source attribution → rodapé

Cada bloco contém: nome + percentual (topo), número gigante 200px (meio), barra de progresso (fundo).

Bloco destacado (Claude): fundo laranja translúcido + número em #FF6B00
Bloco secundário (ChatGPT): fundo escuro + número apagado

```python
("content", {
    "num": 2,
    "layout": "data",
    "title": "O dado que ninguém esperava",
    "body": "Crescimento em uso corporativo — Q1 2026 (Ramp AI Index)",
    "chart": [
        {"stat": "6×", "label": "mais crescimento do Claude", "color": "#FF6B00"},
        {"label": "Claude",  "pct": 86, "val": "6×", "color": "#FF6B00"},
        {"label": "ChatGPT", "pct": 14, "val": "1×", "color": "#555"},
        {"source": "Ramp AI Index — transações reais, não pesquisa"},
    ]
})
```

**Estrutura do `chart`:**
- `{"stat": ..., "label": ..., "color": ...}` → item de stat (não vira barra, só referência)
- `{"label": ..., "pct": ..., "val": ..., "color": ...}` → barra de comparação
- `{"source": ...}` → attribution no rodapé

---

## Fotos — Regras absolutas (aprendidas na produção real)

### REGRA 1: Nunca repetir fotos no mesmo carrossel

**Cada slide com foto usa uma `photo_query` diferente.** Usar a mesma chave em dois slides = mesma foto aparece duas vezes = leitor percebe = carrossel amador.

Verifique: antes de fechar o carrossel, liste todas as `photo_query` usadas. Nenhuma pode se repetir. Se não tiver chave nova suficiente no `SLIDE_PHOTO_IDS`, adicione novas entradas antes de rodar.

### REGRA 2: `photo_height: "flex"` é sempre o padrão — SEMPRE

`flex` significa: a foto ocupa exatamente o espaço que sobrar depois do texto. Se o texto é curto → foto grande. Se o texto é longo → foto menor. **Nunca deixa espaço em branco. Nunca corta.**

```python
# CORRETO — foto se adapta ao texto automaticamente
("content", {
    "layout": "standard",
    "photo_height": "flex",   # ← sempre isso, salvo exceção justificada
    "title": "...",
    "body": "..."
})
```

Alturas fixas em pixels (`"320px"`, `"420px"`) SÓ se usadas quando você quer deliberadamente comprimir a foto independente do texto — raramente necessário.

### REGRA 3: Texto longo demais + foto = sem foto

Se o slide `heavy` tem 5+ frases longas, a foto flex vai virar uma tira de ~150px de altura — parece cortada, é feia. **Solução: remova a foto desse slide.** Use `spotlight` ou `data` para alternar o ritmo visual.

**Critério prático:**
- Título + corpo ocupa mais de 900px de altura → não coloca foto
- Título + corpo ocupa entre 500–900px → foto flex funciona bem
- Título + corpo ocupa menos de 500px → foto flex domina o slide (ideal para abertura)

### REGRA 4: Toda foto precisa ter relação visual com o tema

A foto não é decoração. O leitor olha a foto e instantaneamente entende do que o slide fala — antes de ler uma palavra.

❌ **Errado:** slide sobre automação de processos → foto de datacenter genérica
✅ **Certo:** slide sobre automação de processos → foto de alguém mapeando um fluxo, post-its no quadro, teclado com código

❌ **Errado:** slide sobre IA em pequenos negócios → foto de arranha-céus
✅ **Certo:** slide sobre IA em pequenos negócios → foto de dono de loja atendendo cliente, café, barbearia

**Antes de escolher a `photo_query`, se pergunte:** "Um leitor que vê só essa foto entende o contexto do slide?"

### Ritmo visual — padrão de 6 slides

```
Slide 1 (cover):       foto full escura — editorial, foto domina
Slide 2 (standard):    foto flex — texto curto, foto grande, impacto
Slide 3 (spotlight):   sem foto — pausa dramática, slide escuro
Slide 4 (data/heavy):  sem foto OU foto flex com texto médio
Slide 5 (heavy):       foto flex — texto mais longo, foto menor naturalmente
Slide 6 (CTA):         sem foto — escuro como cover
```

O carrossel precisa **respirar**. Cover escuro → bege aberto → escuro de pausa → dados → bege argumento → escuro CTA = ritmo profissional.

---

## Sistema de fotos — tudo sobre os IDs

### Fotos de cover (COVER_PHOTOS)
Uma por carrossel, ID completo com `photo-` no dicionário:

```python
COVER_PHOTOS = {
    "01-meta-muse-spark":      "https://images.unsplash.com/photo-1609921141835-710b7fa6e438?w=1080&h=1350&fit=crop&auto=format&q=85",
    "02-anthropic-sp":         "https://images.unsplash.com/photo-1519501025264-65ba15a82390?w=1080&h=1350&fit=crop&auto=format&q=85",
    "03-claude-mythos":        "https://images.unsplash.com/photo-1614064641938-3bbee52942c7?w=1080&h=1350&fit=crop&auto=format&q=85",
    "04-claude-vs-chatgpt":    "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=1080&h=1350&fit=crop&auto=format&q=85",
    "05-ia-pequenos-negocios": "https://images.unsplash.com/photo-1503951914875-452162b0f3f1?w=1080&h=1350&fit=crop&auto=format&q=85",
}
```

### Fotos por slide (SLIDE_PHOTO_IDS)
**SEM o prefixo `photo-`** — o template adiciona automaticamente:

```python
SLIDE_PHOTO_IDS = {
    "social-media-app-smartphone":        "1432888498266-38ffec3eaf0a",
    "whatsapp-chat-messaging":            "1600880292203-757bb62b4baf",
    "small-business-owner-customer":      "1556742049-0cfed4f6a45d",
    "question-uncertainty-thinking":      "1454165804606-c3d57bc86b40",
    "artificial-intelligence-technology": "1677442135703-1787eea5ce01",
    "brazil-business-office-work":        "1554224155-6726b3ff858f",
    "open-door-opportunity-light":        "1441986300917-64674bd600d8",
    "neural-network-brain-ai":            "1620712943543-bcc4688e7485",
    "security-restricted-access-lock":    "1555949963-ff9fe0c870eb",
    "futuristic-technology-abstract":     "1518770660439-4636190af475",
    "data-analytics-chart-growth":        "1460925895917-afdab827c52f",
    "corporate-office-meeting-team":      "1497366811353-6870744d04b2",
    "comparison-balance-choice":          "1551836022-deb4988cc6c0",
    "strategy-decision-thinking-business":"1529699211952-734e80c4d42b",
    "barber-scissors-haircut":            "1562004760-aceed7bb0fe3",
    "personal-trainer-gym-fitness":       "1534438327276-14e5300c3a48",
    "entrepreneur-laptop-startup":        "1516321318423-f06f85e504b3",
    "smartphone-message-notification":    "1511707171634-5f897ff02aa9",
}
```

### Como a URL é construída no código
```python
url = f"https://images.unsplash.com/photo-{photo_id}?w=1080&h=1350&fit=crop&auto=format&q=85"
```

Se o ID no dicionário tiver `photo-` incluído → URL vira `photo-photo-XXXX` → **404 em todas as fotos**.

### Formato válido de ID Unsplash
IDs do CDN `images.unsplash.com` têm sempre o formato longo:
```
XXXXXXXXXX-XXXXXXXXXXXX
(dois blocos numéricos separados por hífen)
Exemplo: 1432888498266-38ffec3eaf0a
```

IDs curtos tipo `ZMlcuVf2URA` (base62) são IDs de página, **não funcionam no CDN**.

### Como encontrar e adicionar novos IDs — workflow com Firecrawl

Quando o `SLIDE_PHOTO_IDS` não tem uma chave adequada para o tema do slide, use este fluxo:

**Passo 1 — buscar no Unsplash via Firecrawl search:**
```bash
firecrawl search "unsplash person using laptop startup office" --limit 5 -o .firecrawl/unsplash-search.md
```

Busque em inglês, termos visuais concretos. Evite conceitos abstratos ("technology", "future") — prefira cenas reais ("person coding laptop", "barber cutting hair", "small shop owner").

**Passo 2 — pegar o ID longo da URL da foto:**
A URL da página de uma foto no Unsplash é `unsplash.com/photos/XXXX-YYYYYYY`.
O ID da imagem CDN está no formato longo: `1234567890123-abcdef123456`.

Para resolver um ID curto (página) para o ID longo (CDN), use:
```python
import urllib.request

class NoRedirect(urllib.request.HTTPErrorProcessor):
    def http_response(self, req, resp):
        return resp

opener = urllib.request.build_opener(NoRedirect)
opener.addheaders = [("Referer", "https://unsplash.com/")]
resp = opener.open(f"https://unsplash.com/photos/{short_id}/download?force=true")
location = resp.headers.get("Location", "")
# location = "https://images.unsplash.com/photo-1234567890123-abcdef123456?..."
long_id = location.split("photo-")[1].split("?")[0]
```

**Passo 3 — adicionar ao dicionário:**
```python
SLIDE_PHOTO_IDS = {
    ...
    "nome-descritivo-da-cena": "1234567890123-abcdef123456",   # sem photo-
}
```

**Passo 4 — testar antes de rodar tudo:**
```bash
# Baixar só essa foto para verificar visualmente
python -c "
from pathlib import Path
import urllib.request, base64
photo_id = '1234567890123-abcdef123456'
url = f'https://images.unsplash.com/photo-{photo_id}?w=400&h=500&fit=crop&auto=format&q=85'
urllib.request.urlretrieve(url, '.img-cache/test.jpg')
print('Foto baixada em .img-cache/test.jpg')
"
```

Abrir `.img-cache/test.jpg` e confirmar que a foto faz sentido para o slide antes de commitar.

### Regra de unicidade por carrossel
- Cada slide DEVE ter uma `photo_query` diferente
- Foto do cover ≠ fotos dos slides internos (IDs diferentes)
- Fotos tematicamente autoexplicativas: alguém vê a foto sem ler → entende o contexto do slide

---

## Estrutura de um carrossel — é flexível, não predefinida

**Não existe sequência obrigatória de slides.** O copy define quantos slides, em que ordem, com que densidade de texto. O design adapta.

A única regra fixa: **último slide é sempre CTA.**

O resto depende do que Fecchio entregou. Um carrossel pode ter 5 slides ou 8. Pode ter dois spotlights seguidos. Pode não ter nenhum dado. Pode ter três heavy consecutivos. Cada conteúdo tem sua estrutura ideal.

### Anatomia de cada tipo de slide

**`cover`** — sempre o primeiro:
```python
("cover", {
    "headline": "Manchete em até 8 palavras fortes",
    "subheadline": "Uma linha de contexto — o que o leitor vai aprender",
})
```

**`content` standard** — texto curto, foto domina:
```python
("content", {
    "num": N,
    "layout": "standard",
    "photo_query": "chave-unica-no-SLIDE_PHOTO_IDS",
    "photo_height": "flex",   # SEMPRE flex — foto preenche o que sobrar
    "title": "Título direto",
    "body": "1–2 frases com <strong>destaque</strong>."
})
```

**`content` heavy** — texto longo, foto menor:
```python
("content", {
    "num": N,
    "layout": "heavy",
    "photo_query": "chave-unica-diferente-das-outras",
    "photo_height": "flex",   # SEMPRE flex — nunca fixo em pixels
    "title": "Título",
    "body": "3–5 frases.<br><br>Segundo parágrafo. <strong>Conclusão.</strong>"
})
```

> **Se o texto for muito longo (5+ frases densas):** remova a foto completamente — não passe `photo_query`. O slide fica só texto no bege. Isso é melhor do que foto virar tira de 150px.

**`content` spotlight** — pausa dramática, sem foto:
```python
("content", {
    "num": N,
    "layout": "spotlight",
    "accent": "Primeira linha em laranja.\nDemais linhas em branco.\nUma ideia por linha.",
    "body": "Sub-texto em cinza abaixo da frase principal."  # pode ser ""
})
```

**`content` data** — comparação numérica, sem foto:
```python
("content", {
    "num": N,
    "layout": "data",
    "title": "Título do dado",
    "body": "Contexto — fonte, período",
    "chart": [
        {"label": "Opção A", "pct": 85, "val": "6×",  "color": "#FF6B00"},
        {"label": "Opção B", "pct": 15, "val": "1×",  "color": "#555"},
        {"source": "Fonte — metodologia"},
    ]
})
```

**`cta`** — sempre o último:
```python
("cta", {
    "main": "Frase principal com <span>destaque em laranja</span>.",
    "sub": "Sub-texto — o que fazer agora."
})
```

### Exemplo real de estrutura variável

```python
# 5 slides — carrossel enxuto
slides = [cover, standard, spotlight, heavy, cta]

# 7 slides — carrossel completo
slides = [cover, standard, spotlight, heavy, data, heavy, cta]

# 6 slides — com dois argumentos
slides = [cover, standard, heavy, data, heavy, cta]
```

O número e a ordem emergem do copy. O design não força.

---

## Erros que VÃO acontecer — causas e soluções

### Erro: 404 em todas as fotos de slide
**Sintoma:** imagens não aparecem, slides ficam com fundo preto sólido
**Causa:** ID com prefixo `photo-` no dicionário + template adiciona outro `photo-`
**Solução:** remover `photo-` de todos os IDs em `SLIDE_PHOTO_IDS`. Verificar com:
```python
# ID correto:
"barber-scissors-haircut": "1562004760-aceed7bb0fe3"
# ID errado (404):
"barber-scissors-haircut": "photo-1562004760-aceed7bb0fe3"
```

### Erro: 404 com ID curto
**Sintoma:** erro de status 404 ao tentar baixar a foto
**Causa:** ID base62 tipo `ZMlcuVf2URA` não funciona no CDN
**Solução:** usar apenas IDs numéricos longos. Ver seção "Como adicionar um novo ID".

### Erro: `KeyError: 'label'` no chart
**Causa:** loop de barras tentando acessar `item['label']` no item `{"source": "..."}`
**Solução:** verificar o tipo do item antes:
```python
for item in chart:
    if "source" in item: continue   # pula o attribution
    if "stat"   in item: continue   # pula o stat highlight
    # agora é seguro
    bar_color = item.get("color", "#555")
    rows += f'... {item["label"]} ... {item["pct"]}% ...'
```

### Erro: espaço vazio abaixo da foto
**Causa:** `height="300px"` fixo quando o texto acima é curto — sobra espaço vazio preto ou bege abaixo
**Solução:** usar `height="flex"` quando o texto for curto. Usar altura fixa só quando há texto suficiente para preencher o espaço acima.

### Erro: spotlight com laranja em todo o texto
**Causa:** CSS sem especificidade suficiente para só a primeira linha
**Solução no CSS:**
```css
.spot-line              { color: #FFFFFF; }          /* todas brancas */
.spot-line:first-child  { color: #FF6B00; }          /* só a primeira laranja */
```

### Erro: slide data com espaço vazio no meio
**Causa:** containers com `flex:1` e poucos elementos — elementos centralizam e deixam vazio
**Solução:** usar dois blocos full-width com `justify-content: space-between` internamente — nome no topo, número no centro, barra no fundo. Os blocos preenchem a altura naturalmente.

---

## Componentes CSS — valores exatos em uso

### Stripe laranja topo (slides bege)
```css
.top-stripe { width: 100%; height: 5px; background: #FF6B00; }
```

### Header dos slides bege
```css
.header-handle { font-size: 18px; font-weight: 700; color: #FF6B00; }
.header-mid    { font-size: 17px; font-weight: 500; color: #aaa; }
.header-right  { font-size: 17px; font-weight: 400; color: #bbb; }
```

### Tipografia slides bege (standard/heavy)
```css
h2   { font-size: 56px; font-weight: 900; color: #0A0A0A; letter-spacing: -0.03em; }
.body { font-size: 27px; font-weight: 400; color: #2a2a2a; line-height: 1.62; }
/* heavy: */
h2[heavy] { font-size: 46px; }
.body[heavy] { font-size: 24px; line-height: 1.72; }
```

### Spotlight
```css
.spot-line              { font-size: 80px; font-weight: 900; color: #FFFFFF; line-height: 1.0; letter-spacing: -0.03em; }
.spot-line:first-child  { color: #FF6B00; }
.spot-sub               { font-size: 24px; font-weight: 400; color: rgba(255,255,255,0.50); border-left: 3px solid #FF6B00; padding-left: 22px; }
```

### Data slide — blocos de comparação
```css
.dblock-num  { font-size: 200px; font-weight: 900; line-height: 0.85; letter-spacing: -0.05em; }
.dblock-name { font-size: 28px; font-weight: 800; }
.dblock-pct  { font-size: 28px; font-weight: 800; }
.dblock-track { height: 14px; border-radius: 7px; }
```

### Cover
```css
h1              { font-size: 72px; font-weight: 900; color: #FFFFFF; line-height: 1.05; letter-spacing: -0.02em; }
.subheadline    { font-size: 28px; font-weight: 400; color: rgba(255,255,255,0.65); border-left: 3px solid #FF6B00; padding-left: 20px; }
```

---

## Princípios de design descobertos na prática

**1. Laranja é reserva de atenção, não decoração**
Um elemento laranja por slide. O elemento mais importante. Se tudo for laranja, nada chama atenção.

**2. Escuro e claro criam ritmo**
Cover escuro → slides bege → spotlight escuro → slides bege → CTA escuro.
Slides do mesmo fundo em sequência ficam monótonos. Alternar é criar respiração.

**3. Foto diferente = narrativa visual**
A foto de barbearia no slide de barbearia não é decoração — é contexto visual que prepara o leitor antes de ler uma palavra. Foto genérica = slide genérico. Foto relevante = slide que pertence ao carrossel.

**4. Variedade de tamanho de foto = variedade de ritmo**
Foto grande = impacto. Foto pequena = leitura densa. O olho segue o ritmo antes de ler o texto. Todos os slides com foto do mesmo tamanho = feed entediante.

**5. Números grandes = credibilidade**
Um `6×` em 200px comunica mais do que "cresceu 6 vezes" no corpo do texto. Dados merecem tratamento visual proporcional.

**6. O carrossel é um roteiro, não uma lista**
Cada slide tem papel: abertura (gancho), desenvolvimento (argumento), virada (spotlight), dado (prova), conclusão (heavy), CTA (conversão). Escrever slides como lista = slides sem tensão. Escrever como roteiro = carrossel que leva o leitor.

**7. flex:1 em foto nunca deixa espaço vazio**
A regra de ouro: usar `flex:1` na foto e deixar o CSS decidir quanto espaço ela ocupa. Altura fixa só quando o designer sabe exatamente quanto texto vai aparecer no slide.
