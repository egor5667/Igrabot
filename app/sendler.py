from aiogram import Bot
import DBcontrol

from testconf import TOKEN_API, ADM_IDS
bot = Bot(token=TOKEN_API)



async def sedText(users, text):
    for row in users:
        try:
            await bot.send_message(row[0], text)
            if int(row[1]) != 1:
                DBcontrol.rassl.setActive(row[0], 1)
        except:
            DBcontrol.rassl.setActive(row[0], 0)

async def sendFID(users, text):
    for row in users:
        try:
            await bot.send_message(row, text)
        except:
            await bot.send_message(ADM_IDS[0], f'Человек с ID {row}')
