from userbot import tgbot
import asyncio

@tgbot.on(events.NewMessage(incoming=True, pattern="[Aa]sistan"))
async def evnt (e):
    await e.reply("DENEME")

