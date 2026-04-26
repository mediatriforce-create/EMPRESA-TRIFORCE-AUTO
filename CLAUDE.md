# CLAUDE.md — Triforce Auto

## Regra de Design: LEIA ANTES DE QUALQUER ENTREGA VISUAL

### Para trabalhos DA Triforce Auto (site, LP própria, design system, materiais internos):

**OBRIGATÓRIO seguir o Design System em:**
```
C:\Users\media\OneDrive\Desktop\EMPRESA TRIFORCE AUTO\design-system.html
```

Tokens, componentes e padrões visuais que DEVEM ser respeitados:

| Token | Valor | Uso |
|---|---|---|
| `--accent` | `#FF6600` | Laranja principal — CTAs, destaques, hl |
| `--black` | `#050505` | Preto neo-brutalist (bordas, sombras) |
| `--dark` | `#0d0d0d` | Fundo escuro padrão |
| `--dark2` | `#141414` | Fundo escuro secundário |
| `--light` | `#F5F0E8` | Fundo claro (bege) |
| `--border` | `3px solid #050505` | Borda neo-brutalist |
| `--shadow` | `0 4px 0 #050505` | Sombra neo-brutalist |
| `--font` | `Montserrat` | Única fonte permitida |

**Padrões obrigatórios — Triforce Auto:**
- `btn-cartoon`: borda neo-brutalist + shimmer + `cta-pulse`. É o CTA padrão. Zero exceção.
- Alternância dark/light entre seções (nunca dois dark ou dois light seguidos)
- Aurora orbs (`rgba(255,102,0,...)` + `filter:blur`) em seções escuras
- Grid overlay sutil (`.grid-overlay`) em seções escuras
- `section-watermark` ghost text em seções de impacto
- `reveal` + `IntersectionObserver` em todos os elementos que entram na tela
- Travessão (—) **PROIBIDO** em qualquer texto visível

---

### Para trabalhos de CLIENTES da Triforce Auto:

**NUNCA aplicar a identidade da Triforce Auto (#FF6600, #050505, estilo neo-brutalist).**

Cada cliente tem sua própria identidade. Consultar a skill `claude-design` e o arquivo:
```
.claude/skills/clientes-playbook.md
```

Salvar LP de cliente sempre em:
```
clientes/{slug-do-cliente}/lp/
```

**Perfis de cliente e abordagem:**

| Perfil | Abordagem |
|---|---|
| Fantasma Digital | LP simples, foco em WhatsApp/localização/horários |
| Canva Warrior | Padroniza na LP o novo padrão visual |
| Franqueado | Credencial da rede + diferencial da unidade |
| Profissional com Marca | LP sofisticada, mais seções, conversão além do WhatsApp |
| Reinventor | Estrutura flexível, evita elementos que ficam desatualizados |

---

## Regra de Git

**Início de sessão:** `git pull`
**Fim de sessão:** `git push`

Diretório: `C:\Users\media\OneDrive\Desktop\EMPRESA TRIFORCE AUTO`
