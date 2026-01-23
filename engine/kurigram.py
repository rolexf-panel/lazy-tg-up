from pyrogram import Client
from config import BOT_TOKEN

def get_client():
    return Client(
        name="kurigram",
        bot_token=BOT_TOKEN,
        api_id=6,
        api_hash="eb06d4abfb49dc3eeb1aeb98ae0f581e",
        in_memory=True
    )
