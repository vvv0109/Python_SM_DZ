from unittest.mock import call
import random
from aiogram.types import InputFile
from config import dp, bot
from aiogram import types
from aiogram.dispatcher.filters import Text
total=150
take=150
@dp.message_handler(commands=['start'])
async def start_bot(message: types.Message):
    w=str(message)
    print(w)
    with open('users.txt', 'a', encoding='utf-8') as txt:
        print(w, file=txt)
    keyboard = types.ReplyKeyboardMarkup()
    button_1 = types.KeyboardButton(text="Всё или ничего! Погнали")
    keyboard.add(button_1)
    button_2 = "Да ну...пойду отсюда"
    keyboard.add(button_2)
    photo = InputFile("12.png")
    await bot.send_photo(chat_id=message.chat.id, photo=photo, reply_markup=keyboard)
@dp.message_handler(commands=['startr'])
async def choice_bot(message: types.Message):
    flag = (message.text)
    if flag=="Да ну...пойду отсюда":
        await message.reply(f'!!! СЛАБАК!!!')
    else:
        await message.reply(f'{message.from_user.first_name}, НАЧНЁМ ИГРУ ')
@dp.message_handler()
async def all_bot(message: types.Message):
    global total
    flag = (message.text)
    if flag=="Да ну...пойду отсюда":
        await message.reply(f'!!! СЛАБАК!!! ОТКАЗАТЬСЯ НЕЛЬЗЯ!!!')
    await message.reply(f'{message.from_user.first_name}, НАЧНЁМ ИГРУ ')
    take = (message.text)
    print(take)
    take = int(take)
    print(f'{message.from_user.first_name} взял {take}' )
    if 0 < take <29:
         total-=int(message.text)
         await message.reply(f'{message.from_user.first_name}, взял {message.text} конфет, осталось {total} ')
    else:
         await message.reply(f'!!! Ошибка, введи допустимо значение конфет!!!')
    q=random.randint(0, 29)
    total -= q
    await message.reply(f'Бот, взял {q} конфет, осталось {total} ')
    return








