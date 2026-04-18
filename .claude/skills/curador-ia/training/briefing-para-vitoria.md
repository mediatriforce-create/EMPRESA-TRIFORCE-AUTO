---
skill: curador-ia
doc: briefing-para-vitoria
version: "2.0"
update_reason: "Rafael + Fecchio entregam o Python completo com visuais incluídos — Vitória só roda o gerador"
---

# Briefing para Vitória — v2.0

## O que mudou

Na v1.0, Rafael entregava um briefing em texto e Vitória buscava as imagens.
Isso criava retrabalho: Vitória tinha que descobrir o visual de cada slide do zero.

**Na v2.0:** Rafael + Fecchio entregam o dicionário Python completo — texto, estrutura e visuais já resolvidos. Vitória cola no `gerar-carroseis.py` e roda.

---

## Pipeline novo

```
Rafael (pesquisa + visuais) ──┐
                               ├──► estrutura Python completa ──► Vitória (roda gerador) ──► Bruno (revisa)
Fecchio (copy dos slides)  ──┘
```

### O que Rafael entrega para Fecchio

- Fatos verificados com fonte (ex: "SWE-bench 87,6% — fonte: anthropic.com/news/claude-opus-4-7")
- **URLs de visuais por tema** encontradas nas fontes oficiais:
  - Gráficos e tabelas de benchmark → URL direta do CDN da empresa
  - Logo oficial → URL do press kit ou Clearbit
  - Interface do produto → URL da imagem no blog/press kit oficial
  - Se não encontrou visual oficial → descreve a cena ideal (vira `photo_query` Unsplash)
- Contexto editorial: por que importa agora, para quem

### O que Fecchio entrega para Vitória

O dicionário Python do carrossel, pronto para colar no `CARROSEIS`:

```python
{
    "slug": "11-nome-do-tema",
    "cover_photo_query": "descrição visual da cover em inglês",  # ou cover_image_url se encontrou
    "slides": [
        ("cover", {
            "headline": "Título sem ponto final",
            "subheadline": "Contexto em 1-2 linhas sem ponto final",
        }),
        ("content", {
            "num": 2,
            "layout": "standard",         # standard | heavy | spotlight | data
            "image_url": "https://cdn.empresa.com/imagem-real.png",  # visual encontrado por Rafael
            "title": "Título sem ponto final",
            "body": "Texto com <strong>dado</strong> em bold. Fonte inline (empresa, mês/ano)",
        }),
        ("content", {
            "num": 3,
            "layout": "spotlight",
            "accent": "Frase de impacto\nem duas linhas",
            "title": "", "body": "Subtexto opcional do spotlight",
        }),
        ("cta", {
            "main": "Linha principal<br><span>Linha em laranja</span>",
            "sub": "Descrição do canal — @triforceauto",
        }),
    ]
}
```

---

## Campos de visual por slide — escolher o mais certo, não o mais fácil

Cada slide tem UMA fonte de visual. Rafael encontra o melhor disponível, Fecchio decide qual campo usar:

| Campo | Quando usar | Exemplo |
|---|---|---|
| `image_url` | URL direta de imagem pública (CDN, press kit, blog oficial) | Gráfico do SWE-bench da Anthropic, logo do produto, screenshot de interface |
| `photo_query` | Nenhuma imagem real encontrada → Unsplash API busca automaticamente | `"entrepreneur laptop startup"`, `"robot handshake human"` |
| `screenshot_file` | Print manual salvo em `banco-de-imagens/manual/` | Tweet relevante, interface que precisa de login |

**Regra:** não é um tipo só. Um carrossel pode ter `image_url` no slide 2, `photo_query` no slide 4, `spotlight` sem foto no slide 3. O visual serve o conteúdo — não o contrário.

### Como Rafael encontra image_url

1. Acessa a fonte da notícia (anthropic.com, openai.com, techcrunch, etc.)
2. Inspeciona as imagens da página (gráficos, interfaces, tabelas)
3. Pega a URL direta do CDN — ex: `https://www-cdn.anthropic.com/images/.../chart.png`
4. Testa se a URL é acessível diretamente (sem login, sem redirect de autenticação)
5. Se sim → coloca como `image_url` no slide correspondente
6. Se não → usa `photo_query` com descrição visual precisa em inglês

### photo_query: como escrever bem

- Descreve a cena, não o conceito: `"man reviewing code on monitor at night"` > `"software developer"`
- Sem abstrações: `"lock on laptop keyboard security"` > `"cybersecurity concept"`
- Sem marca/empresa: `"ai chatbot interface dark screen"` > `"claude interface"`
- Em inglês sempre (Unsplash API)

---

## Regras de copy para os slides

- **Zero pontos finais** em `title` e `headline`
- **Zero travessões (—)** — usar vírgula, ponto, dois pontos ou quebrar em frase nova
- `body` pode ter ponto final, mas cada parágrafo máximo 2 linhas
- Fonte sempre inline no corpo: `(anthropic.com, abr/2026)` — nunca numa nota separada
- Bold (`<strong>`) só no dado mais importante do slide — 1 por slide no máximo
- Spotlights: `accent` é a frase de impacto. Primeira linha fica laranja automaticamente. Não colocar ponto final
- Slides `data`: usa o campo `chart` com lista de itens, não `body`

---

## Checklist antes de entregar para Vitória

- [ ] Todos os `title` e `headline` sem ponto final
- [ ] Nenhum travessão (—) em títulos
- [ ] Cada slide tem um visual definido (`image_url`, `photo_query`, ou sem foto para spotlight/data)
- [ ] Nenhum `photo_query` se repete no mesmo carrossel
- [ ] Spotlights têm `"title": ""` e `"body": ""`  mesmo que vazios
- [ ] Cover tem `cover_photo_query` ou `cover_image_url`
- [ ] Último slide é `("cta", {...})`
- [ ] Fonte citada em pelo menos 1 dado por slide
