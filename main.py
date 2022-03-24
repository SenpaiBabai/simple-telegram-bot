from bot import Bot
from config import BOT_TOKEN
from loguru import logger

logger.add("my_log.log", colorize=True, format="<green>{time}</green> <level>{message}</level>")

my_bot = Bot(token=BOT_TOKEN)

for event in my_bot.start_pooling():
    logger.info("Новый ивент")