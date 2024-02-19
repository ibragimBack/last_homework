from aiogram import Router,types, F
from aiogram.filters import Command
from bot import db

from keyboards.choose_genre_kb import choose_genre_kb

choose_genre_router = Router()

@choose_genre_router.message(Command('choose_genre'))
async def chosen(message: types.Message):
    await message.answer(f'{message.from_user.first_name} выберите жанр', reply_markup=choose_genre_kb())


@choose_genre_router.message(F.text.lower() == 'боевик')
async def information(message: types.Message):
    genres = db.get_films_by_genre_name('Боевик')
    for genre in genres:
        await message.answer(f'Name: {genre[0]}\nDescription: {genre[1]}\nRating: {genre[2]}\nImage: {genre[3]}')


@choose_genre_router.message(F.text.lower() == 'романтика')
async def information(message: types.Message):
    genres = db.get_films_by_genre_name('Романтика')
    for genre in genres:
        await message.answer(f'Name: {genre[0]}\nDescription: {genre[1]}\nRating: {genre[2]}\nImage: {genre[3]}')


@choose_genre_router.message(F.text.lower() == 'комедия')
async def information(message: types.Message):
    genres = db.get_films_by_genre_name('Комедия')
    for genre in genres:
        await message.answer(f'Name: {genre[0]}\nDescription: {genre[1]}\nRating: {genre[2]}\nImage: {genre[3]}')


@choose_genre_router.message(F.text.lower() == 'приключения')
async def information(message: types.Message):
    genres = db.get_films_by_genre_name('Приключения')
    for genre in genres:
        await message.answer(f'Name: {genre[0]}\nDescription: {genre[1]}\nRating: {genre[2]}\nImage: {genre[3]}')


@choose_genre_router.message(F.text.lower() == 'фантастика')
async def information(message: types.Message):
    genres = db.get_films_by_genre_name('Фантастика')
    for genre in genres:
        await message.answer(f'Name: {genre[0]}\nDescription: {genre[1]}\nRating: {genre[2]}\nImage: {genre[3]}')


@choose_genre_router.message(F.text.lower() == 'мистика')
async def information(message: types.Message):
    genres = db.get_films_by_genre_name('Мистика')
    for genre in genres:
        await message.answer(f'Name: {genre[0]}\nDescription: {genre[1]}\nRating: {genre[2]}\nImage: {genre[3]}')