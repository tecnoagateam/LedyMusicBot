import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(filters.private & filters.sticker)
async def stickers(_, message):
       await message.reply(f"**Göndərdiyin Stickerin ID-si:**  `{message.sticker.file_id}`", quote=True)
