---
skill: curador-ia
doc: briefing-para-vitoria
version: "1.0"
---

# Briefing de Design para Vitória — Formato e Protocolo

## Por que esse documento existe

Rafael entrega conteúdo. Vitória entrega visual. O briefing de design é o único ponto de contato entre os dois — e precisa ser preciso o suficiente para que Vitória produza sem precisar perguntar nada.

Um briefing incompleto cria retrabalho, atraso no agendamento e inconsistência visual. Um briefing bem preenchido garante que Vitória entrega o batch em 48h sem vai e vem.

---

## Template de briefing — preenchimento obrigatório por pauta

```
BRIEFING DE DESIGN — [slug da pauta]
Data de entrega solicitada: [data]
Prioridade: [normal / urgente]

---

CONTEÚDO
Tema: [assunto em português, sem jargão]
Headline sugerida: [máx. 8 palavras — impacto direto, começa pelo problema ou dado]
Subtítulo (opcional): [complementa a headline — máx. 12 palavras]
Dados ou números de destaque: [se houver — ex: "4x mais barato", "98% de precisão"]

---

FORMATO
Tipo: [card único / carrossel / reels cover]
Número de slides (se carrossel): [N]
Estrutura dos slides (se carrossel):
  Slide 1 (cover): [o que vai na cover — headline + dado principal]
  Slide 2: [título do item + conteúdo resumido]
  Slide 3: [...]
  Último slide: [CTA + call para salvar/seguir]

---

VISUAL
Fundo preferencial: [escuro (preto) / claro (bege) / a critério da Vitória]
Elemento visual sugerido: [foto editorial? ícone? abstrato? a critério?]
Cor de destaque: [laranja para qual elemento — ex: "laranja no dado numérico"]
Referência de estilo (se houver): [URL ou descrição — opcional]

---

LEGENDA
Rascunho completo: [colar o rascunho de legenda pt-BR conforme training/legenda-instagram-br.md]
Gancho (primeira linha): [repetir isolado — é o que define o visual do cover]

---

OBSERVAÇÕES
[qualquer contexto adicional que ajude Vitória — ex: "esse tema tem muito texto técnico, priorizar hierarquia clara nos slides internos"]
```

---

## Regras de preenchimento

### Headline
- Máximo 8 palavras
- Começa pelo problema do ICP ou pelo dado concreto — nunca pelo nome da empresa/produto
- Teste: se a headline funciona sozinha num card escuro sem explicação adicional, está boa
- Exemplos bons: "Seu WhatsApp pode atender sozinho agora" / "IA que custa 4x menos foi lançada"
- Exemplos ruins: "Anthropic Claude 3.5 Haiku lançado" / "Novidade incrível no mundo da IA"

### Estrutura de carrossel
- Cover (slide 1) sempre escuro + headline + subtítulo
- Slides internos (2 a N-1) sempre claros (bege) + conteúdo numerado
- Último slide sempre com CTA: "Salva esse post" ou "Segue para mais"
- Rafael define o conteúdo de cada slide — Vitória define o visual

### Dado ou número de destaque
- Se a notícia tem um número forte, ele vai em laranja no visual
- Rafael indica qual número merece destaque — Vitória decide a composição
- Se não há número, indicar "sem destaque numérico"

### Fundo preferencial
- Rafael sugere, Vitória decide
- Regra geral: notícia de impacto → fundo escuro. Ferramenta prática → pode ser claro
- Em caso de dúvida: "a critério da Vitória" é resposta válida

---

## Protocolo de entrega

### Onde entregar
- Notion: database "Pauta Curadoria IA", campo "Briefing de Design"
- Status da pauta deve mudar para `em produção` no momento da entrega

### Prazo
- Briefing entregue até 12h do dia de produção (conforme rotina de `garimpagem-diaria.md`)
- Vitória tem 48h para entregar o visual a partir do recebimento do briefing
- Para posts urgentes (notícia quente do dia): briefing entregue até 13h, Vitória tem 6h para cover + 1 slide

### Comunicação de urgência
Se a pauta for urgente (notícia quente que precisa sair no mesmo dia), Rafael sinaliza no briefing:

```
Prioridade: URGENTE
Motivo: [ex: "lançamento do GPT-5 hoje — janela de 24h para ser relevante"]
```

E notifica Larissa diretamente sobre a urgência — não espera ela encontrar no Notion.

---

## O que Rafael NÃO decide no briefing

- Composição exata dos elementos visuais (posição, tamanho, espaçamento)
- Escolha de imagem ou geração de imagem editorial
- Tipografia específica
- Versão final da headline (Rafael sugere, Vitória pode melhorar)
- Ordem visual dentro de um slide

Vitória tem autonomia total sobre as decisões visuais. O briefing é insumo, não instrução de design.

---

## Exemplos de briefing preenchido

### Exemplo 1 — Carrossel sobre ferramenta de WhatsApp

```
BRIEFING DE DESIGN — whatsapp-ia-atendimento
Data de entrega solicitada: 2026-04-18
Prioridade: normal

CONTEÚDO
Tema: Ferramenta de IA que automatiza atendimento no WhatsApp para pequenos negócios
Headline sugerida: Seu WhatsApp pode atender sozinho agora
Subtítulo: Sem contratar atendente. Sem custo de agência.
Dados ou números de destaque: (nenhum número forte nessa pauta)

FORMATO
Tipo: carrossel
Número de slides: 5
Estrutura dos slides:
  Slide 1 (cover): Headline + subtítulo
  Slide 2: O que a ferramenta faz (responde dúvidas, confirma horário, manda lembrete)
  Slide 3: Para quem funciona melhor (barbearia, salão, personal trainer)
  Slide 4: O que ainda não faz (limitações honestas)
  Slide 5: CTA — "Salva esse post. Explico como configurar nos próximos."

VISUAL
Fundo preferencial: escuro no cover, claro nos internos
Elemento visual sugerido: ícone de WhatsApp ou mensagem de chat — a critério
Cor de destaque: laranja no título de cada slide interno

LEGENDA
Rascunho completo:
WhatsApp com IA respondendo cliente? Já tem solução funcionando pra pequenos negócios.

Não é chatbot engessado de 2019. É assistente que responde dúvida, confirma horário e manda lembrete — tudo automatizado, tudo no número que o cliente já tem.

Na prática: barbearia ou salão que não consegue atender pelo WhatsApp em horário de pico pode resolver isso sem contratar atendente.

Você já testou algum bot de atendimento? Funcionou ou foi mais problema?

Gancho (primeira linha): WhatsApp com IA respondendo cliente? Já tem solução funcionando pra pequenos negócios.

OBSERVAÇÕES
Conteúdo prático e direto. Público é dono de barbearia/salão. Priorizar clareza nos slides internos — não sobrecarregar com texto técnico.
```

---

### Exemplo 2 — Card único sobre lançamento de modelo

```
BRIEFING DE DESIGN — claude-haiku-mais-barato
Data de entrega solicitada: 2026-04-19
Prioridade: normal

CONTEÚDO
Tema: Anthropic lançou versão mais barata do Claude — custo 4x menor por uso
Headline sugerida: IA profissional por 4x menos. Acabou de lançar.
Subtítulo: (a critério da Vitória)
Dados ou números de destaque: "4x mais barato" — destaque em laranja

FORMATO
Tipo: card único
Número de slides: 1

VISUAL
Fundo preferencial: escuro
Elemento visual sugerido: tipografia forte + dado em destaque — sem imagem editorial obrigatória
Cor de destaque: laranja no "4x"

LEGENDA
Rascunho completo:
A Anthropic lançou uma versão do Claude que custa 4x menos por mensagem.

Isso não é só notícia técnica. Significa que ferramentas que você já paga ficam mais baratas pra rodar — ou que quem ainda não usa vai ter menos desculpa.

Na prática: chatbots de atendimento, geradores de conteúdo e automações que usam Claude vão ficar mais acessíveis pra pequenos negócios.

Você já usa alguma ferramenta de IA no seu negócio ou ainda tá no modo manual?

Gancho (primeira linha): A Anthropic lançou uma versão do Claude que custa 4x menos por mensagem.

OBSERVAÇÕES
O dado "4x" é o coração desse post. Tudo gira em torno dele visualmente.
```
