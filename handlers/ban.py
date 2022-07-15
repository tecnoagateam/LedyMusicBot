 #əbədilik ban 👋👋i

import os
from config import BOT_USERNAME
from helpers.decorators import authorized_users_only
from pyrogram import Client, filters
from pyrogram.types import Message, User


@Client.on_message(filters.command(["ban", f"ban@{BOT_USERNAME}"]))
@authorized_users_only
async def ban(bot, message):
    chatid = message.chat.id
    if message.reply_to_message:
        admins_list = await bot.get_chat_members(
            chat_id=chatid, filter="administrators"
        )
        admins = []
        for admin in admins_list:
            id = admin.user.id
            admins.append(id)
        userid = message.from_user.id
        if userid in admins:
            user_to_ban = message.reply_to_message.from_user.id
            if user_to_ban in admins:
                await message.reply(text="Adminləri ban edə bilmərəm")
            else:
                try:
                    await bot.ban_chat_member(chat_id=chatid, user_id=user_to_ban)
                    await message.reply_text(
                        f"**❗ Biri Daha Getdi**\n{message.reply_to_message.from_user.mention} xoş getdin! 👋"
                    )
                except Exception as error:
                    await message.reply_text(f"`Xəta:` {error}")
        else:
            await message.reply_text("Gözəl cəhd, lakin səhv hərəkət...")
