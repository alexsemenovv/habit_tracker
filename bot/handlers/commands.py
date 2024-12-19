from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from bot.keyboards.inline_keyboard import main_keyboard

cmd_router = Router()


@cmd_router.message(Command("commands"))
async def get_commands_list(message: Message):
    await message.answer("Список команд", reply_markup=main_keyboard())


@cmd_router.callback_query(F.data == "add_h")
async def cmd_start(call: CallbackQuery):
    """Обрабатываем кнопку 'добавить привычку' """
    await call.message.answer("Сработал CallbackQuery!!!")
