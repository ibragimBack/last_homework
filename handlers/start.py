from aiogram import Router,types,F
from aiogram.filters import Command

start_router = Router()

@start_router.message(Command('start'))
async def start_command(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text='Посмотреть код этого бота', url='https://github.com/ibragimBack/telegram_bot')
            ],
            [
                types.InlineKeyboardButton(text='О нашем боте', callback_data='geeks_bot')
            ],
            [
                types.InlineKeyboardButton(text='Адрес', callback_data='БЦ Victory')
            ]
        ]
    )
    await message.answer(f"Привет {message.from_user.first_name}", reply_markup=kb)


@start_router.callback_query(F.data == 'БЦ Victory')
async def victory(callback: types.CallbackQuery):
    await callback.message.answer('Ибраимова 103, Бизнес центр Victory 2 крыло 2 и 4 этаж')


@start_router.callback_query(F.data == 'geeks_bot')
async def victory(callback: types.CallbackQuery):
    await callback.message.answer('Этот бот поможет вам выбрать вам по вкусу аниме, сериал или фильм')