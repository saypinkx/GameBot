from aiogram import types


def start_markup():
    keyboard = types.InlineKeyboardMarkup()
    handler_button0 = types.InlineKeyboardButton(text='👤Мой профиль', callback_data='my_donations')
    handler_button1 = types.InlineKeyboardButton(text='🛒Магазин', callback_data='donate_blood')
    handler_button2 = types.InlineKeyboardButton(text='💬Отзывы', callback_data='magazine')
    handler_button3 = types.InlineKeyboardButton(text='⚔️Клуб', callback_data='club')
    handler_button4 = types.InlineKeyboardButton(text='⚙️Главная', callback_data='start')
    keyboard.row(handler_button0, handler_button1)
    keyboard.row(handler_button2, handler_button3)
    keyboard.row(handler_button4)
    return keyboard
