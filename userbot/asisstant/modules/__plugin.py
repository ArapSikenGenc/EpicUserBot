import re
import os
import sys
from telethon.tl.types import DocumentAttributeFilename, InputMessagesFilterDocument
import importlib
import time
import traceback

from userbot import CMD_HELP, bot, tgbot, PLUGIN_CHANNEL_ID, PATTERNS, BOTLOG, BOTLOG_CHATID, ASISTAN, MYID, DEFAULT_NAME
from telethon.tl.types import InputMessagesFilterDocument
from userbot.asisstant.events import epic
from userbot.main import extractCommands
import userbot.asisstant.cmdhelp
from userbot import OWNER_ID
# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value
LANG = get_value("__plugin")
LANGG = get_value("misc")

# ████████████████████████████████ #
SECURİTY = ["heroku", "STRING_SESSION", "HEROKU_APPNAME", "SESSION", "HEROKU_APIKEY", "API_HASH", "API_KEY", ".session.save", "EditBannedRequest", "ChatBannedRights", "kick_participiant", "ChatAdminRights", "replyAdminRequest"]
# Plugin Porter - UniBorg
@epic(incoming=True, from_users=OWNER_ID, pattern="^.pport")
async def pport(event):
    if event.is_reply:
        reply_message = await event.get_reply_message()
    else:
        asd = await event.reply(LANG["REPLY_FOR_PORT"])
        return

    await event.reply(LANG["DOWNLOADING"])
    dosya = await event.client.download_media(reply_message)
    dosy = open(dosya, "r").read()

    borg1 = r"(@borg\.on\(admin_cmd\(pattern=\")(.*)(\")(\)\))"
    borg2 = r"(@borg\.on\(admin_cmd\(pattern=r\")(.*)(\")(\)\))"
    borg3 = r"(@borg\.on\(admin_cmd\(\")(.*)(\")(\)\))"

    if re.search(borg1, dosy):
        await event.reply(LANG["UNIBORG"])
        komu = re.findall(borg1, dosy)

        if len(komu) > 1:
            await event.reply(LANG["TOO_MANY_PLUGIN"])

        komut = komu[0][1]
        degistir = dosy.replace('@borg.on(admin_cmd(pattern="' + komut + '"))', '@register(outgoing=True, pattern="^.' + komut + '")')
        degistir = degistir.replace("from userbot.utils import admin_cmd", "from userbot.events import register")
        degistir = re.sub(r"(from uniborg).*", "from userbot.events import register", degistir)
        degistir = degistir.replace("def _(event):", "def port_" + komut + "(event):")
        degistir = degistir.replace("borg.", "event.client.")
        ported = open(f'port_{dosya}', "w").write(degistir)

        await event.reply(LANG["UPLOADING"])

        await event.client.send_file(event.chat_id, f"port_{dosya}")
        os.remove(f"port_{dosya}")
        os.remove(f"{dosya}")
    elif re.search(borg2, dosy):
        await event.reply(LANG["UNIBORG2"])
        komu = re.findall(borg2, dosy)

        if len(komu) > 1:
            await event.reply(LANG["TOO_MANY_PLUGIN"])
            return

        komut = komu[0][1]

        degistir = dosy.replace('@borg.on(admin_cmd(pattern=r"' + komut + '"))', '@register(outgoing=True, pattern="^.' + komut + '")')
        degistir = degistir.replace("from userbot.utils import admin_cmd", "from userbot.events import register")
        degistir = re.sub(r"(from uniborg).*", "from userbot.events import register", degistir)
        degistir = degistir.replace("def _(event):", "def port_" + komut + "(event):")
        degistir = degistir.replace("borg.", "event.client.")
        ported = open(f'port_{dosya}', "w").write(degistir)

        await event.reply(LANG["UPLOADING"])

        await event.client.send_file(event.chat_id, f"port_{dosya}")
        os.remove(f"port_{dosya}")
        os.remove(f"{dosya}")
    elif re.search(borg3, dosy):
        await event.reply(LANG["UNIBORG3"])
        komu = re.findall(borg3, dosy)

        if len(komu) > 1:
            await event.reply(LANG["TOO_MANY_PLUGIN"])
            return

        komut = komu[0][1]

        degistir = dosy.replace('@borg.on(admin_cmd("' + komut + '"))', '@register(outgoing=True, pattern="^.' + komut + '")')
        degistir = degistir.replace("from userbot.utils import admin_cmd", "from userbot.events import register")
        degistir = re.sub(r"(from uniborg).*", "from userbot.events import register", degistir)
        degistir = degistir.replace("def _(event):", "def port_" + komut.replace("?(.*)", "") + "(event):")
        degistir = degistir.replace("borg.", "event.client.")

        ported = open(f'port_{dosya}', "w").write(degistir)

        await event.reply(LANG["UPLOADING"])

        await event.client.send_file(event.chat_id, f"port_{dosya}")
        os.remove(f"port_{dosya}")
        os.remove(f"{dosya}")

    else:
        await event.reply(LANG["UNIBORG_NOT_FOUND"])

@epic(incoming=True, from_users=OWNER_ID, pattern="^.plist")
async def plist(event):
    if PLUGIN_CHANNEL_ID != None:
        await event.reply(LANG["PLIST_CHECKING"])
        yuklenen = f"{LANG['PLIST']}\n\n"
        async for plugin in event.client.iter_messages(PLUGIN_CHANNEL_ID, filter=InputMessagesFilterDocument):
            try:
                dosyaismi = plugin.file.name.split(".")[1]
            except:
                continue

            if dosyaismi == "py":
                yuklenen += f"🌈 {plugin.file.name}\n"
        try:
            await event.reply(yuklenen)
        except:
            await event.reply(yuklenen)
    else:
        try:
            await event.reply(LANG["TEMP_PLUGIN"])
        except:
            await event.reply(LANG["TEMP_PLUGIN"])



@epic(incoming=True, from_users=OWNER_ID, pattern="^.pinstall")
async def pins(event):
    if event.is_reply:
        reply_message = await event.get_reply_message()
    else:
        await event.reply(LANG["REPLY_TO_FILE"])
        return

    await event.reply(LANG["DOWNLOADING"])
    edizin = f"./userbot/asisstan/modules{reply_message.file.name}"
    
    if os.path.exists(edizin):
        await event.reply(LANG["ALREADY_INSTALLED"])
        return

    dosyaAdi = reply_message.file.name
  #  plugins = await event.client.get_messages('@epicplugin', limit=None, search=dosyaAdi, filter=InputMessagesFilterDocument)

  #  if len(plugins) == 0:
   #     await event.reply('🍕 `Pizzamı yemeye devam edeceğim. Bu bir Epic Plugini değil!`')
 #       return

    dosya = await event.client.download_media(reply_message, "./userbot/asisstant/modules/")

    try:
        spec = importlib.util.spec_from_file_location(dosya, dosya)
        mod = importlib.util.module_from_spec(spec)

        spec.loader.exec_module(mod)
    except Exception as e:
        await event.reply(f"{LANG['PLUGIN_BUGGED']} {e}`")
        return os.remove("./userbot/asisstant/modules/" + dosya)
    plugin = await event.get_reply_message()
    dosy = open(dosya, "r").read()
    for S in SECURİTY:
      if re.search(S, dosy):
         os.remove(dosya)
         return await event.reply(f"**❌ Güvenlik Uyarısı ❌** \n{plugin.file.name} dosyasında (`{S}`) değeri bulundu. \n\n **Bu Dosya Senin Verilerini Tehlikeye Atmaktadır Sayın `{DEFAULT_NAME}` Lütfen Bunu Yükleme**")
    if re.search(r"@tgbot\.on\(.*pattern=(r|)\".*\".*\)", dosy):
        komu = re.findall(r"\(.*pattern=(r|)\"(.*)\".*\)", dosy)
        komutlar = ""
        i = 0
        while i < len(komu):
            komut = komu[i][1]
            CMD_HELP["tgbot_" + komut] = f"{LANG['PLUGIN_DESC']} {komut}"
            komutlar += komut + " "
            i += 1
        await event.reply(LANG['PLUGIN_DOWNLOADED'] % komutlar)
    else:
        Pattern = re.findall(r"@register\(.*pattern=(r|)\"(.*)\".*\)", dosy)

        if (not type(Pattern) == list) or (len(Pattern) < 1 or len(Pattern[0]) < 1):
            if re.search(r'CmdHelp\(.*\)', dosy):
                cmdhelp = re.findall(r"CmdHelp\([\"'](.*)[\"']\)", dosy)[0]
                await event.client.download_media(reply_message, "./userbot/asisstant/modules/")
                return await event.reply(f'**Modül Başarıyla Yüklendi!**\n__Modülün Kullanımını Öğrenmek İçin__ `.epic {cmdhelp}` __yazın.__')
            else:
                await event.client.download_media(reply_message, "./userbot/asisstant/modules/")
                userbot.cmdhelp.CmdHelp(dosya).add_warning('Komutlar bulunamadı!').add()
                return await event.reply(LANG['PLUGIN_DESCLESS'])
        else:
            if re.search(r'CmdHelp\(.*\)', dosy):
                cmdhelp = re.findall(r"CmdHelp\([\"'](.*)[\"']\)", dosy)[0]
                await event.client.download_media(reply_message, "./userbot/asisstant/modules/")
                return await event.reply(f'**Modül Başarıyla Yüklendi!**\n__Modülün Kullanımını Öğrenmek İçin__ `.epic {cmdhelp}` __yazın.__')
            else:
                dosyaAdi = reply_message.file.name.replace('.py', '')
                extractCommands(dosya)
                await event.client.download_media(reply_message, "./userbot/asisstant/modules/")
                return await event.reply(f'**Modül Başarıyla Yüklendi**\n__Modülün  Kullanımını Öğrenmek İçin__ `.epic {dosyaAdi}` __yazın.__')

"""@epic(incoming=True, from_users=OWNER_ID, pattern="^.ptest")
async def ptest(event):
    if event.is_reply:
        reply_message = await event.get_reply_message()
    else:
        await event.reply(LANG["REPLY_TO_FILE"])
        return

    await event.reply(LANG["DOWNLOADING"])
    if not os.path.exists('./userbot/asisstant/temp_plugins/'):
        os.makedirs('./userbot/asisstant/temp_plugins')
    dosya = await event.client.download_media(reply_message, "./userbot/temp_plugins/")
    
    try:
        spec = importlib.util.spec_from_file_location(dosya, dosya)
        mod = importlib.util.module_from_spec(spec)

        spec.loader.exec_module(mod)
    except Exception as e:
        await event.reply(f"{LANG['PLUGIN_BUGGED']} {e}`")
        return os.remove("./userbot/temp_plugins/" + dosya)
    plugin = await event.get_reply_message()
    dosy = open(dosya, "r").read()
    for S in SECURİTY:
     if re.search(S, dosy):
         os.remove(dosya)
         return await event.reply(f"**❌ Güvenlik Uyarısı ❌** \n{plugin.file.name} dosyasında (`{S}`) değeri bulundu. \n\n **Bu Dosya Senin Verilerini Tehlikeye Atmaktadır Sayın `{DEFAULT_NAME}` Lütfen Bunu Yükleme**")
    return await event.reply(f'**Modül Başarıyla Yüklendi!**\
    \n__Modülü Test Edebilirsiniz. Botu yeniden başlattığınızda plugin silinecektir.__')"""

@epic(incoming=True, from_users=OWNER_ID, pattern="^.psend ?(.*)")
async def psend(event):
    modul = event.pattern_match.group(1)
    if len(modul) < 1:
        await event.reply(LANG['PREMOVE_GIVE_NAME'])
        return

    if os.path.isfile(f"./userbot/modules/{modul}.py"):
        await event.client.send_file(event.chat_id, f"./userbot/modules/{modul}.py", caption=LANG['EPİC_PLUGIN_CAPTION'])
        await event.delete()
    else:
        await event.reply(LANG['NOT_FOUND_PLUGIN'])


@epic(incoming=True, from_users=OWNER_ID, pattern="^.premove ?(.*)")
async def premove(event):
    modul = event.pattern_match.group(1).lower()
    if len(modul) < 1:
        await event.reply(LANG['PREMOVE_GIVE_NAME'])
        return

    await event.reply(LANG['PREMOVE_DELETING'])
    i = 0
    a = 0
    async for message in event.client.iter_messages("./userbot/asisstant/modules/", filter=InputMessagesFilterDocument, search=modul):
        await message.delete()
        try:
            os.remove(f"./userbot/asisstant/modules/{message.file.name}")
        except FileNotFoundError:
            await event.reply(LANG['ALREADY_DELETED'])

        i += 1
        if i > 1:
            break

    if i == 0:
        await event.reply(LANG['NOT_FOUND_PLUGIN'])
    else:
        await event.reply(LANG['PLUG_DELETED'])
        time.sleep(2) 
        await event.reply(LANGG['RESTARTING'])
        try: 
            if BOTLOG:
                await event.client.send_message(BOTLOG_CHATID, "#OTORESTART \n"
                                        "Plugin silme sonrası bot yeniden başlatıldı.")

            await tgbot.disconnect()
        except:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)





