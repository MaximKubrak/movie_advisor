from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from data_base import sqlite_db,base,cur
from Handlers.create_bot import bot
import config
from Handlers.create_bot import dp

class FsmAdmin(StatesGroup):
    category = State()
    name = State()
    description = State()
    price = State()

#начало диалога с администратором
async def cancel(message: types.Message,state:FSMContext):
    current_state = await state.get_state()
    if(current_state==None):
        return
    await state.finish()
    await message.reply("отменено",reply=False)

async def cm_start(message:types.Message):
    print(message.from_user.id)
   # if(message.from_user.id!=config.id1):
    #    await message.reply("Нет прав",reply=False)
     #   return None
    await FsmAdmin.category.set()
    await message.reply("Категория",reply=False)
async def load_category(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["category"] = message.text
    await FsmAdmin.next()
    await message.reply("Имя", reply=False)

async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["name"] = message.text
    await FsmAdmin.next()
    await message.reply("Описание", reply=False)

async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["description"] = message.text
    await FsmAdmin.next()
    await message.reply("Цена", reply=False)

async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["price"] = message.text
    await sqlite_db.sql_add_command(state)
    await state.finish()

async def show_menu(message: types.Message):
    for ret in cur.execute("SELECT name, category, description, price FROM menu").fetchall():
        await bot.send_message(message.from_user.id, f"Название {ret[0]}\nКатегория {ret[1]}\nОписание {ret[2]}\nЦена {ret[3]}")


def register_handlers_admin(dp: Dispatcher):
        dp.register_message_handler(cancel, Text(equals="отмена", ignore_case=True), state="*")
        dp.register_message_handler(cm_start, commands=["add"], state=None)
        dp.register_message_handler(load_category, state=FsmAdmin.category)
        dp.register_message_handler(load_name, state=FsmAdmin.name)
        dp.register_message_handler(load_description, state=FsmAdmin.description)
        dp.register_message_handler(load_price, state=FsmAdmin.price)
        dp.register_message_handler(show_menu, commands=["show"])