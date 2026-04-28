import { NextRequest, NextResponse } from "next/server";
import { createClient } from "@/lib/supabase/server";
import { parseMercadoPagoPDF } from "@/lib/parseMercadoPago";

export async function POST(req: NextRequest) {
  const supabase = await createClient();

  const { data: { user } } = await supabase.auth.getUser();
  if (!user) {
    return NextResponse.json({ error: "Não autenticado" }, { status: 401 });
  }

  const formData = await req.formData();
  const file = formData.get("pdf") as File | null;

  if (!file) {
    return NextResponse.json({ error: "Nenhum arquivo enviado" }, { status: 400 });
  }

  const arrayBuffer = await file.arrayBuffer();
  const buffer = Buffer.from(arrayBuffer);

  let pdfText: string;
  try {
    const { PDFParse } = await import("pdf-parse");
    const parser = new PDFParse({ data: buffer });
    const result = await parser.getText();
    pdfText = result.text;
  } catch (e) {
    console.error("pdf-parse error:", e);
    return NextResponse.json({ error: "Erro ao ler o PDF" }, { status: 422 });
  }

  const transactions = parseMercadoPagoPDF(pdfText);

  if (transactions.length === 0) {
    return NextResponse.json({ error: "Nenhuma transação encontrada no PDF" }, { status: 422 });
  }

  // Inserir no Supabase (ignorar duplicados pelo operation_id)
  const rows = transactions.map((tx) => ({
    user_id: user.id,
    date: tx.date,
    description: tx.description,
    amount: tx.amount,
    category: tx.category,
  }));

  const { data, error } = await supabase
    .from("transactions")
    .insert(rows)
    .select();

  if (error) {
    return NextResponse.json({ error: error.message }, { status: 500 });
  }

  return NextResponse.json({
    imported: data.length,
    transactions: data,
  });
}
