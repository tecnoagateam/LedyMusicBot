import asyncio

from pyrogram import Client, filters
from pyrogram.types import Dialog, Chat, Message
from pyrogram.errors import UserAlreadyParticipant

from ledymusic.ledymusic import client as aditya
from config import SUDO_USERS

@Client.on_message(filters.command(["reklam"]))
async def broadcast(_, message: Message):
    sent=0
    failed=0
    if message.from_user.id not in SUDO_USERS:
        return
    else:
        wtf = await message.reply("`Reklam yayını başladı...`")
        if not message.reply_to_message:
            await wtf.edit("**__Reklam üçün mesajı yanıtlayın...__**")
            return
        lmao = message.reply_to_message.text
        async for dialog in aditya.iter_dialogs():
            try:
                await aditya.send_message(dialog.chat.id, lmao)
                sent = sent+1
                await wtf.edit(f"`Reklam uğurla göndərilir` \n\n**Gönderildi:** `{sent}` Söhbət \n**Uğursuz:** {failed} Söhbət")
                await asyncio.sleep(3)
            except:
                failed=failed+1
        await message.reply_text(f"`Reklam uğurla göndərildi' \n\n**Gönderildi:** `{sent}` Söhbət \n**Uğursuz:** {failed} Söhbət")
