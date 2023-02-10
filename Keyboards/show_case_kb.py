from Handlers.create_bot import bot
from data_base import cur
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

res = cur.execute("SELECT category,price FROM menu").fetchall()
inline_btn_1 = InlineKeyboardButton(res[0][0], callback_data='button1')
inline_btn_2 = InlineKeyboardButton(res[1][0], callback_data='button2')
inline_kb = InlineKeyboardMarkup(row_width=1).add(inline_btn_1, inline_btn_2)
num = 1

# inline_kb = InlineKeyboardMarkup().add(inline_btn_3)
# inline_kb = InlineKeyboardMarkup().add(inline_btn_1,inline_btn_2)
# inline_kb = InlineKeyboardMarkup().add(inline_btn_1,inline_btn_2,inline_btn_3)
# inline_kb = InlineKeyboardMarkup().row(inline_btn_1,inline_btn_2,inline_btn_3)
# inline_kb = InlineKeyboardMarkup().add(inline_btn_4,inline_btn_5,inline_btn_6)

inline_btn_3 = InlineKeyboardButton('1 месяц',callback_data = 'button3')
inline_btn_4 = InlineKeyboardButton('3 месяца',callback_data = 'button4')
inline_kb2 = InlineKeyboardMarkup(row_width=1).row(inline_btn_3,inline_btn_4)


inline_btn_5 = InlineKeyboardButton('Добавить в корзину',callback_data = 'button5')
#inline_btn_6 = InlineKeyboardButton('<-',callback_data = 'button6')
inline_btn_7 = InlineKeyboardButton('Выбрать другой',callback_data = 'button7')
#inline_btn_8 = InlineKeyboardButton('->',callback_data = 'button8')
inline_btn_9 = InlineKeyboardButton('Вернуться в каталог',callback_data = 'button9')
inline_kb3 = InlineKeyboardMarkup().insert(inline_btn_5).add(inline_btn_7).insert(inline_btn_9)

def keyb(num):
    inline_btn_10 = InlineKeyboardButton(' - ',callback_data = 'button10')
    inline_btn_11= InlineKeyboardButton(num ,callback_data = 'button11')
    inline_btn_12 = InlineKeyboardButton(' + ',callback_data = 'button12')
    inline_btn_13 = InlineKeyboardButton(f' {int(res[0][1])*num} - перейти в корзину ',callback_data = 'button13')
    inline_kb4 = InlineKeyboardMarkup().add(inline_btn_10, inline_btn_11, inline_btn_12).insert(inline_btn_13)
    return inline_kb4

