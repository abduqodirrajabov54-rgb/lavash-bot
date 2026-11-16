import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN")

MENU = [["💪 Energiya va Quvvat", "🧬 Testosteron"], ["🧴 Ocean Mahsulotlari", "💰 Narxlar"], ["📞 Maslahat olish", "ℹ️ Ma'lumot"]]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Assalomu alaykum! Ocean Estet - Erkaklar uchun botiga xush kelibsiz 💪\n\nBu yerda mahsulotlar haqida ma'lumot olasiz.\nMuhim: Bu dori emas, ishlatishdan oldin shifokor bilan maslahatlashing.",
        reply_markup=ReplyKeyboardMarkup(MENU, resize_keyboard=True)
    )

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "💪 Energiya va Quvvat":
        await update.message.reply_text("💪 Energiya va quvvat uchun mahsulotlar:\n\n1. Ocean Power - energiya va chidamlilik uchun\n2. Ocean Energy - kunlik holsizlikka qarshi\n\nBatafsil maslahat uchun 📞 Maslahat olish ni bosing")
    elif text == "🧬 Testosteron":
        await update.message.reply_text("🧬 Testosteronni qo'llab-quvvatlash:\n\nTabiiy qo'shimchalar va vitaminlar haqida ma'lumot.\n\n⚠️ Testosteron darajasini avval analiz bilan tekshirish kerak. O'zingizcha dori ichmang, avval shifokor ko'rigidan o'ting.")
    elif text == "🧴 Ocean Mahsulotlari":
        await update.message.reply_text("🧴 Ocean Estet mahsulotlari ro'yxati:\n\n- Ocean Power\n- Ocean Energy  \n- Ocean Vitamin Complex\n\nQaysi biri senga mosligini bilish uchun 📞 Maslahat olish ni bos.")
    elif text == "💰 Narxlar":
        await update.message.reply_text("💰 Narxlar admin bilan kelishiladi.\nNarxlar partiyaga qarab o'zgarishi mumkin.\n\nAniq narx uchun 📞 Maslahat olish ni bosing.")
    elif text == "📞 Maslahat olish":
        await update.message.reply_text("📞 Maslahat uchun yozing: @abduqodir\n\nYoshingiz va muammongizni yozing, sizga mos mahsulotni aytamiz.\nMaxfiy saqlanadi 🤫")
    elif text == "ℹ️ Ma'lumot":
        await update.message.reply_text("ℹ️ Ocean Estet - erkaklar salomatligi uchun tabiiy qo'shimchalar.\n\nBu bot davolamaydi, faqat ma'lumot beradi.\nHar qanday mahsulotni ishlatishdan oldin shifokor bilan maslahatlashing.")
    else:
        await update.message.reply_text("Menyudan tanlang 👇")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))
    app.run_polling()

if __name__ == "__main__":
    main()
