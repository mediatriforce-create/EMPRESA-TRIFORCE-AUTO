# Scan Estratégico — Conhecimento por Gap
**Data:** 2026-04-13
**Responsável:** Gabriela (RH) — pesquisa para contratação Copywriter Senior (Fecchio)
**Contexto:** Triforce Auto — agência digital, LPs para pequenos negócios presenciais + empreendedores digitais, pré-receita (zero vendas)

---

## GAP 1 — Copy para Negócio Presencial Local (BR)

### Diferenças fundamentais vs. infoproduto

| Dimensão | Negócio Presencial Local | Infoproduto |
|----------|--------------------------|-------------|
| Objetivo de conversão | Agendamento / visita / ligação imediata | Venda online, upsell digital |
| Prova social | Depoimentos locais + fotos reais de clientes do bairro | Resultados em números, estudos de caso digitais |
| Entrega prometida | Experiência física + serviço presencial | Acesso a conteúdo digital, garantia de entrega imediata |
| Estrutura de LP | Simples: localização + horários + serviços + CTA de agendamento | Complexa: problema + solução + bônus + garantia + urgência + CTA |
| Tom | Humano, local, próximo | Educativo/autoridade, gatilhos de curiosidade, prova de resultados |
| Urgência | "Vagas limitadas hoje", horários de pico | Bônus expirando, turmas fechadas, lançamentos |
| SEO | Cidade/bairro/ponto de referência nos textos | Keywords de nicho + termos de pesquisa de produto |

### Elementos que funcionam para presenciais BR

- **Headline com benefício + tempo + local:** "Barba alinhada em 20 minutos no coração do [Bairro]"
- **Benefícios sobre features:** o que o cliente ganha (tempo, aparência, conforto) > lista de serviços
- **Autoridade local:** mencionar bairro, rua, referência geográfica — cria identidade territorial
- **CTA de baixo atrito:** "Agende no WhatsApp", "Reserve seu horário", "Passe na loja hoje" — sem fricção
- **Tom por segmento:**
  - Barbearia: masculino, moderno, confiante, direto
  - Salão feminino: acolhedor, inclusivo, transformador
  - Personal trainer: motivacional, resultado-orientado, próximo
- **Gatilhos simples:** inauguração, horário estendido, desconto 1a visita, fidelidade
- **Microdados locais:** ponto de referência, horário de pico da região, facilidade de acesso/estacionamento

### Estrutura de LP mínima para presencial

```
1. Headline (benefício + local)
2. Subtítulo (o que é, quem é para)
3. 3 bullets de benefício
4. Prova social (foto real + 1 linha de depoimento)
5. Oferta de entrada (desconto 1a visita ou combo)
6. CTA principal (WhatsApp / agendamento)
7. Localização + horários
8. CTA secundário (Google Maps)
```

### Diferença crítica de copy vs. infoproduto
Infoproduto vende **transformação futura** — o copy trabalha desejo, dor, mecanismo único.
Presencial vende **conveniência + experiência presente** — o copy trabalha proximidade, confiança e facilidade de acesso. Sem longos loops de objeção. Sem VSL. Direto ao "agende agora".

---

## GAP 2 — Microcopy Web

### Princípios fundamentais (UX Writing)

- **Clareza > criatividade** — o usuário não deve parar para pensar
- **Brevidade com propósito** — cortar até o ponto em que cortar mais perde significado
- **Linguagem do usuário** — zero jargão técnico
- **Consistência** — mesma ação = mesmas palavras em todo o sistema
- **Voice constante + tone adaptável** — personalidade fixa, tom muda por contexto

### Por tipo de elemento

#### Botões / CTAs
- Estrutura: **verbo de ação + resultado específico**
- Aprovado: "Salvar alterações", "Agendar agora", "Ver disponibilidade", "Enviar mensagem"
- Reprovado: "OK", "Enviar", "Clique aqui", "Saiba mais" (sem contexto)
- Primeiro person converte mais: "Quero meu desconto" > "Obter desconto"
- Pares claros: Salvar / Cancelar — Excluir / Manter — Enviar / Salvar rascunho

#### Labels de formulário
- Sempre visíveis (não usar placeholder como substituto de label)
- Sentence case: "Nome completo" > "NOME COMPLETO"
- Concisas: "E-mail" > "Digite seu endereço de e-mail aqui"
- Obrigatório indicado discretamente: asterisco + legenda

#### Placeholders
- Papel: suporte/exemplo, nunca substituto de label
- Aprovado: "ex: joao@gmail.com" — mostra formato esperado
- Reprovado: "Digite seu e-mail" — duplica a label, some ao clicar

#### Mensagens de erro
- Estrutura 3 partes: **o que aconteceu + por que + como corrigir**
- Aprovado: "E-mail inválido. Verifique se digitou corretamente, como nome@exemplo.com"
- Reprovado: "Erro de validação", "Campo inválido", "Tente novamente"
- Tom: nunca culpar o usuário — "Não foi possível..." > "Você errou..."

#### Empty States
- 3 componentes: o que pertence aqui + por que está vazio + call to action
- Aprovado: "Seus agendamentos aparecerão aqui. Marque seu primeiro horário."
- Reprovado: "Nenhum item encontrado"

#### Onboarding
- Mostrar valor antes de pedir esforço
- Progresso explícito: "Etapa 2 de 4 — quase lá"
- Encorajamento progressivo — micro-celebrações em cada etapa

#### Success states
- Confirmar o que aconteceu + o que acontece agora
- Aprovado: "Agendamento confirmado! Você receberá uma confirmação por WhatsApp."
- Reprovado: "Sucesso!"

### Framework de revisão de microcopy
1. **Voice Check** — tom consistente com a marca?
2. **Issues** — quais elementos têm problemas?
3. **Patterns** — erros recorrentes que indicam problema sistêmico?
4. **Quick Wins** — mudanças de 5 minutos com alto impacto?

### Testes de validação de microcopy
- **Readback test** — leia em voz alta; se soar estranho, reescreva
- **Screenshot test** — sem contexto, a mensagem é clara?
- **Stress test** — e se o texto tiver o dobro do tamanho?
- **Translation test** — funciona em outro idioma? (indica se é muito idiomático)
- **Truncation test** — como fica cortado em mobile?

---

## GAP 3 — Formato de Entrega para Dev/Designer

### Formato recomendado para contexto Triforce Auto (React/TS + Figma)

#### Estrutura do documento de copy (markdown)

```markdown
# [Nome do Projeto] — Copy Doc
Versão: X.X | Data: YYYY-MM-DD | Responsável: [Copywriter]

## Tela/Componente: [Nome]

### Copy Principal
- **Headline:** [texto]
- **Subheadline:** [texto]
- **CTA Primário:** [texto do botão]
- **CTA Secundário:** [texto]

### Microcopy
| Elemento | Copy | Variante/Estado | Limite |
|----------|------|-----------------|--------|
| Input label | Nome completo | — | — |
| Placeholder | ex: João Silva | — | — |
| Erro | Nome obrigatório. Digite seu nome completo. | error | 80 chars |
| CTA | Agendar agora | default | 20 chars |
| CTA | Aguarde... | loading | — |

### Notas de implementação (para Felipe/Dev)
- Chave i18n sugerida: `home.hero.title`
- aria-label obrigatório no botão de agendamento
- Erro aparece inline sob o campo, não em toast

### Notas de design (para Camila/Designer)
- CTA primary: máximo 24 chars para não quebrar em mobile 375px
- Empty state: ícone + headline + CTA (ver exemplo na seção X)
```

#### Convenções de nomenclatura de componentes
- Padrão: `[Tipo][Funcionalidade][Estado]`
- Exemplos: `ButtonCTA`, `ButtonCTALoading`, `InputEmail`, `CardServiço`, `BadgePromo`
- Variantes de copy: `copy.home.hero.title` / `copy.home.cta.label`

#### Boas práticas de handoff
- Uma seção por tela/componente — não misturar telas no mesmo bloco
- Indicar limite de caracteres para elementos críticos (botões, headlines mobile)
- Sinalizar condicionais: "se usuário já agendou antes → copy alternativa"
- Entregar em Markdown (legível no GitHub, Notion, VSCode e Figma comments)
- Sempre incluir: copy padrão + copy de estado vazio + copy de erro + copy de sucesso

#### Ferramentas de handoff no stack Triforce Auto
- **Figma Dev Mode** — anotações de copy direto no componente (Camila anota, Felipe consome)
- **Arquivo Markdown no repo** — `/src/copy/[tela].md` versionado com o código
- **Strings file opcional** — `/src/i18n/pt-BR.json` com chaves para copy reutilizável

---

## GAP 4 — Copy Sem Prova Social (Pré-Receita)

### Problema central
Triforce Auto está em pré-receita. Zero clientes, zero depoimentos, zero resultados anteriores para mostrar. Copy precisa converter mesmo assim.

### Estratégias validadas

#### 1. Prova social alternativa (sem depoimentos reais)
- **Prova do método:** descrever as etapas do processo em detalhe — clareza sobre o processo funciona como confiança
- **Prova de competência:** mostrar amostras do trabalho (mockups, demos, protótipos de LP)
- **Credenciais indiretas:** referências a frameworks reconhecidos, ferramentas usadas, benchmarks do setor
- **Documentação da jornada:** "estamos construindo ao vivo" — transparência estratégica como diferencial

#### 2. Trust signals sem depoimentos
- **Garantia clara:** "Reembolso integral se não gostar do resultado após 7 dias" — elimina risco percebido
- **Processo transparente:** mostrar cada etapa (briefing → design → copy → aprovação → entrega) — tangibiliza o intangível
- **Especificidade do entregável:** "Você recebe: 1 LP em React, copy completa, Figma entregável, 30 dias de suporte" — detalhe cria credibilidade
- **Prazo concreto:** "Entrega em 7 dias úteis" > "Entrega rápida"

#### 3. Estrutura de copy pré-receita

```
Headline: [Transformação específica] para [avatar] — sem precisar de [objeção comum]
Subtítulo: [O que você entrega hoje, concreto]
Método: 3-5 passos nomeados do seu processo
CTA de baixo risco: "Diagnóstico gratuito de 20 min" > "Compre agora"
Garantia: texto visível, próximo ao CTA
```

#### 4. Linguagem de "pioneiro"
- "Vagas abertas para clientes fundadores — preço especial para os primeiros 5"
- "Estamos em beta — ajude a moldar o produto e pague menos"
- Transforma ausência de histórico em vantagem (preço, atenção, co-criação)

#### 5. Quando conseguir o primeiro depoimento
- Perguntas estruturadas para extrair depoimento útil:
  1. "Qual era sua situação antes?"
  2. "O que mudou depois da LP?"
  3. "O que você diria para alguém considerando contratar?"
- Resultado: depoimento com estrutura Antes/Depois/Recomendação — máxima conversão

#### Armadilhas a evitar
- Nunca inventar ou exagerar resultados — perda imediata de credibilidade
- Nunca usar depoimentos genéricos sem atribuição ("Cliente satisfeito")
- Não tentar copiar estrutura de infoproduto com prova social pesada — a ausência fica óbvia

---

## GAP 5 — SEO Copy Local

### Elementos de copy com impacto em SEO local

#### Title tag (meta title)
- Fórmula: `[Serviço Principal] em [Cidade/Bairro] | [Nome do Negócio]`
- Exemplos:
  - "Barbearia em Pinheiros, SP | Barber King"
  - "Personal Trainer no Centro de Curitiba | João Fitness"
- Limite: 50-60 caracteres
- Incluir: palavra-chave primária + localização + nome da marca

#### Meta description
- Fórmula: `[Benefício principal] + [localização] + [diferencial] + [CTA]`
- Exemplo: "Cortes masculinos e barba no coração de Pinheiros. Atendimento sem fila, agenda online. Agende pelo WhatsApp."
- Limite: 150-160 caracteres
- Incluir: palavra-chave, localização, um diferencial, uma ação

#### H1 da página
- Uma única ocorrência, clara, com palavra-chave + localização
- Exemplo: "A melhor barbearia no Centro de [Cidade]"

#### Corpo do texto (copy natural com SEO)
- Mencionar cidade/bairro de forma natural (não forçada) no mínimo 2-3 vezes
- Incluir pontos de referência locais: "perto do metrô X", "a 200m do [ponto famoso]"
- Mencionar serviços específicos com localização: "corte masculino em [bairro]", "depilação a laser no [bairro]"
- Evitar keyword stuffing — Google penaliza, copy fica robótica

#### Google Meu Negócio (GMB) — copy do perfil
- Descrição do negócio: 750 caracteres — usar os primeiros 250 como gancho (aparecem sem clicar em "mais")
- Incluir: o que faz + localização + diferencial + horários + CTA de contato
- Serviços: nomear cada serviço exatamente como o cliente pesquisa (não usar nomes internos)
- Posts GMB: copy curta (150-300 chars), imagem + CTA de agendamento

#### Estratégia de palavras-chave para LP local
- Primária: `[serviço] + [cidade]` — "barbearia São Paulo"
- Secundária: `[serviço] + [bairro]` — "barbearia Vila Madalena"
- Long tail: `melhor [serviço] + [bairro]` — "melhor corte masculino Vila Olímpia"
- Near me: Google interpreta automaticamente — não precisa de cópia literal "perto de mim"

#### Schema Markup (sinalizar para Felipe/Dev)
- `LocalBusiness` schema — nome, endereço, telefone, horário, avaliações
- `Service` schema — para cada serviço oferecido
- Gerado pelo dev, mas copy do Copywriter deve alimentar os campos de texto do schema

---

## Síntese dos Gaps — Cobertura Final

| Gap | Cobertura | Fonte |
|-----|-----------|-------|
| GAP 1 — Copy presencial local BR | COBERTO | Pesquisa estratégica (scan-estrategico.md) |
| GAP 2 — Microcopy web | COBERTO | Skill `ux-writing` (petekp) + pesquisa |
| GAP 3 — Handoff dev/designer | COBERTO | Pesquisa + template (scan-estrategico.md) |
| GAP 4 — Copy sem prova social | COBERTO | Pesquisa estratégica (scan-estrategico.md) |
| GAP 5 — SEO copy local | COBERTO | Pesquisa estratégica (scan-estrategico.md) |

### Gaps residuais (não resolvidos por skills ou pesquisa)
- **Copy em português BR com nuances regionais** — nenhuma skill em PT-BR encontrada. O copywriter (Fecchio) precisa ter esse conhecimento como competência nativa.
- **Copy para personal trainer com prova de método** — específico demais para skill genérica. Requer briefing aprofundado por segmento.
