from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import BOT_USERNAME, BOT_NAME as bot
from helpers.filters import command, other_filters2
# EfsaneMusicVaves tarafından düzenlendi. 

@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]))
async def start(_, message: Message):
                await message.reply_photo(
                "https://telegra.ph/file/e669d8ec6be16f4b7cc39.jpg",
                caption=(f"""**Salam {message.from_user.mention} 🎵\nMən {bot}!\nSəsli söhbətlərdə müsiqi oynada bilən botam. Qrupda mənə admin hüquqları verməyi unutmayın.**"""),
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
                        "📚 Əmrlər" , callback_data= "cbmelumat"
                    ),
                    InlineKeyboardButton(
                        "📱 Rəsmi Kanal", url=f"https://t.me/ledyplaylist"
                    )
                ]
                
           ]
        ),
    )
  


@Client.on_message(command(["melumat", f"melumat@{BOT_USERNAME}"]))
async def bilgi(_, message: Message):
      await message.reply_text(" ❗ Qeyd:\nBotun aktif çalışması üçün aşağıdakı 3 yetkisi olmalıdır:\n- Mesaj silmə yetkisi,\n- Bağlantı ilə dəvət etmə yetkisi,\n- Səsli söhbəti yönətmə yetkisi.", 
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
                         "🍁 Support 🍁", url="https://t.me/Tenha055")
                 ]
             ]
         )
    )


@Client.on_callback_query(filters.regex("cbmelumat"))
async def cbbilgi(_, query: CallbackQuery):
    await query.edit_message_text(" ❗ Qeyd:\nBotun aktif çalışması üçün aşağıdakı 3 yetkisi olmalıdır:\n- Mesaj silmə yetkisi,\n- Bağlantı ilə dəvət etmə yetkisi,\n- Səsli söhbəti yönətmə yetkisi.", 
    reply_markup=InlineKeyboardMarkup(
      [
        [
          InlineKeyboardButton(
            "🍁 Hərkəs üçün əmrlər 🍁", callback_data ="herkes")
        ],
        [
          InlineKeyboardButton(
            "👑 Admin Əmrləri ",callback_data ="admin")
        ],
        [
          InlineKeyboardButton(
            "🏠 Ana Menüyu", callback_data="cbstart")
        ],
        [
          InlineKeyboardButton(
            "🍁 Support 🍁", url="https://t.me/SOQrup")
        ]
      ]
     ))


@Client.on_callback_query(filters.regex("herkes"))
async def herkes(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>Salam {query.from_user.mention}!\nBu botun hərkəs üçün əmrlər menyusu 😉\n\n ▶️ /oynad <song name> - istədiyin musiqini oynad\n 🍁 \n 🎵 /tap <song name> - istədiyiniz musiqini sürətli endirə bilərsiniz \n 🎵 /vtap istədiyiniz videonu sürətli endirə bilərsiniz\n 🔍 /axtar <query> - YouTube-dən video linkləri axtar \n\n</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "🍁 Support 🍁", url="https://t.me/SOQrup")
                 ],
                 [
                     InlineKeyboardButton(
                         "⬅️ Geri ⬅️", callback_data="cbmelumat")
                 ] 
             ]
         )
         )


@Client.on_callback_query(filters.regex("admin"))
async def admin(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>Salam {query.from_user.mention}!\nBu botun adminler üçün Ərmlər menyusu🤩\n\n ▶️ /davam - musiqi oynatmaqa davam et\n ⏸️ /dayandir - oynayan treki duraklatmak üçün\n 🔄 /atla- Sıraya alınmış müsiqini atladır.\n ⏹ /son - müsiqi oynatmağı sonladırar\n 🔼 /ver botun sadecə yönətici üçün işlədilə bilən əmrləri işlədə bilməsi üçün kullancıya yetki ver\n 🔽 /al botun yönətici əmrləri işlədilə bilən kullancının yetkisini al\n\n ⚪ /assistantelavet - assistant qrubunuza qatılar.\n\n</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "🍁 Support 🍁", url="https://t.me/SOQrup")
                 ],
                 [
                     InlineKeyboardButton(
                         "⬅️ Geri ⬅️", callback_data="cbmelumat")
                 ] 
             ]
         )
         )


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(f"""**Salam {query.from_user.mention} 🎵\nMən {bot}!\nSəsli sohbətlərdə müsiqi oynada bilən botam. Qrupda admin hüquqları verməyiniz şərt..**""",
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
                        "🍁 Support 🍁", url="https://t.me/SOQrup"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📚 Əmrlər" , callback_data= "cbmelumat"
                    ),
                    InlineKeyboardButton(
                        "📱 Rəsmi Kanal ", url=f"https://t.me/ledyplaylist"
                    )
                ]
                
           ]
        ),
    )
