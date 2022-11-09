import sqlite3 as sq
from Handlers.create_bot import bot
from Handlers import client

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton



class BotDB:

    def __init__(self,db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

	def create_start():
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
			return ret[0]
