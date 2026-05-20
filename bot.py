from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "7577500849:AAGNfrb6Kwn2SLSM4rdHrb-x4Km_JklMQNU"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🔥 TEST 1", callback_data="test1")],
        [InlineKeyboardButton("📊 STATUS", callback_data="status")]
    ]

    await update.message.reply_text(
        "Привет 👋 бот работает",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()

    if q.data == "test1":
        await q.edit_message_text("🔥 TEST 1 работает отлично!")

    elif q.data == "status":
        await q.edit_message_text(
            "📊 STATUS:\n\n"
            "✔ Bot online\n"
            "✔ Callback working\n"
            "✔ System OK"
        )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    print("Bot started...")
    app.run_polling()

if __name__ == "__main__":
    main()