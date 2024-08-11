import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from config import TOKEN_API
from app.handlers import router



bot = Bot(token=TOKEN_API)
dp = Dispatcher()




# @dp.message(Command("start"))
# async def cmd_start(message: types.Message):
#     kb = [
#         [types.KeyboardButton(text="Сам пшел нахуй!")],
#         [types.KeyboardButton(text="Нет, это ты иди нахуй")]
#     ]
#     keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
#     await message.answer("Пошел нахуй!", reply_markup=keyboard)
#
# @dp.message(F.text.lower() == "нет, это ты иди нахуй")
# async def one(message: types.Message):
#     await message.reply("Нет, ты!")
#
# @dp.message(F.text.lower() == "сам пшел нахуй!")
# async def two(message: types.Message):
#     await message.reply("ТОлько после тебя!")
async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
