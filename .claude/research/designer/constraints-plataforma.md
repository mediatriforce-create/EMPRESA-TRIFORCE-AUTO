# Constraints da Plataforma — Figma MCP
**Data:** 2026-04-13
**Responsável:** Gabriela (RH)
**Fonte:** developers.figma.com/docs/figma-mcp-server/plans-access-and-permissions/, alexbobes.com, perplexity_ask, forum.figma.com

---

## 1. RATE LIMITS POR PLANO (VALORES EXATOS)

### Chamadas por mês / por minuto

| Plano | Tipo de seat | Chamadas/mês | Chamadas/minuto | Uso prático |
|-------|-------------|-------------|----------------|-------------|
| Starter (Free) | Qualquer | **6/mês** | — | Apenas experimentação pontual |
| Qualquer plano | View/Collab | **6/mês** | — | Insuficiente para trabalho real |
| Professional | Full ou Dev | 200/dia | **10/min** | Viável para trabalho diário |
| Organization | Full ou Dev | 200/dia | **15/min** | Confortável para uso intensivo |
| Enterprise | Full ou Dev | **600/dia** | **20/min** | Uso intensivo e automações |

### Tools ISENTAS de rate limit
- `add_code_connect_map`
- `generate_figma_design`
- `whoami`

### Impacto prático para a Camila
- **Plano mínimo recomendado:** Professional com Dev seat (10 chamadas/min, 200/dia)
- **Sessão de design intensiva** (ex.: handoff de LP completa com ~20 seções) pode atingir o limite diário do Professional
- **Erro 429** ("Too Many Requests") aparece após 1–2h de uso intensivo no Professional

---

## 2. O QUE O FIGMA MCP PODE FAZER

### Tools de Leitura (sem restrição de plano — sujeitas a rate limits)

| Tool | Função |
|------|--------|
| `get_design_context` | Extrai contexto completo do frame selecionado: código React+Tailwind + screenshot + hints de tokens |
| `get_screenshot` | Captura screenshot da seleção atual |
| `get_metadata` | XML com IDs, nomes, tipos, posição, tamanhos de nodes |
| `get_variable_defs` | Lista todas as variáveis/tokens usados na seleção (cores, espaçamento, tipografia) |
| `get_figjam` | Converte diagramas FigJam para XML processável |
| `get_code_connect_map` | Recupera mapeamentos node Figma → componente React existente |

### Tools de Escrita (requer autenticação e permissão no arquivo)

| Tool | Função | Restrição |
|------|--------|-----------|
| `use_figma` | Cria/edita/deleta qualquer objeto no canvas via Plugin API | Requer acesso de edição ao arquivo |
| `create_new_file` | Cria novo arquivo Design ou FigJam | Requer conta com permissão de criar arquivos |
| `generate_diagram` | Gera diagrama FigJam a partir de Mermaid | Requer acesso ao FigJam |
| `search_design_system` | Busca componentes nas libraries conectadas | Requer libraries publicadas e conectadas |
| `send_code_connect_mappings` | Confirma mapeamentos Figma ↔ componentes React | **Requer Organization ou Enterprise** |
| `get_code_connect_suggestions` | Detecta mapeamentos automáticos | **Requer Organization ou Enterprise** |
| `add_code_connect_map` | Mapeia manualmente node Figma → componente React | **Requer Organization ou Enterprise** |
| `create_design_system_rules` | Gera arquivo de regras do projeto | Requer acesso ao arquivo |

---

## 3. O QUE O FIGMA MCP NÃO PODE FAZER

### Limitações funcionais confirmadas

| O que não funciona | Detalhe |
|-------------------|---------|
| **Editar design files via MCP oficial** | O servidor MCP oficial da Figma é **read-only** para design. A `use_figma` (Plugin API) é a exceção — ela pode escrever, mas requer Figma Desktop com plugin ativo |
| **Exportar assets raster** | Não consegue exportar PNG/SVG/JPG de assets. Exportação de assets deve ser feita manualmente no Figma ou via REST API separada |
| **Acessar pixels de imagens** | Não lê o conteúdo de bitmaps dentro do design (só metadados e posição) |
| **Prototype interactions** | Não acessa definições de animação, transições ou fluxos de prototype |
| **Executar plugins** | Não pode disparar plugins Figma através do MCP |
| **Acessar comentários** | Não lê ou escreve comentários/anotações no arquivo |
| **Acessar version history** | Histórico de versões não é acessível via MCP |
| **Motion design specs** | Especificações de motion design complexas não são extraídas |
| **Code Connect em plano Professional** | Toda funcionalidade de Code Connect (`get_code_connect_suggestions`, `send_code_connect_mappings`, `add_code_connect_map`) é exclusiva de **Organization e Enterprise** |

---

## 4. SERVIDOR REMOTO vs SERVIDOR LOCAL (DESKTOP)

| Aspecto | Servidor Remoto | Servidor Local (Desktop) |
|---------|----------------|------------------------|
| Instalação | Zero — OAuth simples | Requer Figma Desktop app |
| Latência | Maior (round-trip cloud) | Menor (local) |
| Requer plano pago | Não (mas rate limits severos no free) | Sim (Dev ou Full seat) |
| Funcionalidades extras | — | Acesso a seleção ativa no Figma Desktop |
| `get_design_context` | Requer URL do node explícita | Funciona com seleção ativa |
| Disponibilidade | Sempre (não depende de app aberto) | Depende do Figma Desktop estar rodando |
| **Recomendação Triforce** | Para sessões de leitura/consulta | Para sessões de design ativo (handoff) |

---

## 5. CODE CONNECT — RESTRIÇÃO CRÍTICA

**Code Connect** é a feature que mapeia componentes Figma para componentes React reais no codebase, eliminando código duplicado no handoff.

| Requisito | Detalhe |
|-----------|---------|
| Plano mínimo | **Organization** (não disponível no Professional) |
| Seat type | Full ou Dev seat |
| Custo | Organization plan: ~$45/editor/mês (USD) — verificar pricing atual |
| Alternativa sem Code Connect | Usar `get_code_connect_map` para leitura se o mapeamento já existir — mas não dá para criar novos mapeamentos |

**Impacto:** Se a Camila estiver no plano Professional, o fluxo de Code Connect (`figma-code-connect-components`) descrito no scan-operacional.md **não funcionará**. O handoff terá que ser feito manualmente com revisão de componentes.

**Workaround para plano Professional:**
1. Usar `get_design_context` sem Code Connect (gera código de referência)
2. Revisar manualmente quais componentes do codebase correspondem
3. Documentar o mapeamento em `DESIGN_SYSTEM.md` no repositório

---

## 6. QUALIDADE DO OUTPUT — LIMITAÇÕES CONHECIDAS

| Problema | Manifestação | Como mitigar |
|----------|-------------|-------------|
| **Valores Tailwind hardcoded** | `get_design_context` pode gerar `leading-[22.126px]` em vez de classes do design system | Revisar output e mapear para tokens do projeto |
| **Responsive sem múltiplos frames** | Não infere breakpoints automaticamente | Criar frames separados para mobile/tablet/desktop no Figma |
| **Estados interativos ausentes** | Hover, active, focus não são gerados automaticamente | Criar variants no Figma por estado e fazer handoff de cada uma |
| **ARIA attributes** | Código gerado raramente inclui atributos de acessibilidade | Adicionar manualmente ou usar `vercel-labs/web-design-guidelines` para auditoria |
| **Event handlers** | Lógica de interação não é gerada | Felipe implementa separadamente |

---

## 7. PERMISSÕES NECESSÁRIAS NO ARQUIVO FIGMA

Para que o MCP funcione corretamente, a Camila precisa:

| Permissão | Para quê | Como obter |
|-----------|---------|-----------|
| **Can view** | `get_design_context`, `get_screenshot`, `get_metadata` | Padrão para qualquer colaborador |
| **Can edit** | `use_figma` (escrita no canvas) | Owner precisa dar acesso de edição |
| **Ser membro do time/workspace** | Acessar arquivos do workspace | Owner do workspace adiciona como membro |
| **Library publicada** | `search_design_system` funcionar | Camila ou owner publica a library |
| **Organization/Enterprise + Dev seat** | Code Connect | Requer upgrade de plano |

---

## 8. DIAGNÓSTICO DE PLANO — CHECKLIST PARA CAMILA

Antes do primeiro projeto, verificar:

```
[ ] Qual plano Figma você usa atualmente? (Starter / Professional / Organization / Enterprise)
[ ] Qual tipo de seat? (Viewer / Collab / Full / Dev)
[ ] Você tem acesso a Dev Mode nos arquivos de cliente?
[ ] Você precisa de Code Connect no workflow?
    → Se SIM: requer Organization ou Enterprise plan
[ ] Quantos projetos simultâneos você terá?
    → Professional: 200 chamadas/dia (suficiente para 1-2 projetos ativos)
    → Organization: mesmos 200/dia mas com 15/min (menos throttling)
```

---

## 9. RECOMENDAÇÃO DE PLANO PARA A TRIFORCE

| Cenário | Plano recomendado | Justificativa |
|---------|------------------|--------------|
| Camila é a única designer, projetos sequenciais | **Professional + Dev seat** | 200 chamadas/dia suficientes; sem Code Connect ainda |
| Camila + Felipe em projetos simultâneos | **Organization** | Code Connect disponível + 15/min sem throttling |
| Escala (3+ projetos simultâneos) | **Enterprise** | 600/dia, 20/min, suporte prioritário |

**Recomendação imediata:** Iniciar no **Professional com Dev seat** (~$25/mês). Quando o pipeline Figma → React estiver rodando e Code Connect for necessário, migrar para Organization.

---

*Constraints documentados em 2026-04-13 | Gabriela (RH) | Triforce Auto*
*Fontes: developers.figma.com/docs/figma-mcp-server/plans-access-and-permissions/ | help.figma.com/hc/en-us/articles/23920389749655-Code-Connect | alexbobes.com/tech/figma-mcp-the-cto-guide-to-design-to-code-in-2026/*
