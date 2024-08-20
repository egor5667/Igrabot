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
