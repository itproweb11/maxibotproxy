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
    chat_id = call.message.chat.id
    msg_id = call.message.message_id

    if call.data == "tariffs":
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("← Назад", callback_data="back"))
        bot.edit_message_text("📋 Доступные тарифы:\n\n• 1 неделя — 0 руб\n• 1 месяц — 200 руб\n• 3 месяца — 390 руб\n• 6 месяцев — 690 руб\n• 12 месяцев — 1190 руб", chat_id, msg_id, reply_markup=markup)

    elif call.data == "buy":
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("Перейти к оплате", url="https://maxiproxy.net"))
        markup.add(InlineKeyboardButton("← Назад", callback_data="back"))
        bot.edit_message_text("🔗 Переходи к оплате:", chat_id, msg_id, reply_markup=markup)

    elif call.data == "account":
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("🔑 Открыть Личный кабинет", url="https://maxiproxy.net"))
        markup.add(InlineKeyboardButton("← Назад", callback_data="back"))
        bot.edit_message_text("👤 Переходи в личный кабинет:", chat_id, msg_id, reply_markup=markup)

    elif call.data == "support":
        bot.send_message(chat_id, "🛠 Пиши сюда напрямую админу 👇")
        bot.send_message(chat_id, "https://t.me/ivan_diner")

    elif call.data == "back":
        markup = InlineKeyboardMarkup(row_width=2)
        markup.add(
            InlineKeyboardButton("💰 Тарифы", callback_data="tariffs"),
            InlineKeyboardButton("🛒 Купить", callback_data="buy"),
            InlineKeyboardButton("👤 Личный кабинет", callback_data="account"),
            InlineKeyboardButton("🛠 Поддержка", callback_data="support")
        )
        bot.edit_message_text("👋 Привет! Это MaxiBot Proxy.\n\nВыбери нужный раздел:", chat_id, msg_id, reply_markup=markup)

bot.infinity_polling()