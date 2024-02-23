from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from markup import try_again_kb, lending_kb, tg_kb, what_kb, tests_kb, menu_kb, start_quiz_kb
from aiogram import Router
from states import Menu, QuizMenu

router = Router()


async def finish_quiz(message, current_game, state: FSMContext):
    points = current_game.points

    if current_game.topic == "programming1":
        if points <= 4:
            await message.answer(f"Ваш результат: {points}/{current_game.max_points}. Может попробуете снова?", reply_markup=try_again_kb)
            await state.set_state(QuizMenu.try_again)
        elif points <= 8:
            await message.answer(
                f"Ваш результат: {points}/{current_game.max_points}. Поздравляем, вы хорошо осведомлены! Рекомендуем записаться на курсы по олимпиадной подготовке на одной из летних смен в Университете Иннополис, пройти контест и получить рекомендацию на уровень сложности.",
                reply_markup=lending_kb)
            await message.answer("Теперь можете попробовать следующий уровень, выбрав его в меню", reply_markup=what_kb)
        else:
            await message.answer(
                f"Ваш результат: {points}/{current_game.max_points}. Поздравляем, вы отлично осведомлены! Рекомендуем записаться на курсы по олимпиадной подготовке на одной из летних смен в Университете Иннополис, пройти контест и получить рекомендацию на уровень сложности.",
                reply_markup=lending_kb)
            await message.answer("Теперь можете попробовать следующий уровень, выбрав его в меню", reply_markup=what_kb)

    elif current_game.topic == "programming2":
        if points <= 7:
            await message.answer(
                f"Ваш результат: {points}/{current_game.max_points}. Для изучения основ языка программирования Python приглашаем вас на летнюю смену в Университет Иннополис",
                reply_markup=lending_kb
            )
            await message.answer("Хотите вернуться в меню, или попробовать другой квиз?", reply_markup=what_kb)

        else:
            await message.answer(
                f"Ваш результат: {points}/{current_game.max_points}. Поздравляем! Вы показали отличные результаты! Для углубления знаний приглашаем на наши летние смены по программированию на Python.",
                reply_markup=lending_kb
            )
            await message.answer("Хотите вернуться в меню, или попробовать другой квиз?", reply_markup=what_kb)

    elif current_game.topic == "olymp_programming1":
        if points <= 3:
            await message.answer(
                f"Ваш результат: {points}/{current_game.max_points}. Рекомендуем записаться на курсы по олимпиадной подготовке на одной из летних смен в Университете Иннополис, пройти контест и получить рекомендацию на уровень сложности.",
                reply_markup=lending_kb
            )
            await message.answer("Хотите вернуться в меню, или попробовать другой квиз?", reply_markup=what_kb)
        else:
            await message.answer(
                f"Ваш результат: {points}/{current_game.max_points}. Отлично! Рекомендуем записаться на курсы по олимпиадной подготовке на одной из летних смен в Университете Иннополис, пройти контест и получить рекомендацию на уровень сложности.",
                reply_markup=lending_kb
            )
            await message.answer("Теперь можете попробовать следующий уровень, выбрав его в меню", reply_markup=what_kb)

    elif current_game.topic == "olymp_programming2":
        await message.answer(
            f"Ваш результат: {points}/{current_game.max_points}. Рекомендуем записаться на курсы по олимпиадной подготовке на одной из летних смен в Университете Иннополис, пройти контест и получить рекомендацию на уровень сложности.",
            reply_markup=lending_kb
        )
        await message.answer("Хотите вернуться в меню, или попробовать другой квиз?", reply_markup=what_kb)

    elif current_game.topic == "inf_bez":
        await message.answer(f"Ваш результат: {points}/{current_game.max_points}. Спасибо за участие! Следите за новостями в Телеграм-канале Довуза Университета Иннополис", reply_markup=tg_kb)
        await message.answer("Хотите вернуться в меню, или попробовать другой квиз?", reply_markup=what_kb)


@router.message(QuizMenu.finish)
async def what(message: Message, state: FSMContext):
    if message.text == "Пройти еще один квиз":
        await message.answer("Выберите квиз", reply_markup=tests_kb)
        await state.set_state(Menu.quiz)
    elif message.text == "Открыть меню":
        await message.answer("Меню:\n\nОб олимпиадах: видео о модуле для детей \"Олимпиады для поступления в ИТ-вузы\". Посмотрите и запишитесь на бесплатное обучение!\n\nО поступлении в Университет Иннополис: узнайте условия поступления в наш университет в 2024 году и запишитесь на модуль \"Подготовка к поступлению в ИТ-вузы\" бесплатно!\nПройти квиз: выберите любое направление и попробуйте свои силы на разных уровнях квиза", reply_markup=menu_kb)
        await state.set_state(Menu.menu)


@router.message(QuizMenu.try_again)
async def try_again(message: Message, state: FSMContext):
    if message.text == "Попробовать снова":
        await message.answer("Нажмите 'начать', чтобы начать квиз снова", reply_markup=start_quiz_kb)
        await state.set_state(QuizMenu.start_quiz)
    elif message.text == "Нет :( Получить рекомендации и вернуться в меню":
        await message.answer(
            f"Рекомендуем записаться на курсы начального уровня по программированию на одной из летних смен в Университете Иннополис",
            reply_markup=lending_kb)
        await message.answer("Хотите вернуться в меню, или попробовать другой квиз?", reply_markup=what_kb)
        await state.set_state(QuizMenu.finish)
    elif message.text == "Выбрать другой квиз":
        await message.answer("Выберите квиз", reply_markup=tests_kb)
        await state.set_state(Menu.quiz)

