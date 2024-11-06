from data.loader import bot, translator
from telebot import types
from keyboards.reply import lang_kb
from keyboards.inline import add_to_favorite_kb
from googletrans import LANGCODES
from database import db



@bot.message_handler(func=lambda msg: msg.text=='Translation')
def start_translation(message: types.Message):
    chat_id=message.chat.id
    bot.send_message(chat_id, 'Choose language from which translate',
                     reply_markup=lang_kb())

    bot.register_next_step_handler(message, get_lang_from)

def get_lang_from(message: types.Message):
     chat_id=message.chat.id
     bot.send_message(chat_id, 'Choose language to which    translate',
                      reply_markup=lang_kb())

     bot.register_next_step_handler(message,get_lang_to, message.text)


def get_lang_to(message: types.Message, lang_from):
    print('lang_from', lang_from)
    print('lang_to', message.text)

    chat_id=message.chat.id
    bot.send_message(chat_id, 'Write text for translation', reply_markup=types.ReplyKeyboardRemove())
    bot.register_next_step_handler(message,translate, lang_from, message.text)


def translate(message: types.Message, lang_from: str,  lang_to: str):
    code_from=LANGCODES.get(lang_from)
    code_to=LANGCODES.get(lang_to)
    text=message.text
    translated_text=translator.translate(text, code_to, code_from).text
    db.add_translation(
        original=message.text,
        translated=translated_text,
        code_from=code_from,
        code_to=code_to,
        chat_id=message.chat.id
    )
    msg=f'''
Original: <b>{text}</b>
Translation: <b>{translated_text}</b>
From which: <b>{code_from}</b>
To which: <b>{code_to}</b>
'''
    bot.send_message(message.chat.id, msg, parse_mode='HTML',
                     reply_markup=add_to_favorite_kb())



@bot.message_handler(func=lambda msg: msg.text=='History')
def history(message: types.Message):
    chat_id=message.chat.id
    history_records=db.get_history(chat_id)

    if not history_records:
        bot.send_message(chat_id, 'Your history of translations')
    else:
        history_message = 'Your history of translations:\n'
        for record in history_records:
            history_message += f'{record}\n'
        bot.send_message(chat_id, history_message)






