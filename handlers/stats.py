from handlers.database.users_sql import Users, num_users
from handlers.database.chats_sql import Chats, num_chats
from handlers.database import SESSION
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(~filters.edited & ~filters.service, group=1)
async def users_sql(_, message: Message):
    if message.from_user:
        q = SESSION.query(Users).get(int(message.from_user.id))
        if not q:
            SESSION.add(Users(message.from_user.id))
            SESSION.commit()
        else:
            SESSION.close()


@Client.on_message(~filters.edited & filters.group, group=2)
async def chats_sql(_, message: Message):
    if message.chat:
        q = SESSION.query(Chats).get(int(message.chat.id))
        if not q:
            SESSION.add(Chats(message.chat.id))
            SESSION.commit()
        else:
            SESSION.close()


@Client.on_message(filters.user() & ~filters.edited & filters.command("stat"))
async def _stats(_, message: Message):
    users = await num_users()
    chats = await num_chats()
    await message.reply(f"Total Users : {users} \n\nTotal Chats : {chats}", quote=True)
