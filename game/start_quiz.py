from aiogram import Router
from aiogram.types import Message
from states import Menu, QuizMenu
from aiogram.fsm.context import FSMContext
from markup import tests_kb, menu_kb, start_quiz_kb
from quizes import inf_bez, olymp_programming2, olymp_programming1, programming1, programming2
from game.send_question import send_question
from game.variables import Variables
import messages

router = Router()


@router.message(QuizMenu.start_quiz)
async def quiz(message: Message, state: FSMContext):
    if message.text == "Выбрать другой квиз":
        await state.set_state(Menu.quiz)
        await message.answer("Выберите направление", reply_markup=tests_kb)
    elif message.text.lower() == "открыть меню":
        await message.answer(
            text=messages.menuMessage,
            reply_markup=menu_kb,
            parse_mode="html")
        await state.set_state(Menu.menu)
    elif message.text != "Начать":
        await message.answer("Я Вас не понимаю :( Нажмите 'начать', чтобы начать квиз", reply_markup=start_quiz_kb)
    else:
        current_game = Variables()
        await state.set_state(QuizMenu.game)
        data_dict = await state.get_data()
        topic = data_dict.get("topic")
        max_points = data_dict.get("max_points")
        current_game.topic = topic
        current_game.points = 0
        current_game.current_question = 0
        current_game.max_points = max_points

        if topic == "programming1":
            current_game.questions = programming1.questions
        elif topic == "programming2":
            current_game.questions = programming2.questions
        elif topic == "olymp_programming1":
            current_game.questions = olymp_programming1.questions
        elif topic == "olymp_programming2":
            current_game.questions = olymp_programming2.questions
        elif topic == "inf_bez":
            current_game.questions = inf_bez.questions
        await state.update_data(current_game=current_game.to_dict())
        await send_question(message, current_game)
