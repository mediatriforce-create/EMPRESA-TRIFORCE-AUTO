// Parser do extrato PDF Mercado Pago
// Testado com texto real extraido do PDF

export interface ParsedTransaction {
  date: string;        // YYYY-MM-DD
  description: string;
  amount: number;      // positivo = entrada, negativo = saída
  category: string;
  operation_id: string;
}

// ── Regras de categorizacao ────────────────────────────────────
const CATEGORY_RULES: { pattern: RegExp; category: string }[] = [
  { pattern: /rendimentos/i,                    category: "Rendimentos"   },
  { pattern: /pix recebido/i,                   category: "Receita"       },
  { pattern: /pix enviado/i,                    category: "Transferencia" },
  { pattern: /spotify/i,                        category: "Streaming"     },
  { pattern: /netflix/i,                        category: "Streaming"     },
  { pattern: /google/i,                         category: "Servicos"      },
  { pattern: /apple/i,                          category: "Servicos"      },
  { pattern: /amazon/i,                         category: "Servicos"      },
  { pattern: /cantina/i,                        category: "Alimentacao"   },
  { pattern: /restaurante|lanchonete|padaria/i, category: "Alimentacao"   },
  { pattern: /uber|99|taxi|ifood/i,             category: "Transporte"    },
  { pattern: /farmacia|drogaria/i,              category: "Saude"         },
  { pattern: /pagamento com qr pix/i,           category: "Pagamento"     },
  { pattern: /pagamento/i,                      category: "Pagamento"     },
];

function categorize(desc: string): string {
  for (const r of CATEGORY_RULES) {
    if (r.pattern.test(desc)) return r.category;
  }
  return "Outros";
}

function parseDate(raw: string): string {
  const [d, m, y] = raw.split("-");
  return `${y}-${m}-${d}`;
}

function parseAmount(raw: string): number {
  return parseFloat(raw.replace(",", "."));
}

// Linhas a ignorar completamente
const SKIP = /^(Data\s|Descri|ID da|Valor|Saldo|Saldo inicial|Saldo final|Entradas|saídas|DETALHE|período|CPF|Ag[eê]ncia|Conta:|Mercado Pago|Voc[eê]|0800|CNPJ|Av\.|www\.|Data de gera|--\s*\d|EXTRATO|Joaquim|^\d\/\d$)/i;

// Padrao: (tudo antes)(ID 10+ digitos) R$ (valor) R$ (saldo)
const TX_PATTERN = /^(.*?)(\d{10,})\s+R\$\s*([-\d,.]+)\s+R\$\s*([\d,.]+)\s*$/;

// Data no inicio: DD-MM-YYYY (resto...)
const DATE_LINE = /^(\d{2}-\d{2}-\d{4})\s*(.*)/;

export function parseMercadoPagoPDF(text: string): ParsedTransaction[] {
  const results: ParsedTransaction[] = [];
  const lines = text.split("\n").map((l) => l.trim()).filter(Boolean);

  let currentDate = "";
  let descParts: string[] = [];

  for (const line of lines) {
    // Pular cabecalhos, rodapes e linhas de separacao
    if (SKIP.test(line)) continue;

    // Verificar se a linha contem um padrao de transação completo
    // (pode comecar com data ou com descrição acumulada)
    const txMatch = line.match(TX_PATTERN);

    if (txMatch && currentDate) {
      // txMatch[1] = texto antes do ID (pode ser parte da descrição)
      const extraDesc = txMatch[1].trim();
      if (extraDesc) descParts.push(extraDesc);

      const description = descParts.join(" ").trim();
      const operationId = txMatch[2];
      const amount = parseAmount(txMatch[3]);

      if (description) {
        results.push({
          date: parseDate(currentDate),
          description,
          amount,
          category: categorize(description),
          operation_id: operationId,
        });
      }

      // Resetar estado
      currentDate = "";
      descParts = [];
      continue;
    }

    // Linha comeca com data
    const dateMatch = line.match(DATE_LINE);
    if (dateMatch) {
      currentDate = dateMatch[1];
      const rest = dateMatch[2].trim();

      // A data pode ja ter descrição + ID na mesma linha
      const inlineTx = rest.match(TX_PATTERN);
      if (inlineTx) {
        const description = inlineTx[1].trim();
        const operationId = inlineTx[2];
        const amount = parseAmount(inlineTx[3]);
        if (description) {
          results.push({
            date: parseDate(currentDate),
            description,
            amount,
            category: categorize(description),
            operation_id: operationId,
          });
        }
        currentDate = "";
        descParts = [];
      } else {
        // descrição comeca aqui, continua nas proximas linhas
        descParts = rest ? [rest] : [];
      }
      continue;
    }

    // Linha de descrição intermediaria (entre data e ID)
    if (currentDate) {
      descParts.push(line);
    }
  }

  return results;
}
