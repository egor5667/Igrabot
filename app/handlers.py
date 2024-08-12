from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram import Router
import app.keyboards as kb


router = Router()


class Reg(StatesGroup):
    name = State()
    Sname = State()


@router.message(Command("help"))
async def help_comand(message: Message):
    await message.reply("Какой-то текст")


@router.message(Command('start'))
async def start_comand(message: Message, state: FSMContext):
    await message.answer("Привет! Меня зовут Игрик. Я бот-помощник клуба настольных игр 'Играриум'. Давай знакомиться.",
                         reply_markup=kb.settings)
    await state.set_state(Reg.name)
    await message.answer("Введите свое имя")


@router.message(Reg.name)
async def reg_s2(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Reg.Sname)
    await message.answer("Введите фамилию")


@router.message(Reg.Sname)
async def regFin(message: Message, state: FSMContext):
    await state.update_data(Sname=message.text)
    data = await state.get_data()
    await message.answer(f"Регистрация завершена.Имя {data['name']}, фамилия {data['Sname']}")
    await state.clear()


@router.message(Command('hell'))
async def hell_comand(message: Message):
    await message.answer("ЭТО МОЁ БЛЯТЬ ДУШЕВНОЕ РАВНОВЕСИЕ!")
