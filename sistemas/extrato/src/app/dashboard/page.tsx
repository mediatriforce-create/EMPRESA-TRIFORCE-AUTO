import { createClient } from "@/lib/supabase/server";
import { redirect } from "next/navigation";
import DashboardClient from "@/components/extrato/DashboardClient";
import { Transaction, Profile } from "@/types";

export default async function DashboardPage() {
  const supabase = await createClient();

  const {
    data: { user },
  } = await supabase.auth.getUser();

  if (!user) {
    redirect("/login");
  }

  // Buscar transações
  const { data: transactions, error: txError } = await supabase
    .from("transactions")
    .select("*")
    .order("date", { ascending: false });

  // Buscar perfil do usuario logado
  const { data: profile } = await supabase
    .from("profiles")
    .select("*")
    .eq("id", user.id)
    .single();

  // Buscar todos os perfis para exibir nome do criador no extrato
  const { data: profiles } = await supabase.from("profiles").select("*");

  return (
    <DashboardClient
      user={user}
      profile={profile as Profile | null}
      initialTransactions={(transactions as Transaction[]) || []}
      profiles={(profiles as Profile[]) || []}
    />
  );
}
