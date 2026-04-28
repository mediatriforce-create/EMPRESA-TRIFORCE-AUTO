"use client";

import { useState, useRef } from "react";
import { Upload, X, FileText, CheckCircle, AlertCircle } from "lucide-react";

interface ImportModalProps {
  open: boolean;
  onClose: () => void;
  onImported: (count: number) => void;
}

export default function ImportModal({ open, onClose, onImported }: ImportModalProps) {
  const [file, setFile] = useState<File | null>(null);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<{ ok: boolean; message: string } | null>(null);
  const inputRef = useRef<HTMLInputElement>(null);

  if (!open) return null;

  function handleDrop(e: React.DragEvent) {
    e.preventDefault();
    const f = e.dataTransfer.files[0];
    if (f?.type === "application/pdf") setFile(f);
  }

  async function handleImport() {
    if (!file) return;
    setLoading(true);
    setResult(null);

    const form = new FormData();
    form.append("pdf", file);

    const res = await fetch("/api/import-extrato", { method: "POST", body: form });

    let json: { error?: string; imported?: number } = {};
    try { json = await res.json(); } catch { /* empty response */ }

    if (!res.ok) {
      setResult({ ok: false, message: json.error || "Erro interno no servidor" });
    } else {
      setResult({ ok: true, message: `${json.imported} transações importadas com sucesso.` });
      onImported(json.imported ?? 0);
    }

    setLoading(false);
  }

  function handleClose() {
    setFile(null);
    setResult(null);
    onClose();
  }

  return (
    <div
      style={{
        position: "fixed", inset: 0, zIndex: 1000,
        background: "rgba(5,5,5,0.85)",
        display: "flex", alignItems: "center", justifyContent: "center",
      }}
      onClick={(e) => { if (e.target === e.currentTarget) handleClose(); }}
    >
      <div
        style={{
          background: "#141414",
          border: "3px solid #050505",
          boxShadow: "0 6px 0 #050505",
          width: "100%",
          maxWidth: 480,
          padding: 32,
        }}
      >
        {/* Header */}
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 24 }}>
          <h2 style={{ fontFamily: "Montserrat, sans-serif", fontWeight: 800, fontSize: 16, color: "#F5F0E8", textTransform: "uppercase", letterSpacing: "0.06em" }}>
            Importar Extrato
          </h2>
          <button onClick={handleClose} style={{ background: "none", border: "none", cursor: "pointer", color: "rgba(245,240,232,0.5)" }}>
            <X size={20} />
          </button>
        </div>

        <p style={{ fontFamily: "Montserrat, sans-serif", fontSize: 12, color: "rgba(245,240,232,0.5)", marginBottom: 20 }}>
          Envie o PDF do extrato Mercado Pago. As transações serão importadas e categorizadas automaticamente.
        </p>

        {/* Drop zone */}
        <div
          onClick={() => inputRef.current?.click()}
          onDrop={handleDrop}
          onDragOver={(e) => e.preventDefault()}
          style={{
            border: file ? "3px solid #FF6600" : "3px dashed rgba(245,240,232,0.2)",
            background: file ? "rgba(255,102,0,0.06)" : "rgba(245,240,232,0.02)",
            padding: "32px 24px",
            textAlign: "center",
            cursor: "pointer",
            marginBottom: 20,
            transition: "all 0.15s",
          }}
        >
          <input
            ref={inputRef}
            type="file"
            accept="application/pdf"
            style={{ display: "none" }}
            onChange={(e) => setFile(e.target.files?.[0] || null)}
          />
          {file ? (
            <div style={{ display: "flex", alignItems: "center", justifyContent: "center", gap: 10 }}>
              <FileText size={20} color="#FF6600" />
              <span style={{ fontFamily: "Montserrat, sans-serif", fontWeight: 700, fontSize: 13, color: "#FF6600" }}>
                {file.name}
              </span>
            </div>
          ) : (
            <>
              <Upload size={28} color="rgba(245,240,232,0.3)" style={{ margin: "0 auto 10px" }} />
              <p style={{ fontFamily: "Montserrat, sans-serif", fontWeight: 700, fontSize: 13, color: "rgba(245,240,232,0.4)" }}>
                Clique ou arraste o PDF aqui
              </p>
              <p style={{ fontFamily: "Montserrat, sans-serif", fontSize: 11, color: "rgba(245,240,232,0.2)", marginTop: 4 }}>
                Extrato Mercado Pago (.pdf)
              </p>
            </>
          )}
        </div>

        {/* Resultado */}
        {result && (
          <div
            style={{
              display: "flex", alignItems: "center", gap: 8,
              padding: "10px 14px",
              background: result.ok ? "rgba(34,197,94,0.1)" : "rgba(220,38,38,0.1)",
              border: `2px solid ${result.ok ? "#22c55e" : "#dc2626"}`,
              marginBottom: 16,
              color: result.ok ? "#86efac" : "#fca5a5",
              fontSize: 13,
              fontFamily: "Montserrat, sans-serif",
              fontWeight: 600,
            }}
          >
            {result.ok ? <CheckCircle size={16} /> : <AlertCircle size={16} />}
            {result.message}
          </div>
        )}

        {/* Botoes */}
        <div style={{ display: "flex", gap: 12 }}>
          <button onClick={handleClose} className="btn-cartoon btn-cartoon-ghost" style={{ flex: 1 }}>
            {result?.ok ? "Fechar" : "Cancelar"}
          </button>
          {!result?.ok && (
            <button
              onClick={handleImport}
              className="btn-cartoon btn-cartoon-primary"
              disabled={!file || loading}
              style={{ flex: 1, opacity: !file || loading ? 0.6 : 1 }}
            >
              <Upload size={14} />
              {loading ? "Importando..." : "Importar"}
            </button>
          )}
        </div>
      </div>
    </div>
  );
}
