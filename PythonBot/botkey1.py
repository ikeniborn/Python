# Настройки
import telebot
from telebot import types

token = '547154758:AAH8iuy36guDYVgLB7coMlKmMhB1tQjHclA'
bot = telebot.TeleBot(token)
# Обработка команд


@bot.message_handler(commands=['start'])



def start(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton (name) for name in ['Магнит', 'Х5',
                                                            'Дикси', 'Красное и Белое','/start']])
    msg=bot.send_message(m.chat.id, 'Выбери сеть', reply_markup=keyboard)
    bot.register_next_step_handler (msg,name1 )


@bot.message_handler (content_types = ["text"])

def name1 (m):
    if m.text == 'Х5':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(*[types.InlineKeyboardButton(text=name, callback_data=name) for
                       name in ['Перекресток', 'Пятерочка', 'Карусель', 'ПятЪница']])
        bot.send_message(m.chat.id, 'Выбери формат',
                         reply_markup=keyboard)
    elif m.text == 'Дикси':
        bot.send_message (m.chat.id, 'Пшел нахуй!',parse_mode='Markdown')
    elif m.text == 'Красное и Белое':
        bot.send_message(m.chat.id, 'Алкомаркет', parse_mode='Markdown')
    elif m.text == 'Магнит':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(*[types.InlineKeyboardButton(text=name, callback_data=name) for
                       name in ['Аптека', 'Косметик', 'Семейный', 'Магазин у дома']])
        bot.send_message(m.chat.id, 'Выбери формат',
                              reply_markup=keyboard)


@bot.callback_query_handler(func=lambda c: True)
def name2 (c):
    if c.data == 'Магазин у дома':
        bot.edit_message_text(
            chat_id=c.message.chat.id, message_id=c.message.message_id,
        text='MD',
        parse_mode='Markdown')
    elif c.data == 'Косметик':
        bot.edit_message_text(
            chat_id=c.message.chat.id, message_id=c.message.message_id,
        text='MK',
        parse_mode='Markdown')
    elif c.data == 'Семейный':
        bot.edit_message_text(
            chat_id=c.message.chat.id, message_id=c.message.message_id,
            text='GM',
            parse_mode='Markdown')
    elif c.data == 'Аптека':
        bot.edit_message_text(
            chat_id=c.message.chat.id, message_id=c.message.message_id,
            text='MA',
            parse_mode='Markdown')
    elif c.data == 'Пятерочка':
        bot.edit_message_text(
            chat_id=c.message.chat.id, message_id=c.message.message_id,
            text='MDDD',
            parse_mode='Markdown')
    elif c.data == 'Карусель':
        bot.edit_message_text(
            chat_id=c.message.chat.id, message_id=c.message.message_id,
            text='ГМ',
            parse_mode='Markdown')
    elif c.data == 'Перекресток':
        bot.edit_message_text(
            chat_id=c.message.chat.id, message_id=c.message.message_id,
            text='СМ',
            parse_mode='Markdown')
    elif c.data == 'ПятЪница':
        bot.send_photo(chat_id=c.message.chat.id, photo='https://i.ytimg.com/vi/TULkxmM75RU/maxresdefault.jpg')


bot.polling(none_stop=True)










