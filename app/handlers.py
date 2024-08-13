from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram import Router, F


import app.keyboards as kb
from statuses import Reg

router = Router()

dfac = {
    'et': 'Естественно-технологический факультет',
    'sport': 'Высшая шк. физической культуры и спорта',
    'ist': 'Исторический факультет',
    'doshfak': 'Факультет дошкольного образования',
    'fiko': 'Факультет инклюзивного и коррекц. образования',
    'inyaz': 'Факультет иностранных языков',
    'mfi': 'Факультет математики, физики и информатики',
    'unk': 'Факультет подгот. учителей начальных классов',
    'filfak': 'Филологический факультет',
    'colege': 'Колледж',
    'psifak': 'Факультет психологии',
    'ppi': 'Профессионально-педагогический институт'
}




@router.message(Command("help"))
async def help_comand(message: Message):
    await message.reply("Какой-то текст")


@router.message(Command('start'))
async def start_comand(message: Message, state: FSMContext):
    await message.answer("Привет! Меня зовут Игрик. Я бот-помощник клуба настольных игр 'Играриум'. Давай знакомиться.")
    await state.set_state(Reg.qname)
    await message.answer("Введите свое имя")

# @router.callback_query(F.data == 'catalog')
# async def catal(calback: CallbackQuery):
#     await calback.answer('')
#     await calback.message.edit_text('Привет!', reply_markup=kb.settings)

@router.message(Reg.qname)
async def reg_s2(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Reg.qsname)
    await message.answer("Введите фамилию")


@router.message(Reg.qsname)
async def regFin(message: Message, state: FSMContext):
    await state.update_data(Sname=message.text)
    await message.answer("Выберите свой факультет", reply_markup=kb.faculty_one)

@router.callback_query(F.data == 'next')


@router.message(Command('hell'))
async def hell_comand(message: Message):
    await message.answer("ЭТО МОЁ БЛЯТЬ ДУШЕВНОЕ РАВНОВЕСИЕ!")
