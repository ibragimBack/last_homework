from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def parsing_kb():
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='парсинг ссылок с сайта'),
                KeyboardButton(text='парсинг тайтла с сайта')
            ]
        ]
    )
    return kb