import heroku3
from functools import wraps
from config import HEROKU_API_KEY, HEROKU_APP_NAME


heroku_client = heroku3.from_key(HEROKU_API_KEY) if HEROKU_API_KEY else None


def check_heroku(func):
    @wraps(func)
    async def heroku_cli(client, message):
        heroku_app = None
        if not heroku_client:
            await message.reply_text(
                "`Bunun işləməsi üçün HEROKU_API_KEY Açarını əlavə edin!`",
                parse_mode="markdown",
            )
        elif not HEROKU_APP_NAME:
            await message.reply_text(
                "`Bunun işləməsi üçün lütfən HEROKU_APP_NAME Açarını əlavə edin!`",
                parse_mode="markdown",
            )
        if HEROKU_APP_NAME and heroku_client:
            try:
                heroku_app = heroku_client.app(HEROKU_APP_NAME)
            except:
                await message.reply_text(
                    message,
                    "`Heroku Api Açarı və Proqram Adı Uyğun deyil!`",
                    parse_mode="markdown",
                )
            if heroku_app:
                await func(client, message, heroku_app)

    return heroku_cli
