# Ops — Triforce Auto

Pasta de estado operacional da empresa.

## Arquivos

- `accounts.yaml` — plataformas e contas em uso
- `alerts.yaml` — alertas ativos e resolvidos

## Regras

- Dados com `status: nao_confirmado` devem ser validados no primeiro `/onboarding`
- Nunca guardar senhas ou tokens aqui — apenas nomes de conta e função
