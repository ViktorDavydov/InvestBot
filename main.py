import telebot
import os
from telebot import types

token = os.getenv("telebot_token")

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет! Нажми /button")


@bot.message_handler(commands=['button'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Кнопка любви")
    item2 = types.KeyboardButton("Кнопка милости")
    item3 = types.KeyboardButton("Кнопка грусти")
    item4 = types.KeyboardButton("Кнопка любопытства")
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    markup.add(item4)
    bot.send_message(message.chat.id, "А теперь выбери кнопку!", reply_markup=markup)


@bot.message_handler(content_types='text')
def button_reply(message):
    if message.text == "Кнопка любви":
        bot.send_photo(message.chat.id,
                       photo="https://cdn.otkritkiok.ru/posts/big/volsebnaya-animacionnaya-otkrytka-ya-lyublyu-tebya-166258.jpg")
    elif message.text == "Кнопка любопытства":
        bot.send_photo(message.chat.id, photo="https://photos.app.goo.gl/8JXzm1TXVcZBKHnb6")
    elif message.text == "Кнопка грусти":
        bot.send_photo(message.chat.id, photo="https://photos.app.goo.gl/4CvMETkDDsDZKQQi8")
        bot.send_photo(message.chat.id, photo="https://photos.app.goo.gl/ohyfsWmfbPBnmPFA8")
    elif message.text == "Кнопка милости":
        bot.send_photo(message.chat.id, photo="https://photos.app.goo.gl/EAEKuvSN4w85YNMo9")


bot.infinity_polling()
