import os
import telebot

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Bot activo 📊 Envíame un partido")

@bot.message_handler(func=lambda message: True)
def responder(message):
    texto = message.text.lower()

    if "madrid" in texto:
        bot.reply_to(message, "📊 Madrid: +12 remates / +6 corners aprox")
    else:
        bot.reply_to(message, "Analizando apuesta... 📊")

bot.polling()
