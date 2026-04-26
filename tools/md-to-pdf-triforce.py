"""Convert markdown to Triforce Auto styled HTML for PDF print."""
import sys
import markdown
from pathlib import Path

if len(sys.argv) < 4:
    print("Usage: md-to-pdf-triforce.py <input.md> <output.html> <title>")
    sys.exit(1)

md_path = Path(sys.argv[1])
html_path = Path(sys.argv[2])
title = sys.argv[3]

md_content = md_path.read_text(encoding="utf-8")

html_body = markdown.markdown(
    md_content,
    extensions=["tables", "fenced_code", "toc", "attr_list", "sane_lists"],
)

css = """
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800;900&display=swap');

@page { size: A4; margin: 18mm 16mm; }

* { box-sizing: border-box; margin: 0; padding: 0; }

body {
  font-family: 'Montserrat', -apple-system, sans-serif;
  color: #050505;
  line-height: 1.55;
  font-size: 10.5pt;
  background: #F5F0E8;
}

.cover {
  background: #0d0d0d;
  color: #F5F0E8;
  padding: 40mm 14mm;
  margin: -18mm -16mm 24px -16mm;
  text-align: center;
  border-bottom: 4px solid #FF6600;
  page-break-after: always;
  min-height: 260mm;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  position: relative;
}
.cover::before {
  content: '';
  position: absolute;
  inset: 0;
  background:
    radial-gradient(circle at 20% 30%, rgba(255,102,0,0.18), transparent 40%),
    radial-gradient(circle at 80% 70%, rgba(255,102,0,0.12), transparent 45%);
  pointer-events: none;
}
.cover-logo {
  font-size: 14pt;
  font-weight: 800;
  letter-spacing: 4px;
  color: #FF6600;
  margin-bottom: 18px;
  text-transform: uppercase;
}
.cover h1 {
  font-size: 44pt;
  font-weight: 900;
  line-height: 1.05;
  color: #F5F0E8;
  border: none;
  margin-bottom: 20px;
  letter-spacing: -1px;
  text-transform: uppercase;
}
.cover-accent {
  color: #FF6600;
}
.cover-sub {
  font-size: 13pt;
  font-weight: 500;
  color: #F5F0E8;
  opacity: 0.82;
  max-width: 120mm;
  margin: 0 auto 40px;
  line-height: 1.5;
}
.cover-meta {
  border-top: 3px solid #FF6600;
  padding-top: 20px;
  font-size: 10pt;
  font-weight: 600;
  letter-spacing: 2px;
  text-transform: uppercase;
  opacity: 0.75;
}

h1 {
  color: #050505;
  font-size: 22pt;
  font-weight: 900;
  text-transform: uppercase;
  letter-spacing: -0.5px;
  border-bottom: 3px solid #050505;
  padding-bottom: 10px;
  margin-top: 32px;
  margin-bottom: 18px;
  page-break-after: avoid;
  page-break-before: always;
}
h1:first-of-type { page-break-before: auto; }

h2 {
  color: #050505;
  font-size: 15pt;
  font-weight: 800;
  margin-top: 24px;
  margin-bottom: 10px;
  padding: 8px 14px;
  background: #FF6600;
  color: #050505;
  border: 3px solid #050505;
  box-shadow: 4px 4px 0 #050505;
  display: inline-block;
  text-transform: uppercase;
  page-break-after: avoid;
}

h3 {
  color: #050505;
  font-size: 12.5pt;
  font-weight: 800;
  margin-top: 18px;
  margin-bottom: 8px;
  padding-left: 12px;
  border-left: 4px solid #FF6600;
  page-break-after: avoid;
}

h4 {
  color: #050505;
  font-size: 11pt;
  font-weight: 700;
  margin-top: 14px;
  margin-bottom: 6px;
}

p {
  margin: 10px 0;
  text-align: left;
  color: #050505;
}

ul, ol { margin: 10px 0; padding-left: 22px; }
li { margin: 4px 0; }

strong { color: #050505; font-weight: 800; }
em { color: #050505; font-style: italic; }

code {
  background: #050505;
  color: #FF6600;
  padding: 2px 6px;
  border-radius: 0;
  font-family: 'Montserrat', monospace;
  font-size: 9.5pt;
  font-weight: 700;
}

blockquote {
  border: 3px solid #050505;
  background: #FF6600;
  box-shadow: 4px 4px 0 #050505;
  margin: 16px 4px;
  padding: 14px 18px;
  color: #050505;
  font-weight: 700;
  font-size: 12pt;
  page-break-inside: avoid;
}

table {
  border-collapse: collapse;
  width: 100%;
  margin: 14px 0;
  font-size: 9.5pt;
  page-break-inside: avoid;
  background: #ffffff;
  border: 3px solid #050505;
  box-shadow: 4px 4px 0 #050505;
}
th {
  background: #050505;
  color: #FF6600;
  padding: 9px 11px;
  text-align: left;
  font-weight: 800;
  text-transform: uppercase;
  font-size: 9pt;
  letter-spacing: 0.5px;
  border-bottom: 2px solid #FF6600;
}
td {
  padding: 8px 11px;
  border-bottom: 1px solid #050505;
  vertical-align: top;
  color: #050505;
}
tr:last-child td { border-bottom: none; }
tr:nth-child(even) td { background: #F5F0E8; }

hr {
  border: none;
  border-top: 3px solid #050505;
  margin: 28px 0;
}

a {
  color: #050505;
  text-decoration: none;
  font-weight: 700;
  border-bottom: 2px solid #FF6600;
}

.footer-stamp {
  margin-top: 40px;
  padding: 20px;
  background: #050505;
  color: #F5F0E8;
  text-align: center;
  border: 3px solid #050505;
  box-shadow: 4px 4px 0 #FF6600;
}
.footer-stamp strong {
  color: #FF6600;
  font-size: 14pt;
  letter-spacing: 3px;
  text-transform: uppercase;
}
"""

html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<title>{title}</title>
<style>{css}</style>
</head>
<body>
<div class="cover">
  <div class="cover-logo">Triforce Auto</div>
  <h1>Oferta<br><span class="cover-accent">Comercial</span></h1>
  <div class="cover-sub">
    Proposta Protocolo AAA para TAC Distribuidora<br>
    Atração ativa de clientes B2B de hortifruti na Bahia.
  </div>
  <div class="cover-meta">Período Teste · 3 Meses · 2026</div>
</div>
{html_body}
<div class="footer-stamp">
  <strong>Triforce Auto</strong><br>
  <span style="font-size:9pt; letter-spacing:1px;">Máquinas de atração ativa · 2026</span>
</div>
</body>
</html>
"""

html_path.write_text(html, encoding="utf-8")
print(f"HTML written to {html_path}")
