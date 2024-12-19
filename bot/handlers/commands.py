import logging

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from bot.keyboards.inline_keyboard import main_keyboard

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - [%(levelname)s] -  %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")
logger = logging.getLogger(__name__)

cmd_router = Router()


@cmd_router.message(Command("commands"))
async def get_commands_list(message: Message):
    logger.info("Нажата команда /commands")
    await message.answer("Список команд", reply_markup=main_keyboard())
