import asyncio

from pyrogram import Client, filters
from pyrogram.types import Dialog, Chat, Message
from pyrogram.errors import UserAlreadyParticipant

from callsmusic.callsmusic import client as aditya
from config import SUDO_USERS
import asyncio

@Client.on_message(filters.command(["broadcast", "yayin"]))
async def broadcast(_, message: Message):
    sent=0
    failed=0
    if message.from_user.id not in SUDO_USERS:
        return
    else:
        wtf = await message.reply("`broadcast başladı...`")
        if not message.reply_to_message:
            await wtf.edit("mesaj yazın yada mesaj yanitlayin!")
            return
        lmao = message.reply_to_message.text
        async for dialog in USER.iter_dialogs():
            try:
                await USER.send_message(dialog.chat.id, lmao)
                sent = sent+1
                await wtf.edit(f"`broadcasting...` \n\n**Gönderilen:** `{sent}` Chats \n**Gönderilmeyen:** {failed} Chats")
                await asyncio.sleep(3)
            except:
                failed=failed+1
                #await wtf.edit(f"`broadcasting...` \n\n**Gönderilen:** `{sent}` Chats \n**Gönderilmeyen:** {failed} Chats")
                
            
        await message.reply_text(f"`Broadcast Finished ` \n\n**Gönderilen:** `{sent}` Chats \n**Gönderilmeyen:** {failed} Chats")
