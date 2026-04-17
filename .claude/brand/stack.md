---
generated_at: 2026-04-13
---

# Stack — Triforce Auto

## Infraestrutura em uso

| Plataforma   | Função                          | Status      |
|--------------|---------------------------------|-------------|
| GitHub       | Versionamento de código         | ativo       |
| Vercel       | Deploy de front-end             | ativo       |
| Cloudflare   | DNS, CDN, proteção              | ativo       |
| Supabase     | Banco de dados, auth, RLS       | ativo       |

## Stack de desenvolvimento
- **Front-end:** React + TypeScript
- **Banco:** Supabase (Postgres + RLS)
- **Deploy:** Vercel
- **DNS/CDN:** Cloudflare

## MCPs disponíveis
- `mcp__claude_ai_Supabase__*` — integração direta com Supabase
- `mcp__claude_ai_Cloudflare_Developer_Platform__*` — Workers, KV, D1, R2
- `mcp__plugin_empresa_perplexity__*` — pesquisa de mercado

## A definir
- [ ] Plataforma de pagamento (Stripe, Kiwify, Hotmart?)
- [ ] Ferramenta de e-mail marketing
- [ ] Analytics (GA4, Plausible?)
