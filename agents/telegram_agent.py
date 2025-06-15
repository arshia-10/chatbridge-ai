import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
latest_message = {"text": "", "sender": None}
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    user_id = update.message.chat_id
    print(f" Message from {user_id}: {text}")

    latest_message["text"] = text
    latest_message["sender"] = user_id
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
def get_latest_telegram_message():
    return latest_message if latest_message["text"] else None

async def send_telegram_reply(user_id, text):
    await application.bot.send_message(chat_id=user_id, text=text)
