from aiogram.utils.keyboard import InlineKeyboardBuilder

from database.database import Product
from utilits.callbackData import OrderData


def get_buy(product: Product):
    builder = InlineKeyboardBuilder()
    builder.button(text="Купить", callback_data=OrderData(id=product.id, name=product.name, price=product.price))
    return builder.as_markup()
