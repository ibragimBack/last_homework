from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def iron_man_kb():
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='Марвел'),
                KeyboardButton(text='Железный Человек')
            ],
            [
                KeyboardButton(text='Человек Паук'),
                KeyboardButton(text='Война Бесконечности')
            ]
        ]
    )
    return kb

def artificial_intelligence_kb():
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='Джарвис'),
                KeyboardButton(text='Пятница')
            ],
            [
                KeyboardButton(text='Альтрон'),
                KeyboardButton(text='Все ответы неправильные')
            ]
        ]
    )
    return kb

def latest_brand_armor_kb():
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='Марк 50'),
                KeyboardButton(text='Марк 102')
            ],
            [
                KeyboardButton(text='Марк 7'),
                KeyboardButton(text='Марк 85')
            ]
        ]
    )
    return kb