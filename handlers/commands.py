from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from keyboards.reply import main_keyboard, admin_keyboard
from settings import settings

command_router = Router()


@command_router.message(Command('start'))
async def start(message: Message):
    if message.from_user.id in settings.ADMIN_ID:
        await message.answer("Hello Admin.", reply_markup=admin_keyboard())
    else:
        await message.answer("Hello. I am The shop Bot!", reply_markup=main_keyboard())
