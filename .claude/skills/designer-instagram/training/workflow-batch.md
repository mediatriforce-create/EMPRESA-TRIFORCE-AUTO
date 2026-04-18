# Workflow de Producao em Batch

> Material de treinamento — Vitoria, Designer Instagram Triforce Auto
> Canal: curadoria de IA | Paleta: #FF6B00 / #0A0A0A / #F5F0EB | Referencia: @hollyfield.ia
> Meta: 20-30 posts/semana, max 48h por batch

---

## A logica do batch profissional

Designers amadores criam um post por vez. Designers de sistema criam 20 posts em uma unica sessao organizada.

A diferenca nao e velocidade — e modo de operacao:
- Post unitario: abre o app, cria, exporta, fecha. Repete 20x.
- Batch: planeja todos os 20 de uma vez, produz no mesmo contexto, exporta tudo junto.

O batch reduz a troca de contexto (maior gasto de tempo) e garante consistencia visual — todos os posts foram criados com o mesmo estado mental e as mesmas referencias abertas.

---

## 1. Estrutura semanal — calendario de producao

### O ciclo de uma semana de producao:

| Dia | Atividade | Tempo estimado |
|---|---|---|
| Segunda | Receber briefing semanal (titulos dos 7+ posts) | 15 min |
| Segunda | Escrever prompts de IA para todos os covers | 20 min |
| Segunda | Gerar covers no Midjourney/Leonardo | 30 min |
| Terca | Tratamento Photoshop de todos os covers | 45 min |
| Terca | Montar todos os carrosseis no Figma | 90 min |
| Quarta | Revisao interna + ajustes (max 1 rodada) | 30 min |
| Quarta | Exportacao final + entrega | 20 min |

Total: ~4h por semana para 7-10 posts
Para escalar para 20-30 posts: mantenha os mesmos templates, aumente o volume na etapa de Figma

---

## 2. Estrutura de pastas — nomenclatura obrigatoria

Uma estrutura de pastas consistente elimina o tempo de "onde esta o arquivo?".

### Estrutura completa:

```
producao/
  semana-01/
    briefing/
      semana-01_briefing.md        ← titulos, headlines, temas
    raw/
      covers-ia/
        raw_cover_ferramentas-ia_v1.png
        raw_cover_5-prompts-chatgpt_v1.png
      fotos-banco/
        foto_server-room_unsplash.jpg
    treated/
      cover_ferramentas-ia_v1.png
      cover_5-prompts-chatgpt_v1.png
    figma/
      [link para o arquivo Figma da semana]
    export/
      cover_ferramentas-ia_v1.png
      carousel_5-prompts-chatgpt_v1_slide-01.png
      carousel_5-prompts-chatgpt_v1_slide-02.png
      [...]
      reels-cover_automacao-ia_v1.png
    entrega/
      semana-01_batch-completo.zip
      semana-01_legendas.md
```

### Convencao de nomenclatura de arquivos (obrigatoria):

```
[formato]_[slug-do-tema]_[versao].[extensao]

Exemplos:
cover_ferramentas-ia-marketing_v1.png
carousel_5-usos-chatgpt_v1_slide-01.png
carousel_5-usos-chatgpt_v1_slide-02.png
reels-cover_prompt-engineering_v1.png
cover_ferramentas-ia-marketing_v2.png   ← revisao
```

**Regras de nomenclatura:**
- Tudo minusculo, sem acento, sem espaco (use hifen)
- Slug do tema: 3-5 palavras maximas
- Versao: v1 (primeira entrega), v2 (apos revisao)
- Numero do slide: sempre com dois digitos (slide-01, nao slide-1)

---

## 3. O canvas de producao no Figma

### Como organizar uma sessao de batch no Figma:

1. Abra o arquivo `[TriforceAuto] Design System Instagram`
2. Crie uma nova Page: `Producao / Semana-01`
3. Crie um frame container de grade:
   - Frame: Auto Layout, Grid Auto Layout
   - Colunas: 3, Gap: 24px, Padding: 48px
4. Instancie os componentes dentro da grade (nao crie novos frames do zero)
5. Preencha: apenas headline e imagem mudam entre instancias

### Order de preenchimento no canvas:

Preencha todos os covers primeiro, depois todos os slides internos, depois todos os CTAs. Nao tente completar um carrossel inteiro antes de ir pro proximo — isso gera troca de contexto.

Ordem recomendada:
1. Todos os covers (1 por post) — confirma a identidade visual da semana
2. Todos os slides internos (item por item, todos os carrosseis de uma vez)
3. Todos os slides de CTA (um padrao, muda apenas o CTA especifico)
4. Revisao visual rapida (scroll pela grade — inconsistencias ficam obvias)
5. Exportacao em lote

---

## 4. Automacao no Figma — plugins que aceleram o batch

### Google Sheets Sync — populacao automatica de conteudo:

Esta e a automacao mais poderosa para o canal. Ao inves de digitar headline por headline, voce prepara uma planilha e o plugin preenche tudo.

**Setup da planilha:**

```
Coluna A: frame_name         (ex: carousel_5-prompts-chatgpt_v1/slide-01)
Coluna B: headline           (ex: "5 prompts que mudam tudo")
Coluna C: numero_slide       (ex: "01")
Coluna D: corpo              (ex: "Use este prompt para resumir qualquer texto em...")
Coluna E: cta                (ex: "Salve para usar depois")
Coluna F: data_publicacao    (ex: 2026-04-21)
```

**Como usar:**
1. Configure os text layers nos componentes com nomes identicos as colunas (`{headline}`, `{corpo}`)
2. No Figma: Plugins > Google Sheets Sync
3. Conecte a planilha (ID da sheet do Google)
4. Clique "Sync" — todos os frames sao preenchidos automaticamente

Resultado: 20 slides preenchidos em 30 segundos.

### BatchGen — geracao de variacoes em massa:

Para quando voce tem um template e precisa de N versoes com dados diferentes:

1. Configure o template com campos nomeados
2. Importe CSV com os dados (headline, numero, cor de tema)
3. BatchGen gera todas as variantes automaticamente
4. Exporte todas de uma vez

### Figma Workflows — automacao de tarefas repetitivas:

Plugin que permite criar "macros" de acoes Figma:
- Renomear multiplos frames seguindo um padrao
- Aplicar o mesmo estilo a layers selecionados
- Reorganizar elementos na grade

---

## 5. Exportacao em lote — configuracao definitiva

### Preparando os frames para exportacao:

1. Selecione todos os frames de producao da semana (Ctrl+A na pagina de producao)
2. No painel direito, desca ate "Export"
3. Adicione configuracao de exportacao:
   - Formato: PNG
   - Escala: 1x (se o frame ja esta em 1080px)
   - Sufixo: vazio (o nome do frame ja e o nome do arquivo)
4. Clique "Export [N] layers"
5. Figma gera um ZIP automaticamente

### Verificacao do ZIP antes de entregar:

Abra o ZIP e confirme:
- Nenhum arquivo com nome "Frame" (indica nomenclatura nao feita)
- Quantidade correta de arquivos (se o batch e 7 posts com 6 slides cada = 42 arquivos minimo)
- Tamanho dos arquivos consistente (variacao grande pode indicar erro de escala)

---

## 6. Automacao Photoshop — batch de tratamento integrado

### Script de batch completo para tratamento semanal:

**Configuracao (uma vez, reutiliza para sempre):**

1. Grave a Action `semana_tratamento_covers`:
   - Abrir imagem
   - Aplicar Color Grade (Curves + Hue/Saturation preset editorial)
   - Aplicar Noise Overlay (pattern preset)
   - Redimensionar para 1080x1080 (ou deixar a resolucao original se ja estiver correta)
   - Salvar como PNG na pasta de saida
   - Fechar arquivo

2. Executar batch:
   - `File > Automate > Batch`
   - Action: `semana_tratamento_covers`
   - Source: `raw/semana-XX/covers-ia/`
   - Destination: `treated/`
   - File Naming: `Document Name` + `_treated`

Resultado: todos os covers tratados automaticamente. Voce so confere o resultado final.

---

## 7. Sistema de legenda — entrega completa

O batch nao e so imagens — e imagem + legenda. Entregar so PNG sem legenda obriga outra pessoa a criar do zero o que voce, designer, ja sabe.

### Template de arquivo de legendas:

```markdown
# Legendas — Semana 01

---

## cover_ferramentas-ia-marketing_v1
[carrossel 6 slides]

Legenda sugerida:
As ferramentas de IA que todo profissional de marketing precisa conhecer em 2025.
Salve e compartilhe com quem precisa ver.

Hashtags: #inteligenciaartificial #marketingdigital #ia #ferramentas #produtividade

---

## cover_5-prompts-chatgpt_v1
[carrossel 5 slides]

Legenda sugerida:
5 prompts que eu uso toda semana e que voce provavelmente ainda nao conhece.
Qual voce vai testar primeiro?

Hashtags: #chatgpt #prompts #ia #automacao #produtividade

---
```

---

## 8. Checklist completo de entrega do batch semanal

### Pre-producao:
- [ ] Briefing recebido com todos os titulos/temas da semana
- [ ] Planilha de conteudo preenchida (headline, corpo, CTA de cada slide)
- [ ] Prompts de IA escritos para todos os covers

### Geracao de imagem:
- [ ] Todos os covers gerados no Midjourney/Leonardo
- [ ] Seeds anotados no arquivo de biblioteca
- [ ] Imagens com `--no text` (sem texto aleatorio)

### Tratamento Photoshop:
- [ ] Batch de color grade executado
- [ ] Noise overlay aplicado
- [ ] Imagens tratadas na pasta `treated/`

### Figma — layout:
- [ ] Page de producao da semana criada
- [ ] Todos os frames preenchidos via Google Sheets Sync ou manualmente
- [ ] Nomenclatura de frames aplicada (formato_slug_v1)
- [ ] Revisao visual rapida (scroll pela grade)
- [ ] Nenhum slide com mais de 3 elementos
- [ ] Hierarquia tipografica correta (3 niveis em todos os slides)

### Exportacao:
- [ ] Exportacao em lote feita (ZIP do Figma)
- [ ] ZIP conferido (quantidade e nomes corretos)
- [ ] Arquivos movidos para pasta `export/`

### Entrega:
- [ ] Arquivo de legendas criado (`semana-XX_legendas.md`)
- [ ] ZIP final criado (`semana-XX_batch-completo.zip`)
- [ ] Entregue com flag de formato em cada item: `[carrossel 6 slides]`, `[card]`, `[reels cover]`

---

## 9. Metricas de performance do batch

### O que medir a cada semana:

| Metrica | Meta | Como medir |
|---|---|---|
| Volume entregue | Minimo 20 posts/mes | Conta os arquivos do ZIP |
| Prazo | Max 48h por demanda | Data do briefing vs data de entrega |
| Taxa de retrabalho | Max 1 revisao por batch | Conta versoes v2, v3 |
| Tempo de producao | Reduzir 10% a cada mes | Cronometre a sessao de batch |
| Consistencia visual | Subjetivo — todos parecem da mesma campanha | Avaliacao mensal com Joaquim |

### O que fazer quando o prazo aperta:

Prioridade de corte (em ordem — o que cortar primeiro):
1. Slides opcionais de carrossel (reduz de 6 para 5 slides)
2. Slide de CTA personalizado (usa template padrao sem customizacao)
3. Variante de reels cover (entrega so o card, sem o cover vertical)

Nunca corte: o cover (e o unico que determina se o post e aberto).

---

## 10. Auditoria Mensal do Design System

O design system apodrece em silêncio. Em 6 meses sem revisão: componentes fora do padrão, nomenclatura inconsistente, templates desatualizados. A auditoria mensal previne isso.

### Frequência: uma vez por mês, última sexta do mês, 30 minutos.

### Checklist de auditoria (30 min):

**Componentes (10 min):**
- [ ] Abrir a página "Components Library" no Figma
- [ ] Verificar se todos os componentes Cover, Slide Interno, Slide CTA e Reels Cover estão usando as variables da coleção `Brand Colors` (nenhum hex solto)
- [ ] Verificar se as Component Properties estão corretas: `headline`, `has_badge`, `image_style`, `logo_position` (cover); `number`, `headline`, `body`, `has_icon`, `theme` (slide interno)
- [ ] Se algum componente foi editado diretamente (não via property), corrigir agora

**Templates (10 min):**
- [ ] Abrir a página "Templates"
- [ ] Verificar se o Template de Carrossel 6 slides, Card 1:1, Card 4:5 e Reels Cover 9:16 ainda refletem o estilo atual do canal
- [ ] Comparar visualmente com o post de maior alcance das últimas 4 semanas (pegar do log de performance) — se o estilo atual difere muito, atualizar o template
- [ ] Verificar se os tamanhos de fonte nos templates seguem a escala definida (headline 48px, corpo 16px, label 12px)

**Nomenclatura (5 min):**
- [ ] Buscar na página de produção da última semana por frames com nome "Frame" ou "Copy of" — renomear para o padrão `formato_slug_v1`
- [ ] Verificar se os componentes seguem a convenção de ponto (`.cover/dark_photo`, `.slide-interno/light`)
- [ ] Confirmar que a biblioteca de prompts (`prompts-biblioteca.md`) foi atualizada com os seeds dos covers aprovados nas últimas 4 semanas

**Exportação (5 min):**
- [ ] Abrir o ZIP do último batch e confirmar que nenhum arquivo tem "Frame" no nome
- [ ] Confirmar que todos os arquivos seguem `[formato]_[slug]_v[n].png`

### Registro da auditoria:

Ao final, adicionar ao arquivo `producao/log-auditoria.md`:

```
Data: YYYY-MM-DD | Componentes OK: sim/nao | Templates atualizados: sim/nao | Problemas encontrados: [lista] | Corrigidos: sim/nao
```

Se algum problema não puder ser corrigido na sessão de 30 minutos, registrar como pendência e resolver antes do próximo batch.

---

## 11. Escalando de 20 para 30 posts/semana

Para escalar o volume sem aumentar o tempo:

**Otimizacao 1:** Google Sheets Sync configurado e funcionando (elimina digitacao manual — ganha 60 min/semana)

**Otimizacao 2:** Action Photoshop gravada e testada (elimina tratamento manual — ganha 30 min/semana)

**Otimizacao 3:** Biblioteca de prompts com 20+ prompts aprovados por categoria (elimina escrita de prompt do zero — ganha 20 min/semana)

**Otimizacao 4:** Template de legenda pre-preenchido com formulas (headline automaticamente vira legenda com pequeno ajuste — ganha 30 min/semana)

Total de ganho: ~2,5h por semana. Suficiente para produzir mais 8-10 posts extras.
