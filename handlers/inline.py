from pyrogram.handlers import InlineQueryHandler
from youtubesearchpython import VideosSearch
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent
from pyrogram import Client, errors


@Client.on_inline_query()
async def search(client, query):
    answers = []
    string = query.query.lower().strip().rstrip()

    if string == "":
        await client.answer_inline_query(
            query.id,
            results=answers,
            switch_pm_text=("YouTube'dən video axtar..."),
            switch_pm_parameter="melumat",
            cache_time=0
        )
        return
    else:
        videosSearch = VideosSearch(string.lower(), limit=999999999999)
        for v in videosSearch.result()["result"]:
            answers.append(
                InlineQueryResultArticle(
                    title=v["title"],
                    description=("Duration: {} Views: {}").format(
                        v["duration"],
                        v["viewCount"]["short"]
                    ),
                    input_message_content=InputTextMessageContent(
                        "`/oynad https://www.youtube.com/watch?v={}`".format(
                            v["id"]
                        )
                    ),
                    thumb_url=v["thumbnails"][0]["url"]
                )
            )
        try:
            await query.answer(
                results=answers,
                cache_time=0
            )
        except errors.QueryIdInvalid:
            await query.answer(
                results=answers,
                cache_time=0,
                switch_pm_text=("Heçnə tapmadım"),
                switch_pm_parameter="start",
            )


__handlers__ = [
    [
        InlineQueryHandler(
            search
        )
    ]
]
