"""
Analisa um perfil do Instagram usando sessão salva pelo instagram_login_browser.py.

Uso:
    python tools/instagram_profile.py @handle
    python tools/instagram_profile.py handle

Saída: JSON com dados do perfil no stdout.
"""

import asyncio
import sys
import json
import io
from pathlib import Path
from playwright.async_api import async_playwright

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

SESSION_FILE = Path(__file__).parent / "instagram_cookies.json"


def parse_number(text: str) -> str:
    """Limpa texto de número (ex: '121K followers' -> '121K')."""
    if not text:
        return None
    return text.strip().split()[0].replace(",", ".")


async def analyze_profile(username: str) -> dict:
    username = username.lstrip("@").strip()

    if not SESSION_FILE.exists():
        return {"error": "Sessão não encontrada. Rode instagram_login_browser.py primeiro."}

    cookies = json.loads(SESSION_FILE.read_text())

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            viewport={"width": 1280, "height": 800},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        await context.add_cookies(cookies)
        page = await context.new_page()

        await page.goto(f"https://www.instagram.com/{username}/", wait_until="domcontentloaded", timeout=60000)
        await page.wait_for_timeout(5000)

        data = await page.evaluate("""() => {
            // Stats via links (mais confiável)
            const followerLink = document.querySelector("a[href*='/followers/']");
            const followingLink = document.querySelector("a[href*='/following/']");

            // Posts: primeiro número no header que não seja K/M
            const header = document.querySelector("header");
            const numSpans = header
                ? Array.from(header.querySelectorAll("span"))
                    .map(s => s.innerText.trim())
                    .filter(t => /^[0-9][0-9,\\.]*$/.test(t))
                : [];

            // Nome completo: span dentro do header que não seja o username
            const h2 = document.querySelector("h2");
            const username = h2 ? h2.innerText.trim() : "";
            const allSpans = header ? Array.from(header.querySelectorAll("span")) : [];
            const nameSpan = allSpans.find(s => {
                const t = s.innerText.trim();
                return t.length > 2 && t !== username && !/^[0-9,\.KM]+$/.test(t) && !t.includes("follower") && !t.includes("following") && s.children.length === 0;
            });

            // Bio: span dir=auto com mais de 20 chars e que não seja o nome
            const fullName = nameSpan ? nameSpan.innerText.trim() : "";
            const allDirAuto = Array.from((header || document).querySelectorAll("span[dir='auto'], h1[dir='auto']"));
            const bioEl = allDirAuto.find(el => {
                const t = el.innerText.trim();
                return t.length > 20 && t !== fullName && !el.closest("article");
            });

            // Site externo
            const linkEl = document.querySelector("a[rel*='noopener'][href*='l.instagram.com'], a[rel='me noopener noreferrer']");

            // Categoria
            const catEl = Array.from(document.querySelectorAll("span, div"))
                .find(el => ["Criador digital", "Coach", "Educação", "Empresário", "Consultor",
                             "Empresa", "Marca pessoal", "Infoprodutor", "Especialista"].some(c => el.innerText.trim() === c));

            // Conta verificada
            const verified = !!document.querySelector("svg[aria-label='Verificado']") ||
                             !!document.querySelector("svg[aria-label='Verified']");

            return {
                followerText: followerLink ? followerLink.innerText : null,
                followingText: followingLink ? followingLink.innerText : null,
                numSpans: numSpans.slice(0, 5),
                nome: nameSpan ? nameSpan.innerText.trim() : null,
                bio: bioEl ? bioEl.innerText.trim() : null,
                site: linkEl ? linkEl.getAttribute("href") : null,
                categoria: catEl ? catEl.innerText.trim() : null,
                verificado: verified,
            };
        }""")

        result = {
            "username": username,
            "nome": data.get("nome"),
            "bio": data.get("bio"),
            "seguidores": parse_number(data.get("followerText")),
            "seguidores_exato": data.get("followerText"),
            "seguindo": parse_number(data.get("followingText")),
            "posts": data.get("numSpans")[0] if data.get("numSpans") else None,
            "site": data.get("site"),
            "categoria": data.get("categoria"),
            "verificado": data.get("verificado"),
            "url": f"https://www.instagram.com/{username}/",
        }

        await browser.close()
        return result


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"error": "Uso: python instagram_profile.py @handle"}))
        sys.exit(1)

    result = asyncio.run(analyze_profile(sys.argv[1]))
    print(json.dumps(result, ensure_ascii=False, indent=2))
