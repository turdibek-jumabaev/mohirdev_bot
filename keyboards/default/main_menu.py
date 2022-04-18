from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

MAIN_MENU = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Kurslar"),
            KeyboardButton(text="Practicum"),
            KeyboardButton(text="Maqolalar"),
        ],
        [
            KeyboardButton(text="Ustozlar"),
        ],
    ],
    resize_keyboard=True,
)
