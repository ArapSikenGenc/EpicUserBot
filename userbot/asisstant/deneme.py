from userbot import tgbot
import asyncio
from telethon import events
@tgbot.on(events.NewMessage(incoming=True, pattern="deneme"))
async def evnt (e):
    await e.reply("DENEME")

