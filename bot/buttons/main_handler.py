from os import getenv
from pyexpat.errors import messages

from aiogram import F, html
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, KeyboardButton, CallbackQuery, BotCommand, InlineKeyboardButton, InlineQuery, \
    InlineQueryResultArticle, InputTextMessageContent, LabeledPrice, PreCheckoutQuery
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from bot.dispatcher import dp
from bot.functions import *
from aiogram.utils.i18n import gettext as _
from aiogram.utils.i18n import lazy_gettext as __
from config.config import *
import random




    # class ButtonState(StatesGroup):
    #     language = State()
    #
    #
    # def make_buttons(buttons_list: list[str], adjustments: list[int]):
    #     keyboard = ReplyKeyboardBuilder()
    #     keyboard.add(*[KeyboardButton(text=button) for button in buttons_list])
    #     keyboard.adjust(*adjustments)
    #
    #     return keyboard.as_markup(resize_keyboard=True)
    #
    #
    # def make_inline_buttons(inline_buttons: list[str], adjustments: list[int]):
    #     keyboard = InlineKeyboardBuilder()
    #     keyboard.add(*[InlineKeyboardButton(text=button, callback_data=button)
    #                    for button in inline_buttons])
    #     keyboard.adjust(*adjustments)
    #
    #     return keyboard.as_markup()
    #
    #
    # @dp.message(F.text == __("Orqaga"))
    # @dp.message(Command(commands=["start", "restart"]))
    # async def handle_start_commands(msg: Message) -> None:
    #     await msg.bot.set_my_commands([
    #         BotCommand(command="/start", description="Start"),
    #         BotCommand(command="/restart", description="Restart")
    #     ])
    #
    #     buttons_list = [_("📝 Buyurtma berish"), _("🤖 Sodiqlik QR"), _("Filiallar"), _("Taklif va shikoyatlar"), _("Geolakatsiyani yuborish"),
    #                     _("Mening ballarim"), _("Manzillarim"), _("Sozlamalar")]
    #     adjustments = [4,4]
    #
    #     buttons = make_buttons(buttons_list, adjustments)
    #     await msg.answer(_("Salom! Sakurafoodga  xush kelibsiz!"), reply_markup=buttons)
    #
    #
    # random_user = None
    #
    #
    # @dp.message(F.text == __("📝 Buyurtma berish"))
    # async def handle_chats(msg: Message):
    #     await msg.answer("Bot vaqtincha ish faoliyatini tugatdi iltimos keyinroq urinib koring")
    #
    # @dp.message(F.text == __("🤖 Sodiqlik QR"))
    # async def handle_stop(msg: Message):
    #     await msg.answer("Suhbat yakunlandi!")
    #
    #
    # # About handler
    # @dp.message(F.text == __("🤖 Bot haqida"))
    # async def handle_about(msg: Message):
    #     info = _("""
    #     Anonymous Chat boti sizga boshqa foydalanuvchilar bilan anonim tarzda
    # muloqot olib borishingizga imkon beradi.
    #
    # ❗️Iltimos, nomaqbul so'zlardan foydalanmang, aks holda botdan chetlashtirilasiz!
    # """)
    #
    #     await msg.answer(info)
    #
    #
    # # Tillarni handle qilish
    # @dp.message(F.text == __("🇺🇿/🇷🇺/🇺🇸 Til"))
    # async def handle_languages(msg: Message, state: FSMContext):
    #     langs = [_("🇺🇿 O'zbekcha"), _("🇷🇺 Русский"), _("🇺🇸 English"), _("Orqaga")]
    #     adjustments = [3, 1]
    #     buttons = make_buttons(langs, adjustments)
    #
    #     await state.set_state(ButtonState.language)
    #     await msg.answer(_("Tilni tanlang"), reply_markup=buttons)
