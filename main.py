import telebot
import os

bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "✅ Бот работает в группе!\n\nПривет от MaxiBot Proxy")

@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.reply_to(message, "Я вижу сообщение: " + message.text)

bot.infinity_polling()
