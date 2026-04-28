import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Extrato | Triforce Auto",
  description: "Plataforma de prestação de Contas - Triforce Auto",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="pt-BR">
      <body>{children}</body>
    </html>
  );
}
