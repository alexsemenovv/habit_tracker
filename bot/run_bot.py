import logging

from bot.create_bot import bot
from bot.handlers.start import start_router
from bot.handlers.help import help_router
from bot.handlers.commands import cmd_router
from bot.handlers.add_habit import add_habit_router
from bot.config import settings

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - [%(levelname)s] -  %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")
logger = logging.getLogger(__name__)

routers = [start_router, help_router, cmd_router, add_habit_router]  # создаём список с роутерами


async def start_bot():
    try:
        await bot.send_message(settings.ADMIN_ID, f'Я запущен🥳.')
    except:
        pass


async def stop_bot():
    try:
        await bot.send_message(settings.ADMIN_ID, 'Бот остановлен. За что?😔')
    except:
        pass
