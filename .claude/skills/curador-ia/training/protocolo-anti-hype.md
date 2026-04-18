---
skill: curador-ia
doc: protocolo-anti-hype
version: "1.0"
---

# Protocolo Anti-Hype e Anti-Fake

## Contexto

Em 2025, o volume de desinformação sobre IA cresceu 3x. O mercado de conteúdo sobre IA mistura notícia real, exagero editorial, marketing de produto e fake news deliberada — às vezes na mesma publicação.

O Rafael não é apenas curador — é filtro. Publicar uma informação falsa ou exagerada sobre IA destrói a credibilidade do canal mais rápido do que qualquer algoritmo.

---

## Como identificar fake news de IA

### Red flags de desinformação

**Na manchete:**
- "IA vai [fazer algo definitivo] até [data próxima]" sem fonte primária
- "Cientistas criaram IA que [afirmação extraordinária]" sem link para paper
- "[Empresa X] destruiu todos os concorrentes com novo modelo" sem benchmark real
- "Vazamento confirma que [empresa] está desenvolvendo AGI"
- Qualquer manchete com "fim de", "substituição total de", "nunca mais"

**No corpo do artigo:**
- "Fontes próximas à empresa disseram..." sem nome ou confirmação independente
- Benchmark sem metodologia (qual dataset? quais condições? quem testou?)
- "Disponível em breve" sem data concreta
- Citação de tweet como se fosse comunicado oficial
- Artigo sem data de publicação visível
- Artigo que cita apenas outros artigos — sem fonte primária na cadeia

**Na fonte:**
- Site criado há menos de 6 meses
- Domínio semelhante a veículo legítimo (ex: techcrurnch.com, theeverge.net)
- Sem página "sobre" ou "equipe editorial" identificável
- Histório de publicação sempre alinhado com uma agenda específica

---

## Fontes confiáveis vs. não confiáveis

### Tier 1 — Alta confiança (fonte primária)
- Blog oficial das empresas: anthropic.com/blog, openai.com/blog, deepmind.google/blog, ai.meta.com/blog
- Repositórios oficiais: github.com/anthropics, github.com/openai
- Papers publicados em arXiv com autores identificados de instituições conhecidas
- Press releases distribuídos via PR Newswire, BusinessWire, GlobeNewswire

### Tier 2 — Alta confiança (jornalismo verificado)
- The Verge (theverge.com)
- Ars Technica (arstechnica.com)
- MIT Technology Review (technologyreview.com)
- TechCrunch (techcrunch.com)
- Wired (wired.com)
- Reuters Technology
- Bloomberg Technology

### Tier 3 — Confiança moderada (verificar com Tier 1 ou 2)
- VentureBeat
- ZDNet
- Gizmodo
- 9to5Google
- Newsletters de criadores individuais (mesmo os respeitados erram — checar fonte)

### Tier 4 — Baixa confiança (nunca usar como fonte única)
- Threads, tweets, posts de LinkedIn sem link para fonte
- Artigos de blogs sem equipe editorial identificável
- Sites de "AI news" criados em 2024-2025 sem histórico verificável
- Vídeos do YouTube como fonte de fato (podem comentar um fato, não são a fonte)
- Reddit, Hacker News (úteis para descoberta, não como fonte de fato)

### Sobre newsletters e criadores individuais
Simon Willison, Ben's Bites, The Batch — são curadoria de qualidade, não fonte primária. Usam para descobrir — mas sempre checam a fonte original antes de publicar.

---

## Red flags de hype (diferente de fake)

Hype não é necessariamente mentira — é exagero ou contexto omitido.

**Sinais de hype:**
- Benchmark apresentado sem comparativo ("modelo X atingiu 95%!" — 95% em quê? Comparado com o quê?)
- Demo impressionante que não representa uso real (condições controladas, cherry-picked)
- "Disponível para todos" quando na verdade é lista de espera ou acesso limitado
- Preço de lançamento apresentado como preço definitivo (geralmente muda)
- Capacidade anunciada que depende de hardware que 99% dos usuários não têm
- Resultado de "early adopters" apresentado como resultado médio esperado

**Como lidar com hype sem ignorar a notícia:**
A notícia pode ser real. O exagero fica de fora. Nível 3 é o espaço para contextualizar o que ainda não está confirmado na prática.

---

## Protocolo quando não consegue confirmar

### Passo 1 — Para. Não publica.
Intuição jornalística não substitui fonte primária. Se o claim parece grande demais ou a fonte parece fraca, parar é a decisão certa.

### Passo 2 — Busca a fonte primária (máx. 15 min)
- Acessar diretamente o site da empresa/instituição envolvida
- Buscar no Perplexity: "[empresa/produto] [claim] official announcement"
- Buscar no Google News por data (filtrar últimas 24h ou 7 dias)

### Passo 3 — Verifica confirmação independente (máx. 15 min)
- Pelo menos 2 fontes Tier 1 ou Tier 2 reportaram o mesmo fato?
- Se sim: pode avançar para pauta
- Se não: aguarda

### Passo 4 — Se não confirmou em 30 min
- Entra no Notion com status `aguardando confirmação`
- Adiciona nota: o que foi encontrado, o que falta confirmar
- Revisita na manhã seguinte
- Se em 48h não houver confirmação: move para `descartado`

### Passo 5 — Casos urgentes ou estratégicos
Se o assunto é grande (crise de segurança, regulação urgente, acontecimento que afeta muitos usuários) e há dúvida, reportar ao fundador antes de qualquer decisão de publicar ou descartar.

---

## Checklist anti-hype/anti-fake (aplicar antes de cada pauta)

- [ ] Tenho URL de fonte Tier 1 (fonte primária)?
- [ ] Ou tenho pelo menos 2 URLs de fontes Tier 2?
- [ ] O claim principal está na fonte — não é interpretação minha?
- [ ] Verifiquei a data de publicação da fonte (não é notícia antiga sendo recirculada)?
- [ ] Benchmark ou dado numérico tem metodologia ou contexto explicado?
- [ ] O produto/modelo está de fato disponível — ou é anúncio de intenção?
- [ ] Não há conflito de interesse óbvio na fonte?
- [ ] Minha legenda não exagera o claim além do que a fonte afirma?

---

## O que fazer quando uma pauta publicada estava errada

Acontece. O protocolo é claro:

1. Identificar o erro exato (dado incorreto, claim exagerado, fonte incorreta)
2. Comunicar ao fundador imediatamente
3. Editar a legenda com correção explícita (não silenciosa)
4. Se relevante, publicar post de correção — transparência é ativo, não fraqueza
5. Documentar o caso na coluna "Descartados" do Notion com a nota "publicado com erro — lição aprendida" para referência futura

A credibilidade do canal é mais importante do que qualquer post individual.
