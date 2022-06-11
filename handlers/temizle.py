import os

from pyrogram import Client, filters
from pyrogram.types import Message

from config import BOT_USERNAME
from helpers.decorators import errors, sudo_users_only
from helpers.filters import command


downloads = os.path.realpath("downloads")
raw = os.path.realpath("raw_files") # the code is not created for removing raw_files but if you want to create it, use this


@Client.on_message(command([""temizle", f"temizle@{BOT_USERNAME}"]))
@errors
@sudo_users_only
async def clear_downloads(_, message: Message):
    ls_dir = os.listdir(downloads)
    if ls_dir:
        for file in os.listdir(downloads):
            os.remove(os.path.join(downloads, file))
        await message.reply_text("✅ Sᴜᴄᴄᴇssғᴜʟʟʏ Rᴇᴍᴏᴠᴇᴅ ᴀʟʟ Dᴏᴡɴʟᴏᴀᴅᴇᴅ Fɪʟᴇs ғʀᴏᴍ Mʏ Dᴀᴛᴀʙᴀsᴇ...")
    else:
        await message.reply_text("❌ Nᴏ Fɪʟᴇs ᴇxɪsᴛɪɴɢ ɪɴ ᴍʏ Dᴀᴛᴀʙᴀsᴇ...")
