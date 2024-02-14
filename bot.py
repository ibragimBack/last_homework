from aiogram import Bot,Dispatcher,types
from dotenv import load_dotenv
from os import getenv
from db.base import DB_Film

load_dotenv()
bot = Bot(token=getenv('TOKEN'))
dp = Dispatcher()
db = DB_Film()

async def set_commands():
    await bot.set_my_commands([
        types.BotCommand(command='start', description='Начало'),
        types.BotCommand(command='myinfo', description='Информация о вас'),
        types.BotCommand(command='random_pic', description='Случайное фото'),
        types.BotCommand(command='choose_genre', description='Выбор жанра'),
        types.BotCommand(command='movie_poll', description='Опрос'),
        types.BotCommand(command='top_films', description='топ фильмы')
    ])
