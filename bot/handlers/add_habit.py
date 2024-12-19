import logging

from aiogram import F, Router
from aiogram.types import CallbackQuery

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - [%(levelname)s] -  %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")
logger = logging.getLogger(__name__)

add_habit_router = Router()


@add_habit_router.callback_query(F.data == "add_h")
async def cmd_start(call: CallbackQuery):
    """Обрабатываем кнопку 'добавить привычку' """
    logger.info("Обрабатываем кнопку add_h")
    await call.message.answer("Сработал CallbackQuery!!!")
