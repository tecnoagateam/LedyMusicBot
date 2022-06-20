import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message
from helpers.filters import command
from helpers.decorators import authorized_users_only
from config import BOT_USERNAME


@Client.on_message(command(["tagall", f"tagall@{BOT_USERNAME}"]))
@authorized_users_only
async def tagall(client, message):
    await message.delete()
    chat_id = message.chat.id
    string = ""
    limit = 1
    icm = client.iter_chat_members(chat_id)
    async for member in icm:
        tag = member.user.username
        if limit <= 10:
            string += f"@{tag}\n" if tag != None else f"{member.user.mention}\n"
            limit += 1
        else:
            await client.send_message(chat_id, text=string)
            limit = 1
            string = ""
            await asyncio.sleep(2)
