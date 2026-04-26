"""
Abre um browser real para você logar no Instagram manualmente.
Salva a sessão (cookies) para uso posterior sem precisar logar de novo.

Uso:
    python tools/instagram_login_browser.py
"""

import asyncio
import json
from pathlib import Path
from playwright.async_api import async_playwright

SESSION_FILE = Path(__file__).parent / "instagram_cookies.json"


async def login():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=50)
        context = await browser.new_context(
            viewport={"width": 1280, "height": 800},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = await context.new_page()

        print("Abrindo Instagram no browser...")
        await page.goto("https://www.instagram.com/accounts/login/")
        await page.wait_for_timeout(2000)

        print("\nFaca o login normalmente no browser que abriu.")
        print("Aguardando voce logar... (detecta automaticamente)")

        # Aguarda até detectar que está logado (URL muda para feed ou aparece nav)
        for _ in range(120):
            await page.wait_for_timeout(1000)
            url = page.url
            if "instagram.com" in url and "/accounts/login" not in url and "/challenge" not in url:
                logged_in = await page.query_selector("nav")
                if logged_in:
                    print("Login detectado!")
                    break

        # Salva cookies da sessão
        cookies = await context.cookies()
        SESSION_FILE.write_text(json.dumps(cookies, ensure_ascii=False, indent=2))
        print(f"\nSessão salva em: {SESSION_FILE}")
        print("Pronto. Use instagram_profile.py para analisar perfis.")

        await browser.close()


if __name__ == "__main__":
    asyncio.run(login())
