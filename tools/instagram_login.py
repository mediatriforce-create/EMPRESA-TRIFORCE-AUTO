"""
Roda UMA VEZ para autenticar no Instagram e salvar a sessão.
Após isso, usa instagram_profile.py para analisar perfis sem precisar de senha.

Uso:
    python tools/instagram_login.py
"""

from instagrapi import Client
from instagrapi.exceptions import ChallengeRequired, TwoFactorRequired
from pathlib import Path

SESSION_FILE = Path(__file__).parent / "instagram_session.json"


def challenge_code_handler(username, choice):
    """Chamado quando Instagram pede código de verificação."""
    print(f"\nInstagram enviou código de verificação para: {choice}")
    code = input("Digite o código recebido: ").strip()
    return code


def login():
    username = input("Instagram username: ").strip()
    password = input("Instagram password: ").strip()

    cl = Client()
    cl.delay_range = [1, 3]
    cl.challenge_code_handler = challenge_code_handler

    print("\nFazendo login...")
    try:
        cl.login(username, password)
        cl.dump_settings(SESSION_FILE)
        print(f"\nSessão salva em: {SESSION_FILE}")
        print("Pronto. Use instagram_profile.py para analisar perfis.")
    except ChallengeRequired:
        print("\nInstagram pediu verificação adicional. Tentando resolver...")
        try:
            cl.challenge_resolve(cl.last_json)
            cl.dump_settings(SESSION_FILE)
            print(f"\nSessão salva em: {SESSION_FILE}")
            print("Pronto. Use instagram_profile.py para analisar perfis.")
        except Exception as e:
            print(f"\nErro ao resolver challenge: {e}")
    except TwoFactorRequired:
        print("\nAutenticação de dois fatores ativa.")
        code = input("Digite o código do app autenticador: ").strip()
        try:
            cl.login(username, password, verification_code=code)
            cl.dump_settings(SESSION_FILE)
            print(f"\nSessão salva em: {SESSION_FILE}")
            print("Pronto. Use instagram_profile.py para analisar perfis.")
        except Exception as e:
            print(f"\nErro no 2FA: {e}")
    except Exception as e:
        print(f"\nErro no login: {e}")


if __name__ == "__main__":
    login()
