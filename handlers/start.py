from aiogram.types import Message
import database
from aiogram.filters import CommandStart
from states import Form
from aiogram.fsm.context import FSMContext
from aiogram import Router
import messages
import markup
from states import Menu

router = Router()


@router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    # await database.db_start()
    # if not await database.is_exists(message.from_user.id):
    #     await state.set_state(Form.wait)
    #     await database.db_start()
    #     await message.answer(f"Перед тем, как начать, вам нужно заполнить небольшую анкету. Нажмите /form, чтобы начать")
    # else:
    await message.answer(
        text=messages.menuMessage,
        reply_markup=markup.menu_kb,
        parse_mode='html')
    await state.set_state(Menu.menu)

