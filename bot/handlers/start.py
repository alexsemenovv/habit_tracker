import logging

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from backend.api.utils import send_data
from backend.dao.dao import UserDAO

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - [%(levelname)s] -  %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")
logger = logging.getLogger(__name__)

start_router = Router()


@start_router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    """Обработка команды старт"""
    logger.info("Нажата команда /start")

    # создаём словарь с данными пользователя
    data = {
        "telegram_id": message.from_user.id,
        "first_name": message.from_user.first_name,
        "username": message.from_user.username,
        "last_name": message.from_user.last_name
    }

    # Проверяем существует ли юзер. Если нет - то добавляем его в бд
    user = await UserDAO.find_one_or_none(telegram_id=message.from_user.id)
    if not user:
        logger.error("USER не найден")
        await send_data(
            url="http://localhost:8000/auth/register",
            data=data
        )
        logger.info("Пользователь добавлен в БД")

    logger.info("Получаем токен")
    token_response = await send_data(
        url="http://localhost:8000/auth/login",
        data=data
    )
    token = token_response.json().get("access_token")

    # Сохраняем токен (в базе данных)
    await UserDAO.update_token(telegram_id=message.from_user.id, token=token)

    await message.answer(
        "Приветствую тебя!👋\n"
        "Это бот-трекер для отслеживания привычек👁\n"
        "Если хочешь посмотреть что умеет этот бот жми /help👈\n"
        "Если хочешь посмотреть список команд, жми /commands"
    )
