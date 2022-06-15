import os
from os import getenv
from dotenv import load_dotenv
from helpers.uptools import fetch_heroku_git_url

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("SESSION_NAME", "AgAOWWIGqnaYhdAhyPxtZwdMSlsq9dbcvCE4ClbmncigNwP2_OaNenwDr0ThnmLmaTl1s6c694fzZgXDoCTUbosfc0T9CorC8l5Po8YgbqfArqiBLrPDADV3uJAGnCcXvrM6ERr5yzJaQg6xz")
BOT_TOKEN = getenv("BOT_TOKEN", "5146456073:AAFnPscOEytDNNuq8nEvch9moHVs0mFJ368")
BOT_NAME = getenv("BOT_NAME", "𝐋𝐄𝐃𝐘 𝐌𝐔𝐒𝐈𝐂") 
API_ID = int(getenv("API_ID", "18052289"))
API_HASH = getenv("API_HASH", "552525f45a3066fee54ca7852235c19c")
BOT_USERNAME = getenv("BOT_USERNAME", "SSmusicLedy_bot")
BOT_OWNER = getenv("BOT_OWNER", "1924693109")
PMPERMIT = getenv("PMPERMIT", "ENABLE")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "9999"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ . ! $ # 1 2 3 4 5 6 7 8 9 0 , aga ledy").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1924693109").split()))

#  ------------------------------------------------------------------------------------------------------------ 
#    Yeni güncellemede...


# DB_URL new mode -------ledyservic------

DATABASE_URL = getenv("DATABASE_URL")

# Log kanalı.... 
LOG_CHANNEL = getenv("LOG_CHANNEL")

# Support Channel/Group
SUPPORT_NAME = getenv("SUPPORT_NAME", "SOQrup")
CHANNEL_NAME = getenv("CHANNEL_NAME", "ledyplaylist")

#  ------------DahasiLedyServic--------------
