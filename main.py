import telebot
import os
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))

@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(
        InlineKeyboardButton("💰 Тарифы", callback_data="tariffs"),
        InlineKeyboardButton("🛒 Купить", callback_data="buy"),
        InlineKeyboardButton("👤 Личный кабинет", callback_data="account"),
        InlineKeyboardButton("🛠 Поддержка", callback_data="support")
    )
    
    bot.send_message(message.chat.id, "👋 Привет! Это MaxiBot Proxy.\n\nВыбери нужный раздел:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == "tariffs":
        text = "📋 Доступные тарифы:\n\n• 1 неделя — 0 руб\n• 1 месяц — 200 руб\n• 3 месяца — 390 руб\n• 6 месяцев — 690 руб\n• 12 месяцев — 1190 руб"
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id)
    
    elif call.data == "buy":
        bot.edit_message_text("🔗 Переходи к оплате:", call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, "https://maxiproxy.net")
    
    elif call.data == "account":
        markup = InlineKeyboardMarkup()
        btn = InlineKeyboardButton("🔑 Открыть Личный кабинет", url="https://maxiproxy.net")
        markup.add(btn)
        bot.edit_message_text("👤 Переходи в личный кабинет:", call.message.chat.id, call.message.message_id, reply_markup=markup)
    
    elif call.data == "support":
        bot.send_message(call.message.chat.id, "🛠 Пиши сюда напрямую админу 👇")
        bot.send_message(call.message.chat.id, "https://t.me/ivan_diner")

bot.infinity_polling()