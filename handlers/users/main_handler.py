from loader import dp
from data.matnlar import ustozlar, kurslar
from states.main_state import MainMenuState
from keyboards.default.ustozlar_btn import USTOZLAR_BUTTON
from keyboards.inline.kurslar import KURSLAR_BUTTON
from utils.db_api.mohirdev import get_data

from aiogram import types


@dp.message_handler(content_types=types.ContentType.TEXT)
async def echo(message: types.Message):
    if message.text == 'Kurslar':
        data = await get_data()
        await message.answer(kurslar(), reply_markup=KURSLAR_BUTTON(result=data))

    elif message.text == 'Practicum':
        await message.answer('Practicum')

    elif message.text == 'Maqolalar':
        await message.answer('Maqolalar')

    elif message.text == 'Ustozlar':
        await message.answer(text=ustozlar(), reply_markup=USTOZLAR_BUTTON)
        await MainMenuState.ustozlar.set()

    else:
        await message.answer('Bunday bo\'lim mavjud emas')
