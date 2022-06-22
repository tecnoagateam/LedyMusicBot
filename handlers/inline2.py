#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram.types import (InlineQueryResultArticle,
                            InputTextMessageContent)

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="Yayımı dayandır",
            description=f"Yayımı dayandır.",
            thumb_url="https://telegra.ph/file/c0a1c789def7b93f13745.png",
            input_message_content=InputTextMessageContent("/dayandir"),
        ),
        InlineQueryResultArticle(
            title="Yayıma davam",
            description=f"dayandırılan musiqini davam etdir.",
            thumb_url="https://telegra.ph/file/02d1b7f967ca11404455a.png",
            input_message_content=InputTextMessageContent("/davam"),
        ),
        InlineQueryResultArticle(
            title="Yayım Ötür",
            description=f"Müsiqini Növbəyə ötür",
            thumb_url="https://telegra.ph/file/98b88e52bc625903c7a2f.png",
            input_message_content=InputTextMessageContent("/otur"),
        ),
        InlineQueryResultArticle(
            title="Yayım Son",
            description="Yayımı dayandır Assistantı Səslidən ayır.",
            thumb_url="https://telegra.ph/file/d2eb03211baaba8838cc4.png",
            input_message_content=InputTextMessageContent("/son"),
        ),
    ]
)
