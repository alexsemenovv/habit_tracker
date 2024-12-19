from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

help_router = Router()


@help_router.message(Command("help"))
async def echo_msg(message: Message):
    await message.answer("➕ Добавить привычку - Добавление (надеюсь полезной ) привычки в твой список\n"
                         "➖ Удалить привычку - Удаление привычки из твоего списка\n"
                         "📝 Редактировать привычку - Редактирование твоей привычки(название, кол-во дней и тд.)")