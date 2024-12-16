from loader import bot
from logging import DEBUG
import logging

logging.basicConfig(level=DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    bot.infinity_polling()
