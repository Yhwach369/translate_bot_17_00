from data.loader import bot
from telebot import types
from keyboards.reply import start_kb
from database import db


@bot.message_handler(commands=['start'])
def start(message: types.Message):
    chat_id=message.chat.id
    db_user_id, is_exists =db.get_user_id(chat_id)
    if not is_exists:
        db.add_user(chat_id)

    print(db_user_id)
    first_name=message.from_user.first_name
    msg=f'Hello, {first_name}. Welcome to translater bot.\nChoose command below 👇🏿👇🏿👇🏿.'
    bot.send_message(chat_id, msg, reply_markup=start_kb())



