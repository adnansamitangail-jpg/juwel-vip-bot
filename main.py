import os
import telebot

# আপনার টেলিগ্রাম বটের টোকেন
TOKEN = "7340220943:AAGjugOLf2ZHGEx99aSWhkjz7XS64oS2cPY"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "স্বাগতম! আপনার HTML ফাইল এখানে আপলোড করুন, আমি অ্যাপ (APK) তৈরি করে দেব।")

@bot.message_handler(content_types=['document'])
def handle_docs(message):
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    
    # ফাইল সেভ করা
    with open(message.document.file_name, 'wb') as new_file:
        new_file.write(downloaded_file)
        
    bot.reply_to(message, "ফাইল সফলভাবে পাওয়া গেছে! অ্যাপ তৈরি প্রক্রিয়া শুরু হচ্ছে...")

bot.infinity_polling()
