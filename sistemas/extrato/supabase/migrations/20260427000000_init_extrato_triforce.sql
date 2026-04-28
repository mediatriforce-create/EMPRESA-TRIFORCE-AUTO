-- =============================================================
-- TRIFORCE AUTO - Plataforma de Prestacao de Contas
-- Schema + RLS
-- =============================================================

-- Habilitar extensao UUID (ja ativa no Supabase por padrao)
-- create extension if not exists "pgcrypto";

-- =============================================================
-- TABELA: transactions
-- =============================================================
create table if not exists public.transactions (
  id          uuid primary key default gen_random_uuid(),
  user_id     uuid not null references auth.users(id) on delete cascade,
  date        date not null,
  description text not null,
  amount      decimal(10,2) not null,  -- positivo = entrada, negativo = saida
  category    text,
  created_at  timestamptz not null default now(),
  updated_at  timestamptz not null default now()
);

-- Indice para queries por data
create index if not exists transactions_date_idx on public.transactions(date desc);
-- Indice para queries por usuario
create index if not exists transactions_user_id_idx on public.transactions(user_id);

-- Trigger para atualizar updated_at automaticamente
create or replace function public.set_updated_at()
returns trigger as $$
begin
  new.updated_at = now();
  return new;
end;
$$ language plpgsql;

drop trigger if exists transactions_updated_at on public.transactions;
create trigger transactions_updated_at
  before update on public.transactions
  for each row execute function public.set_updated_at();

-- =============================================================
-- ROW LEVEL SECURITY
-- =============================================================
alter table public.transactions enable row level security;

-- DROP policies existentes (para re-run seguro)
drop policy if exists "Usuarios autenticados veem todas as transacoes" on public.transactions;
drop policy if exists "Usuario insere propria transacao" on public.transactions;
drop policy if exists "Usuario atualiza propria transacao" on public.transactions;
drop policy if exists "Usuario deleta propria transacao" on public.transactions;

-- SELECT: todos os usuarios autenticados veem tudo
create policy "Usuarios autenticados veem todas as transacoes"
  on public.transactions
  for select
  to authenticated
  using (true);

-- INSERT: usuario logado insere com seu user_id
create policy "Usuario insere propria transacao"
  on public.transactions
  for insert
  to authenticated
  with check (auth.uid() = user_id);

-- UPDATE: so o criador pode editar
create policy "Usuario atualiza propria transacao"
  on public.transactions
  for update
  to authenticated
  using (auth.uid() = user_id)
  with check (auth.uid() = user_id);

-- DELETE: so o criador pode deletar
create policy "Usuario deleta propria transacao"
  on public.transactions
  for delete
  to authenticated
  using (auth.uid() = user_id);

-- =============================================================
-- TABELA: profiles (nome exibido no header)
-- =============================================================
create table if not exists public.profiles (
  id           uuid primary key references auth.users(id) on delete cascade,
  display_name text not null,
  created_at   timestamptz not null default now()
);

alter table public.profiles enable row level security;

drop policy if exists "Perfis visiveis para autenticados" on public.profiles;
drop policy if exists "Usuario atualiza proprio perfil" on public.profiles;

create policy "Perfis visiveis para autenticados"
  on public.profiles
  for select
  to authenticated
  using (true);

create policy "Usuario atualiza proprio perfil"
  on public.profiles
  for update
  to authenticated
  using (auth.uid() = id);

-- Trigger: criar perfil automaticamente ao cadastrar usuario
create or replace function public.handle_new_user()
returns trigger as $$
begin
  insert into public.profiles (id, display_name)
  values (
    new.id,
    coalesce(new.raw_user_meta_data->>'display_name', split_part(new.email, '@', 1))
  )
  on conflict (id) do nothing;
  return new;
end;
$$ language plpgsql security definer;

drop trigger if exists on_auth_user_created on auth.users;
create trigger on_auth_user_created
  after insert on auth.users
  for each row execute function public.handle_new_user();

-- =============================================================
-- DADOS INICIAIS DE EXEMPLO (comentar em producao)
-- =============================================================
-- Inserir transacoes de exemplo requer user_id real.
-- Use o painel Supabase ou a aplicacao para criar as primeiras transacoes.

-- =============================================================
-- CATEGORIAS SUGERIDAS (referencia, nao e uma tabela obrigatoria)
-- =============================================================
-- 'Servicos'
-- 'Fornecedores'
-- 'Salarios'
-- 'Marketing'
-- 'Infraestrutura'
-- 'Impostos'
-- 'Vendas'
-- 'Outros'
