# Etapa 2 — Deep Dive: Skills do Orquestrador (Triforce Auto)

> Diretor / Orquestrador de Equipe — foco em avaliacao de especialistas, roteamento, handoffs e calibracao estrategica.
> Gerado em: 2026-04-20

---

## 1. Roteamento de Tarefas

### O que e essa skill

Classificar cada pedido que chega do fundador (ou surge internamente) e direcionar ao especialista certo, na hora certa, com o contexto certo. E a porta de entrada de toda a cadeia operacional.

### Por que e critica para o Orquestrador da Triforce Auto

Todo pedido do fundador passa por aqui antes de qualquer execucao. Um roteamento errado gera retrabalho duplo: o especialista errado perde tempo tentando executar algo fora do seu dominio, e o especialista certo recebe tarde, sem contexto.

### Perplexity Research Brief

**Projeto:** Triforce Auto — agencia digital pre-receita, 8 especialistas, canal de aquisicao outbound (Instagram DM / WhatsApp), stack React/TS + Supabase + Vercel. O Orquestrador precisa de um sistema de classificacao de pedidos para rotear tarefas aos especialistas corretos (Caio/prospeccao, Mateus/copy, Felipe/dev, Vitoria/design, Larissa/social, Rafael/IA, Marcelo/revisao codigo, Bruno/revisao design). Buscar: criterios de roteamento para digital agency team, rubrica de classificacao por tipo de tarefa, como evitar embotelhar especialistas criticos, frameworks de routing para times criativos e tecnicos em 2025-2026.

### Sistema de classificacao: 3 perguntas-gatilho

Ao receber qualquer pedido, o Orquestrador responde internamente:

**Pergunta 1 — Qual e a competencia central exigida?**
- Gerar leads / prospectar: Caio
- Escrever texto persuasivo / CTA / copy de LP: Mateus
- Construir ou alterar pagina/sistema: Felipe
- Criar visual para Instagram / carrossel / story: Vitoria
- Publicar, agendar, engajar nas redes: Larissa
- Pesquisar, curar, usar ferramentas IA: Rafael
- Revisar codigo antes de publicar: Marcelo
- Revisar design antes de publicar: Bruno
- Tarefa envolve multiplos especialistas: mapear handoff (ver skill 3)

**Pergunta 2 — Qual e a relacao urgencia x complexidade?**
- Alta urgencia + baixa complexidade: rotear direto, brief curto
- Alta urgencia + alta complexidade: rotear com brief detalhado E sinalizar risco de prazo
- Baixa urgencia + alta complexidade: rotear com prazo estendido, espaco para iteracao
- Baixa urgencia + baixa complexidade: batch com outras tarefas do mesmo especialista

**Pergunta 3 — Ha dependencias de handoff?**
- Se a tarefa exige output de um especialista como input de outro (ex: Rafael pesquisa → Mateus escreve → Felipe implementa), o Orquestrador deve mapear a sequencia ANTES de delegar o primeiro passo.
- Nunca delegar passo 1 sem garantir que o receptor do passo 2 esta disponivel.

### Matriz de roteamento por tipo de entrega

| Tipo de Pedido | Especialista Primario | Dependencias Tipicas |
|---|---|---|
| Producao de LP | Felipe (build) | Mateus (copy) → Vitoria (assets) → Marcelo (revisao) |
| Carrossel Instagram | Vitoria (design) | Rafael (pesquisa tema) → Bruno (revisao) → Larissa (publicacao) |
| Campanha de prospeccao | Caio (leads) | Rafael (ICP/pesquisa) → Mateus (copy DM) |
| Automacao / IA | Rafael (curadoria) | Felipe (implementacao tecnica se necessario) |
| Revisao de codigo | Marcelo | Felipe (entrega) → Marcelo (revisao) → Felipe (correcao) |
| Revisao de design | Bruno | Vitoria (entrega) → Bruno (revisao) → Vitoria (correcao) |
| Post organico | Larissa | Mateus (copy) → Vitoria (arte) → Larissa (agendamento) |

### Red flags de roteamento errado

- Especialista entrega algo que nao era o que o fundador queria: provavelmente o pedido foi mal classificado na entrada
- Felipe recebe tarefas de design ou copy que nao sao dele: o Orquestrador confundiu "precisa de site" com "precisa de tudo junto"
- Caio prospectando sem copy aprovado: foi roteado antes da dependencia estar resolvida
- Mateus escreve copy sem pesquisa de ICP do Rafael: ordem de handoff invertida

### Como avaliar se o roteamento esta funcionando

- Taxa de retrabalho por tarefa (ideal: menor que 20% das entregas retornam por erro de roteamento)
- Numero de tarefas que voltam para o Orquestrador por "especialista errado"
- Tempo medio entre pedido do fundador e inicio de execucao pelo especialista certo (benchmark: menos de 4h para tarefas urgentes, menos de 24h para tarefas normais)

---

## 2. Delegacao Orientada a Intento

### O que e essa skill

Passar o brief com o "por que" estrategico, nao apenas o "o que fazer". O especialista recebe contexto suficiente para tomar decisoes proprias sem precisar perguntar a cada micro-escolha.

### Por que e critica para o Orquestrador da Triforce Auto

Time de 8 pessoas em pre-receita nao tem margem para reunioes de alinhamento frequentes. Se o Orquestrador passa apenas lista de instrucoes, o especialista fica preso ao que foi pedido e nao consegue adaptar quando surge uma variavel nova. Com intento claro, o especialista age com autonomia dentro dos limites certos.

### Perplexity Research Brief

**Projeto:** Triforce Auto — pre-receita, time lean. O Orquestrador delega para 8 especialistas via mensagem async (WhatsApp/Notion). Buscar: formato de brief orientado a intento para times pequenos de agencia digital, como estruturar o "por que" antes do "o que", frameworks de delegacao que reduzem perguntas de volta, exemplos de brief para copywriter / dev web / designer IG em contexto de producao de landing page e carrossel Instagram. Referencia: frameworks DEEA, 6T, RACI adaptados para time de 8 pessoas pre-receita 2025-2026.

### Formato padrao de brief do Orquestrador

Todo brief entregue pelo Orquestrador deve conter os 7 campos abaixo. Campos em negrito sao obrigatorios; os demais sao opcionais se o contexto for obvio.

```
TAREFA: [o que precisa ser feito, em 1-2 frases]
INTENTO: [por que isso importa agora, qual resultado de negocio isso apoia]
INPUTS: [o que o especialista ja tem disponivel para comecar]
DONO: [nome do especialista responsavel pela entrega]
PRAZO: [data/hora limite ou SLA do tipo de tarefa]
CRITERIO DE SUCESSO: [como o Orquestrador vai saber que a entrega esta boa]
GATILHO DE ESCALADA: [o que justifica o especialista parar e pedir ajuda antes do prazo]
```

### Exemplo aplicado: brief para Mateus (copy de LP)

```
TAREFA: Escrever copy completo para LP do cliente Barbearia Nova Era (homepage).
INTENTO: LP vai ser o ativo central da campanha de prospeccao que o Caio vai usar essa semana. Quanto mais rapido o copy estiver pronto, mais cedo o Caio consegue converter os leads que ja estao na lista.
INPUTS: Pesquisa de ICP feita pelo Rafael (arquivo em [link]). Referencia visual da LP no Figma (link). Tom de voz: direto, sem frescura, fala com homem 25-45 anos.
DONO: Mateus
PRAZO: Quinta 18h
CRITERIO DE SUCESSO: headline clara com beneficio, CTA visivel em cada dobra, sem jargao de marketing.
GATILHO DE ESCALADA: Se o ICP do Rafael estiver incompleto ou contraditorio, avisar antes de escrever.
```

### Red flags de delegacao mal feita

- Especialista entrega algo tecnicamente correto mas estrategicamente errado: intento nao foi comunicado
- Especialista faz multiplas perguntas de volta antes de comecar: inputs insuficientes ou criterio de sucesso vago
- Entrega chega no prazo mas precisa de refacao completa: criterio de sucesso nao foi definido na delegacao
- Especialista entregou mais do que pedido (gold-plating): escopo nao estava claro

### Niveis de delegacao por maturidade do especialista

| Nivel | Descricao | O que o Orquestrador passa |
|---|---|---|
| 1 — Demonstracao | Especialista novo na funcao | Mostra como fazer, acompanha de perto |
| 2 — Tentativa guiada | Especialista aprendendo | Brief detalhado + checklist de entrega |
| 3 — Execucao independente | Especialista maduro na funcao | Brief de intento, criterio de sucesso, prazo |
| 4 — Ensina outros | Especialista senior | Apenas intento e resultado esperado |

Para o time atual da Triforce: Felipe e Marcelo operam no nivel 3-4. Caio, Vitoria e Larissa dependem do tipo de tarefa. Mateus e Rafael operam em 3 para tarefas conhecidas, 2 para tarefas novas.

### Como avaliar se a delegacao orientada a intento esta funcionando

- Numero de perguntas de volta por tarefa delegada (meta: menos de 1 por entrega)
- Taxa de retrabalho apos entrega (meta: menos de 15%)
- Velocidade de inicio de execucao pelo especialista apos receber o brief

---

## 3. Gestao de Handoffs

### O que e essa skill

Garantir que a transicao entre especialistas preserve 100% do contexto relevante. O receptor de um handoff deve conseguir comecar sem fazer perguntas ao emissor.

### Por que e critica para o Orquestrador da Triforce Auto

O fluxo mais critico da Triforce e o de producao de LP e carrossel, que envolve 3-4 especialistas em sequencia. Cada ponto de transicao e um ponto de perda de contexto. O Orquestrador e o responsavel por garantir que o pacote de handoff existe antes de liberar o proximo passo.

### Perplexity Research Brief

**Projeto:** Triforce Auto — fluxo de producao envolve Rafael (pesquisa) → Mateus (copy) → Felipe (build) → Marcelo (revisao codigo) / Vitoria (design) → Bruno (revisao design) → Larissa (publicacao). Buscar: como estruturar pacotes de handoff assincrono para agencias digitais pequenas, o que incluir no documento de transicao entre especialistas criativos e tecnicos, como evitar perda de contexto em handoffs async, melhores praticas de design-to-code handoff, custo real de handoffs mal feitos em times criativos 2025-2026.

### Estrutura do pacote de handoff padrao

Todo handoff entre especialistas deve conter:

**1. O que foi feito**
- Resumo do trabalho entregue
- Decisoes tomadas e por que
- O que foi descartado e por que

**2. O que o proximo especialista precisa fazer**
- Tarefa especifica e escopo exato
- Inputs disponiveis (links, arquivos, referencias)
- Restricoes que devem ser respeitadas

**3. Perguntas em aberto**
- O que o emissor nao sabe e o receptor pode precisar resolver
- Alertas sobre pontos de atencao

**4. Criterio de conclusao**
- Como o receptor sabe que terminou a sua parte
- Quem recebe o proximo handoff e quando

### Handoffs criticos na Triforce Auto

**Fluxo LP completa:**
```
Rafael (pesquisa ICP + referencias)
  → [HANDOFF 1]
Mateus (copy: headline, body, CTA)
  → [HANDOFF 2]
Vitoria (assets visuais da LP)
  → [HANDOFF 3]
Felipe (build no React/Vercel)
  → [HANDOFF 4]
Marcelo (revisao de codigo)
  → [HANDOFF 5]
Bruno (revisao visual final)
  → ENTREGA
```

**Fluxo carrossel Instagram:**
```
Rafael (tema, referencias visuais, dados)
  → [HANDOFF 1]
Mateus (copy dos slides)
  → [HANDOFF 2]
Vitoria (design dos slides)
  → [HANDOFF 3]
Bruno (revisao design)
  → [HANDOFF 4]
Larissa (publicacao e legenda)
  → PUBLICADO
```

### Red flags de handoff mal gerenciado

- Receptor faz perguntas que ja foram respondidas no trabalho anterior: pacote de handoff incompleto
- Felipe comeca a buildar antes do copy estar revisado: handoff liberado cedo demais
- Bruno revisa design sem saber o que a LP precisa converter: contexto de negocio nao foi propagado
- Larissa publica sem saber qual CTA foi acordado: handoff de Mateus nao incluiu intencao do texto
- Retrabalho de Felipe porque o design mudou apos o build: handoffs saindo de ordem

### Como o Orquestrador valida um handoff antes de liberar

Checklist rapido antes de notificar o proximo especialista:

- [ ] O receptor tem todos os arquivos/links necessarios?
- [ ] As decisoes tomadas na etapa anterior estao documentadas?
- [ ] O escopo do receptor esta claro (o que fazer E o que nao fazer)?
- [ ] O criterio de conclusao da proxima etapa esta definido?
- [ ] O receptor esta disponivel (ver skill 4)?

### Metricas de qualidade de handoff

- Tempo medio perdido por handoff incompleto (benchmark de mercado: handoffs ruins custam 20-30% do tempo total de um projeto)
- Numero de perguntas feitas pelo receptor ao emissor apos receber o handoff (meta: zero para handoffs padronizados)

---

## 4. Leitura de Capacidade do Time

### O que e essa skill

Saber, a qualquer momento, quem esta sobrecarregado, disponivel ou bloqueado. Pre-condicao para rotear certo — sem isso, o Orquestrador empilha tarefas nos especialistas errados.

### Por que e critica para o Orquestrador da Triforce Auto

Com apenas 8 pessoas, nao ha redundancia de papeis. Felipe e o unico dev. Vitoria e a unica designer. Se um deles esta no limite, qualquer nova tarefa cria gargalo. O Orquestrador precisa saber disso antes de delegar, nao depois.

### Perplexity Research Brief

**Projeto:** Triforce Auto — time de 8 especialistas sem ferramenta pesada de gestao. Buscar: como rastrear capacidade real de um time pequeno sem software dedicado, sinais de sobrecarga em especialistas criativos e tecnicos, como perguntar disponibilidade sem criar reunioes desnecessarias, templates de capacidade para time de 8 pessoas, como identificar gargalo antes de virar problema em agencia digital pre-receita 2025-2026.

### Mapa de capacidade semanal (modelo simples)

O Orquestrador mantem uma tabela mental (ou Notion) com 3 colunas por especialista:

| Especialista | Status atual | Proximo disponivel |
|---|---|---|
| Caio | Em prospeccao ativa (lista X) | Quinta |
| Mateus | Escrevendo LP Barbearia | Amanha |
| Felipe | Build LP em andamento | Sexta |
| Vitoria | Carrossel 3 slides faltando | Hoje 17h |
| Larissa | Agendamento da semana feito | Disponivel |
| Rafael | Pesquisando nicho Y | Hoje |
| Marcelo | Aguardando Felipe | Disponivel |
| Bruno | Aguardando Vitoria | Disponivel |

Atualizar ao inicio de cada dia util. Pode ser via mensagem rapida no WhatsApp: "Oi [nome], o que voce tem em andamento hoje?"

### Sinais de sobrecarga por especialista

**Felipe (Dev):**
- Demorando mais de 24h para responder duvidas tecnicas simples
- Commits com erros basicos que nao sao dele
- Pedindo prazo estendido para tarefas que normalmente faria rapido

**Vitoria (Designer):**
- Designs entregues com menos cuidado no detalhe
- Reutilizando elementos sem adaptar ao contexto
- Silencio prolongado (nao responde checks de status)

**Mateus (Copy):**
- Copies repetindo estruturas sem adaptar ao cliente
- Entregas atrasadas sem aviso previo
- Pedindo mais tempo para tarefas de escopo conhecido

**Rafael (Curador IA):**
- Pesquisas rasas, sem fontes solidas
- Saindo do escopo e tentando executar em vez de curar
- Outputs de IA nao revisados antes de enviar

**Caio (Prospector):**
- Leads com qualidade caindo (ICP mal qualificado)
- Diminuindo cadencia de abordagens sem comunicar
- Respondendo leads existentes com atraso

### Gargalos criticos a monitorar

- **Felipe bloqueado:** para toda producao tecnica. Prioridade maxima para desbloquear.
- **Vitoria bloqueada:** para carrosseis e assets de LP. Dependencia direta de Larissa e Bruno.
- **Mateus bloqueado:** copy e o input de quase tudo. LP sem copy = Felipe nao tem o que buildar.
- **Rafael bloqueado:** sem pesquisa, Mateus escreve no escuro, Caio prospecta sem ICP.

### Como o Orquestrador age quando detecta gargalo

1. Identificar se o gargalo e de volume (muitas tarefas) ou de bloqueio (esperando input de outro)
2. Se volume: redistribuir ou atrasar tarefas de menor prioridade estrategica
3. Se bloqueio: resolver o bloqueio diretamente antes de qualquer outra acao
4. Nunca empilhar nova tarefa em especialista ja no limite sem remover uma tarefa anterior

---

## 5. Criterio de Qualidade por Especialista

### O que e essa skill

Saber o que e "bom o suficiente" para cada funcao sem precisar executar. O Orquestrador nao precisa saber escrever copy ou codar — precisa saber reconhecer quando o output esta pronto para a proxima etapa.

### Por que e critica para o Orquestrador da Triforce Auto

Em pre-receita, cada entrega ruim tem custo alto. Uma LP que nao converte desperdicou trabalho de 4+ especialistas. O Orquestrador e a ultima linha de QA generalista antes da entrega ao cliente ou ao mercado.

### Perplexity Research Brief

**Projeto:** Triforce Auto — Orquestrador revisa entregas de 8 especialistas sem ser especialista em nenhuma das areas. Buscar: criterios de avaliacao de qualidade para copywriter de LP/Instagram, dev web React (codigo limpo, sem erros de console, performance), designer Instagram (alinhamento de marca, hierarquia visual), social media (frequencia, engajamento, tom), curador de IA (qualidade de pesquisa, relevancia de output), prospector (qualidade de lead, taxa de resposta), revisor de codigo e revisor de design. QA checklists para cada papel em agencia digital 2025-2026.

### QA Checklist por especialista

**Caio — Prospector**

Entrega boa:
- Lead tem Instagram com perfil completo, ativo nos ultimos 30 dias
- Lead se encaixa no ICP definido (negocio presencial OU empreendedor digital, sem LP ou com LP ruim)
- Score justificado com pelo menos 2 sinais de compra identificados
- Mensagem de abordagem personalizada (nao generica)

Red flags:
- Leads sem WhatsApp identificado
- Perfis com menos de 500 seguidores sem justificativa
- Mensagens padrao sem personalizacao
- Leads de nicho fora do ICP

**Mateus — Copywriter**

Entrega boa:
- Headline comunica beneficio concreto em menos de 10 palavras
- CTA visivel em cada dobra da LP (ou em cada slide do carrossel)
- Linguagem do cliente-alvo, sem jargao de marketing
- Objecoes mais comuns endereçadas no texto
- Sem erros de ortografia

Red flags:
- Headline generica ("Solucoes para o seu negocio")
- CTA fraco ou ausente ("Saiba mais" sem contexto)
- Texto longo demais sem quebras visuais
- Tom que nao combina com o cliente-alvo definido no brief

**Felipe — Dev Web**

Entrega boa:
- Zero erros no console do navegador
- Pagina carrega em menos de 3 segundos (mobile)
- Responsiva em mobile e desktop
- Formulario de contato/WhatsApp funciona
- Deploy feito e URL ativa

Red flags:
- Erros de console (mesmo que "nao quebrem" o visual)
- Layout quebrado no mobile
- Links mortos ou botoes sem acao
- Imagens sem alt text ou compressao

**Vitoria — Designer Instagram**

Entrega boa:
- Paleta de cores coerente com identidade do cliente
- Tipografia legivel em tela de celular
- Hierarquia visual clara (o olho sabe onde ir primeiro)
- Elementos alinhados (sem pixel-drift visivel)
- Formato correto por plataforma (1:1 / 4:5 / 9:16)

Red flags:
- Cores sem relacao com a marca do cliente
- Texto pequeno demais para leitura no feed
- Slide com muito conteudo (mais de 40 palavras por slide)
- Falta de consistencia visual entre slides do mesmo carrossel

**Larissa — Social Media**

Entrega boa:
- Legenda com CTA claro no final
- Hashtags relevantes ao nicho (nao genericas)
- Horario de publicacao no pico de engajamento do perfil
- Tom de voz consistente com a identidade da marca

Red flags:
- Legenda generica que poderia ser de qualquer marca
- Publicacao sem CTA
- Hashtags irrelevantes ou banidas
- Erro de ortografia em texto publicado

**Rafael — Curador IA**

Entrega boa:
- Pesquisa com pelo menos 3 fontes identificadas
- Output de IA revisado e editado (nao raw)
- Conclusoes acionaveis (nao apenas descricao)
- Formato adequado para o proximo especialista usar (ex: se vai para Mateus, ja estruturado como insumo de copy)

Red flags:
- Pesquisa com uma unica fonte ou sem fonte
- Output de IA colado sem edicao
- Informacoes contradicias sem resolucao
- Formato de entrega que obriga o receptor a reformatar antes de usar

**Marcelo — Revisor de Codigo**

Entrega boa:
- Lista de issues categorizada por severidade (critico / minor / sugestao)
- Cada issue com localizacao exata (arquivo + linha)
- Sugestao de correcao para cada item critico
- Confirmacao de que o build passa sem erros apos correcoes

Red flags:
- Revisao que aprova codigo com erros de console
- Issues sem localizacao especifica
- Revisao superficial (apenas visual, sem checar logica)
- Devolucao sem priorizacao (tudo listado como igualmente urgente)

**Bruno — Revisor de Design**

Entrega boa:
- Feedback categorizado: alinhamento de marca / hierarquia visual / erros tecnicos
- Screenshots anotados indicando exatamente o que mudar
- Aprovacao explica o que foi validado, nao apenas "aprovado"
- Feedback dado antes do prazo de publicacao

Red flags:
- Feedback vago ("nao gostei do visual")
- Aprovacao sem criterio explicito
- Feedback dado depois do prazo de publicacao
- Revisao que nao verifica formato/resolucao corretos

---

## 6. Tracking de Pipeline sem Ferramenta Pesada

### O que e essa skill

Manter visibilidade de todas as tarefas ativas sem depender de software complexo. O Orquestrador e o hub de informacao — substitui o fundador como ponto de acompanhamento.

### Por que e critica para o Orquestrador da Triforce Auto

Pre-receita significa sem budget para ferramentas pagas robustas. O Orquestrador precisa de um sistema que funcione com Notion ou Trello gratuito, que seja atualizado de forma consistente e que sinalize riscos antes que virem crises.

### Perplexity Research Brief

**Projeto:** Triforce Auto — time de 8, sem ferramenta paga de gestao. Buscar: como montar Kanban funcional no Notion ou Trello para agencia digital pequena, colunas ideais para pipeline de producao criativa + tecnica, sistema de color-code de risco sem overhead, como atualizar o board sem criar burocracia, diferenca entre Notion e Trello para uso em pre-receita, templates de kanban para agencia digital 2025-2026.

### Estrutura do board Kanban do Orquestrador

**Colunas:**

| Coluna | O que entra | Responsavel de mover |
|---|---|---|
| A Rotear | Pedido chegou, ainda nao foi delegado | Orquestrador |
| Em Andamento | Tarefa delegada, especialista executando | Especialista |
| Em Handoff | Tarefa concluida por um especialista, aguardando proximo | Orquestrador |
| Em Revisao | Entregue para Bruno ou Marcelo revisar | Revisor |
| Concluido | Aprovado e entregue/publicado | Orquestrador |
| Bloqueado | Parado aguardando algo externo | Orquestrador |

**Sistema de color-code de risco:**

- Verde: no prazo, sem problemas
- Amarelo: em andamento, mas proximo do prazo
- Vermelho: atrasado ou em risco de nao entregar
- Cinza: bloqueado (aguardando input externo)
- Roxo: dependencia critica (move uma outra tarefa)

**Campos obrigatorios em cada card:**

- Nome da tarefa
- Especialista responsavel
- Prazo
- Cor de risco
- Dependencias (qual card precisa estar concluido antes)
- Link para o pacote de handoff (quando aplicavel)

### Rotina de manutencao do board

- **Diariamente (5 min):** mover cards que mudaram de status, atualizar cores de risco
- **Semanalmente (15 min):** revisar coluna "Em Andamento" para identificar tarefas paradas sem atualizacao
- **A cada nova tarefa:** criar card antes de delegar (nunca delegar sem card)

### Red flags no board

- Tarefa em "Em Andamento" ha mais de 3 dias sem atualizacao: provavel bloqueio silencioso
- Coluna "Em Handoff" acumulando cards: Orquestrador nao esta processando as transicoes
- Tarefa movida direto de "Em Andamento" para "Concluido" sem passar por "Em Revisao": revisao foi pulada
- Nenhum card em vermelho quando o time esta visivelmente atrasado: cores nao estao sendo atualizadas

---

## 7. Sintese de Briefing do Fundador

### O que e essa skill

Receber um pedido vago do fundador ("precisamos de uma LP para esse cliente") e transformar em brief acionavel antes de delegar. Identificar lacunas antes que virem problemas.

### Por que e critica para o Orquestrador da Triforce Auto

O fundador opera em nivel estrategico e raramente tem tempo para estruturar pedidos completos. Se o Orquestrador passa pedidos vagos adiante, o especialista perde tempo fazendo suposicoes ou perguntando de volta ao fundador, criando gargalo no unico ponto que deveria estar protegido.

### Perplexity Research Brief

**Projeto:** Triforce Auto — fundador passa pedidos vagos ao Orquestrador, que precisa transformar em brief acionavel para especialistas. Buscar: como converter feedback e pedidos vagos em instrucoes claras para equipes criativas e tecnicas, tecnicas de elicitacao de requisitos para pedidos ambiguos, como resumir de volta para confirmar entendimento, perguntas-chave para clarificar brief de LP e carrossel Instagram, quando perguntar vs quando assumir em contexto de agencia digital 2025-2026.

### Protocolo de sintese em 4 passos

**Passo 1 — Ouvir e registrar o pedido bruto**
Nao interromper. Deixar o fundador falar tudo. Registrar em texto (mesmo que seja um audio: transcrever).

**Passo 2 — Classificar o que esta claro vs. o que esta vago**

Categorias de informacao necessaria para qualquer tarefa:
- Resultado de negocio esperado (o que muda depois que essa tarefa for feita?)
- Cliente/nicho alvo
- Prazo real (nao o "seria bom ter" — o "precisa estar no ar ate quando")
- Tom e restricoes (o que nao pode aparecer? o que e inegociavel?)
- Formato e canal (LP? Carrossel? Post? WhatsApp?)

**Passo 3 — Fazer no maximo 3 perguntas de clarificacao**

Regra: nunca fazer mais de 3 perguntas de uma vez. Priorizar as que desbloqueiam mais decisoes downstream.

Exemplos de perguntas de alto valor:
- "Qual e o objetivo principal dessa LP — capturar lead ou vender direto?"
- "Quem e o dono do negocio? Tem algum material de identidade visual?"
- "Quando isso precisa estar no ar? Ha uma data de lancamento de campanha?"

**Passo 4 — Resumir de volta antes de delegar**

Antes de criar o brief para o especialista, confirmar com o fundador em 3-4 linhas: "Entendi que voce quer [X] para [Y], com prazo [Z], com o objetivo de [resultado]. Correto?"

### Red flags de sintese mal feita

- Brief chega ao especialista com campo "INTENTO" vazio: o Orquestrador nao perguntou o por que
- Especialista pergunta "mas para qual cliente isso e?" depois de receber o brief: informacao basica nao foi capturada
- Tarefa entregue dentro do escopo mas fundador diz "nao era isso": o resumo de confirmacao nao foi feito
- Prazo do especialista e o prazo do fundador sao diferentes: nao houve alinhamento de expectativa

### Perguntas-gatilho por tipo de tarefa

**Para LP:**
- Qual produto/servico vai na LP?
- Qual e o CTA principal? (WhatsApp / Formulario / Ligacao)
- Tem identidade visual do cliente?
- Quando precisa estar no ar?
- Vai ter trafego pago ou apenas organico?

**Para carrossel Instagram:**
- Qual e o tema/mensagem central?
- E para o perfil do cliente ou para a Triforce?
- Qual e o CTA do ultimo slide?
- Tem alguma referencia visual?
- Quando publica?

**Para campanha de prospeccao:**
- Qual nicho vai ser prospectado?
- Qual e a oferta que o Caio vai apresentar?
- Qual e o volume de abordagens esperado?

---

## 8. Proxy do Fundador

### O que e essa skill

Tomar decisoes operacionais autonomamente, sem precisar consultar o fundador a cada escolha. Escalando apenas bloqueios reais: scope creep, conflito de prioridade nao resolvivel no nivel operacional, recurso indisponivel.

### Por que e critica para o Orquestrador da Triforce Auto

O objetivo do cargo e exatamente este: liberar o fundador para o nivel estrategico. Se o Orquestrador consulta o fundador em decisoes operacionais rotineiras, o cargo nao esta cumprindo sua funcao.

### Perplexity Research Brief

**Projeto:** Triforce Auto — Orquestrador tem autonomia total em decisoes operacionais. Buscar: como chief of staff atua como proxy do fundador, framework de decisao autonoma vs escalada (decision rights matrix), quais decisoes nunca devem ser tomadas sem o fundador, como construir confianca para ampliar autonomia, exemplos de decisoes operacionais vs estrategicas em agencia digital pre-receita, como evitar "second CEO syndrome" 2025-2026.

### Decision Rights Matrix da Triforce Auto

**Verde — Orquestrador decide sozinho:**
- Roteamento de qualquer tarefa operacional
- Ajuste de prazo dentro do SLA definido (ate 20% de atraso)
- Reordenacao de prioridades dentro do sprint atual
- Aprovacao de entrega de especialista (dentro dos criterios de qualidade definidos)
- Resolucao de conflito de handoff entre especialistas
- Adicao de tarefa nova ao board se estiver dentro do escopo ja aprovado

**Amarelo — Orquestrador decide com registro (informa o fundador depois):**
- Mudanca de escopo em tarefa em andamento (pequena, nao muda o resultado final)
- Atraso acima de 20% do prazo previsto
- Decisao de design ou copy que nao tem precedente claro
- Aprovacao de entrega borderline (usa julgamento, documenta razao)

**Vermelho — Orquestrador escala ao fundador antes de decidir:**
- Nova tarefa que nao existia no plano original (scope creep real)
- Conflito de prioridade entre dois objetivos estrategicos
- Especialista impossibilitado de entregar (doença, bloqueio nao resolvivel)
- Decisao que afeta cliente diretamente (preco, prazo, entregavel acordado com cliente)
- Contratacao ou desligamento

### Como o Orquestrador age como proxy na pratica

- Responde ao time com confianca, sem frases como "preciso confirmar com o fundador" para decisoes verdes
- Documenta as decisoes tomadas no nivel amarelo para o fundador revisar depois
- Nunca usa "o fundador decidiu" quando foi ele quem decidiu — assume a decisao
- Quando escala ao fundador (nivel vermelho), chega com opcoes e recomendacao, nao apenas com o problema

### Red flags de proxy mal executado

- Orquestrador consulta o fundador mais de 2x por dia em decisoes rotineiras: autonomia nao esta sendo exercida
- Time percebe que o Orquestrador "nao tem poder real": confianca do time e do fundador deteriora
- Orquestrador toma decisoes estrategicas sem o fundador: extrapolou o escopo
- Decisoes contradizem o que o fundador teria decidido: precisa calibrar leitura do fundador

---

## 9. Gestao de SLAs Internos

### O que e essa skill

Definir prazos padrao por tipo de entrega e monitorar cumprimento. Sinalizar atraso antes de virar problema — nao depois.

### Por que e critica para o Orquestrador da Triforce Auto

Sem SLA, cada tarefa tem prazo negociado na hora, o que cria inconsistencia e atritos. Com SLA padronizado, o time sabe o que se espera de cada entrega e o Orquestrador consegue identificar gargalos sistemicos (ex: Bruno sempre atrasa mais de 24h — isso e dado, nao impressao).

### Perplexity Research Brief

**Projeto:** Triforce Auto — time de 8, sem ferramenta paga. Buscar: como definir SLAs internos para equipes de agencia digital (design, copy, dev, revisao), prazos tipicos de mercado por tipo de entrega, como monitorar cumprimento sem burocracia, como comunicar SLA ao time sem criar resistencia, o que fazer quando o SLA e sistematicamente descumprido, internal SLA templates para times criativos 2025-2026.

### Tabela de SLAs internos da Triforce Auto (proposta inicial)

| Tipo de Entrega | Responsavel | SLA Padrao | SLA Urgente |
|---|---|---|---|
| Pesquisa de ICP / tema | Rafael | 24h | 4h |
| Copy de carrossel (5-10 slides) | Mateus | 24h | 8h |
| Copy de LP completa | Mateus | 48h | 24h |
| Design de carrossel (5-10 slides) | Vitoria | 48h | 24h |
| Assets visuais de LP | Vitoria | 24h | 8h |
| Build de LP (React/Vercel) | Felipe | 72h | 48h |
| Revisao de codigo | Marcelo | 24h | 4h |
| Revisao de design | Bruno | 24h | 4h |
| Lista de leads qualificados (20) | Caio | 48h | 24h |
| Publicacao de post | Larissa | 2h apos aprovacao | 1h |

### Protocolo de gestao de SLA

**Quando o Orquestrador deve agir:**
- T-25% do prazo: check-in leve ("Oi, como ta o andamento?")
- T-10% do prazo: se nao tiver atualizacao, check-in direto
- Prazo vencido sem entrega: acionar imediatamente, entender causa, ajustar

**Categorias de descumprimento:**

| Causa | Acao do Orquestrador |
|---|---|
| Especialista sobrecarregado | Redistribuir ou priorizar |
| Bloqueio (aguardando input) | Resolver o bloqueio |
| Tarefa subestimada no escopo | Ajustar SLA para o tipo e documentar |
| Problema pessoal / imprevisto | Redistribuir com urgencia |
| Padrao repetido (especialista sempre atrasa) | Conversa individual + revisao de workload |

### Como comunicar SLA ao time sem criar resistencia

- Apresentar como acordo mutuo, nao como imposicao: "Qual e o prazo razoavel pra voce nesse tipo de entrega?"
- Primeiro ciclo: usar SLAs como referencia, nao como punicao
- Revisao mensal: ajustar baseado no que esta funcionando

### Metricas de SLA

- Taxa de cumprimento de SLA por especialista (meta: acima de 80%)
- Atraso medio quando SLA e descumprido (benchmark aceitavel: menos de 4h de atraso)
- Tipos de entrega com maior taxa de descumprimento (identificar gargalos sistemicos)

---

## 10. Conhecimento de Adjacencia Tecnica

### O que e essa skill

Entender o suficiente de cada especialidade do time para avaliar a qualidade do output sem precisar executar. Saber o que e possivel, o que e rapido, o que e complexo — em React, Figma, copy de resposta direta, Meta Ads, SEO e funil de vendas.

### Por que e critica para o Orquestrador da Triforce Auto

Sem adjacencia tecnica, o Orquestrador nao consegue avaliar se Felipe esta subestimando uma tarefa, se o design da Vitoria esta fraco ou se o copy do Mateus esta faltando o ponto central. Nao precisa saber executar — precisa saber reconhecer qualidade e ter vocabulario para dar feedback.

### Perplexity Research Brief

**Projeto:** Triforce Auto — Orquestrador precisa avaliar outputs de dev React/Vercel, design Figma para Instagram, copywriting de LP e carrossel, curadoria de IA, prospeccao Instagram. Buscar: o que um gerente nao-tecnico precisa saber para avaliar codigo React sem codar, como avaliar design para Instagram sem ser designer, criterios de LP de alta conversao que nao exigem expertise, como avaliar curadoria de IA sem ser especialista em ferramentas, vocabulario minimo de cada especialidade para dar feedback util 2025-2026.

### Adjacencia tecnica minima por area

**React / Dev Web (Felipe e Marcelo)**

O que o Orquestrador precisa saber:
- O que e um erro de console e por que importa (sinal de codigo quebrado mesmo que visual ok)
- O que e "responsivo" e como testar (redimensionar janela do navegador)
- O que e tempo de carregamento e como medir no Google PageSpeed Insights
- O que e um deploy e como verificar que o site esta no ar (URL funcionando)
- Diferenca entre um bugfix (horas) e uma nova feature (dias)

Vocabulario util:
- "O console do navegador esta limpo?" (F12 → Console → zero erros)
- "Carregou no PageSpeed acima de 80?"
- "O formulario de contato testado em mobile?"

**Figma / Design Instagram (Vitoria e Bruno)**

O que o Orquestrador precisa saber:
- O que e hierarquia visual (titulo > subtitulo > corpo — o olho segue uma ordem)
- O que e consistencia de marca (mesma paleta, mesma tipografia em todos os slides)
- O que e legibilidade em mobile (texto minimo de 16pt para leitura no feed)
- Formatos corretos: feed 1080x1080 (1:1), reels 1080x1920 (9:16), stories 1080x1920

Vocabulario util:
- "A hierarquia visual esta clara no primeiro slide?"
- "O texto esta legivel em tela de 6 polegadas?"
- "Os slides 1-5 estao coerentes com a paleta definida?"

**Copywriting (Mateus)**

O que o Orquestrador precisa saber:
- O que e uma headline de beneficio vs. headline generica
- O que e CTA e onde ele precisa estar (visivel sem scroll na primeira dobra)
- O que e prova social e por que entra no meio/fim da LP
- O que e objecao e como ela aparece no texto

Vocabulario util:
- "A headline comunica um beneficio especifico?"
- "Tem CTA na primeira dobra?"
- "Onde entra a prova social?"
- "A linguagem e do cliente-alvo ou de agencia de marketing?"

**Curadoria de IA (Rafael)**

O que o Orquestrador precisa saber:
- A diferenca entre output raw de IA e output curado (editado, verificado, formatado)
- O que e alucinacao de IA e como identificar (afirmacao sem fonte verificavel)
- O que e um prompt bem estruturado vs. um prompt generico
- Quando usar IA para pesquisa vs. quando usar para geracao de texto

Vocabulario util:
- "O output foi revisado antes de enviar?"
- "Ha fonte identificada para cada afirmacao factual?"
- "O formato esta pronto para o proximo especialista usar ou precisa ser reformatado?"

**Prospeccao Instagram (Caio)**

O que o Orquestrador precisa saber:
- O que e ICP (Ideal Customer Profile) e como verificar se o lead se encaixa
- Sinais de intenção de compra no Instagram (postagem recente de produto sem LP, bio sem link, anuncio rodando sem landing page)
- Diferenca entre volume de leads e qualidade de leads
- O que e taxa de resposta e como calcular

Vocabulario util:
- "Esse lead tem LP ou so o Instagram?"
- "Qual foi o sinal de compra identificado?"
- "Qual e a taxa de resposta dessa lista?"

---

## 11. Fluencia em IA

### O que e essa skill

Entender o que o curador de IA (Rafael) faz, avaliar a qualidade dos outputs de ferramentas de IA usadas pelo time, e saber quando uma tarefa deve ser automatizada vs. delegada para um humano.

### Por que e critica para o Orquestrador da Triforce Auto

A Triforce usa IA como stack central. Rafael e o especialista, mas o Orquestrador precisa de fluencia suficiente para avaliar o trabalho do Rafael, identificar onde IA pode acelerar outros especialistas e evitar que o time dependa cegamente de outputs de IA sem revisao humana.

### Perplexity Research Brief

**Projeto:** Triforce Auto — IA usada como stack central, Rafael como curador. Buscar: como gestor de agencia digital avalia qualidade de output de ferramentas de IA (ChatGPT, Claude, Perplexity), quando automatizar vs. delegar para humano em producao de LP e carrossel, como identificar alucinacao de IA sem ser especialista tecnico, o que e fluencia em IA para gestores nao-tecnicos em 2025-2026, frameworks de governanca de IA para times pequenos de agencia digital.

### O que o Orquestrador precisa saber sobre IA

**Nivel 1 — Fundamentos que todo gestor precisa ter:**
- IA gera probabilidades, nao verdades: todo output precisa de revisao humana antes de usar
- Qualidade do output depende da qualidade do prompt: prompt vago = resposta vaga
- IA nao tem contexto do negocio do cliente a menos que esse contexto seja fornecido no prompt
- Alucinacao: IA pode inventar fatos que parecem verdadeiros — checar afirmacoes factuais sempre

**Nivel 2 — Quando usar IA vs. humano:**

| Tarefa | IA adequada? | Obervacao |
|---|---|---|
| Pesquisa de mercado / ICP | Sim (com revisao) | Rafael cuida disso |
| Primeiro rascunho de copy | Sim (com revisao de Mateus) | IA gera estrutura, Mateus refina |
| Copy final para publicar | Nao | Requer voz humana e julgamento |
| Geracao de assets visuais | Parcialmente | Ferramentas de imagem IA como suporte, Vitoria decide |
| Codigo de LP | Sim (com revisao de Marcelo) | Acelerador, nao substituto |
| Decisao estrategica | Nao | IA pode dar dados, humano decide |
| Prospeccao e abordagem | Nao | Personalizacao exige julgamento humano |

**Nivel 3 — Como avaliar o trabalho do Rafael:**

- O output foi produzido com um prompt documentado ou o Rafael apenas "testou coisas"?
- As fontes sao verificaveis (URL, data de acesso)?
- O output passou por edicao antes de ser entregue?
- O formato esta pronto para uso pelo proximo especialista?
- O Rafael consegue explicar por que escolheu aquela ferramenta para aquela tarefa?

### Red flags de uso ruim de IA no time

- Output de IA entregue sem edicao ("colei aqui o que o ChatGPT gerou")
- Afirmacoes factuais sem fonte ("segundo pesquisas...")
- Dependencia excessiva: Rafael so usa IA e para de pensar criticamente
- Sub-uso: time evita IA por medo e faz manualmente o que poderia ser acelerado
- IA usada para decisoes que exigem julgamento humano (estrategia, tom de voz de cliente)

---

## 12. Gestao de Conflito entre Equipes

### O que e essa skill

Resolver colisoes de prioridade e mal-entendidos de handoff sem envolver o fundador. Facilitar alinhamento rapido quando dois especialistas ou duas demandas competem pelo mesmo recurso.

### Por que e critica para o Orquestrador da Triforce Auto

Em pre-receita, picos de demanda sao comuns. Caio fecha uma oportunidade e precisa de LP urgente — mas Felipe esta no limite. Vitoria esta produzindo carrossel urgente — mas Bruno nao consegue revisar porque tem outra fila. O Orquestrador precisa resolver isso sem travar nem consultar o fundador.

### Perplexity Research Brief

**Projeto:** Triforce Auto — conflitos tipicos: Caio pede LP urgente vs. Felipe com backlog cheio; Vitoria entrega design vs. Bruno com outra revisao; Mateus esperando pesquisa do Rafael mas Rafael esta em outra tarefa. Buscar: frameworks de resolucao de conflito de prioridade em times criativos pequenos, como mediar sem tomar partido, como definir criterios objetivos de prioridade para resolver disputa de recurso, quando o gerente decide vs. quando facilita negociacao entre as partes, estrategias para resolucao rapida de conflito cross-funcional 2025-2026.

### Tipos de conflito mais comuns na Triforce Auto

**Tipo 1 — Conflito de prioridade de recurso**
Duas tarefas competem pelo mesmo especialista ao mesmo tempo.
Ex: Caio fechou lead e quer LP em 48h, mas Felipe ja esta buildando LP de outro cliente.

Resolucao:
1. Verificar qual tarefa tem maior impacto direto em receita (calibracao estrategica — skill 14)
2. Verificar se ha flexibilidade de prazo em uma das tarefas
3. Se nenhuma pode ceder: escalar ao fundador com recomendacao clara ("recomendo priorizar X porque Y")

**Tipo 2 — Conflito de handoff (expectativas diferentes)**
Um especialista entregou o que entendia como certo; o receptor esperava algo diferente.
Ex: Mateus entregou copy "completo" mas Felipe diz que falta copy para o formulario.

Resolucao:
1. Verificar o brief original: o escopo estava claro?
2. Se escopo estava vago: responsabilidade do Orquestrador (corrigir o brief template)
3. Se escopo estava claro mas o especialista interpretou errado: devolver com especificacao exata do que falta
4. Nunca transformar em conflito pessoal — e sempre sobre o processo, nao sobre a pessoa

**Tipo 3 — Conflito de qualidade**
Bruno ou Marcelo reprovar trabalho que o especialista acredita estar ok.
Ex: Bruno reprova design da Vitoria, Vitoria discorda do feedback.

Resolucao:
1. Verificar se os criterios de qualidade foram comunicados antes da entrega (ver skill 5)
2. Se criterios existem: Bruno/Marcelo tem autoridade — a revisao prevalece
3. Se criterios nao existiam: oportunidade de documentar o criterio para evitar repeticao
4. Orquestrador media o alinhamento, nao toma partido estetico

### Framework rapido de resolucao (5 minutos)

1. Ouvir as duas partes separadamente (2 min cada)
2. Identificar: e conflito de recursos, expectativas ou qualidade?
3. Aplicar criterio objetivo (impacto em receita / escopo documentado / criterio de qualidade)
4. Comunicar a decisao com clareza e razao
5. Documentar o padrao para evitar repeticao

### Red flags de conflito mal gerenciado

- Conflito dura mais de 24h sem resolucao: Orquestrador nao agiu
- Especialistas deixam de comunicar entre si e passam pelo Orquestrador para tudo: dependencia excessiva
- O mesmo tipo de conflito ocorre mais de 2x: causa raiz nao foi endereçada (provavelmente um SOP faltando)

---

## 13. Registro e Evolucao de Processos

### O que e essa skill

Documentar o que funcionou e transformar em SOP reutilizavel. Construir a base operacional da empresa enquanto executa — para que a segunda LP seja mais rapida que a primeira, e a decima seja quase automatica.

### Por que e critica para o Orquestrador da Triforce Auto

Pre-receita e o momento de instalar os processos que vao escalar. Cada LP produzida e cada carrossel entregue e uma oportunidade de refinar o processo. Sem registro, o time repete os mesmos erros e o onboarding de novos membros começa do zero.

### Perplexity Research Brief

**Projeto:** Triforce Auto — agencia em pre-receita construindo processos enquanto executa. Buscar: como documentar SOPs para producao de LP e carrossel Instagram em agencia digital pequena, quando documentar (durante vs. apos a execucao), qual formato de SOP e mais facil de manter por time pequeno, como transformar o que funcionou em template reutilizavel, ferramentas gratuitas para manter base de processos (Notion, Confluence free, Google Docs), como garantir que os SOPs sao realmente usados 2025-2026.

### Quando documentar

**Durante a execucao (preferencial):**
- Quando uma tarefa nova e feita pela primeira vez, o especialista registra os passos enquanto faz
- Ferramentas como Scribe (extensao gratuita) capturam o processo automaticamente enquanto o usuario executa

**Apos a entrega (minimo aceitavel):**
- Reuniao de 15 min (ou mensagem async) apos entrega: "o que funcionou, o que teria feito diferente, o que faltou no processo"
- Orquestrador consolida em SOP antes da proxima tarefa do mesmo tipo

### Estrutura minima de SOP para a Triforce Auto

```
NOME DO PROCESSO: [ex: Producao de LP completa]
VERSAO: [data da ultima atualizacao]
RESPONSAVEIS: [quem executa cada etapa]

ETAPAS:
1. [acao] — [responsavel] — [SLA]
2. ...

INPUTS NECESSARIOS:
- [o que precisa estar pronto antes de comecar]

OUTPUTS ESPERADOS:
- [o que deve estar pronto ao terminar]

CHECKLIST DE QUALIDADE:
- [ ] [criterio 1]
- [ ] [criterio 2]

PONTOS DE ATENCAO:
- [o que costuma dar errado e como evitar]
```

### SOPs prioritarios para criar primeiro

1. **Fluxo completo de producao de LP** (Rafael → Mateus → Vitoria → Felipe → Marcelo → Bruno)
2. **Fluxo de producao de carrossel Instagram** (Rafael → Mateus → Vitoria → Bruno → Larissa)
3. **Fluxo de prospeccao** (Rafael → Caio → Mateus copy DM)
4. **Checklist de publicacao de LP** (testes antes de ir ao ar)
5. **Onboarding de novo cliente** (o que coletar no primeiro contato)

### Como garantir que os SOPs sao usados

- Linkar o SOP no card do Kanban quando a tarefa comeca
- Incluir o checklist de qualidade como parte do handoff
- Revisar o SOP sempre que uma entrega gerar retrabalho evitavel

---

## 14. Calibracao de Prioridade Estrategica

### O que e essa skill

Distinguir o que faz a empresa vender vs. o que e producao secundaria. Em pre-receita, a unica prioridade real e chegar na primeira venda o mais rapido possivel. Tudo que nao contribui para isso e ruido.

### Por que e critica para o Orquestrador da Triforce Auto

Sem calibracao estrategica, o time pode estar ocupado sem estar produtivo. Carrossei lindos para o Instagram da Triforce nao pagam contas se o pipeline de vendas esta parado. O Orquestrador e o guardian do foco — garante que o time gasta energia no que move a agulha.

### Perplexity Research Brief

**Projeto:** Triforce Auto — agencia em pre-receita, canal de aquisicao outbound Instagram/WhatsApp. Buscar: como priorizar tarefas em startup pre-receita para chegar na primeira venda, frameworks de calibracao estrategica (OKR simplificado, ICE score, MoSCoW), diferenca entre tarefa que gera receita e tarefa que gera aparencia de trabalho, como o Chief of Staff/Orquestrador protege o foco da equipe, o que cortar primeiro quando o time esta sobrecarregado em pre-receita 2025-2026.

### A pergunta central de calibracao

Antes de aceitar qualquer tarefa no board, o Orquestrador faz uma pergunta:

**"Isso move o time em direcao a primeira venda, ou e uma tarefa de conforto?"**

Tarefas de conforto sao aquelas que parecem produtivas mas nao estao no caminho critico para receita. Exemplos:
- Redesign do logo da Triforce Auto (nao e o que vende)
- Post organico para o Instagram da Triforce sem campanha de prospeccao ativa
- Documentacao interna que ninguem vai usar ainda
- Reuniao de alinhamento sem pauta especifica

### Framework de priorizacao ICE adaptado para a Triforce

Para cada tarefa candidata, o Orquestrador atribui nota de 1-3 em cada dimensao:

| Dimensao | Pergunta | Nota |
|---|---|---|
| Impacto | Quanto isso contribui para fechar a primeira venda? | 1 (nenhum) / 2 (medio) / 3 (alto) |
| Confianca | Temos clareza do que fazer e de que vai funcionar? | 1 (baixa) / 2 (media) / 3 (alta) |
| Esforco | Quanto tempo/energia vai custar? | 1 (alto) / 2 (medio) / 3 (baixo) |

Score ICE = Impacto x Confianca x Esforco (maximo 27)

Qualquer tarefa com score abaixo de 6 que nao seja de manutencao critica e candidata a corte ou adiamento.

### Hierarquia de prioridade na Triforce Auto (pre-receita)

1. **Tier 1 — Critico para receita:** LP de cliente pronta para prospectar / script de DM para Caio / pesquisa de ICP para campanha ativa
2. **Tier 2 — Suporte direto a receita:** revisao de codigo antes de publicar LP / revisao de design antes de publicar carrossel / qualificacao de leads
3. **Tier 3 — Infra e processo:** documentacao de SOP / onboarding de processo / melhoria de template
4. **Tier 4 — Nice-to-have:** conteudo organico da Triforce sem campanha / melhorias esteticas sem impacto em conversao

### O que cortar primeiro quando o time esta sobrecarregado

1. Cortar Tier 4 completamente
2. Pausar Tier 3 exceto o que desbloqueia Tier 1 ou 2
3. Nunca cortar revisoes (Marcelo e Bruno) — custo de publicar algo ruim e maior que o atraso
4. Nunca cortar pesquisa de Rafael se ha campanha ativa — sem ICP, tudo o mais e desperdicio

### Red flags de calibracao errada

- Time esta ocupado, mas nenhuma LP nova entrou no ar essa semana
- Caio esta sem leads qualificados para prospectar: pipeline travado no mais critico
- Mais energia gasta em conteudo organico do que em producao de LP para clientes
- Reunioes de alinhamento sem pauta de vendas
- Orquestrador aprovando tarefas Tier 4 enquanto Tier 1 esta atrasado

---

*Etapa 2 concluida. 14 skills com deep dive completo, incluindo research brief Perplexity, criterios de avaliacao, red flags, checklists de QA e metricas por especialista.*
