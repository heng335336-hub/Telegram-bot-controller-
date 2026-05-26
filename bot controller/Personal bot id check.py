from telegram.ext import ApplicationBuilder, MessageHandler, filters

BOT_TOKEN = '8272486762:AAEdf3t_rRIQec-O2vwKNd5vLmfE5uGoXXc'

async def get_chat_id(update, context):
    chat_id = update.effective_chat.id
    chat_type = update.effective_chat.type
    print(f"Chat ID: {chat_id}, Chat Type: {chat_type}")
    await update.message.reply_text(f"Chat ID: {chat_id}")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, get_chat_id))

print("Bot is running... Send a message to your bot in a group or PM.")
app.run_polling()