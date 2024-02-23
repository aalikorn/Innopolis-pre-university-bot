from aiogram.types import Message
import database
from aiogram.filters import CommandStart
from states import Form
from aiogram.fsm.context import FSMContext
from aiogram import Router

router = Router()


@router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    await state.set_state(Form.wait)
    await database.db_start()
    await database.create_profile(user_id=message.from_user.id)
    await message.answer(f"Перед тем, как начать, вам нужно заполнить небольшую анкету из трех вопросов: имя, фамилия и адрес электронной почты. Нажмите /form, чтобы начать")

