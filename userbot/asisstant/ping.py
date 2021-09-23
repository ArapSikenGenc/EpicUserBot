
# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
# EpicUserBot - ByMisakiMey - Erdembey


from datetime import datetime
from userbot import OWNER_ID, tgbot

@tgbot.on(NewMessage(pattern='/ping'))
async def _(event):
 if event.sender_id in OWNER_ID:
    start = datetime.now()
    msg = await event.reply("Pong!")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await msg.edit(f"**Pong!!**\n `{ms} ms`")
