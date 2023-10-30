from typing import Optional
from aiogram.filters.callback_data import CallbackData

from database.database import Product


class OrderData(CallbackData, prefix="buy"):
    # product: Product
    id: int
    name: str
    price: int
