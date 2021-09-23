from requests import get
import sys
from asyncio import create_subprocess_shell as asyncsubshell
from asyncio import subprocess as asyncsub
from os import remove
from time import gmtime, strftime
from traceback import format_exc
from telethon import events

from userbot import tgbot, PATTERNS, EPİC_VERSION


def register(**args):
    """ Yeni bir etkinlik kaydedin. """
    pattern = args.get('pattern', None)
    disable_edited = args.get('disable_edited', False)
    groups_only = args.get('groups_only', False)
    trigger_on_fwd = args.get('trigger_on_fwd', False)
    trigger_on_inline = args.get('trigger_on_inline', False)
    disable_errors = args.get('disable_errors', False)

    if pattern:
        args["pattern"] = pattern.replace("^.", "^["+ PATTERNS + "]")
    if "disable_edited" in args:
        del args['disable_edited']

    if "ignore_unsafe" in args:
        del args['ignore_unsafe']

    if "groups_only" in args:
        del args['groups_only']

    if "disable_errors" in args:
        del args['disable_errors']

    if "trigger_on_fwd" in args:
        del args['trigger_on_fwd']
      
    if "trigger_on_inline" in args:
        del args['trigger_on_inline']

    def decorator(func):
        async def wrapper(check):
            try:
                await func(check)
                

            except events.StopPropagation:
                raise events.StopPropagation
            except KeyboardInterrupt:
                pass
            except BaseException:
                if not disable_errors:
                    date = strftime("%Y-%m-%d %H:%M:%S", gmtime())

                    eventtext = str(check.text)
                    text = "**==ASİSTAN HATA RAPORU==**\n"
                    link = "[Epic Destek Grubuna](https://t.me/HydraDestek)"
                    if len(eventtext)<10:
                        text += f"\n**🗒️ Şu yüzden:** {eventtext}\n"
                    text += "\nℹ️ İsterseniz, bunu bildirebilirsiniz."
                    text += f"- sadece bu mesajı {link} gönderin.\n"
                    text += "Hata ve tarih haricinde hiçbir şey kayıt edilmez.\n"

                    ftext = "========== UYARI =========="
                    ftext += "\nBu dosya sadece burada yüklendi,"
                    ftext += "\nSadece hata ve tarih kısmını kaydettik,"
                    ftext += "\nGizliliğinize saygı duyuyoruz,"
                    ftext += "\nBurada herhangi bir gizli veri varsa"
                    ftext += "\nBu hata raporu olmayabilir, kimse verilerinize ulaşamaz.\n"
                    ftext += "--------ASİSTAN HATA GUNLUGU--------\n"
                    ftext += "\nTarih: " + date
                    ftext += "\nGrup ID: " + str(check.chat_id)
                    ftext += "\nGönderen kişinin ID: " + str(check.sender_id)
                    ftext += "\n\nOlay Tetikleyici:\n"
                    ftext += str(check.text)
                    ftext += "\n\nHata metni:\n"
                    ftext += str(sys.exc_info()[1])
                    ftext += "\n\n\nGeri izleme bilgisi:\n"
                    ftext += str(format_exc())
                    ftext += "\n\n--------ASİSTAN HATA GUNLUGU BITIS--------"
                    ftext += "\n\n================================\n"
                    ftext += f"====== BOTVER : {EPİC_VERSION} ======\n"
                    ftext += "================================"

                    command = "git log --pretty=format:\"%an: %s\" -7"

                    ftext += "\n\n\nSon 7 commit:\n"

                    process = await asyncsubshell(command,
                                                  stdout=asyncsub.PIPE,
                                                  stderr=asyncsub.PIPE)
                    stdout, stderr = await process.communicate()
                    result = str(stdout.decode().strip()) \
                        + str(stderr.decode().strip())

                    ftext += result

                    file = open("error.log", "w+")
                    file.write(ftext)
                    file.close()

                    remove("error.log")
            else:
                pass
        if not disable_edited:
            tgbot.add_event_handler(wrapper, events.MessageEdited(**args))
        tgbot.add_event_handler(wrapper, events.NewMessage(**args))

        return wrapper

    return decorator