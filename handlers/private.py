from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import BOT_USERNAME, BOT_NAME as bot
from helpers.filters import command, other_filters2
# EfsaneMusicVaves tarafından düzenlendi. 

@Client.on_message(command(["start", f"start@{BOT_USERNAME}", "ledy", f"ledy@{BOT_USERNAME}"]))
async def start(_, message: Message):
                await message.reply_photo(
                "https://telegra.ph/file/4afbb46f4899c16317607.jpg",
                caption=(f"""✧═════════•❀•═════════✧
**Salam {message.from_user.mention} Xoş gəldin!\nMən {bot}, 𝑺𝒖𝒑𝒆𝒓 𝑭𝒂𝒔𝒕 𝑴𝒖𝒔𝒊𝒄\nSəsli söhbətlərdə müsiqi yayınlaya bilən botam. Qrupda mənə admin hüquqları verməyi unutmayın.**    ✧═════════•❀•═════════✧
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
async def melumat(_, message: Message):
      await message.reply_text("\nBotun Aktiv işləməsi üçün aşağıdakı 3 yetkisi olmalıdır:\n- Mesaj silmə yetkisi,\n- Bağlantı ilə dəvət etmə yetkisi,\n- Səsli söhbəti yönətmə yetkisi.", 
      reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "🍁 Hərkəs üçün Əmrlər", callback_data="herkes")
                 ],[                     
                     InlineKeyboardButton(
                         "🧑‍✈️ Adminlər üçün Əmrlər", callback_data="owner")
                 ],[                     
                     InlineKeyboardButton(
                         "😻 Tagger Modulu [BETA]", callback_data="tagger")
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
async def cbmelumat(_, query: CallbackQuery):
    await query.edit_message_text("\nBotun Aktiv işləməsi üçün aşağıdakı 3 yetkisi olmalıdır:\n- Mesaj silmə yetkisi,\n- Bağlantı ilə dəvət etmə yetkisi,\n- Səsli söhbəti yönətmə yetkisi.", 
    reply_markup=InlineKeyboardMarkup(
      [
        [
          InlineKeyboardButton(
            "🍁 Hərkəs üçün əmrlər 🍁", callback_data ="herkes")
        ],
        [
          InlineKeyboardButton(
            "🧑‍✈️ Admin Əmrləri 🧑‍✈️",callback_data ="owner")
        ],
        [
          InlineKeyboardButton(
            "😻 Tagger Modulu 😻",callback_data ="tagger")
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
                         "⬅️ Geri", callback_data="cbmelumat")
                 ] 
             ]
         )
         )


@Client.on_callback_query(filters.regex("owner"))
async def owner(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>Salam {query.from_user.mention}!\nBu Botun Adminlər Üçün Əmrlər Menyusu:\n\n ⏸️ /dayandir - Yayınlanan musiqini dayandır\n ▶️ /davam - Musiqi yayınlamağa davam et\n 🔄 /otur - Növbədê olan musiqiyə ötur\n ⏹ /son - Musiqi yayınlamağı sonlandır\n 🔼 /ver Kullancıya yetki ver\n 🔽 /al Yetki verilmiş Kullancının yetkisini al\n ❤️ /assistantqosul - Assistant Qrupa qoşular\n 🖤 /assistantcix - Assistant Qrupu tərk edər.\n\n</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "🛠️ Dəstək", url="https://t.me/SOQrup")                           
                 ],
                 [
                     InlineKeyboardButton(
                         "⬅️ Geri", callback_data="cbmelumat")
                 ] 
             ]
         )
         )


@Client.on_callback_query(filters.regex("tagger"))
async def tagger(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>Salam {query.from_user.mention}!\nBu botun userləri Tağ etmək üçün Əmrlər menyusu:\n Nəzərinizə çatdırım ki, Bu modül [beta] versiadadır, Hələ Dərc edilmiyib.\n\n /ledytag - userləri beşli tağ edər.\n\n</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "🛠️ Dəstək", url="https://t.me/SOQrup")
                 ],
                 [
                     InlineKeyboardButton(
                         "⬅️ Geri", callback_data="cbmelumat")
                 ] 
             ]
         )
         )


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(f"""✧═══════•❀•═══════✧     **Salam {query.from_user.mention} Xoş gəldin!\nMən {bot}, 𝑺𝒖𝒑𝒆𝒓 𝑭𝒂𝒔𝒕 𝑴𝒖𝒔𝒊𝒄\nSəsli söhbətlərdə müsiqi yayınlaya bilən botam. Qrupda mənə admin hüquqları verməyi unutmayın.**    ✧═══════•❀•═══════✧""",
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
