from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State


class Reg(StatesGroup):
    qname = State()
    qsname = State()
    qinstit = State()
    fped = State()
    noped = State()
    qfaculty = State()
    qcourse = State()
    fcheck = State()

class AdmStatus(StatesGroup):
    qact = State()
    meets = State()
    tech = State()
    qTextsends = State()
    confsends = State()
    confsendsID = State()
    phoID = State()
    stikID = State()
    qRolesends = State()
    qsendID = State()
    startMeets = State()
    TechGet = State()
    controlPanel = State()
    getUID = State()
    startSendAchive = State()
    endSendAchive = State()
    coinCount = State()
    coinUser = State()


class editProfile(StatesGroup):
    qedit = State()
    editname = State()
    editsname = State()
    editFaculty = State()
    editCourse = State()

class feedBackForms(StatesGroup):
    startForm = State()

class userMenu(StatesGroup):
    qact = State()
    qhelp = State()
    qprof = State()


