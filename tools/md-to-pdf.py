"""Convert markdown file to styled HTML for Chrome headless PDF print."""
import sys
import markdown
from pathlib import Path

if len(sys.argv) < 3:
    print("Usage: md-to-pdf.py <input.md> <output.html>")
    sys.exit(1)

md_path = Path(sys.argv[1])
html_path = Path(sys.argv[2])

md_content = md_path.read_text(encoding="utf-8")

html_body = markdown.markdown(
    md_content,
    extensions=["tables", "fenced_code", "toc", "attr_list", "sane_lists"],
)

css = """
@page { size: A4; margin: 20mm 18mm; }
* { box-sizing: border-box; }
body {
  font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, sans-serif;
  color: #1a1a1a;
  line-height: 1.55;
  font-size: 10.5pt;
  max-width: 100%;
  margin: 0;
  padding: 0;
}
h1 {
  color: #0f3d20;
  font-size: 22pt;
  border-bottom: 3px solid #e8611a;
  padding-bottom: 8px;
  margin-top: 28px;
  margin-bottom: 14px;
  page-break-after: avoid;
}
h1:first-child {
  margin-top: 0;
  font-size: 26pt;
  border-bottom-width: 4px;
}
h2 {
  color: #1a4a2e;
  font-size: 15pt;
  margin-top: 24px;
  margin-bottom: 10px;
  padding-bottom: 4px;
  border-bottom: 1px solid #d4d4d4;
  page-break-after: avoid;
}
h3 {
  color: #2d6b45;
  font-size: 12.5pt;
  margin-top: 18px;
  margin-bottom: 6px;
  page-break-after: avoid;
}
h4 { color: #374151; font-size: 11pt; margin-top: 14px; margin-bottom: 4px; }
p { margin: 8px 0; text-align: justify; }
ul, ol { margin: 8px 0; padding-left: 22px; }
li { margin: 3px 0; }
strong { color: #0f3d20; }
em { color: #374151; }
code {
  background: #f4f4f2;
  padding: 1px 5px;
  border-radius: 3px;
  font-family: 'Cascadia Code', Consolas, monospace;
  font-size: 9.5pt;
  color: #b91c1c;
}
pre {
  background: #f7f7f5;
  padding: 12px;
  border-left: 3px solid #e8611a;
  border-radius: 4px;
  overflow-x: auto;
  font-size: 9pt;
}
pre code { background: none; color: #1a1a1a; padding: 0; }
blockquote {
  border-left: 4px solid #e8611a;
  background: #fef7f1;
  margin: 12px 0;
  padding: 10px 16px;
  color: #374151;
  font-style: italic;
}
table {
  border-collapse: collapse;
  width: 100%;
  margin: 12px 0;
  font-size: 9.5pt;
  page-break-inside: avoid;
}
th {
  background: #1a4a2e;
  color: white;
  padding: 8px 10px;
  text-align: left;
  font-weight: 600;
  border: 1px solid #1a4a2e;
}
td {
  padding: 7px 10px;
  border: 1px solid #d4d4d4;
  vertical-align: top;
}
tr:nth-child(even) td { background: #f9f9f8; }
hr {
  border: none;
  border-top: 2px solid #e8611a;
  margin: 24px 0;
}
a { color: #1a4a2e; text-decoration: none; border-bottom: 1px dotted #2d6b45; }
.header-stamp {
  background: linear-gradient(135deg, #1a4a2e 0%, #2d6b45 100%);
  color: white;
  padding: 24px 28px;
  margin: -20mm -18mm 24px -18mm;
  text-align: center;
}
.header-stamp h1 {
  color: white;
  border: none;
  margin: 0;
  padding: 0;
  font-size: 24pt;
}
.header-stamp p { margin: 6px 0 0; opacity: 0.9; font-size: 11pt; }
"""

html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<title>Benchmark — TAC Distribuidora</title>
<style>{css}</style>
</head>
<body>
<div class="header-stamp">
  <h1>BENCHMARK TAC DISTRIBUIDORA</h1>
  <p>Pesquisa de Mercado e Estratégia Comercial &middot; Triforce Auto</p>
</div>
{html_body}
</body>
</html>
"""

html_path.write_text(html, encoding="utf-8")
print(f"HTML written to {html_path}")
