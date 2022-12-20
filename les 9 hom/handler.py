from aiogram import types, Dispatcher
import commands

def registred_handler(dp: Dispatcher):
    dp.register_message_handler(commands.start_bot, commands=['start'])
    dp.register_message_handler(commands.all_bot)


