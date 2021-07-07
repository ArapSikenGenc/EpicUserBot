from telethon.tl.types import ChannelParticipantsAdmins

from userbot.events import register as misaki
from userbot.cmdhelp import CmdHelp
from userbot import bot


@misaki(outgoing=True, pattern="^.tagall ?(.*)$")
async def _(event):
    if event.fwd_from:
        return
    mentions = event.pattern_match.group(1)
    chat = await event.get_input_chat()
    async for x in bot.iter_participants(chat, 2000):
        mentions += f" \n [{x.first_name}](tg://user?id={x.id})"
    await event.reply(mentions)
    await event.delete()


@misaki(outgoing=True, pattern="^.admin ?(.*)$")
async def _(event):
    if event.fwd_from:
        return
    mentions = "Adminlər: "
    chat = await event.get_input_chat()
    async for x in bot.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f" \n [{x.first_name}](tg://user?id={x.id})"
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()

CmdHelp('tags').add_command(
    'tagall', '<sebep>', 'Bir mesajda 100 üye etiketler (Maksimum 2000)'
).add_command(
    'admin', '<sebep>', 'Grupdaki adminleri bir mesajda etiketler.'
).add_command(
    'tag', '<sebep>', 'Grubdaki üyeleri tek tek etiketler. (Maksimum 2000)'
).add_command(
    'alladmin', '<sebep>', 'Qrupdaki adminləri bir mesajda etiketləyər.'
).add_command(
    'kill all', None, 'etiketleme işlemini durdurur.'
).add()
