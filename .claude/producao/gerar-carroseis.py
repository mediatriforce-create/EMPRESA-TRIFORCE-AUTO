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
.header-handle { font-size:18px; font-weight:700; color:#FF6B00; }
.header-mid    { font-size:17px; font-weight:500; color:#aaa; }
.header-right  { font-size:17px; font-weight:400; color:#bbb; }
.content {
  flex: 1; display: flex; flex-direction: column;
  justify-content: flex-start; gap: 24px;
  min-height: 0; overflow: hidden;
}
h2 {
  font-size: 56px; font-weight: 900; color: #0A0A0A;
  line-height: 1.08; letter-spacing: -0.03em; margin: 0;
}
.body { font-size:27px; font-weight:400; color:#2a2a2a; line-height:1.62; margin:0; }
.body strong { font-weight:700; color:#0A0A0A; }
.footer {
  display: flex; align-items: center; justify-content: space-between;
  margin-top: 28px; padding-top: 20px;
  border-top: 1.5px solid rgba(10,10,10,0.10); flex-shrink: 0;
}
.footer-left { display:flex; align-items:center; gap:12px; }
.footer-avatar {
  width:36px; height:36px; border-radius:50%;
  background:#FF6B00; display:flex; align-items:center; justify-content:center; flex-shrink:0;
}
.footer-name   { font-size:17px; font-weight:800; color:#0A0A0A; }
.footer-handle { font-size:14px; font-weight:400; color:#999; }
.swipe { font-size:16px; font-weight:600; color:#FF6B00; }
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


def _img_box(logo_b64=None, bg_file=None, logo_domain=None, height="flex"):
    """Retorna HTML do bloco de imagem. height='flex' preenche espaço, ou valor CSS fixo."""
    h_style = "flex:1; min-height:240px;" if height == "flex" else f"height:{height}; flex-shrink:0;"

    if logo_b64:
        return f"""<div style="width:100%; {h_style} border-radius:20px; overflow:hidden;
    background:#111; display:flex; align-items:center; justify-content:center;">
    <img src="{logo_b64}" style="max-height:200px;max-width:620px;object-fit:contain;">
  </div>"""

    if bg_file and Path(bg_file).exists():
        raw = Path(bg_file).read_bytes()
        b64 = base64.b64encode(raw).decode()
        return f"""<div style="width:100%; {h_style} border-radius:20px; overflow:hidden;
    background:url('data:image/jpeg;base64,{b64}') center/cover no-repeat;"></div>"""

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


def content_slide(num, title, body_html, logo_domain=None, logo_b64=None, bg_file=None,
                  layout="standard", chart=None, accent=None, photo_height=None):
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

        img = _img_box(logo_b64, bg_file, logo_domain, height=h)
        if layout == "heavy":
            title_style = 'style="font-size:46px;"'
            body_style  = 'style="font-size:24px;line-height:1.72;"'
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
    <span class="dsource">{source_html}</span>
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
  width: 100%; height: 100%;
  display: flex; flex-direction: column;
  padding: 72px 72px 60px;
  position: relative;
}
.spot-top { flex-shrink: 0; margin-bottom: auto; }
.spot-tag {
  font-size: 18px; font-weight: 600;
  color: rgba(255,255,255,0.25); letter-spacing: 0.06em;
  text-transform: uppercase;
}
.spot-center {
  flex: 1; display: flex; flex-direction: column;
  justify-content: center; gap: 40px;
}
.spot-lines { display: flex; flex-direction: column; gap: 0; }
.spot-line {
  font-size: 80px; font-weight: 900;
  color: #FFFFFF; line-height: 1.0;
  letter-spacing: -0.03em; display: block;
}
.spot-line:first-child { color: #FF6B00; }
.spot-sub {
  font-size: 24px; font-weight: 400;
  color: rgba(255,255,255,0.50); line-height: 1.55;
  max-width: 820px;
  border-left: 3px solid #FF6B00; padding-left: 22px;
}
.spot-bottom {
  display: flex; align-items: center; justify-content: space-between;
  padding-top: 32px; border-top: 1px solid rgba(255,255,255,0.08);
  flex-shrink: 0; margin-top: auto;
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
]




# ─── GERADOR ───────────────────────────────────────────────────────────────────

CACHE_DIR = Path(__file__).parent / ".img-cache"
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
}


async def download_slide_photos(browser, carroseis: list) -> dict:
    """Baixa fotos dos slides — usa dicionário fixo ou busca automática via Unsplash API."""
    photos = {}
    page = await browser.new_page(viewport={"width": 1080, "height": 1350})

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
                    html = cover_slide(
                        data["headline"], data["subheadline"], slide_num,
                        logo_domain=carousel.get("cover_logo_domain"),
                        bg_file=cover_photos.get(slug)
                    )

                elif slide_type == "content":
                    logo_domain = data.get("logo_domain")
                    slide_photo = slide_photos.get(data.get("photo_query")) or cover_photos.get(slug)
                    html = content_slide(
                        data["num"], data["title"], data["body"],
                        logo_domain=logo_domain,
                        logo_b64=logos.get(logo_domain),
                        bg_file=slide_photo,
                        layout=data.get("layout", "standard"),
                        chart=data.get("chart"),
                        accent=data.get("accent"),
                        photo_height=data.get("photo_height"),
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
