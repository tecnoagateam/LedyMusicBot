import pyrogram
import asyncio
import os
from pyrogram import filters, Client as aga

@aga.on_message((filters.command(["report"]) | filters.regex("@admins") | filters.regex("@admin")) & filters.group)
async def report_user(bot, message):
    if message.reply_to_message:
        chat_id = message.chat.id
        reporter = str(message.from_user.id)
        mention = message.from_user.mention
        admins = await bot.get_chat_members(chat_id=chat_id, filter="administrators")
        success = True
        report = f"**𝖱𝖾𝗉𝗈𝗋𝗍𝖾𝗋:** {mention} ({reporter})" + "\n"
        report += f"**Səbəb:** {message.reply_to_message.link}"
        for admin in admins:
            try:
                reported_post = await message.reply_to_message.forward(admin.user.id)
                await reported_post.reply_text(
                    text=report,
                    chat_id=admin.user.id,
                    disable_web_page_preview=True
                )
                success = True
            except:
                pass
        if success:
            await message.reply_text("Adminlərə bildirildi!")
