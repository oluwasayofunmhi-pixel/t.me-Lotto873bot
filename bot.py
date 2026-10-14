from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# ============================================
# PASTE YOUR BOT TOKEN HERE (from BotFather)
# ============================================
TOKEN = "PASTE_YOUR_BOT_TOKEN_HERE"


# ============================================
# COMMAND HANDLERS
# ============================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👟 Welcome to SneakerHer!\n\n"
        "Your daily source for women's sneaker news, drops, restocks, and deals.\n\n"
        "Here's what I can do:\n\n"
        "/latest — Latest sneaker updates\n"
        "/drops — Upcoming releases\n"
        "/restock — Restock alerts\n"
        "/sales — Deals & discounts\n"
        "/brands — Browse by brand\n"
        "/styles — Browse by style\n"
        "/size — Size guide & tips\n"
        "/about — About this bot\n"
        "/contact — Send feedback\n\n"
        "Stay stylish and never miss a drop! 👟✨"
    )


async def latest(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👟 LATEST SNEAKER UPDATES\n\n"
        "No updates yet. Check back soon!"
    )


async def drops(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📅 UPCOMING DROPS\n\n"
        "No upcoming drops yet. Stay tuned!"
    )


async def restock(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔁 RESTOCK ALERTS\n\n"
        "No restocks yet. We'll notify you!"
    )


async def sales(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💸 DEALS & DISCOUNTS\n\n"
        "No active sales right now. Check back soon!"
    )


async def brands(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏷️ BROWSE BY BRAND\n\n"
        "Available brands:\n"
        "• Nike\n"
        "• Adidas\n"
        "• New Balance\n"
        "• Puma\n"
        "• Asics\n\n"
        "More coming soon!"
    )


async def styles(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👠 BROWSE BY STYLE\n\n"
        "• Running\n"
        "• Basketball\n"
        "• Casual\n"
        "• Platform\n"
        "• Chunky\n"
        "• Minimal\n\n"
        "Pick a style to explore!"
    )


async def size(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📏 WOMEN'S SNEAKER SIZE GUIDE\n\n"
        "US 5 = EU 35.5 = UK 3\n"
        "US 6 = EU 36.5 = UK 4\n"
        "US 7 = EU 38 = UK 5\n"
        "US 8 = EU 39 = UK 6\n"
        "US 9 = EU 40.5 = UK 7\n"
        "US 10 = EU 42 = UK 8\n\n"
        "Tip: Sneakers usually fit true to size. "
        "Go half a size up for narrow feet."
    )


async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "ℹ️ ABOUT SNEAKERHER\n\n"
        "SneakerHer is your daily source for women's sneaker news, "
        "drops, restocks, and deals.\n\n"
        "Built for women who love sneakers. 👟"
    )


async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📬 CONTACT & FEEDBACK\n\n"
        "Have a question or want to request a sneaker update?\n"
        "Send your message here and we'll get back to you."
    )


# ============================================
# MAIN FUNCTION
# ============================================

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("latest", latest))
    app.add_handler(CommandHandler("drops", drops))
    app.add_handler(CommandHandler("restock", restock))
    app.add_handler(CommandHandler("sales", sales))
    app.add_handler(CommandHandler("brands", brands))
    app.add_handler(CommandHandler("styles", styles))
    app.add_handler(CommandHandler("size", size))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CommandHandler("contact", contact))

    print("SneakerHer bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
