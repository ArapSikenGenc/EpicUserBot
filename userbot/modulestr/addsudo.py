import os
from userbot.cmdhelp import CmdHelp
from userbot.events import register
from userbot import (
    HEROKU_APPNAME,
    HEROKU_APIKEY,
    SUDO_ID
)
import heroku3
from telethon.tl.functions.users import GetFullUserRequest

Heroku = heroku3.from_key(HEROKU_APIKEY)
heroku_api = "https://api.heroku.com"
epicsudo = os.environ.get("SUDO_ID", None)


@register(outgoing=True,
          pattern=r"^.sudoekle")
async def addsudo(event):
    await event.edit("Kullanıcı sudo olarak ayarlanıyor...")
    epic = "SUDO_ID"
    if HEROKU_APPNAME is not None:
        app = Heroku.app(HEROKU_APPNAME)
    else:
        await event.edit("HEROKU:" "\nLütfen **HEROKU_APPNAME** değerini tanımlayın.")
        return
    heroku_var = app.config()
    if event is None:
        return
    try:
        epictext = await get_user(event)
    except Exception:
        await event.edit("Lütfen bir kullanıcının mesajına cevap verin.")
    if epicsudo:
        yenisudo = f"{epicsudo} {epictext}"
    else:
        yenisudo = f"{epictext}"
    await event.edit("Kullanıcı sudo olarak ayarlandı!\nBotunuz yeniden başlatılıyor...")
    heroku_var[epic] = yenisudo


async def get_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.forward:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.forward.sender_id)
            )
        else:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.sender_id)
            )
    epictext = replied_user.user.id
    return epictext
    
    
Help = CmdHelp('sudoekle')
Help.add_command('sudoekle', None, 'Mesajına cevap verdiğiniz kullanıcını botunuzda admin yapar.')
Help.add_info('@faridxz tarafından @EpicUserBot için hazırlanmıştır.')
Help.add()
