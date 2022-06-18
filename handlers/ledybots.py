from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import BOT_USERNAME, BOT_NAME as bot
from helpers.filters import command, other_filters2



 
@Client.on_message(command(["ledybots", f"ledybots@{BOT_USERNAME}"]))
async def start(_, message: Message):
                await message.reply_photo(
                "",
                caption=(f"""✧═══════•❀•═══════✧
**Salam {message.from_user.mention}!\n\nLedy Botlar ən sürətli və güclü telegram botlarıdır.\n\nSən Onlardan Rahat və təhlükəsiz istifadə edə bilərsən!    ✧═══════•❀•═══════✧
"""),
         reply_markup=InlineKeyboardMarkup(
            [
