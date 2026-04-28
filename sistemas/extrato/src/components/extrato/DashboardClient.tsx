"use client";

import { useState, useCallback } from "react";
import { User } from "@supabase/supabase-js";
import {
  Transaction,
  Profile,
  TransactionFilters,
  TransactionFormData,
} from "@/types";
import {
  filterTransactions,
  calculateSummary,
  getAvailableMonths,
} from "@/lib/utils";
import { createClient } from "@/lib/supabase/client";
import Header from "./Header";
import SummaryCards from "./SummaryCards";
import Filters from "./Filters";
import TransactionTable from "./TransactionTable";
import TransactionModal from "./TransactionModal";
import DeleteConfirmModal from "./DeleteConfirmModal";
import ImportModal from "./ImportModal";
import { ToastContainer, ToastData } from "./Toast";
import { Plus, RefreshCw, Upload } from "lucide-react";

interface DashboardClientProps {
  user: User;
  profile: Profile | null;
  initialTransactions: Transaction[];
  profiles: Profile[];
}

let toastIdCounter = 0;

export default function DashboardClient({
  user,
  profile,
  initialTransactions,
  profiles,
}: DashboardClientProps) {
  const supabase = createClient();

  const [transactions, setTransactions] =
    useState<Transaction[]>(initialTransactions);

  const availableMonths = getAvailableMonths(transactions);
  const defaultMonth = availableMonths[0] ?? "all";

  const [filters, setFilters] = useState<TransactionFilters>({
    selectedMonth: defaultMonth,
    type: "all",
  });
  const [modalOpen, setModalOpen] = useState(false);
  const [importOpen, setImportOpen] = useState(false);
  const [editingTx, setEditingTx] = useState<Transaction | null>(null);
  const [deleteId, setDeleteId] = useState<string | null>(null);
  const [deleteLoading, setDeleteLoading] = useState(false);
  const [refreshing, setRefreshing] = useState(false);
  const [toasts, setToasts] = useState<ToastData[]>([]);

  // ── Toast helpers ────────────────────────────────────────────
  function addToast(message: string, type: ToastData["type"]) {
    const id = String(++toastIdCounter);
    setToasts((prev) => [...prev, { id, message, type }]);
  }

  const removeToast = useCallback((id: string) => {
    setToasts((prev) => prev.filter((t) => t.id !== id));
  }, []);

  // ── Refresh ──────────────────────────────────────────────────
  async function handleRefresh() {
    setRefreshing(true);
    const { data, error } = await supabase
      .from("transactions")
      .select("*")
      .order("date", { ascending: false });

    if (!error && data) {
      setTransactions(data as Transaction[]);
    }
    setRefreshing(false);
  }

  // ── Salvar (create ou update) ─────────────────────────────────
  async function handleSave(formData: TransactionFormData) {
    const rawAmount = parseFloat(formData.amount.replace(",", "."));
    const finalAmount =
      formData.type === "expense" ? -Math.abs(rawAmount) : Math.abs(rawAmount);

    if (editingTx) {
      // UPDATE
      const { error } = await supabase
        .from("transactions")
        .update({
          date: formData.date,
          description: formData.description,
          amount: finalAmount,
          category: formData.category || null,
        })
        .eq("id", editingTx.id);

      if (error) throw new Error(error.message);

      setTransactions((prev) =>
        prev.map((t) =>
          t.id === editingTx.id
            ? {
                ...t,
                date: formData.date,
                description: formData.description,
                amount: finalAmount,
                category: formData.category || null,
              }
            : t
        )
      );
      addToast("Transação atualizada com sucesso.", "success");
    } else {
      // INSERT
      const { data, error } = await supabase
        .from("transactions")
        .insert({
          user_id: user.id,
          date: formData.date,
          description: formData.description,
          amount: finalAmount,
          category: formData.category || null,
        })
        .select()
        .single();

      if (error) throw new Error(error.message);

      setTransactions((prev) => [data as Transaction, ...prev]);
      addToast("transação lançada com sucesso.", "success");
    }

    setEditingTx(null);
  }

  // ── Deletar ──────────────────────────────────────────────────
  async function handleDeleteConfirm() {
    if (!deleteId) return;
    setDeleteLoading(true);

    const { error } = await supabase
      .from("transactions")
      .delete()
      .eq("id", deleteId);

    if (error) {
      addToast("Erro ao excluir transação.", "error");
    } else {
      setTransactions((prev) => prev.filter((t) => t.id !== deleteId));
      addToast("Transação excluída.", "success");
    }

    setDeleteLoading(false);
    setDeleteId(null);
  }

  // ── Handlers de UI ───────────────────────────────────────────
  function handleOpenNew() {
    setEditingTx(null);
    setModalOpen(true);
  }

  function handleEdit(tx: Transaction) {
    setEditingTx(tx);
    setModalOpen(true);
  }

  function handleCloseModal() {
    setModalOpen(false);
    setEditingTx(null);
  }

  // ── Dados filtrados ──────────────────────────────────────────
  const filteredTransactions = filterTransactions(transactions, filters);
  const summary = calculateSummary(filteredTransactions); // resumo do mes selecionado

  return (
    <div style={{ minHeight: "100vh", background: "#0d0d0d" }}>
      <Header user={user} profile={profile} />

      {/* Conteudo principal */}
      <main
        style={{
          maxWidth: 1400,
          margin: "0 auto",
          padding: "40px 32px",
        }}
      >
        {/* Titulo da pagina */}
        <div
          style={{
            display: "flex",
            alignItems: "flex-start",
            justifyContent: "space-between",
            marginBottom: 32,
          }}
        >
          <div>
            <h1
              style={{
                fontFamily: "Montserrat, sans-serif",
                fontWeight: 900,
                fontSize: 28,
                color: "#F5F0E8",
                textTransform: "uppercase",
                letterSpacing: "0.04em",
                lineHeight: 1,
              }}
            >
              Extrato
            </h1>
            <p
              style={{
                fontFamily: "Montserrat, sans-serif",
                fontWeight: 500,
                fontSize: 13,
                color: "rgba(245,240,232,0.4)",
                marginTop: 6,
              }}
            >
              {transactions.length} transações no total
            </p>
          </div>

          <div style={{ display: "flex", gap: 12, alignItems: "center" }}>
            <button
              onClick={handleRefresh}
              className="btn-cartoon btn-cartoon-ghost btn-cartoon-sm"
              disabled={refreshing}
              title="Atualizar"
            >
              <RefreshCw size={14} style={{ animation: refreshing ? "spin 1s linear infinite" : "none" }} />
              {refreshing ? "Atualizando..." : "Atualizar"}
            </button>

            <button
              onClick={() => setImportOpen(true)}
              className="btn-cartoon btn-cartoon-ghost btn-cartoon-sm"
            >
              <Upload size={14} />
              Importar PDF
            </button>

            <button onClick={handleOpenNew} className="btn-cartoon btn-cartoon-primary">
              <Plus size={16} />
              Nova transação
            </button>
          </div>
        </div>

        {/* Cards de resumo */}
        <SummaryCards summary={summary} />

        {/* Secao do extrato */}
        <div
          style={{
            background: "#141414",
            border: "3px solid #050505",
            boxShadow: "0 4px 0 #050505",
          }}
        >
          {/* Header da secao */}
          <div
            style={{
              padding: "20px 24px",
              borderBottom: "2px solid #050505",
              display: "flex",
              alignItems: "center",
              justifyContent: "space-between",
              flexWrap: "wrap",
              gap: 16,
            }}
          >
            <div>
              <h2
                style={{
                  fontFamily: "Montserrat, sans-serif",
                  fontWeight: 800,
                  fontSize: 14,
                  color: "#F5F0E8",
                  textTransform: "uppercase",
                  letterSpacing: "0.06em",
                }}
              >
                Lançamentos
              </h2>
              <p
                style={{
                  fontFamily: "Montserrat, sans-serif",
                  fontWeight: 500,
                  fontSize: 12,
                  color: "rgba(245,240,232,0.3)",
                  marginTop: 2,
                }}
              >
                {filteredTransactions.length} resultado
                {filteredTransactions.length !== 1 ? "s" : ""} com os filtros
                atuais
              </p>
            </div>

            <Filters filters={filters} availableMonths={availableMonths} onChange={setFilters} />
          </div>

          {/* Tabela */}
          <div style={{ padding: 24, paddingTop: 0 }}>
            <div style={{ marginTop: 0 }}>
              <TransactionTable
                transactions={filteredTransactions}
                profiles={profiles}
                currentUserId={user.id}
                onEdit={handleEdit}
                onDelete={(id) => setDeleteId(id)}
              />
            </div>
          </div>
        </div>
      </main>

      {/* Modal de importação */}
      <ImportModal
        open={importOpen}
        onClose={() => setImportOpen(false)}
        onImported={(count) => {
          addToast(`${count} transações importadas com sucesso.`, "success");
          handleRefresh();
          setImportOpen(false);
        }}
      />

      {/* Modal de transação */}
      <TransactionModal
        open={modalOpen}
        onClose={handleCloseModal}
        onSave={handleSave}
        editingTransaction={editingTx}
      />

      {/* Modal de confirmacao de delete */}
      <DeleteConfirmModal
        open={!!deleteId}
        onClose={() => setDeleteId(null)}
        onConfirm={handleDeleteConfirm}
        loading={deleteLoading}
      />

      {/* Toasts */}
      <ToastContainer toasts={toasts} onRemove={removeToast} />

      {/* CSS inline para spin animation */}
      <style>{`
        @keyframes spin {
          from { transform: rotate(0deg); }
          to { transform: rotate(360deg); }
        }
      `}</style>
    </div>
  );
}
