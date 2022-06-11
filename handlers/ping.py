from config import BOT_USERNAME


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]))
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("__pinging...__")
    delta_ping = time() - start
    await m_reply.edit_text("🏓 `PONG!!`\n" f"⚡️ `{delta_ping * 1000:.3f} ms`")
