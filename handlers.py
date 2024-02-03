from aiogram import Router
from aiogram.types import Message
import murkup
import database
from aiogram.filters import CommandStart
from datahandling import name_handling


router = Router()
user_data = ''


@router.message(CommandStart())
async def start(message: Message):
    await database.db_start()
    global user_data
    await database.create_profile(user_id=message.from_user.id)
    if user_data == '':
        await message.answer(f"Пожалуйста, введите имя и почту через пробел: ")
    else:
        await message.answer("Меню: ", reply_markup=murkup.to_menu_kb)


@router.message(lambda message: user_data == '')
async def set_name(message: Message):
    global user_data
    test_data = message.text
    if test_data.count(' ') == 1:
        user_data = test_data
        data = await name_handling(user_data)
        await database.edit_profile(data, message.from_user.id)
        await message.answer("Спасибо! Меню: ", reply_markup=murkup.to_menu_kb)
    else:
        await message.answer(f"Пожалуйста, введите корректные имя и почту через пробел: ")


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