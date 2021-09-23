
# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
# EpicUserBot - ByMisakiMey - Erdembey

from datetime import datetime
from userbot import tgbot, bot
from telethon import events
from userbot import tgbot, OWNER_ID
from userbot.utils.events import register
import asyncio

@register(events.NewMessage(incoming=True, pattern="Mia"))
async def evnt (e):
    start = datetime.now()
    msg = await evnt.reply("Pong!")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await msg.edit(f"**Pong!!**\n `{ms} ms`")
    

