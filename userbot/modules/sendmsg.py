"""
Erdem Bey / EpicUserBot Modul birleştirmesi
"""
import re
import os
from telethon import events
from userbot import bot
from userbot.events import register
from userbot.cmdhelp import CmdHelp

# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value
LANG = get_value("afk")

# ████████████████████████████████ #
@register(outgoing=True, pattern="^.send ?(.*)")
async def pm(event):
 
    p = event.pattern_match.group(1)
    m = p.split(" ")

    chat_id = m[0]
    try:  
        chat_id = int(chat_id)
    except BaseException:
        
        pass
  
    msg = ""
    mssg = await event.get_reply_message() 
    if event.reply_to_msg_id:
        await event.client.send_message(chat_id, mssg)
        await event.edit("@EpicUserBot `Mesajı gönderdi ✔️`")
    for i in m[1:]:
        msg += i + " "
    if msg == "":
        return
    try:
        await event.client.send_message(chat_id, msg)
        await event.edit("@EpicUserBot `Mesajı gönderdi ✔️`")
    except BaseException:
        await event.edit("** @EpicUserBot Mesajınızı Gönderemedi :(**")
        
CmdHelp('sendmsg').add_command(
    'send', '.pmyaz <kullanıcı/grup/kanal/bot linki> <mesajınız>', 'Yazdığınız mesajı veya yanıtladığınız mesajı belirttiğiniz linke gönderir', '.send @epicuserbot selam'
).add()
