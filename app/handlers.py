#Файл, в котором прописанны хэндлеры, отвечающие за регистрацию пользователей


from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram import Router, F


import app.keyboards as kb
from app.statuses import Reg
import DBcontrol

router = Router()

reg_info = {}



@router.message(Command("help"))
async def help_comand(message: Message):
    await message.reply("Какой-то текст")


@router.message(Command('start'))
async def start_comand(message: Message, state: FSMContext):
    await message.answer("Привет! Меня зовут Игрик. Я бот-помощник клуба настольных игр 'Играриум'. Давай знакомиться.")
    if DBcontrol.RegistrDB.FindID(int(message.from_user.id)):
        await message.answer('С возвращением!')
    else:
        DBcontrol.RegistrDB.sentID(int(message.from_user.id))
        await state.set_state(Reg.qname)
        await message.answer("Введите свое имя")


@router.message(F.text == 'СЖЕЕЕЧЬ ВСЁЁЁЁ!!!!!')
async def delall(message: Message):
    await message.answer('ВСЁ СГОРЕЛО НАХУЙ! Теперь можно возвращаться в начало.\n\n'
                         'Нажми на 👉 /start')


@router.message(Reg.qname)
async def reg_s2(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    DBcontrol.RegistrDB.sentName(int(message.from_user.id), message.text)
    await state.set_state(Reg.qsname)
    await message.answer("Введите фамилию")


@router.message(Reg.qsname)
async def reg_s3(message: Message, state: FSMContext):
    await state.update_data(sname=message.text)
    await state.set_state(Reg.qinstit)
    await message.answer("Ты из педагогического?", reply_markup=kb.YNkeyb)


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
async def check_reg(message: Message, state: FSMContext):
    await state.update_data(course=message.text)
    info = await state.get_data()
    global reg_info
    reg_info[str(message.from_user.id)] = info
    # print(reg_info)
    await message.answer(f'Я понял тебя. Все данные записаны. Поздравляю!)\n\n'
                         f'Давай всё проверим.\n'
                         f'Тебя зовут {reg_info[str(message.from_user.id)]['name']} {reg_info[str(message.from_user.id)]['sname']}\n'
                         f'Ты из педа: {reg_info[str(message.from_user.id)]["instit"]}\n'
                         f'твой факультет: {reg_info[str(message.from_user.id)]["faculty"]}\n'
                         f'Курс: {reg_info[str(message.from_user.id)]["course"]}\n\n\n'
                         f'*Если вы не учитесь в ЮУрГГПУ, мы не собираем информацию о Вашем факультете')
    await message.answer('Всё правильно?', reply_markup=kb.YNkeyb)
    await state.set_state(Reg.fcheck)


@router.message(Reg.fcheck)
async def FinCheck(message: Message, state: FSMContext):
    if message.text == '✅Да':
        await message.answer('Ура! Поздравляю, теперь регистрация закончилась. Спасибо, что присоединился к нам!')
        import DBcontrol
        await DBcontrol.sent_registData(reg_info)
        await state.clear()
    if message.text == '❌Нет':
        await message.answer('Ой, давай попробуем пройти пройти регистрацию еще раз. '
                             'Если снова не получится, я передам информацию о проблеме в техническую поддержку.\n\n'
                             'Нажми 👉 /start')
        # Сделать уведомление для админов о проблемушках



@router.message(Command('hell'))
async def hell_comand(message: Message):
    await message.answer("ЭТО МОЁ БЛЯТЬ ДУШЕВНОЕ РАВНОВЕСИЕ!", reply_markup=kb.base_key)
