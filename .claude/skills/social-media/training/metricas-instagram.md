---
skill: social-media
doc: metricas-instagram
version: "1.0"
created_at: 2026-04-17
---

# Métricas Instagram — KPIs, o que medir, como interpretar

## Princípio

Métrica que não gera decisão é ruído. Para cada número que você acompanha, precisa saber: "o que eu faço diferente se esse número cair?"

---

## KPIs primários

### 1. Alcance (Reach)

**O que é:** número de contas únicas que viram o post.

**Como medir:** Meta Business Suite → Insights do post → Alcance.

**Benchmark para canal em crescimento:**
- Carrossel: alcance orgânico entre 5-15% dos seguidores é saudável
- Reels: pode ultrapassar 100% — distribui para não-seguidores
- Stories: 20-40% dos seguidores é bom

**Como interpretar:**
- Alcance caindo sem mudança de frequência = queda de relevância para o algoritmo → testar novo gancho
- Reels com alcance alto mas engajamento baixo = atraiu público errado → revisar tema
- Alcance crescendo = o algoritmo está distribuindo → manter o formato e horário

---

### 2. Taxa de Engajamento

**O que é:** (curtidas + comentários + salvamentos + compartilhamentos) ÷ alcance × 100.

**Como medir:** calcula manualmente com dados do Meta Business Suite.

**Benchmark:**
- Abaixo de 1%: fraco
- 1-3%: dentro da média para contas em crescimento
- Acima de 3%: ótimo — replicar o formato

**O que peso mais:**
- Salvamentos > compartilhamentos > comentários > curtidas
- Salvamento = o post tem valor prático. O algoritmo adora.
- Curtida = reflexo passivo. Pouco peso real.

**Como interpretar:**
- Engajamento baixo com alcance alto = conteúdo não ressoa → mudar gancho ou formato
- Salvamentos altos = conteúdo útil, educativo → mais desse tipo
- Comentários altos = post gerou opinião → explorar controvérsias leves ou perguntas diretas

---

### 3. CTR (Click-Through Rate) — link na bio / Stories

**O que é:** percentual de pessoas que clicaram no link depois de ver o conteúdo.

**Como medir:**
- Stories com link: Meta Business Suite → Insights → Cliques no link
- Bio: Google Analytics com UTM `utm_source=instagram`

**Benchmark:**
- Stories com CTA direto para link: 1-3% de CTR é razoável
- Bio: varia muito com o post — monitorar semana a semana

**Como interpretar:**
- CTR baixo = CTA fraco ou público não qualificado → reescrever CTA do Stories ou mudar o link da bio conforme campanha ativa
- CTR alto mas sem conversão no site = problema no site, não no Instagram → avisar Felipe/Fecchio

---

### 4. Crescimento de Seguidores

**O que é:** delta de seguidores na semana/mês.

**Como medir:** Meta Business Suite → Visão geral → Seguidores.

**O que acompanhar:**
- Crescimento bruto (novos seguidores)
- Churn (quem deixou de seguir)
- Net growth = novos - churn

**Benchmark:**
- Canal novo (0-1k): crescer 5-10% ao mês é ótimo
- Canal médio (1k-10k): 2-5% ao mês é saudável
- Canal consolidado: foco em qualidade, não volume

**Como interpretar:**
- Crescimento explosivo em um post = Reels viralizou ou seguiu tendência → repetir tema/formato
- Churn alto = público errado foi atraído ou expectativa não atendida → revisar posicionamento
- Crescimento estagnado com engajamento bom = público fiel mas fechado → aumentar frequência de Reels

---

### 5. ROI de Conteúdo

**O que é:** resultado gerado por hora investida em cada formato.

**Como calcular:**
- Mapeia horas investidas por formato (carrossel: 3h, Reels: 5h, post único: 1h)
- Cruza com engajamento, alcance e CTR de cada formato
- Identifica qual formato traz mais resultado por hora

**Como interpretar:**
- Carrossel com alto salvamento e baixo tempo de produção = melhor ROI → priorizar
- Reels com alto alcance mas lento de produzir = ROI médio → manter 1/semana, não mais
- Stories com alto CTR e mínimo de produção = ROI excelente → diário sempre

---

## Relatório semanal para o fundador

Toda sexta, registra no Notion e apresenta ao fundador:

```
Semana [data]:
- Post com mais alcance: [título] — [número] pessoas
- Post com mais engajamento: [título] — [taxa]%
- Crescimento de seguidores: +[número] ([total atual])
- Cliques no link (GA4): [número] sessões vindas do Instagram
- Insight da semana: [o que aprendeu, o que vai testar]
- Proposta de ajuste: [se houver]
```

---

## O que NÃO medir como KPI principal

- Curtidas isoladas: vaidade pura
- Número de posts publicados: volume não é estratégia
- Impressões totais sem contexto de alcance: uma pessoa ver 10 vezes não vale 10 pessoas diferentes
- Seguidores comprados ou inflados: destroem taxa de engajamento e o algoritmo penaliza

---

## Ferramenta por métrica

| Métrica | Onde medir |
|---|---|
| Alcance e impressões | Meta Business Suite |
| Engajamento detalhado | Meta Business Suite + Buffer |
| CTR de Stories | Meta Business Suite |
| CTR de bio | Google Analytics (UTM) |
| Crescimento de seguidores | Meta Business Suite |
| Melhores horários | Later + Buffer |
| ROI de conteúdo | Cálculo manual no Notion |

---

## Métricas de conversão

Engajamento alto sem intenção de compra é vaidade. Esta seção define como rastrear o que importa de verdade para uma empresa pré-receita: sinais de que o Instagram está gerando oportunidades de venda, mesmo antes de qualquer venda ser fechada.

### Por que rastrear conversão antes de ter receita

A Triforce ainda não fechou a primeira venda. Isso significa que qualquer dado de conversão real agora — DMs, cliques, visitas à LP — é o mapa da primeira venda. Não medir isso é operar no escuro.

---

### Métricas de conversão que importam

**1. Cliques no link da bio**

**O que é:** número de pessoas que clicaram no link da bio após ver um post.

**Como medir:**
- Meta Business Suite → Insights do perfil → Cliques no site
- Google Analytics: filtrar por `utm_source=instagram&utm_medium=social`
- UTM padrão para o link da bio: `utm_source=instagram&utm_medium=bio&utm_campaign=[mês-ano]`

**Como interpretar:**
- Pico de cliques depois de um post específico = esse post gerou intenção de saber mais → identificar o padrão e replicar o formato/tema
- Cliques na bio sem visita à LP = problema no link (URL quebrada, redirecionamento lento) → avisar Felipe
- Zero cliques em semanas seguidas = CTA fraco ou público não qualificado → revisar a chamada nos posts e o link da bio

---

**2. DMs originadas do Instagram**

**O que é:** mensagens diretas recebidas no perfil que têm origem em um post ou Story — especialmente as que perguntam sobre o serviço, pedem orçamento ou mencionam o conteúdo publicado.

**Como rastrear:**
- Toda DM recebida deve ser registrada no Notion com: data, origem (qual post gerou), pergunta feita, status (respondida / lead quente / lead frio)
- Não há ferramenta automática — é registro manual, mas é o dado mais valioso que o canal pode gerar

**Template de registro de DM no Notion:**
```
Data: [data]
Origem: post [título] publicado em [data]
Pergunta / mensagem: [resumo]
Perfil: [link ou descrição — é ICP?]
Status: lead quente / lead frio / não é lead
Encaminhado para fundador: sim / não
```

**Como interpretar:**
- DM de ICP que pergunta sobre preço ou como funciona = lead quente → passar imediatamente para o fundador
- DM de curiosidade sem intenção de compra = lead frio → registrar e nutrir com conteúdo
- Muitas DMs sobre o mesmo tema = esse tema ressoa com o ICP → aumentar frequência de posts sobre ele

---

**3. Rastreamento com UTM sem venda realizada**

Mesmo sem venda fechada, UTMs permitem mapear qual conteúdo gera intenção. Estrutura UTM padronizada:

| Parâmetro | Valor padrão | Variável |
|---|---|---|
| utm_source | instagram | nunca muda |
| utm_medium | bio / stories / reels | conforme origem |
| utm_campaign | [mês-ano] | ex: abril-2026 |
| utm_content | [formato-tema] | ex: carrossel-whatsapp-ia |

Exemplo de link completo para o link da bio:
`https://triforceauto.com.br?utm_source=instagram&utm_medium=bio&utm_campaign=abril-2026`

Quando um Stories tem link swipe-up:
`https://triforceauto.com.br?utm_source=instagram&utm_medium=stories&utm_campaign=abril-2026&utm_content=stories-ferramenta-agendamento`

**No GA4:** criar segmento "Tráfego Instagram" e acompanhar sessões + eventos de conversão (clique no WhatsApp, envio de formulário, tempo na página acima de 2 min como proxy de intenção).

---

### Template de relatório semanal atualizado

O relatório semanal passa a incluir a seção "Intenções de compra" além das métricas de engajamento.

```
Semana [data início] a [data fim]:

— ENGAJAMENTO —
Post com mais alcance: [título] — [número] pessoas
Post com mais engajamento: [título] — [taxa]%
Post com mais salvamentos: [título] — [número]
Crescimento de seguidores: +[número] ([total atual])

— CONVERSÃO —
Cliques no link da bio (GA4): [número] sessões vindas do Instagram
DMs recebidas: [número total]
  → Leads quentes (perguntaram sobre serviço): [número]
  → Leads frios (curiosidade/conteúdo): [número]
  → Não são leads: [número]
Leads quentes encaminhados para o fundador: [número]

— INSIGHT DA SEMANA —
O que gerou mais intenção de compra: [post ou formato]
Por que esse conteúdo funcionou: [hipótese]
O que testar na próxima semana: [proposta]

— PROPOSTA DE AJUSTE —
[Se houver — mudança de tema, formato, horário ou CTA]
```

**Regra:** qualquer lead quente (DM com intenção de compra) é reportado ao fundador imediatamente — não espera o relatório de sexta.

---

### O que NÃO confundir com conversão

- Curtidas em post sobre preço ≠ intenção de compra
- Salvar um post sobre LP ≠ lead — pode ser concorrente ou curioso
- Visita ao perfil sem DM ou clique no link ≠ lead qualificado

Conversão é ação que move o seguidor em direção à venda: clicar, perguntar, visitar a LP. O resto é engajamento — importante, mas diferente.
