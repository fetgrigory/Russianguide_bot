'''
This module make

Athor: Fetkulin Grigory, Fetkulin.G.R@yandex.ru
Starting 2023/02/08
Ending 2023/03/25

'''
# Установка необходимых библиотек
import telebot
from telebot import types
from settings import TG_TOKEN

# Подключение API ключа
bot = telebot.TeleBot(TG_TOKEN)


# Функция, обрабатывающая команду /start
@bot.message_handler(commands=['start'])
def welcome(message):
    # клавиатура
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Путешествовать")
    btn2 = types.KeyboardButton("Изучать историю")
    btn3 = types.KeyboardButton("Смотреть карту")
    markup.add(btn1, btn2, btn3)

    bot.send_message(message.chat.id,
                     "Здравствуйте, {0.first_name}!\nМеня зовут<b> {1.first_name}</b>, Что будем делать? Путешествовать? Изучать историю? Смотреть карту?".format(
                         message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Путешествовать':
            # Купить авиа/жд билеты, бронирование отеля:
            bot.send_message(message.chat.id, "https://www.tutu.ru/")
            # Подключение карты
        elif message.text == 'Смотреть карту':
            bot.send_message(message.chat.id, "https://yandex.ru/maps/")
        elif message.text == 'Изучать историю':
            # Список городов
            markup = types.InlineKeyboardMarkup(row_width=2)
            btn1 = types.InlineKeyboardButton("Москва", callback_data='city_1')
            btn2 = types.InlineKeyboardButton("Санкт-Петербург", callback_data='city_2')
            btn3 = types.InlineKeyboardButton("Нижний Новгород", callback_data='city_3')
            btn4 = types.InlineKeyboardButton("Сергиев Посад", callback_data='city_4')
            btn5 = types.InlineKeyboardButton("Переславль", callback_data='city_5')
            btn6 = types.InlineKeyboardButton("Ростов", callback_data='city_6')
            btn7 = types.InlineKeyboardButton("Кострома", callback_data='city_7')
            btn8 = types.InlineKeyboardButton("Иваново", callback_data='city_8')
            btn9 = types.InlineKeyboardButton("Суздаль", callback_data='city_9')
            btn10 = types.InlineKeyboardButton("Владимир", callback_data='city_10')

            markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10)

            bot.send_message(message.chat.id, 'Историю какого города желаете изучить?', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # Информация о городах
    try:
        if call.message:
            if call.data == 'city_1':
                bot.send_message(call.message.chat.id,
                                 'https://ru.wikipedia.org/wiki/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0')
            elif call.data == 'city_2':
                bot.send_message(call.message.chat.id,
                                 'https://ru.wikipedia.org/wiki/%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3')
            elif call.data == 'city_3':
                bot.send_message(call.message.chat.id,
                                 'https://ru.wikipedia.org/wiki/%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9_%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4')
            elif call.data == 'city_4':
                bot.send_message(call.message.chat.id,
                                 'https://ru.wikipedia.org/wiki/%D0%A1%D0%B5%D1%80%D0%B3%D0%B8%D0%B5%D0%B2_%D0%9F%D0%BE%D1%81%D0%B0%D0%B4')
            elif call.data == 'city_5':
                bot.send_message(call.message.chat.id,
                                 'https://ru.wikipedia.org/wiki/%D0%9F%D0%B5%D1%80%D0%B5%D1%81%D0%BB%D0%B0%D0%B2%D0%BB%D1%8C-%D0%97%D0%B0%D0%BB%D0%B5%D1%81%D1%81%D0%BA%D0%B8%D0%B9')
            elif call.data == 'city_6':
                bot.send_message(call.message.chat.id,
                                 'https://ru.wikipedia.org/wiki/%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2')
            elif call.data == 'city_7':
                bot.send_message(call.message.chat.id,
                                 'https://ru.wikipedia.org/wiki/%D0%9A%D0%BE%D1%81%D1%82%D1%80%D0%BE%D0%BC%D0%B0')
            elif call.data == 'city_8':
                bot.send_message(call.message.chat.id,
                                 'https://ru.wikipedia.org/wiki/%D0%98%D0%B2%D0%B0%D0%BD%D0%BE%D0%B2%D0%BE')
            elif call.data == 'city_9':
                bot.send_message(call.message.chat.id,
                                 'https://ru.wikipedia.org/wiki/%D0%A1%D1%83%D0%B7%D0%B4%D0%B0%D0%BB%D1%8C')
            elif call.data == 'city_10':
                bot.send_message(call.message.chat.id,
                                 'https://ru.wikipedia.org/wiki/%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%BC%D0%B8%D1%80_(%D0%B3%D0%BE%D1%80%D0%BE%D0%B4,_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D1%8F)')
            # удалить встроенные кнопки
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Приятного изучения!",reply_markup=None)


    except Exception as e:
        print(repr(e))


# Запуск бота
bot.polling(none_stop=True)
