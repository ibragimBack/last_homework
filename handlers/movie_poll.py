from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from keyboards.movie_poll_kb import iron_man_kb, artificial_intelligence_kb, latest_brand_armor_kb

class MoviePoll(StatesGroup):
    name = State()
    age = State()
    favorite_actor = State()
    favorite_film = State()
    iron_man = State()
    artificial_intelligence = State()
    latest_brand_armor = State()

movie_poll_router = Router()

@movie_poll_router.message(Command('movie_poll'))
async def process_movie_poll(message: types.Message, state: FSMContext):
    await state.set_state(MoviePoll.name)
    await message.answer("Если хотите остановить опрос используйте команду /stop")
    await message.answer("Как вас зовут?")

@movie_poll_router.message(Command('stop'))
async def stop(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Спасибо за уделенное время")

@movie_poll_router.message(MoviePoll.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(f"Приятно познакомится {message.text}")
    await state.set_state(MoviePoll.age)
    await message.answer("Сколько вам лeт?")

@movie_poll_router.message(MoviePoll.age)
async def process_age(message: types.Message, state: FSMContext):
    age = message.text
    if not age.isdigit():
        await message.answer("Вазраст должен быть числом!")
        return
    await state.update_data(age=message.text)
    await state.set_state(MoviePoll.favorite_actor)
    await message.answer("Ваш любимый актер или актриса?")

@movie_poll_router.message(MoviePoll.favorite_actor)
async def process_favorite_actor(message: types.Message, state: FSMContext):
    await state.update_data(favorite_actor=message.text)
    await state.set_state(MoviePoll.favorite_film)
    await message.answer("Ваш любимый фильм?")

@movie_poll_router.message(MoviePoll.favorite_film)
async def process_favorite_film(message: types.Message, state: FSMContext):
    await state.update_data(favorite_film=message.text)
    await state.set_state(MoviePoll.iron_man)
    await message.answer("Из какого фильма персонаж по имени Тони Старк?", reply_markup=iron_man_kb())

@movie_poll_router.message(MoviePoll.iron_man)
async def process_favorite_film(message: types.Message, state: FSMContext):
    await state.update_data(iron_man=message.text)
    await state.set_state(MoviePoll.artificial_intelligence)
    await message.answer("Как зовут первого исскуственного интелекта помощника Тони Старка?", reply_markup=artificial_intelligence_kb())

@movie_poll_router.message(MoviePoll.artificial_intelligence)
async def process_iron_man(message: types.Message, state: FSMContext):
    await state.update_data(artificial_intelligence=message.text)
    await state.set_state(MoviePoll.latest_brand_armor)
    await message.answer("Назовите марку последней брони Железного Человека?", reply_markup=latest_brand_armor_kb())

@movie_poll_router.message(MoviePoll.latest_brand_armor)
async def process_latest_brand_armor(message: types.Message, state: FSMContext):
    remove_kb = types.ReplyKeyboardRemove()
    await state.update_data(latest_brand_armor=message.text)
    data = await state.get_data()
    await message.answer(f'Спасибо за уделенное время и вот ваши данные {data}', reply_markup=remove_kb)
    await state.clear()


