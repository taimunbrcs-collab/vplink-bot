import requests
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.environ.get("BOT_TOKEN")
VPLINK_API = "ed6f17d2ab020aca3c500dc0b914a1c58a3243b8"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👑 VpLink Bot Online! Link pathao vai! @Tw1xezz0")

async def short_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    long_url = update.message.text.strip()
    if not long_url.startswith("http"):
        return
    msg = await update.message.reply_text("⏳ Shorting...")
    try:
        r = requests.get(f"https://vplink.in/api?api={VPLINK_API}&url={long_url}").json()
        short = r.get('shortenedUrl')
        await msg.edit_text(f"✅ Done!\nOriginal: {long_url}\nShort: {short}")
    except Exception as e:
        await msg.edit_text(f"Error: {e}")

app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, short_link))
app.run_polling()
