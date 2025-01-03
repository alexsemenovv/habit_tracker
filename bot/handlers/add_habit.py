import logging

from aiogram import F, Router
from aiogram.types import CallbackQuery

from backend.api.utils import send_data
from backend.dao.dao import UserDAO

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - [%(levelname)s] -  %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")
logger = logging.getLogger(__name__)

add_habit_router = Router()


@add_habit_router.callback_query(F.data == "add_h")
async def cmd_start(call: CallbackQuery):
    """Обрабатываем кнопку 'добавить привычку' """
    logger.info("Обрабатываем кнопку add_h")

    user = await UserDAO.find_one_or_none(telegram_id=call.from_user.id)
    if not user or not user.token:
        logger.error(f"Пользователь, tg_id={call.from_user.id}")
        raise ValueError("Токен пользователя не найден")

    headers = {
        "Authorization": f"Bearer {user.token}"
    }

    habit = {
        "habit_name": 'Пресс',
        "description": 'Качать пресс каждый день',
        "user_id": "33"
    }
    logger.info('Отправляем запрос')
    await send_data(
        url="http://localhost:8000/api/habits",
        data=habit,
        headers=headers
    )
    await call.message.answer("Сработал CallbackQuery!!!")
