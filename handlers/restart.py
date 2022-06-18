from handlers import check_heroku
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram import Client, filters
from helpers.decorators import sudo_users_only
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery


@Client.on_message(command(["restart"]) & ~filters.edited)
@sudo_users_only 
@check_heroku
async def gib_restart(client, message, hap):
    msg_ = await message.reply_photo(
                                     photo="https://telegra.ph/file/84121d4d66583f22b508e.jpg", 
                                     caption="**⏳ Yenidən işə salınma başladıldı**...\n\n🌜 Mənim Sahibim Zəhmət Olmasa Biraz Gözləyin.**"
   )
    hap.restart()
