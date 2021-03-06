import random
import os
from flask import Flask, request
import logging

# Подключаем модуль для Телеграма
import telebot

# Указываем токен
TOKEN = '1625118390:AAGK2RDBJxd3c_i39v9yYbl-0EmB5MoZbEQ'
bot = telebot.TeleBot(TOKEN)
# Импортируем типы из модуля, чтобы создавать кнопки
from telebot import types

# Списки для рандома (по содержанию)

watchlist = ['"Медный всадник" А.С. Пушкин: https://www.mariinsky.ru/playbill/repertoire/ballet/bronze_horseman/',
             '"Вишневый сад" А.П. Чехов: https://www.youtube.com/watch?v=L9FfoPSzNRY',
             '"Вишневый сад" А.П. Чехов: https://www.youtube.com/watch?v=yDJOSUHDpQI',
             '"Дон Кихот" М. де Сервантес: https://www.kinopoisk.ru/film/650699/',
             '"Дон Кихот" М. де Сервантес: https://artchive.ru/publications/894~Don_Kikhot_s_luchshimi_kartinami_i_illjustratsijami_ot_Dore_i_Dali_do_Serova_i_Zvereva',
             '"Преступление и наказание" Ф.М. Достоевский: https://ok.ru/video/1333906705013']

readlist = ['"Дон Кихот" М. де Сервантес: https://www.liveinternet.ru/users/noche_de_mayo/post132031822/',
            '"Дон Кихот" М. де Сервантес: https://mel.fm/mneniye_eksperta/317248-film_adaptation_don_quixote',
            '"Вишневый сад" А.П. Чехов: http://chehov-lit.ru/chehov/vospominaniya/stanislavskij.htm',
            '"Вишневый сад" А.П. Чехов: https://polka.academy/articles/482',
            '"Преступление и наказание" Ф.М. Достоевский: https://dostoevskyworld.ru/',
            '"Преступление и наказание" Ф.М. Достоевский: https://arzamas.academy/mag/419-dost',
            '"Преступление и наказание" Ф.М. Достоевский: https://ru.rbth.com/zhizn/256-dostoevsky-munch-krik']

listenlist = ['"Медный всадник" А.С. Пушкин: https://www.youtube.com/watch?v=8stiZXNoC9g',
              '"Дон Кихот" М. де Сервантес: https://soundcloud.com/polyarinov/6-don-kikhot-idealnyy-metaroman']

# Метод, который получает сообщения и обрабатывает их
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # Если написали «Привет»
    if message.text == "Книги" or message.text == "книги":
        pisateli = open('images/pisateli.png', 'rb')
        bot.send_photo(message.from_user.id, pisateli)

        # Готовим кнопки
        keyboard = types.InlineKeyboardMarkup()
        key_pushkin = types.InlineKeyboardButton(text='А.С. Пушкин "Медный всадник"', callback_data='mv')
        # И добавляем кнопку на экран
        keyboard.add(key_pushkin)
        key_chehov = types.InlineKeyboardButton(text='А.П. Чехов "Вишневый сад"', callback_data='vs')
        keyboard.add(key_chehov)
        key_servantes = types.InlineKeyboardButton(text='М. де Сервантес "Дон Кихот"', callback_data='dk')
        keyboard.add(key_servantes)
        # Показываем все кнопки сразу и пишем сообщение о выборе
        bot.send_message(message.from_user.id, text='Выбери итересующую тебя книгу', reply_markup=keyboard)


    elif message.text == "Смотреть" or message.text == "смотреть":
        bot.send_message(message.from_user.id, random.choice(watchlist))

    elif message.text == "Читать" or message.text == "читать":
        bot.send_message(message.from_user.id, random.choice(readlist))

    elif message.text == "Слушать" or message.text == "слушать":
        bot.send_message(message.from_user.id, random.choice(listenlist))

    elif message.text == "Проект" or message.text == "проект":
        logo = open('images/logo.png', 'rb')
        bot.send_photo(message.from_user.id, logo)
        bot.send_message(message.from_user.id, "Привет!   Данное приложение создаётся в рамках проекта Digital Реставрация, цель которого соединить историю и современность."
                                               " Ну и помочь тебе с литературой:) Выбранные для проекта книги входят в школьную программу и уже были прочитаны несчётное количество раз, ведь некоторым из них больше полувека!"
                                               " Все они не только были бережно отреставрированы, но теперь внутри у каждой из них есть QR-коды, по которым можно найти интересные и полезные материалы, которые учитель точно не расскажет на уроке."
                                               "Специально для того, чтобы во всем разобраться или по-новому взглянуть на привычные произведения в нашем приложении создана подборка самых лучших материалов, от фильмов и спектаклей до подкастов и аудиокниг."
                                               " Разнообразие доступных форматов точно не даст заскучать.")





    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
        bot.send_message(message.from_user.id, "Если хочешь увидеть суть книги в одной гифке, то напиши 'книги'.")
        bot.send_message(message.from_user.id, "Если хочешь посмотреть фильмы, спектакли или иллюстрации, то напиши 'смотреть'.")
        bot.send_message(message.from_user.id, "Если хочешь послушать аудиогниги или подкасты, то напиши 'слушать'.")
        bot.send_message(message.from_user.id, "Если хочешь почитать интересные статьи, то напиши 'читать'.")
        bot.send_message(message.from_user.id, "Если хочешь больше узнать о проекте, то напиши 'проект'.")

    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Пожалуйста, напиши /help.")


#Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    # Если нажали на одну из 3 кнопок — выводим информацию
   if call.data == "mv":
       mv = open('images/mv.gif', 'rb')
       bot.send_animation(call.from_user.id, mv)

   if call.data == "vs":
       vs = open('images/vs.gif', 'rb')
       bot.send_animation(call.from_user.id, vs)
   if call.data == "dk":
       dk = open('images/dk.gif', 'rb')
       bot.send_animation(call.from_user.id, dk)

# # Запускаем постоянный опрос бота в Телеграме
# bot.polling(none_stop=True, interval=0)
# print('done')

if "HEROKU" in list(os.environ.keys()):
    print('I HEROKU')
    logger = telebot.logger
    telebot.logger.setLevel(logging.INFO)

    server = Flask(__name__)
    @server.route('/' + TOKEN, methods=['POST'])
    def getMessage():
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return "!", 200

    @server.route("/")
    def webhook():
        bot.remove_webhook()
        bot.set_webhook(url="https://secure-dawn-49690.herokuapp.com/" + TOKEN)
        print('set webhook')
        return "?", 200
    server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))
else:
    # если переменной окружения HEROKU нету, значит это запуск с машины разработчика.
    # Удаляем вебхук на всякий случай, и запускаем с обычным поллингом.
    bot.remove_webhook()
    bot.polling(none_stop=True)