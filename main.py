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
    
    bot.reply_to(message, "👋 Привет! Это MaxiBot Proxy.\n\nВыбери нужный раздел:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    bot.answer_callback_query(call.id)
    chat_id = call.message.chat.id

    if call.data == "tariffs":
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("← Назад", callback_data="back"))
        bot.send_message(chat_id, "📋 Доступные тарифы:\n\n• 1 неделя — 0 руб\n• 1 месяц — 200 руб\n• 3 месяца — 390 руб\n• 6 месяцев — 690 руб\n• 12 месяцев — 1190 руб", reply_markup=markup)

    elif call.data == "buy":
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("Перейти к оплате", url="https://maxiproxy.net"))
        markup.add(InlineKeyboardButton("← Назад", callback_data="back"))
        bot.send_message(chat_id, "🔗 Переходи к оплате:", reply_markup=markup)

    elif call.data == "support":
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("← Назад", callback_data="back"))
        bot.send_message(chat_id, "🛠 Пиши напрямую админу 👇\nhttps://t.me/ivan_diner", reply_markup=markup)

    elif call.data == "back":
        markup = InlineKeyboardMarkup(row_width=2)
        markup.add(
            InlineKeyboardButton("💰 Тарифы", callback_data="tariffs"),
            InlineKeyboardButton("🛒 Купить", callback_data="buy")
        )
        markup.add(
            InlineKeyboardButton("👤 Личный кабинет", web_app=WebAppInfo(url="https://maxiproxy.net")),
            InlineKeyboardButton("🛠 Поддержка", callback_data="support")
        )
        bot.send_message(chat_id, "👋 Привет! Это MaxiBot Proxy.\n\nВыбери нужный раздел:", reply_markup=markup)

bot.infinity_polling()
