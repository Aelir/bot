import telebot;
import sqlite3;

conn= sqlite3.connect('user.db')
bot = telebot.TeleBot('1999025660:AAEn6x7onApegNmC8O68r78tYsILlE1-kio', parse_mode=None);
cur = conn.cursor();

@bot.message_handler(commands=['start'])
def welcome (message):
    bot.send_message(message.chat.id,"Вечер в хату")


@bot.message_handler(content_types=['Text'])
def run (message):
   if message.text == "Привет":
       bot.send_message(message.chat.id, 'Привет user')
   elif message.text == "/help":
       bot.send_message(message.chat.id, 'help')
   else:
       bot.send_message(message.chat.id, 'Я тебя не понимаю')
bot.polling(none_stop=True, interval=0)