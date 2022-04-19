from loader import dp, bot
from states.main_state import MainMenuState
from keyboards.default.ustozlar_btn import USTOZLAR_BUTTON, USTOZLAR_BUTTON_2, USTOZLAR_BUTTON_3
from data.matnlar import ustozlar

from aiogram import types


@dp.message_handler(state=MainMenuState.ustozlar)
async def echo(message: types.Message):
    if message.text == 'Anvar Narzullaev':
        await message.answer('Anvar Narzullaev')

    elif message.text == 'Ahmadjon Xashimov':
        await message.answer('Ahmadjon Xashimov')

    elif message.text == 'Farhod Dadajonov':
        await message.answer('Farhod Dadajonov')

    elif message.text == 'Qudrat Abdurahimov':
        await message.answer('Qudrat Abdurahimov')

    elif message.text == 'Muhammadjavohirbek Sur\'atov':
        await message.answer('Muhammadjavohirbek Sur\'atov')

    elif message.text == 'Samar Badriddinov':
        await message.answer('Samar Badriddinov')

    elif message.text == 'Muhammadrasul':
        await message.answer('Muhammadrasul')

    elif message.text == 'Ulugbek Samigjonov':
        await message.answer('Ulugbek Samigjonov')

    elif message.text == 'Zayniddin Mamarasulov':
        await message.answer('Zayniddin Mamarasulov')

    elif message.text == 'Zohidjon Akbarov':
        await message.answer('Zohidjon Akbarov')

    elif message.text == 'Bexruz Xolmuminov':
        await message.answer('Bexruz Xolmuminov')

    elif message.text == 'Mansurbek Abdullaev':
        await message.answer('Mansurbek Abdullaev')

    # next page & back page
    elif message.text == 'Keyingisi':
        await message.answer(text=ustozlar(), reply_markup=USTOZLAR_BUTTON_2)
        await message.delete()
        await bot.delete_message(message.chat.id, int(message.message_id-1))

    elif message.text == 'Oldingisi':
        await message.answer(text=ustozlar(), reply_markup=USTOZLAR_BUTTON)
        await message.delete()
        await bot.delete_message(message.chat.id, int(message.message_id-1))

    elif message.text == 'Оldingisi':
        await message.answer(text=ustozlar(), reply_markup=USTOZLAR_BUTTON_2)
        await message.delete()
        await bot.delete_message(message.chat.id, int(message.message_id-1))

    elif message.text == 'Kеyingisi':
        await message.answer(text=ustozlar(), reply_markup=USTOZLAR_BUTTON_3)
        await message.delete()
        await bot.delete_message(message.chat.id, int(message.message_id-1))

    else:
        await message.delete()
