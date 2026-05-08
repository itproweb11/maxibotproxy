import telebot
import os

bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))

# Отвечает на ЛЮБОЕ сообщение в группе
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, "✅ Я вижу твоё сообщение!\nТы написал: " + message.text)

bot.infinity_polling()
