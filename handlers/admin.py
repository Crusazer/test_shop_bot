from settings import settings
from FSM.FSM import AddProduct
from database.database import db, Product

from aiogram import Bot, filters
from aiogram.fsm.context import FSMContext
from aiogram.types.message import Message
from aiogram.filters import Command
from aiogram import Router, F

admin_router = Router()
# This work only for admins
admin_router.message.filter(F.from_user.id.in_(settings.ADMIN_ID))


@admin_router.message(Command("cancel"))
@admin_router.message(F.text.lower() == "отмена")
async def cmd_cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Все действия отменены!")


@admin_router.message(F.text == "Добавить товар")
async def command_add_product(message: Message, state: FSMContext):
    """ Add a product to the DataBase  """
    await message.answer(text="Введите название товара: ")
    await state.set_state(AddProduct.add_name)


@admin_router.message(AddProduct.add_name)
async def get_name(message: Message, state: FSMContext):
    """ Step 1 of create a product. Getting the product name to add to the database"""
    await state.update_data(name=message.text)
    await message.answer(f"Теперь введите описание товара: ")
    await state.set_state(AddProduct.add_description)


@admin_router.message(AddProduct.add_description)
async def get_description(message: Message, state: FSMContext):
    """ Step 2 of create a product. Getting the product description to add to the database """
    await state.update_data(description=message.text)
    await message.answer(f"Теперь пришлите фото продукта: ")
    await state.set_state(AddProduct.add_photo)


@admin_router.message(AddProduct.add_photo, F.photo)
async def get_photo(message: Message, state: FSMContext):
    """ Step 3 of create a product. Getting the photo to add to the database """
    await state.update_data(photo=message.photo[-1].file_id)
    await message.answer("Введите цену товара: ")
    await state.set_state(AddProduct.add_price)


@admin_router.message(AddProduct.add_photo)
async def get_photo_incorrect(message: Message):
    """ If got message without a photo """
    await message.answer("Отправьте пожалуйста фото продукта: ")


@admin_router.message(AddProduct.add_price)
async def get_price(message: Message, state: FSMContext):
    await state.update_data(price=int(message.text))
    await message.answer("Введите количество товара: ")
    await state.set_state(AddProduct.add_count)


@admin_router.message(AddProduct.add_price)
async def get_price_incorrect(message: Message):
    """ If got incorrect price """
    await message.answer(f"Отправьте пожалуйста фото продукта: ")


@admin_router.message(AddProduct.add_count)
async def get_count_product(message: Message, state: FSMContext):
    await state.update_data(count=int(message.text))
    values = await state.get_data()
    product = Product(db.get_last_product_id() + 1, *values.values())
    db.add_product(product)
    await state.clear()


@admin_router.message(Command("add_admin"))
async def add_admin(message: Message):
    if message.text.split()[1].isdigit():
        settings.ADMIN_ID.append(int(message.text.split()[1]))
        await message.answer(f"Пользователь <b>{message.text.split()[1]}</b> стал администратором!")
    else:
        await message.answer("Операция не удалась!")
