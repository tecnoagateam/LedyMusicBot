from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import BOT_USERNAME, BOT_NAME as bot
from helpers.filters import command, other_filters2
# EfsaneMusicVaves tarafından düzenlendi. 

@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]))
async def start(_, message: Message):
                await message.reply_photo(
                "https://telegra.ph/file/e669d8ec6be16f4b7cc39.jpg",
                caption=(f"""**Salam {message.from_user.mention} 🎵\nMən {bot}!\nSəsli sohbətlərdə müsiqi oynada bilən botam. Qrupa mənə admin hüquqları verməyiniz şərt.**"""),
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🍁 ❰ Qrubuna Əlavə et ❱ 🍁", url=f"https://t.me/SSmusicLedy_bot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔊 Asistan", url="https://t.me/LedyMusicAssistant"
                    ),
                    InlineKeyboardButton(
                        "🛠️ Support", url="https://t.me/SOQrup"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📚 Əmrlər" , callback_data= "cbbilgi"
                    ),
                    InlineKeyboardButton(
                        "📱 Rəsmi Kanal", url=f"https://t.me/ledyplaylist"
                    )
                ]
                
           ]
        ),
    )
  


@Client.on_message(command(["bilgi", f"bilgi@{BOT_USERNAME}"]))
async def bilgi(_, message: Message):
      await message.reply_text(" ❗ Not:\n Botun aktif çalışması için şu üç yetkiye ihtiyaç vardır:\n- Mesaj silme yetkisi,\n- Bağlantı ile davet etme yetkisi,\n- Sesli sohbeti yönetme yetkisi.", 
      reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "✦ Hərkəs üçün əmrlər", callback_data="herkes")
                 ],[                     
                     InlineKeyboardButton(
                         "✦ Adminlər üçün Əmrlər", callback_data="admin")
                 ],[
                     InlineKeyboardButton(
                         "✦ Ana menyu", callback_data="cbstart")
                 ],[
                     InlineKeyboardButton(
                         "🍁 Admin 🍁", url="https://t.me/Tenha055")
                 ]
             ]
         )
    )


@Client.on_callback_query(filters.regex("cbbilgi"))
async def cbbilgi(_, query: CallbackQuery):
    await query.edit_message_text(" ❗ Not:\nBotun aktif çalışması için şu üç yetkiye ihtiyaç vardır:\n- Mesaj silme yetkisi,\n- Bağlantı ile davet etme yetkisi,\n- Sesli sohbeti yönetme yetkisi.", 
    reply_markup=InlineKeyboardMarkup(
      [
        [
          InlineKeyboardButton(
            "✨Herkes için Komutlar", callback_data ="herkes")
        ],
        [
          InlineKeyboardButton(
            "👑Yönetici Komutları",callback_data ="admin")
        ],
        [
          InlineKeyboardButton(
            "🏠Ana Menü", callback_data="cbstart")
        ],
        [
          InlineKeyboardButton(
            "⚙ Geliştirici", url="https://t.me/Tenha055")
        ]
      ]
     ))


@Client.on_callback_query(filters.regex("herkes"))
async def herkes(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>Selam {query.from_user.mention}!\nBu botun herkes için komut menüsü 😉\n\n ▶️ /oynat - şarkı çalmak için youtube url'sine veya şarkı dosyasına yanıt verme\n ▶️ /oynat <song name> - istediğiniz şarkıyı çal\n 🔴 \n 🎵 /bul <song name> - istediğiniz şarkıları hızlı bir şekilde bulun\n 🎵 /vbul istediğiniz videoları hızlı bir şekilde bulun\n 🔍 /ara <query> - youtube'da ayrıntıları içeren videoları arama\n\n</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "⚙ Admin", url="https://t.me/Tenha055")
                 ],
                 [
                     InlineKeyboardButton(
                         "⬅️ Geri ⬅️", callback_data="cbbilgi")
                 ] 
             ]
         )
         )


@Client.on_callback_query(filters.regex("admin"))
async def admin(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>Salam {query.from_user.mention}!\nBu botun adminler üçün Ərmlər menyusu🤩\n\n ▶️ /devam - musiqi oynatmaqa davam et\n ⏸️ /durdur - çalan parçayı duraklatmak için\n 🔄 /atla- Sıraya alınmış müzik parçasını atlatır.\n ⏹ /son - müzik çalmayı durdurma\n 🔼 /ver botun sadece yönetici için kullanılabilir olan komutlarını kullanabilmesi için kullanıcıya yetki ver\n 🔽 /al botun yönetici komutlarını kullanabilen kullanıcının yetkisini al\n\n ⚪ /asistan - Müzik asistanı grubunuza katılır.\n\n</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "🍁 Admin 🍁", url="https://t.me/Tenha055")
                 ],
                 [
                     InlineKeyboardButton(
                         "⬅️ Geri ⬅️", callback_data="cbbilgi")
                 ] 
             ]
         )
         )


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(f"""**Slaam {query.from_user.mention} 🎵\nMən {bot}!\nSəsli sohbətlərdə müsiqi oynada bilən botam. Qrupda admin hüquqları verməyiniz şərt..**""",
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ Qrubuna Əlavə et ❱ ➕", url=f"https://t.me/SSmusicLedy_bot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔊 Asistan", url="https://t.me/LedyMusicAssistant"
                    ),
                    InlineKeyboardButton(
                        "🍁 Support", url="https://t.me/SOQrup"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📚 Əmrlər" , callback_data= "cbbilgi"
                    ),
                    InlineKeyboardButton(
                        "📱 Rəsmi Kanal ", url=f"https://t.me/ledyplaylist"
                    )
                ]
                
           ]
        ),
    )
