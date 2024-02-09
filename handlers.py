from aiogram import Router
from aiogram.types import Message
import murkup
import database
from aiogram.filters import CommandStart


router = Router()
user_data = ''


@router.message(CommandStart())
async def start(message: Message):
    await database.db_start()
    global user_data
    await database.create_profile(user_id=message.from_user.id)
    await message.answer(f"Перед тем, как начать, вам нужно заполнить небольшую анкету из трех вопросов: имя, фамилия и адрес электронной почты. Нажмите /form, чтобы начать")


@router.message()
async def echo(message: Message):
    if message.text in ['Открыть меню', 'Назад в меню']:
        await message.answer("Меню: ", reply_markup=murkup.menu_kb)
    elif message.text == "онлайн-курс":
        await message.answer("Нажмите кнопку, чтобы перейти на сайт", reply_markup=murkup.link_kb)
        await message.answer("Меню: ", reply_markup=murkup.menu_kb)
    elif message.text in ["об олимпиадах", "обратно к олимпиадам"]:
        await message.answer("Выберите интересующую олимпиаду", reply_markup=murkup.olymp_kb)
    elif message.text == "ВсОШ":
        await message.answer("Информация об олимпиаде", reply_markup=murkup.course_info_kb)
    elif message.text == "РсОШ":
        await message.answer("Информация об олимпиаде", reply_markup=murkup.course_info_kb)
    elif message.text == "InnopolisOpen":
        await message.answer("Информация об олимпиаде", reply_markup=murkup.course_info_kb)
    elif message.text == "Как подготовиться?":
        await message.answer("Информация о курсах", reply_markup=murkup.course_info_kb)
    elif message.text == "квест":
        await message.answer("Выберите направление", reply_markup=murkup.tests_kb)
    else:
        await message.answer(f"Я тебя не понимаю :(")