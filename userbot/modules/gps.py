from geopy.geocoders import Nominatim
from telethon.tl import types

from userbot.events import register
from userbot.cmdhelp import CmdHelp

# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value
LANG = get_value("gps")

# ████████████████████████████████ #

@register(outgoing=True, pattern=r"^.gps (.*)")
async def gps(event):
    if event.fwd_from:
        return
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    input_str = event.pattern_match.group(1)

    if not input_str:
        return await event.edit("`Epicye Bir Bölgenin İsmini Vermezsen Bulamaz Ki.`")

    await event.edit("**Buluyorum...**")

    geolocator = Nominatim(user_agent="erdembey")
    geoloc = geolocator.geocode(input_str)
    if geoloc:
        lon = geoloc.longitude
        lat = geoloc.latitude
        await event.reply(
            input_str,
            file=types.InputMediaGeoPoint(types.InputGeoPoint(lat, lon)),
            reply_to=reply_to_id,
        )
        await event.delete()
    else:
        await event.edit("`Özür Dilerim Bu Bölgeyi Bulamadım Şey Hata Yapmış Olabilirsin :(`")

CmdHelp('gps').add_command('gps', LANG['GPS1'], LANG['GPS2']).add()
