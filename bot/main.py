import logging
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from config import TOKEN
from handlers.start import start_router

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - [%(levelname)s] -  %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")
logger = logging.getLogger(__name__)

bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage()) # состояния пользователей будут храниться в оперативной памяти


async def main() -> None:
    dp.include_router(start_router) # Добавляем роутер start_router в диспетчер dp
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot) # Запускаем бота в режиме опроса (polling)

if __name__ == "__main__":
    asyncio.run(main())


