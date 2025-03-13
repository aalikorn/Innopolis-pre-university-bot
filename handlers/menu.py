from aiogram import Router
from aiogram.enums import ParseMode
from aiogram.types import Message
import markup
from aiogram.filters import Command
from states import Menu
from aiogram.fsm.context import FSMContext
import messages

router = Router()


@router.message(Command("menu"))
async def menu(message: Message,  state: FSMContext):
    await state.set_state(Menu.menu)
    await message.answer(text=messages.menuMessage,
                         reply_markup=markup.menu_kb,
                         parse_mode=ParseMode.HTML)


@router.message(Menu.menu)
async def menu_actions(message: Message,  state: FSMContext):
    # if message.text == "Об олимпиадах":
    #     await message.answer_video(video='BAACAgIAAxkBAAMjZc_Z5WlS7Yqjjh50XZCFfKtQrkAAAjE3AAJNroFK92i6udsaMSA0BA',
    #                                caption='Посмотри видео-описание бесплатного модуля для школьников «Олимпиады для поступления в ИТ-вуз»',
    #                                reply_markup=markup.free_kb)
    #     await message.answer("Меню: ",
    #                          reply_markup=markup.menu_kb,
    #                          parse_mode=ParseMode.HTML)
    if message.text == "О подготовке к обучению в ИТ-вузах":
        await message.answer_video(video='BAACAgIAAxkBAAIbwGfSlZp5AAHI2xHzVRIpdjJ2_bSZfAAC82IAAp8akUoAAbO-0WotIHU2BA',
                                   caption='Посмотри видео-описание курса для школьников «Подготовка к обучению в ИТ-вузах»',
                                   reply_markup=markup.course_kb)
        await message.answer("Меню: ",
                             reply_markup=markup.menu_kb,
                             parse_mode=ParseMode.HTML)
    elif message.text == "О поступлении в Университет Иннополис":
        await message.answer_video(video='BAACAgIAAxkBAAMkZc_aJxPfEIOZt2rF-7iy949aWUYAAjU3AAJNroFKN58-IQ4MA_s0BA',
                                   reply_markup=markup.ituni_kb_new)
        await message.answer("Меню: ",
                             reply_markup=markup.menu_kb,
                             parse_mode=ParseMode.HTML)
    elif message.text == "О поступлении в колледж Университета Иннополис":
        await message.answer_photo(caption="Приглашаем выпускников 9 класса в колледж Университета Иннополис на направления: «Мехатроника и робототехника» и «Информационные системы и программирование».",
                                   photo='AgACAgIAAxkBAAIbtGfSk40_0RHh0ur03LFZSPaN36edAAIa7TEbnxqRSiXiVLzT5sfCAQADAgADbQADNgQ',
                                   reply_markup=markup.college_kb)
        await message.answer("Меню: ",
                             reply_markup=markup.menu_kb,
                             parse_mode=ParseMode.HTML)
    elif message.text == "Пройти квиз":
        await state.set_state(Menu.quiz)
        await message.answer("Выберите направление", reply_markup=markup.tests_kb)
    elif message.text == "Контакты":
        await message.answer("Наши контакты:", reply_markup=markup.link_kb)
        await message.answer("Меню: ",
                             reply_markup=markup.menu_kb,
                             parse_mode=ParseMode.HTML)
    elif message.text in ("/start", "/menu"):
        await message.answer(
            text=messages.menuMessage,
            reply_markup=markup.menu_kb,
            parse_mode=ParseMode.HTML)
    else:
        await message.answer(text="Я вас не понимаю :(\n\n" + messages.menuMessage,reply_markup=markup.menu_kb,
                         parse_mode=ParseMode.HTML)