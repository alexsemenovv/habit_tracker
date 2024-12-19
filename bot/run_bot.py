import asyncio
import logging

from create_bot import bot, dp
from handlers.start import start_router
from handlers.help import help_router
from handlers.commands import cmd_router
from handlers.add_habit import add_habit_router

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - [%(levelname)s] -  %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")
logger = logging.getLogger(__name__)

routers = [start_router, help_router, cmd_router, add_habit_router]  # создаём список с роутерами


async def main() -> None:
    """Функция запуска бота"""
    logger.info("Запускаем бота")
    dp.include_routers(*routers)  # Добавляем роутеры в диспетчер dp
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)  # Запускаем бота в режиме опроса (polling)


if __name__ == "__main__":
    asyncio.run(main())
