# Scan Estratégico — Designer UI/UX Senior (Camila)
**Data:** 2026-04-13
**Responsável:** Gabriela (RH)
**Stage:** 3 — Pesquisa de gaps estratégicos

---

## GAP 1 — Kit de Componentes para Nicho Local BR

### O que foi encontrado

- **Seções obrigatórias para LP de negócio local presencial (ordem validada):**
  Hero com CTA direto → Cardápio de Serviços com preços → Galeria/Portfólio → Equipe → Depoimentos locais → Mapa + Horários → FAQ → Rodapé completo

- **Componentes UI essenciais:**
  - Cards de serviço (imagem + título + preço + CTA)
  - Sticky CTA de WhatsApp (canto inferior direito, link pré-preenchido com serviço)
  - Carrossel de galeria com lightbox
  - Formulário curto (máx. 3-4 campos: nome, telefone, serviço)
  - Mapa embedado Google Maps com marcação de localização
  - Badge de trust: estrelas Google, número de avaliações, selos
  - Modal de confirmação de agendamento

- **Gatilhos locais BR específicos:**
  - Menção de bairro/cidade no headline (SEO local + conexão emocional)
  - Botão WhatsApp com pré-preenchimento ("Quero agendar: [serviço]")
  - Depoimentos com nome + cidade/bairro do cliente
  - Destaque de horários noturnos e finais de semana (diferencial local)

- **Recursos Figma Community identificados:**
  - `figma.com/community/file/1462650517969554341` — Small Business Landing Page (free)
  - `figma.com/community/file/1289433328810299968` — Landing Page UI Kit & Design System Vol 1.0
  - Landify (ByPeople): 500+ components, 170+ premade blocks, totalmente responsivo — referência de estrutura modular
  - `figma.com/community/file/1441856685135940864` — Landing page with design system

- **Gap específico de nicho BR:** Não existe kit Figma pronto para barbearia/salão/personal trainer BR com copy em português e gatilhos locais. A solução é montar um **kit interno** reaproveitando os templates genéricos acima + adaptar seções para os 3 nichos-alvo.

### Framework SOP — Estrutura de LP por Nicho

| Seção | Barbearia | Salão de Beleza | Personal Trainer |
|-------|-----------|-----------------|-----------------|
| Hero | "Corte + barba em [cidade]" + foto do espaço | "Transformação real em [bairro]" + before/after | "Treino 1:1 em [cidade]" + foto do treino |
| Serviços | Lista de cortes + preços fixos | Serviços + faixa de preço | Planos/pacotes de treino |
| Prova social | Google Reviews + fotos de cortes | Before/after + avaliações | Transformações de alunos |
| CTA principal | WhatsApp agendamento | WhatsApp ou form simples | Form captação + WhatsApp |
| Mapa | Obrigatório | Obrigatório | Opcional (atendimento domiciliar) |

---

## GAP 2 — Pipeline Figma Variables → Tailwind

### O que foi encontrado

- **Três abordagens viáveis identificadas (do mais simples ao mais robusto):**

  **Opção A — Plugin direto (zero-config, recomendado para a Triforce):**
  - **Figma Token Exporter** (`figma.com/community/plugin/1345069854741911632`) — exporta variáveis Figma em CSS, SASS, Less, Stylus e Tailwind com seleção de coleção/modo. Melhor para projetos menores.
  - **Tokens to Tailwind CSS** (`figma.com/community/plugin/1222415071406554904`) — gera utility classes Tailwind direto de local styles Figma.
  - **Tailwind Tokens** (tailwindtokens.com) — plugin free, sincroniza design system Figma ↔ Tailwind CSS variables instantaneamente.

  **Opção B — Token Studio + Style Dictionary (robusto, recomendado para escala):**
  - Token Studio: plugin Figma que gerencia tokens como JSON no repositório (sync com GitHub/GitLab)
  - Style Dictionary (Amazon): transforma o JSON em outputs para qualquer plataforma (CSS vars, Tailwind config, iOS, Android)
  - Documentação: `docs.tokens.studio/transform-tokens/style-dictionary`
  - Pipeline: Figma Variables → Token Studio (JSON) → Style Dictionary → `tailwind.config.js`

  **Opção C — Script manual (para quem já tem codebase):**
  - Plugin "Variables Import Export" (Magic Grass) + script Node.js
  - Gist de referência: `gist.github.com/mchlkucera/d58d58750093a860e4db5241179d43d0`
  - Requer `fs` e `lodash` instalados

- **Recurso de referência completo:** `figmafy.com/figma-variables-to-code-tokens-to-tailwind-css-vars/` — mapeia Figma Variables → Tailwind + CSS custom properties com exemplos e free token starter kit.

- **npm package direto:** `figma-tokens-to-tailwind-variables` (v1.1.3) — converte JSON do Figma Tokens para variáveis TailwindCSS.

### Framework SOP — Tokens para Triforce Auto

```
SETUP INICIAL (uma vez por cliente):
1. No Figma: criar coleções de Variables (cores, espaçamento, tipografia)
2. Instalar plugin Figma Token Exporter
3. Exportar como Tailwind → colar em tailwind.config.js do projeto
4. Definir CSS custom properties no globals.css para tokens de tema

MANUTENÇÃO:
- Toda mudança de cor/tipografia no Figma → re-exportar via plugin → atualizar config
- Token Studio (se escalar): sync automático via GitHub Actions
```

---

## GAP 3 — Figma Component Properties → React Props

### O que foi encontrado

- **Mapeamento direto entre tipos de propriedades Figma e props React:**

| Tipo Figma | Equivalente React | Exemplo |
|------------|-------------------|---------|
| **Variant** | `enum` / union type | `size: 'sm' \| 'md' \| 'lg'` |
| **Boolean** | `boolean` prop | `hasIcon: boolean`, `isDisabled: boolean` |
| **Text** | `string` prop | `label: string`, `children: ReactNode` |
| **Instance Swap** | `ReactNode` / componente injetado | `icon: ReactNode`, `leftSlot: ReactNode` |

- **Artigo canônico da Figma sobre isso:** `figma.com/blog/the-shared-language-of-props/` — melhores práticas para bridging linguagens de design e desenvolvimento. Leitura obrigatória para a Camila.

- **Atenção com Boolean props:** O artigo `component-driven.dev/articles/boolean-flags-in-figma` alerta contra abuso de boolean props em Figma — preferir Variants para estados (hover, active, disabled) em vez de booleans, pois variants geram código mais limpo.

- **Locofy como referência de mapeamento automático:**
  - Variant → enum/union props React
  - Instance Swap → children prop
  - Boolean → boolean prop
  - Documentação em `locofy.ai/docs/custom-components/structure-components/`

- **Com Figma Code Connect (já no toolkit da Camila):**
  - Variantes Figma mapeiam diretamente para props do componente React via `figma.enum()`, `figma.boolean()`, `figma.string()`
  - Exemplo: `variant: figma.enum('Size', { small: 'sm', medium: 'md', large: 'lg' })`
  - Uma vez configurado, `get_design_context` já entrega o componente com as props corretas

### Framework SOP — Estrutura de Componente Figma para React

```
REGRAS DE NOMECLATURA (Figma → React):
- Variant "State" com valores: Default, Hover, Active, Disabled → prop `state` enum
- Variant "Size" com valores: SM, MD, LG → prop `size: 'sm' | 'md' | 'lg'`
- Boolean "hasIcon" → prop `icon?: ReactNode` (opcional)
- Text "Label" → prop `children: string`
- Instance Swap "Icon" → prop `icon: React.ComponentType`

ESTRUTURA PADRÃO DE COMPONENTE:
interface ButtonProps {
  variant: 'primary' | 'secondary' | 'ghost';
  size?: 'sm' | 'md' | 'lg';
  children: string;
  icon?: React.ReactNode;
  disabled?: boolean;
  onClick?: () => void;
}
```

---

## GAP 4 — Benchmarks CRO Negócios Locais BR

### O que foi encontrado

- **Taxa de conversão média para LPs de serviços locais no Brasil (2025):**
  - Faixa geral: **2% a 6%** (tráfego pago; orgânico tende a ser mais baixo)
  - Serviços de beleza/barbearia com boa prova social e CTA WhatsApp: **4-8%** (estimativa com base em dados de agências BR)
  - Desktop converte **8% mais** que mobile (venuelabs.com/pt/landing-page-conversion-rates/) — apesar do tráfego mobile ser maior
  - Referência Unbounce: `unbounce.com/conversion-benchmark-report/` — 57M conversões em 41K LPs por setor

- **O que FUNCIONA para negócios locais BR:**
  - Botão WhatsApp com pré-preenchimento de serviço (menor atrito possível)
  - Formulário com máx. 3 campos (nome + telefone + serviço)
  - Prova social local: Google Reviews com foto + nome + bairro do cliente
  - Before/after real (barbearia: fotos de corte; salão: transformações; personal: progresso de aluno)
  - Preço visível ou faixa de preço explícita (reduz objeção de barreira financeira)
  - Horários disponíveis mencionados no hero (ex.: "Atende sábado e domingo")
  - Sticky CTA que acompanha o scroll
  - Headline com nome do bairro/cidade (ex.: "Barbearia no Itaim Bibi")

- **O que NÃO FUNCIONA:**
  - Formulários com mais de 5 campos (queda abrupta de conversão)
  - Hero com slider/carousel automático (distrai, não converte)
  - Ausência de preço ou qualquer indicativo de valor (gera insegurança)
  - Sem endereço ou mapa visível (negócio local sem localização perde confiança)
  - Copy genérico: "melhor atendimento da cidade" sem prova
  - Site lento (>3s no mobile) — maioria do tráfego local vem de celular

- **Hierarquia de conversão validada para LP local:**
  ```
  Hero (problema + solução + CTA) →
  Serviços com preço →
  Prova social (fotos reais + avaliações) →
  Sobre/equipe (humaniza) →
  Localização + horários →
  CTA final + rodapé com contato
  ```

- **Benchmark de CTA por canal BR:**
  - WhatsApp: melhor taxa de início de conversa (familiar ao público BR)
  - Ligação telefônica: funciona para público 35+ em cidades menores
  - Formulário web: funciona para nichos premium (personal trainer high-ticket)
  - Agendamento online (Calendly/etc): adoção crescendo, ainda baixa em barbearia/salão popular

---

## GAP 5 — Brand Identity Workflow para Negócios Locais BR

### O que foi encontrado

- **Processo em 5 etapas validado para pequenos negócios BR:**

  1. **Posicionamento (30min):** Definir público-alvo + conceito da marca (vintage, moderno, local/artesanal) + frase de posicionamento de 1 linha
  2. **Conceito visual (1-2h):** Escolher 1 conceito principal e manter consistência. Para barbearia: clássico vintage, moderno minimalista, ou rooted no bairro. Para salão: premium, natural/orgânico, ou urbano jovem.
  3. **Sistema visual central:**
     - Logotipo: 1 símbolo + variação texto-only (2 versões no máximo)
     - Tipografia: 1 fonte principal + 1 secundária (não mais que 2)
     - Paleta: 2-3 cores base + 1 cor de acento (códigos HEX + CMYK)
  4. **Mini brand guide (1 página):** Uso do logo, paleta, tipografia, tom de voz em 3 adjetivos
  5. **Implementação rápida:** Fachada/sinalização, perfil social (foto capa + bio alinhada), cartão de visita

- **Recursos Figma para brand identity:**
  - `figma.com/community/file/912149013401287731` — Brand and Design System Kit V1.1 (free, usa Figma variables)
  - `figma.com/community/file/1230932286616490770` — Brand Guidelines (logo + tipografia + cor + ilustrações)
  - Brand Design Kit v6 (YouTube): setup de nova marca em minutos com Figma local variables — referência de processo acelerado

- **Combinações de identidade visual testadas por nicho:**

  | Nicho | Conceito | Paleta sugerida | Tipografia |
  |-------|----------|-----------------|------------|
  | Barbearia vintage | Tradição + masculino | Preto/creme/vermelho escuro | Serif leve + Display vintage |
  | Barbearia moderna | Clean + premium | Preto/cinza-chumbo/dourado | Sans-serif geométrica |
  | Salão premium | Elegância + feminino | Off-white/rose/preto | Serif clássica + script sutil |
  | Salão jovem/urbano | Vibrante + acessível | Coral/terracota/nude | Sans-serif arredondada |
  | Personal trainer | Performance + confiança | Preto/verde-oliva ou azul-escuro | Sans-serif bold |

- **Regra de ouro local BR:** Incluir elemento que evoque o bairro ou cultura local de forma sutil (um ponto de referência, cor da cidade, nome do bairro na assinatura visual) — cria pertencimento sem perder profissionalismo.

- **Sequência com skills do toolkit:**
  ```
  borghei/brand-strategist → posicionamento + only-we test
  erichowens/web-design-expert → direção visual + mood board + paleta OKLCH
  [Figma use_figma] → criação das variáveis de tokens no arquivo do cliente
  figma-create-design-system-rules → documenta o sistema para o projeto
  ```

---

## FRAMEWORKS/SOPs MAIS PRÁTICOS (resumo executivo)

### SOP 1 — Onboarding de novo cliente (do briefing ao Figma)
```
1. borghei/brand-strategist: briefing estratégico (30-60min)
   → Output: frase de posicionamento + público + diferencial
2. erichowens/web-design-expert: direção visual
   → Output: conceito + paleta OKLCH + tipografia + mood reference
3. Figma create_new_file + use_figma: criar arquivo do cliente
4. use_figma: criar Variables (cores, espaçamento, tipografia) no arquivo
5. Plugin Token Exporter: exportar para tailwind.config.js
6. figma-create-design-system-rules: gerar arquivo de regras do projeto
```

### SOP 2 — Design de LP (nicho local BR)
```
Estrutura canônica de seções:
Hero → Serviços+Preços → Galeria → Equipe → Depoimentos → Localização → FAQ → Rodapé

Componentes obrigatórios:
- Sticky WhatsApp CTA (bottom-right, pré-preenchido)
- Cards de serviço (foto + nome + preço + botão)
- Google Reviews widget (mínimo 3 depoimentos com foto)
- Google Maps embed
- Badge de avaliação (estrelas + número)

Regras CRO:
- CTA acima da dobra em TODOS os dispositivos
- Preço ou faixa visível
- Formulário: máx. 3 campos
- Sem carousel no hero
```

### SOP 3 — Handoff Figma → React/Tailwind
```
1. get_design_context: por seção (não por página inteira)
2. Verificar Code Connect mapeado antes de gerar novo código
3. Mapear Figma Component Properties → React props (tabela do Gap 3)
4. get_variable_defs: confirmar tokens usados na seção
5. vercel-labs/web-design-guidelines: auditoria pré-entrega
6. coreyhaines31/page-cro: revisão CRO final
```

---

## BENCHMARKS CONCRETOS ENCONTRADOS

| Métrica | Valor | Fonte |
|---------|-------|-------|
| Taxa de conversão média LP serviços locais BR | 2% a 6% | PontiDigital BR + múltiplas agências |
| Desktop converte mais que mobile | +8% | VenueLabs 2025 |
| Tempo de carregamento crítico | <3 segundos | Consenso BR 2025 |
| Campos em formulário (máx para não perder conversão) | 3-4 campos | Best practices validadas |
| Campos com maior impacto de saída do funil | >5 campos | Múltiplos estudos |
| Referência de benchmarks por setor (57M conversões) | Unbounce Benchmark Report | unbounce.com/conversion-benchmark-report/ |

---

## GAPS SEM COBERTURA BOA

### Gap parcialmente coberto: Benchmarks CRO específicos por nicho BR
A pesquisa encontrou dados gerais de conversão para serviços locais BR (2-6%), mas não encontrou dados separados por nicho (barbearia vs salão vs personal trainer). A variação pode ser significativa — personal trainer high-ticket provavelmente converte menos mas com ticket maior. **Recomendação:** a Triforce deveria começar a mensurar e acumular dados próprios desde o primeiro projeto.

### Gap não coberto: Plataformas de agendamento online BR
Não foi aprofundada a integração com plataformas de agendamento populares no BR (Trinks, SetMore, Booksy, Calendly traduzido). Essas integrações impactam diretamente o CTA e a conversão. **Recomendação:** pesquisa pontual futura para mapear qual plataforma de agenda funciona melhor por nicho e faixa de preço.

### Gap não coberto: Tráfego pago local BR (Meta Ads + Google Ads)
O contexto de conversão de LP muda dependendo da origem do tráfego (tráfego frio de Meta vs busca ativa no Google). LPs para tráfego de pesquisa local ("barbearia perto de mim") podem ter taxas de conversão bem diferentes. **Recomendação:** endereçar quando o time incluir especialista em tráfego/media buying.

---

## RECURSOS PRIORITÁRIOS PARA A CAMILA

### Links salvos para referência imediata
- `figmafy.com/figma-variables-to-code-tokens-to-tailwind-css-vars/` — pipeline completo tokens → Tailwind
- `figma.com/blog/the-shared-language-of-props/` — mapeamento props Figma → React
- `docs.tokens.studio/transform-tokens/style-dictionary` — Token Studio + Style Dictionary
- `component-driven.dev/articles/boolean-flags-in-figma` — boas práticas boolean props
- `unbounce.com/conversion-benchmark-report/` — benchmarks CRO por setor
- `pontidigital.com.br/blog/taxa-conversao-landing-page-benchmarks/` — benchmarks BR

### Plugins Figma para instalar
1. **Figma Token Exporter** — exporta variables para Tailwind/CSS/SASS
2. **Tokens to Tailwind CSS** — gera utility classes do local styles
3. **Tailwind Tokens** (tailwindtokens.com) — sync design system ↔ Tailwind

### Templates Figma para usar como base
1. `figma.com/community/file/1462650517969554341` — Small Business Landing Page (free)
2. `figma.com/community/file/1289433328810299968` — Landing Page UI Kit & Design System
3. `figma.com/community/file/912149013401287731` — Brand and Design System Kit V1.1
4. `figma.com/community/file/1230932286616490770` — Brand Guidelines

---

*Scan concluído em 2026-04-13 | Stage 3 completo | Próximo: onboarding da Camila*
