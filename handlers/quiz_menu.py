from aiogram import Router
from aiogram.types import Message
from states import Menu, QuizMenu
from aiogram.fsm.context import FSMContext
from markup import tests_kb, menu_kb, levels_kb, start_quiz_kb
from aiogram.enums import ParseMode
import messages

router = Router()


@router.message(Menu.quiz)
async def quiz_choice(message: Message, state: FSMContext):
    if message.text == "Программирование на Python":
        await state.update_data(topic="programming")
        await message.answer("Выберите уровень:\n\n1) Легче\n2) Сложнее", reply_markup=levels_kb)
        await state.set_state(QuizMenu.level)
    elif message.text == "Олимпиадное программирование":
        await state.update_data(topic="olymp_programming")
        await message.answer("Выберите уровень:\n\n1) Легче\n2) Сложнее", reply_markup=levels_kb)
        await state.set_state(QuizMenu.level)
    elif message.text == "Информационная безопасность":
        await state.update_data(topic="inf_bez")
        await state.update_data(max_points="12")
        await state.set_state(QuizMenu.start_quiz)
        await message.answer("Квиз состоит из 12 вопросов, после прохождения вы сможете узнать свой результат. Нажмите 'начать', чтобы начать квиз", reply_markup=start_quiz_kb)
    elif message.text == "Открыть меню":
        await state.set_state(Menu.menu)
        await message.answer(text=messages.menuMessage,
                             reply_markup=menu_kb,
                             parse_mode=ParseMode.HTML)
    elif message.text == "Для колледжа: ИТ или Робототехника":
        await state.update_data(topic="college")
        await message.answer("Тест поможет вам определиться какаой путь выбрать: ИТ или Робототехника. Тест состоит из 6 вопросов.  Нажмите 'начать', чтобы начать тест.", reply_markup=start_quiz_kb)
        await state.set_state(QuizMenu.start_quiz)
    else:
        await message.answer("Я вас не понимаю :( Какой квиз вы хотели бы пройти?", reply_markup=tests_kb)


@router.message(QuizMenu.level)
async def level_choice(message: Message, state: FSMContext):
    if message.text.lower() in ("легче", "сложнее"):
        data_dict = await state.get_data()
        topic = data_dict.get("topic")
        await state.set_state(QuizMenu.to_quiz)
        if message.text.lower() == "легче":
            topic = topic + "1"
        else:
            topic = topic + "2"
        await state.update_data(topic=topic)
        n = 0
        if topic == "programming1":
            n = 10
        elif topic == "programming2":
            n = 10
        elif topic == "olymp_programming1":
            n = 5
        elif topic == "olymp_programming2":
            n = 13
        await state.update_data(max_points=str(n))
        await message.answer(f"Квиз состоит из {n} вопросов, после прохождения вы сможете узнать свой результат. Нажмите 'начать', чтобы начать квиз", reply_markup=start_quiz_kb)
        await state.set_state(QuizMenu.start_quiz)
    elif message.text.lower() == "назад":
        await state.update_data(topic="")
        await state.set_state(Menu.quiz)
        await message.answer("Выберите направление", reply_markup=tests_kb)
    elif message.text.lower() == "открыть меню":
        await message.answer(
            text = messages.menuMessage,
            reply_markup=menu_kb,
            parse_mode=ParseMode.HTML)
        await state.set_state(Menu.menu)
    else:
        await message.answer("Я вас не понимаю :( Выберите уровень:\n\n1) Общий уровень\n2) Уровень D",
                             reply_markup=levels_kb)


