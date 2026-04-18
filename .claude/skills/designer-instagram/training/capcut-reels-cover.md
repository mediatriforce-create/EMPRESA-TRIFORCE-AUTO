# CapCut Pro 2025 — Reels Cover com Motion para Canal Editorial Dark

> Material de treinamento — Vitoria, Designer Instagram Triforce Auto
> Canal: curadoria de IA | Paleta: #FF6B00 / #0A0A0A / #F5F0EB | Uso: thumbnails animados para reels

---

## Quando usar CapCut (e não Figma ou Photoshop)

CapCut entra no fluxo quando o reels cover precisa de **movimento**. O PNG exportado do Figma é estático — funciona para feed, não para a thumbnail de reel quando há animação.

Use CapCut para:
- Reels cover com movimento sutil na imagem (Ken Burns, zoom lento, parallax)
- Thumbnail de reel com texto animado (entrada de headline com fade ou slide)
- Cover com partículas ou efeito de luz em loop
- Exportação de versão animada do cover para upload como thumbnail no Instagram

Para reels cover 100% estático, continue usando Figma + Photoshop. CapCut entra apenas quando o movimento agrega.

---

## 1. Setup do projeto no CapCut Desktop

### Configuração inicial para reels cover:

1. Abra o CapCut Desktop (versão Pro 2025)
2. Clique em "Create project"
3. Em "Canvas size", selecione **9:16** (1080x1920) — formato padrão de reels cover vertical
4. Frame rate: **30fps** (Instagram recomenda 30fps para compatibilidade máxima)
5. Importe o PNG tratado do cover (exportado do Figma/Photoshop)

### Estrutura de layers no CapCut para cover editorial:

```
Timeline:
  Track 1 (base): imagem de background (foto editorial tratada no PS)
  Track 2 (overlay): gradiente preto de baixo para cima (PNG com transparência)
  Track 3 (texto): headline — layer de texto do CapCut
  Track 4 (branding): logo Triforce Auto (PNG com fundo transparente)
  Track 5 (efeito): partículas ou noise opcional
```

Trabalhar em layers separadas (não achatar tudo em uma imagem) é o que permite animar cada elemento independentemente.

---

## 2. Keyframes — o motor do movimento

Keyframes são marcadores na timeline que definem como um elemento muda ao longo do tempo. Dois keyframes = uma transição automática entre os dois estados.

### Tipos de keyframe disponíveis no CapCut:

| Tipo | O que anima | Uso no cover editorial |
|---|---|---|
| Position | Move o elemento na tela | Ken Burns: pan lento da imagem de fundo |
| Scale | Aumenta ou diminui tamanho | Ken Burns: zoom lento de 100% para 108% |
| Rotation | Gira o elemento | Raramente — evitar no estilo dark editorial |
| Opacity | Transparência (0-100%) | Fade in da headline, fade in do logo |
| Effect | Animações de efeito visual | Glitch, blur, flash — usar com contenção |

### Como adicionar keyframes (passo a passo):

1. Selecione o layer que quer animar (ex: imagem de fundo)
2. Mova o playhead para o ponto de início (frame 0)
3. No painel direito, localize o ícone de diamante ao lado de "Position" ou "Scale"
4. Clique no diamante — primeiro keyframe criado (estado inicial)
5. Mova o playhead para o ponto final (ex: frame 90 = 3 segundos a 30fps)
6. Altere o valor da propriedade (ex: Scale de 100% para 108%)
7. CapCut cria automaticamente a transição entre os dois keyframes

### Regra de ouro para o estilo dark editorial:

Movimento deve ser **quase imperceptível em tempo real** — só notável quando comparado com versão estática. O cover editorial não é vídeo de TikTok. O movimento existe para dar vida, não para distrair.

Valores seguros:
- Scale: de 100% para 105-108% em 4-6 segundos (zoom lentíssimo)
- Position: deslocamento máximo de 20-30px em 4-6 segundos (pan sutil)
- Opacity para headline: de 0% a 100% nos primeiros 0,5 segundo (entrada limpa)

---

## 3. Efeito Ken Burns — o movimento padrão do canal

Ken Burns é o movimento combinado de zoom + pan lento em uma imagem estática. É o padrão para reels cover editoriais de canal dark.

### Como aplicar Ken Burns no CapCut:

**Configuração para 5 segundos de duração:**

```
Keyframe 1 (frame 0):
  Scale: 100%
  Position X: 0
  Position Y: 0

Keyframe 2 (frame 150 = 5 segundos a 30fps):
  Scale: 108%
  Position X: -15px (desloca levemente para a esquerda)
  Position Y: -10px (desloca levemente para cima)
```

Resultado: a imagem de fundo cresce imperceptivelmente e se move com suavidade — o cover parece "respirar".

### Ken Burns com Ease In/Out:

Após criar os keyframes, clique com o botão direito em cada keyframe e selecione "Ease In/Out". Isso suaviza a aceleração e desaceleração do movimento — elimina a sensação mecânica.

Sem Ease In/Out: movimento linear e artificial.
Com Ease In/Out: movimento orgânico, editorial.

---

## 4. Texto animado — entrada da headline

A headline não precisa aparecer imediatamente. Uma entrada limpa (fade in de 0,3 segundo) faz o cover parecer mais produzido.

### Fade in da headline:

1. Selecione o layer de texto (headline)
2. No menu "Animations" (painel esquerdo), escolha "In animations"
3. Selecione "Fade" — duração: 0.3 segundos
4. Resultado: headline aparece suavemente nos primeiros frames

### Alternativa — Slide Up (para headlines curtas):

1. "In animations" > "Rise" ou "Fly in (bottom)"
2. Duração: 0.2-0.3 segundos
3. Efeito: headline sobe levemente ao aparecer — mais dinâmico, ainda editorial

**Evitar:** animações com bounce, rotação, shake ou qualquer efeito que destoe do tom sério do canal. O movimento é sutil ou não existe.

---

## 5. Templates no CapCut — quando usar

O CapCut Pro oferece templates prontos com motion design. Para o canal editorial dark, a maioria não serve — são templates para TikTok, vibrantes e rápidos.

### Como filtrar templates úteis:

1. Na seção "Templates", filtre por: "Minimal", "Dark", "Editorial", "Corporate"
2. Priorize templates com fundo escuro e movimento lento
3. Teste o template com a imagem de cover já tratada no PS antes de adaptar

### Quando adaptar vs criar do zero:

- **Adaptar template:** quando o template já tem a estrutura certa (fundo escuro, texto central, branding no rodapé) e só precisa das imagens e textos trocados. Economiza 15-20 minutos.
- **Criar do zero:** quando nenhum template serve o estilo dark editorial do canal. Mais controle, mais tempo.

Para o canal Triforce Auto: recomendado criar do zero nas primeiras 3 semanas para dominar o fluxo. Depois, salvar o projeto como template próprio (ver seção 7).

---

## 6. Configurações de exportação para Instagram

### Para reels cover animado (exportação como vídeo):

```
Resolução: 1080x1920 (9:16)
Frame rate: 30fps
Formato: MP4
Codec: H.264
Bitrate: 5.000-8.000 kbps (CapCut Pro permite ajuste manual)
Áudio: sem áudio (cover é thumbnail — áudio vem do vídeo real do reel)
Duração: 3-6 segundos (suficiente para o loop do thumbnail)
```

### Como exportar no CapCut Desktop:

1. Clique em "Export" (canto superior direito)
2. Resolução: 1080p
3. Frame rate: 30fps
4. Quality: "High" (não use "Medium" — Instagram comprime o upload, já começa alto)
5. Format: MP4
6. Clique "Export" e salve na pasta `export/semana-XX/`

### Nomenclatura do arquivo exportado:

```
reels-cover_[slug-do-tema]_motion_v1.mp4

Exemplos:
reels-cover_ferramentas-ia_motion_v1.mp4
reels-cover_chatgpt-novidades_motion_v1.mp4
```

### Para upload no Instagram como thumbnail do reel:

1. No Instagram, ao publicar o reel, toque em "Editar capa"
2. Selecione "Escolher do celular" (transfira o MP4 para o celular primeiro)
3. O Instagram usa o primeiro frame do vídeo como thumbnail — posicione o frame mais forte no início

---

## 7. Salvando o projeto como template reutilizável

Após criar o primeiro cover com motion e aprovar, salvar como template interno.

### Como salvar:

1. Com o projeto finalizado, acesse "File > Save as Template" (ou equivalente na versão desktop)
2. Nomeie: `triforceauto_reels-cover_dark_v1`
3. Marque os layers de imagem, headline e logo como "placeholders editáveis"
4. Para os batches seguintes: abra o template, substitua apenas imagem e headline, exporte

Resultado: o segundo reels cover leva 5 minutos, não 30.

---

## 8. Integração com o fluxo de produção semanal

O CapCut entra apenas se o reel da semana precisar de cover animado. Não é obrigatório toda semana.

### Onde encaixa na semana:

| Dia | Atividade |
|---|---|
| Terça | Tratamento Photoshop + composição Figma (carrosséis e cards) |
| Terça (fim) | Se houver reel na semana: abrir CapCut, criar cover animado (30 min) |
| Quarta | Revisão + exportação de tudo junto |

### Decisão: cover estático vs animado

| Situação | Usar |
|---|---|
| Reel curto (até 15s) com texto sobreposto | Cover animado no CapCut — reforça o estilo |
| Reel longo com narração/conteúdo denso | Cover estático do Figma — simplicidade prioriza a mensagem |
| Post de carrossel ou card (não é reel) | Sempre estático — CapCut não entra |

---

## 9. Erros comuns a evitar

- **Movimento rápido demais:** zoom de 100% para 120% em 1 segundo parece tremido, não editorial. Máximo 8% de zoom em 4+ segundos.
- **Texto animado com delay longo:** se a headline demora mais de 1 segundo para aparecer, quem assiste o thumbnail não vê a informação. Entrada máxima: 0,5 segundo.
- **Exportar em qualidade baixa:** CapCut default pode ser "Medium". Sempre conferir antes de exportar.
- **Usar música/áudio no cover:** o thumbnail de reel não tem áudio próprio. Exporte sempre sem áudio.
- **Não testar no celular:** antes de subir, transferir o arquivo para o celular e ver como fica no feed do Instagram. O que parece bom no desktop pode parecer pesado no mobile.

---

## Checklist CapCut antes de entregar

- [ ] Projeto em 9:16, 1080x1920, 30fps
- [ ] Layers organizados: fundo, overlay, texto, branding
- [ ] Movimento Ken Burns com Ease In/Out aplicado
- [ ] Headline com fade in de até 0,5 segundo
- [ ] Duração do cover: entre 3 e 6 segundos
- [ ] Exportado em MP4, 1080p, 5.000+ kbps
- [ ] Sem áudio no arquivo exportado
- [ ] Nomenclatura: `reels-cover_[slug]_motion_v1.mp4`
- [ ] Testado no celular antes de entregar
