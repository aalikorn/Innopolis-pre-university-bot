from aiogram import Router
from aiogram.types import Message
from states import Menu, QuizMenu
from aiogram.fsm.context import FSMContext
from game.send_question import send_question
from game.finish_quiz import finish_quiz
from game.variables import Variables


router = Router()


@router.message(QuizMenu.game)
async def handle_answer(message: Message, state: FSMContext):
    data_dict = await state.get_data()
    current_game = Variables.from_dict(data_dict.get("current_game"))
    if message.text.lower() == 'завершить квиз':
        current_game.current_question = len(current_game.questions)
    else:
        question = current_game.questions[current_game.current_question]
        if data_dict.get("topic") != "college":
            if message.text.lower() in question.get("A"):
                current_game.points += 1
        else:
            if question.get("map").get(message.text) == "ИТ":
                await state.update_data(it=data_dict.get("it") + 1)
            elif question.get("map").get(message.text) == "Р":
                await state.update_data(r=data_dict.get("r") + 1)
            elif question.get("map").get(message.text) == "О":
                await state.update_data(o=data_dict.get("o") + 1)
            else:
                await state.update_data(o=data_dict.get("o") + 1)
        current_game.current_question += 1
    if current_game.current_question == len(current_game.questions):
        await state.set_state(QuizMenu.finish)
        await finish_quiz(message, current_game, state)
    else:
        await send_question(message, current_game)
    await state.update_data(current_game=current_game.to_dict())







