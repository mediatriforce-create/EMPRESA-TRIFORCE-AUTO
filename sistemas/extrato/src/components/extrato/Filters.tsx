"use client";

import { FilterType, TransactionFilters } from "@/types";
import { formatMonthLabel } from "@/lib/utils";
import { ChevronLeft, ChevronRight, ChevronDown } from "lucide-react";

interface FiltersProps {
  filters: TransactionFilters;
  availableMonths: string[]; // ["2026-04", "2026-03", ...]
  onChange: (filters: TransactionFilters) => void;
}

const typeOptions: { value: FilterType; label: string }[] = [
  { value: "all",     label: "Todos os tipos"   },
  { value: "income",  label: "Apenas entradas"  },
  { value: "expense", label: "Apenas saídas"    },
];

export default function Filters({ filters, availableMonths, onChange }: FiltersProps) {
  const currentIdx = availableMonths.indexOf(filters.selectedMonth);
  const canPrev = currentIdx < availableMonths.length - 1;
  const canNext = currentIdx > 0;

  function goPrev() {
    if (canPrev) onChange({ ...filters, selectedMonth: availableMonths[currentIdx + 1] });
  }

  function goNext() {
    if (canNext) onChange({ ...filters, selectedMonth: availableMonths[currentIdx - 1] });
  }

  const label =
    filters.selectedMonth === "all"
      ? "Todos os meses"
      : formatMonthLabel(filters.selectedMonth);

  const labelCapitalized = label.charAt(0).toUpperCase() + label.slice(1);

  return (
    <div style={{ display: "flex", alignItems: "center", gap: 12, flexWrap: "wrap" }}>

      {/* Navegador de mes */}
      <div style={{ display: "flex", alignItems: "center", gap: 0 }}>
        <button
          onClick={goPrev}
          disabled={!canPrev}
          style={{
            background: "#0d0d0d",
            border: "3px solid #050505",
            borderRight: "none",
            boxShadow: "0 3px 0 #050505",
            padding: "8px 10px",
            cursor: canPrev ? "pointer" : "not-allowed",
            opacity: canPrev ? 1 : 0.3,
            display: "flex",
            alignItems: "center",
          }}
          title="Mes anterior"
        >
          <ChevronLeft size={14} color="#F5F0E8" />
        </button>

        <div
          style={{
            background: "#0d0d0d",
            border: "3px solid #050505",
            boxShadow: "0 3px 0 #050505",
            padding: "8px 20px",
            fontFamily: "Montserrat, sans-serif",
            fontWeight: 800,
            fontSize: 13,
            color: "#FF6600",
            textTransform: "uppercase",
            letterSpacing: "0.06em",
            minWidth: 160,
            textAlign: "center",
            userSelect: "none",
          }}
        >
          {labelCapitalized}
        </div>

        <button
          onClick={goNext}
          disabled={!canNext}
          style={{
            background: "#0d0d0d",
            border: "3px solid #050505",
            borderLeft: "none",
            boxShadow: "0 3px 0 #050505",
            padding: "8px 10px",
            cursor: canNext ? "pointer" : "not-allowed",
            opacity: canNext ? 1 : 0.3,
            display: "flex",
            alignItems: "center",
          }}
          title="Proximo mes"
        >
          <ChevronRight size={14} color="#F5F0E8" />
        </button>
      </div>

      {/* Filtro de tipo */}
      <div style={{ position: "relative" }}>
        <select
          className="select-neo"
          value={filters.type}
          onChange={(e) => onChange({ ...filters, type: e.target.value as FilterType })}
          style={{ paddingRight: 36, minWidth: 170 }}
        >
          {typeOptions.map((opt) => (
            <option key={opt.value} value={opt.value}>{opt.label}</option>
          ))}
        </select>
        <ChevronDown
          size={14}
          style={{ position: "absolute", right: 12, top: "50%", transform: "translateY(-50%)", color: "rgba(245,240,232,0.5)", pointerEvents: "none" }}
        />
      </div>
    </div>
  );
}
