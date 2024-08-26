#Файл, в котором прописанны хэндлеры, отвечающие за регистрацию пользователей
from datetime import datetime
from time import sleep

from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram import Router, F, Bot

from testconf import TOKEN_API
bot = Bot(token=TOKEN_API)

import app.keyboards as kb
from app.keyboards import KeyAdm
from config import SPEC_ROLE
from lerning import users
from testconf import ADM_IDS, SPEC_ROLE
from app.statuses import Reg, AdmStatus
import DBcontrol
from  app.Timecontrol import TimeCount
from app.sendler import sedText

router = Router()

reg_info = {}



@router.message(Command("help"))
async def help_comand(message: Message):
    await message.reply("Какой-то текст")


@router.message(Command('start'))
async def start_comand(message: Message, state: FSMContext):
    await message.answer("Привет! Меня зовут Игрик. Я бот-помощник клуба настольных игр 'Играриум'.")
    if DBcontrol.RegistrDB.FindID(int(message.from_user.id)):
        await message.answer('С возвращением!')
    else:
        DBcontrol.RegistrDB.sentID(int(message.from_user.id))
        await state.set_state(Reg.qname)
        await message.answer("Давай знакомиться! \n"
                             "Введите свое имя")
    if ADM_IDS.count(str(message.from_user.id)) > 0:
        DBcontrol.RegistrDB.sentRole(int(message.from_user.id), 'adm')
        if SPEC_ROLE.count(str(message.from_user.id)) > 0:
            await message.answer('Вам назначена роль "Конь-в-пальто". Поздравляю!')
        await state.set_state(AdmStatus.qact)
        await message.answer('Вам назначена роль "Администратор"', reply_markup=kb.KeyAdm.menuKey)
    else:
        DBcontrol.RegistrDB.sentRole(int(message.from_user.id), 'chlen')


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
    DBcontrol.RegistrDB.sentSName(int(message.from_user.id), str(message.text))
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
    DBcontrol.RegistrDB.sentInstitute(int(message.from_user.id), str(message.text))


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
    DBcontrol.RegistrDB.sentFacult(int(message.from_user.id), str(message.text))
    await message.answer('Понял, принял, теперь напиши на каком ты курсе. Достаточно просто отправить цифру в чат',
                         reply_markup=kb.base_key)
    await state.set_state(Reg.qcourse)


@router.message(Reg.qcourse)
async def check_reg(message: Message, state: FSMContext):
    await state.update_data(course=message.text)
    DBcontrol.RegistrDB.sentCourse(int(message.from_user.id), str(message.text))
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
        # await DBcontrol.sent_registData(reg_info)
        await state.clear()
    if message.text == '❌Нет':
        await message.answer('Ой, давай попробуем пройти пройти регистрацию еще раз. '
                             'Если снова не получится, я передам информацию о проблеме в техническую поддержку.\n\n'
                             'Нажми 👉 /start')
        # Сделать уведомление для админов о проблемушках



@router.message(Command('hell'))
async def hell_comand(message: Message):
    await message.answer("ЭТО МОЁ БЛЯТЬ ДУШЕВНОЕ РАВНОВЕСИЕ!", reply_markup=kb.base_key)



@router.message(AdmStatus.qact)
async def GetAdmAct(message: Message, state: FSMContext):
    if message.text == 'Встречи':
        await message.answer('Выберите действие', reply_markup=KeyAdm.meetKey)
        await state.set_state(AdmStatus.meets)
    elif message.text == 'Создать рассылку':
        await message.answer('Введите текст расылки')
        await state.set_state(AdmStatus.qTextsends)

@router.message(AdmStatus.meets)
async def GetMeets(message: Message, state: FSMContext):
    if message.text == 'Начать встречу':
        global st_meet
        st_meet = datetime.now()
        await message.answer(f'Вы запустили встречу в {st_meet.strftime("%H:%M")}')

    elif message.text == 'Завершить встречу':
        end_meet = datetime.now()
        await message.answer('Встреча завершется...')
        DBcontrol.Meets.sendMeetData(datetime.now().strftime("%d.%m.%Y"),
                                     st_meet.strftime("%H:%M"),
                                     end_meet.strftime("%H:%M"),
                                     TimeCount(st_meet, end_meet))
        sleep(5)
        await message.answer(f'Встреча завершена в {end_meet.strftime("%H:%M")}. \n\n '
                             f'Длительность встречи: {TimeCount(st_meet, end_meet)} секунд', reply_markup=KeyAdm.menuKey)
        await state.set_state(AdmStatus.qact)

@router.message(AdmStatus.qTextsends)
async def GetSendText(message: Message, state: FSMContext):
    global sendlerText
    sendlerText = message.text
    await message.answer(f'Проверьте текст рассылки \n\n'
                         f'{sendlerText}', reply_markup=KeyAdm.sendKey)
    await state.set_state(AdmStatus.confsends)

@router.message(AdmStatus.confsends)
async def GetSendText(message: Message, state: FSMContext):
    if message.text == 'Завершить создание рассылки':
        await message.answer('Отправляю сообщения...')
        users = DBcontrol.rassl.getUsersID('adm')
        await sedText(users, sendlerText)
        await message.answer('Успешная рассылка')

    elif message.text == 'Редактировать текст':
        await message.answer('Давай поновый. Всё хуйня. Вводи всё еще раз.')
        await state.set_state(AdmStatus.qTextsends)






