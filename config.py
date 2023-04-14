import os
from os import getenv
from dotenv import load_dotenv
from helpers.uptools import fetch_heroku_git_url

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("SESSION_NAME", "AgClBHUsSGWhIN-lgq5LuPS3NZPOI2q-dwRHF6DMzVdRfm5yBzLcJqXSlEZdf0iLIMFcC2YVEr9M1hFc2vx2QKxRgSvhCSSu79YeY_H7qJ4vz_ScnoIjs2kmGVd6RcUERrCNECQvyhk_qZiqjgk5n3JNzQNUPztt5ynK-HbHYwQx8tF3DdQPFI-mRIfzJnsdoTGMX_Yin7cG7XjF-nXV5tmEFPL0scIl_VCrVm4Ezgm8d9U9ThMoga-Ptxhl1hlSQvQNThdioVbVN3cMhC9QC_0278J8GCqy2EyOi_w2CkImQznsQpchozdSeONHrZwCmBi_tkZzVGnV9yHqrd-wM660Wp7lFQA")
BOT_TOKEN = getenv("BOT_TOKEN", "6254171749:AAFn9tbZaVK4nTuhAbYX6mVqzVPYpJ-YdNk")
BOT_NAME = getenv("BOT_NAME", "NILAY MUSİC") 
API_ID = int(getenv("API_ID", "18052289"))
API_HASH = getenv("API_HASH", "552525f45a3066fee54ca7852235c19c")
BOT_USERNAME = getenv("BOT_USERNAME", "nilaymusicbot")
BOT_OWNER = getenv("BOT_OWNER", "1924693109")
PMPERMIT = getenv("PMPERMIT", "ENABLE")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/AzeMusic/LedyMusicBot")

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ . ! $ # ledy").split())

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
