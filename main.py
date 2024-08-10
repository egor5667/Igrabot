import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from config import TOKEN_API
from statesForm import StepForm


bot = Bot(token=TOKEN_API)
dp = Dispatcher()



class Reg(StatesGroup):
    name = State()
    Sname = State()



@dp.message(Command("help"))
async def help_comand(message: Message):
    await message.reply("Какой-то текст")




@dp.message(Command('start'))
async def start_comand(message: Message, state: FSMContext):
    await message.answer("Привет! Меня зовут Игрик. Я бот-помощник клуба настольных игр 'Играриум'. Давай знакомиться.")
    await state.set_state(Reg.name)
    await message.answer("Введите свое имя")

@dp.message(Reg.name)
async def reg_s2(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Reg.Sname)
    await message.answer("Введите фамилию")

@dp.message(Reg.Sname)
async def regFin(message: Message, state: FSMContext):
    await state.update_data(Sname=message.text)
    data = await state.get_data()
    await message.answer(f"Регистрация завершена.Имя {data['Name']}, фамилия {data['Sname']}")
    await state.clear()




@dp.message(Command('hell'))
async def hell_comand(message: Message):
    await message.answer("ЭТО МОЁ БЛЯТЬ ДУШЕВНОЕ РАВНОВЕСИЕ!")

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
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
