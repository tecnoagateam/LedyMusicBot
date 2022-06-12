import os
import sys
import asyncio

from helpers.filters import command
from pyrogram import Client, filters
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message
from config import BOT_USERNAME
from time import time
from time import sleep
from datetime import datetime

# System Uptime
START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (
    ('Week', 60 * 60 * 24 * 7),
    ('Day', 60 * 60 * 24),
    ('Hour', 60 * 60),
    ('Min', 60),
    ('Sec', 1)
)
async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)

@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]))
async def ping(client, m: Message):
   start = time()
   current_time = datetime.utcnow()
   m_reply = await m.edit("`Pinging...`")
   delta_ping = time() - start
   await m_reply.edit("**0% ▒▒▒▒▒▒▒▒▒▒**")
   await m_reply.edit("**20% ██▒▒▒▒▒▒▒▒**")
   await m_reply.edit("**40% ████▒▒▒▒▒▒**")
   await m_reply.edit("**60% ██████▒▒▒▒**")
   await m_reply.edit("**80% ████████▒▒**")
   await m_reply.edit("**100% ██████████**")
   await asyncio.sleep(1)
   end = datetime.now()
   uptime_sec = (current_time - START_TIME).total_seconds()
   uptime = await _human_time_duration(int(uptime_sec))
   await m_reply.edit(f"🏓 **Pong!!** `{delta_ping * 1000:.3f} ms`\n\n**Uptime** - `{uptime}`")
