from googletrans import Translator
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from helpers.list import list

@Client.on_message(filters.command(["tr"]))
async def left(client,message):
	if (message.reply_to_message):
		try:
			lgcd = message.text.split("/tr")
			lg_cd = lgcd[1].lower().replace(" ", "")
			tr_text = message.reply_to_message.text
			translator = Translator()
			translation = translator.translate(tr_text,dest = lg_cd)
			hehek = InlineKeyboardMarkup(
                                [
                                    [
                                        InlineKeyboardButton(
                                            text=f"Bütün Dillər", url="https://cloud.google.com/translate/docs/languages"
                                        )
                                    ],
				    [
                                        InlineKeyboardButton(
                                            "Bağla", callback_data="cls"
                                        )
                                    ],
                                ]
                            )
			try:
				for i in list:
					if list[i]==translation.src:
						fromt = i
					if list[i] == translation.dest:
						to = i 
				await message.reply_text(f"Tərcümə {fromt.capitalize()} -dən {to.capitalize()}\n\n```{translation.text}```", reply_markup=hehek, quote=True)
			except:
			   	await message.reply_text(f"Tərcümə **{translation.src}** -dən **{translation.dest}**\n\n```{translation.text}```", reply_markup=hehek, quote=True)
			

		except :
			print("error")
	else:
			 ms = await message.reply_text("Siz mesaja cavab verməklə bu əmrdən istifadə edə bilərsiniz")
			 await ms.delete()
