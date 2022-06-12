import os
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.new_chat_members)
async def auto_welcome(bot: Client, msg: Message):
    first = msg.from_user.first_name
    last = msg.from_user.last_name
    mention = msg.from_user.mention
    username = msg.from_user.username
    id = msg.from_user.id
    group_name = msg.chat.title
    group_username = msg.chat.username
    name_button = "🍁 Qoşul 🍁"
    link_button = "https://t.me/ledyplaylist"
    welcome_text = f"Salam, {mention}, {group_name}-a Xoş gəldin! Səni aramızda görməyimizə şadıq.❤️\n 🦅İnanırıq ki, Söhbət Çatında Xoşa gəlməz şeylər baş verməz, Qrupa Qatıldınızsa Qaydalara əməl edin!\n\n**Sənin ID-in** : `{id}`"
    WELCOME_TEXT = os.environ.get("WELCOME_TEXT", welcome_text)
    print("Welcome Message Activate")
    BUTTON = bool(os.environ.get("WELCOME_BUTTON"))
    if not BUTTON:
       await msg.reply_text(text=WELCOME_TEXT.format(
           first = msg.from_user.first_name,
           last = msg.from_user.last_name,
           username = None if not msg.from_user.username else '@' + msg.from_user.username,
           mention = msg.from_user.mention,
           id = msg.from_user.id,
           group_name = msg.chat.title,
           group_username = None if not msg.chat.username else '@' + msg.chat.username
          )
       )
    else:
       await msg.reply_text(text=WELCOME_TEXT.format(
           first = msg.from_user.first_name,
           last = msg.from_user.last_name,
           username = None if not msg.from_user.username else '@' + msg.from_user.username,
           mention = msg.from_user.mention,
           id = msg.from_user.id,
           group_name = msg.chat.title,
           group_username = None if not msg.chat.username else '@' + msg.chat.username
          ),
       reply_markup=InlineKeyboardMarkup(
               [
                   [
                       InlineKeyboardButton
                           (
                               name_button, url=link_button
                           )
                   ]  
               ]
           )
       )  
