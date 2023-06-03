import telebot
from pytube import YouTube
import os
from dotenv import load_dotenv

load_dotenv()

TELEKEY = os.getenv("TELEKEY")

bot = telebot.TeleBot(TELEKEY)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет! Этот бот поможет тебе скачать видео с YouTube. Пожалуйста, отправь мне ссылку на видео.")

@bot.message_handler(func=lambda message: True)
def download_video(message):
    try:
        video = YouTube(message.text)
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row('Высокое качество', 'Низкое качество')
        bot.send_message(message.chat.id, "Выберите качество видео:", reply_markup=keyboard)
        bot.register_next_step_handler(message, selected_quality, video)
    except:
        bot.reply_to(message, "Упс! Что-то пошло не так. Пожалуйста, отправьте мне правильную ссылку на видео.")

def selected_quality(message, video):
    quality = message.text
    if quality == "Высокое качество":
        output = video.streams.get_highest_resolution()
    elif quality == "Низкое качество":
        output = video.streams.get_lowest_resolution()
    else:
        bot.reply_to(message, "Упс! Что-то пошло не так. Пожалуйста, попробуйте еще раз.")
        return
    bot.send_chat_action(message.chat.id, 'upload_video')
    bot.send_video(message.chat.id, output.url)

bot.polling()
