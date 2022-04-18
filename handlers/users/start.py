from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from data.matnlar import start
from keyboards.default.main_menu import MAIN_MENU


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(start(message.from_user.full_name), reply_markup=MAIN_MENU)
