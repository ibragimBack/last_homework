from aiogram import Router, types, F
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from bot import bot, scheduler


class Remind(StatesGroup):
    user_text = State()

remind_router = Router()

@remind_router.message(F.text.lower() == 'напомни')
async def remind_func(message: types.Message, state: FSMContext):
    await state.set_state(Remind.user_text)
    await message.answer(f'Здравствуйте {message.from_user.username} что вам напомнить?')

@remind_router.message(Remind.user_text)
async def process_user_text(message: types.Message, state: FSMContext):
    await state.update_data(text=message.text)
    data = await state.get_data()
    scheduler.add_job(
        remind_process,
        'interval',
        seconds=10,
        kwargs={'chat_id': message.from_user.id,'text': data['text']}
    )

async def remind_process(chat_id: int, text: str):
    await bot.send_message(
        chat_id=chat_id,
        text=text
    )
