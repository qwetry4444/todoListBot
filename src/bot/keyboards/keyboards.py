from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import types
from aiogram.utils.keyboard import (
ReplyKeyboardMarkup, ReplyKeyboardBuilder, InlineKeyboardBuilder, InlineKeyboardMarkup, KeyboardButton,
InlineKeyboardButton
)



# start_keyboard = ReplyKeyboardMarkup(
#     keyboard=[[KeyboardButton(text="Функции"), KeyboardButton(text="О нас")]],
#     resize_keyboard=True
# )

functions_keyboard = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Добавить"), KeyboardButton(text="Отметить"), KeyboardButton(text="Удалить")],
              [KeyboardButton(text="Список задач")]],
    resize_keyboard=True
)