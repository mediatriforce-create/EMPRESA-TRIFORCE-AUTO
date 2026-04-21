"""
Baixa imagens dos posts de um perfil do Instagram usando sessão salva.

Uso:
    python tools/instagram_download_images.py @handle [--limit 12] [--out pasta]

Exemplos:
    python tools/instagram_download_images.py @dr.rafaelfonsecaa
    python tools/instagram_download_images.py @dr.rafaelfonsecaa --limit 20 --out assets/dr-rafael

Saída: imagens salvas em --out (padrão: assets/{handle}/)
"""

import asyncio
import sys
import json
import io
import argparse
import re
from pathlib import Path
from urllib.parse import urlparse, urlencode
import httpx
from playwright.async_api import async_playwright

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

SESSION_FILE = Path(__file__).parent / "instagram_cookies.json"


def sanitize_filename(url: str, index: int) -> str:
    """Gera nome de arquivo a partir da URL ou índice."""
    path = urlparse(url).path
    name = Path(path).name
    # Remove query strings e parâmetros
    name = re.sub(r"[?&].*", "", name)
    if not name.endswith((".jpg", ".jpeg", ".png", ".webp")):
        name = f"post_{index:02d}.jpg"
    else:
        name = f"post_{index:02d}_{name}"
    return name


async def download_images(username: str, limit: int, out_dir: Path):
    username = username.lstrip("@").strip()

    if not SESSION_FILE.exists():
        print(json.dumps({"error": "Sessão não encontrada. Rode instagram_login_browser.py primeiro."}))
        sys.exit(1)

    cookies = json.loads(SESSION_FILE.read_text())
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"Abrindo perfil: @{username}")
    print(f"Limite: {limit} imagens | Destino: {out_dir}")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            viewport={"width": 1280, "height": 900},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        await context.add_cookies(cookies)
        page = await context.new_page()

        await page.goto(f"https://www.instagram.com/{username}/", wait_until="domcontentloaded", timeout=60000)
        await page.wait_for_timeout(4000)

        # Verificar se o perfil carregou
        title = await page.title()
        if "Page Not Found" in title or "Login" in title:
            print(json.dumps({"error": f"Perfil @{username} não encontrado ou sessão expirada."}))
            await browser.close()
            sys.exit(1)

        print("Perfil carregado. Coletando imagens...")

        image_urls = []
        scroll_attempts = 0
        max_scrolls = 20

        while len(image_urls) < limit and scroll_attempts < max_scrolls:
            # Coletar URLs de imagens dos posts do grid
            urls = await page.evaluate("""() => {
                const imgs = Array.from(document.querySelectorAll("article img, main img"));
                return imgs
                    .filter(img => {
                        const src = img.src || "";
                        return src &&
                            src.startsWith("https://") &&
                            (src.includes("instagram") || src.includes("cdninstagram") || src.includes("fbcdn")) &&
                            !src.includes("s150x150") &&
                            !src.includes("s32x32") &&
                            img.width > 100;
                    })
                    .map(img => img.src);
            }""")

            for url in urls:
                if url not in image_urls:
                    image_urls.append(url)

            if len(image_urls) >= limit:
                break

            # Scroll para carregar mais posts
            await page.evaluate("window.scrollBy(0, 800)")
            await page.wait_for_timeout(2000)
            scroll_attempts += 1

        image_urls = image_urls[:limit]
        print(f"URLs coletadas: {len(image_urls)}")

        # Baixar imagens usando httpx com cookies da sessão
        cookie_header = "; ".join([f"{c['name']}={c['value']}" for c in cookies if "instagram" in c.get("domain", "")])

        downloaded = []
        async with httpx.AsyncClient(timeout=30, follow_redirects=True) as client:
            for i, url in enumerate(image_urls, 1):
                filename = sanitize_filename(url, i)
                dest = out_dir / filename

                if dest.exists():
                    print(f"  [{i}/{len(image_urls)}] Já existe: {filename}")
                    downloaded.append(str(dest))
                    continue

                try:
                    resp = await client.get(url, headers={
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                        "Referer": f"https://www.instagram.com/{username}/",
                        "Cookie": cookie_header,
                    })
                    if resp.status_code == 200:
                        dest.write_bytes(resp.content)
                        print(f"  [{i}/{len(image_urls)}] Baixado: {filename} ({len(resp.content) // 1024}KB)")
                        downloaded.append(str(dest))
                    else:
                        print(f"  [{i}/{len(image_urls)}] Erro {resp.status_code}: {filename}")
                except Exception as e:
                    print(f"  [{i}/{len(image_urls)}] Falha: {filename} — {e}")

        await browser.close()

    print(f"\nConcluído. {len(downloaded)} imagens salvas em: {out_dir}")
    result = {
        "username": username,
        "total_coletadas": len(image_urls),
        "total_baixadas": len(downloaded),
        "destino": str(out_dir),
        "arquivos": downloaded,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Baixa imagens de um perfil do Instagram.")
    parser.add_argument("handle", help="Handle do Instagram (ex: @dr.rafaelfonsecaa)")
    parser.add_argument("--limit", type=int, default=12, help="Número máximo de imagens (padrão: 12)")
    parser.add_argument("--out", type=str, default=None, help="Pasta de destino (padrão: assets/{handle})")
    args = parser.parse_args()

    handle = args.handle.lstrip("@").strip()
    out_dir = Path(args.out) if args.out else Path("assets") / handle

    asyncio.run(download_images(handle, args.limit, out_dir))
