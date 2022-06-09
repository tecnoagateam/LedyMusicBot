import os
from os import path
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery
from pyrogram.types import Message, Voice, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserAlreadyParticipant
from ledymusic import ledymusic, queues
from ledymusic.ledymusic import client as USER
from helpers.admins import get_administrators
import requests
import aiohttp
import youtube_dl
from youtube_search import YoutubeSearch
import converter
from downloaders import youtube
from config import DURATION_LIMIT, BOT_USERNAME
from helpers.filters import command
from helpers.decorators import errors
from helpers.errors import DurationLimitError
from helpers.gets import get_url, get_file_name
from pytgcalls import StreamType
from pytgcalls.types.input_stream import InputAudioStream
from pytgcalls.types.input_stream import InputStream
import aiofiles
import ffmpeg
from PIL import Image, ImageFont, ImageDraw


def transcode(filename):
    ffmpeg.input(filename).output("input.raw", format='s16le', acodec='pcm_s16le', ac=2, ar='48k').overwrite_output().run() 
    os.remove(filename)

# Convert seconds to mm:ss
def convert_seconds(seconds):
    seconds = seconds % (24 * 3600)
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%02d:%02d" % (minutes, seconds)


# Convert hh:mm:ss to seconds
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))


# Change image size
def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage

async def generate_cover(requested_by, title, views, duration, thumbnail):
    async with aiohttp.ClientSession() as session:
        async with session.get(thumbnail) as resp:
            if resp.status == 200:
                f = await aiofiles.open("background.png", mode="wb")
                await f.write(await resp.read())
                await f.close()

    image1 = Image.open("etc/background.png")
    image2 = Image.open("etc/foreground.png")
    image3 = changeImageSize(1280, 720, image1)
    image4 = changeImageSize(1280, 720, image2)
    image5 = image3.convert("RGBA")
    image6 = image4.convert("RGBA")
    Image.alpha_composite(image5, image6).save("temp.png")
    img = Image.open("temp.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("etc/font.otf", 32)
    draw.text((190, 550), f"Ad: {title}", (255, 255, 255), font=font)
    draw.text(
        (190, 590), f"Müddet: {duration}", (255, 255, 255), font=font
    )
    draw.text((190, 630), f"İzlenme: {views}", (255, 255, 255), font=font)
    draw.text((190, 670),
        f"Sifariş: {requested_by}",
        (255, 255, 255),
        font=font,
    )
    img.save("final.png")
    os.remove("temp.png")
    os.remove("background.png")


# ==================================LedyVaves======================================================== 
@Client.on_callback_query(filters.regex("cls"))
async def cls(_, query: CallbackQuery):
    await query.message.delete()

# LedyMusicVaves düzənlənmişdir.

@Client.on_message(command(["oynad", f"oynad@{BOT_USERNAME}", "play"]) 
                   & filters.group
                   & ~filters.edited 
                   & ~filters.forwarded
                   & ~filters.via_bot)
async def play(_, message: Message):

    lel = await message.reply("❄️ **Səsliyə Qoşuluram...**")
    
    administrators = await get_administrators(message.chat)
    chid = message.chat.id

    try:
        user = await USER.get_me()
    except:
        user.first_name = "LedyMusicAssistant"
    usar = user
    wew = usar.id
    try:
        await _.get_chat_member(chid, wew)
    except:
        for administrator in administrators:
            if administrator == message.from_user.id:
                try:
                    invitelink = await _.export_chat_invite_link(chid)
                except:
                    await lel.edit(
                        "<b>İlk məni Qrupuna yönətici olaraq əlavə et!</b>")
                    return

                try:
                    await USER.join_chat(invitelink)
                    await USER.send_message(
                        message.chat.id, "**Salam, Assistant bu Söhbətə müsiqi yayınlamaq üçün qatıldı**")

                except UserAlreadyParticipant:
                    pass
                except Exception:
                    await lel.edit(
                        f"<b>🍁 gözləmə Xətası 🍁</b> \n\Salam {user.first_name}, Assistant, çoxlu qatılma istəkləri nədəni ilə qrubunuza qatılmadı. Assistantın qrupta yasaqlı olmadığından əmin olun və daha sonra yenidən cəhd edin!")
    try:
        await USER.get_chat(chid)
    except:
        await lel.edit(
            f"<i>Salam {user.first_name}, Assistant bu sohbətdə deyil, yöneticidən göndərməsini istəyin /play ilk dəfə əlavə etmək üçün Əmr.</i>")
        return
    
    audio = (message.reply_to_message.audio or message.reply_to_message.voice) if message.reply_to_message else None
    url = get_url(message)

    if audio:
        if round(audio.duration / 400) > DURATION_LIMIT:
            raise DurationLimitError(
                f"❌ Daha uzun videolar {DURATION_LIMIT} dəqiqələrin oynadılamasına icazə verilməz!"
            )

        file_name = get_file_name(audio)
        title = file_name
        thumb_name = "https://telegra.ph/file/801c43e6695d576f99a52.jpg"
        thumbnail = thumb_name
        duration = round(audio.duration / 60)
        views = "Ledy Music Logo"

        keyboard = InlineKeyboardMarkup(
            [
                [

                    InlineKeyboardButton(
                        text="🗑️ Bağla",
                        callback_data="cls")
                    
                ]
            ]
        )
        
        requested_by = message.from_user.first_name
        await generate_cover(requested_by, title, views, duration, thumbnail)  
        file_path = await converter.convert(
            (await message.reply_to_message.download(file_name))
            if not path.isfile(path.join("downloads", file_name)) else file_name
        )

    elif url:
        try:
            results = YoutubeSearch(url, max_results=1).to_dict()
            # print results
            title = results[0]["title"]       
            thumbnail = results[0]["thumbnails"][0]
            thumb_name = f'thumb{title}.jpg'
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, 'wb').write(thumb.content)
            duration = results[0]["duration"]
            url_suffix = results[0]["url_suffix"]
            views = results[0]["views"]
            durl = url
            durl = durl.replace("youtube", "youtubepp")
            
            secmul, dur, dur_arr = 1, 0, duration.split(':')
            for i in range(len(dur_arr)-1, -1, -1):
                dur += (int(dur_arr[i]) * secmul)
                secmul *= 60
                
            keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("🛠️ Dəstək", url=f"https://t.me/SOQrup"),
                InlineKeyboardButton("📱 Kanal", url=f"https://t.me/ledyplaylist"),
            ],[
                InlineKeyboardButton("🗑️ Bağla", callback_data="cls"),
                InlineKeyboardButton("🎬 YouTube'də izlə", url=f"{url}"),
            ],
        ]
    )
        except Exception as e:
            title = "NaN"
            thumb_name = "https://telegra.ph/file/4afbb46f4899c16317607.jpg"
            duration = "NaN"
            views = "NaN"
            keyboard = InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="İzləmək üçün 🎬",
                                url=f"https://youtube.com")

                        ]
                    ]
                )
        if (dur / 60) > DURATION_LIMIT:
             await lel.edit(f"❌ Daha uzun videolar {DURATION_LIMIT} dəqiqələrin oynadılamasına icazə verilməz!")
             return
        requested_by = message.from_user.first_name
        await generate_cover(requested_by, title, views, duration, thumbnail)     
        file_path = await converter.convert(youtube.download(url))
    else:
        if len(message.command) < 2:
            return await lel.edit("🤔 **Dinləmək istədiyin musiqi nədir?**")
        await lel.edit("🔎 **Biraz Gözləyin...**")
        query = message.text.split(None, 1)[1]
        # print(query)
        await lel.edit("❄️ **Səsliyə Qoşuluram...**")
        try:
            results = YoutubeSearch(query, max_results=1).to_dict()
            url = f"https://youtube.com{results[0]['url_suffix']}"
            # print results
            title = results[0]["title"]       
            thumbnail = results[0]["thumbnails"][0]
            thumb_name = f'thumb{title}.jpg'
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, 'wb').write(thumb.content)
            duration = results[0]["duration"]
            url_suffix = results[0]["url_suffix"]
            views = results[0]["views"]
            durl = url
            durl = durl.replace("youtube", "youtubepp")

            secmul, dur, dur_arr = 1, 0, duration.split(':')
            for i in range(len(dur_arr)-1, -1, -1):
                dur += (int(dur_arr[i]) * secmul)
                secmul *= 60
                
        except Exception as e:
            await lel.edit(
                "❌ Musiqi tapılmadı.\n\nBaşqa bir musiqi adı yazın."
            )
            print(str(e))
            return

        keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("🛠️ Dəstək", url=f"https://t.me/SOQrup"),
                InlineKeyboardButton("📱 Kanal", url=f"https://t.me/ledyplaylist"),
            ],[
                InlineKeyboardButton("🗑️ Bağla", callback_data="cls"),
                InlineKeyboardButton("🎬 YouTube'də izlə", url=f"{url}"),
            ],
        ]
    )
        
        if (dur / 60) > DURATION_LIMIT:
             await lel.edit(f"❌ Daha uzun videolar {DURATION_LIMIT} dəqiqələrin oynadılamasına icazə verilməz!")
             return
        requested_by = message.from_user.first_name
        await generate_cover(requested_by, title, views, duration, thumbnail)  
        file_path = await converter.convert(youtube.download(url))
  
    ACTV_CALLS = []
    chat_id = message.chat.id
    for x in ledymusic.pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))
    if int(message.chat.id) in ACTV_CALLS:
        position = await queues.put(message.chat.id, file=file_path)
        await message.reply_photo(
        photo="final.png",
        caption="**❄️ Ad:** {}\n**🕒 Müddət:** {}\n**🐣 Sifariş:** {}\n\n**🚧 Növbə:** {}".format(
        title, duration, message.from_user.mention(), position
        ),
        reply_markup=keyboard)
        os.remove("final.png")
        return await lel.delete()
    else:
        await ledymusic.pytgcalls.join_group_call(
                chat_id, 
                InputStream(
                    InputAudioStream(
                        file_path,
                    ),
                ),
                stream_type=StreamType().local_stream,
            )

        await message.reply_photo(
        photo="final.png",
        reply_markup=keyboard,
        caption="**❄️ Ad:** {}\n**🕒 Müddət:** {}\n**🐣 Sifariş:** {}\n\n**🍁 Chat ✬`{}`✬**".format(
        title, duration, message.from_user.mention(), message.chat.title
        ), )
        os.remove("final.png")
        return await lel.delete()
