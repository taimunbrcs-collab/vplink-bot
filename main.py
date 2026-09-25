import requests
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

BOT_TOKEN = os.environ.get("BOT_TOKEN")
VPLINK_API = "ed6f17d2ab020aca3c500dcf99b5d8"

async def start(update: Update, context):
    await update.message.reply_text("👋 Welcome! Link pathao, ami short kore dibo!")

async def short_link(update: Update, context):
    long_url = update.message.text.strip()
    if not long_url.startswith("http"):
        return
    msg = await update.message.reply_text("⏳ Shortening...")
    try:
        r = requests.get(f"https://vplink.in/api?api={VPLINK_API}&url={long_url}")
        data = r.json()
        short = data.get('shortenedUrl') or data.get('shortened_url') or r.text
        await msg.edit_text(f"✅ Done!\n\n{short}")
    except Exception as e:
        await msg.edit_text(f"Error: {e}")

app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, short_link))
app.run_polling()
