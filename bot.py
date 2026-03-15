import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
from commands import start, chat, get_daily_chart
from utils.chart_generator import ChartGenerator
load_dotenv()
API_TOKEN = os.getenv("MATKA_FATHER_BOT_KEY")

template_path = os.getcwd()+'/templates/daily.png'
font_path_archivo = os.getcwd()+'/fonts/ArchivoBlack-Regular.ttf'
font_path_cinzel = os.getcwd()+'/fonts/Cinzel-Regular.ttf'

# Build the application
app = ApplicationBuilder().token(API_TOKEN).build()

# Add handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("daily_chart", get_daily_chart))
# app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

# Run the bot
print("Bot is starting...")
app.run_polling()