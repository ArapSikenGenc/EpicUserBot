from telethon.tl.functions.channels import GetFullChannelRequest as getchat
from telethon.tl.functions.phone import CreateGroupCallRequest as startvc
from telethon.tl.functions.phone import DiscardGroupCallRequest as stopvc
from telethon.tl.functions.phone import GetGroupCallRequest as getvc
from telethon.tl.functions.phone import InviteToGroupCallRequest as invitetovc
from userbot.events import register
from userbot import bot, get_call
from userbot.cmdhelp import CmdHelp


def user_list(l, n):
    for i in range(0, len(l), n):
        yield l[i : i + n]

@register(outgoing=True, groups_only=True, pattern="^.vcba[sş]lat$")
async def start_voice(c):
    chat = await c.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    photo = None

    if not admin and not creator:
        await c.edit("`Bu eylemi yapmak için admin olmalıyım.`")
        return
    try:
        await c.client(startvc(c.chat_id))
        await c.edit("`Sesli sohbet başladı!`")
    except Exception as ex:
        await c.edit(f"Bir hata oluştu\nHata: `{ex}`")


@register(outgoing=True, groups_only=True, pattern="^.vcb[ıi]t[ıi]r$")
async def stop_voice(c):
    chat = await c.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    photo = None

    if not admin and not creator:
        await c.edit("`Bunu yapmak için admin olmalıyım!`")
        return
    try:
        await c.client(stopvc(await get_call(c)))
        await c.edit("`Sesli sohbet başarıyla sonlandırıldı!`")
    except Exception as ex:
        await c.edit(f"Bir hata oluştu\nHata: `{ex}`")



@register(outgoing=True, groups_only=True, pattern="^.vcdavet")
async def _(c):
    await c.edit("`Üyeler sesli sohbete davet ediliyor...`")
    users = []
    z = 0
    async for x in c.client.iter_participants(c.chat_id):
        if not x.bot:
            users.append(x.id)
    cyber = list(user_list(users, 6))
    for p in cyber:
        try:
            await c.client(invitetovc(call=await get_call(c), users=p))
            z += 6
        except BaseException:
            pass
    await c.edit(f"`{z}` **Üyeler çağrıldı...**")


Help = CmdHelp('vc')
Help.add_command('vcbaslat', None, 'Bir grupta sesli sohbet başlatır.')
Help.add_command('vcbitir', None, 'Sesli sohbeti sonlandırır.')
Help.add_command('vcdavet', None, 'Gruptaki üyeleri sesli sohbete davet eder.')
Help.add_info('@EpicUserBot Sesli Sohbet Resmi Modülüdür.')
Help.add()    
