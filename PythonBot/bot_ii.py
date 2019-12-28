# Настройки
import telebot
from telebot import types

token = '547154758:AAH8iuy36guDYVgLB7coMlKmMhB1tQjHclA'
bot = telebot.TeleBot(token)
# Обработка команд


@bot.message_handler(commands=['start'])



def start(m):

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton (name) for name in ['Магнит', 'Пятерочка',
                                                            'Дикси', 'Красное и Белое','/start']])
    msg=bot.send_message(m.chat.id, 'Какие акции интересны?(За мат извиняюсь,'
                                    ' это пилотная версия и я психую)', reply_markup=keyboard)
    bot.register_next_step_handler (msg,name1 )
    return start

@bot.message_handler(content_types=  ["text"])
def name1 (m):
    if m.text == 'Пятерочка':
        bot.send_message (m.chat.id, 'Пшел нахуй',parse_mode='Markdown')
    elif m.text == 'Дикси':
        bot.send_message (m.chat.id, 'Пшел нахуй!',parse_mode='Markdown')
    elif m.text == 'Красное и Белое':
        bot.send_message(m.chat.id, 'Пшел нахуй!!', parse_mode='Markdown')
    elif m.text == 'Магнит':
        bot.send_message(m.chat.id, 'Мяяяу нахуй^^', parse_mode='Markdown')
    else :
        bot.send_message(m.chat.id, 'Ошибка нахуй!!!!', parse_mode='Markdown')

bot.polling(none_stop=True)




