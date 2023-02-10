from aiogram.utils import executor
from Handlers.create_bot import dp
from data_base import sqlite_db
import data_base
from Handlers import client, admin

async def on_startup(_):
    print('Бот вышел в онлайн')

admin.register_handlers_admin(dp)
client.register_handlers_client(dp)





executor.start_polling(dp,skip_updates=True, on_startup=on_startup)