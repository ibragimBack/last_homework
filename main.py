import asyncio
from aiogram import Bot,Dispatcher,types
from aiogram.filters import Command
from dotenv import load_dotenv
from os import getenv
from random import choice

load_dotenv()
bot = Bot(token=getenv('TOKEN'))
dp = Dispatcher()

@dp.message(Command('start'))
async def start_command(message: types.Message):
    await message.answer(f"Привет {message.from_user.first_name}")

@dp.message(Command('myinfo'))
async def info(message: types.Message):
    photo_1 = types.FSInputFile('images/cat.jpeg')
    photo_2 = types.FSInputFile('images/horse.jpeg')
    photo_3 = types.FSInputFile('images/porshe_911.jpeg')
    photo_4 = types.FSInputFile('images/Unknown.jpeg')
    random_photo = [photo_4, photo_3, photo_2, photo_1]
    await message.answer_photo(photo=(choice(random_photo)), caption=f'''Ващи данные:
    Ваш id: {message.from_user.id}
    Ваше имя: {message.from_user.first_name}
    Ваш user name: {message.from_user.username}
    ''')

@dp.message(Command('random_pic'))
async def picture(message: types.Message):
    photo_1 = types.FSInputFile('images/cat.jpeg')
    photo_2 = types.FSInputFile ('images/horse.jpeg')
    photo_3 = types.FSInputFile('images/porshe_911.jpeg')
    photo_4 = types.FSInputFile ('images/Unknown.jpeg')
    random_photo = [photo_4, photo_3, photo_2, photo_1]
    await message.answer_photo(photo=(choice(random_photo)))

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())