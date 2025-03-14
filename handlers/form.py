import re

from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from re import fullmatch, match
from database import edit_profile
from states import Form
from markup import agree_conf_kb, agree_adds_kb

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
    await state.set_state(Form.phone)
    await message.answer("Введите номер телефона в формате +7...")


@router.message(Form.phone)
async def form_phone(message: Message, state: FSMContext):
    if fullmatch(r'^\+7\d{10}$', message.text):
        await state.update_data(phone=message.text)
        await state.set_state(Form.email)
        await message.answer("Введите адрес электронной почты")
    else:
        await message.answer("Введите корректный номер телефона в формате +7...")


@router.message(Form.email)
async def form_email(message: Message, state: FSMContext):
    if fullmatch("([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+)", message.text):
        await state.update_data(email=message.text)
        await state.set_state(Form.birth_date)
        await message.answer(
            "Введите дату рождения в формате ДД.ММ.ГГГГ",
        )
    else:
        await message.answer("Введите корректный адрес электронной почты")


@router.message(Form.birth_date)
async def form_birth(message: Message, state: FSMContext):
    if fullmatch(r'^(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.\d{4}$', message.text):
        await state.update_data(birth_date=message.text)
        await state.set_state(Form.grade)
        await message.answer(
            "В каком классе школы вы учитесь? Напишите 0, если не учитесь в школе",
        )
    else:
        await message.answer("Введите дату рождения в формате ДД.ММ.ГГГГ")


@router.message(Form.grade)
async def form_grade(message: Message, state: FSMContext):
    if message.text.isdigit() and len(message.text) < 3:
        await state.update_data(grade=int(message.text))
        await state.set_state(Form.interests)
        await message.answer(
            "Вам интересны: 1) Колледж 2) Бакалавриат 3) Магистратура 4) Аспирантура 5) Образовательные курсы 6) Другое\n\nНапишите цифры всех подходящих вариантов без пробелов и других разделительных символов. Пример: 15",
        )
    else:
        await message.answer("Отправьте только число - класс школы, в котором вы учитесь. Напишите 0, если не учитесь в школе")


@router.message(Form.interests)
async def form_interests(message: Message, state: FSMContext):
    if message.text.isdigit() and len(message.text) < 7:
        await state.update_data(interests=int(message.text))
        await state.set_state(Form.conf_agreement)
        await message.answer(
            "Продолжая, соглашаюсь с политикой обработки персональных данных",
            reply_markup= agree_conf_kb
        )
    else:
        await message.answer("Вам интересны: 1) Колледж 2) Бакалавриат 3) Магистратура 4) Аспирантура 5) Образовательные курсы 6) Другое\n\nНапишите цифры всех подходящих вариантов без пробелов и других разделительных символов. Пример: 15")


@router.message(Form.conf_agreement)
async def form_conf(message: Message, state: FSMContext):
    if message.text == "Соглашаюсь, продолжить":
        await state.update_data(conf="yes")
        await state.set_state(Form.adds_agreement)
        await message.answer("Я хочу получать по указанным каналам связи рекламную и справочную информацию от Университета Иннополис об образовательных программах, достижениях, проектах и иных новостях",
                             reply_markup=agree_adds_kb)
    else:
        await message.answer("Нажимая кнопку \"завершить регистрацию\", вы соглашаетесь с политикой обработки персональных данных",
                             reply_markup= agree_conf_kb)


@router.message(Form.adds_agreement)
async def form_interests(message: Message, state: FSMContext):
    if message.text == "Соглашаюсь, продолжить":
        await state.update_data(adds="yes")
        data_dict = await state.get_data()
        await state.clear()
        data = list(data_dict.values())
        await edit_profile(data, message.from_user.id)
        await message.answer("Спасибо, анкета заполнена! Нажмите /menu, чтобы перейти в меню")
    elif message.text == "Не соглашаюсь":
        await state.update_data(adds="no")
        data_dict = await state.get_data()
        await state.clear()
        data = list(data_dict.values())
        await edit_profile(data, message.from_user.id)
        await message.answer("Спасибо, анкета заполнена! Нажмите /menu, чтобы перейти в меню")
    else:
        await message.answer(
            "Нажимая кнопку \"завершить регистрацию\", вы соглашаетесь с политикой обработки персональных данных",
            reply_markup=agree_conf_kb)


@router.message(Form.wait)
async def wait(message: Message):
    await message.answer(f"Не понимаю :( Перед тем, как начать, вам нужно заполнить небольшую анкету "
                         f"из трех вопросов: имя, фамилия и адрес электронной почты. Нажмите /form, чтобы начать")

