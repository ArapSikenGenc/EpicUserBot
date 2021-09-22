from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from pytgcalls_wrapper import Wrapper
from userbot import client
import logging
from userbot.asisstant.yardim import mahniniseslendir, Text
from os import remove
import os
import youtube_dl
from youtube_search import YoutubeSearch
import requests



pytgcalls = PyTgCalls(client)
pycalls = Wrapper(pytgcalls, "raw")

@client.on_message(filters.command(['seslendir'], ['!','.','/']) & filters.me)
async def seslendir(_, message):
    txt = message.text.split(" ", 1)
    type_ = None
    try:
        song_name = txt[1]
        type_ = "url"
    except IndexError:
        reply = message.reply_to_message
        if reply:
            if reply.audio:
                med = reply.audio
            elif reply.video:
                med = reply.video
            elif reply.voice:
                med = reply.voice
            else:
                return await message.reply_text(Text.how_to)
            song_name = med.file_name
            type_ = "tg"
    if type_ == "url":
        if "youtube" not in song_name and "youtu.be" not in song_name:
            return await message.reply_text(Text.not_yet)
        await message.reply_text("Oxunur `{}`".format(song_name))
        await mahniniseslendir(pycalls, message, song_name)
    elif type_ == "tg":
        x = await message.reply_text(Text.dl)
        file_ = await reply.download()
        await x.edit("`Səsləndirilir...`")
        await mahniniseslendir(pycalls, message, file_)
        remove(file_)
    else:
        return await message.reply_text(Text.how_to)


@client.on_message(filters.command(['pause'], ['!','.','/']) & filters.me)
async def pause(_, message):
    pycalls.pause(message.chat.id)
    await message.reply_text("Musiqiyə ara verildi.")


@client.on_message(filters.command(['resume'], ['!','.','/']) & filters.me)
async def resume(_, message):
    pycalls.resume(message.chat.id)
    await message.reply_text("Musiqi davam etdirilir.")

pytgcalls.run()
