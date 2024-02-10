from aiogram import Bot,Dispatcher,types
from dotenv import load_dotenv
from os import getenv

load_dotenv()
bot = Bot(token=getenv('TOKEN'))
dp = Dispatcher()

async def set_commands():
    await bot.set_my_commands([
        types.BotCommand(command='start', description='Начало'),
        types.BotCommand(command='myinfo', description='Информация о вас'),
        types.BotCommand(command='random_pic', description='Случайное фото'),
        types.BotCommand(command='choose_genre', description='Выбор жанра'),
        types.BotCommand(command='movie_poll', description='Опрос')
    ])
