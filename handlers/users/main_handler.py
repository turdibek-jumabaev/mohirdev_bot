from loader import dp
from states.main_state import MainMenuState

from aiogram import types


@dp.message_handler(content_types=types.ContentType.TEXT)
async def echo(message: types.Message):
    if message.text == 'Kurslar':
        await message.answer('Kurslar')

    elif message.text == 'Practicum':
        await message.answer('Practicum')

    elif message.text == 'Maqolalar':
        await message.answer('Maqolalar')

    elif message.text == 'Ustozlar':
        await message.answer('Ustozlar')

    else:
        await message.answer('Bunday bo\'lim mavjud emas')
