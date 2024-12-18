from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def main_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text="Добавить привычку", callback_data="add_h")
    builder.button(text="Удалить привычку", callback_data="remove_h")
    builder.button(text="Редактировать привычку", callback_data="edit_h")
    builder.adjust(2, 1)
    return builder.as_markup()
