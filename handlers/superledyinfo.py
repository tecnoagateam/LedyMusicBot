import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message((filters.private | filters.group) & filters.command(["ledyinfo", "ledyinfo@SSmusicledy_bot"]))
async def ledyinfo(bot, update):
    if (not update.reply_to_message) and ((not update.forward_from) or (not update.forward_from_chat)):
        info = user_info(update.from_user)
    elif update.reply_to_message and update.reply_to_message.forward_from:
        info = user_info(update.reply_to_message.forward_from)
    elif update.reply_to_message and update.reply_to_message.forward_from_chat:
        info = chat_info(update.reply_to_message.forward_from_chat) 
    elif (update.reply_to_message and update.reply_to_message.from_user) and (not update.forward_from or not update.forward_from_chat):
        info = user_info(update.reply_to_message.from_user)
    else:
        return
    try:
        await update.reply_text(
            text=info,
            reply_markup=BUTTONS,
            disable_web_page_preview=True,
            quote=True
        )
    except Exception as error:
        await update.reply_text(error)

def user_info(user):
    text = "--**Super Ledy User İnfo:**--\n"
    text += f"\n**Ad:** `{user.first_name}`"
    text += f"\n**Soyad:** `{user.last_name},`" if user.last_name else ""
    text += f"\n**Tağ Ad:** @{user.username}" if user.username else ""
    text += f"\n**Link:** {user.mention}" if user.username else ""
    text += f"\n**ID:** `{user.id}`"
    text += f"\n**DC:** `{user.dc_id}`" if user.dc_id else ""
    text += f"\n**Silindi:** True" if user.is_deleted else ""
    text += f"\n**Bot:** True" if user.is_bot else ""
    text += f"\n**Verifiziert:** True" if user.is_verified else ""
    text += f"\n**Verifiziert:** True" if user.is_verified else ""
    text += f"\n**Betrug:** True" if user.is_scam else ""
    text += f"\n**Fake:** True" if user.is_fake else ""
    text += f"\n**Support:** True" if user.is_support else ""
    text += f"\n**Dil:** {user.language_code}" if user.language_code else ""
    text += f"\n**Status:** {user.status}" if user.status else ""
    text += f"\n\n--**Super Ledy İnfo:**--"
    return text

def chat_info(chat):
    text = "--**Super Ledy Chat Info**--\n" 
    text += f"\n**Ad:** `{chat.title}`"
    text += f"\n**Tağ Ad:** @{chat.username}" if chat.username else ""
    text += f"\n**Art:** `{chat.type}`"
    text += f"\n**ID:** `{chat.id}`"
    text += f"\n**DC:** `{chat.dc_id}`"
    text += f"\n**Verifiziert:** True" if chat.is_verified else ""
    text += f"\n**Verifiziert:** True" if chat.is_verified else ""
    text += f"\n**Yaradıldı*in:** True" if chat.is_creator else ""
    text += f"\n**Betrug:** True" if chat.is_scam else ""
    text += f"\n**Fake:** True" if chat.is_fake else ""
    text += f"\n\--**Super Ledy Chat Info**--"
    return text
