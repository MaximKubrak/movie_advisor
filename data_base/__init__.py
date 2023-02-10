import sqlite3
base = sqlite3.connect("Muxomor.db")
cur = base.cursor()
base.execute('CREATE TABLE IF NOT EXISTS menu(id INTEGER PRIMARY KEY, category TEXT, name TEXT, description TEXT, price TEXT)')
base.execute('CREATE TABLE IF NOT EXISTS korz(id INTEGER PRIMARY KEY, category TEXT, description TEXT, price TEXT)')
base.commit()

