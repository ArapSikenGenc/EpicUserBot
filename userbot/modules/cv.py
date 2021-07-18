# Credit Vermeyi Unutmayın Zsten Açık Kaynaklı Kodlar
#Epicuserbot-Erdembey-ixelizm-ByMisakiMey

from telethon import events 
import asyncio 
from userbot.events import register as epic
from userbot import (MYID)
from userbot.main import PLUGIN_MESAJLAR
from userbot.cmdhelp import CmdHelp

@epic(incoming=True, pattern="^.cv")
async def cvhazırlama(ups):
    if ups.fwd_from:
        return
    if ups.is_reply:
        reply = await ups.get_reply_message()
        replytext = reply.text
        reply_user = await ups.client.get_entity(reply.from_id)
        ren = reply_user.id
        if ren == MYID:
            await ups.reply(f"{PLUGIN_MESAJLAR['cv']}")
		        
@epic(outgoing=True, pattern="^.mycv")
async def komut(e):
        await e.edit(f"{PLUGIN_MESAJLAR['cv']}")

CmdHelp("cv").add_command(
	"cv",  "Herhangi biri sizi yanıtlayarak cv nizi görebilir."
	).add_command(
	"mycv", "Cv nizi kendiniz görüntülersiniz "
	).add_command(
	".değiştir cv", "cv-nizi değiştirmek için"
).add()
