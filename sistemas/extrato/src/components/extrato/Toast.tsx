"use client";

import { useEffect, useState } from "react";
import { CheckCircle, XCircle, X } from "lucide-react";

export type ToastType = "success" | "error";

export interface ToastData {
  id: string;
  message: string;
  type: ToastType;
}

interface ToastItemProps {
  toast: ToastData;
  onRemove: (id: string) => void;
}

function ToastItem({ toast, onRemove }: ToastItemProps) {
  useEffect(() => {
    const timer = setTimeout(() => onRemove(toast.id), 3500);
    return () => clearTimeout(timer);
  }, [toast.id, onRemove]);

  const isSuccess = toast.type === "success";

  return (
    <div
      className="animate-slide-in"
      style={{
        display: "flex",
        alignItems: "center",
        gap: 10,
        padding: "12px 16px",
        background: "#141414",
        border: `3px solid ${isSuccess ? "#16a34a" : "#dc2626"}`,
        boxShadow: `0 4px 0 #050505`,
        minWidth: 300,
        maxWidth: 420,
        fontFamily: "Montserrat, sans-serif",
      }}
    >
      {isSuccess ? (
        <CheckCircle size={18} color="#4ade80" style={{ flexShrink: 0 }} />
      ) : (
        <XCircle size={18} color="#f87171" style={{ flexShrink: 0 }} />
      )}

      <span
        style={{
          flex: 1,
          fontSize: 13,
          fontWeight: 600,
          color: "#F5F0E8",
        }}
      >
        {toast.message}
      </span>

      <button
        onClick={() => onRemove(toast.id)}
        style={{
          background: "transparent",
          border: "none",
          cursor: "pointer",
          color: "rgba(245,240,232,0.4)",
          display: "flex",
          alignItems: "center",
          padding: 2,
          flexShrink: 0,
        }}
      >
        <X size={14} />
      </button>
    </div>
  );
}

interface ToastContainerProps {
  toasts: ToastData[];
  onRemove: (id: string) => void;
}

export function ToastContainer({ toasts, onRemove }: ToastContainerProps) {
  return (
    <div
      style={{
        position: "fixed",
        bottom: 32,
        right: 32,
        display: "flex",
        flexDirection: "column",
        gap: 10,
        zIndex: 500,
      }}
    >
      {toasts.map((t) => (
        <ToastItem key={t.id} toast={t} onRemove={onRemove} />
      ))}
    </div>
  );
}
