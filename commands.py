from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os
from utils.chart_generator import ChartGenerator

template_path = os.getcwd()+'/templates/daily.png'
font_path_archivo = os.getcwd()+'/fonts/ArchivoBlack-Regular.ttf'
font_path_cinzel = os.getcwd()+'/fonts/Cinzel-Regular.ttf'



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.first_name
    system_message = f"start {user_id}! I am a chatbot. How can I help you today?"
    await update.message.reply_text(system_message)

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.first_name
    system_message = f"chat {user_id}! I am a chatbot. How can I help you today?"
    await update.message.reply_text(system_message)

async def get_daily_chart(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Generate the image in memory
    c = ChartGenerator(font_path_archivo=font_path_archivo,font_path_cinzel=font_path_cinzel)
    c.get_single_template(template_path=template_path)
    # c.save(file="new saved.png")
    img = c.get_img()    
    # Send the buffer directly to Telegram
    await update.message.reply_photo(
        photo=img,
        caption="Market today"
    )

