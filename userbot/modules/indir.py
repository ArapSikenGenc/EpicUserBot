from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.events import register
from userbot.cmdhelp import CmdHelp
from userbot import bot

# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value
LANG = get_value("indir")

# ████████████████████████████████ #

@register(outgoing=True, pattern="^.indir ?(.*)")
async def epicnsta(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("`Yüklemek için Link Verin`")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await event.edit("`Yüklemek İçin Link Verin`")
        return
    chat = "@SaveAsbot"
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("`Epic İndiremedi Bazı Hatalar Nedeniyle Başka Link Dene Be Tatlım ✓`")
        return
    asc = await event.edit("`Epic Yüklüyor Sabırlı Ol...`")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=523131145)
            )
            await event.client.send_message(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.edit(" @SaveAsBot `botunun Engelini Kaldırın Tekrar Deneyin")
            return
        if response.text.startswith("Forward"):
            await event.edit(
                "`Gizlilik ayarlarınızdakı ileti kismini düzeltin.`"
            )
        elif "Что поддерживается?" in response.text:
            await event.edit(
                "⛔️ `Bu linkin ne olduğu hakkında bir fikrim yok!`"
            )
        else:
            await event.delete()
            await event.client.send_file(
                event.chat_id,
                response.message.media,
                caption=f"@EpicUserBot `ile yüklendi`",
            )
            await event.client.send_read_acknowledge(conv.chat_id)
            

CmdHelp('indir').add_command('indir', None, LANG['İN2']).add_info(LANG['İN2']).add()