from telebot import types
from googletrans import LANGCODES


def start_kb():
    kb=types.ReplyKeyboardMarkup(
        resize_keyboard=True
    )
    kb.row(
        types.KeyboardButton(text='Translation'),
        types.KeyboardButton(text='History'),

    )
    return kb


def lang_kb():
    kb=types.ReplyKeyboardMarkup(
        resize_keyboard=True
    )
    buttons=[]
    for lang in LANGCODES.keys():
        buttons.append(
            types.KeyboardButton(text=lang)
        )
    kb.add(*buttons)
    return kb
