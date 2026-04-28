"use client";

import { User } from "@supabase/supabase-js";
import { Profile } from "@/types";
import { LogOut } from "lucide-react";
import { createClient } from "@/lib/supabase/client";
import { useRouter } from "next/navigation";

interface HeaderProps {
  user: User;
  profile: Profile | null;
}

export default function Header({ user, profile }: HeaderProps) {
  const router = useRouter();
  const supabase = createClient();

  const displayName =
    profile?.display_name ||
    user.email?.split("@")[0] ||
    "Usuario";

  async function handleSignOut() {
    await supabase.auth.signOut();
    router.push("/login");
    router.refresh();
  }

  return (
    <header
      style={{
        background: "#141414",
        borderBottom: "3px solid #050505",
        position: "sticky",
        top: 0,
        zIndex: 100,
      }}
    >
      <div
        style={{
          maxWidth: 1400,
          margin: "0 auto",
          padding: "0 32px",
          height: 64,
          display: "flex",
          alignItems: "center",
          justifyContent: "space-between",
        }}
      >
        {/* Logo + nome */}
        <div style={{ display: "flex", alignItems: "center", gap: 12 }}>
          <div
            style={{
              width: 36,
              height: 36,
              background: "#FF6600",
              border: "2px solid #050505",
              boxShadow: "0 3px 0 #050505",
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              flexShrink: 0,
            }}
          >
            <span style={{ fontSize: 16, fontWeight: 900, color: "#050505" }}>T</span>
          </div>
          <div>
            <div
              style={{
                fontFamily: "Montserrat, sans-serif",
                fontWeight: 900,
                fontSize: 14,
                color: "#F5F0E8",
                letterSpacing: "0.06em",
                textTransform: "uppercase",
                lineHeight: 1,
              }}
            >
              TRIFORCE AUTO
            </div>
            <div
              style={{
                fontFamily: "Montserrat, sans-serif",
                fontWeight: 500,
                fontSize: 10,
                color: "#FF6600",
                letterSpacing: "0.1em",
                textTransform: "uppercase",
                marginTop: 2,
              }}
            >
              prestação de Contas
            </div>
          </div>
        </div>

        {/* Separador */}
        <div
          style={{
            flex: 1,
            height: 1,
            background: "rgba(245,240,232,0.06)",
            margin: "0 32px",
          }}
        />

        {/* Usuario + logout */}
        <div style={{ display: "flex", alignItems: "center", gap: 16 }}>
          <div style={{ textAlign: "right" }}>
            <div
              style={{
                fontFamily: "Montserrat, sans-serif",
                fontWeight: 700,
                fontSize: 13,
                color: "#F5F0E8",
              }}
            >
              {displayName}
            </div>
            <div
              style={{
                fontFamily: "Montserrat, sans-serif",
                fontWeight: 500,
                fontSize: 11,
                color: "rgba(245,240,232,0.4)",
              }}
            >
              {user.email}
            </div>
          </div>

          <button
            onClick={handleSignOut}
            className="btn-cartoon btn-cartoon-ghost btn-cartoon-sm"
            title="Sair"
          >
            <LogOut size={14} />
            Sair
          </button>
        </div>
      </div>
    </header>
  );
}
