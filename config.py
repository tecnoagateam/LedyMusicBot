import os
from os import getenv
from dotenv import load_dotenv
from helpers.uptools import fetch_heroku_git_url

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("SESSION_NAME", "AgBzq8m8g6enm3IArmNZ81UZz9syzUmNKgfFTI99hqDFnIKnBbEVH-2slzwGMYLZ5VL5s3pK5LE9dP24J4TZcXvERskJazsntNdSGlY07qOlPFS-nioscaK7o0by4lBNAEsbdOeWqDaIR232BiqO-dUARMHDE2GbT1V4Lm0BmQ3wzfHMtyqIwlKMpqV0O042EWDBkROx7X-ZgreXENYMa2j-M0cXvZqzPhjUk0upLHPoQUZ_w470cs4X5ImSoy8TihXzq2vyoGJR0v4XamVZk2YGEKRzI90mxMN4K2lHN1dWtqhfEkDdA_jzVNSzWU6eUeVuK8vAKCyr9S5GZs6InudeAAAAASysEsgA")
BOT_TOKEN = getenv("BOT_TOKEN", "5146456073:AAGapgoEgLVsamNA4038PpKkvanrz1h1VxM")
BOT_NAME = getenv("BOT_NAME", "𝐋𝐄𝐃𝐘 𝐌𝐔𝐒𝐈𝐂") 
API_ID = int(getenv("API_ID", "18052289"))
API_HASH = getenv("API_HASH", "552525f45a3066fee54ca7852235c19c")
BOT_USERNAME = getenv("BOT_USERNAME", "SSmusicLedy_bot")
BOT_OWNER = getenv("BOT_OWNER", "1924693109")
PMPERMIT = getenv("PMPERMIT", "ENABLE")
HEROKU_API_KEY = getenv("HEROKU_API_KEY", "")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", "")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "9999"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/tecnoagateam/LedyMusicBot")

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ . ! $").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1924693109").split()))

#  ------------------------------------------------------------------------------------------------------------ 
#    Yeni güncellemede...


# DB_URL new mode -------ledyservic------


# Log kanalı.... 
LOG_CHANNEL = getenv("LOG_CHANNEL")

# Support Channel/Group
SUPPORT_NAME = getenv("SUPPORT_NAME", "SOQrup")
CHANNEL_NAME = getenv("CHANNEL_NAME", "ledyplaylist")

#  ------------DahasiLedyServic--------------


#TECNO system+cpu+ram+GB=100%
