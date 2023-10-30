from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery
from utilits.callbackData import OrderData

callback_router = Router()


@callback_router.callback_query(OrderData.filter())
async def create_order(callback: CallbackQuery, callback_data: OrderData):
    # TODO: create logic ordered
    # await callback.answer(f"Функция в разработке.\nПокупка товара {order_data.product.name} по цене "
    #                       f"{order_data.product.price}\n id = {order_data.product.id}", show_alert=True)
    await callback.answer(f"Функция в разработке.\nПокупка товара {callback_data.name} по цене "
                          f"{callback_data.price}\n id = {callback_data.id}", show_alert=True)
