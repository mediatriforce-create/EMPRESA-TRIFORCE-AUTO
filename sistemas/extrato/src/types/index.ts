export interface Transaction {
  id: string;
  user_id: string;
  date: string;
  description: string;
  amount: number;
  category: string | null;
  created_at: string;
  updated_at: string;
}

export interface Profile {
  id: string;
  display_name: string;
  created_at: string;
}

export interface TransactionWithProfile extends Transaction {
  profiles?: Profile;
}

export type FilterType = "all" | "income" | "expense";

export interface TransactionFilters {
  selectedMonth: string; // "YYYY-MM" ou "all"
  type: FilterType;
}

export interface SummaryData {
  totalIncome: number;
  totalExpense: number;
  balance: number;
}

export type TransactionFormData = {
  date: string;
  description: string;
  amount: string;
  category: string;
  type: "income" | "expense";
};
