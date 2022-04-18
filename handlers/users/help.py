from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp
from data.matnlar import help


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    await message.answer(help())
