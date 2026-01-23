import requests
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, ContextTypes, filters
from config import BOT_TOKEN, GITHUB_TOKEN, GITHUB_REPO
from locales import id as ID, en as EN

LANG = {}

def t(chat, key):
    return (ID.TEXT if LANG.get(chat,"id")=="id" else EN.TEXT)[key]

async def start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    kb = InlineKeyboardMarkup([
        [InlineKeyboardButton("🇮🇩", callback_data="lang:id"),
         InlineKeyboardButton("🇬🇧", callback_data="lang:en")]
    ])
    await update.message.reply_text(ID.TEXT["welcome"], reply_markup=kb)

async def lang(update: Update, ctx):
    q = update.callback_query
    LANG[q.message.chat_id] = q.data.split(":")[1]
    await q.edit_message_text(t(q.message.chat_id,"accepted"))

async def handle(update: Update, ctx):
    m = update.message
    if not (m.document or (m.text and m.text.startswith("http"))):
        await m.reply_text(t(m.chat_id,"invalid"))
        return

    status = await m.reply_text(t(m.chat_id,"processing"))

    payload = {
        "chat_id": m.chat_id,
        "message_id": status.message_id,
        "file_id": m.document.file_id if m.document else None,
        "url": m.text if m.text else None
    }

    requests.post(
        f"https://api.github.com/repos/{GITHUB_REPO}/dispatches",
        headers={"Authorization": f"token {GITHUB_TOKEN}"},
        json={"event_type":"upload","client_payload":payload}
    )

async def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(lang))
    app.add_handler(MessageHandler(filters.ALL, handle))
    app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
