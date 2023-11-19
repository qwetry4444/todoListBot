from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram import Router, types
from src import text
from src.bot.keyboards.keyboards import functions_keyboard

start_router = Router(name="start")


@start_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(text.start_message(message.from_user.full_name), reply_markup=functions_keyboard)

