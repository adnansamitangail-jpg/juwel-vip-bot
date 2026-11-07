import os
import telebot

# আপনার নতুন টোকেন এবং অ্যাডমিন আইডি
TOKEN = '7340220943:AAGjugOLf2ZHGEx99aSWhkjz7XS64oS2cPY'
ADMIN_ID = 6655792170

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    if message.from_user.id != ADMIN_ID:
        bot.reply_to(message, "⚠️ আপনার এই বট ব্যবহার করার অনুমতি নেই।")
        return
    
    bot.reply_to(message, "🤖 জুয়েল ভিআইপি এআই এপিক কনভার্টার বটে আপনাকে স্বাগতম!\n\nআপনার কোড বা HTML ফাইলটি সেন্ড করুন, আমি AI ত্রুটি চেক করে APK তৈরি শুরু করে দেব।")

@bot.message_handler(content_types=['document'])
def handle_docs(message):
    if message.from_user.id != ADMIN_ID:
        return
        
    bot.reply_to(message, "📂 ফাইল সফলভাবে পাওয়া গেছে! অ্যাপ তৈরি প্রক্রিয়া শুরু হচ্ছে...")

if __name__ == '__main__':
    print("Bot is running...")
    bot.infinity_polling()
