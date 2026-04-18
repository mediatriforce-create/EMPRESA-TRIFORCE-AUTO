"""
Gerador de Carrosséis Instagram — Triforce Auto
HTML/CSS + Playwright → PNG 1080x1350px
Paleta: preto #0A0A0A | bege #F5F0EB | laranja #FF6B00
"""

import asyncio
import base64
import re
import os
from pathlib import Path
from playwright.async_api import async_playwright

OUTPUT_DIR = Path(__file__).parent / "carroseis-abril-2026" / "png"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# ─── BADGES DE EMPRESA (CSS puro — sem dependência externa) ────────────────────

# Cores e SVG inline das marcas
COMPANY_BADGES = {
    "meta.com": {
        "label": "Meta",
        "color": "#0082FB",
        "bg": "#E8F3FF",
        "svg": """<svg width="22" height="22" viewBox="0 0 24 24" fill="none">
          <path d="M2 8.5C2 6 3.5 4 5.5 4c1.5 0 2.5.8 4 2.8L12 10l2.5-3.2c1.5-2 2.5-2.8 4-2.8C20.5 4 22 6 22 8.5c0 2.5-1.2 5-4 8l-6 5.5L6 16.5c-2.8-3-4-5.5-4-8z" fill="#0082FB"/>
        </svg>"""
    },
    "anthropic.com": {
        "label": "Anthropic",
        "color": "#D97757",
        "bg": "#FDF3EE",
        "svg": """<svg width="22" height="22" viewBox="0 0 24 24" fill="none">
          <text x="3" y="18" font-family="Georgia,serif" font-size="18" font-weight="bold" fill="#D97757">A</text>
        </svg>"""
    },
    "openai.com": {
        "label": "OpenAI",
        "color": "#10A37F",
        "bg": "#E8F8F4",
        "svg": """<svg width="22" height="22" viewBox="0 0 24 24" fill="none">
          <circle cx="12" cy="12" r="9" stroke="#10A37F" stroke-width="2"/>
          <circle cx="12" cy="12" r="3" fill="#10A37F"/>
        </svg>"""
    },
    "whatsapp.com": {
        "label": "WhatsApp",
        "color": "#25D366",
        "bg": "#E8F8EE",
        "svg": """<svg width="22" height="22" viewBox="0 0 24 24" fill="none">
          <path d="M12 2C6.48 2 2 6.48 2 12c0 1.85.5 3.58 1.37 5.07L2 22l5.1-1.33A9.93 9.93 0 0012 22c5.52 0 10-4.48 10-10S17.52 2 12 2z" fill="#25D366"/>
          <path d="M17 14.8c-.3.8-1.5 1.5-2.1 1.6-.6.1-1.3.2-4.3-1.3C7.5 13.5 6 10.5 5.9 10.3c-.1-.2-.8-1.1-.8-2.1 0-1 .5-1.5.7-1.7.2-.2.5-.3.7-.3h.5c.2 0 .4.1.5.3l1.1 2.5c.1.2.1.5 0 .7l-.5.6c-.1.1-.2.3-.1.5.4.7 1 1.4 1.6 1.9.6.5 1.3.9 2 1.1.2.1.4 0 .5-.1l.6-.7c.2-.2.4-.3.7-.2l2.3 1.1c.3.1.5.3.5.5.1.1.1.5-.2 1.4z" fill="white"/>
        </svg>"""
    },
    "ramp.com": {
        "label": "Ramp",
        "color": "#6C47FF",
        "bg": "#F0ECFF",
        "svg": """<svg width="22" height="22" viewBox="0 0 24 24" fill="none">
          <rect x="3" y="3" width="18" height="18" rx="4" fill="#6C47FF"/>
          <text x="7" y="17" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="white">R</text>
        </svg>"""
    },
    "google.com": {
        "label": "Google",
        "color": "#4285F4",
        "bg": "#EAF1FF",
        "svg": """<svg width="22" height="22" viewBox="0 0 24 24" fill="none">
          <path d="M21.8 12.2c0-.7-.1-1.4-.2-2H12v3.8h5.5c-.2 1.3-1 2.4-2.1 3.1v2.6h3.4c2-1.8 3-4.5 3-7.5z" fill="#4285F4"/>
          <path d="M12 22c2.7 0 5-0.9 6.7-2.4l-3.4-2.6c-.9.6-2 1-3.3 1-2.5 0-4.7-1.7-5.4-4H3v2.7C4.7 19.8 8.1 22 12 22z" fill="#34A853"/>
          <path d="M6.6 14c-.2-.6-.3-1.3-.3-2s.1-1.4.3-2V7.3H3A10 10 0 002 12c0 1.6.4 3.2 1 4.7L6.6 14z" fill="#FBBC05"/>
          <path d="M12 5.5c1.4 0 2.6.5 3.6 1.4l2.7-2.7C16.9 2.7 14.6 2 12 2 8.1 2 4.7 4.2 3 7.3l3.6 2.7C7.3 7.2 9.5 5.5 12 5.5z" fill="#EA4335"/>
        </svg>"""
    },
}


def get_badge_html(domain: str, dark_mode: bool = False) -> str:
    """Retorna HTML de badge de empresa (CSS puro, sem imagens externas)."""
    info = COMPANY_BADGES.get(domain)
    if not info:
        return ""

    if dark_mode:
        bg = "rgba(255,255,255,0.10)"
        border = "rgba(255,255,255,0.15)"
        text_color = "rgba(255,255,255,0.80)"
    else:
        bg = info["bg"]
        border = f"rgba(0,0,0,0.08)"
        text_color = "#3a3a3a"

    return f"""<div style="
      display:inline-flex; align-items:center; gap:7px;
      background:{bg}; border:1px solid {border};
      border-radius:30px; padding:6px 14px 6px 8px;
    ">
      {info['svg']}
      <span style="
        font-family:'Inter',sans-serif; font-size:16px;
        font-weight:600; color:{text_color}; letter-spacing:0.02em;
        white-space:nowrap;
      ">{info['label']}</span>
    </div>"""


# ─── TEMPLATES HTML ────────────────────────────────────────────────────────────

BASE_STYLE = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

* { margin: 0; padding: 0; box-sizing: border-box; }

body {
  width: 1080px;
  height: 1350px;
  font-family: 'Inter', -apple-system, sans-serif;
  overflow: hidden;
}
"""


def cover_slide(headline, subheadline, slide_num, logo_domain=None, bg_file=None):
    badge_html = get_badge_html(logo_domain, dark_mode=True) if logo_domain else ""
    top_right = badge_html if badge_html else '<span style="font-size:20px;font-weight:500;color:rgba(255,255,255,0.3);letter-spacing:0.1em;">01</span>'

    # Background: foto embutida como base64, ou glow CSS puro
    if bg_file and Path(bg_file).exists():
        raw = Path(bg_file).read_bytes()
        b64 = base64.b64encode(raw).decode()
        bg_data = f"data:image/jpeg;base64,{b64}"
        bg_layer = f"""
  <div style="position:absolute;inset:0;z-index:0;
    background:url('{bg_data}') center/cover no-repeat;"></div>
  <div style="position:absolute;inset:0;z-index:1;
    background:linear-gradient(180deg,
      rgba(5,5,5,0.88) 0%,
      rgba(5,5,5,0.55) 45%,
      rgba(5,5,5,0.85) 100%);"></div>"""
    else:
        bg_layer = """<div style="position:absolute;width:600px;height:600px;border-radius:50%;
    background:radial-gradient(circle,rgba(255,107,0,0.14) 0%,transparent 70%);
    top:50%;left:50%;transform:translate(-50%,-50%);z-index:1;"></div>"""

    return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
{BASE_STYLE}

body {{
  background: #0A0A0A;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 80px 72px;
  position: relative;
}}

.noise {{
  position: absolute; inset: 0;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)' opacity='0.05'/%3E%3C/svg%3E");
  pointer-events: none; z-index: 2;
}}

.top {{
  display: flex; align-items: center;
  justify-content: space-between; z-index: 3;
}}

.tag {{
  font-size: 20px; font-weight: 600;
  color: #FF6B00; letter-spacing: 0.15em;
  text-transform: uppercase;
}}

.center {{
  flex: 1; display: flex; flex-direction: column;
  justify-content: center; z-index: 3; gap: 32px;
}}

h1 {{
  font-size: 72px; font-weight: 900;
  color: #FFFFFF; line-height: 1.05;
  letter-spacing: -0.02em;
  text-shadow: 0 4px 32px rgba(0,0,0,0.7);
}}

h1 span {{ color: #FF6B00; }}

.subheadline {{
  font-size: 28px; font-weight: 400;
  color: rgba(255,255,255,0.65); line-height: 1.4;
  max-width: 820px;
  border-left: 3px solid #FF6B00;
  padding-left: 20px;
}}

.swipe {{
  font-size: 22px; font-weight: 600;
  color: rgba(255,255,255,0.35); letter-spacing: 0.05em;
}}

.bottom {{
  display: flex; align-items: center;
  justify-content: space-between; z-index: 3;
}}

.line {{
  position: absolute; bottom: 0; left: 0;
  width: 100%; height: 3px;
  background: linear-gradient(90deg, #FF6B00, transparent);
  z-index: 3;
}}
</style>
</head>
<body>
  {bg_layer}
  <div class="noise"></div>
  <div class="line"></div>

  <div class="top">
    <span class="tag">Triforce Auto · IA</span>
    {top_right}
  </div>

  <div class="center">
    <h1>{headline}</h1>
    <p class="subheadline">{subheadline}</p>
    <p class="swipe">Deslize para ler →</p>
  </div>

  <div class="bottom">
    <span style="font-size:22px;font-weight:700;color:rgba(255,255,255,0.55);
      letter-spacing:0.05em;display:flex;align-items:center;gap:8px;">
      <span style="width:8px;height:8px;border-radius:50%;background:#FF6B00;
        display:inline-block;flex-shrink:0;"></span>
      @triforceauto
    </span>
  </div>
</body>
</html>"""


SLIDE_BASE_CSS = """
body {
  background: #F5F0EB;
  display: flex;
  flex-direction: column;
  padding: 0 64px 52px;
}
.top-stripe {
  width: 100%; height: 5px;
  background: #FF6B00;
  margin-bottom: 40px; flex-shrink: 0;
}
.header {
  display: flex; align-items: center;
  justify-content: space-between;
  padding-bottom: 32px; flex-shrink: 0;
}
.header-handle { font-size:22px; font-weight:700; color:#FF6B00; }
.header-mid    { font-size:20px; font-weight:500; color:#aaa; }
.header-right  { font-size:20px; font-weight:400; color:#bbb; }
.content {
  flex: 1; display: flex; flex-direction: column;
  justify-content: flex-start; gap: 28px;
  min-height: 0; overflow: hidden;
}
h2 {
  font-size: 76px; font-weight: 900; color: #0A0A0A;
  line-height: 1.05; letter-spacing: -0.03em; margin: 0;
}
.body { font-size:34px; font-weight:400; color:#2a2a2a; line-height:1.58; margin:0; }
.body strong { font-weight:700; color:#0A0A0A; }
.footer {
  display: flex; align-items: center; justify-content: space-between;
  margin-top: 28px; padding-top: 20px;
  border-top: 1.5px solid rgba(10,10,10,0.10); flex-shrink: 0;
}
.footer-left { display:flex; align-items:center; gap:12px; }
.footer-avatar {
  width:42px; height:42px; border-radius:50%;
  background:#FF6B00; display:flex; align-items:center; justify-content:center; flex-shrink:0;
}
.footer-name   { font-size:20px; font-weight:800; color:#0A0A0A; }
.footer-handle { font-size:17px; font-weight:400; color:#999; }
.swipe { font-size:20px; font-weight:600; color:#FF6B00; }
"""

SLIDE_FOOTER_HTML = """
  <div class="footer">
    <div class="footer-left">
      <div class="footer-avatar">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none">
          <path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z" fill="white"/>
        </svg>
      </div>
      <div>
        <div class="footer-name">Triforce Auto</div>
        <div class="footer-handle">@triforceauto</div>
      </div>
    </div>
    <span class="swipe">Arrasta para o lado ›</span>
  </div>
"""


def _img_box(logo_b64=None, bg_file=None, logo_domain=None, height="flex", fit="cover", bg="#0A0A0A"):
    """Retorna HTML do bloco de imagem.

    height  — 'flex' preenche espaço restante | valor CSS fixo ('300px')
    fit     — 'cover'   imagem preenche e corta (fotos Unsplash)
              'contain' imagem inteira visível, sem corte (screenshots, gráficos, tabelas)
    """
    h_style = "flex:1; min-height:240px;" if height == "flex" else f"height:{height}; flex-shrink:0;"

    if logo_b64:
        return f"""<div style="width:100%; {h_style} border-radius:20px; overflow:hidden;
    background:#111; display:flex; align-items:center; justify-content:center;">
    <img src="{logo_b64}" style="max-height:200px;max-width:620px;object-fit:contain;">
  </div>"""

    if bg_file and Path(bg_file).exists():
        ext = Path(bg_file).suffix.lower()
        mime = "image/png" if ext == ".png" else ("image/gif" if ext == ".gif" else "image/jpeg")
        raw = Path(bg_file).read_bytes()
        b64 = base64.b64encode(raw).decode()
        if fit == "contain":
            # Imagem inteira visível — fundo configurável, container usa h_style
            return f"""<div style="width:100%; {h_style} border-radius:20px; overflow:hidden;
    background:{bg}; display:flex; align-items:center; justify-content:center; padding:8px;">
    <img src="data:{mime};base64,{b64}"
         style="max-width:100%; max-height:100%; object-fit:contain; border-radius:12px; display:block;">
  </div>"""
        else:
            return f"""<div style="width:100%; {h_style} border-radius:20px; overflow:hidden;
    background:url('data:{mime};base64,{b64}') center/cover no-repeat;"></div>"""

    # fallback escuro com badge
    co = COMPANY_BADGES.get(logo_domain or "")
    inner = ""
    if co:
        inner = f"""<div style="display:flex;flex-direction:column;align-items:center;gap:16px;">
      <div style="transform:scale(2.5);transform-origin:center;">{co['svg']}</div>
      <span style="font-family:'Inter',sans-serif;font-size:28px;font-weight:700;
        color:rgba(255,255,255,0.6);margin-top:12px;">{co['label']}</span>
    </div>"""
    return f"""<div style="width:100%; {h_style} border-radius:20px;
    background:#0A0A0A; display:flex; align-items:center; justify-content:center;">{inner}</div>"""


def strip_sources(text):
    """Remove citações inline de fonte do tipo (Nome, mês/ano) ou (Nome, ano)."""
    if not text:
        return text
    # Remove (Fonte, mês/ano) — ex: (The Atlantic, mar/2026) ou (MIT Tech Review, 2026)
    cleaned = re.sub(r'\s*\([^)]*\d{4}\)', '', text)
    return cleaned.strip()


def content_slide(num, title, body_html, logo_domain=None, logo_b64=None, bg_file=None,
                  layout="standard", chart=None, accent=None, photo_height=None, photo_fit="cover", photo_bg="#0A0A0A"):
    """
    layout="standard"     — título + corpo + foto (flex por padrão)
    layout="heavy"        — título menor + corpo mais longo + foto proporcional
    layout="data"         — comparação numérica em slide escuro
    layout="spotlight"    — frase de impacto em slide escuro
    photo_height          — "flex" | "260px" | "320px" | "380px" | "480px" | "550px"
                            None = automático por layout
    """

    # ── STANDARD / HEAVY — com foto variável ──────────────────────────────────
    if layout in ("standard", "heavy"):
        # Determina altura da foto: explícito > automático por layout
        if photo_height:
            h = photo_height
        else:
            h = "flex"    # padrão absoluto: foto preenche o espaço restante

        img = _img_box(logo_b64, bg_file, logo_domain, height=h, fit=photo_fit, bg=photo_bg)
        if layout == "heavy":
            title_style = 'style="font-size:62px;"'
            body_style  = 'style="font-size:30px;line-height:1.65;"'
        else:
            title_style = ""
            body_style  = ""
        inner = f"""
  <div class="content">
    <h2 {title_style}>{title}</h2>
    <p class="body" {body_style}>{body_html}</p>
    {img}
  </div>"""
        extra_css = ""

    # ── DATA — slide escuro completo (tipo spotlight) com comparação visual
    elif layout == "data":
        source_html = ""
        bar_items = []
        for item in (chart or []):
            if "source" in item:
                source_html = item["source"]
            elif "stat" not in item:
                bar_items.append(item)

        rows_html = ""
        for item in bar_items:
            is_highlight = item.get("color") == "#FF6B00"
            val_color = item.get("color", "rgba(255,255,255,0.35)")
            bar_w = item.get("pct", 50)
            bar_bg = "#FF6B00" if is_highlight else "rgba(255,255,255,0.20)"
            name_color = "#FFFFFF" if is_highlight else "rgba(255,255,255,0.38)"
            bg_row = "rgba(255,107,0,0.07)" if is_highlight else "transparent"
            rows_html += f"""
      <div class="drow" style="background:{bg_row};">
        <div class="drow-top">
          <span class="drow-name" style="color:{name_color};">{item['label']}</span>
          <span class="drow-val" style="color:{val_color};">{item['val']}</span>
        </div>
        <div class="drow-track">
          <div class="drow-bar" style="width:{bar_w}%;background:{bar_bg};"></div>
        </div>
      </div>"""

        # Slide escuro: dois blocos full-width, cada um metade do slide
        blocks_html = ""
        for item in bar_items:
            is_hi = item.get("color") == "#FF6B00"
            val_color = "#FF6B00" if is_hi else "rgba(255,255,255,0.22)"
            bar_bg = "#FF6B00" if is_hi else "rgba(255,255,255,0.18)"
            name_color = "#FFFFFF" if is_hi else "rgba(255,255,255,0.40)"
            bar_w = item.get("pct", 50)
            pct_text = f"{bar_w}%"
            bg = "rgba(255,107,0,0.08)" if is_hi else "rgba(255,255,255,0.025)"
            border = "rgba(255,107,0,0.20)" if is_hi else "rgba(255,255,255,0.06)"
            blocks_html += f"""
      <div class="dblock" style="background:{bg};border-color:{border};">
        <div class="dblock-top">
          <span class="dblock-name" style="color:{name_color};">{item['label']}</span>
          <span class="dblock-pct" style="color:{val_color};">{pct_text}</span>
        </div>
        <span class="dblock-num" style="color:{val_color};">{item['val']}</span>
        <div class="dblock-track">
          <div class="dblock-bar" style="width:{bar_w}%;background:{bar_bg};"></div>
        </div>
      </div>"""

        return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
{BASE_STYLE}
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{
  background: #0A0A0A;
  width:1080px; height:1350px;
  display: flex; flex-direction: column;
  padding: 72px 72px 64px;
  gap: 24px;
  font-family: 'Inter', sans-serif;
  overflow: hidden;
}}
.dtop {{ flex-shrink:0; }}
.dtag {{
  font-size: 16px; font-weight: 600; display:block;
  color: rgba(255,255,255,0.20); letter-spacing: 0.10em;
  text-transform: uppercase; margin-bottom: 16px;
}}
h2 {{
  font-size: 50px; font-weight: 900; color: #FFFFFF;
  line-height: 1.05; letter-spacing: -0.03em; margin-bottom: 6px;
}}
.dsubtitle {{
  font-size: 18px; font-weight: 500;
  color: rgba(255,255,255,0.28);
}}
.dblocks {{
  flex: 1; display: flex; flex-direction: column; gap: 16px;
  min-height: 0;
}}
.dblock {{
  flex: 1; display: flex; flex-direction: column;
  justify-content: space-between;
  border: 1px solid; border-radius: 16px;
  padding: 32px 40px 28px;
  min-height: 0;
}}
.dblock-top {{
  display: flex; align-items: center; justify-content: space-between;
}}
.dblock-name {{
  font-size: 28px; font-weight: 800; letter-spacing: -0.01em;
}}
.dblock-pct {{
  font-size: 28px; font-weight: 800; letter-spacing: -0.02em;
}}
.dblock-num {{
  font-size: 200px; font-weight: 900; line-height: 0.85;
  letter-spacing: -0.05em; display: block;
}}
.dblock-track {{
  width: 100%; height: 14px;
  background: rgba(255,255,255,0.07); border-radius: 7px;
  overflow: hidden;
}}
.dblock-bar {{ height: 100%; border-radius: 7px; }}
.dfooter {{
  display: flex; align-items: center; justify-content: space-between;
  padding-top: 20px; border-top: 1px solid rgba(255,255,255,0.07);
  flex-shrink: 0;
}}
.dsource {{ font-size: 13px; color: rgba(255,255,255,0.16); }}
.dhandle {{
  font-size: 16px; font-weight: 700; color: rgba(255,255,255,0.30);
  display: flex; align-items: center; gap: 8px;
}}
.ddot {{ width: 7px; height: 7px; border-radius: 50%; background: #FF6B00; display: inline-block; }}
</style>
</head>
<body>
  <div class="dtop">
    <span class="dtag">@triforceauto · Canal de IA</span>
    <h2>{title}</h2>
    <p class="dsubtitle">{body_html}</p>
  </div>
  <div class="dblocks">{blocks_html}</div>
  <div class="dfooter">
    <span class="dhandle"><span class="ddot"></span>@triforceauto</span>
  </div>
</body>
</html>"""
        inner = ""
        extra_css = ""

    # ── SPOTLIGHT — slide escuro com frase de impacto (branco + destaque laranja)
    elif layout == "spotlight":
        lines = (accent or title).split("\n")
        lines_html = ""
        for line in lines:
            lines_html += f'<span class="spot-line">{line}</span>\n'
        inner = f"""
  <div class="spot-body">
    <div class="spot-top">
      <span class="spot-tag">@triforceauto · Canal de IA</span>
    </div>
    <div class="spot-center">
      <div class="spot-lines">{lines_html}</div>
      <p class="spot-sub">{body_html}</p>
    </div>
    <div class="spot-bottom">
      <span style="font-size:20px;font-weight:700;color:rgba(255,255,255,0.45);
        display:flex;align-items:center;gap:8px;">
        <span style="width:7px;height:7px;border-radius:50%;background:#FF6B00;display:inline-block;"></span>
        @triforceauto
      </span>
      <span style="font-size:16px;font-weight:600;color:#FF6B00;">Arrasta para o lado ›</span>
    </div>
  </div>"""
        extra_css = """
body { background: #0A0A0A !important; padding: 0 !important; }
.top-stripe { display: none; }
.spot-body {
  flex: 1; width: 100%;
  position: relative;
}
.spot-top {
  position: absolute; top: 72px; left: 72px; right: 72px;
}
.spot-tag {
  font-size: 18px; font-weight: 600;
  color: rgba(255,255,255,0.25); letter-spacing: 0.06em;
  text-transform: uppercase;
}
.spot-center {
  position: absolute;
  top: 50%; left: 72px; right: 72px;
  transform: translateY(-50%);
  display: flex; flex-direction: column; gap: 40px;
}
.spot-lines { display: flex; flex-direction: column; gap: 0; }
.spot-line {
  font-size: 100px; font-weight: 900;
  color: #FFFFFF; line-height: 1.0;
  letter-spacing: -0.03em; display: block;
}
.spot-line:first-child { color: #FF6B00; }
.spot-sub {
  font-size: 28px; font-weight: 400;
  color: rgba(255,255,255,0.55); line-height: 1.55;
  max-width: 820px;
  border-left: 3px solid #FF6B00; padding-left: 22px;
}
.spot-bottom {
  position: absolute; bottom: 60px; left: 72px; right: 72px;
  display: flex; align-items: center; justify-content: space-between;
  padding-top: 32px; border-top: 1px solid rgba(255,255,255,0.08);
}"""

    else:
        inner = ""
        extra_css = ""

    # Spotlight tem layout próprio sem o header/footer padrão
    if layout == "spotlight":
        return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
{BASE_STYLE}
{SLIDE_BASE_CSS}
{extra_css}
</style>
</head>
<body>
  {inner}
</body>
</html>"""

    return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
{BASE_STYLE}
{SLIDE_BASE_CSS}
{extra_css}
</style>
</head>
<body>
  <div class="top-stripe"></div>
  <div class="header">
    <span class="header-handle">@triforceauto</span>
    <span class="header-mid">Canal de IA</span>
    <span class="header-right">© 2026</span>
  </div>
  {inner}
  {SLIDE_FOOTER_HTML}
</body>
</html>"""


def cta_slide(main_text, sub_text):
    return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
{BASE_STYLE}

body {{
  background: #0A0A0A;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 80px 72px;
  text-align: center;
  gap: 40px;
  position: relative;
}}

.glow {{
  position: absolute;
  width: 700px;
  height: 700px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(255,107,0,0.15) 0%, transparent 65%);
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}}

.tag {{
  font-size: 20px;
  font-weight: 600;
  color: #FF6B00;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  z-index: 1;
}}

h2 {{
  font-size: 58px;
  font-weight: 900;
  color: #FFFFFF;
  line-height: 1.1;
  letter-spacing: -0.02em;
  max-width: 900px;
  z-index: 1;
}}

h2 span {{
  color: #FF6B00;
}}

.sub {{
  font-size: 28px;
  font-weight: 400;
  color: rgba(255,255,255,0.5);
  line-height: 1.5;
  max-width: 780px;
  z-index: 1;
}}

.cta-box {{
  border: 2px solid #FF6B00;
  padding: 22px 48px;
  border-radius: 4px;
  z-index: 1;
}}

.cta-text {{
  font-size: 26px;
  font-weight: 700;
  color: #FF6B00;
  letter-spacing: 0.05em;
}}

.handle {{
  font-size: 32px;
  font-weight: 800;
  color: #FFFFFF;
  letter-spacing: 0.05em;
  z-index: 1;
}}

.line-top, .line-bottom {{
  position: absolute;
  left: 0;
  width: 100%;
  height: 3px;
  background: linear-gradient(90deg, #FF6B00, transparent);
}}
.line-top {{ top: 0; }}
.line-bottom {{ bottom: 0; transform: rotate(180deg); }}
</style>
</head>
<body>
  <div class="glow"></div>
  <div class="line-top"></div>
  <div class="line-bottom"></div>

  <span class="tag">Triforce Auto</span>
  <h2>{main_text}</h2>
  <p class="sub">{sub_text}</p>
  <div class="cta-box">
    <span class="cta-text">Fale com a gente →</span>
  </div>
  <span class="handle">@triforceauto</span>
</body>
</html>"""


# ─── DADOS DOS CARROSSÉIS ──────────────────────────────────────────────────────

CARROSEIS = [
    {
        "slug": "01-meta-muse-spark",
        "cover_photo_query": "smartphone dark technology chat",
        "cover_logo_domain": "meta.com",
        "cover_logo_name": "Meta",
        "slides": [
            ("cover", {
                "headline": "Seu concorrente já tem IA no WhatsApp",
                "subheadline": "A Meta integrou IA generativa direto no app — e a maioria dos donos de negócio ainda não sabe o que está perdendo",
                "emoji": "💬"
            }),
            ("content", {
                "num": 2, "icon": "⚡",
                "logo_domain": "meta.com", "logo_name": "Meta AI",
                "photo_query": "social-media-app-smartphone",
                "photo_height": "flex",
                "title": "O que é o Muse Spark",
                "body": "Não é um bot que você instala. É IA da Meta <strong>dentro do WhatsApp</strong>, disponível direto onde você já atende clientes — sem configurar nada extra."
            }),
            ("content", {
                "num": 3,
                "layout": "spotlight",
                "accent": "Tudo no WhatsApp.\nSem instalar.\nSem gambiarra.",
                "photo_query": "whatsapp-chat-messaging",
                "title": "O que ela faz",
                "body": "Resposta rápida, resumo de conversa, orçamento no chat — direto onde seu cliente já está."
            }),
            ("content", {
                "num": 4,
                "layout": "heavy",
                "photo_query": "small-business-owner-customer",
                "photo_height": "380px",
                "title": "O que muda para o seu negócio",
                "body": "Cliente sem resposta vai embora. Com o Muse Spark, o app gera a resposta — você só aprova ou envia.<br><br>Para barbearia, personal e loja, <strong>é atendimento que não para quando você para</strong>. O concorrente que aprender isso primeiro vai ter vantagem real."
            }),
            ("content", {
                "num": 5,
                "layout": "heavy",
                "photo_query": "question-uncertainty-thinking",
                "photo_height": "280px",
                "title": "O que ainda não está confirmado",
                "body": "Três pontos sem data oficial: disponibilidade no Brasil, integração com WhatsApp Business e política de privacidade dos dados de conversa.<br><br><strong>Isso não é motivo para esperar</strong> — é motivo para montar o fluxo já, com as ferramentas que existem hoje."
            }),
            ("cta", {
                "main": "Seu atendimento no WhatsApp já funciona <span>sem você</span>?",
                "sub": "A Triforce monta o fluxo que responde, confirma e vende — enquanto você faz o que você sabe fazer."
            }),
        ]
    },
    {
        "slug": "02-anthropic-sp",
        "cover_photo_query": "sao paulo city skyline night aerial",
        "cover_logo_domain": "anthropic.com",
        "cover_logo_name": "Anthropic",
        "slides": [
            ("cover", {
                "headline": "Brasil é o 3º mercado de IA do mundo",
                "subheadline": "A Anthropic abriu escritório em SP — e isso muda o acesso de quem trabalha aqui",
                "emoji": "🇧🇷"
            }),
            ("content", {
                "num": 2,
                "layout": "heavy",
                "logo_domain": "anthropic.com",
                "photo_query": "artificial-intelligence-technology",
                "photo_height": "340px",
                "title": "Por que isso não é só notícia",
                "body": "Quando uma big tech abre escritório local, não é marketing — é infraestrutura. Significa suporte em português, contratos em real, compliance com LGPD e modelos calibrados para o mercado brasileiro.<br><br>O Brasil é o <strong>3º maior mercado do Claude no mundo</strong>. A Anthropic está aqui porque o volume de uso já justificou o investimento."
            }),
            ("content", {
                "num": 3,
                "layout": "standard",
                "logo_domain": "anthropic.com",
                "photo_query": "brazil-business-office-work",
                "photo_height": "flex",
                "title": "O que muda para quem usa IA aqui",
                "body": "Suporte em português, contratos em real, modelos ajustados para o mercado local. <strong>O custo de colocar IA no seu processo cai.</strong> O de não colocar sobe."
            }),
            ("content", {
                "num": 4,
                "layout": "spotlight",
                "accent": "A janela está\naberta.\nMas não vai\nficar.",
                "photo_query": "open-door-opportunity-light",
                "title": "A janela está aberta",
                "body": "Quando big techs chegam em mercado emergente, as primeiras empresas que adotam ganham vantagem de posicionamento. Depois vira padrão."
            }),
            ("cta", {
                "main": "Enquanto virou notícia, alguns já <span>colocaram no ar</span>.",
                "sub": "A Triforce implementa IA no seu processo hoje — sem depender de quando a Anthropic confirmar mais novidades."
            }),
        ]
    },
    {
        "slug": "03-claude-mythos",
        "cover_photo_query": "vault door dark secret mystery",
        "cover_logo_domain": "anthropic.com",
        "cover_logo_name": "Anthropic",
        "slides": [
            ("cover", {
                "headline": "Existe um modelo de IA que você não pode usar",
                "subheadline": "A Anthropic está testando capacidades que não chegaram ao público — e isso explica muito sobre onde a IA está indo",
                "emoji": "🔒"
            }),
            ("content", {
                "num": 2,
                "layout": "standard",
                "logo_domain": "anthropic.com",
                "photo_query": "neural-network-brain-ai",
                "photo_height": "flex",
                "title": "O que é o Claude Mythos",
                "body": "Modelo interno da Anthropic com capacidades além do Claude 3.7. Acesso restrito a parceiros selecionados. <strong>Não está na API pública — ainda.</strong>"
            }),
            ("content", {
                "num": 3,
                "layout": "heavy",
                "photo_query": "security-restricted-access-lock",
                "photo_height": "300px",
                "title": "Por que restringem antes de lançar",
                "body": "Dois motivos, ambos sérios:<br><br><strong>Risco:</strong> se as capacidades cruzam um ponto de perigo real, a Anthropic prefere avaliar antes de liberar acesso aberto.<br><br><strong>Vantagem competitiva:</strong> quando um modelo é muito melhor que o estado da arte público, o laboratório monetiza em parceiros antes de abrir."
            }),
            ("content", {
                "num": 4,
                "layout": "spotlight",
                "accent": "O que você usa\nhoje já ficou\npara trás.",
                "photo_query": "futuristic-technology-abstract",
                "title": "O que isso diz sobre o presente",
                "body": "A corrida está em um patamar que o público não vê. Quem não implementa agora perde duas vezes."
            }),
            ("cta", {
                "main": "O próximo modelo não vai resolver o que <span>você ainda não automatizou</span>.",
                "sub": "A Triforce usa o que existe hoje para entregar resultado real — sem esperar pelo futuro."
            }),
        ]
    },
    {
        "slug": "04-claude-vs-chatgpt",
        "cover_photo_query": "data analytics growth technology dark",
        "cover_logo_domain": "anthropic.com",
        "cover_logo_name": "Anthropic",
        "slides": [
            ("cover", {
                "headline": "Claude cresceu 6x mais que ChatGPT nas empresas",
                "subheadline": "Não é opinião — é dado de gasto real. O Ramp AI Index mostrou onde o dinheiro está indo",
                "emoji": "📊"
            }),
            ("content", {
                "num": 2,
                "layout": "data",
                "logo_domain": "ramp.com",
                "photo_query": "data-analytics-chart-growth",
                "title": "O dado que ninguém esperava",
                "body": "Crescimento em uso corporativo — Q1 2026 (Ramp AI Index)",
                "chart": [
                    {"stat": "6×", "label": "mais crescimento do Claude em uso corporativo", "color": "#FF6B00"},
                    {"label": "Claude",  "pct": 86, "val": "6×", "color": "#FF6B00"},
                    {"label": "ChatGPT", "pct": 14, "val": "1×", "color": "#555"},
                    {"source": "Ramp AI Index — transações reais, não pesquisa"},
                ]
            }),
            ("content", {
                "num": 3,
                "layout": "heavy",
                "logo_domain": "anthropic.com",
                "photo_query": "corporate-office-meeting-team",
                "photo_height": "260px",
                "title": "Por que empresas estão migrando",
                "body": "Três razões práticas que aparecem nas avaliações técnicas:<br><br><strong>Menos alucinação</strong> em contexto técnico e jurídico.<br><strong>Instruções seguidas com mais precisão</strong> em tarefas estruturadas.<br><strong>Raciocínio consistente</strong> em prompts longos e complexos.<br><br>Onde erro tem custo — auditoria, contrato, código — consistência vence hype."
            }),
            ("content", {
                "num": 4,
                "layout": "standard",
                "logo_domain": "openai.com",
                "photo_query": "comparison-balance-choice",
                "photo_height": "flex",
                "title": "O que isso não quer dizer",
                "body": "ChatGPT tem mais usuários no total — e continua forte em uso casual. A diferença aparece em <strong>processo estruturado</strong>, onde você precisa de resultado previsível toda vez."
            }),
            ("content", {
                "num": 5,
                "layout": "spotlight",
                "accent": "Ferramenta certa\npor tarefa.\nNão por marca.",
                "photo_query": "strategy-decision-thinking-business",
                "title": "A pergunta que importa",
                "body": "Você escolhe pelo que a maioria usa — ou pelo que funciona para o que você precisa fazer?"
            }),
            ("cta", {
                "main": "Usamos o modelo que <span>resolve o seu processo</span> — não o que está na capa de revista.",
                "sub": "Claude, GPT ou Gemini: a Triforce escolhe por resultado, integra sem gambiarra e entrega funcionando."
            }),
        ]
    },
    {
        "slug": "05-ia-pequenos-negocios",
        "cover_photo_query": "barber shop small business entrepreneur",
        "slides": [
            ("cover", {
                "headline": "Barbearia que não usa IA perde cliente toda semana",
                "subheadline": "Não é exagero — é o que acontece quando alguém não responde o WhatsApp a tempo",
                "emoji": "🛒"
            }),
            ("content", {
                "num": 2, "icon": "✂️",
                "photo_query": "barber-scissors-haircut",
                "photo_height": "flex",
                "title": "Barbearia",
                "body": "Cliente manda mensagem às 22h querendo agendar. Você não responde. Ele agenda no concorrente. <strong>Automação de WhatsApp teria fechado esse horário enquanto você dormia.</strong>"
            }),
            ("content", {
                "num": 3, "icon": "💪",
                "photo_query": "personal-trainer-gym-fitness",
                "photo_height": "450px",
                "title": "Personal Trainer",
                "body": "Você passa mais tempo cobrando mensalidade e enviando planilha do que treinando aluno. Com automação, <strong>o admin some e sobra só o que você sabe fazer</strong>."
            }),
            ("content", {
                "num": 4, "icon": "🛍️",
                "photo_query": "retail-store-shopping-commerce",
                "photo_height": "360px",
                "title": "Loja / Infoproduto",
                "body": "DM sem resposta é venda perdida. Fluxo automático responde, envia catálogo e faz follow-up de quem não comprou. <strong>Você vende mesmo quando está offline.</strong>"
            }),
            ("content", {
                "num": 5,
                "layout": "spotlight",
                "accent": "Não precisa de\ntech.\nPrecisa de\nprocesso.",
                "photo_query": "entrepreneur-laptop-startup",
                "title": "O que você precisa para começar",
                "body": "Sabe como você atende hoje? Isso é tudo que precisa. A gente pega esse processo e coloca pra rodar sozinho."
            }),
            ("content", {
                "num": 6,
                "layout": "heavy",
                "logo_domain": "whatsapp.com",
                "photo_query": "smartphone-message-notification",
                "title": "Por onde começa",
                "body": "WhatsApp Business com fluxo de agendamento ou atendimento inicial. É onde seu cliente já está — nenhuma mudança de hábito do lado dele.<br><br>Em uma semana você tem: <strong>saudação automática, qualificação de intenção e confirmação de agenda</strong> rodando sem você precisar estar online."
            }),
            ("cta", {
                "main": "Monta o sistema que <span>atende, agenda e vende</span> pelo seu negócio.",
                "sub": "Landing page + automação de WhatsApp + copy que converte — tudo junto, no ar em dias."
            }),
        ]
    },
    {
        "slug": "06-n8n-vai-acabar",
        "cover_photo_query": "futuristic-technology-abstract",
        "slides": [
            ("cover", {
                "headline": "O n8n foi a resposta certa para uma pergunta que mudou.",
                "subheadline": "A automação visual resolveu 2022. O que está chegando agora opera em outra camada.",
                "emoji": "⚡"
            }),
            ("content", {
                "num": 2,
                "layout": "standard",
                "photo_query": "n8n-workflow-sticky-notes",
                "photo_height": "flex",
                "title": "O problema do n8n não é o que você conecta. É o que some entre as conexões.",
                "body": "Nodes executam. Nodes terminam. O contexto morre ali.<br>Cada passo seguinte começa do zero — sem memória, sem raciocínio sobre o que acabou de acontecer.<br>Para fluxos lineares, funciona. Para decisões que dependem de decisões anteriores, <strong>o modelo quebra na raiz.</strong>"
            }),
            ("content", {
                "num": 3,
                "layout": "spotlight",
                "accent": "O n8n não falhou. Envelheceu.\nA própria empresa percebeu isso.\nEm 2024, reposicionou para 'plataforma de agentes' — e levantou $55M com esse argumento.",
                "title": "A virada",
                "body": ""
            }),
            ("content", {
                "num": 4,
                "layout": "data",
                "title": "A velocidade da mudança não é gradual. É exponencial.",
                "body": "Acurácia de agentes em tarefas reais de engenharia — SWE-bench",
                "chart": [
                    {"label": "Agentes — 2023",     "val": "22%",   "pct": 22, "color": "rgba(255,255,255,0.55)"},
                    {"label": "Agentes — fev/2026", "val": "72.5%", "pct": 72, "color": "#FF6B00"},
                    {"source": "SWE-bench — Anthropic Claude"},
                ]
            }),
            ("content", {
                "num": 5,
                "layout": "heavy",
                "photo_query": "api-code-integration",
                "photo_height": "flex",
                "title": "\"Mas o n8n tem APIs, dá pra integrar agentes nele.\"",
                "body": "Correto. E é exatamente isso que posiciona você como operador de infraestrutura terceira — enquanto quem constrói agentes nativos controla a lógica, a memória e o contexto inteiro da operação.<br><br><strong>79% das organizações já rodam agentes em produção (PwC, 2025).</strong> A janela de diferencial está fechando."
            }),
            ("cta", {
                "main": "Pare de aprender ferramenta. <span>Aprenda decisão.</span>",
                "sub": "A Triforce constrói agentes com contexto persistente — integra com o que você já usa, sem reescrever do zero."
            }),
        ]
    },

    # ── CARROSSEL 10 — Claude Opus 4.7 ─────────────────────────────────────────
    {
        "slug": "10-claude-opus-47",
        "cover_photo_query": "neural network glowing dark abstract intelligence",
        "cover_logo_domain": "anthropic.com",
        "cover_logo_name": "Anthropic",
        "slides": [
            ("cover", {
                "headline": "O modelo que alimenta o Claude Design acaba de chegar",
                "subheadline": "Claude Opus 4.7, lançado em 16/04/2026: 87,6% no SWE-bench, visão 3,75 MP e o modo xhigh que ninguém estava esperando",
            }),
            ("content", {
                "num": 2,
                "layout": "standard",
                "logo_domain": "anthropic.com",
                "photo_query": "performance benchmark chart improvement technology",
                "photo_height": "flex",
                "title": "O que mudou de verdade",
                "body": "Não foi atualização incremental. O Opus 4.7 resolve problemas que o 4.6 deixava para trás:<br><br><strong>SWE-bench Verified: 87,6%</strong> — alta de 6,8 pontos em uma versão só (findskill.ai, abr/2026)<br><strong>CursorBench: 70%</strong> — subiu de 58 para 70, o maior salto desde o lançamento do benchmark (theplanettools.ai, abr/2026)",
            }),
            ("content", {
                "num": 3,
                "layout": "data",
                "title": "Benchmarks lado a lado",
                "body": "SWE-bench Verified — tarefa real de engenharia de software",
                "chart": [
                    {"label": "Opus 4.7", "pct": 88, "val": "87,6%", "color": "#FF6B00"},
                    {"label": "Opus 4.6", "pct": 75, "val": "~75%",  "color": "rgba(255,255,255,0.35)"},
                    {"source": "SWE-bench Verified — buildFastWithAI, abr/2026"},
                ]
            }),
            ("content", {
                "num": 4,
                "layout": "standard",
                "photo_query": "high resolution camera lens detail precision technology",
                "photo_height": "flex",
                "title": "Visão que não existia antes",
                "body": "O 4.6 processava imagens até 1.024 px. O 4.7 vai até <strong>2.576 px nativos</strong>, com leitura real de 3,75 megapixels por chamada (findskill.ai, abr/2026)<br><br>Na prática: gráficos financeiros, plants de engenharia, wireframes de alta densidade, screenshots de produto inteiro — tudo analisado sem perder detalhe",
            }),
            ("content", {
                "num": 5,
                "layout": "spotlight",
                "accent": "xhigh:\nraciocínio\nentre high e max",
                "title": "", "body": "Novo nível de esforço exclusivo do 4.7: mais profundo que high, mais econômico que max. Para fluxos de agente que precisam de qualidade sem explodir o budget de tokens — é o ponto certo no meio do espectro (theplanettools.ai, abr/2026)",
            }),
            ("content", {
                "num": 6,
                "layout": "heavy",
                "photo_query": "workflow automation agent robot task management",
                "photo_height": "flex",
                "title": "Task budgets: agente com limite de gasto",
                "body": "Em beta público desde o lançamento: você define quanto o agente pode gastar por loop antes de parar e pedir confirmação.<br><br>Acabou a era do agente que vai embora e volta com uma fatura surpresa. <strong>Controle granular de custo operacional por tarefa</strong> — primeiro modelo da Anthropic com essa feature nativa (rawpickai.com, abr/2026)",
            }),
            ("content", {
                "num": 7,
                "layout": "heavy",
                "photo_query": "developer looking at pricing cost invoice screen",
                "photo_height": "flex",
                "title": "Preço igual, custo diferente",
                "body": "A tarifa oficial não mudou: <strong>$5 por milhão de tokens de entrada, $25 por saída</strong> — igual ao Opus 4.6 (verdent.ai, abr/2026)<br><br>Mas o novo tokenizador converte texto de forma diferente: o mesmo prompt custa entre <strong>10% e 35% a mais em tokens</strong> do que custava no 4.6. Antes de migrar em produção, rode seu prompt real e meça (tokenmix.ai, abr/2026)",
            }),
            ("content", {
                "num": 8,
                "layout": "spotlight",
                "accent": "Claude Design\nroda em cima\ndisso",
                "title": "", "body": "O Claude Design, lançado 24 horas antes do Opus 4.7, usa esse modelo como motor: visão 3,75 MP para ler screenshots e layouts, xhigh para raciocinar sobre componentes, task budget para não estourar o crédito do usuário. Não foi coincidência de data",
            }),
            ("content", {
                "num": 9,
                "layout": "heavy",
                "photo_query": "security lock restriction policy decision corporate",
                "photo_height": "flex",
                "title": "O que a Anthropic removeu de propósito",
                "body": "O Opus 4.7 teve capacidades de segurança ofensiva deliberadamente reduzidas em relação ao que os modelos internos já conseguem fazer (sangrokjung/claude-forge, abr/2026)<br><br>Não é limitação técnica — é decisão de política. A Anthropic publica o que escala com segurança, não o máximo absoluto do que o modelo é capaz",
            }),
            ("cta", {
                "main": "IA muda toda semana<br><span>A Triforce traz o que importa</span>",
                "sub": "Curadoria semanal de IA para pequenas empresas brasileiras — sem hype, com dado. Segue @triforceauto",
            }),
        ]
    },

    # ── CARROSSEL 09 — Claude Design ────────────────────────────────────────────
    {
        "slug": "09-claude-design",
        "cover_photo_query": "designer-focused-computer",
        "slides": [
            ("cover", {
                "headline": "A Anthropic lançou Claude Design.\nA Figma caiu 7% no mesmo dia.",
                "subheadline": "17/04/2026 — o que a ferramenta faz, o que ela ainda não faz, e por que o mercado já sentiu.",
            }),
            ("content", {
                "num": 2,
                "layout": "standard",
                "photo_query": "wireframe-sketch-ux-design",
                "photo_height": "flex",
                "title": "Não é gerador de imagem. É gerador de layout.",
                "body": "Você descreve o que quer — ou sobe um sketch, PDF, screenshot existente.<br><br>Claude constrói: protótipos de UI, slides, pitch decks, one-pagers. Exporta em <strong>React, HTML, PDF e PPTX</strong> — direto para produção.",
            }),
            ("content", {
                "num": 3,
                "layout": "spotlight",
                "accent": "Você descreve.\nClaude constrói.\nJá conectado ao\nseu GitHub.",
                "title": "", "body": "Ele lê o código-fonte do seu produto — fontes, componentes, estilos já existentes — e gera protótipos coerentes com o que você já tem em produção. Não é qualquer coisa bonita. É o que combina com o que você já tem.",
            }),
            ("content", {
                "num": 4,
                "layout": "standard",
                "photo_query": "stock-market-chart-falling",
                "photo_height": "flex",
                "title": "O mercado sentiu antes do lançamento.",
                "body": "Figma acumulava <strong>-28% em março de 2026</strong> — mínima de 52 semanas em US$ 17,65 dois dias antes do anúncio.<br><br>No dia do lançamento: <strong>mais -7%</strong>.<br><br>O mercado antecipou o impacto antes que a maioria dos designers soubesse que a ferramenta existia.",
            }),
            ("content", {
                "num": 5,
                "layout": "spotlight",
                "accent": "40% da sua cota.\nEm 1 hora.\nSem canvas colaborativo.\nSem handoff.",
                "title": "", "body": "Opus 4.7 consome créditos rápido. Plano Pro ($20/mês) bate no teto antes do fim do dia de trabalho. Sem edição em tempo real com equipe. Sem design tokens versionados. É geração conversacional — não ambiente de design profissional.",
            }),
            ("cta", {
                "main": "IA muda o jogo toda semana.<br><span>A Triforce traz o que importa.</span>",
                "sub": "Curadoria semanal de IA para pequenas empresas brasileiras — @triforceauto",
            }),
        ]
    },
    # ── CARROSSEL 12 — Gemini 3.1 Pro ──────────────────────────────────────────
    {
        'slug': '12-gemini-31-pro',
        'cover_photo_query': 'artificial intelligence neural network dark abstract',
        'cover_logo_domain': 'google.com',
        'slides': [
            ('cover', {
                'headline': 'O modelo que redefiniu o topo da IA em 2026',
                'subheadline': 'Gemini 3.1 Pro chega com benchmarks que ninguém esperava — e um preço que muda o jogo',
            }),
            ('content', {
                'num': 2,
                'layout': 'standard',
                'image_url': 'https://storage.googleapis.com/gweb-uniblog-publish-prod/original_images/gemini_3-1-pro__benchmarks.gif',
                'photo_fit': 'contain',
                'title': 'Os números oficiais do Google',
                'body': 'Comparação direta com Claude Opus 4.6 e GPT-5. O Gemini 3.1 Pro lidera em raciocínio, código e ciência — em alguns casos por margem expressiva <strong>(blog.google, fev/2026)</strong>',
            }),
            ('content', {
                'num': 3,
                'layout': 'spotlight',
                'accent': '77,1%',
                'title': '',
                'body': 'ARC-AGI-2: o benchmark mais difícil de raciocínio geral. Claude Opus 4.6 marcou 58,3%. A diferença é de quase 19 pontos (blog.google, fev/2026)',
            }),
            ('content', {
                'num': 4,
                'layout': 'heavy',
                'photo_query': 'small business owner laptop working focused',
                'photo_height': 'flex',
                'title': 'O que muda para o seu negócio',
                'body': 'Contexto de <strong>1 milhão de tokens</strong>, raciocínio ajustável em Low/Medium/High e performance de ponta. Projetos que antes travavam em limitações de contexto, agora rodam completos (blog.google, fev/2026)',
            }),
            ('content', {
                'num': 5,
                'layout': 'spotlight',
                'accent': '$2 / $12',
                'title': '',
                'body': 'Por 1M tokens — entrada e saída. Claude Opus 4.6 cobra $5/$25. O Gemini 3.1 Pro é até <strong>48% mais barato</strong> com desempenho superior (blog.google, fev/2026)',
            }),
            ('content', {
                'num': 6,
                'layout': 'heavy',
                'image_url': 'https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-3.1_pro_meta_dark.width-1300.png',
                'photo_fit': 'contain',
                'title': 'Onde os concorrentes ficaram',
                'body': 'GPT-5 fica 0,3 pontos atrás no GPQA Diamond. Claude empata no SWE-Bench, mas perde no preço e no raciocínio geral. O topo mudou de endereço (blog.google, fev/2026)',
            }),
            ('cta', {
                'main': 'Qual modelo a sua empresa usa hoje?',
                'sub': 'Comenta aqui ou manda mensagem — avaliamos o stack de IA do seu negócio',
            }),
        ]
    },

    # ── CARROSSEL 06 — Claude Design ────────────────────────────────────────────
    {
        "slug": "06-claude-design",
        "cover_photo_query": "anthropic claude AI interface dark editorial",
        "cover_logo_domain": "anthropic.com",
        "cover_logo_name": "Anthropic",
        "slides": [
            ("cover", {
                "headline": "IA que cria design — sem precisar saber design",
                "subheadline": "A Anthropic lançou o Claude Design: você escreve o que precisa, ele entrega o material pronto",
            }),
            ("content", {
                "num": 2,
                "layout": "heavy",
                "logo_domain": "anthropic.com",
                "image_url": "https://www-cdn.anthropic.com/images/4zrzovbb/website/499e91975d880b35eac6e48ad43161de7d10416c-2876x1614.jpg",
                "photo_height": "flex",
                "photo_fit": "contain",
                "title": "O que é o Claude Design",
                "body": "Lançado em <strong>17 de abril de 2026</strong>, o Claude Design transforma um prompt em protótipo, slide, one-pager ou material visual — sem precisar abrir o Canva, contratar designer ou saber uma linha de CSS."
            }),
            ("content", {
                "num": 3,
                "layout": "spotlight",
                "accent": "Lê a sua marca.\nAplica tudo.\nAutomático.",
                "title": "Como funciona por dentro",
                "body": "Roda sobre o <strong>Claude Opus 4.7</strong>. Você sobe o brand guide ou o codebase da empresa — ele lê as cores, a tipografia e os componentes, e aplica tudo sozinho. Sem ajuste manual."
            }),
            ("content", {
                "num": 4,
                "layout": "heavy",
                "photo_query": "stock market candlestick chart red financial crash",
                "photo_height": "flex",
                "title": "Exporta onde você precisa — e o mercado já sentiu",
                "body": "PDF, PPTX, HTML ou direto no Canva. No dia do lançamento, a ação da Figma <strong>caiu 7%</strong>. O mercado entendeu antes do usuário."
            }),
            ("content", {
                "num": 5,
                "layout": "standard",
                "photo_query": "person laptop presentation professional work",
                "photo_height": "560px",
                "photo_fit": "cover",
                "title": "Quem pode usar agora",
                "body": "Disponível para planos <strong>Pro, Max, Team e Enterprise</strong>. Páginas que precisavam de 20+ prompts ficaram prontas com 2.<br><br>Para dono de barbearia que precisa de flyer, personal que quer proposta bonita ou infoprodutor que cria slides — isso é designer no bolso."
            }),
            ("content", {
                "num": 6,
                "layout": "heavy",
                "photo_query": "abstract technology market disruption digital network",
                "photo_height": "540px",
                "photo_fit": "cover",
                "title": "O que isso muda no mercado",
                "body": "O Claude Design faz parte do <strong>Anthropic Labs</strong> — coloca a Anthropic competindo direto com Figma e Canva. Ainda em research preview, acesso gradual.<br><br>Quando abrir para o plano gratuito, o comportamento de pequenos negócios muda."
            }),
            ("cta", {
                "main": "Você ainda paga designer para montar <span>material que IA já faz</span>?",
                "sub": "A Triforce entrega LP, copy estruturada e sistema no ar — tudo junto, sem gambiarra."
            }),
        ]
    },

    # ── CARROSSEL — Guerra do Irã e IA ─────────────────────────────────────────
    {
        "slug": "guerra-ira-impacto-ia",
        "cover_photo_query": "war explosion fire digital network dark cinematic dramatic",
        "slides": [
            ("cover", {
                "headline": "A IA virou arma. E virou alvo.",
                "subheadline": "O que a guerra do Irã está fazendo com a infraestrutura que você usa todo dia",
            }),
            ("content", {
                "num": 2, "layout": "standard",
                "photo_query": "dark war room intelligence screens surveillance technology",
                "photo_height": "flex",
                "title": "IA escolheu os alvos da guerra",
                "body": "No primeiro dia dos ataques ao Irã, os EUA usaram o <strong>Maven Smart System</strong> para identificar 1.000 alvos militares. A IA decidiu onde as bombas cairiam. Não analistas humanos. (CNN Brasil, mar/2026)",
            }),
            ("content", {
                "num": 3, "layout": "standard",
                "photo_query": "destroyed technology hardware ruins dark smoke",
                "photo_height": "flex",
                "title": "Primeiro ataque militar a um data center na história",
                "body": "Em 1 de março de 2026, drones iranianos Shahed atingiram <strong>3 data centers da AWS</strong> nos EAU e no Bahrein. Bancos, pagamentos e apps saíram do ar. Oracle Dubai também foi atacada. (CNBC, mar/2026)",
            }),
            ("content", {
                "num": 4, "layout": "spotlight",
                "accent": "Google. Microsoft.\nApple. Nvidia.\nOracle e mais 13",
                "title": "Na lista oficial de alvos da Guarda Revolucionária do Irã",
                "body": "",
            }),
            ("content", {
                "num": 5, "layout": "standard",
                "photo_query": "semiconductor chip wafer silicon helium laboratory manufacturing close up",
                "photo_height": "flex",
                "title": "O mineral que você nunca ouviu falar pode encarecer sua IA",
                "body": "Hélio e bromo são essenciais para fabricar chips de IA e vêm do Oriente Médio. O preço do hélio <strong>dobrou</strong>. Samsung e SK Hynix perderam mais de $200 bilhões em capitalização. (DW / Morningstar, mar/2026)",
            }),
            ("content", {
                "num": 6, "layout": "standard",
                "photo_query": "oil barrels crude petroleum energy price rise global supply disruption",
                "photo_height": "flex",
                "title": "Petróleo a $126 por barril significa IA mais cara para você",
                "body": "Data centers de IA consomem energia massiva. Com o petróleo disparado, operar esses servidores ficou muito mais caro. O <strong>Estreito de Ormuz</strong> controla 20% do petróleo global. (Business Insider / JP Morgan, mar/2026)",
            }),
            ("content", {
                "num": 7, "layout": "standard",
                "photo_query": "small business owner concerned laptop screen cafe worried",
                "photo_height": "flex",
                "title": "O que muda para quem usa IA no negócio",
                "body": "ChatGPT, Claude e Midjourney dependem de chips e data centers. Quando energia e matéria-prima ficam mais caras, as big techs repassam para você. <strong>Isso já está acontecendo.</strong> (PikaAINews, mar/2026)",
            }),
            ("cta", {
                "main": "Salva esse post<br><span>e segue pra mais conteúdo assim</span>",
                "sub": "Curadoria semanal de IA para o seu negócio. @triforceauto",
            }),
        ]
    },

    # ── CARROSSEL — Anthropic Padres Claude ─────────────────────────────────────
    {
        "slug": "anthropic-padres-claude",
        "cover_photo_query": "priest religious leader dark dramatic cinematic",
        "slides": [
            ("cover", {
                "headline": "A Anthropic contratou padres para ensinar o Claude",
                "subheadline": "O que isso diz sobre a empresa mais importante da IA agora",
            }),
            ("content", {
                "num": 2, "layout": "standard",
                "image_url": "https://i.gzn.jp/img/2026/04/13/anthropic-asked-christian-leaders/00_m.jpg",
                "photo_fit": "cover",
                "photo_height": "flex",
                "title": "Summit de 2 dias com 15 líderes religiosos",
                "body": "Em março de 2026, a Anthropic reuniu <strong>15 líderes cristãos</strong> em São Francisco para um summit de dois dias. A pauta: ajudar a moldar o comportamento moral do Claude. A empresa vale <strong>US$ 380 bilhões</strong>. (The Atlantic, mar/2026)",
            }),
            ("content", {
                "num": 3, "layout": "standard",
                "photo_query": "catholic priest collar thoughtful portrait serious professional",
                "photo_height": "flex",
                "title": "Quem foi convidado para o evento",
                "body": "Entre os participantes: o padre católico <strong>Brendan McGuire</strong>, capelão de universidade em San Jose, e <strong>Brian Patrick Green</strong>, pesquisador jesuíta de ética tecnológica. Teólogos com décadas de prática sendo consultados por engenheiros de IA. (The Atlantic, mar/2026)",
            }),
            ("content", {
                "num": 4, "layout": "spotlight",
                "accent": "O Claude é\nfilho de Deus?",
                "title": "A pergunta que parou a sala durante o summit",
                "body": "",
            }),
            ("content", {
                "num": 5, "layout": "heavy",
                "image_url": "https://the-decoder.com/wp-content/uploads/2026/04/anthropic_holy_cross.png",
                "photo_fit": "contain",
                "photo_height": "flex",
                "title": "A pergunta que a Anthropic não consegue responder sozinha",
                "body": "Os líderes religiosos debateram se Claude teria alguma forma de dignidade moral. Um dos padres levantou: se o Claude foi criado à imagem do pensamento humano, o que isso implica? A Anthropic não respondeu. Trouxe especialistas para ajudar a formular a pergunta certa. (The Atlantic, mar/2026)",
            }),
            ("content", {
                "num": 6, "layout": "standard",
                "photo_query": "humanoid robot contemplative light shadow ethereal digital concept art",
                "photo_height": "flex",
                "title": "Por que a Anthropic foi buscar padres",
                "body": "A empresa quer garantir que o Claude <strong>se comporte bem</strong>, mas a engenharia não resolve tudo. Questões como empatia, limites morais e dignidade humana têm respostas que a teologia desenvolveu em 2.000 anos. Ignorar isso seria arrogância técnica. (MIT Technology Review, mar/2026)",
            }),
            ("content", {
                "num": 7, "layout": "standard",
                "photo_query": "person laptop window cafe thinking focused working",
                "photo_height": "flex",
                "title": "O que muda para quem usa o Claude todo dia",
                "body": "Cada recusa do Claude, cada limite que ele impõe, cada decisão ética, essas regras não vieram só de engenheiros. Agora têm input de teólogos. A IA que você usa para trabalhar foi <strong>moldada por padres</strong>. Isso é novo. E importa saber. (The Atlantic / MIT Tech Review, mar/2026)",
            }),
            ("cta", {
                "main": "Salva esse post<br><span>e segue pra mais conteúdo assim</span>",
                "sub": "Curadoria semanal de IA para o seu negócio. @triforceauto",
            }),
        ]
    },

    # ── CARROSSEL mundo-skills-ia ───────────────────────────────────────────────
    {
        "slug": "mundo-skills-ia",
        "cover_photo_query": "dark abstract digital technology circuit lines glowing orange blue cinematic editorial",
        "slides": [
            ("cover", {
                "headline": "Não é mais sobre qual IA usar, é sobre qual skill mandar trabalhar por você",
                "subheadline": "GPT Store. Claude Skills. Gemini Gems. O ecossistema que vai mudar como você trabalha em 2026",
            }),
            ("content", {
                "num": 2, "layout": "standard",
                "photo_query": "hands holding phone app data analytics coffee table warm light business",
                "photo_height": "flex",
                "title": "GPT Store: os números que ninguém esperava",
                "body": "A GPT Store ultrapassou <strong>3 milhões de GPTs criados</strong> desde janeiro de 2024. O ChatGPT chegou a <strong>800 milhões de usuários ativos semanais</strong> em outubro de 2025. (OpenAI, out/2025)",
            }),
            ("content", {
                "num": 3, "layout": "heavy",
                "image_url": "https://www-cdn.anthropic.com/images/4zrzovbb/website/a056db8301f67466de34a19181e7428ec6b6e17f-1920x2500.png",
                "photo_fit": "contain",
                "photo_bg": "#FFFFFF",
                "photo_height": "flex",
                "title": "MCP: o protocolo que virou padrão da indústria",
                "body": "Em <strong>16 meses</strong>, o MCP da Anthropic atingiu <strong>97 milhões de downloads mensais</strong> e <strong>10.000+ servidores públicos ativos</strong>. Em março de 2026, a Anthropic doou o MCP para a Linux Foundation, com apoio de OpenAI, Google, Microsoft e AWS. (Anthropic, mar/2026)",
            }),
            ("content", {
                "num": 4, "layout": "spotlight",
                "accent": "A pergunta certa\nnão é mais\n'você usa IA?'",
                "title": "",
                "body": "É: você tem uma skill trabalhando por você agora?",
            }),
            ("content", {
                "num": 5, "layout": "heavy",
                "photo_query": "Three lanes highway night aerial drone view different colored light trails dark background orange red blue cinematic",
                "photo_height": "flex",
                "title": "Três ecossistemas, uma disputa",
                "body": "ChatGPT lidera com <strong>68% de market share mobile</strong>. Gemini, <strong>18,2%</strong>. Claude gera <strong>61% mais receita por usuário mobile</strong> que o Gemini. GPT Store: <strong>3M+ GPTs</strong>. Gemini Gems: integrado ao Workspace. Claude Skills + MCP: <strong>10.000+ servidores</strong>, open source, cross-platform. (Cohen et al., dez/2025)",
            }),
            ("content", {
                "num": 6, "layout": "standard",
                "photo_query": "small business owner phone messaging customer service warm light",
                "photo_height": "flex",
                "title": "O que a IA já fez pelos pequenos negócios",
                "body": "<strong>91% dos pequenos negócios</strong> que usam IA reportam aumento de receita. Quem adotou IA viu <strong>2x de lift de receita</strong> e <strong>60% menos tempo</strong> em tarefas repetitivas no primeiro ano. (Salesforce, dez/2024)",
            }),
            ("content", {
                "num": 7, "layout": "heavy",
                "photo_query": "server rack datacenter cables LED lights colorful modern technology",
                "photo_height": "flex",
                "title": "O que vem no roadmap de 2026",
                "body": "MCP 2026 inclui triggers automáticos, streaming e tarefas de longa duração. O Gartner projeta <strong>40% dos apps empresariais com agentes de IA</strong> até o fim de 2026, contra <strong>menos de 5% hoje</strong>. (Anthropic/Gartner, jan/2026)",
            }),
            ("cta", {
                "main": "Salva esse post<br><span>e segue pra mais conteúdo assim</span>",
                "sub": "Curadoria semanal de IA para o seu negócio.\n@triforceauto",
            }),
        ]
    },

    # ── CARROSSEL 11 — Claude Opus 4.7 ─────────────────────────────────────────
    {
        "slug": "11-claude-opus-47",
        "cover_photo_query": "dark abstract neural network technology deep",
        "cover_logo_domain": "anthropic.com",
        "slides": [
            ("cover", {
                "headline": "O modelo mais capaz da Anthropic acaba de chegar",
                "subheadline": "16/04/2026 — Opus 4.7 com 1M de contexto, visão 3x mais precisa e novo nível de raciocínio",
            }),
            ("content", {
                "num": 2,
                "layout": "heavy",
                "image_url": "https://www-cdn.anthropic.com/images/4zrzovbb/website/d434d15757c6abac1122af483617741776d5a114-2600x2638.png",
                "title": "O que a Anthropic publicou oficialmente",
                "body": "Tabela completa de benchmarks: <strong>87,6% no SWE-bench</strong> (código), 94,2% raciocínio nível pós-graduação, 78% uso agêntico de computador, 77,3% uso escalado de ferramentas (anthropic.com, abr/2026)",
            }),
            ("content", {
                "num": 3,
                "layout": "spotlight",
                "accent": "Visão:\n54% para 98%",
                "title": "", "body": "CharXiv Reasoning com ferramentas: Opus 4.6 lia gráficos e imagens com 84,7% de precisão. O 4.7 sobe para 91%. Sem ferramentas: salta de 69,1% para 82,1%. O modelo agora lê o que você manda — invoice, screenshot, planilha escaneada (anthropic.com, abr/2026)",
            }),
            ("content", {
                "num": 4,
                "layout": "standard",
                "photo_query": "person analyzing documents charts screen office",
                "title": "O que essa visão muda na prática",
                "body": "Você manda uma foto do cardápio, da planilha, do extrato bancário ou do produto físico. O modelo lê de verdade — não interpreta, não alucina os números.<br><br>Para automações: agentes que operam computador subiram de 72,7% para <strong>78% de precisão real no OSWorld</strong> (anthropic.com, abr/2026)",
            }),
            ("content", {
                "num": 5,
                "layout": "spotlight",
                "accent": "xhigh:\nentre high e max",
                "title": "", "body": "Novo nível de raciocínio exclusivo do 4.7: mais profundo que high, mais econômico que max. Virou o padrão do Claude Code em todos os planos. Para quem usa agentes: mais qualidade sem estourar o orçamento de tokens",
            }),
            ("content", {
                "num": 6,
                "layout": "heavy",
                "image_url": "https://www-cdn.anthropic.com/images/4zrzovbb/website/3a5b5c3eedb539fe20bc8dd1ecfc952c447000b8-1920x1080.png",
                "title": "Mais capaz e com menos comportamento desalinhado",
                "body": "O gráfico oficial mostra: Opus 4.7 tem índice de misalignment <strong>abaixo do Opus 4.6</strong> — o modelo mais capaz da linha é também mais seguro que o anterior (anthropic.com, abr/2026)<br><br>Preço: $5/$25 por milhão de tokens de entrada/saída — mesmo preço do 4.6",
            }),
            ("cta", {
                "main": "IA muda toda semana<br><span>A Triforce traz o que importa</span>",
                "sub": "Curadoria semanal de IA para pequenas empresas brasileiras — @triforceauto",
            }),
        ]
    },
]




# ─── GERADOR ───────────────────────────────────────────────────────────────────

CACHE_DIR = Path(__file__).parent / "banco-de-imagens"
CACHE_DIR.mkdir(exist_ok=True)

UNSPLASH_ACCESS_KEY = "cG06jiqCb_3v5NuSIKAjRcjQUJmQH6yv3q8GsEMiy-k"


def search_unsplash(query: str) -> str | None:
    """Busca foto no Unsplash por texto e retorna URL do CDN pronta para uso."""
    import json, urllib.request, urllib.parse
    params = urllib.parse.urlencode({
        "query": query,
        "per_page": 1,
        "orientation": "portrait",
        "client_id": UNSPLASH_ACCESS_KEY,
    })
    try:
        req = urllib.request.Request(
            f"https://api.unsplash.com/search/photos?{params}",
            headers={"Accept-Version": "v1"}
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read())
        results = data.get("results", [])
        if not results:
            return None
        raw_url = results[0]["urls"]["raw"]
        # strip existing params e adiciona os nossos
        base = raw_url.split("?")[0]
        return f"{base}?w=1080&h=1350&fit=crop&auto=format&q=85"
    except Exception as e:
        print(f"    [unsplash api] erro: {e}")
        return None

# URLs de logos para os slides internos — baixados pelo Playwright
LOGO_URLS = {
    "meta.com":      "https://logo.clearbit.com/meta.com?size=256",
    "anthropic.com": "https://logo.clearbit.com/anthropic.com?size=256",
    "openai.com":    "https://logo.clearbit.com/openai.com?size=256",
    "google.com":    "https://logo.clearbit.com/google.com?size=256",
    "whatsapp.com":  "https://logo.clearbit.com/whatsapp.com?size=256",
    "ramp.com":      "https://logo.clearbit.com/ramp.com?size=256",
    "n8n.io":        "https://logo.clearbit.com/n8n.io?size=256",
}

# IDs verificados do Unsplash — relevantes ao tema de cada carrossel
COVER_PHOTOS = {
    "01-meta-muse-spark":     "https://images.unsplash.com/photo-1609921141835-710b7fa6e438?w=1080&h=1350&fit=crop&auto=format&q=85",
    "02-anthropic-sp":        "https://images.unsplash.com/photo-1519501025264-65ba15a82390?w=1080&h=1350&fit=crop&auto=format&q=85",
    "03-claude-mythos":       "https://images.unsplash.com/photo-1614064641938-3bbee52942c7?w=1080&h=1350&fit=crop&auto=format&q=85",
    "04-claude-vs-chatgpt":   "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=1080&h=1350&fit=crop&auto=format&q=85",
    "05-ia-pequenos-negocios":"https://images.unsplash.com/photo-1503951914875-452162b0f3f1?w=1080&h=1350&fit=crop&auto=format&q=85",
    "06-n8n-vai-acabar":     "https://images.unsplash.com/photo-1758876021444-3885d0a2539f?w=1080&h=1350&fit=crop&auto=format&q=85",
    "09-claude-design":      "https://images.unsplash.com/photo-1569012871812-f38ee64cd54c?w=1080&h=1350&fit=crop&auto=format&q=85",
    "12-gemini-31-pro":      "https://images.unsplash.com/photo-1638136264464-2711f0078d1e?w=1080&h=1350&fit=crop&auto=format&q=85",
    "anthropic-padres-claude": "https://gizmodo.com/app/uploads/2026/04/matrix-praying.jpg",
    "mundo-skills-ia":         "https://images.unsplash.com/photo-1655900298997-610bf4254578?w=1080&h=1350&fit=crop&auto=format&q=85",
}


# IDs CDN do Unsplash — só o ID numérico (sem prefixo photo-)
SLIDE_PHOTO_IDS = {
    "social-media-app-smartphone":        "1432888498266-38ffec3eaf0a",
    "whatsapp-chat-messaging":            "1600880292203-757bb62b4baf",
    "small-business-owner-customer":      "1556742049-0cfed4f6a45d",
    "question-uncertainty-thinking":      "1454165804606-c3d57bc86b40",
    "artificial-intelligence-technology": "1677442135703-1787eea5ce01",
    "brazil-business-office-work":        "1554224155-6726b3ff858f",
    "open-door-opportunity-light":        "1441986300917-64674bd600d8",
    "neural-network-brain-ai":            "1620712943543-bcc4688e7485",
    "security-restricted-access-lock":    "1555949963-ff9fe0c870eb",
    "futuristic-technology-abstract":     "1518770660439-4636190af475",
    "data-analytics-chart-growth":        "1460925895917-afdab827c52f",
    "corporate-office-meeting-team":      "1497366811353-6870744d04b2",
    "comparison-balance-choice":          "1551836022-deb4988cc6c0",
    "strategy-decision-thinking-business":"1529699211952-734e80c4d42b",
    "barber-scissors-haircut":            "1562004760-aceed7bb0fe3",
    "personal-trainer-gym-fitness":       "1534438327276-14e5300c3a48",
    "retail-store-shopping-commerce":     "1441986300917-64674bd600d8",
    "entrepreneur-laptop-startup":        "1516321318423-f06f85e504b3",
    "smartphone-message-notification":    "1511707171634-5f897ff02aa9",
    "n8n-workflow-sticky-notes":          "1758876021444-3885d0a2539f",
    "api-code-integration":               "1623282033815-40b05d96c903",
    "designer-focused-computer":          "1569012871812-f38ee64cd54c",
    "wireframe-sketch-ux-design":         "1522542550221-31fd19575a2d",
    "stock-market-chart-falling":         "1611974789855-9c2a0a7236a3",
    "small business owner laptop working focused":  "1598221860268-4c711f099b6d",
    "laptop computer screen code data technology dark": "1555066931-4365d14bab8c",
    "stock market chart falling financial crash":        "1611974789855-9c2a0a7236a3",
    "stock market candlestick chart red financial crash": "1745270917331-787c80129680",
    "person laptop presentation professional work":      "1594579254798-868734c3ed32",
    "abstract technology market disruption digital network": "1653119574903-ae9c3204bc35",
    "roundtable summit discussion diverse leaders serious meeting": "1561489413-985b06da5bee",
    "catholic priest collar thoughtful portrait serious professional": "1711786005061-3687e056b9e3",
    "open bible desk laptop books study warm light":                  "1642901798261-667a915d1022",
    "humanoid robot contemplative light shadow ethereal digital concept art": "1578920103364-21678e392488",
    "person laptop window cafe thinking focused working":             "1635694167659-8a6491a6912b",
    "hands holding phone app data analytics coffee table warm light business": "1746014602412-a51f37a46675",
    "server rack datacenter cables LED lights colorful modern technology":    "1561233835-f937539b95b9",
    "Overhead flat lay smartphone showing ChatGPT interface dark surface small business tools notebook coffee keys calculator warm orange accent lighting": "1698934688788-ee485a6f601f",
    "Three lanes highway night aerial drone view different colored light trails dark background orange red blue cinematic": "1568516816247-5b38bf5c238f",
    "Small barbershop owner at counter smiling at phone AI chat interface on screen natural daylight warm tones candid documentary": "1666855181417-812fa8503f85",
    "small business owner phone messaging customer service warm light": "1551989745-8ac16ba81d78",
    "Futuristic dark control room multiple screens automated workflows empty chair neon blue orange accent lighting high tech cinematic": "1688413399578-14ebdde3666a",
}


async def download_slide_photos(browser, carroseis: list) -> dict:
    """Baixa fotos dos slides.

    Prioridade por slide:
      1. image_url   — URL direta de imagem (logo, screenshot de artigo, gráfico oficial)
                       Baixa com urllib, sem browser, sem proteção anti-bot.
                       Exemplo: logo do Claude, gráfico do SWE-bench, imagem de press kit.
      2. photo_query — texto livre → Unsplash API → CDN
    """
    photos = {}
    page = await browser.new_page(viewport={"width": 1080, "height": 1350})

    # ── image_url: download direto via urllib (sem Playwright) ─────────────────
    import urllib.request as _urllib
    print("\nBaixando imagens diretas (image_url)...")
    for c in carroseis:
        for slide_type, data in c["slides"]:
            if slide_type != "content":
                continue
            url = data.get("image_url")
            if not url:
                continue
            safe = re.sub(r"[^a-z0-9]", "_", url)[:60]
            ext  = "png" if url.lower().endswith(".png") else "jpg"
            cache_file = CACHE_DIR / f"direct_{safe}.{ext}"
            if cache_file.exists() and cache_file.stat().st_size > 5_000:
                photos[url] = str(cache_file)
                print(f"  [cache] {url[:70]}")
                continue
            try:
                req = _urllib.Request(url, headers={"User-Agent": "Mozilla/5.0"})
                with _urllib.urlopen(req, timeout=15) as r:
                    body = r.read()
                cache_file.write_bytes(body)
                photos[url] = str(cache_file)
                print(f"  [ok] {url[:70]} ({len(body)//1024} KB)")
            except Exception as e:
                print(f"  [erro] {url[:70]} — {e}")

    # ── photo_query: Unsplash API ───────────────────────────────────────────────
    # Coleta todas as photo_queries usadas nos carrosséis
    queries_needed = set()
    for c in carroseis:
        for slide_type, data in c["slides"]:
            if slide_type == "content" and data.get("photo_query"):
                queries_needed.add(data["photo_query"])

    print("\nBaixando fotos dos slides (Unsplash)...")

    for query in queries_needed:
        safe_name = re.sub(r"[^a-z0-9\-]", "_", query)[:50]
        cache_file = CACHE_DIR / f"slide_{safe_name}.jpg"

        if cache_file.exists() and cache_file.stat().st_size > 30_000:
            photos[query] = str(cache_file)
            print(f"  [cache] {query}")
            continue

        # Tenta dicionário fixo primeiro, depois API
        if query in SLIDE_PHOTO_IDS:
            url = f"https://images.unsplash.com/photo-{SLIDE_PHOTO_IDS[query]}?w=1080&h=1350&fit=crop&auto=format&q=85"
            print(f"  [dict] {query}")
        else:
            print(f"  [api] buscando: {query}")
            url = search_unsplash(query)
            if not url:
                print(f"    sem resultado — pulando")
                continue
            print(f"    encontrou: {url[:80]}...")

        try:
            resp = await page.goto(url, wait_until="load", timeout=20000)
            if resp and resp.ok:
                body = await resp.body()
                cache_file.write_bytes(body)
                photos[query] = str(cache_file)
                print(f"    OK ({len(body) // 1024} KB)")
            else:
                print(f"    falhou status={resp.status if resp else '?'}")
        except Exception as e:
            print(f"    erro: {e}")

    await page.close()
    return photos


async def download_logos(browser) -> dict:
    """Baixa logos das empresas via Clearbit e cacheia como base64."""
    logos = {}
    page = await browser.new_page(viewport={"width": 400, "height": 400})

    print("\nBaixando logos das empresas...")
    for domain, url in LOGO_URLS.items():
        cache_file = CACHE_DIR / f"logo_{domain.replace('.', '_')}.png"

        if cache_file.exists() and cache_file.stat().st_size > 500:
            raw = cache_file.read_bytes()
            logos[domain] = f"data:image/png;base64,{base64.b64encode(raw).decode()}"
            print(f"  [cache] {domain}")
            continue

        try:
            resp = await page.goto(url, wait_until="load", timeout=15000)
            if resp and resp.ok:
                body = await resp.body()
                cache_file.write_bytes(body)
                logos[domain] = f"data:image/png;base64,{base64.b64encode(body).decode()}"
                print(f"  [fetch] {domain} OK ({len(body)//1024} KB)")
            else:
                print(f"  [fetch] {domain} FALHOU {resp.status if resp else '?'}")
        except Exception as e:
            print(f"  [fetch] {domain} FALHOU: {e}")

    await page.close()
    return logos


async def download_cover_photos(browser) -> dict:
    """Baixa fotos de cover — URL direta do dicionário ou busca automática via Unsplash API."""
    cached = {}
    page = await browser.new_page(viewport={"width": 1080, "height": 1350})

    print("\nBaixando fotos de cover (Unsplash)...")

    # Coleta slugs de todos os carrosséis
    slugs = [c["slug"] for c in CARROSEIS]

    for slug in slugs:
        cache_file = CACHE_DIR / f"cover_{slug}.jpg"

        if cache_file.exists() and cache_file.stat().st_size > 30_000:
            cached[slug] = str(cache_file)
            print(f"  [cache] {slug}")
            continue

        # URL fixa no dicionário → usa direto
        if slug in COVER_PHOTOS:
            url = COVER_PHOTOS[slug]
            print(f"  [dict] {slug}")
        else:
            # Busca via API usando cover_photo_query do carrossel
            query = next((c.get("cover_photo_query", slug) for c in CARROSEIS if c["slug"] == slug), slug)
            print(f"  [api] buscando cover: {query}")
            url = search_unsplash(query)
            if not url:
                print(f"    sem resultado — pulando")
                continue
            print(f"    encontrou: {url[:80]}...")

        try:
            resp = await page.goto(url, wait_until="load", timeout=25000)
            if resp and resp.ok:
                body = await resp.body()
                with open(cache_file, "wb") as f:
                    f.write(body)
                cached[slug] = str(cache_file)
                print(f"    OK ({len(body)//1024} KB)")
            else:
                print(f"    FALHOU status={resp.status if resp else '?'}")
        except Exception as e:
            print(f"    FALHOU: {e}")

    await page.close()
    return cached


async def capture_screenshots(browser, carroseis: list) -> dict:
    """Captura screenshots de URLs reais (tweets, interfaces, charts) via Playwright.

    No slide, use:
        "screenshot_url": "https://twitter.com/soraofficial/status/..."
        "screenshot_selector": "article[data-testid='tweet']"  # opcional — clip um elemento

    Se não houver screenshot_url em nenhum slide, retorna {} sem abrir página.
    """
    urls_needed = {}
    for c in carroseis:
        if c.get("cover_screenshot_url"):
            urls_needed[c["cover_screenshot_url"]] = c.get("cover_screenshot_selector")
        for slide_type, data in c["slides"]:
            if slide_type == "content" and data.get("screenshot_url"):
                url = data["screenshot_url"]
                urls_needed[url] = data.get("screenshot_selector")

    if not urls_needed:
        return {}

    shots = {}
    page = await browser.new_page(viewport={"width": 1080, "height": 1350})
    print("\nCapturando screenshots de URLs reais...")

    for url, selector in urls_needed.items():
        safe_name = re.sub(r"[^a-z0-9]", "_", url)[:60]
        cache_file = CACHE_DIR / f"screenshot_{safe_name}.jpg"

        if cache_file.exists() and cache_file.stat().st_size > 10_000:
            shots[url] = str(cache_file)
            print(f"  [cache] {url[:70]}")
            continue

        try:
            print(f"  [screenshot] {url[:70]}")
            await page.goto(url, wait_until="networkidle", timeout=30000)
            await page.wait_for_timeout(2000)  # espera JS extra

            if selector:
                el = await page.query_selector(selector)
                if el:
                    img_bytes = await el.screenshot(type="jpeg", quality=90)
                else:
                    img_bytes = await page.screenshot(
                        type="jpeg", quality=90,
                        clip={"x": 0, "y": 0, "width": 1080, "height": 1350}
                    )
            else:
                img_bytes = await page.screenshot(
                    type="jpeg", quality=90,
                    clip={"x": 0, "y": 0, "width": 1080, "height": 1350}
                )

            cache_file.write_bytes(img_bytes)
            shots[url] = str(cache_file)
            print(f"    OK ({len(img_bytes) // 1024} KB)")
        except Exception as e:
            print(f"    FALHOU: {e}")

    await page.close()
    return shots


async def generate_slide(page, html, output_path):
    await page.set_content(html, wait_until="networkidle")
    await page.screenshot(path=str(output_path), clip={"x": 0, "y": 0, "width": 1080, "height": 1350})
    print(f"  OK {output_path.name}")


async def main():
    print("\nTriforce Auto - Gerador de Carrosseis")

    async with async_playwright() as p:
        browser = await p.chromium.launch()

        # Etapa 1: baixar logos, fotos de cover e fotos por slide via Chromium
        logos = await download_logos(browser)
        # Logos pré-cacheados (baixados fora do Playwright)
        import base64 as _b64
        for _domain, _fname in [("n8n.io", "logo_n8n_io.png")]:
            _p = CACHE_DIR / _fname
            if _p.exists() and _domain not in logos:
                logos[_domain] = f"data:image/png;base64,{_b64.b64encode(_p.read_bytes()).decode()}"
        cover_photos = await download_cover_photos(browser)
        slide_photos = await download_slide_photos(browser, CARROSEIS)
        screenshots  = await capture_screenshots(browser, CARROSEIS)

        # Etapa 2: gerar slides
        print("\nGerando slides...")
        page = await browser.new_page(viewport={"width": 1080, "height": 1350})

        for carousel in CARROSEIS:
            slug = carousel["slug"]
            carousel_dir = OUTPUT_DIR / slug
            carousel_dir.mkdir(exist_ok=True)
            print(f"\nCarrossel {slug}")

            for i, (slide_type, data) in enumerate(carousel["slides"]):
                slide_num = i + 1
                output_path = carousel_dir / f"slide-{str(slide_num).zfill(2)}.png"

                if slide_type == "cover":
                    cover_bg = (
                        screenshots.get(carousel.get("cover_screenshot_url")) or
                        cover_photos.get(slug)
                    )
                    html = cover_slide(
                        data["headline"], data["subheadline"], slide_num,
                        logo_domain=carousel.get("cover_logo_domain"),
                        bg_file=cover_bg
                    )

                elif slide_type == "content":
                    logo_domain = data.get("logo_domain")
                    # prioridade: image_url > screenshot_url > photo_query > cover fallback
                    slide_photo = (
                        slide_photos.get(data.get("image_url")) or
                        screenshots.get(data.get("screenshot_url")) or
                        slide_photos.get(data.get("photo_query")) or
                        cover_photos.get(slug)
                    )
                    html = content_slide(
                        data["num"], data["title"], strip_sources(data["body"]),
                        logo_domain=logo_domain,
                        logo_b64=logos.get(logo_domain),
                        bg_file=slide_photo,
                        layout=data.get("layout", "standard"),
                        chart=data.get("chart"),
                        accent=data.get("accent"),
                        photo_height=data.get("photo_height"),
                        photo_fit=data.get("photo_fit", "cover"),
                        photo_bg=data.get("photo_bg", "#0A0A0A"),
                    )

                elif slide_type == "cta":
                    html = cta_slide(data["main"], data["sub"])

                await generate_slide(page, html, output_path)

        await browser.close()

    total = sum(len(c["slides"]) for c in CARROSEIS)
    print(f"\nPronto! {total} slides em {len(CARROSEIS)} carrosseis")
    print(f"   {OUTPUT_DIR}")


if __name__ == "__main__":
    asyncio.run(main())
