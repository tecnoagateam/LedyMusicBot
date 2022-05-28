from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import BOT_USERNAME, BOT_NAME as bot
from helpers.filters import command, other_filters2
# EfsaneMusicVaves tarafından düzenlendi. 

@Client.on_message(command(["start", f"start@{BOT_USERNAME}", "ledy", f"ledy@{BOT_USERNAME}"]))
async def start(_, message: Message):
                await message.reply_photo(
                "https://telegra.ph/file/e669d8ec6be16f4b7cc39.jpg",
                caption=(f"""✧═════════•❀•═════════✧
**Salam {message.from_user.mention} Xoş gəldin!\nMən {bot}, Super Fast Music\nSəsli söhbətlərdə müsiqi yayınlaya bilən botam. Qrupda mənə admin hüquqları verməyi unutmayın.**    ✧═════════•❀•═════════✧
"""),
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🍁 ❰ Qrubuna Əlavə et ❱ 🍁", url=f"https://t.me/SSmusicLedy_bot?startgroup=melumat"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔊 Assistant", url="https://t.me/LedyMusicAssistant"
                    ),
                    InlineKeyboardButton(
                        "🛠️ Dəstək", url="https://t.me/SOQrup"
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
  


@Client.on_message(command(["melumat", f"melumat@{BOT_USERNAME}", "help", f"help@{BOT_USERNAME}"]))
async def bilgi(_, message: Message):
      await message.reply_text("\nBotun Aktiv işləməsi üçün aşağıdakı 3 yetkisi olmalıdır:\n- Mesaj silmə yetkisi,\n- Bağlantı ilə dəvət etmə yetkisi,\n- Səsli söhbəti yönətmə yetkisi.", 
      reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "🍁 Hərkəs üçün Əmrlər", callback_data="herkes")
                 ],[                     
                     InlineKeyboardButton(
                         "🧑‍✈️ Adminlər üçün Əmrlər", callback_data="admin")
                 ],[
                     InlineKeyboardButton(
                         "🏠 Ana menyu", callback_data="cbstart")
                 ],[
                     InlineKeyboardButton(
                         "🛠️ Dəstək", url="https://t.me/SOQrup")
                 ]
             ]
         )
    )


@Client.on_callback_query(filters.regex("cbmelumat"))
async def cbbilgi(_, query: CallbackQuery):
    await query.edit_message_text("\nBotun Aktiv işləməsi üçün aşağıdakı 3 yetkisi olmalıdır:\n- Mesaj silmə yetkisi,\n- Bağlantı ilə dəvət etmə yetkisi,\n- Səsli söhbəti yönətmə yetkisi.", 
    reply_markup=InlineKeyboardMarkup(
      [
        [
          InlineKeyboardButton(
            "🍁 Hərkəs üçün əmrlər 🍁", callback_data ="herkes")
        ],
        [
          InlineKeyboardButton(
            "🧑‍✈️ Admin Əmrləri 🧑‍✈️",callback_data ="admin")
        ],
        [
          InlineKeyboardButton(
            "🏠 Ana Menyu", callback_data="cbstart")
        ],
        [
          InlineKeyboardButton(
            "🛠️ Dəstək ", url="https://t.me/SOQrup")
        ]
      ]
     ))


@Client.on_callback_query(filters.regex("herkes"))
async def herkes(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>Salam {query.from_user.mention}!\nBu botun hərkəs üçün əmrlər menyusu:\n\n ▶️ /oynad <song name> - istədiyin musiqini dinlə\n  \n 🎵 /tap <song name> - istədiyin musiqini sürətli endir \n 🎥 /vtap istədiyin videonu sürətli endir\n 🔍 /axtar <query> - YouTube-dən video linkləri axtar \n\n</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "🛠️ Dəstək", url="https://t.me/SOQrup")
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
    await query.edit_message_text(f"""<b>Salam {query.from_user.mention}!\nBu botun adminler üçün Əmrlər menyusu:\n\n ▶️ /davam - musiqi oynatmağa davam et\n ⏸️ /dayandir - oynayan musiqini dayandırmaq üçün\n 🔄 /otur- Oynadılan müsiqini ötürür.\n ⏹ /son - müsiqi oynatmağı sonladırar\n 🔼 /ver botun sadecə yönətici üçün işlədilə bilən əmrləri işlədə bilməsi üçün kullancıya yetki ver\n 🔽 /al botun yönətici əmrləri işlədilə bilən kullancının yetkisini al\n ⚪ /assistantqosul - Assistant qrubunuza qatılar.\n /assistantcix - ⚫ Assistant Qrupunuzu tərk edər.\n\n</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "🛠️ Dəstək", url="https://t.me/SOQrup")
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
    await query.edit_message_text(f"""✧═════════•❀•═════════✧   **Salam {query.from_user.mention} Xoş gəldin!\nMən {bot}, Super Fast Music\nSəsli söhbətlərdə müsiqi yayınlaya bilən botam. Qrupda mənə admin hüquqları verməyi unutmayın.**    ✧═════════•❀•═════════✧""",
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🍁 ❰ Qrubuna Əlavə et ❱ 🍁", url=f"https://t.me/SSmusicLedy_bot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔊 Assistant", url="https://t.me/LedyMusicAssistant"
                    ),
                    InlineKeyboardButton(
                        "🛠️ Dəstək", url="https://t.me/SOQrup"
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
