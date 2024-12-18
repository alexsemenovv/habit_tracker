import asyncio

from create_bot import bot, dp
from handlers.start import start_router


async def main() -> None:
    dp.include_router(start_router) # Добавляем роутер start_router в диспетчер dp
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot) # Запускаем бота в режиме опроса (polling)

if __name__ == "__main__":
    asyncio.run(main())


