from aiogram import Router, types
from aiogram.filters import Command
from bot import db

db_films_router = Router()

@db_films_router.message(Command('top_films'))
async def process_top_films(message: types.Message):
    films = db.get_films()
    for film in films:
        await message.answer(f'Name: {film[1]}\nDescription: {film[2]}\nRating: {film[3]}\nGenre:{film[4]}\nImage: {film[5]}')