from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def choose_genre_kb():
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='Боевик'),
                KeyboardButton(text='Комедия')
            ],
            [
                KeyboardButton(text='Романтика'),
                KeyboardButton(text='Мистика')
            ],
            [
                KeyboardButton(text='Фантастика'),
                KeyboardButton(text='Приключения')
            ]
        ]
    )
    return kb