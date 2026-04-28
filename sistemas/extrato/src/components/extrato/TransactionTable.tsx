"use client";

import { Transaction, Profile } from "@/types";
import { formatCurrency, formatDate } from "@/lib/utils";
import { Pencil, Trash2 } from "lucide-react";

interface TransactionTableProps {
  transactions: Transaction[];
  profiles: Profile[];
  currentUserId: string;
  onEdit: (transaction: Transaction) => void;
  onDelete: (id: string) => void;
}

export default function TransactionTable({
  transactions,
  profiles,
  currentUserId,
  onEdit,
  onDelete,
}: TransactionTableProps) {
  function getProfileName(userId: string): string {
    const p = profiles.find((p) => p.id === userId);
    return p?.display_name || "Usuario";
  }

  if (transactions.length === 0) {
    return (
      <div
        style={{
          padding: "60px 40px",
          textAlign: "center",
          background: "#141414",
          border: "3px solid #050505",
          boxShadow: "0 4px 0 #050505",
        }}
      >
        <div
          style={{
            fontSize: 40,
            marginBottom: 12,
            opacity: 0.3,
          }}
        >
          📋
        </div>
        <p
          style={{
            fontFamily: "Montserrat, sans-serif",
            fontWeight: 700,
            fontSize: 14,
            color: "rgba(245,240,232,0.4)",
            textTransform: "uppercase",
            letterSpacing: "0.06em",
          }}
        >
          Nenhuma transação encontrada
        </p>
        <p
          style={{
            fontFamily: "Montserrat, sans-serif",
            fontWeight: 500,
            fontSize: 12,
            color: "rgba(245,240,232,0.2)",
            marginTop: 6,
          }}
        >
          Ajuste os filtros ou lance uma nova transação
        </p>
      </div>
    );
  }

  return (
    <div
      style={{
        background: "#141414",
        border: "3px solid #050505",
        boxShadow: "0 4px 0 #050505",
        overflow: "hidden",
      }}
    >
      <table
        style={{
          width: "100%",
          borderCollapse: "collapse",
          fontFamily: "Montserrat, sans-serif",
        }}
      >
        <thead>
          <tr style={{ background: "#0d0d0d" }}>
            {["Data", "descrição", "Categoria", "lançado por", "Valor", "Ações"].map(
              (header, i) => (
                <th
                  key={i}
                  style={{
                    padding: "14px 20px",
                    textAlign: i >= 4 ? "right" : "left",
                    fontWeight: 800,
                    fontSize: 11,
                    color: "rgba(245,240,232,0.5)",
                    textTransform: "uppercase",
                    letterSpacing: "0.08em",
                    borderBottom: "2px solid #050505",
                    whiteSpace: "nowrap",
                  }}
                >
                  {header}
                </th>
              )
            )}
          </tr>
        </thead>
        <tbody>
          {transactions.map((tx, i) => {
            const isOwner = tx.user_id === currentUserId;
            const isIncome = tx.amount > 0;

            return (
              <tr
                key={tx.id}
                className="animate-fade-in"
                style={{
                  borderBottom: "1px solid rgba(5,5,5,0.8)",
                  transition: "background 0.15s ease",
                  animationDelay: `${i * 0.03}s`,
                }}
                onMouseEnter={(e) => {
                  (e.currentTarget as HTMLTableRowElement).style.background =
                    "rgba(255,102,0,0.04)";
                }}
                onMouseLeave={(e) => {
                  (e.currentTarget as HTMLTableRowElement).style.background =
                    "transparent";
                }}
              >
                {/* Data */}
                <td
                  style={{
                    padding: "16px 20px",
                    fontSize: 13,
                    fontWeight: 600,
                    color: "rgba(245,240,232,0.6)",
                    whiteSpace: "nowrap",
                  }}
                >
                  {formatDate(tx.date)}
                </td>

                {/* descrição */}
                <td
                  style={{
                    padding: "16px 20px",
                    fontSize: 13,
                    fontWeight: 600,
                    color: "#F5F0E8",
                    maxWidth: 320,
                  }}
                >
                  <div
                    style={{
                      overflow: "hidden",
                      textOverflow: "ellipsis",
                      whiteSpace: "nowrap",
                    }}
                  >
                    {tx.description}
                  </div>
                </td>

                {/* Categoria */}
                <td style={{ padding: "16px 20px" }}>
                  {tx.category ? (
                    <span
                      style={{
                        display: "inline-flex",
                        alignItems: "center",
                        padding: "2px 10px",
                        background: "rgba(255,102,0,0.1)",
                        border: "1px solid rgba(255,102,0,0.3)",
                        fontSize: 11,
                        fontWeight: 700,
                        color: "#FF6600",
                        letterSpacing: "0.04em",
                        textTransform: "uppercase",
                        whiteSpace: "nowrap",
                      }}
                    >
                      {tx.category}
                    </span>
                  ) : (
                    <span
                      style={{
                        fontSize: 12,
                        color: "rgba(245,240,232,0.2)",
                        fontStyle: "italic",
                      }}
                    >
                      sem categoria
                    </span>
                  )}
                </td>

                {/* lançado por */}
                <td
                  style={{
                    padding: "16px 20px",
                    fontSize: 12,
                    fontWeight: 600,
                    color: "rgba(245,240,232,0.4)",
                    whiteSpace: "nowrap",
                  }}
                >
                  {getProfileName(tx.user_id)}
                  {isOwner && (
                    <span
                      style={{
                        marginLeft: 6,
                        fontSize: 10,
                        color: "#FF6600",
                        fontWeight: 700,
                      }}
                    >
                      (voce)
                    </span>
                  )}
                </td>

                {/* Valor */}
                <td
                  style={{
                    padding: "16px 20px",
                    textAlign: "right",
                    whiteSpace: "nowrap",
                  }}
                >
                  <span
                    style={{
                      fontFamily: "Montserrat, sans-serif",
                      fontWeight: 900,
                      fontSize: 15,
                      color: isIncome ? "#4ade80" : "#f87171",
                      letterSpacing: "-0.01em",
                    }}
                  >
                    {isIncome ? "+" : ""}
                    {formatCurrency(tx.amount)}
                  </span>
                </td>

                {/* Ações */}
                <td style={{ padding: "16px 20px", textAlign: "right" }}>
                  <div
                    style={{
                      display: "flex",
                      alignItems: "center",
                      justifyContent: "flex-end",
                      gap: 8,
                    }}
                  >
                    {isOwner ? (
                      <>
                        <button
                          onClick={() => onEdit(tx)}
                          title="Editar"
                          style={{
                            display: "inline-flex",
                            alignItems: "center",
                            justifyContent: "center",
                            width: 32,
                            height: 32,
                            background: "transparent",
                            border: "2px solid #050505",
                            boxShadow: "0 3px 0 #050505",
                            cursor: "pointer",
                            color: "rgba(245,240,232,0.6)",
                            transition:
                              "transform 0.1s ease, box-shadow 0.1s ease, color 0.1s ease",
                          }}
                          onMouseEnter={(e) => {
                            const el = e.currentTarget as HTMLButtonElement;
                            el.style.transform = "translateY(-2px)";
                            el.style.boxShadow = "0 5px 0 #050505";
                            el.style.color = "#F5F0E8";
                          }}
                          onMouseLeave={(e) => {
                            const el = e.currentTarget as HTMLButtonElement;
                            el.style.transform = "translateY(0)";
                            el.style.boxShadow = "0 3px 0 #050505";
                            el.style.color = "rgba(245,240,232,0.6)";
                          }}
                        >
                          <Pencil size={13} />
                        </button>

                        <button
                          onClick={() => onDelete(tx.id)}
                          title="Deletar"
                          style={{
                            display: "inline-flex",
                            alignItems: "center",
                            justifyContent: "center",
                            width: 32,
                            height: 32,
                            background: "transparent",
                            border: "2px solid #050505",
                            boxShadow: "0 3px 0 #050505",
                            cursor: "pointer",
                            color: "rgba(248,113,113,0.6)",
                            transition:
                              "transform 0.1s ease, box-shadow 0.1s ease, color 0.1s ease",
                          }}
                          onMouseEnter={(e) => {
                            const el = e.currentTarget as HTMLButtonElement;
                            el.style.transform = "translateY(-2px)";
                            el.style.boxShadow = "0 5px 0 #050505";
                            el.style.color = "#f87171";
                          }}
                          onMouseLeave={(e) => {
                            const el = e.currentTarget as HTMLButtonElement;
                            el.style.transform = "translateY(0)";
                            el.style.boxShadow = "0 3px 0 #050505";
                            el.style.color = "rgba(248,113,113,0.6)";
                          }}
                        >
                          <Trash2 size={13} />
                        </button>
                      </>
                    ) : (
                      <span
                        style={{
                          fontSize: 11,
                          color: "rgba(245,240,232,0.15)",
                          fontStyle: "italic",
                        }}
                      >
                        sem permissao
                      </span>
                    )}
                  </div>
                </td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
}
