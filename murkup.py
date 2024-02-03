from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

to_menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Открыть меню")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="онлайн-курс")],
        [KeyboardButton(text="об олимпиадах")],
        [KeyboardButton(text="квест")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

link_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Перейти на сайт", url = "https://dovuz.innopolis.university")]
    ]
)

olymp_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="ВсОШ")],
        [KeyboardButton(text="РсОШ")],
        [KeyboardButton(text="InnopolisOpen")],
        [KeyboardButton(text="Открыть меню")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

course_info_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Как подготовиться?")],
        [KeyboardButton(text="обратно к олимпиадам")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

tests_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="программирование")],
        [KeyboardButton(text="олимпиадное программирование")],
        [KeyboardButton(text="информационная безопасность")],
        [KeyboardButton(text="Открыть меню")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)