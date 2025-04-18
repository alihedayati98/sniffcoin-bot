import telebot
import os

API_TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام شکارچی! من آماده‌ام پامپ بعدی رو واست بو بکشم!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "فعلاً در حال یادگیری شکارم...")

bot.polling()