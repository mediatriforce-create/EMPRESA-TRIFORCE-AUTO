# Constraints da Plataforma — Figma MCP
**Fonte:** developers.figma.com/docs/figma-mcp-server/plans-access-and-permissions/ | alexbobes.com | 2026-04-13

---

## 1. Rate Limits por Plano

| Plano | Seat tipo | Chamadas/mês | Chamadas/dia | Chamadas/min |
|-------|----------|-------------|-------------|--------------|
| Starter (Free) | Qualquer | **6/mês** | — | — |
| Qualquer plano | Viewer / Collab | **6/mês** | — | — |
| Professional | Full ou Dev | ilimitado | **200/dia** | **10/min** |
| Organization | Full ou Dev | ilimitado | **200/dia** | **15/min** |
| Enterprise | Full ou Dev | ilimitado | **600/dia** | **20/min** |

### Tools isentas de rate limit
- `add_code_connect_map`
- `generate_figma_design`
- `whoami`

### Impacto prático
- Starter/Free: apenas experimentação pontual — inviável para trabalho real
- Professional + Dev: viável para 1–2 projetos ativos sequenciais
- Sessão de handoff completa (~20 seções) pode atingir o limite diário do Professional
- Erro 429 ("Too Many Requests") após 1–2h de uso intensivo no Professional → pausar e retomar

---

## 2. Figma MCP — O que Pode e O que Não Pode

### Tools de Leitura (disponíveis em todos os planos pagos)

| Tool | Função |
|------|--------|
| `get_design_context` | Extrai código React+Tailwind + screenshot + hints de uma seleção. Tool principal do workflow. |
| `get_screenshot` | Captura screenshot da seleção atual |
| `get_metadata` | XML com IDs, nomes, tipos, posição e tamanhos de nodes |
| `get_variable_defs` | Lista todas as variáveis/tokens usados na seleção (cores, espaçamento, tipografia) |
| `get_figjam` | Converte diagramas FigJam para XML processável |
| `get_code_connect_map` | Recupera mapeamentos node Figma → componente React existente (leitura) |

### Tools de Escrita

| Tool | Função | Restrição |
|------|--------|-----------|
| `use_figma` | Cria/edita/deleta qualquer objeto no canvas via Plugin API | Requer Figma Desktop com plugin ativo + acesso de edição ao arquivo |
| `create_new_file` | Cria novo arquivo Design ou FigJam | Requer conta com permissão de criar arquivos |
| `generate_diagram` | Gera diagrama FigJam a partir de descrição (Mermaid) | Requer acesso ao FigJam |
| `search_design_system` | Busca componentes nas libraries conectadas | Requer libraries publicadas e conectadas |
| `create_design_system_rules` | Gera arquivo de regras do projeto | Requer acesso ao arquivo |
| `get_code_connect_suggestions` | Detecta mapeamentos automáticos Figma ↔ React | **Organization ou Enterprise apenas** |
| `send_code_connect_mappings` | Confirma mapeamentos Figma ↔ componentes React | **Organization ou Enterprise apenas** |
| `add_code_connect_map` | Mapeia manualmente node Figma → componente React | **Organization ou Enterprise apenas** |

### O que o MCP NÃO faz (independente de plano)

| Limitação | Detalhe |
|-----------|---------|
| Exportar assets raster | Não exporta PNG/SVG/JPG — fazer manualmente no Figma |
| Ler pixels de imagens | Acessa só metadados e posição de bitmaps |
| Prototype interactions | Não acessa animações, transições ou fluxos de prototype |
| Executar plugins Figma | Não dispara plugins via MCP |
| Acessar comentários | Não lê nem escreve comentários/anotações |
| Version history | Histórico de versões não acessível |
| Motion design specs | Specs de motion complexas não são extraídas |

---

## 3. Code Connect — Restrição Crítica

**Code Connect** elimina código duplicado no handoff mapeando componentes Figma → componentes React reais no codebase.

| Requisito | Detalhe |
|-----------|---------|
| Plano mínimo | **Organization** (não disponível no Professional) |
| Seat type | Full ou Dev |
| Custo estimado | Organization: ~$45/editor/mês (USD) — verificar pricing atual |

### Workaround para Professional (obrigatório)

Sem Code Connect, o handoff é feito via `DESIGN_SYSTEM.md` manual:

1. Gerar código de referência com `get_design_context`
2. Revisar manualmente quais componentes do codebase do Felipe correspondem
3. Documentar em `DESIGN_SYSTEM.md`:
   - Tabela: componente Figma → componente React → arquivo no codebase
   - Props mapeadas: Variant → enum, Boolean → boolean, Text → string
4. Felipe usa o `DESIGN_SYSTEM.md` como guia de implementação

---

## 4. Servidor Remoto vs Desktop

| Aspecto | Servidor Remoto | Desktop (Local) |
|---------|----------------|----------------|
| Instalação | Zero — OAuth simples | Requer Figma Desktop app |
| Latência | Maior (round-trip cloud) | Menor |
| `get_design_context` | Requer URL do node explícita | Funciona com seleção ativa |
| Disponibilidade | Sempre | Depende do app estar aberto |
| Recomendação | Sessões de leitura/consulta | Sessões de design ativo e handoff |

---

## 5. Qualidade do Output — Limitações Conhecidas

| Problema | Manifestação | Como mitigar |
|----------|-------------|-------------|
| Valores hardcoded | `get_design_context` pode gerar `leading-[22.126px]` em vez de classes do DS | Revisar output e mapear para tokens do projeto |
| Responsive sem múltiplos frames | Não infere breakpoints automaticamente | Criar frames separados mobile/tablet/desktop |
| Estados interativos ausentes | Hover, active, focus não gerados automaticamente | Criar variants por estado e handoff de cada uma |
| ARIA attributes | Código raramente inclui atributos de acessibilidade | Adicionar manualmente ou auditar com `web-design-guidelines` |
| Imagens sem dimensões | `get_design_context` pode omitir width/height | Revisar SEMPRE antes de entregar ao Felipe — causa CLS |

---

## 6. Permissões Necessárias no Arquivo Figma

| Permissão | Para quê |
|-----------|---------|
| Can view | `get_design_context`, `get_screenshot`, `get_metadata` |
| Can edit | `use_figma` (escrita no canvas) |
| Membro do workspace | Acessar arquivos do workspace |
| Library publicada | `search_design_system` funcionar |
| Organization/Enterprise + Dev seat | Code Connect completo |

---

## 7. Quando Fazer Upgrade de Plano

| Cenário | Plano recomendado | Justificativa |
|---------|------------------|--------------|
| Camila é a única designer, projetos sequenciais | **Professional + Dev seat** (~$25/mês) | 200 chamadas/dia suficientes; sem Code Connect por enquanto |
| Pipeline Figma → React rodando, Code Connect necessário | **Organization** (~$45/mês) | Code Connect disponível + 15/min sem throttling |
| 3+ projetos simultâneos ou automações | **Enterprise** | 600/dia, 20/min, suporte prioritário |

**Recomendação atual:** Professional + Dev seat. Migrar para Organization quando Code Connect for necessário e o pipeline estiver maduro.
