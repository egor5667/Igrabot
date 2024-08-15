from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram import Router, F

import app.keyboards as kb
from app.statuses import Reg

router = Router()


@router.message(Command("help"))
async def help_comand(message: Message):
    await message.reply("Какой-то текст")


@router.message(Command('start'))
async def start_comand(message: Message, state: FSMContext):
    await message.answer("Привет! Меня зовут Игрик. Я бот-помощник клуба настольных игр 'Играриум'. Давай знакомиться.")
    await state.set_state(Reg.qname)
    await message.answer("Введите свое имя")


@router.message(F.text == 'СЖЕЕЕЧЬ ВСЁЁЁЁ!!!!!')
async def delall(message: Message):
    await message.answer('ВСЁ СГОРЕЛО НАХУЙ! Теперь можно возвращаться в начало.\n\n'
                         'Нажми на 👉 /start')


@router.message(Reg.qname)
async def reg_s2(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Reg.qsname)
    await message.answer("Введите фамилию")


@router.message(Reg.qsname)
async def reg_s3(message: Message, state: FSMContext):
    await state.update_data(sname=message.text)
    await state.set_state(Reg.qinstit)
    await message.answer("Ты из педагогического?", reply_markup=kb.ped_question)


@router.message(Reg.qinstit)
async def reg_s4(message: Message, state: FSMContext):
    await state.update_data(instit=message.text)
    if message.text == '✅Да':
        await state.set_state(Reg.fped)
        await message.answer('Выбери свой фаультет', reply_markup=kb.faculty_one)
    if message.text == '❌Нет':
        await message.answer('Понял, принял, теперь напиши на каком ты курсе. Достатточно просто отправить цифру в чат')
        await state.update_data(faculty='Нет информации*')
        await state.set_state(Reg.qcourse)


@router.message(Reg.fped, F.text == '⬅️На стр. 1')
async def reg_topage1(message: Message, state: FSMContext):
    await message.answer('Принято! Переходим на страницу 1', reply_markup=kb.faculty_one)


@router.message(Reg.fped, (F.text == '➡️На стр. 2' or F.text == '⬅️На стр. 2'))
async def reg_topage2(message: Message, state: FSMContext):
    await message.answer('Принято! Переходим на страницу 2', reply_markup=kb.faculty_two)


@router.message(Reg.fped, F.text == '➡️На стр. 3')
async def reg_topage3(message: Message, state: FSMContext):
    await message.answer('Принято! Переходим на страницу 3', reply_markup=kb.faculty_three)


@router.message(Reg.fped)
async def reg_s5ped(message: Message, state: FSMContext):
    await state.update_data(faculty=message.text)
    await message.answer('Понял, принял, теперь напиши на каком ты курсе. Достатточно просто отправить цифру в чат',
                         reply_markup=kb.base_key)
    await state.set_state(Reg.qcourse)


@router.message(Reg.qcourse)
async def reg_s6(message: Message, state: FSMContext):
    await state.update_data(course=message.text)
    reg_info = await state.get_data()
    await message.answer(f'Регистрация успешно завершена. Поздравляю!)\n\n'
                         f'Давай всё проверим.\n'
                         f'Тебя зовут {reg_info['name']} {reg_info['sname']}\n'
                         f'Ты из педа: {reg_info["instit"]}\n'
                         f'твой факультет: {reg_info["faculty"]}\n'
                         f'Курс: {reg_info["course"]}\n\n\n'
                         f'*Если вы не учитесь в ЮУрГГПУ, мы не собираем информацию о Вашем факультете')
    await state.clear()


@router.message(Command('hell'))
async def hell_comand(message: Message):
    await message.answer("ЭТО МОЁ БЛЯТЬ ДУШЕВНОЕ РАВНОВЕСИЕ!", reply_markup=kb.base_key)



