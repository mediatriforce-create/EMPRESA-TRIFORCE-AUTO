# Frameworks Estratégicos de Design
**Versão:** 2026-04-13 | Fontes: scan-estrategico.md + validacao-estrategica.md

---

## 1. Brand Identity — 5 Etapas para Negócios Locais BR

### Etapa 1 — Posicionamento (30min)
**Objetivo:** Clareza sobre quem é o cliente e para quem ele serve.

Checklist:
- [ ] Público-alvo definido (idade, gênero, bairro, poder aquisitivo)
- [ ] Conceito da marca escolhido (vintage, moderno, local/artesanal, premium)
- [ ] Frase de posicionamento de 1 linha: "[Quem] + [o que oferece] + [para quem] + [diferencial]"
- [ ] Teste "only-we": o que só este negócio pode afirmar?

### Etapa 2 — Conceito Visual (1–2h)
**Objetivo:** Uma direção, não três opções.

Checklist:
- [ ] 1 conceito principal escolhido e mantido com consistência
- [ ] Referências visuais extraídas via `image-analysis` (paleta, estilo, atmosfera)
- [ ] Resposta à pergunta: "se a marca fosse uma pessoa, como se vestiria?"
- [ ] Paleta em OKLCH para uniformidade perceptual e WCAG automático

### Etapa 3 — Sistema Visual Central
**Objetivo:** Entregar os elementos que o Felipe vai implementar.

Checklist:
- [ ] Logotipo: símbolo + variação texto-only (máx 2 versões)
- [ ] Tipografia: 1 fonte principal + 1 secundária (não mais que 2)
- [ ] Paleta: 2–3 cores base + 1 cor de acento (HEX + OKLCH)
- [ ] Variáveis criadas no Figma (Colors, Typography, Spacing)
- [ ] Token Exporter: exportar para `tailwind.config.js`

### Etapa 4 — Mini Brand Guide (1 página)
**Objetivo:** Documento que o cliente pode guardar e que o Felipe usa de referência.

Checklist:
- [ ] Uso correto do logo (versões, espaçamento mínimo, fundos permitidos)
- [ ] Paleta com nome de cada cor e valores HEX
- [ ] Tipografia: fontes + hierarquia (H1, H2, body, caption)
- [ ] Tom de voz em 3 adjetivos (ex: "próximo, direto, confiável")

### Etapa 5 — Implementação
Checklist:
- [ ] Assets exportados (logo SVG + PNG transparente)
- [ ] `DESIGN_SYSTEM.md` entregue ao Felipe com tokens documentados
- [ ] Perfil social alinhado (foto capa no formato correto)

---

## 2. Kit LP Nicho Local BR — 8 Seções com Especificações

### Seção 1 — Hero
**Objetivo:** Capturar atenção e gerar CTA imediato.
- Headline com nome do bairro/cidade (SEO local + conexão emocional)
- CTA WhatsApp obrigatório acima da dobra (mobile 375px + desktop)
- Badge de avaliação Google (estrelas + número de avaliações)
- Foto real do espaço ou do serviço sendo executado (não stock photo)
- Sem carousel/slider — hero estático converte mais

### Seção 2 — Serviços + Preço
**Objetivo:** Mostrar o que o negócio oferece e quanto custa (reduzir objeção de barreira financeira).
- Cards: imagem + nome do serviço + preço (ou faixa) + botão CTA
- Preço visível — ausência de preço gera insegurança e abandono
- CTA individual por card (WhatsApp pré-preenchido com o serviço)

### Seção 3 — Galeria / Portfólio
**Objetivo:** Prova visual do trabalho.
- Barbearia: fotos de cortes realizados (antes/depois)
- Salão: transformações reais
- Personal trainer: fotos de treinos e evolução de alunos
- Grid ou carrossel com lightbox
- Todas as imagens com dimensões explícitas (width + height)

### Seção 4 — Equipe
**Objetivo:** Humanizar o negócio.
- Fotos reais (não ilustrações)
- Nome + especialidade + tempo de experiência
- Para barbearia solo: o dono em destaque com sua história

### Seção 5 — Depoimentos
**Objetivo:** Prova social local — o gatilho mais forte para negócios locais BR.
- Nome completo + **cidade/bairro** + foto do cliente
- Google Reviews integrado (badge com número de avaliações)
- Mínimo 3 depoimentos
- Preferir depoimentos que mencionem resultado específico + localização

### Seção 6 — Mapa + Horários
**Objetivo:** Facilitar o acesso — obrigatório para negócios com atendimento presencial.
- Google Maps embed com marcação da localização
- Endereço completo com bairro
- Horários com destaque para diferencial (noturno, fim de semana)
- Para personal trainer com atendimento domiciliar: opcional

### Seção 7 — FAQ
**Objetivo:** Responder objeções antes que o visitante abandone.
- 4–6 perguntas mais comuns do nicho
- Incluir: formas de pagamento, cancelamento, tempo de atendimento
- Para barbearia: aceita sem agendamento? Tem estacionamento?

### Seção 8 — Rodapé
**Objetivo:** Contato completo e CTA final.
- CTA WhatsApp de reforço
- Endereço + horários (repetição intencional)
- Links para redes sociais
- Política de privacidade (obrigatório para LGPD)

---

## 3. Gatilhos Locais BR — Exemplos de Referência

> Estes são exemplos estruturais. Copy real é responsabilidade do copywriter.

| Gatilho | Estrutura | Exemplo de referência |
|---------|-----------|----------------------|
| Bairro no headline | "[Serviço] no [Bairro]" | "Barbearia no Itaim Bibi" |
| WhatsApp pré-preenchido | `wa.me/55[ddd][número]?text=Quero+agendar:+[serviço]` | Botão "Agendar corte agora" |
| Depoimento local | "Nome, [Bairro]" | "João Silva, Pinheiros" |
| Horário diferencial | "[Dia/período] disponível" | "Atende sábado até 20h" |
| Badge Google | "X estrelas | Y avaliações no Google" | Widget de avaliação com link |

---

## 4. CRO Visual — Frameworks de Decisão

### Posicionamento de CTA (hierarquia validada)
1. **Acima da dobra, mobile** — CTA principal no hero (WhatsApp)
2. **Após prova social** — CTA secundário após depoimentos
3. **Sticky (bottom mobile)** — botão flutuante sempre visível no scroll
4. **CTA final** — no rodapé como reforço

### Hierarquia de atenção visual
```
Hero (problema + solução + CTA) →
Serviços com preço →
Prova social (fotos reais + avaliações) →
Equipe (humaniza) →
Localização + horários →
CTA final + rodapé
```

### O que FUNCIONA (validado para negócios locais BR)
- Botão WhatsApp com pré-preenchimento de serviço (menor atrito)
- Formulário ≤ 4 campos (nome + telefone + serviço + mensagem opcional)
- Prova social local: Google Reviews com foto + nome + bairro
- Before/after real (barbearia, salão, personal)
- Preço visível ou faixa explícita
- Horários diferenciados no hero
- Sticky CTA acompanhando o scroll

### O que NÃO FUNCIONA
- Formulário com mais de 5 campos (queda abrupta de conversão)
- Hero com carousel/slider automático
- Ausência de preço ou indicativo de valor
- Sem endereço/mapa visível para negócio presencial
- Copy genérico sem prova ("melhor atendimento da cidade")
- Site lento (>3s no mobile)

### Benchmarks de conversão (2025)
| Contexto | Taxa estimada |
|----------|--------------|
| LP genérica de serviços locais (tráfego pago) | 2–6% |
| LP com WhatsApp CTA + prova social local | 4–8% |
| Desktop vs mobile | Desktop converte +8% |
| Formulário >5 campos | < 2% |

---

## 5. Combinações Visuais por Nicho

| Nicho | Conceito | Paleta sugerida | Tipografia |
|-------|---------|----------------|-----------|
| Barbearia vintage | Tradição + masculino + artesanal | Preto / creme / vermelho escuro | Serif leve + Display vintage |
| Barbearia moderna | Clean + premium + urbano | Preto / cinza-chumbo / dourado | Sans-serif geométrica bold |
| Salão premium | Elegância + feminino + sofisticado | Off-white / rose / preto | Serif clássica + script sutil |
| Salão jovem/urbano | Vibrante + acessível + alegre | Coral / terracota / nude | Sans-serif arredondada |
| Personal trainer | Performance + confiança + resultado | Preto / verde-oliva ou azul-escuro | Sans-serif bold condensada |

**Regra de ouro local BR:** Incluir elemento que evoque o bairro ou cultura local de forma sutil — cria pertencimento sem perder profissionalismo.

---

## 6. Anti-AI Checklist — 5 Perguntas

Rodar após cada seção finalizada. Se qualquer resposta for SIM, refazer com decisão visual ousada.

1. **Esta paleta poderia pertencer a qualquer empresa do mesmo nicho?**
   → SIM: trocar pelo menos 1 cor por algo mais específico ao posicionamento do cliente

2. **A tipografia escolhida é a primeira opção "óbvia" para este estilo?**
   → SIM: explorar 3 alternativas menos óbvias antes de decidir

3. **O layout segue o grid de 12 colunas sem nenhuma quebra intencional?**
   → SIM: introduzir pelo menos 1 elemento que rompa a grade em alguma seção

4. **Alguma seção tem exatamente a mesma proporção visual que a anterior?**
   → SIM: variar ritmo (compacto ↔ generoso, escuro ↔ claro, cheio ↔ vazio)

5. **Se eu tirar o logo, este design poderia ser de um concorrente?**
   → SIM: a identidade visual não está diferenciada — voltar à Etapa 2 do brand identity

---

## 7. Figma Component Properties → React Props — Tabela Completa

| Tipo Figma | Equivalente React | Exemplo Figma | Exemplo React |
|------------|------------------|--------------|--------------|
| **Variant** | `enum` / union type | Variant "Size": SM, MD, LG | `size: 'sm' \| 'md' \| 'lg'` |
| **Variant (estado)** | `enum` obrigatório | Variant "State": Default, Hover, Active, Disabled | `state: 'default' \| 'hover' \| 'active' \| 'disabled'` |
| **Boolean** | `boolean` prop | Boolean "hasIcon" | `icon?: ReactNode` (opcional) |
| **Text** | `string` prop | Text "Label" | `children: string` |
| **Instance Swap** | `ReactNode` / componente | Instance Swap "Icon" | `icon: React.ComponentType` |

**Regra:** Preferir Variants sobre Booleans para estados (hover, active, disabled) — gera código mais limpo e é como o Felipe vai implementar.

**Com Code Connect (Organization+):**
```js
figma.connect(Button, 'https://figma.com/...', {
  props: {
    variant: figma.enum('Type', { primary: 'primary', secondary: 'secondary' }),
    disabled: figma.boolean('Disabled'),
    children: figma.string('Label')
  }
})
```

**Sem Code Connect (Professional — workaround):**
Documentar na tabela de mapeamento do `DESIGN_SYSTEM.md`.
