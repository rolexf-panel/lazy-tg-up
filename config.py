import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_REPO = os.getenv("GITHUB_REPO")
PIXELDRAIN_API = os.getenv("PIXELDRAIN_API")

if not all([BOT_TOKEN, GITHUB_TOKEN, GITHUB_REPO]):
    raise RuntimeError("ENV tidak lengkap")
