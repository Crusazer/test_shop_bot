from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButtonPollType, ReplyKeyboardMarkup, KeyboardButton


def main_keyboard() -> ReplyKeyboardMarkup:
    """
    Create a main keyboard
    :return: объект reply-клавиатуры
    """
    keyboard = ReplyKeyboardBuilder()

    keyboard.button(text="Показать все товары")
    keyboard.button(text="Показать следующую страницу")
    keyboard.button(text="Поддержка")

    return keyboard.as_markup(resize_keyboard=True, one_time_keyboard=True)


def make_row_keyboard(items: list[str]) -> ReplyKeyboardMarkup:
    """
        Create a keyboard with buttons in one row
        :param items: text buttons
        :return: object of reply-keyboard
    """
    row = [KeyboardButton(text=item) for item in items]
    return ReplyKeyboardMarkup(keyboard=[row], resize_keyboard=True)


def admin_keyboard() -> ReplyKeyboardMarkup:
    """
    Create an admin keyboard
    :return: object of reply-keyboard
    """
    keyboard = ReplyKeyboardBuilder()

    keyboard.button(text="Добавить товар")
    keyboard.button(text="Показать все товары")
    keyboard.button(text="Показать следующую страницу")
    keyboard.button(text="Отмена")
    keyboard.adjust(2,2)
    return keyboard.as_markup(resize_keyboard=True, one_time_keyboard=True)
