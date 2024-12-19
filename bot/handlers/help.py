import logging

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - [%(levelname)s] -  %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")
logger = logging.getLogger(__name__)

help_router = Router()


@help_router.message(Command("help"))
async def echo_msg(message: Message):
    logger.info("Нажата команда /help")
    await message.answer("➕ Добавить привычку - Добавление (надеюсь полезной ) привычки в твой список\n"
                         "➖ Удалить привычку - Удаление привычки из твоего списка\n"
                         "📝 Редактировать привычку - Редактирование твоей привычки(название, кол-во дней и тд.)\n"
                         "Для просмотра команд, жми /commands")