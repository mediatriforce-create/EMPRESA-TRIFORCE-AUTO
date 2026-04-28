"use client";

import { AlertTriangle, X } from "lucide-react";

interface DeleteConfirmModalProps {
  open: boolean;
  onClose: () => void;
  onConfirm: () => Promise<void>;
  loading?: boolean;
}

export default function DeleteConfirmModal({
  open,
  onClose,
  onConfirm,
  loading,
}: DeleteConfirmModalProps) {
  if (!open) return null;

  return (
    <>
      <div
        onClick={onClose}
        style={{
          position: "fixed",
          inset: 0,
          background: "rgba(5,5,5,0.85)",
          zIndex: 300,
          backdropFilter: "blur(4px)",
        }}
      />

      <div
        className="animate-fade-in"
        style={{
          position: "fixed",
          top: "50%",
          left: "50%",
          transform: "translate(-50%, -50%)",
          zIndex: 301,
          width: 400,
          maxWidth: "calc(100vw - 40px)",
          maxHeight: "calc(100vh - 40px)",
          overflowY: "auto",
          background: "#141414",
          border: "3px solid #050505",
          boxShadow: "0 8px 0 #050505",
          padding: 32,
          textAlign: "center",
        }}
      >
        <div
          style={{
            width: 56,
            height: 56,
            background: "rgba(220,38,38,0.1)",
            border: "3px solid #dc2626",
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            margin: "0 auto 20px",
          }}
        >
          <AlertTriangle size={24} color="#f87171" />
        </div>

        <h3
          style={{
            fontFamily: "Montserrat, sans-serif",
            fontWeight: 900,
            fontSize: 16,
            color: "#F5F0E8",
            marginBottom: 8,
            textTransform: "uppercase",
            letterSpacing: "0.04em",
          }}
        >
          Confirmar exclusao
        </h3>

        <p
          style={{
            fontFamily: "Montserrat, sans-serif",
            fontWeight: 500,
            fontSize: 13,
            color: "rgba(245,240,232,0.5)",
            marginBottom: 28,
            lineHeight: 1.5,
          }}
        >
          esta ação não pode ser desfeita. A transação será removida permanentemente.
        </p>

        <div style={{ display: "flex", gap: 12 }}>
          <button
            onClick={onClose}
            className="btn-cartoon btn-cartoon-ghost"
            style={{ flex: 1 }}
            disabled={loading}
          >
            Cancelar
          </button>
          <button
            onClick={onConfirm}
            className="btn-cartoon btn-cartoon-danger"
            style={{ flex: 1, opacity: loading ? 0.7 : 1 }}
            disabled={loading}
          >
            {loading ? "Excluindo..." : "Excluir"}
          </button>
        </div>
      </div>
    </>
  );
}
