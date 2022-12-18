import sqlite3
from data_base import base,cur
from Handlers.create_bot import bot
async def sql_add_command(state):
	async with state.proxy() as data:
		cur.execute('INSERT INTO menu (category, name, description, price) VALUES (?, ?, ?, ?)', tuple(data.values()))
		base.commit();

async def sql_imp_command(message):
	for ret in cur.execute("SELECT name, category, description, price FROM menu").fetchall():
		await bot.send_message(message.from_user.id, f"Название {ret[0]}\nКатегория {ret[1]}\nОписание {ret[2]}\nЦена {ret[3]}")


async def sql_show_name(message):
	for ret in cur.execute("SELECT name FROM menu").fetchall():
		return ret[0]
