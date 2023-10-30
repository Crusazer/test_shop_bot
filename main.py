import asyncio
from dotenv import load_dotenv

from aiogram import Dispatcher, Bot
from aiogram.filters import Command

from handlers.admin import admin_router
from handlers.callback import callback_router
from settings import settings
from handlers.commands import command_router
from handlers.basic import router

from aiogram.types import BotCommand, BotCommandScopeDefault

async def main():
    load_dotenv()
    bot = Bot(settings.TOKEN, parse_mode="HTML")
    dp = Dispatcher()

    """ Register router """
    dp.include_router(router)
    dp.include_router(command_router)
    dp.include_router(admin_router)
    dp.include_router(callback_router)

    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        await bot.send_message(chat_id=settings.ADMIN_ID[0], text=f"Bot stopped!")
        await asyncio.wait_for(bot.session.close(), timeout=10)


if __name__ == '__main__':
    asyncio.run(main())
