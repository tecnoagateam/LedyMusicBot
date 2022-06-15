import os
import shutil
import sys
import traceback
from functools import wraps
from os import environ, execle

import heroku3
import psutil
from config import BOT_USERNAME, HEROKU_API_KEY, HEROKU_APP_NAME
from helpers.decorators import sudo_users_only, humanbytes
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message


# Stats Of Your Bot
@Client.on_message(command(["stats"]))
@sudo_users_only
async def botstats(_, message: Message):
    total, used, free = shutil.disk_usage(".")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage("/").percent
    await message.reply_text(
        text=f"**📊 stats @{BOT_USERNAME}** \n\n**🤖 bot version:** `V.1.2` \n\n**💾 disk usage:** \n » **disk space:** `{total}` \n » **used:** `{used}({disk_usage}%)` \n » **free:** `{free}` \n\n**🎛 hardware usage:** \n » **CPU usage:** `{cpu_usage}%` \n » **RAM usage:** `{ram_usage}%`",
        parse_mode="Markdown",
        quote=True,
    )


@Client.on_message(command(["logs"]))
@sudo_users_only
@check_heroku
async def logswen(client: Client, message: Message, happ):
    msg = await message.reply_text("`please wait for a moment!`")
    logs = happ.get_log()
    capt = f"Heroku logs `{HEROKU_APP_NAME}`"
    await edit_or_send_as_file(logs, msg, client, capt, "logs")


# Set Heroku Var
@Client.on_message(command(["setvar"]))
@sudo_users_only
@check_heroku
async def setvar(client: Client, message: Message, app_):
    msg = await message.reply_text(message, "`zəhmət olamasa gozleyin...`")
    heroku_var = app_.config()
    _var = get_text(message)
    if not _var:
        await msg.edit("**usage:** `/setvar (var) (value)`")
        return
    if " " not in _var:
        await msg.edit("**usage:** `/setvar (var) (value)`")
        return
    var_ = _var.split(" ", 1)
    if len(var_) > 2:
        await msg.edit("**usage:** `/setvar (var) (value)`")
        return
    _varname, _varvalue = var_
    await msg.edit(f"**variable:** `{_varname}` \n**new value:** `{_varvalue}`")
    heroku_var[_varname] = _varvalue


# Delete Heroku Var
@Client.on_message(command(["delvar"]))
@sudo_users_only
@check_heroku
async def delvar(client: Client, message: Message, app_):
    msg = await message.reply_text(message, "`zəhmət olamasa gozleyin...!`")
    heroku_var = app_.config()
    _var = get_text(message)
    if not _var:
        await msg.edit("`var name silindi!`")
        return
    if _var not in heroku_var:
        await msg.edit("`yoxdur!`")
        return
    await msg.edit(f"sucessfully deleted var `{_var}`")
    del heroku_var[_var]
