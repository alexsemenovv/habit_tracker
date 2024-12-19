import logging

from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - [%(levelname)s] -  %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")
logger = logging.getLogger(__name__)


def main_keyboard() -> InlineKeyboardMarkup:
    logger.info("Выводим клавиатуру пользователю")
    builder = InlineKeyboardBuilder()
    builder.button(text="Добавить привычку", callback_data="add_h")
    builder.button(text="Удалить привычку", callback_data="remove_h")
    builder.button(text="Редактировать привычку", callback_data="edit_h")
    builder.adjust(2, 1)
    return builder.as_markup()
