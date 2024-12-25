import logging

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from backend.dao.dao import UserDAO

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - [%(levelname)s] -  %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")
logger = logging.getLogger(__name__)

start_router = Router()


@start_router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    """Обработка команды старт"""
    logger.info("Нажата команда /start")

    # TODO Здесь нужно выполнить проверку авторизации наверно
    # user = await UserDAO.find_one_or_none(telegram_id=message.from_user.id)

    # if not user:
    #     logger.info("USER не найден")
    #     await UserDAO.add(
    #         telegram_id=message.from_user.id,
    #         first_name=message.from_user.first_name,
    #         last_name=message.from_user.last_name,
    #         username=message.from_user.username
    #     )

    await message.answer(
        "Приветствую тебя!👋\n"
        "Это бот-трекер для отслеживания привычек👁\n"
        "Если хочешь посмотреть что умеет этот бот жми /help👈\n"
        "Если хочешь посмотреть список команд, жми /commands"
    )
