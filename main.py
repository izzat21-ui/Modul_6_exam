import asyncio
import logging
import sys
from aiogram.filters import Command
from aiogram.types import Message, KeyboardButton, BotCommand, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from sqlalchemy import select, insert
from sqlalchemy.orm import sessionmaker
from bot.dispatcher import dp
from config.config import engine, BotConfig
from database.config_sqlalchemy import User

session = sessionmaker(engine)()

def make_buttons(buttons_list: list[str], adjustments: list[int]):
    keyboard = ReplyKeyboardBuilder()
    keyboard.add(*[KeyboardButton(text=button) for button in buttons_list])
    keyboard.adjust(*adjustments)

    return keyboard.as_markup(resize_keyboard=True)


def make_inline_buttons(inline_buttons: list[str], adjustments: list[int]):
    keyboard = InlineKeyboardBuilder()
    keyboard.add(*[InlineKeyboardButton(text=button, callback_data=button)
                   for button in inline_buttons])
    keyboard.adjust(*adjustments)

    return keyboard.as_markup()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    query = select(User).where(User.chat_id == message.from_user.id)
    result = session.execute(query).fetchone()
    user = message.from_user
    if not result:
        query = insert(User).values(chat_id=user.id,
                                    first_name=user.first_name,
                                    last_name=user.last_name,
                                    username=user.username)
        session.execute(query)
        session.commit()
    await message.answer(f"Salom, {html.bold(message.from_user.username)}!")

@dp.message(Command(commands=["start", "restart"]))
async def handle_start_commands(msg: Message) -> None:
    await msg.bot.set_my_commands([
        BotCommand(command="/start", description="Start"),
        BotCommand(command="/restart", description="Restart")
    ])

    buttons_list = ["📝 Buyurtma berish", "🤖 Sodiqlik QR", "Filiallar", "Taklif va shikoyatlar",
                    "Geolakatsiyani yuborish",
                    "Mening ballarim", "Manzillarim", "Sozlamalar"]
    adjustments = [4, 4]

    await msg.answer("Salom! Sakurafoodga  xush kelibsiz!", reply_markup=make_buttons(adjustments, buttons_list))

async def main() -> None:
    bot = Bot(token=BotConfig.TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
