import asyncio
from pyrogram import Client, filters
from config import BOT_USERNAME
from helpers.decorators import sudo_users_only, authorized_users_only
from helpers.filters import command

TG_MAX_SELECT_LEN = 100

@Client.on_message(command(["purge", f"purge@{}"]))
@sudo_users_only
@authorized_users_only
async def purge(client, message):
    """ purge upto the replied message """
    if message.chat.type not in (("supergroup", "channel")):

        return

    is_admin = await admin_check(message)

    if not is_admin:
        return

    status_message = await message.reply_text("Silinir...", quote=True)
    await message.delete()
    message_ids = []
    count_del_etion_s = 0

    if message.reply_to_message:
        for a_s_message_id in range(
            message.reply_to_message.message_id,
            message.message_id
        ):
            message_ids.append(a_s_message_id)
            if len(message_ids) == TG_MAX_SELECT_LEN:
                await client.delete_messages(
                    chat_id=message.chat.id,
                    message_ids=message_ids,
                    revoke=True
                )
                count_del_etion_s += len(message_ids)
                message_ids = []
        if len(message_ids) > 0:
            await client.delete_messages(
                chat_id=message.chat.id,
                message_ids=message_ids,
                revoke=True
            )
            count_del_etion_s += len(message_ids)

    await status_message.edit_text(
        f"{count_del_etion_s} mesaj silindi"
    )
    await asyncio.sleep(5)
    await status_message.delete()
