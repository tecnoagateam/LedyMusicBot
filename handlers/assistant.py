from callsmusic.callsmusic import client as USER
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserAlreadyParticipant
from helpers.decorators import errors, authorized_users_only

@Client.on_message(filters.group & filters.command(["qatil", "assistantelavet", "qoşul", "qos"]))
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>İlk Öncə Məni  Yönətici Etməlisən</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name =  "Ledy music Assistant"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id,"♥️ Sənin əmrinə Gəldim ♥️")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>Assistant artıq Qrupdadır</b>",
        )
        pass
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🍁 Zaman Aşımı Xətası 🍁\n User {user.first_name} Assistant üçün çoxlu qatılma istəkləri nədəni ilə qrubunuza qatılmadı! Assistanın qrupta yasaqlanmadığından əmin olun."
            "\n\nYada Assistan Hesabını Qruba Özun Əlavə et</b>",
        )
        return
    await message.reply_text(
            "<b>🌿 Assistant uğurla Qrupa Qoşuldu 🌿</b>",
        )
    
@USER.on_message(filters.group & filters.command(["ayril", "assistantleave", "get", "cix"]))
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:  
        await message.reply_text(
            f"<b>Assistant qrubunuzdan ayrılamadı!."
            "\n\nYada Özün Çıxarabilərsən</b>",
        )
        return
 
 
 
