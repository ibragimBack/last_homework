from aiogram import Router,types
from aiogram.filters import Command
from random import choice

rp_router = Router()

@rp_router.message(Command('random_pic'))
async def picture(message: types.Message):
    photo_1 = types.FSInputFile('images/cat.jpeg')
    photo_2 = types.FSInputFile ('images/horse.jpeg')
    photo_3 = types.FSInputFile('images/porshe_911.jpeg')
    photo_4 = types.FSInputFile ('images/Unknown.jpeg')
    random_photo = [photo_4, photo_3, photo_2, photo_1]
    await message.answer_photo(photo=(choice(random_photo)))
