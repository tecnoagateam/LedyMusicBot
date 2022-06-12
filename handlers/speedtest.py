import wget
import speedtest

from config import BOT_USERNAME as bname
from pyrogram import Client, filters
from pyrogram.types import Message
from helpers.filters import command, other_filters

@Client.on_message(command(["speedtest", f"speedtest@{bname}"]))
async def run_speedtest(_, message: Message):
    m = await message.reply_text("⚡️ Serverlərdə sürətin yoxlanılması...")
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = await m.edit("⚡️ Yükləmə sürəti yoxlanılır...")
        test.download()
        m = await m.edit("⚡️ Yükləmə sürəti yüklənir...")
        test.upload()
        test.results.share()
        result = test.results.dict()
    except Exception as e:
        await m.edit(e)
        return
    m = await m.edit("💡 **Sürət Test Nəticələri**\n\n**ISP:** -\n**Ölkə:** -")
    path = wget.download(result["share"])

    output = f"""💡 **Sürət Test Nəticələri**
    
<u>**Ledy Bot:**</u>
**ISP:** {result['client']['isp']}
**Ölkə:** {result['client']['country']}
  
<u>**Ｓｅｒｖｅｒ:**</u>
**Ad:** {result['server']['name']}
**Ölkə:** {result['server']['country']}, {result['server']['cc']}
**Sponsor:** {result['server']['sponsor']}
**Gecikmə:** {result['server']['latency']}

⚡️ **Ｐｉｎｇ:** {result['ping']}"""
