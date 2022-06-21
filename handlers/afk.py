import asyncio
import datetime

from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler

from config import BOT_USERNAME



async def afk_handler(client, message):
    try:
        global start, end
        end = datetime.datetime.now().replace(microsecond=0)
        afk_time = end - start
        if message.from_user.is_bot is False:
            await message.reply_text(
                f"<b>Afk {afk_time}</b>\n" f"<b>Səbəb :</b> <i>{reason}</i>"
            )
    except NameError:
        pass


@Client.on_message(filters.command("afk", f"afk@{BOT_USERNAME}"))
async def afk(client, message):
    global start, end, handler, reason
    start = datetime.datetime.now().replace(microsecond=0)
    handler = client.add_handler(
        MessageHandler(afk_handler, (filters.public))
    )
    if len(message.text.split()) >= 2:
        reason = message.text.split(" ", maxsplit=1)[1]
    else:
        reason = "None"
    await message.edit("<b>I'm going afk</b>")


@Client.on_message(filters.command("unafk", f"unafk@{BOT_USERNAME}") & filters.me)
async def unafk(client, message):
    try:
        global start, end
        end = datetime.datetime.now().replace(microsecond=0)
        afk_time = end - start
        await message.edit(f"<b>I'm not AFK anymore.\nI was afk {afk_time}</b>")
        client.remove_handler(*handler)
    except NameError:
        await message.edit("<b>You weren't afk</b>")
        await asyncio.sleep(3)
        await message.delete()
