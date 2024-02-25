from aiogram import types, Router, F
from aiogram.filters import Command
from keyboards.parsing_kb import parsing_kb
from parser.houses import get_houses_links, get_html, MAIN_URL, get_title

parsing_router = Router()

html = get_html(MAIN_URL)

@parsing_router.message(Command('parsing'))
async def parsing_kb_process(message: types.Message):
    await message.answer('Hello choose option', reply_markup=parsing_kb())

@parsing_router.message(F.text.lower() == 'парсинг ссылок с сайта')
async def parsing_links(message: types.Message):
    links = '\n'.join(get_houses_links(html))
    await message.answer(links)

@parsing_router.message(F.text.lower() == 'парсинг тайтла с сайта')
async def parsing_title(message: types.Message):
    title = get_title(html)
    await message.answer(title)

