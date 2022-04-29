import telebot

import os

import random

bot = telebot.TeleBot("1933383897:AAE0GA6hT1wOuIx26xa14dFIhYDHOIMwc2Y")


def log(message, answer):
    print("\n ------------")

    from datetime import datetime

    print(datetime.now())

    print("Сообщение от {0} {1}. (id = {2}) \n Текст - {3}".format(message.from_user.first_name,

                                                                   message.from_user.last_name,

                                                                   str(message.from_user.id),

                                                                   message.text))


@bot.message_handler(commands=["start"])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)

    user_markup.row('/start', '/stop')

    user_markup.row('фото', 'аудио', 'документы')
    user_markup.row('стикер', 'локация')


    bot.send_message(message.from_user.id, 'Добро пожаловать', reply_markup=user_markup)


@bot.message_handler(commands=["stop"])
def handle_start(message):

    hide_markup = telebot.types.ReplyKeyboardRemove()

    bot.send_message(message.from_user.id, '...', reply_markup=hide_markup)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == 'фото':

        directory = 'C:/'

        all_files_in_directory = os.listdir(directory)

        random_file = random.choice(all_files_in_directory)

        img = open(directory + '/' + random_file, 'rb')

        bot.send_chat_action(message.from_user.id, 'upload_photo')

        bot.send_photo(message.from_user.id, img)

        img.close()

    elif message.text == 'аудио':

        audio = open("/Users/apple/Music/iTunes/iTunes Media/Music/One Republic/Unknown Album/Counting Stars.mp3", 'rb')

        bot.send_chat_action(message.from_user.id, 'upload_audio')

        bot.send_audio(message.from_user.id, audio)

        audio.close()

    elif message.text == 'документы':

        directory = '/Users/apple/Desktop/job'

        all_files_in_directory = os.listdir(directory)

        print(all_files_in_directory)

        for files in all_files_in_directory:
            document = open(directory + '/' + files, 'rb')

            bot.send_chat_action(message.from_user.id, 'upload_document')

            bot.send_document(message.from_user.id, document)

            document.close()


    elif message.text == 'локация':

        bot.send_chat_action(message.from_user.id, 'upload_location')

        bot.send_location(message.from_user.id, 66.2497976, -97.8220)
    else:
        answer = "Извините, я еще не научился отвечать на такие сообщения"


bot.polling(none_stop=True, interval=0)
