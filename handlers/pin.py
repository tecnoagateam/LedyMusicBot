from config import BOT_USERNAME
from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(command(["pin", f"pin@{BOT_USERNAME}"]))
@sudo_users_only
@auth_users_only
async def pin(_, message: Message):
    if not message.reply_to_message:
        return
    await message.reply_to_message.pin()


@Client.on_message(command(["unpin", f"unpin@{BOT_USERNAME}"]))
@sudo_users_only
@auth_users_only
async def unpin(_, message: Message):
    if not message.reply_to_message:
        return
    await message.reply_to_message.unpin()
