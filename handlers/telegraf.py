import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from telegraph import upload_file
from config import BOT_USERNAME
from helpers.filters import command
from helpers.decorators import errors

DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/")

@Client.on_message(filters.private & filters.media)
async def getmedia(bot, update):
    medianame = DOWNLOAD_LOCATION + str(update.from_user.id)
    try:
        message = await update.reply(
            text="`Göndərdiyiniz Media Telegrafa Yüklənir...`",
            quote=True,
            disable_web_page_preview=True
        )
        await bot.download_media(
            message=update,
            file_name=medianame
        )
        response = upload_file(medianame)
        try:
            os.remove(medianame)
        except:
            pass
    except Exception as error:
        print(error)
        text=f"Xəta : <code>{error}</code>"
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton('Dəstək', url="https://t.me/SOQrup")
            ]]
        )
        await message.edit_text(
            text=text,
            disable_web_page_preview=True,
            reply_markup=reply_markup
        )
        return
    text=f"**Link :** `https://telegra.ph{response[0]}`"
    reply_markup=InlineKeyboardMarkup(
        [[
        InlineKeyboardButton(text="Link-i aç", url=f"https://telegra.ph{response[0]}"),
        InlineKeyboardButton(text="Telegrama Paylaş", url=f"https://telegram.me/share/url?url=https://telegra.ph{response[0]}") 
        ]]
    )
    await message.edit_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )




@Client.on_message(command(["telegraph", f"telegraph@{BOT_USERNAME}"]))
@errors
async def paste(_, message: Message):
    reply = message.reply_to_message

    if not reply or not reply.text:
        return await message.reply("**Mesajı Yanıtla...")

    if len(message.command) < 2:
        return await message.reply("**Nümunə:**\n\n /telegraph [Mesaj]")

    page_name = message.text.split(None, 1)[1]
    page = telegraph.create_page(
        page_name, html_content=reply.text.html.replace("\n", "<br>")
    )
    return await message.reply(
        f"**Link:** {page['url']}",
        disable_web_page_preview=True,
    )
