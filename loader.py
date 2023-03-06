from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from loguru import logger

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)

logger.add('log_info.log',
           format="{time} - {level} - {message}",
           level='DEBUG')
