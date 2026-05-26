import aiohttp
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TELEGRAM_TOKEN = "8272486762:AAEdf3t_rRIQec-O2vwKNd5vLmfE5uGoXXc"
OPENAI_API_KEY = "AIzaSyBbHeITnlc1Z3p5e6E_snAvx88K3G1dqi8"

BOT_USERNAME = "@hglim334bot"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text

    # Only reply when tagged in groups
    if update.message.chat.type in ["group", "supergroup"]:
        if BOT_USERNAME.lower() not in user_message.lower():
            return
        user_message = user_message.replace(BOT_USERNAME, "").strip()

    url = "https://aistudio.google.com/projects"

    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "user", "content": user_message}
        ]
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=payload) as response:
            result = await response.json()

    try:
        reply = result["choices"][0]["message"]["content"]
    except:
        reply = "Error generating response."

    await update.message.reply_text(reply)

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Bot is running...")
app.run_polling()