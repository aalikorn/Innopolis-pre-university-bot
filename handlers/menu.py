from aiogram import Router
from aiogram.enums import ParseMode
from aiogram.types import Message
import markup
from aiogram.filters import Command
from states import Menu
from aiogram.fsm.context import FSMContext

router = Router()


@router.message(Command("menu"))
async def menu(message: Message,  state: FSMContext):
    await state.set_state(Menu.menu)
    await message.answer(f"Меню:\n\n<b>Об олимпиадах:</b> видео о модуле для детей \"Олимпиады для поступления в ИТ-вузы\". Посмотрите и запишитесь на бесплатное обучение!\n\n<b>О поступлении в Университет Иннополис:</b> узнайте условия поступления в наш университет в 2024 году и запишитесь на модуль \"Подготовка к поступлению в ИТ-вузы\" бесплатно!\n\n<b>Пройти квиз:</b> выберите любое направление и попробуйте свои силы на разных уровнях квиза",
                         reply_markup=markup.menu_kb,
                         parse_mode=ParseMode.HTML)


@router.message(Menu.menu)
async def menu_actions(message: Message,  state: FSMContext):
    if message.text == "Об олимпиадах":
        await message.answer_video(video='BAACAgIAAxkBAAMjZc_Z5WlS7Yqjjh50XZCFfKtQrkAAAjE3AAJNroFK92i6udsaMSA0BA',
                                   caption='Посмотри видео-описание бесплатного модуля для школьников «Олимпиады для поступления в ИТ-вуз»',
                                   reply_markup=markup.free_kb)
        await message.answer("Меню:\n\n<b>Об олимпиадах:</b> видео о модуле для детей \"Олимпиады для поступления в ИТ-вузы\". Посмотрите и запишитесь на бесплатное обучение!\n\n<b>О поступлении в Университет Иннополис:</b> узнайте условия поступления в наш университет в 2024 году и запишитесь на модуль \"Подготовка к поступлению в ИТ-вузы\" бесплатно!\n\n<b>Пройти квиз:</b> выберите любое направление и попробуйте свои силы на разных уровнях квиза",
                             reply_markup=markup.menu_kb,
                             parse_mode=ParseMode.HTML)
    elif message.text == "О поступлении в Университет Иннополис":
        await message.answer_video(video='BAACAgIAAxkBAAMkZc_aJxPfEIOZt2rF-7iy949aWUYAAjU3AAJNroFKN58-IQ4MA_s0BA',
                                   caption="Узнайте условия поступления в Университет Иннополис в 2024 году",
                                   reply_markup=markup.ituni_kb)
        await message.answer("Меню:\n\n<b>Об олимпиадах:</b> видео о модуле для детей \"Олимпиады для поступления в ИТ-вузы\". Посмотрите и запишитесь на бесплатное обучение!\n\n<b>О поступлении в Университет Иннополис:</b> узнайте условия поступления в наш университет в 2024 году и запишитесь на модуль \"Подготовка к поступлению в ИТ-вузы\" бесплатно!\n\n<b>Пройти квиз:</b> выберите любое направление и попробуйте свои силы на разных уровнях квиза",
                             reply_markup=markup.menu_kb,
                             parse_mode=ParseMode.HTML)
    elif message.text == "Пройти квиз":
        await state.set_state(Menu.quiz)
        await message.answer("Выберите направление", reply_markup=markup.tests_kb)
    elif message.text == "Контакты":
        await message.answer("Наши контакты:", reply_markup=markup.link_kb)
        await message.answer("Меню:\n\n<b>Об олимпиадах:</b> видео о модуле для детей \"Олимпиады для поступления в ИТ-вузы\". Посмотрите и запишитесь на бесплатное обучение!\n\n<b>О поступлении в Университет Иннополис:</b> узнайте условия поступления в наш университет в 2024 году и запишитесь на модуль \"Подготовка к поступлению в ИТ-вузы\" бесплатно!\n\n<b>Пройти квиз:</b> выберите любое направление и попробуйте свои силы на разных уровнях квиза",
                             reply_markup=markup.menu_kb,
                             parse_mode=ParseMode.HTML)
    else:
        await message.answer(f"Я вас не понимаю :( Меню:\n\n<b>Об олимпиадах:</b> видео о модуле для детей \"Олимпиады для поступления в ИТ-вузы\". Посмотрите и запишитесь на бесплатное обучение!\n\n<b>О поступлении в Университет Иннополис:</b> узнайте условия поступления в наш университет в 2024 году и запишитесь на модуль \"Подготовка к поступлению в ИТ-вузы\" бесплатно!\n\n<b>Пройти квиз:</b> выберите любое направление и попробуйте свои силы на разных уровнях квиза",
                         reply_markup=markup.menu_kb,
                         parse_mode=ParseMode.HTML)