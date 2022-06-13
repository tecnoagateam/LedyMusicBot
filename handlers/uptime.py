from time import time
from datetime import datetime
from pyrogram import Client, filters
from config import BOT_USERNAME
from helpers.filters import command
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("days", 60 * 60 * 24),
    ("h", 60 * 60),
    ("m", 60),
    ("s", 1)
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


@Client.on_message(filters.command(["uptime", f"uptime@{BOT_USERNAME}"]))
async def get_uptime(client, message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "**Ledy Music Bot Status:\n\n"
        f"• **iş vaxtı:** `{uptime}`\n"
        f"• **başlama vaxtı:** `{START_TIME_ISO}`"
    )



@Client.on_message(command(["alive", f"alive@{BOT_USERNAME}"]) & filters.group)
async def alive(client, message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        f"""****\n\n<b>⏰ **uptime:**</b> `{uptime}`""",
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

