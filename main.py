import asyncio
from aiogram import types
from handlers.bot import bot,dp
from handlers import (
    start_router,
    myinfo_router,
    rp_router,
    choice_router
)

dp.include_router(start_router)

dp.include_router(myinfo_router)

dp.include_router(rp_router)

dp.include_router(choice_router)

async def main():
    await bot.set_my_commands([
        types.BotCommand(command='start', description='Начало'),
        types.BotCommand(command='myinfo', description='Информация о вас'),
        types.BotCommand(command='random_pic', description='Случайное фото'),
        types.BotCommand(command='choice', description='Выбор жанра')
    ])
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())