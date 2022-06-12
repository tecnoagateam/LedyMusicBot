from time import time
from config import BOT_USERNAME

from helpers.filters import command
from pyrogram import Client, filters


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]))
async def ping_pong(client, message):
    start = time()
    m_reply = await message.reply_text("__pinging...__")
    delta_ping = time() - start
    await m_reply.edit("**0% ▒▒▒▒▒▒▒▒▒▒**")
    await m_reply.edit("**20% ██▒▒▒▒▒▒▒▒**")
    await m_reply.edit("**40% ████▒▒▒▒▒▒**")
    await m_reply.edit("**60% ██████▒▒▒▒**")
    await m_reply.edit("**80% ████████▒▒**")
    await m_reply.edit("**100% ██████████**")
    await m_reply.edit_text("🏓 `PONG!!`\n" f"⚡️ `{delta_ping * 1000:.3f} ms`")

