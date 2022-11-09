import sqlite3 as sq
from Handlers.create_bot import bot
from Handlers import client

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton



def sql_start():
	global base, cur
	base =sq.connect('Muxomor.db')
	cur = base.cursor()
	if base:
		print('Data base connected OK')
	base.execute('CREATE TABLE IF NOT EXISTS menu(id INTEGER PRIMARY KEY, category TEXT, name TEXT, description TEXT, price TEXT)')
	#base.execute('CREATE TABLE IF NOT EXISTS korz(id INTEGER PRIMARY KEY, category TEXT, description TEXT, price TEXT)')
	base.commit()

async def sql_add_command(state):
	async with state.proxy() as data:
		cur.execute('INSERT INTO menu VALUES (?, ?, ?, ?)', tuple(data.values()))
		base.commit()

async def sql_imp_command(message):
	for ret in cur.execute("SELECT * FROM menu").fetchall():
		await bot.send_message(message.from_user.id, f"Название {ret[0]}\nКатегория {ret[1]}\nОписание {ret[2]}\nЦена {ret[3]}")


async def sql_show_name(message):
	for ret in cur.execute("SELECT name FROM menu").fetchall():
		await bot.send_message(message.from_user.id,f'{ret[0]}', reply_markup= client_kb.main_menu)

	# first_one = res[0]
	# return first_one

