import telebot
import os

TOKEN = os.environ.get("8617640822:AAE6lPE9Z3pRqdPtvksmfFcFUej_2aNiYuA")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привіт! Я твій бот 👋")

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "Доступні команди:\n/start — почати\n/help — допомога")

bot.polling()
