from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os, config

#https://t.me/PolitePatriotBot
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)
