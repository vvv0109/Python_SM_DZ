from aiogram.utils import executor
from aiogram import Bot, types

from config import dp
import handler

async def bot_start(_):
    print("Бот запущен")
    handler.registred_handler(dp)



if __name__=='__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True, on_startup=bot_start)
