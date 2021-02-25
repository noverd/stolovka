from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import logging
logging.basicConfig(level=logging.INFO)

TOKEN = "1629708314:AAG-0b5MK6tk9zzaJFXDqX7tvPFcYuAMrRQ"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def echo(message: types.Message):
    await message.reply("Привет")


if __name__ == '__main__':
    executor.start_polling(dp)
