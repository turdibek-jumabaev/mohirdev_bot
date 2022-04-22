from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def keyboard(result, start, end):
    KB = []
    for i in range(start, end):
        KB.append(InlineKeyboardButton(
            text=f"{result[i]['title']}", callback_data=result[i]['link'].split("/")[-2]))
    return KB


def KEYBOARD(result, a, b):
    return InlineKeyboardMarkup(
        row_width=2,
        inline_keyboard=keyboard(result=result, start=a, end=b)
    )
