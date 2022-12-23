from unittest.mock import call
from random import randint
from aiogram.types import InputFile
from config import dp, bot
from aiogram import types
from aiogram.dispatcher.filters import Text
flag=str()
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
@dp.message_handler()
async def all_bot(message: types.Message):
    global flag
    global total
    flag = (message.text)
    if (flag == "Да ну...пойду отсюда"):
        await message.reply(f'!!! СЛАБАК!!!')
        photo = InputFile("13.jpg")
        await bot.send_photo(chat_id=message.chat.id, photo=photo)
        total=150
    elif(flag == "Всё или ничего! Погнали" ):
        await message.reply(f'{message.from_user.first_name}, НАЧНЁМ ИГРУ, ВВЕДИ ЧИСЛО ')
    print(flag)
    take = flag
    print(take)
    take = int(take)
    if 0 < take <29:
         total-=int(message.text)
         await message.reply(f'{message.from_user.first_name}, взял(а) {message.text} конфет, осталось {total} ')
    else:
         await message.reply(f'!!! Ты можешь взять только 29 конфет. Ход переходит Пиле!!!')
    if total<=29:
        await message.reply(f'Игра окончена!, Ты СВОБОДЕН')
        total=150
    move = total % 29
    if move == 0:
        move = randint(1, 29) if total >= 29 else total
    total -= move
    await message.reply(f'Пила, взял {move} конфет, осталось {total} ')
    if total<=29:
        await message.reply(f'Ты можешь взять не больше 28 конфет, после твоего хода оснется не больше 28 конфет на столе и ПИЛА их все забирает, Игра окончена!,выиграл Пила ')
        photo = InputFile("13.jpg")
        await bot.send_photo(chat_id=message.chat.id, photo=photo)
        total=150










