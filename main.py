import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage

from handlers import form, menu, quiz_menu, start
from config_reaader import config
from antiflood import AntiFloodMiddleware
from game import handle_answer, start_quiz, finish_quiz
from aiogram.fsm.storage.redis import RedisStorage



async def main():
    bot = Bot(config.bot_token.get_secret_value())
    storage = RedisStorage.from_url("redis://localhost:6379/0")
    dp = Dispatcher(storage=storage)
    dp.message.middleware(AntiFloodMiddleware())
    dp.include_routers(
        form.router,
        menu.router,
        quiz_menu.router,
        start.router,
        start_quiz.router,
        handle_answer.router,
        finish_quiz.router
    )
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())


