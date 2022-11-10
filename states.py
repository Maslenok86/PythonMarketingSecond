from aiogram.dispatcher.filters.state import StatesGroup, State

class States(StatesGroup):
    questionSex = State()
    questionAge = State()
    questionWebsite = State()
    questionSending = State()
    questionEnvelope = State()
    questionDecor = State()
    questionAbroad = State()
    questionEnding = State()
