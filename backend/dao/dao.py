import logging

from backend.dao.base import BaseDAO
from backend.models import User, Habit


logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - [%(levelname)s] -  %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")
logger = logging.getLogger(__name__)

class UserDAO(BaseDAO):
    model = User

    @classmethod
    async def update_token(cls, telegram_id: int, token: str) -> None:
        """Обновляет токен пользователя в базе данных."""
        logger.info('Обновляем токен у пользователя')
        user = await cls.find_one_or_none(telegram_id=telegram_id)
        if not user:
            raise ValueError(f"Пользователь с telegram_id={telegram_id} не найден")

        await cls.update(user, token=token)




class HabitDAO(BaseDAO):
    model = Habit
