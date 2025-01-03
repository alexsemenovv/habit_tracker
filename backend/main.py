from contextlib import asynccontextmanager
import logging

from fastapi import FastAPI, Request
from aiogram.types import Update

from bot.create_bot import bot, dp
from bot.config import settings
from bot.run_bot import routers, start_bot, stop_bot
from backend.api.habits import router as habits_router
from backend.api.auth import router as auth_router

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - [%(levelname)s] -  %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.info("Starting bot setup...")
    dp.include_routers(*routers)
    await start_bot()
    webhook_url = settings.get_webhook()
    await bot.set_webhook(
        url=webhook_url,
        allowed_updates=dp.resolve_used_update_types(),
        drop_pending_updates=True
    )
    logging.info(f"Webhook set to {webhook_url}")
    yield
    await bot.delete_webhook()
    await stop_bot()
    logger.info('Webhook removed')


app = FastAPI(lifespan=lifespan)
app.include_router(habits_router)
app.include_router(auth_router)


@app.post("/webhook")
async def webhook(request: Request) -> None:
    logger.info('Received webhook request')
    update = Update.model_validate(await request.json(), context={"bot": bot})
    await dp.feed_update(bot, update)
    logging.info("Update processed")
