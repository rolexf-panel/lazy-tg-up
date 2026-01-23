import requests
from config import BOT_TOKEN

def edit(chat_id, msg_id, text):
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/editMessageText",
        json={
            "chat_id": chat_id,
            "message_id": msg_id,
            "text": text
        },
        timeout=10
    )
