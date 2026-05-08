import telebot
import os
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

bot = telebot.TeLeBot(os.getenv("BOT_TOKEN"))

@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(
        InlineKeyboardButton("💰 Тарифы", callback_data="tariffs"),
        InlineKeyboardButton("🛒 Купить", callback_data="buy")
    )
    markup.add(
        InlineKeyboardButton("👤 Личный кабинет", web_app=WebAppInfo(url="https://maxiproxy.net")),
        InlineKeyboardButton("🛠 Поддержка", callback_data="support")
    )
    
    bot.reply_to(message, "👋 Привет! Это MaxiBot Proxy.\n\nВыбери нужный раздел:", reply_markup=markup)

# ... (остальной код callback можешь оставить как был)

bot.infinity_polling()
