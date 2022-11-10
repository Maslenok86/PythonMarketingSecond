from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

sexKeyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Женский'),
            KeyboardButton(text='Мужской')
        ]

    ],
    resize_keyboard=True
)

ageKeyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Меньше 18 лет'),
            KeyboardButton(text='От 18 до 32 лет'),
            KeyboardButton(text='От 33 до 49 лет'),
            KeyboardButton(text='Старше 50 лет'),
        ]

    ],
    resize_keyboard=True
)

websiteKeyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Пользуюсь посткроссинг-сайтами'),
            KeyboardButton(text='Не пользуюсь посткроссинг-сайтами')
        ]

    ],
    resize_keyboard=True
)

sendingKeyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Раз в год'),
            KeyboardButton(text='Раз в три месяца'),
            KeyboardButton(text='Раз в месяц'),

        ],
        [
            KeyboardButton(text='Раз в неделю'),
            KeyboardButton(text='3 раза в неделю'),
            KeyboardButton(text='Каждый день'),
        ]

    ],
    resize_keyboard=True
)
envelopeKeyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Пользуюсь конвертами'),
            KeyboardButton(text='Не использую конврты')
        ]

    ],
    resize_keyboard=True
)
decorKeyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='В технике скрапбукинг'),
            KeyboardButton(text='Простое оформление в одном стиле'),
        ],
        [
            KeyboardButton(text='Оформление из подручных средств'),
            KeyboardButton(text='Не оформляю открытку'),
        ]

    ],
    resize_keyboard=True
)
abroadKeyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Оправляю за границу'),
            KeyboardButton(text='Оправляю в пределах России')
        ]

    ],
    resize_keyboard=True
)
