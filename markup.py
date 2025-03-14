from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


agree_conf_kb = ReplyKeyboardMarkup(
    keyboard=[
            [KeyboardButton(text="Соглашаюсь, продолжить")]
        ],
        resize_keyboard=True,
        one_time_keyboard=True,
)

agree_adds_kb = ReplyKeyboardMarkup(
    keyboard=[
            [KeyboardButton(text="Соглашаюсь, продолжить")],
            [KeyboardButton(text="Не соглашаюсь")]
        ],
        resize_keyboard=True,
        one_time_keyboard=True,
)

gift_kb = ReplyKeyboardMarkup(
    keyboard=[
            [KeyboardButton(text="Получить подарок")],
            [KeyboardButton(text="Вернуться в меню")]
        ],
        resize_keyboard=True,
        one_time_keyboard=True,
)

to_menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Меню")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="О подготовке к обучению в ИТ-вузах")],
        [KeyboardButton(text="О поступлении в Университет Иннополис")],
        [KeyboardButton(text="О поступлении в колледж Иннополис")],
        [KeyboardButton(text="Пройти квиз")],
        [KeyboardButton(text="Контакты")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

link_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Телеграм-канал Довуза", url="https://t.me/dovuziu ")],
        [InlineKeyboardButton(text="Сайт Довуза", url="https://dovuz.innopolis.university/")],
        [InlineKeyboardButton(text="Информация о летних курсах 2025", url="https://dovuz.innopolis.university/offline-programms")],
        [InlineKeyboardButton(text="Сайт Колледжа Иннополис", url="https://innopolis.college/?utm_source=telegram&utm_medium=tgbot&utm_campaign=innopolis.college&utm_content=innokotuserbot")],
        [InlineKeyboardButton(text="Телеграм-канал Колледжа Иннополис", url="https://t.me/+2z9RJrr9tVlhNWUy")],
    ]
)

free_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Узнать больше об олимпиадах", url="https://learn.innopolis.university/invite/3JH9N")],
    ]
)

ituni_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Подготовка к поступлению в Ит-вузы", url="https://learn.innopolis.university/invite/XVYPS")],
    ]
)

ituni_kb_new = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Узнать подробнее", url="https://apply.innopolis.university/")],
    ]
)

college_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Узнать подробнее", url="https://innopolis.college/?utm_source=telegram&utm_medium=tgbot&utm_campaign=innopolis.college&utm_content=innokotuserbot")],
    ]
)

course_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Узнать о курсах", url="https://dovuz.innopolis.university/preparation")],
    ]
)

lending_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Узнать подробнее", url="https://dovuz.innopolis.university/offline-programms")],
    ]
)

tg_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Перейти в Телеграм-канал", url="https://t.me/dovuziu")],
        [InlineKeyboardButton(text="Перейти на сайт", url="https://dovuz.innopolis.university/")],
        [InlineKeyboardButton(text="Узнать больше о программах обучения", url="https://dovuz.innopolis.university/offline-programms")]
    ]
)

tests_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Программирование на Python")],
        [KeyboardButton(text="Олимпиадное программирование")],
        [KeyboardButton(text="Информационная безопасность")],
        [KeyboardButton(text="Открыть меню")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

levels_kb = ReplyKeyboardMarkup(
    keyboard=[
            [KeyboardButton(text="1")],
            [KeyboardButton(text="2")]
        ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

start_quiz_kb = ReplyKeyboardMarkup(
    keyboard=[
            [KeyboardButton(text="Начать")],
            [KeyboardButton(text="Выбрать другой квиз")]
        ],
    resize_keyboard=True,
    one_time_keyboard=True,
)


try_again_kb = ReplyKeyboardMarkup(
    keyboard=[
            [KeyboardButton(text="Попробовать снова")],
            [KeyboardButton(text="Нет :( Получить рекомендации и вернуться в меню")],
            [KeyboardButton(text="Выбрать другой квиз")]
        ],
    resize_keyboard=True,
    one_time_keyboard=True,
)


try_more_kb = ReplyKeyboardMarkup(
    keyboard=[
            [KeyboardButton(text="Попробовать")],
            [KeyboardButton(text="Открыть меню")]
        ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

what_kb = ReplyKeyboardMarkup(
    keyboard=[
            [KeyboardButton(text="Пройти еще один квиз")],
            [KeyboardButton(text="Открыть меню")]
        ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
