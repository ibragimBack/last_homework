from aiogram import Router,types
from aiogram.filters import Command
from random import choice

myinfo_router = Router()

@myinfo_router.message(Command('myinfo'))
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