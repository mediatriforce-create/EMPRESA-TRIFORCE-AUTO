---
skill: social-media
doc: ferramentas
version: "1.0"
created_at: 2026-04-17
---

# Ferramentas — Como usar no canal de curadoria IA

## Meta Business Suite

**O que é:** painel central do Instagram e Facebook da conta Triforce Auto.

**Uso no canal:**
- Acompanhar métricas nativas pós-publicação: alcance, impressões, engajamento
- Gerenciar inbox (comentários + DMs) sem sair da ferramenta
- Verificar crescimento de seguidores semana a semana
- Base para decisões de impulsionamento (quando aprovado pelo fundador)

**Rotina:** acesso diário pela manhã — checar performance do post do dia anterior. Registrar no Notion o que saiu fora do padrão (positivo ou negativo).

**Atenção:** métricas nativas do Meta são o principal ponto de verdade para alcance e engajamento. Google Analytics complementa com dados de clique.

---

## Later

**O que é:** ferramenta de calendário visual e agendamento para Instagram.

**Uso no canal:**
- Montar o calendário mensal visualmente — ver o feed antes de publicar
- Definir slots fixos: carrossel (Seg/Qua/Sex), Reels (Sáb), Stories (diário)
- Preview do grid para garantir consistência visual com a paleta #FF6B00 / #0A0A0A / #F5F0EB
- Agendamento com horário otimizado por audiência

**Fluxo semanal:**
1. Segunda: abre o Later, confirma slots da semana
2. Terça-Quinta: arrasta os cards recebidos da Vitória para os slots
3. Confere preview do feed — alinhamento visual antes de confirmar
4. Publica via Buffer (Later pode publicar direto, mas Buffer centraliza análise)

**Dica de uso com IA:** exportar o calendário mensal do Later em CSV e colar no Notion para análise de frequência e gaps.

---

## Buffer

**O que é:** ferramenta de publicação automatizada e análise de performance.

**Uso no canal:**
- Publicação automática nos horários definidos (integra com Later ou opera sozinho)
- Análise pós-post: engajamento, CTR, melhores horários por formato
- Relatório semanal exportável — base para o report ao fundador

**Rotina de análise:**
- 48h após cada post: abre Buffer, anota engajamento e CTR
- Sexta-feira: exporta relatório semanal, identifica top 3 posts e bottom 3
- Registra insight no Notion ("carrossel de ferramentas teve 3x mais salvamentos — repetir formato")

**Atenção:** Buffer mostra CTR de links em Stories/bio. Cruzar com Google Analytics para validar conversão real.

---

## Notion com IA

**O que é:** hub editorial central — onde tudo começa e tudo se registra.

**Estrutura do espaço Notion para o canal:**

```
Canal IA — Triforce Auto
├── Calendário Mensal (linked database com Later)
├── Banco de Pautas
│   ├── Em aberto
│   ├── Em produção
│   ├── Aprovados
│   └── Publicados
├── Temas Semanais
├── Análises de Performance
└── Briefings para Vitória / Mateus
```

**Como usar o Notion AI no fluxo:**
1. Abre o bloco de brainstorm da semana
2. Prompt: "Sugira 12 ideias de posts sobre [tema da semana] para um canal de curadoria de IA voltado a empreendedores digitais. Tom direto, sem jargão, foco em resultado concreto."
3. Filtra as melhores, edita para a voz da marca
4. Move para "Em produção" com responsável e deadline

**Templates úteis no Notion:**
- Template de pauta: título, formato (carrossel/Reels/Stories), gancho, legenda draft, hashtags, CTA, responsável visual
- Template de análise semanal: top post, bottom post, insight, ação para próxima semana

---

## Google Analytics

**O que é:** rastreamento de tráfego para o site da Triforce Auto vindo do Instagram.

**Uso no canal:**
- UTM nas URLs da bio e Stories swipe-up: `utm_source=instagram&utm_medium=social&utm_campaign=[nome-campanha]`
- Verificar quantas sessões vieram do Instagram por semana
- Identificar qual tipo de post (carrossel, Reels, Stories) gera mais cliques para o site
- Cruzar com conversões (contato, WhatsApp, formulário) para calcular ROI de conteúdo

**Rotina:**
- Semanal: acessa GA4, filtra canal Instagram, anota sessões e conversões
- Mensal: apresenta ao fundador o relatório de tráfego orgânico social com tendência

**Configuração mínima necessária:**
- GA4 instalado no site (responsabilidade do Felipe)
- UTMs padronizados em todo link do Instagram
- Meta de conversão configurada no GA4 (ex: clique no WhatsApp)
