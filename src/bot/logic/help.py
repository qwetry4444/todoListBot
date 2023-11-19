from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram import Router, types
from src import text
from src.bot.keyboards.keyboards import functions_keyboard

help_router = Router(name="help")

@help_router.message(Command(commands="help"))
async def echo_handler(message: types.Message) -> None:
    await message.answer(text.help_message, reply_markup=functions_keyboard)
