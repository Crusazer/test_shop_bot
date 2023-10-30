from aiogram.fsm.context import FSMContext

from FSM.FSM import WatchGoods
from database.database import db
from keyboards.inline import get_buy
from settings import settings

from aiogram import Bot
from aiogram.types.message import Message
from aiogram import Router, F
from utilits.callbackData import OrderData

router = Router()


@router.startup()
async def start_bot(bot: Bot):
    for i in settings.ADMIN_ID:
        await bot.send_message(chat_id=i, text="Bot started!")


@router.message(F.text.lower() == "id")
async def get_id(message: Message):
    await message.answer(f"Your id: {message.from_user.id}")


@router.message(F.text == "Показать следующую страницу")
async def get_goods(message: Message, bot: Bot, state: FSMContext):
    # If user press button "Каталог товаров" first time
    if await state.get_state() is None:
        await state.set_state(WatchGoods.watch)
        await state.update_data(page=0)

    # Get goods on the page
    page = (await state.get_data())["page"]
    products = db.get_goods(page * settings.PAGE_SIZE, settings.PAGE_SIZE)
    # If not goods anymore. Next to end page
    if not products:
        await message.answer("Товары закончились. При нажатии каталог товаров товары будут показаны заново.")
        await state.update_data(page=0)
    else:
        # Send page of goods to user
        for product in products:
            await bot.send_photo(chat_id=message.chat.id,
                                 photo=product.photo_id,
                                 caption=f"<b>{product.name}</b>\n"
                                         f"<b>Описание товара:</b>\n\t\t{product.description}\n\n"
                                         f"<b>Цена:</b>\n\t\t{product.price} рублей.",
                                 reply_markup=get_buy(product))
        page += 1
        await state.update_data(page=page)


@router.message(F.text == "Показать все товары")
async def get_goods(message: Message, bot: Bot):
    products = db.get_all_goods()

    for product in products:
        await bot.send_photo(chat_id=message.chat.id,
                             photo=product.photo_id,
                             caption=f"<b>{product.name}</b>\n"
                                     f"<b>Описание товара:</b>\n\t\t{product.description}\n\n"
                                     f"<b>Цена:</b>\n\t\t{product.price} рублей.",
                             reply_markup=get_buy(product))
