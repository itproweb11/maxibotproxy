import telebot
import os
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))

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
    
    # reply_to лучше работает в группах
    bot.reply_to(message, "👋 Привет! Это MaxiBot Proxy.\n\nВыбери нужный раздел:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    bot.answer_callback_query(call.id)   # ОБЯЗАТЕЛЬНО для групп

    if call.data == "tariffs":
        bot.send_message(call.message.chat.id, "📋 Доступные тарифы:\n\n• 1 неделя — 0 руб\n• 1 месяц — 200 руб\n• 3 месяца — 390 руб\n• 6 месяцев — 690 руб\n• 12 месяцев — 1190 руб")

    elif call.data == "buy":
        bot.send_message(call.message.chat.id, "🔗 Переходи к оплате:\nhttps://maxiproxy.net")

    elif call.data == "support":
        bot.send_message(call.message.chat.id, "🛠 Пиши напрямую админу 👇")
        bot.send_message(call.message.chat.id, "https://t.me/ivan_diner")

bot.infinity_polling()
