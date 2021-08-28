import logging
from aiogram import Bot, Dispatcher
from shazamio import Shazam

API_TOKEN = '1862285490:AAHyFKYuAWY8-NeC9rZ_5uRNDzu1aMNkDI4'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
shazam = Shazam()
