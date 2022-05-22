import io
import os

from pyrogram import filters
from tswift import Song

from pyrogram import Client as pbot




# Bu pluginler @tenha055 tərəfindən qurulur.


@pbot.on_message(filters.command(["lyric", "lyrics"]))
async def _(client, message):
    lel = await message.reply("Mahnı Sözləri Axtarılır...")
    query = message.text
    if not query:
        await lel.edit("`Mən nə tapmalıyam`")
        return

    song = ""
    song = Song.find_song(query)
    if song:
        if song.lyrics:
            reply = song.format()
        else:
            reply = "Həmin mahnı üçün heç bir söz tapılmadı!"
    else:
        reply = "lyrics tapılmadı! ifaçı adı ilə birlikdə mahnı ilə birlikdə cəhd edin."

    if len(reply) > 4095:
        with io.BytesIO(str.encode(reply)) as out_file:
            out_file.name = "lyrics.text"
            await client.send_document(
                message.chat.id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=query,
                reply_to_msg_id=message.message_id,
            )
            await lel.delete()
    else:
        await lel.edit(reply)  # edit or reply
