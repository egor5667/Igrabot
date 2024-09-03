#Файл, в котором прописанны хэндлеры, отвечающие за взаимодействие с пользователями
from datetime import datetime
from time import sleep

from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram import Router, F, Bot

from testconf import TOKEN_API
bot = Bot(token=TOKEN_API)

import app.keyboards as kb
from app.keyboards import KeyAdm, base_key, editKey
from testconf import ADM_IDS, SPEC_ROLE
from app.statuses import Reg, AdmStatus, userMenu, editProfile
import DBcontrol
from  app.Timecontrol import TimeCount
from app.sendler import sedText
import AchiveControl

router = Router()

reg_info = {}



@router.message(Command("help"))
async def help_comand(message: Message):
    await message.reply("Я буду напоминатьо вам о встречах, раздавать достижения в клубе и сообщать важную информацию.")


@router.message(Command('start'))
async def start_comand(message: Message, state: FSMContext):
    await message.answer("Привет! Меня зовут Игрик. Я бот-помощник клуба настольных игр 'Играриум'.")
    await message.answer('Из-за большого количества запросов время ответа может быть увеличено.\n Спасибо за понимание.')
    if DBcontrol.RegistrDB.FindID(int(message.from_user.id)):
        text = AchiveControl.AchFReg.getRegAch(message.from_user.id)
        if text != 'None':
            await message.answer(text)
        await message.answer('С возвращением!', reply_markup=base_key)
        await state.set_state(userMenu.qact)
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
    await message.answer('Понял, принял, теперь напиши на каком ты курсе. Достаточно просто отправить цифру в чат')
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
                         f'Тебя зовут {reg_info[str(message.from_user.id)]["name"]} {reg_info[str(message.from_user.id)]["sname"]}\n'
                         f'Ты из педа: {reg_info[str(message.from_user.id)]["instit"]}\n'
                         f'твой факультет: {reg_info[str(message.from_user.id)]["faculty"]}\n'
                         f'Курс: {reg_info[str(message.from_user.id)]["course"]}\n\n\n'
                         f'*Если вы не учитесь в ЮУрГГПУ, мы не собираем информацию о Вашем факультете')
    await message.answer('Всё правильно?', reply_markup=kb.YNkeyb)
    await state.set_state(Reg.fcheck)


@router.message(Reg.fcheck)
async def FinCheck(message: Message, state: FSMContext):
    if message.text == '✅Да':
        await message.answer_photo(photo = 'AgACAgIAAxkBAAICm2bUdxAgj2vU6NzkyzLftKfofBQtAALR3jEbFY6hSidi3586Bn4rAQADAgADeQADNQQ',
                                   caption ='Ура! Поздравляю, теперь регистрация закончилась. Спасибо, что присоединился к нам!',
                                   reply_markup=base_key)
        await message.answer(AchiveControl.AchFReg.getRegAch(message.from_user.id))
        await message.answer_sticker('CAACAgIAAxkBAAICnmbUdyeDAevdrt88kPc9EI5pwmugAAIYVQACFThpSoaY4Mhc9xoLNQQ')
        await state.set_state(userMenu.qact)
        del reg_info[str(message.from_user.id)]
    if message.text == '❌Нет':
        await message.answer('Ой, давай попробуем пройти пройти регистрацию еще раз. '
                             'Если снова не получится, я передам информацию о проблеме в техническую поддержку.\n\n'
                             'Нажми 👉 /start')
        await bot.send_message(ADM_IDS[0], f'АЛАРМ! У пользователя с  @{message.from_user.username}"'
                                           f' проблемы с регистрацией. Пожалуйста уточни у него, всё ли хорошо.')


@router.message(userMenu.qact)
async def startUserMenu(message: Message, state: FSMContext):
    if message.text == 'Профиль':
        await message.answer(f'И так, что мы знаем о тебе?\n'
                             f'Имя: {DBcontrol.GetData.GetUserInfo(message.from_user.id)["name"]} \n'
                             f'Фамилия: {DBcontrol.GetData.GetUserInfo(message.from_user.id)["sname"]}\n'
                             f'Ты из педа? {DBcontrol.GetData.GetUserInfo(message.from_user.id)["institute"]}\n'
                             f'Факультет: {DBcontrol.GetData.GetUserInfo(message.from_user.id)["facult"]}\n'
                             f'Курс: {DBcontrol.GetData.GetUserInfo(message.from_user.id)["course"]} \n\n'
                             f'Посетил встреч: Информация о встречах скоро станет доступна. Следите за обновлниями бота.')
    elif message.text == 'Мне нужна помощь!':
        await message.answer('Напишите пожалуйста, в чем проблема и мы передадим Ваше обращение в поддержку.')
        await state.set_state(userMenu.qhelp)
    elif message.text == 'Редактировать профиль':
        await message.answer('Выберите что нужно отредактировать', reply_markup=editKey)
        await state.set_state(editProfile.qedit)

@router.message(editProfile.qedit)
async def choseEdit(message: Message, state: FSMContext):
    if message.text == 'Имя':
        await message.answer('Введите нове имя')
        await state.set_state(editProfile.editname)
    elif message.text == 'Фамилия':
        await message.answer('Введите новую фамилию')
        await state.set_state(editProfile.editsname)
    elif message.text == 'Факультет':
        await message.answer('Введите новый факультет')
        await state.set_state(editProfile.editFaculty)
    elif message.text == 'Курс':
        await message.answer('Введите новый курс')
        await state.set_state(editProfile.editCourse)
    elif message.text == 'Завершить редактирование':
        await message.answer('Понял, принял. Редактирование завершено', reply_markup=base_key)
        await state.set_state(userMenu.qact)

@router.message(editProfile.editname)
async def editProfileName(message: Message, state: FSMContext):
    DBcontrol.RegistrDB.sentName(message.from_user.id, message.text)
    await message.answer('Имя отредактировано', reply_markup=editKey)
    await state.set_state(editProfile.qedit)

@router.message(editProfile.editsname)
async def editProfileSname(message: Message, state: FSMContext):
    DBcontrol.RegistrDB.sentSName(message.from_user.id, message.text)
    await message.answer('Фамилия отредактирована', reply_markup=editKey)
    await state.set_state(editProfile.qedit)

@router.message(editProfile.editFaculty)
async def editProfileFaculty(message: Message, state: FSMContext):
    DBcontrol.RegistrDB.sentFacult(message.from_user.id, message.text)
    await message.answer('Факультет отредактирован', reply_markup=editKey)
    await state.set_state(editProfile.qedit)

@router.message(editProfile.editCourse)
async def editProfileCourse(message: Message, state: FSMContext):
    DBcontrol.RegistrDB.sentCourse(message.from_user.id, message.text)
    await message.answer('Курс отредактирован', reply_markup=editKey)
    await state.set_state(editProfile.qedit)


@router.message(userMenu.qhelp)
async def sendHelp(message: Message, state: FSMContext):
    text = message.text
    await bot.send_message(ADM_IDS[0], f'Новое обращение: \n\n'
                                       f'{text} \n\n'
                                       f'От пользователя: @{message.from_user.username}')
    await message.answer('Я передал Ваше обращение в поддержку. В ближайшее время c Вами свяжутся.')

# @router.message(Command('hell'))
# async def hell_comand(message: Message):
#     await message.answer("ЭТО МОЁ БЛЯТЬ ДУШЕВНОЕ РАВНОВЕСИЕ!", reply_markup=kb.base_key)



@router.message(AdmStatus.qact)
async def GetAdmAct(message: Message, state: FSMContext):
    if message.text == 'Встречи':
        await message.answer('Выберите действие', reply_markup=KeyAdm.meetKey)
        await state.set_state(AdmStatus.meets)
    elif message.text == 'Создать рассылку':
        await message.answer('Введите текст расылки')
        await state.set_state(AdmStatus.qTextsends)
    elif message.text == 'Получить ID фото':
        await message.answer('Отправьте фото и я напишу его ID в терминал')
        await state.set_state(AdmStatus.phoID)
    elif message.text == 'Получить стикер ID':
        await message.answer('Отправьте стикер')
        await state.set_state(AdmStatus.stikID)

@router.message(AdmStatus.phoID)
async def sendPhotoId(message: Message, state: FSMContext):
    print(f'photo: {message.photo[-1].file_id}')
    await state.set_state(AdmStatus.qact)

@router.message(AdmStatus.stikID)
async def sendStikId(message: Message, state: FSMContext):
    print(f'stiker: {message.sticker.file_id}')
    await state.set_state(AdmStatus.qact)

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
                         f'{sendlerText}', reply_markup=KeyAdm.choseRole)
    await state.set_state(AdmStatus.qRolesends)

@router.message(AdmStatus.qRolesends)
async def GetRoles(message: Message, state: FSMContext):
    global sendlerRole
    sendlerRole = ''
    if message.text == 'Администраторы':
        sendlerRole = 'adm'
        await message.answer(f'Выбрана роль: {sendlerRole}', reply_markup=KeyAdm.sendKey)
        await state.set_state(AdmStatus.confsends)
    elif message.text == 'Участники':
        sendlerRole = 'chlen'
        await message.answer(f'Выбрана роль: {sendlerRole}', reply_markup=KeyAdm.sendKey)
        await state.set_state(AdmStatus.confsends)
    elif message.text == 'По ID':
        await message.answer('Введите ID пользователя')
        await state.set_state(AdmStatus.qsendID)

@router.message(AdmStatus.qsendID)
async def getsendID(message: Message, state: FSMContext):
    global senID
    senID = int(message.text)
    await message.answer('Выбери действие', reply_markup=KeyAdm.sendKey)
    await state.set_state(AdmStatus.confsendsID)

@router.message(AdmStatus.confsendsID)
async def EndIDsendText(message: Message, state: FSMContext):
    if message.text == 'Завершить создание рассылки':
        await message.answer('Отправляю сообщения...')
        await bot.send_message(senID, sendlerText)
        await message.answer('Успешная рассылка', reply_markup=KeyAdm.menuKey)
        await state.set_state(AdmStatus.qact)
    elif message.text == 'Редактировать текст':
        await message.answer('Давай поновый. Всё хуйня. Вводи всё еще раз.')
        await state.set_state(AdmStatus.qTextsends)



@router.message(AdmStatus.confsends)
async def EndSendText(message: Message, state: FSMContext):
    if message.text == 'Завершить создание рассылки':
        await message.answer('Отправляю сообщения...')
        users = DBcontrol.rassl.getUsersID(sendlerRole)
        await sedText(users, sendlerText)
        await message.answer('Успешная рассылка', reply_markup=KeyAdm.menuKey)
        await state.set_state(AdmStatus.qact)
    elif message.text == 'Редактировать текст':
        await message.answer('Давай поновый. Всё хуйня. Вводи всё еще раз.')
        await state.set_state(AdmStatus.qTextsends)






