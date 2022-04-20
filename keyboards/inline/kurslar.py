from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def KURSLAR_BUTTON(result, page=0):
    KB = []
    for i in result:
        KB.append(InlineKeyboardButton(
            text=i["title"], callback_data=i["link"].split("/")[-2]))
    KB = [list(result[i:i+10]) for i in range(len(result))[::10]]
    return InlineKeyboardMarkup(
        inline_keyboard=[
            KB[page]
        ], row_width=2
    )
