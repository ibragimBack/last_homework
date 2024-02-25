import asyncio
from aiogram import Bot
import logging
from bot import bot, dp, db, scheduler, set_commands
from handlers import (
    start_router,
    myinfo_router,
    rp_router,
    choose_genre_router,
    movie_poll_router,
    db_films_router,
    remind_router,
    parsing_router
)

async def on_startup(bot: Bot):
    db.create_tables()
    db.populate_tables()


async def main():
    await set_commands()

    dp.include_router(start_router)
    dp.include_router(myinfo_router)
    dp.include_router(rp_router)
    dp.include_router(choose_genre_router)
    dp.include_router(movie_poll_router)
    dp.include_router(db_films_router)
    dp.include_router(remind_router)
    dp.include_router(parsing_router)

    scheduler.start()

    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())