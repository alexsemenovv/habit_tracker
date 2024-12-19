import asyncio

from create_bot import bot, dp
from handlers.start import start_router
from handlers.help import help_router
from handlers.commands import cmd_router

routers = [start_router, help_router, cmd_router]  # создаём список с роутерами


async def main() -> None:
    dp.include_routers(*routers)  # Добавляем роутеры в диспетчер dp
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)  # Запускаем бота в режиме опроса (polling)


if __name__ == "__main__":
    asyncio.run(main())
