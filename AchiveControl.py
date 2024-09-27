from symtable import Class

from aiogram.types import Message as message
from DBcontrol import Achives
from aiogram import Bot
from testconf import TOKEN_API

bot = Bot(token=TOKEN_API)

class AchFReg:
   def getRegAch(uid):
      if not (Achives.SerchAchive(uid, 'reg')):
         text = ('Поздравляю! Вы получили достижение "Welcome to the club..."\n\n'
                 'Вам начисленно 15 ПИ-коинов')
         Achives.AddAchive(uid, 'reg')
         return text
      return 'None'

class FreeAchive:
   def getFreeAch(uid, servName):
      if not (Achives.SerchAchive(uid, servName)):
         Achives.AddAchive(uid, servName)
         return True
      return False

class achFIgTech:
   def TechUpdate(uid, lvl):
      Achives.TechCount(uid)
      if lvl == 1:
         Achives.coinUpdater(uid, 25)
      elif lvl == 2:
         Achives.coinUpdater(uid, 35)
      elif lvl == 3:
         Achives.coinUpdater(uid, 45)












