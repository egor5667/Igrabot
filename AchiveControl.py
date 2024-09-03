from aiogram.types import Message as message
from DBcontrol import Achives
from aiogram import Bot
from testconf import TOKEN_API

bot = Bot(token=TOKEN_API)

class AchFReg:
   def getRegAch(uid):
      if not (Achives.SerchAchive(uid, 'reg')):
         text = 'Поздравляю! Вы получили достижение "Welcome to the club..."'
         Achives.AddAchive(uid, 'reg')
         return text
      return 'None'












