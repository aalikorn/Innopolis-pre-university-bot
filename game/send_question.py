from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


async def send_question(message, current_game):
    question = current_game.questions[current_game.current_question]

    if len(question.get("O")) == 0:
        options = ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text='завершить квиз')]],
            resize_keyboard=True,
            one_time_keyboard=True,
        )
        if question.get("I") == "":
            await message.answer(question.get("Q"), reply_markup=options)
        else:
            await message.answer_photo(photo=question.get("I"), caption=question.get("Q"), reply_markup=options)
    else:
        options = ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text=option)] for option in question.get("O")] + [[KeyboardButton(text='завершить квиз')]],
            resize_keyboard=True,
            one_time_keyboard=True,
        )
        if question.get("I") == "":
            await message.answer(question.get("Q"), reply_markup=options)
        else:
            await message.answer_photo(photo=question.get("I"), caption=question.get("Q"), reply_markup=options)











