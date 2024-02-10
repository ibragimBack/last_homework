import asyncio
from bot import bot,dp,set_commands
from handlers import (
    start_router,
    myinfo_router,
    rp_router,
    choose_genre_router,
    movie_poll_router
)


async def main():
    await set_commands()

    dp.include_router(start_router)
    dp.include_router(myinfo_router)
    dp.include_router(rp_router)
    dp.include_router(choose_genre_router)
    dp.include_router(movie_poll_router)

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())