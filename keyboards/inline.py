from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def add_to_favorite_kb(translation_id=0):
    kb=InlineKeyboardMarkup()
    kb.add(
        InlineKeyboardButton(text='Add to Favorite',
                             callback_data=f'translation_{translation_id}'),
    )
    return kb

