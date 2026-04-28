"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { createClient } from "@/lib/supabase/client";
import { LogIn, UserPlus, AlertCircle, CheckCircle } from "lucide-react";

export default function LoginPage() {
  const router = useRouter();
  const supabase = createClient();

  const [mode, setMode] = useState<"login" | "register">("login");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [name, setName] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [success, setSuccess] = useState<string | null>(null);

  async function handleLogin(e: React.FormEvent) {
    e.preventDefault();
    setError(null);
    setLoading(true);

    const { error } = await supabase.auth.signInWithPassword({ email, password });

    if (error) {
      setError("Email ou senha incorretos. Tente novamente.");
      setLoading(false);
      return;
    }

    router.push("/dashboard");
    router.refresh();
  }

  async function handleRegister(e: React.FormEvent) {
    e.preventDefault();
    setError(null);
    setLoading(true);

    const { error } = await supabase.auth.signUp({
      email,
      password,
      options: { data: { display_name: name } },
    });

    if (error) {
      setError(error.message);
      setLoading(false);
      return;
    }

    setSuccess("Conta criada! Ja pode entrar.");
    setMode("login");
    setPassword("");
    setLoading(false);
  }

  return (
    <div className="min-h-screen grid-overlay" style={{ background: "#0d0d0d" }}>
      {/* Aurora orbs */}
      <div
        className="aurora-orb"
        style={{
          width: 600,
          height: 600,
          top: -200,
          left: "50%",
          transform: "translateX(-50%)",
        }}
      />
      <div
        className="aurora-orb"
        style={{
          width: 300,
          height: 300,
          bottom: 100,
          right: 100,
        }}
      />

      <div className="relative z-10 min-h-screen flex items-center justify-center px-4">
        <div className="w-full max-w-md animate-fade-in">
          {/* Logo */}
          <div className="text-center mb-10">
            <div
              className="inline-flex items-center justify-center w-16 h-16 mb-4"
              style={{
                background: "#FF6600",
                border: "3px solid #050505",
                boxShadow: "0 4px 0 #050505",
              }}
            >
              <span style={{ fontSize: 28, fontWeight: 900, color: "#050505" }}>T</span>
            </div>
            <h1
              style={{
                fontFamily: "Montserrat, sans-serif",
                fontWeight: 900,
                fontSize: 22,
                color: "#F5F0E8",
                letterSpacing: "0.08em",
                textTransform: "uppercase",
              }}
            >
              TRIFORCE AUTO
            </h1>
            <p
              style={{
                fontFamily: "Montserrat, sans-serif",
                fontWeight: 500,
                fontSize: 12,
                color: "#FF6600",
                letterSpacing: "0.12em",
                textTransform: "uppercase",
                marginTop: 4,
              }}
            >
              prestação de Contas
            </p>
          </div>

          {/* Card */}
          <div className="card-neo" style={{ padding: 36, background: "#141414" }}>
            <h2 style={{ fontFamily: "Montserrat, sans-serif", fontWeight: 800, fontSize: 18, color: "#F5F0E8", marginBottom: 24 }}>
              {mode === "login" ? "Entrar na plataforma" : "Criar conta"}
            </h2>

            {error && (
              <div className="animate-fade-in" style={{ display: "flex", alignItems: "center", gap: 8, padding: "10px 14px", background: "rgba(220,38,38,0.1)", border: "2px solid #dc2626", marginBottom: 20, color: "#fca5a5", fontSize: 13, fontWeight: 600 }}>
                <AlertCircle size={16} /> {error}
              </div>
            )}

            {success && (
              <div className="animate-fade-in" style={{ display: "flex", alignItems: "center", gap: 8, padding: "10px 14px", background: "rgba(34,197,94,0.1)", border: "2px solid #22c55e", marginBottom: 20, color: "#86efac", fontSize: 13, fontWeight: 600 }}>
                <CheckCircle size={16} /> {success}
              </div>
            )}

            <form onSubmit={mode === "login" ? handleLogin : handleRegister} style={{ display: "flex", flexDirection: "column", gap: 16 }}>
              {mode === "register" && (
                <div>
                  <label style={{ display: "block", fontFamily: "Montserrat, sans-serif", fontWeight: 700, fontSize: 12, color: "#F5F0E8", textTransform: "uppercase", letterSpacing: "0.06em", marginBottom: 6 }}>Nome</label>
                  <input type="text" className="input-neo" placeholder="Seu nome" value={name} onChange={(e) => setName(e.target.value)} required />
                </div>
              )}

              <div>
                <label style={{ display: "block", fontFamily: "Montserrat, sans-serif", fontWeight: 700, fontSize: 12, color: "#F5F0E8", textTransform: "uppercase", letterSpacing: "0.06em", marginBottom: 6 }}>Email</label>
                <input id="email" type="email" className="input-neo" placeholder="seu@email.com" value={email} onChange={(e) => setEmail(e.target.value)} required autoComplete="email" />
              </div>

              <div>
                <label style={{ display: "block", fontFamily: "Montserrat, sans-serif", fontWeight: 700, fontSize: 12, color: "#F5F0E8", textTransform: "uppercase", letterSpacing: "0.06em", marginBottom: 6 }}>Senha</label>
                <input id="password" type="password" className="input-neo" placeholder="••••••••" value={password} onChange={(e) => setPassword(e.target.value)} required autoComplete={mode === "login" ? "current-password" : "new-password"} />
              </div>

              <button type="submit" className="btn-cartoon btn-cartoon-primary" disabled={loading} style={{ marginTop: 8, width: "100%", opacity: loading ? 0.7 : 1 }}>
                {mode === "login" ? <LogIn size={16} /> : <UserPlus size={16} />}
                {loading ? (mode === "login" ? "Entrando..." : "Criando...") : (mode === "login" ? "Entrar" : "Criar conta")}
              </button>
            </form>

            <div style={{ textAlign: "center", marginTop: 20 }}>
              <button
                onClick={() => { setMode(mode === "login" ? "register" : "login"); setError(null); setSuccess(null); }}
                style={{ background: "none", border: "none", cursor: "pointer", fontFamily: "Montserrat, sans-serif", fontWeight: 600, fontSize: 12, color: "#FF6600", textDecoration: "underline" }}
              >
                {mode === "login" ? "Criar conta nova" : "Ja tenho conta, entrar"}
              </button>
            </div>
          </div>

          <p style={{ textAlign: "center", fontSize: 11, color: "rgba(245,240,232,0.3)", marginTop: 24, fontFamily: "Montserrat, sans-serif" }}>
            Acesso restrito a membros da Triforce Auto
          </p>
        </div>
      </div>
    </div>
  );
}
