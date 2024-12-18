from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

from bot.keyboards.inline_keyboard import main_keyboard

start_router = Router()


@start_router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    await message.answer(
        "Приветствую тебя!👋\n"
        "Это бот-трекер для отслеживания привычек👁\n"
        "Если хочешь посмотреть что умеет этот бот нажми /help👈",
        reply_markup=main_keyboard()
    )


@start_router.callback_query(F.data == "add_h")
async def cmd_start(call: CallbackQuery):
    """Обрабатываем кнопку 'добавить привычку' """
    await call.message.answer("Сработал CallbackQuery!!!")


@start_router.message(Command("help"))
async def echo_msg(message: Message):
    await message.answer("➕ Добавить привычку - Добавление (надеюсь полезной ) привычки в твой список\n"
                         "➖ Удалить привычку - Удаление привычки из твоего списка\n"
                         "📝 Редактировать привычку - Редактирование твоей привычки(название, кол-во дней и тд.)")
