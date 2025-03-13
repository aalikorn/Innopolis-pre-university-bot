from aiogram.fsm.state import StatesGroup, State


class Form(StatesGroup):
    name = State()
    surname = State()
    email = State()
    wait = State()


class Menu(StatesGroup):
    menu = State()
    olymp = State()
    quiz = State()


class QuizMenu(StatesGroup):
    level = State()
    start_quiz = State()
    to_quiz = State()
    game = State()
    finish = State()
    try_again = State()
    current_game = State()
    gift = State()










