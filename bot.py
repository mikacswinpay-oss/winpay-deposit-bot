from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8771022249:AAFbrsRJOcWehW5NQ-KSXYWFdly_KGImmjU"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["💰 Deposit (UPI)", "🎁 Bonus Offers"],
        ["👑 Premium", "📄 How to Deposit"],
        ["🎧 Customer Support"]
    ]

    await update.message.reply_text(
        "👋 Welcome to WinPay!\n\n"
        "💰 Offline UPI Deposit Available\n"
        "🎁 Exclusive Bonus\n"
        "🛡 Safe & Secure\n"
        "⚡ Fast Approval",
        reply_markup=ReplyKeyboardMarkup(
            keyboard,
            resize_keyboard=True
        )
    )

if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()