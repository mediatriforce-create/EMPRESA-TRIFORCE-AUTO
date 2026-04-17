# Validação Estratégica — Designer UI/UX Senior (Camila)
**Data:** 2026-04-13
**Responsável:** Gabriela (RH)
**Fonte dos dados:** web.dev, developers.figma.com, npmjs.com, perplexity_search, alexbobes.com

---

## TABELA DE VALIDAÇÃO

| Framework | Status | Fonte | Notas |
|-----------|--------|-------|-------|
| **CLS < 0.1 para design** (imagens sem dimensões causam layout shift) | VALIDADO | [web.dev/articles/cls](https://web.dev/articles/cls) | Confirmado: imagens sem `width` + `height` são causa direta de CLS. Fix: atributos de dimensão + CSS `aspect-ratio`. Threshold: ≤0.1 = bom, 0.1–0.25 = médio, >0.25 = ruim. Medido no P75 de page loads. |
| **figma-tokens-to-tailwind-variables** (npm package) | ATUALIZAR | [npmjs.com](https://www.npmjs.com/package/figma-tokens-to-tailwind-variables) | Pacote v1.1.3, última publicação há ~9 meses. Funciona (converte JSON Figma Tokens → Tailwind CSS variables) mas **sem manutenção ativa** e zero dependentes no registry. Não é a opção recomendada para produção. |
| **Token Studio** (alternativa ao pacote acima) | VALIDADO | [tokens-studio/figma-plugin GitHub](https://github.com/tokens-studio/figma-plugin) | Ativo em 2025–2026 com plano Pro e desenvolvimento contínuo. Pipeline recomendado: Token Studio → JSON → Style Dictionary → `tailwind.config.js`. É a opção robusta para projetos em escala. |
| **Plugin Figma Token Exporter** (zero-config) | VALIDADO | [figma.com/community/plugin/1345069854741911632](https://www.figma.com/community/plugin/1345069854741911632) | Exporta Figma Variables diretamente em formato Tailwind/CSS/SASS. Opção mais simples para projetos menores da Triforce. Recomendado como primeira escolha. |
| **Benchmarks de conversão 2–6% para serviços locais** | VALIDADO COM REFINAMENTO | Unbounce, landerlab.io, seedprod.com, growmyads.com | Faixa geral 2–6% confirmada para LP de serviços locais com tráfego pago. Refinamento: serviços locais com WhatsApp + prova social atingem **4–8%** (dados de agências BR). Benchmark Unbounce (57M conversões, 41K LPs) serve como referência por setor. |
| **Figma Component Properties → React Props** (artigo figma.com/blog/the-shared-language-of-props/) | VALIDADO | [figma.com/blog/the-shared-language-of-props/](https://www.figma.com/blog/the-shared-language-of-props/) | URL acessível e artigo ainda relevante em 2026. Conceito central (vocabulary alignment entre design props e code props) é a base do Figma Code Connect atual. Tabela de mapeamento do scan-estrategico.md permanece válida. |

---

## DETALHAMENTO POR FRAMEWORK

### 1. Core Web Vitals — CLS < 0.1

**Status: VALIDADO**

Causa confirmada pelo artigo oficial web.dev:
- Imagens/vídeos sem dimensões explícitas são causa primária de CLS
- Recursos assíncronos sem espaço reservado
- Conteúdo de terceiros (ads, widgets) que redimensiona dinamicamente
- Fontes que renderizam diferente do fallback

**Fix confirmado:**
```html
<!-- ERRADO: causa CLS -->
<img src="foto.jpg" alt="...">

<!-- CORRETO: reserva espaço antes de carregar -->
<img src="foto.jpg" width="800" height="600" alt="...">
```

**Relevância para Camila:** Todo componente de imagem no design (galeria de portfólio, fotos de equipe, before/after) deve ter dimensões explícitas no Figma e no código gerado. `get_design_context` pode gerar código sem `width`/`height` — Camila deve revisar esse ponto no handoff.

---

### 2. figma-tokens-to-tailwind-variables

**Status: ATUALIZAR — usar alternativa**

O pacote npm `figma-tokens-to-tailwind-variables` (v1.1.3) existe e funciona, mas:
- Última publicação: ~9 meses atrás (sem manutenção ativa)
- Zero dependentes no registry npm
- Sem issues ou PRs recentes no repositório

**Recomendação atualizada para o scan-estrategico.md:**

| Opção | Maturidade | Caso de uso |
|-------|-----------|------------|
| Plugin Figma Token Exporter | Alta, ativo | Projetos pequenos/médios Triforce (RECOMENDADO) |
| Token Studio + Style Dictionary | Alta, Pro ativo | Projetos em escala com versionamento GitHub |
| figma-tokens-to-tailwind-variables (npm) | Baixa, sem manutenção | NÃO RECOMENDADO para produção |

---

### 3. Benchmarks de Conversão para Serviços Locais BR

**Status: VALIDADO COM REFINAMENTO**

Faixa 2–6% confirmada por múltiplas fontes independentes. Refinamentos para contexto BR:

| Contexto | Taxa estimada |
|----------|--------------|
| LP genérica de serviços locais (tráfego pago) | 2–6% |
| LP com WhatsApp CTA + prova social local | 4–8% |
| Desktop vs mobile | Desktop converte +8% |
| Formulário >5 campos | Queda abrupta abaixo de 2% |
| Site lento >3s no mobile | Perda significativa de tráfego local |

**Referência de benchmark por setor:** Unbounce Benchmark Report (57M conversões, 41K LPs) — `unbounce.com/conversion-benchmark-report/`

---

### 4. Figma Component Properties → React Props

**Status: VALIDADO**

Artigo `figma.com/blog/the-shared-language-of-props/` está acessível e continua sendo a referência canônica. Em 2025–2026, o conceito evoluiu para o **Figma Code Connect**, que implementa o mapeamento de forma programática:

```js
// Code Connect: Figma Variant → React prop
figma.connect(Button, 'https://figma.com/...', {
  props: {
    variant: figma.enum('Type', {
      primary: 'primary',
      secondary: 'secondary'
    }),
    disabled: figma.boolean('Disabled'),
    children: figma.string('Label')
  }
})
```

**ATENÇÃO — Restrição crítica descoberta:** Code Connect requer **plano Organization ou Enterprise** + **Full ou Dev seat**. Não disponível no plano Professional. Ver constraints-plataforma.md para detalhes.

---

## SÍNTESE DE AÇÕES PARA O STAGE 3

| Ação | Prioridade | Motivo |
|------|-----------|-------|
| Substituir `figma-tokens-to-tailwind-variables` pelo Plugin Token Exporter | ALTA | Pacote npm sem manutenção |
| Adicionar regra de dimensões explícitas em imagens no SOP de handoff | ALTA | CLS confirmado como causa direta |
| Confirmar plano Figma da Camila antes do Stage 3 | CRÍTICA | Code Connect gateado em Organization/Enterprise |
| Atualizar benchmark de conversão para 4–8% com WhatsApp | MÉDIA | Dado mais preciso para nichos BR |

---

*Validação concluída em 2026-04-13 | Gabriela (RH) | Triforce Auto*
