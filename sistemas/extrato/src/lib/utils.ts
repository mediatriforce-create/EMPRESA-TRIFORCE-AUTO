import { type ClassValue, clsx } from "clsx";
import { twMerge } from "tailwind-merge";
import { format, parseISO } from "date-fns";
import { ptBR } from "date-fns/locale";
import { Transaction, TransactionFilters, SummaryData } from "@/types";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

export function formatCurrency(value: number): string {
  return new Intl.NumberFormat("pt-BR", {
    style: "currency",
    currency: "BRL",
  }).format(value);
}

export function formatDate(dateStr: string): string {
  try {
    return format(parseISO(dateStr), "dd/MM/yyyy", { locale: ptBR });
  } catch {
    return dateStr;
  }
}

export function formatDateFull(dateStr: string): string {
  try {
    return format(parseISO(dateStr), "dd 'de' MMMM 'de' yyyy", {
      locale: ptBR,
    });
  } catch {
    return dateStr;
  }
}

export function getTodayISO(): string {
  return format(new Date(), "yyyy-MM-dd");
}

// Retorna lista de meses com transações, ordenados desc — ex: ["2026-03", "2026-02"]
export function getAvailableMonths(transactions: Transaction[]): string[] {
  const set = new Set(transactions.map((t) => t.date.slice(0, 7)));
  return Array.from(set).sort((a, b) => b.localeCompare(a));
}

// "2026-03" → "Março 2026"
export function formatMonthLabel(ym: string): string {
  try {
    return format(parseISO(`${ym}-01`), "MMMM yyyy", { locale: ptBR });
  } catch {
    return ym;
  }
}

export function filterTransactions(
  transactions: Transaction[],
  filters: TransactionFilters
): Transaction[] {
  let result = [...transactions];

  // Filtro por mes
  if (filters.selectedMonth !== "all") {
    result = result.filter((t) => t.date.startsWith(filters.selectedMonth));
  }

  // Filtro por tipo
  if (filters.type === "income") {
    result = result.filter((t) => t.amount > 0);
  } else if (filters.type === "expense") {
    result = result.filter((t) => t.amount < 0);
  }

  // Ordenar por data desc
  result.sort((a, b) => new Date(b.date).getTime() - new Date(a.date).getTime());

  return result;
}

export function calculateSummary(transactions: Transaction[]): SummaryData {
  const totalIncome = transactions
    .filter((t) => t.amount > 0)
    .reduce((sum, t) => sum + t.amount, 0);

  const totalExpense = transactions
    .filter((t) => t.amount < 0)
    .reduce((sum, t) => sum + Math.abs(t.amount), 0);

  return {
    totalIncome,
    totalExpense,
    balance: totalIncome - totalExpense,
  };
}

export const CATEGORIES = [
  "Servicos",
  "Fornecedores",
  "Salarios",
  "Marketing",
  "Infraestrutura",
  "Impostos",
  "Vendas",
  "Outros",
];
