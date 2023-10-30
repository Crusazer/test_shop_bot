from aiogram.fsm.state import StatesGroup, State


class AddProduct(StatesGroup):
    """ State to add new product to DataBase"""
    add_name = State()
    add_description = State()
    add_photo = State()
    add_price = State()
    add_count = State()


class WatchGoods(StatesGroup):
    """ State when user watch goods"""
    page = 0
    watch = State()
