import asyncio
import logging

from aiogram import Bot, Dispatcher
import logging

from testconf import TOKEN_API
from app.handlers import router

bot = Bot(token=TOKEN_API)
dp = Dispatcher()


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
