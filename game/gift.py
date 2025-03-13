import random
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from markup import gift_kb, menu_kb
from aiogram import Router
from states import QuizMenu, Menu
from messages import menuMessage


router = Router()


async def suggest_gift(message: Message, state:FSMContext):
    await state.set_state(QuizMenu.gift)
    await message.answer("Благодарим за участие! Жмите «Получить подарок» - и вам рандомно выпадает один из призов! (только если вы находитесь на выставке)",
                   reply_markup=gift_kb)


@router.message(QuizMenu.gift)
async def give_gift(message: Message, state: FSMContext):
    print(1)
    if message.text == "Получить подарок":
        gifts = ["Браслет", "Блокнот", "Стикерпак", "Свитшот", "Футболка"]
        gift = gifts[random.randint(0, len(gifts) - 1)]
        await message.answer(f"Ваш подарок: {gift}! Если вы сейчас находитесь на выставке, подойдите, пожалуйста, к организаторам и получите приз.")
        await state.set_state(Menu.menu)
        await message.answer(menuMessage, reply_markup=menu_kb)
    elif message.text == "Вернуться в меню":
        await state.set_state(Menu.menu)
        await message.answer(menuMessage, reply_markup=menu_kb)
    else:
        await message.answer("Я не понимаю :( Жмите «Получить подарок» - и вам рандомно выпадает один из призов! (только если вы находитесь на выставке)", reply_markup=gift_kb)