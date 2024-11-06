from data.loader import bot
from telebot import types
from .commands import start





@bot.callback_query_handler(func=lambda call: 'translation' in call.data)
def add_to_favorite(call: types.CallbackQuery):
    print(call.data)
    bot.answer_callback_query(call.id, 'Added to Favorite')
    start(call.message)