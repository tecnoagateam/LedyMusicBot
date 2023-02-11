import aiohttp
from pyrogram import filters
from pyrogram import Client


@Client.on_message(filters.command('git'))
async def github(_, message):
    if len(message.command) != 2:
        await message.reply_text("**Github User Haqqında Məlumat:**\n\n Nümunə: `/git tecnoagateam`")
        return
    username = message.text.split(None, 1)[1]
    URL = f'https://api.github.com/users/{username}'
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.reply_text("404")

            result = await request.json()
            try:
                url = result["html_url"]
                name = result["name"]
                company = result["company"]
                bio = result["bio"]
                created_at = result["created_at"]
                avatar_url = result["avatar_url"]
                blog = result["blog"]
                location = result["location"]
                repositories = result["public_repos"]
                followers = result["followers"]
                following = result["following"]
                caption = f"""**Github Məlumat:** __{name}__
**🧸 Ad:** `{username}`
**💌 Bio:** `{bio}`
**🔗 Profil Link:** [Here]({url})
**⛱ Company:** `{company}`
**🗓 Created On:** `{created_at}`
**🧰 Repositories:** `{repositories}`
**🎓 Blog:** `{blog}`
**📍 Location:** `{location}`
**💡 Followers:** `{followers}`
**📡 Following:** `{following}`"""
            except Exception as e:
                print(str(e))
    await message.reply_photo(photo=avatar_url, caption=caption)
