# Loop de Performance — Dados do Instagram para Decisões de Design

> Material de treinamento — Vitoria, Designer Instagram Triforce Auto
> Canal: curadoria de IA | Paleta: #FF6B00 / #0A0A0A / #F5F0EB

---

## Por que isso importa

Design sem dados é chute. Um cover que para o scroll gera impressão. Um carrossel que entrega valor gera salvamento. Cada métrica do Instagram é um sinal visual — quem sabe ler, ajusta. Quem não sabe, repete o erro.

A Larissa envia os dados toda sexta. Vitória lê, interpreta e age antes de montar o batch da semana seguinte.

---

## 1. As três métricas que importam

### Impressões

**O que é:** quantas vezes o post apareceu na tela de alguém.

**O que mede em design:** a força do cover. Impressão alta significa que o algoritmo distribuiu — e que o cover não afastou quem viu. Impressão baixa pode significar cover fraco (afastou antes de qualquer clique) ou simplesmente distribuição baixa pelo algoritmo (fora do controle do designer).

**Regra prática:**
- Cover com impressão alta = DNA visual funcionando. Anote o que tem nele: composição, peso da headline, relação foto/texto, cor dominante.
- Cover com impressão baixa = pode ser o cover, pode ser o algoritmo. Compare com os outros posts da semana antes de concluir.

---

### Salvamentos

**O que é:** quantas pessoas tocaram em "salvar" o post.

**O que mede em design:** percepção de valor. Salvamento = "isso é útil, vou precisar disso depois". É o sinal mais claro de que o formato funcionou.

**Regra prática:**
- Salvamento alto em carrossel = formato valioso. Hierarquia de slides funcionou. Densidade de informação estava certa (nem vazia, nem sobrecarregada).
- Salvamento baixo em carrossel = slides não entregaram. Verifique: o slide 2 tem uma promessa clara? A hierarquia (número + headline + corpo) está legível? O slide final tem CTA para salvar?
- Salvamento alto em card único = informação concentrada e direta. Formato eficiente para esse tipo de conteúdo.

---

### Alcance (reach)

**O que é:** quantas contas únicas viram o post.

**O que mede em design:** distribuição real. Diferente de impressões (que contam múltiplas visualizações da mesma conta), o alcance mostra quantas pessoas diferentes o post atingiu.

**Regra prática:**
- Alcance alto + salvamento baixo = post chegou em muita gente mas não pareceu valioso. Revisar se o conteúdo dos slides cumpriu a promessa do cover.
- Alcance baixo + salvamento alto = post chegou em poucas pessoas, mas quem viu salvou. Formato valioso, distribuição fraca. Não é problema de design — reportar ao fundador.

---

## 2. Combinações e diagnósticos

### Impressão alta + engajamento baixo (poucos likes, comentários, salvamentos)

**Diagnóstico:** o cover parou o scroll, mas o conteúdo decepcionou.

**O que NÃO mudar:** o cover funcionou. Não mexa na composição, não mude o estilo visual.

**O que reportar:** o problema é de conteúdo, não de design. Avisar Larissa/fundador que o cover funcionou mas o conteúdo não reteve.

---

### Impressão baixa + engajamento alto (quem viu, interagiu)

**Diagnóstico:** o cover não parou o scroll de quem não conhece o canal. O conteúdo é bom, mas o cover falhou.

**O que mudar:** revisar o cover. Comparar com o cover de maior impressão da semana — o que tem de diferente? Peso da headline? Contraste? Tensão visual na imagem?

**Ação concreta:** na semana seguinte, testar um cover mais arrojado para esse tipo de tema.

---

### Salvamento alto = formato carrossel funcionando

**Diagnóstico:** as pessoas querem guardar esse tipo de conteúdo para usar depois.

**O que fazer:** aumentar o volume de carrosséis no batch seguinte. Replicar a estrutura que funcionou: quantos slides, como o dado foi apresentado nos slides internos, qual foi o CTA do último slide.

---

### Salvamento baixo em todos os carrosséis da semana

**Diagnóstico:** os slides internos não estão entregando valor suficiente.

**Checklist de diagnóstico visual:**
- [ ] O slide 1 (cover) faz uma promessa específica?
- [ ] O slide 2 começa a cumprir essa promessa imediatamente?
- [ ] Cada slide tem no máximo 1 ideia principal?
- [ ] O último slide tem um CTA claro para salvar?
- [ ] A hierarquia visual (número > headline > corpo) está sendo respeitada?

---

### Bottom post (menor desempenho da semana)

**O que fazer:** colocar o bottom post ao lado do top post e fazer uma análise visual comparativa:

| Elemento | Top post | Bottom post | Diferença |
|---|---|---|---|
| Composição do cover | | | |
| Peso da headline | | | |
| Relação foto/texto | | | |
| Cor dominante | | | |
| Formato (card/carrossel/reels) | | | |

A diferença visual entre os dois posts geralmente revela o problema. Anotar no log.

---

## 3. O que anotar no log de performance

Arquivo: `producao/log-performance.md`

Formato de entrada semanal:

```markdown
## Semana XX — [data de início] a [data de fim]

Top cover (impressões): [slug do post] — [o que tem visualmente: ex: "headline grande, contraste forte, sem rosto"]
Top carrossel (salvamentos): [slug] — [estrutura: ex: "6 slides, dado numerado, CTA direto no último"]
Bottom post: [slug] — [hipótese visual: ex: "cover muito texto, imagem genérica"]

Ação da semana seguinte:
- [mudança concreta baseada nos dados]
- [o que vai replicar do que funcionou]
- [o que vai evitar com base no bottom]
```

---

## 4. Perguntas para fazer toda sexta ao receber os dados

Antes de fechar a análise, responder mentalmente:

1. O cover mais visto desta semana — o que eu faria diferente se precisasse criar um igual agora?
2. O carrossel mais salvo — a estrutura de slides foi clara o suficiente? O que posso padronizar?
3. O post que menos performou — foi o cover, o conteúdo ou o formato? Se for o cover, como eu o refaria?

Essas três perguntas, respondidas toda sexta, constroem intuição visual baseada em evidência — não em achismo.

---

## 5. O que não concluir a partir dos dados

- **Nunca concluir que um estilo visual "não funciona" com base em 1 semana.** Precisa de pelo menos 3 semanas de dados para ver padrão.
- **Nunca mudar a paleta ou o sistema visual com base em um post ruim.** A consistência é um ativo.
- **Nunca comparar posts com temas diferentes como se fossem equivalentes.** Um post sobre "ferramenta nova" sempre terá mais impressão que um post sobre "conceito técnico" — independente do design.

---

## Checklist do loop de performance (toda sexta)

- [ ] Dados da Larissa recebidos (top impressão, top salvamento, bottom post)
- [ ] Análise visual comparativa feita (top vs bottom)
- [ ] Diagnóstico registrado no log de performance
- [ ] Ação definida para o batch da semana seguinte
- [ ] Se necessário: reportar ao fundador/Larissa algum padrão de conteúdo (não de design)
