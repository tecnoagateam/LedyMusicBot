import random
import os, logging, asyncio
from pyrogram import Client, filters

@Client.on_message(filters(["all", "ledytag"]))
async def mentionall(_, message: Message):
    x = await eor(event, "...")
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.forward:
            replied_user = previous_message.forward.sender_id
        else:
            replied_user = previous_message.sender_id
    else:
        await x.edit("mesajı yanıtla")
    user_id = replied_user
    caption = """<a href='tg://user?id={}'>{}</a>""".format(user_id, input_str)
    await x.edit(caption, parse_mode="HTML")
