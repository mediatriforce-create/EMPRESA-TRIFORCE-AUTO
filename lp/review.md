# Code Review — lp/index.html
**Revisor:** Marcelo (Revisor Senior, Triforce Auto)
**Data:** 2026-04-19
**Arquivo:** `lp/index.html`

---

## Resumo executivo

Código bem estruturado para o objetivo. HTML semântico consistente, JS limpo, performance sólida. Nenhum bloqueante crítico. Há três pontos importantes a corrigir antes de divulgar amplamente e um conjunto de nits menores.

---

## 🔴 Bloqueante

Nenhum.

---

## 🟡 Importante

### 1. SVGs decorativos sem `aria-hidden="true"`
Todos os SVGs inline (ícones de check, X, seta, logo triforce) são puramente decorativos mas estão sem `aria-hidden="true"`. Leitores de tela vão tentar interpretá-los como conteúdo, gerando ruído para usuários com deficiência visual.

**Afeta:** logo nav (linha 164), logo footer (linha 907), todos os ícones de check/X nas seções problema, solução, para-quem, incluído, trust strips.

**Correção:** adicionar `aria-hidden="true"` em cada `<svg>` decorativo. Exemplo:
```html
<svg aria-hidden="true" ...>
```

---

### 2. FAQ sem `aria-expanded` nos botões
Os botões `.faq-trigger` não atualizam `aria-expanded` quando o accordion abre/fecha. Usuários de leitor de tela não têm feedback sobre o estado do painel.

**Linha:** 768, 782, 795, 804, 816, 828 (todos os `<button class="faq-trigger">`).

**Correção:** inicializar com `aria-expanded="false"` no HTML e atualizar via JS no evento de click:
```js
btn.setAttribute('aria-expanded', !isOpen);
```

---

### 3. `og:image` ausente
Todas as outras OG tags estão presentes (`og:title`, `og:description`, `og:type`), mas falta `og:image`. Compartilhamento no WhatsApp e Facebook vai sair sem preview visual, o que reduz significativamente o CTR de link compartilhado.

**Linha:** entre as linhas 8–10 do `<head>`.

**Correção:**
```html
<meta property="og:image" content="https://seudominio.com/og-image.jpg" />
<meta property="og:url" content="https://seudominio.com/" />
```

---

## 🔵 Nit

### N1. `font-700` e `font-600` como classes Tailwind não existem nativamente
O projeto usa `font-700` e `font-600` extensivamente (ex: linhas 169, 228, 245). Essas classes não são tokens padrão do Tailwind — o correto seria `font-bold` (700) e `font-semibold` (600). Funcionam porque o Tailwind CDN é permissivo com valores arbitrários implícitos, mas é frágil se migrar para build com purge/JIT estrito.

**Recomendação:** substituir `font-700` → `font-bold` e `font-600` → `font-semibold` no HTML inteiro.

---

### N2. `opacity-8` não é um token Tailwind válido
Linha 853: `class="... opacity-8 ..."`. O Tailwind não tem `opacity-8` na escala padrão (vai de `opacity-5` para `opacity-10`). O efeito provavelmente está sendo ignorado silenciosamente.

**Correção:** usar `opacity-5` ou `opacity-10`, ou valor arbitrário `opacity-[0.08]`.

---

### N3. Número do WhatsApp placeholder não deve ir ao ar
Linha 872: `https://wa.me/5511999999999` — número fictício. Não é um bug de código, mas se for ao ar assim quebra o único CTA real da página.

**Ação:** substituir pelo número real antes do deploy.

---

### N4. `closeMobileMenu` registrada duas vezes nos links mobile
Os links do menu mobile têm `onclick="closeMobileMenu()"` inline (linhas 198–204) **e** também recebem o listener via `document.querySelectorAll('#mobile-menu a').forEach(...)` no JS (linha 992–994). A função será chamada duas vezes a cada clique. Funciona sem bug visível, mas é código duplicado.

**Correção:** remover os atributos `onclick` inline do HTML e manter apenas o listener do JS.

---

### N5. Sem `<main>` wrapping o conteúdo principal
O corpo da página tem `<nav>`, `<section>`s, `<footer>` mas não há `<main>`. Semanticamente correto seria envolver as sections em `<main>` para navegação por landmarks.

---

### N6. Título do documento é muito longo para SERPs
Linha 6: o `<title>` tem 68 caracteres. Google trunca em ~55–60 caracteres no desktop. O sufixo `"do briefing ao ar em 10 dias"` vai ser cortado.

**Sugestão:** `Triforce Auto — Landing Page que converte em 10 dias`

---

## Checklist final

| Critério | Status |
|---|---|
| `lang="pt-BR"` | ✅ |
| `<title>` presente | ✅ (longo demais — N6) |
| Meta description | ✅ |
| OG tags | ⚠️ falta `og:image` (I3) |
| H1 único | ✅ |
| Hierarquia h1 → h2 → h3 | ✅ |
| HTML semântico (section, nav, footer) | ✅ (falta `<main>` — N5) |
| SVGs com aria-hidden | ❌ (I1) |
| Botões com aria-label ou texto | ✅ (menu btn tem aria-label) |
| FAQ aria-expanded | ❌ (I2) |
| Formulários com labels | N/A (não há form na página) |
| Contraste texto/fundo | ✅ (dark bg + text claro) |
| Tailwind CDN único recurso externo | ✅ (+ Google Fonts, ambos justificados) |
| JS sem vazamento de memória | ✅ |
| Event listeners duplicados | ⚠️ mobile menu (N4) |
| Intersection Observer com unobserve | ✅ |
| Menu mobile funciona | ✅ |
| Responsivo mobile | ✅ |
| Classes Tailwind consistentes | ⚠️ font-700/600 não-padrão (N1), opacity-8 inválido (N2) |
