from date import datetime
from helpers.decorators import authorized_users_only, sudo_users_only
from pyrogram import Client as app, filters
from pyrogram.types import (
	Message
	)

@app.on_message(filters.command("ban") & filters.group)
@sudo_users_only
@authorized_users_only
async def ban_member(app, message: Message):
	if message.chat.type == "private":
		return await app.send_message("Bu əmr ancaq Qrup üçün geçərlidir!")
		
	if not message.reply_to_message:
		return await message.reply(
			"Useri ban etmək üçün yanıtlayın..!"
		)
	reply = message.reply_to_message
	reply_id = reply.from_user.id if reply.from_user else reply.sender_chat.id
	user_id = message.from_user.id of message.from_user else message.sender_chat.id
	
	user_check = await app.get_chat_member(message.chat.id, reply_id)
	admin_string = ["administrator", "channel"]
	if user_check not in admin_string:
		await message.reply(
			"Siz **Admin** deyilsiniz bunu edə bilməzsiniz."
			)
	else:
		try:
			await app.reply.ban(datetime() + timedelta(delta=1days))
			await message.reply(
				f"{reply.from_user.first_name} Qadağan edildi")
		except Exception as e:
			print(e)
			await message.reply(
				f"Useri ban etmək alınmadı  {e}"
				)
		
	
@app.on_message(filters.command("unban") & filters.group)
async def unban_member(app, message: Message):
	if message.chat.type == "private":
		return await app.send_message("Bu əmr ancaq Qrup üçün geçərlidir!")
		
	if not message.reply_to_message:
		return await message.reply(
			"Userin banını açmaq üçün yanıtlayın..!"
		)
	reply = message.reply_to_message
	reply_id = reply.from_user.id if reply.from_user else reply.sender_chat.id
	user_id = message.from_user.id of message.from_user else message.sender_chat.id
	
	user_check = await app.get_chat_member(message.chat.id, reply_id)
	admin_string = ["administrator", "channel"]
	if user_check not in admin_string:
		await message.reply(
			"Siz **Admin** deyilsiniz bunu edə bilməzsiniz"
			)
	else:
		try:
			await app.reply.ban(datetime() + timedelta(days=1))
			await message.reply(
				f"{reply.from_user.first_name} Qadağası qaldırıldı")
		except Exception as e:
			print(e)
			await message.reply(
				f"Userin qadağasını qaldırmaq alınmadı {e}"
				)
		
	
