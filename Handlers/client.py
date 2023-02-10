from contextlib import suppress
from aiogram import types,Dispatcher
from aiogram.utils.exceptions import MessageNotModified

from Handlers.create_bot import dp, bot
from Keyboards import client_kb, show_case_kb
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db



#dp.message_handler(commands = ['start','help'])
async def command_start(message: types.Message):
        await bot.send_message(message.from_user.id, '👋 Вас приветствует бот магазина MUHOMORCHERNOZEM.RU\n\
🍄 Чтобы сделать первый заказ, нажмите кнопку 🌿 Каталог, выберите товары и перейдите в раздел 🛒 Корзина\n\
📦 После оплаты заказа бот отправит Вам трек-номер отправления и будет присылать по нему статусы',reply_markup = client_kb.kb_client)


async def show_case(message:types.Message):
    if message.text == 'Каталог':
        await bot.send_message(message.from_user.id, 'Выберите категорию продукта', reply_markup = show_case_kb.inline_kb)

    if message.text == 'Главное меню':
        await bot.send_message(message.from_user.id,'Ты вернулся в главное меню.', reply_markup= client_kb.kb_client)
    if message.text =='Добавить в корзину':
        await bot.send_message(message.from_user.id, ' ', reply_markup = show_case_kb.keyb(2))


@dp.callback_query_handler(lambda c: c.data == 'button1')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали красный мухомор. Какой курс желаете ?',reply_markup = show_case_kb.inline_kb2)
    await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)

@dp.callback_query_handler(lambda c: c.data == 'button2')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали Пантерный мухомор. Какой курс желаете ?',reply_markup = show_case_kb.inline_kb2)
    await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)


@dp.callback_query_handler(lambda c: c.data == 'button5')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Сколько надо? ',reply_markup = show_case_kb.keyb(1))
    #await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
@dp.callback_query_handler(lambda c: c.data == 'button12')
async def process_callback_button1(callback_query: types.CallbackQuery,num = show_case_kb.num):
    with suppress(MessageNotModified):
        await bot.answer_callback_query(callback_query.id)
        show_case_kb.num+=1
        await callback_query.message.edit_text('Сколько надо?',reply_markup= show_case_kb.keyb(show_case_kb.num))

@dp.callback_query_handler(lambda c: c.data == 'button7')
async def process_callback_button1(callback_query: types.CallbackQuery):
    show_case_kb.num = 1
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Выберите категорию продукта', reply_markup=show_case_kb.inline_kb)
    #await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
@dp.callback_query_handler(lambda c: c.data == 'button9')
async def process_callback_button1(callback_query: types.CallbackQuery):
    show_case_kb.num = 1
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы вернулись в каталог',reply_markup = show_case_kb.inline_kb)
    #await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
@dp.callback_query_handler(lambda c: c.data == 'button13')
async def process_callback_button1(callback_query: types.CallbackQuery):
    show_case_kb.num = 1
    await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)


def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(show_case)