from time import time
from config import BOT_USERNAME

from helpers.filters import command
from pyrogram import Client, filters



@Client.on_message(command(["alive", f"alive@{BOT_USERNAME}"]) & filters.group)
async def alive(client, message):
    await message.reply_text("💠**Mən Çox Gözəl İşləyirəm**💠")
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🦅 Dəstək", url=f"https://t.me/SOQrup"
                    ),
                    InlineKeyboardButton(
                        "🧸 Kanal", url=f"https://t.me/ledyplaylist"
                    )
                ]
            ]
        )
    )



@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]))
async def ping_pong(client, message):
    start = time()
    m_reply = await message.reply_text("__pinging...__")
    delta_ping = time() - start
    await m_reply.edit("**0% ▒▒▒▒▒▒▒▒▒▒**")
    await m_reply.edit_text("🏓 `PONG!!`\n" f"⚡️ `{delta_ping * 1000:.3f} ms`")
