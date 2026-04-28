# Triforce Auto - Plataforma de Prestacao de Contas

Sistema interno para controle de entradas e saidas financeiras da Triforce Auto.

## Stack

- Next.js 14 (App Router)
- TypeScript
- Supabase (Auth + Database)
- Tailwind CSS
- Design System Triforce Auto

## Setup

### 1. Instalar dependencias

```bash
npm install
```

### 2. Configurar variaveis de ambiente

Copie `.env.example` para `.env.local` e preencha com suas credenciais do Supabase:

```bash
cp .env.example .env.local
```

```env
NEXT_PUBLIC_SUPABASE_URL=https://SEU_PROJECT_ID.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=sua_anon_key_aqui
```

### 3. Criar o schema no Supabase

No painel do Supabase, acesse o SQL Editor e execute o arquivo:

```
supabase/schema.sql
```

Isso criara:
- Tabela `transactions` com RLS
- Tabela `profiles` com trigger automatico
- Todas as policies de seguranca

### 4. Criar os usuarios

No painel do Supabase, em **Authentication > Users**, adicione os 3 usuarios:
- Joaquim
- Joao
- Matteo

Cada um com seu e-mail e senha proprios.

### 5. Rodar em desenvolvimento

```bash
npm run dev
```

Acesse em `http://localhost:3000`

### 6. Build para producao

```bash
npm run build
npm start
```

## Estrutura do projeto

```
src/
  app/
    login/          - Pagina de login
    dashboard/      - Dashboard principal (Server Component)
    api/auth/       - Route handler de logout
    globals.css     - Design system global
    layout.tsx      - Layout raiz
  components/
    extrato/
      DashboardClient.tsx     - Componente cliente principal
      Header.tsx              - Cabecalho com usuario e logout
      SummaryCards.tsx        - Cards de resumo (saldo, entradas, saidas)
      Filters.tsx             - Filtros de periodo e tipo
      TransactionTable.tsx    - Tabela de lancamentos
      TransactionModal.tsx    - Modal para criar/editar transacao
      DeleteConfirmModal.tsx  - Modal de confirmacao de exclusao
      Toast.tsx               - Notificacoes de feedback
  lib/
    supabase/
      client.ts     - Cliente Supabase browser
      server.ts     - Cliente Supabase server
      middleware.ts - Auth middleware
    utils.ts        - Utilitarios (formatacao, filtros, calculo)
  middleware.ts     - Middleware Next.js (protecao de rotas)
  types/
    index.ts        - Tipos TypeScript
supabase/
  schema.sql        - Schema + RLS completo
```

## Regras de acesso (RLS)

| Operacao | Regra |
|----------|-------|
| SELECT   | Todos os usuarios autenticados veem todas as transacoes |
| INSERT   | Usuario insere apenas com seu proprio user_id |
| UPDATE   | So o criador pode editar |
| DELETE   | So o criador pode deletar |

## Design System

Cores obrigatorias Triforce Auto:
- Accent: `#FF6600`
- Black: `#050505`
- Dark: `#0d0d0d`
- Light: `#F5F0E8`

Fonte unica: Montserrat
