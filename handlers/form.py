from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from re import fullmatch
from database import edit_profile
from states import Form

router = Router()


@router.message(Command("form"))
async def fill_profile(message: Message, state: FSMContext):
    await state.set_state(Form.name)
    await message.answer("Введите имя")


@router.message(Form.name)
async def form_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Form.surname)
    await message.answer("Введите фамилию")


@router.message(Form.surname)
async def form_surname(message: Message, state: FSMContext):
    await state.update_data(surname=message.text)
    await state.set_state(Form.email)
    await message.answer("Введите адрес электронной почты")


@router.message(Form.email)
async def form_email(message: Message, state: FSMContext):
    if fullmatch("([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+)", message.text):
        await state.update_data(email=message.text)
        data_dict = await state.get_data()
        await state.clear()
        data = list(data_dict.values())
        await edit_profile(data, message.from_user.id)
        await message.answer(
            "Спасибо, анкета заполнена! Нажмите /menu, чтобы перейти в меню",
        )
    else:
        await message.answer("Введите корректный адрес электронной почты")


@router.message(Form.wait)
async def wait(message: Message):
    await message.answer(f"Не понимаю :( Перед тем, как начать, вам нужно заполнить небольшую анкету "
                         f"из трех вопросов: имя, фамилия и адрес электронной почты. Нажмите /form, чтобы начать")

