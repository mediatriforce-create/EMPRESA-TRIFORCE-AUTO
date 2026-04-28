"use client";

import { useEffect, useState } from "react";
import { Transaction, TransactionFormData } from "@/types";
import { getTodayISO, CATEGORIES } from "@/lib/utils";
import { X, ChevronDown } from "lucide-react";

interface TransactionModalProps {
  open: boolean;
  onClose: () => void;
  onSave: (data: TransactionFormData) => Promise<void>;
  editingTransaction?: Transaction | null;
}

const EMPTY_FORM: TransactionFormData = {
  date: "",
  description: "",
  amount: "",
  category: "",
  type: "income",
};

export default function TransactionModal({
  open,
  onClose,
  onSave,
  editingTransaction,
}: TransactionModalProps) {
  const [form, setForm] = useState<TransactionFormData>(EMPTY_FORM);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (editingTransaction) {
      const amount = Math.abs(editingTransaction.amount);
      setForm({
        date: editingTransaction.date,
        description: editingTransaction.description,
        amount: String(amount),
        category: editingTransaction.category || "",
        type: editingTransaction.amount >= 0 ? "income" : "expense",
      });
    } else {
      setForm({ ...EMPTY_FORM, date: getTodayISO() });
    }
    setError(null);
  }, [editingTransaction, open]);

  // Fechar com ESC
  useEffect(() => {
    if (!open) return;
    function onKey(e: KeyboardEvent) {
      if (e.key === "Escape") onClose();
    }
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [open, onClose]);

  if (!open) return null;

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    setError(null);

    if (!form.date || !form.description || !form.amount) {
      setError("Preencha data, descrição e valor.");
      return;
    }

    const numericAmount = parseFloat(form.amount.replace(",", "."));
    if (isNaN(numericAmount) || numericAmount <= 0) {
      setError("Valor deve ser um número positivo.");
      return;
    }

    setLoading(true);
    try {
      await onSave(form);
      onClose();
    } catch (err: unknown) {
      setError(err instanceof Error ? err.message : "Erro ao salvar. Tente novamente.");
    } finally {
      setLoading(false);
    }
  }

  const isEditing = !!editingTransaction;

  return (
    <>
      {/* Overlay */}
      <div
        onClick={onClose}
        style={{
          position: "fixed",
          inset: 0,
          background: "rgba(5,5,5,0.85)",
          zIndex: 200,
          backdropFilter: "blur(4px)",
        }}
      />

      {/* Modal */}
      <div
        className="animate-slide-in"
        style={{
          position: "fixed",
          top: "50%",
          left: "50%",
          transform: "translate(-50%, -50%)",
          zIndex: 201,
          width: 520,
          maxWidth: "calc(100vw - 40px)",
          maxHeight: "calc(100vh - 40px)",
          overflowY: "auto",
          background: "#141414",
          border: "3px solid #050505",
          boxShadow: "0 8px 0 #050505",
        }}
      >
        {/* Header do modal */}
        <div
          style={{
            padding: "20px 28px",
            borderBottom: "2px solid #050505",
            display: "flex",
            alignItems: "center",
            justifyContent: "space-between",
          }}
        >
          <div>
            <h2
              style={{
                fontFamily: "Montserrat, sans-serif",
                fontWeight: 900,
                fontSize: 16,
                color: "#F5F0E8",
                textTransform: "uppercase",
                letterSpacing: "0.04em",
              }}
            >
              {isEditing ? "Editar transação" : "Nova transação"}
            </h2>
            {isEditing && (
              <p
                style={{
                  fontFamily: "Montserrat, sans-serif",
                  fontWeight: 500,
                  fontSize: 11,
                  color: "rgba(245,240,232,0.4)",
                  marginTop: 2,
                }}
              >
                Editando lançamento existente
              </p>
            )}
          </div>
          <button
            onClick={onClose}
            style={{
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              width: 32,
              height: 32,
              background: "transparent",
              border: "2px solid #050505",
              boxShadow: "0 3px 0 #050505",
              cursor: "pointer",
              color: "rgba(245,240,232,0.5)",
              transition: "transform 0.1s, box-shadow 0.1s, color 0.1s",
            }}
            onMouseEnter={(e) => {
              const el = e.currentTarget;
              el.style.transform = "translateY(-2px)";
              el.style.boxShadow = "0 5px 0 #050505";
              el.style.color = "#F5F0E8";
            }}
            onMouseLeave={(e) => {
              const el = e.currentTarget;
              el.style.transform = "translateY(0)";
              el.style.boxShadow = "0 3px 0 #050505";
              el.style.color = "rgba(245,240,232,0.5)";
            }}
          >
            <X size={15} />
          </button>
        </div>

        {/* Corpo do form */}
        <form onSubmit={handleSubmit} style={{ padding: 28 }}>
          {error && (
            <div
              className="animate-fade-in"
              style={{
                padding: "10px 14px",
                background: "rgba(220,38,38,0.1)",
                border: "2px solid #dc2626",
                marginBottom: 20,
                color: "#fca5a5",
                fontSize: 12,
                fontWeight: 600,
                fontFamily: "Montserrat, sans-serif",
              }}
            >
              {error}
            </div>
          )}

          {/* Tipo: entrada ou saída */}
          <div style={{ marginBottom: 20 }}>
            <label
              style={{
                display: "block",
                fontFamily: "Montserrat, sans-serif",
                fontWeight: 700,
                fontSize: 11,
                color: "rgba(245,240,232,0.5)",
                textTransform: "uppercase",
                letterSpacing: "0.08em",
                marginBottom: 8,
              }}
            >
              Tipo
            </label>
            <div style={{ display: "flex", gap: 10 }}>
              {(["income", "expense"] as const).map((t) => (
                <button
                  key={t}
                  type="button"
                  onClick={() => setForm({ ...form, type: t })}
                  style={{
                    flex: 1,
                    padding: "10px 16px",
                    fontFamily: "Montserrat, sans-serif",
                    fontWeight: 700,
                    fontSize: 13,
                    border: "3px solid #050505",
                    boxShadow:
                      form.type === t ? "0 4px 0 #050505" : "0 2px 0 #050505",
                    cursor: "pointer",
                    transition: "all 0.1s ease",
                    background:
                      form.type === t
                        ? t === "income"
                          ? "#16a34a"
                          : "#dc2626"
                        : "#0d0d0d",
                    color:
                      form.type === t ? "#F5F0E8" : "rgba(245,240,232,0.4)",
                    transform:
                      form.type === t ? "translateY(-2px)" : "translateY(0)",
                  }}
                >
                  {t === "income" ? "Entrada (+)" : "Saída (-)"}
                </button>
              ))}
            </div>
          </div>

          {/* Grid: data + valor */}
          <div
            style={{
              display: "grid",
              gridTemplateColumns: "1fr 1fr",
              gap: 16,
              marginBottom: 16,
            }}
          >
            <div>
              <label
                style={{
                  display: "block",
                  fontFamily: "Montserrat, sans-serif",
                  fontWeight: 700,
                  fontSize: 11,
                  color: "rgba(245,240,232,0.5)",
                  textTransform: "uppercase",
                  letterSpacing: "0.08em",
                  marginBottom: 6,
                }}
              >
                Data
              </label>
              <input
                type="date"
                className="input-neo"
                value={form.date}
                onChange={(e) => setForm({ ...form, date: e.target.value })}
                required
              />
            </div>

            <div>
              <label
                style={{
                  display: "block",
                  fontFamily: "Montserrat, sans-serif",
                  fontWeight: 700,
                  fontSize: 11,
                  color: "rgba(245,240,232,0.5)",
                  textTransform: "uppercase",
                  letterSpacing: "0.08em",
                  marginBottom: 6,
                }}
              >
                Valor (R$)
              </label>
              <input
                type="number"
                className="input-neo"
                placeholder="0,00"
                value={form.amount}
                onChange={(e) => setForm({ ...form, amount: e.target.value })}
                min="0.01"
                step="0.01"
                required
              />
            </div>
          </div>

          {/* descrição */}
          <div style={{ marginBottom: 16 }}>
            <label
              style={{
                display: "block",
                fontFamily: "Montserrat, sans-serif",
                fontWeight: 700,
                fontSize: 11,
                color: "rgba(245,240,232,0.5)",
                textTransform: "uppercase",
                letterSpacing: "0.08em",
                marginBottom: 6,
              }}
            >
              descrição
            </label>
            <input
              type="text"
              className="input-neo"
              placeholder="Ex: Pagamento fornecedor XYZ"
              value={form.description}
              onChange={(e) => setForm({ ...form, description: e.target.value })}
              maxLength={200}
              required
            />
          </div>

          {/* Categoria */}
          <div style={{ marginBottom: 28, position: "relative" }}>
            <label
              style={{
                display: "block",
                fontFamily: "Montserrat, sans-serif",
                fontWeight: 700,
                fontSize: 11,
                color: "rgba(245,240,232,0.5)",
                textTransform: "uppercase",
                letterSpacing: "0.08em",
                marginBottom: 6,
              }}
            >
              Categoria (opcional)
            </label>
            <select
              className="select-neo"
              value={form.category}
              onChange={(e) => setForm({ ...form, category: e.target.value })}
              style={{ paddingRight: 36, width: "100%" }}
            >
              <option value="">Sem categoria</option>
              {CATEGORIES.map((cat) => (
                <option key={cat} value={cat}>
                  {cat}
                </option>
              ))}
            </select>
            <ChevronDown
              size={14}
              style={{
                position: "absolute",
                right: 12,
                bottom: 14,
                color: "rgba(245,240,232,0.5)",
                pointerEvents: "none",
              }}
            />
          </div>

          {/* Ações */}
          <div style={{ display: "flex", gap: 12 }}>
            <button
              type="button"
              onClick={onClose}
              className="btn-cartoon btn-cartoon-ghost"
              style={{ flex: 1 }}
            >
              Cancelar
            </button>
            <button
              type="submit"
              className="btn-cartoon btn-cartoon-primary"
              disabled={loading}
              style={{ flex: 1, opacity: loading ? 0.7 : 1 }}
            >
              {loading
                ? "Salvando..."
                : isEditing
                ? "Salvar alterações"
                : "Lançar transação"}
            </button>
          </div>
        </form>
      </div>
    </>
  );
}
