from aiogram.dispatcher.filters.state import State, StatesGroup


class MainMenuState(StatesGroup):
    kurslar = State()
    practicum = State()
    maqolalar = State()
    ustozlar = State()
