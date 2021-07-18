# Credit Vermeyi Unutmayın Zsten Açık Kaynaklı Kodlar
#Epicuserbot-Erdembey-ixelizm-ByMisakiMey

from telethon import events 
import asyncio 
from userbot.events import register as epic
from userbot import (MYID, CV_MSG, DEFAULT_NAME)
from userbot.cmdhelp import CmdHelp


@epic(incoming=True,pattern="^(.cv|cv)")
async def cvhazırlama(ups):
    if ups.fwd_from:
        return
    if ups.is_reply:
        reply = await ups.get_reply_message()
        replytext = reply.text
        reply_user = await ups.client.get_entity(reply.from_id)
        ren = reply_user.id
        if ren == MYID:
            await ups.reply(f"** {DEFAULT_NAME} CV-si:**\n {CV_MSG}")
        else:
            return
    else:
        return


@epic(outgoing=True, pattern="^.mycv") #Kendi CV-mizi Görmek İçin
async def komut(e):
 await e.edit(f"{CV_MSG}")
 


CmdHelp("cv").add_command(
	"cv",  "Herhangi biri sizi yanıtlayarak cv nizi görebilir."
	).add_command(
	"mycv", "Cv nizi kendiniz görüntülersiniz "
	).add_command(
        ".set var CV_MSG", "CV Mesajın"
).add()
