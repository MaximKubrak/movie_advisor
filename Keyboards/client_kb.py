from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton



b1 = KeyboardButton('Привести Друга')
b2 = KeyboardButton('Каталог')
b3 = KeyboardButton('Личный кабинет')
b4 = KeyboardButton('Корзина')
b5 = KeyboardButton('FAQ')
b6 = KeyboardButton('Отзывы')
b7 = KeyboardButton('Поддержка')
b8 = KeyboardButton('Чат')
b9 = KeyboardButton('Разработчик')

b10 = KeyboardButton('Главное меню')

kb_client = ReplyKeyboardMarkup(row_width = 2)


kb_client.add(b1, b2, b3, b4, b5, b6, b7, b8).insert(b9).add(b10)
# main_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(b10)