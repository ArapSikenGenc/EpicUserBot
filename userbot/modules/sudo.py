# HydraDev Erdem Bey ByMisakimey

import os
import re
from userbot.cmdhelp import CmdHelp
from userbot.events import register
from userbot import (
    HEROKU_APPNAME,
    HEROKU_APIKEY,
    SUDO_ID,
    bot,
)
import heroku3
from telethon.tl.functions.users import GetFullUserRequest

Heroku = heroku3.from_key(HEROKU_APIKEY)
heroku_api = "https://api.heroku.com"
epicsudo = os.environ.get("SUDO_ID", None)


@register(outgoing=True,
          pattern=r"^.sudoekle")
async def addsudo(event):
    await event.edit("`Kullanıcı sudo olarak ayarlanıyor`...")
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
        await event.edit("`Lütfen bir kullanıcının mesajına cevap verin.`")
    if epicsudo:
        yenisudo = f"{epicsudo} {epictext}"
    else:
        yenisudo = f"{epictext}"
    await event.edit("`Kullanıcı sudo olarak ayarlandı.👌` \n`Botunuz yeniden başlatılıyor...`")
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

@register(outgoing=True,
          pattern=r"^.sudosil")
async def sudosil(event):
  Heroku = heroku3.from_key(HEROKU_APIKEY)
  app = Heroku.app(HEROKU_APPNAME)
  heroku_var = app.config()
  if not event.is_reply:
    return await event.edit("`Lütfen bir kullanıcının mesajına cevap verin.`")
  if event.is_reply:
    id = (await event.get_reply_message()).sender_id
    ad = (await bot.get_entity(id)).first_name
    op = re.search(str(id), str(epicsudo))
    if op:
      i = ""
      esudo = epicsudo.split(" ")
      esudo.remove(str(id))
      i += str(esudo)
      x = i.replace("[", "")
      xx = x.replace("]", "")
      xxx = xx.replace(",", "")
      hazir = xxx.replace("'", "")
      heroku_var["SUDO_ID"] = hazir
      await event.edit(f"`{ad}``Artık Sudo değil 👌.`\n`Botunuz yeniden başlatılıyor...`")
    else:
      await event.edit(f"`Kusura bakma,` `{ad}` `Zaten Bir Sudo Değil!`")
    if heroku_var["SUDO_ID"] == None:
       await event.edit(f"`Sudo Bulunmamaktadır!`") 
    

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
    epict = replied_user.user.id
    return epict
    
@register(incoming=True, from_users=SUDO_ID, pattern="^.salive$")
async def _(q):
    await q.client.send_message(q.chat_id,"`Sudom ❤️ EpicUserBot Çalışıyor...`")

CmdHelp('sudo').add_command(
    'salive', None, 'Sudonun aktif olup olmadığını kontrol eder.'
    ).add_command(
    'sudoekle', None, 'Mesajına cevap verdiğiniz kullanıcını botunuzda sudo yapar.'
    ).add_command(
    'sudosil', None, 'Mesajına cevap verdiğiniz kullanıcının botunuzda sudoluğunu siler.'
    ).add_command(
        'sdemote', '<kullanıcı adı/yanıtlama>', 'Sohbetteki kişinin yönetici izinlerini iptal eder.'
    ).add_command(
        'sban', '<kullanıcı adı/yanıtlama> <nedeni (isteğe bağlı)>', 'Sohbetteki kişiyi susturur, yöneticilerde de çalışır.'
    ).add_command(
        'sunban', '<kullanıcı adı/yanıtlama>', 'Sohbetteki kişinin yasağını kaldırır.'
    ).add_command(
        'skick', '<kullanıcı adı/yanıtlama> <nedeni (isteğe bağlı)>', 'Gruptan belirttiğiniz kişiyi tekmeler.'
    ).add_command(
        'sgmute', '<kullanıcı adı/yanıtlama> <nedeni (isteğe bağlı)>', 'Kişiyi yönetici olduğunuz tüm gruplarda susturur.'
    ).add_command(
        'sungmute', '<kullanıcı adı/yanıtlama>', 'Kişiyi küresel olarak sessize alınanlar listesinden kaldırır.'
    ).add_command(
        'sgban', '<kullanıcı adı/yanıtlama>', 'Kullanıcıyı küresel olarak yasaklar.'
    ).add_command(
        'sungban', '<kullanıcı adı/yanıtlama>', 'Kullanıcının küresel yasaklamasını kaldırır.'
    ).add_command(
        'spromote', '<kullanıcı adı/yanıtlama> <özel isim (isteğe bağlı)>', 'Sohbetteki kişiye yönetici hakları sağlar.'
    ).add()
