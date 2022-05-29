from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("SESSION_NAME", "AgAOWWIGqnaYhdAhyPxtZwdMSlsq9dbcvCE4ClbmncigNwP2_OaNenwDr0ThnmLmaTl1s6c694fzZgXDoCTUbosfc0T9CorC8l5Po8YgbqfArqiBLrPDADV3uJAGnCcXvrM6ERr5yzJaQg6xz")
BOT_TOKEN = getenv("BOT_TOKEN", "5146456073:AAFnPscOEytDNNuq8nEvch9moHVs0mFJ368")
BOT_NAME = getenv("BOT_NAME", "𝑳𝒆𝒅𝒚") 
API_ID = int(getenv("API_ID", "18052289"))
API_HASH = getenv("API_HASH", "552525f45a3066fee54ca7852235c19c")
BOT_USERNAME = getenv("BOT_USERNAME", "SSmusicLedy_bot")
PMPERMIT = getenv("PMPERMIT", "ENABLE")
HEROKU_API_KEY = getenv("HEROKU_API_KEY", "ef098244-4921-434d-bd7a-172f4315fed0")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "9999"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ . ! $ # 1 2 3 4 5 6 7 8 9 0 , aga ledy").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1924693109").split()))
