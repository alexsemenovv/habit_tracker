import logging

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - [%(levelname)s] -  %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")
logger = logging.getLogger(__name__)

start_router = Router()


@start_router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    logger.info("Нажата команда /start")
    await message.answer(
        "Приветствую тебя!👋\n"
        "Это бот-трекер для отслеживания привычек👁\n"
        "Если хочешь посмотреть что умеет этот бот жми /help👈\n"
        "Если хочешь посмотреть список команд, жми /commands"
    )
