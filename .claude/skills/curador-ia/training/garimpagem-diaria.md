---
skill: curador-ia
doc: garimpagem-diaria
version: "1.0"
---

# Garimpagem Diária — Setup e Rotina

## Feedly — Configuração de Feeds

### Categoria: Labs & Research
- blog.anthropic.com
- openai.com/blog
- deepmind.google/discover/blog
- ai.meta.com/blog
- mistral.ai/news
- huggingface.co/blog
- research.google/blog

### Categoria: Tech & Product
- techcrunch.com (tag: artificial-intelligence)
- theverge.com (tag: ai)
- arstechnica.com (tag: ai)
- venturebeat.com/category/ai
- wired.com/tag/artificial-intelligence
- technologyreview.com

### Categoria: Papers & Academic
- arxiv.org/list/cs.AI/recent
- paperswithcode.com/latest
- alphaxiv.org (papers com destaque)

### Categoria: Brasil & PT
- tecnoblog.com.br
- canaltech.com.br
- olhardigital.com.br
- startups.com.br

### Categoria: Criadores & Comunidade
- simonwillison.net (análises técnicas acessíveis)
- interconnects.ai
- newsletter.theaiedge.io
- bair.berkeley.edu/blog

## Newsletters Essenciais de IA para Seguir

| Newsletter | Foco | Frequência |
|---|---|---|
| The Batch (deeplearning.ai) | Geral, bem curado, Andrew Ng | Semanal |
| Import AI (Jack Clark) | Research + política | Semanal |
| The Rundown AI | Notícias diárias, formato rápido | Diária |
| Ben's Bites | Produtos e ferramentas | Diária |
| TLDR AI | Resumos técnicos | Diária |
| Ahead of AI (Sebastian Raschka) | Papers acessíveis | Quinzenal |
| AI Breakfast | Geral, bom para iniciantes | Diária |
| Lenny's Newsletter | Produto + IA aplicada | Semanal |

Todas recebem em endereço de e-mail dedicado para curadoria — não misturar com e-mail pessoal.

## Perplexity — Queries de Monitoramento

Rodar diariamente no início do bloco de pesquisa. Sempre em inglês.

### Queries de varredura geral
```
AI news today [data atual]
artificial intelligence announcements this week
new AI model released this week
AI product launch [mês atual]
```

### Queries por tema estratégico
```
AI tools for small business owners 2026
AI automation for service businesses
ChatGPT updates this week
Claude Anthropic updates this week
Gemini Google updates this week
AI image generation new model
AI video generation news
open source AI model released
AI regulation news this week
```

### Queries de checagem
```
"[nome do produto/modelo]" announcement official
"[claim específico]" source evidence
[empresa] official blog announcement [assunto]
```

### Queries para ângulo de público
```
AI tools for barbershop owner
AI tools for personal trainer
AI tools for freelancer Brazil
AI small business automation use cases
```

## Estrutura do Painel no Notion

### Database: Pauta Curadoria IA

**Campos obrigatórios:**
- Título (pt-BR, já adaptado)
- Fonte primária (URL)
- Fonte secundária (URL, mínimo 1)
- Data da notícia
- Status: `garimpo` / `filtro` / `aprovado` / `em produção` / `publicado` / `descartado`
- Formato: `card único` / `carrossel` / `reel cover`
- Nível 1 (o que aconteceu — 1 frase)
- Nível 2 (por que importa — 2-3 frases)
- Nível 3 (o que observar — 1-2 frases)
- Rascunho de legenda
- Responsável design: Vitória
- Responsável agendamento: Larissa
- Data publicação planejada

**Views úteis:**
- Por status (kanban)
- Por data de publicação (calendário)
- Descartados (log de ruído — util para padrão de reconhecimento)

## Rotina Diária — Hora a Hora

### 07h00 — Abertura do bloco de pesquisa
- Abrir Feedly. Varrer categorias na ordem: Labs > Tech > Brasil > Criadores
- Marcar com estrela tudo que passa no critério de "pode ser notícia real"
- Tempo máximo: 45 min

### 07h45 — Perplexity queries
- Rodar as queries de varredura geral
- Rodar 3-4 queries temáticas do dia (variar temas ao longo da semana)
- Anotar no Notion todos os candidatos com status `garimpo`
- Tempo máximo: 30 min

### 08h15 — Triagem (filtro editorial das 4 perguntas)
- Para cada item em `garimpo`, aplicar as 4 perguntas
- Mover para `aprovado` ou `descartado`
- Meta: 2-3 notícias aprovadas por dia
- Tempo máximo: 30 min

### 08h45 — Planejamento do dia
- Confirmar 2 pautas prioritárias para o dia
- Verificar se há pauta do dia anterior que ficou em `aguardando confirmação`
- Alinhar com Larissa se tiver alguma pauta urgente ou oportunista (trend do momento)

### 09h00 — Bloco de escrita
- Escrever os 3 níveis para cada pauta aprovada
- Rascunhar legenda completa seguindo estrutura pt-BR
- Preencher briefing de design (sugestão de visual, paleta, destaque de texto)
- Tempo: ~1h30

### 10h30 — Revisão e checagem de fatos
- Checar cada claim do rascunho contra a fonte primária
- Aplicar checklist do protocolo anti-hype
- Ajustar linguagem se necessário
- Tempo: ~30 min

### 11h00 — Entrega
- Mover pautas para status `em produção`
- Enviar briefing para Vitória (design) via Notion
- Enviar resumo do dia para Larissa (datas, formatos, urgências)
- Tempo: ~30 min

### 11h30 — Encerra bloco de produção diária

**Nota:** Fora do bloco de pesquisa, o Rafael não fica monitorando feeds em tempo real. Se surgir uma notícia urgente no meio do dia, Larissa ou o fundador acionam diretamente.
