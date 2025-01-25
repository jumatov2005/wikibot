from telegram.ext import Application, CommandHandler
from telegram import Update
from telegram.ext import CallbackContext
from settings.settings import TELEGRAM_TOKEN


# Start komandasi uchun funksiya
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("SALOM")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="SALOM YANA BIR BOR")


# Ilovani ishga tushirish
if __name__ == "__main__":
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # "start" komandasi uchun handler qo'shish
    application.add_handler(CommandHandler("start", start))

    # Botni ishga tushirish
    application.run_polling()
