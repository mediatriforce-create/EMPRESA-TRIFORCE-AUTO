"use client";

import { SummaryData } from "@/types";
import { formatCurrency } from "@/lib/utils";
import { TrendingUp, TrendingDown, Wallet } from "lucide-react";

interface SummaryCardsProps {
  summary: SummaryData;
}

export default function SummaryCards({ summary }: SummaryCardsProps) {
  const cards = [
    {
      label: "Saldo Atual",
      value: summary.balance,
      icon: <Wallet size={22} />,
      accent:
        summary.balance >= 0
          ? "#FF6600"
          : "#dc2626",
      textColor:
        summary.balance >= 0
          ? "#FF6600"
          : "#f87171",
      bg: "#141414",
    },
    {
      label: "Total Entradas",
      value: summary.totalIncome,
      icon: <TrendingUp size={22} />,
      accent: "#16a34a",
      textColor: "#4ade80",
      bg: "#141414",
    },
    {
      label: "Total Saídas",
      value: summary.totalExpense,
      icon: <TrendingDown size={22} />,
      accent: "#dc2626",
      textColor: "#f87171",
      bg: "#141414",
    },
  ];

  return (
    <div
      style={{
        display: "grid",
        gridTemplateColumns: "1fr 1fr 1fr",
        gap: 20,
        marginBottom: 32,
      }}
    >
      {cards.map((card, i) => (
        <div
          key={i}
          className="animate-fade-in"
          style={{
            background: card.bg,
            border: "3px solid #050505",
            boxShadow: "0 4px 0 #050505",
            padding: "24px 28px",
            animationDelay: `${i * 0.06}s`,
            position: "relative",
            overflow: "hidden",
          }}
        >
          {/* Accent bar lateral */}
          <div
            style={{
              position: "absolute",
              top: 0,
              left: 0,
              width: 4,
              height: "100%",
              background: card.accent,
            }}
          />

          <div
            style={{
              display: "flex",
              alignItems: "flex-start",
              justifyContent: "space-between",
              marginBottom: 12,
            }}
          >
            <span
              style={{
                fontFamily: "Montserrat, sans-serif",
                fontWeight: 700,
                fontSize: 11,
                color: "rgba(245,240,232,0.5)",
                textTransform: "uppercase",
                letterSpacing: "0.08em",
              }}
            >
              {card.label}
            </span>
            <span style={{ color: card.accent, opacity: 0.7 }}>{card.icon}</span>
          </div>

          <div
            style={{
              fontFamily: "Montserrat, sans-serif",
              fontWeight: 900,
              fontSize: 28,
              color: card.textColor,
              letterSpacing: "-0.02em",
              lineHeight: 1,
            }}
          >
            {card.label === "Total Saídas"
              ? formatCurrency(card.value)
              : formatCurrency(card.value)}
          </div>
        </div>
      ))}
    </div>
  );
}
