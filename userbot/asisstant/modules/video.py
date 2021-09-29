"""
VideoPlayerBot, Telegram Video Chat Bot
Copyright (c) 2021  Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
import re
import sys
import time
import ffmpeg
import asyncio
import subprocess
from asyncio import sleep
from youtube_dl import YoutubeDL
from pyrogram import client, filters
from pyrogram.types import Message
from pytgcalls import GroupCallFactory
from userbot import tgbot
from youtubesearchpython import VideosSearch
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from userbot import client
ok = tgbot.get_me()
USERNAME = ok.username
BOT_NAME = ok.first_name
ydl_opts = {
        "quiet": True,
        "geo_bypass": True,
        "nocheckcertificate": True,
}
ydl = YoutubeDL(ydl_opts)
group_call = GroupCallFactory(client, GroupCallFactory.MTPROTO_CLIENT_TYPE.PYROGRAM).get_group_call()


@tgbot.on_callback_query(filters.regex("pause_callback"))
async def pause_callbacc(tgbot, CallbackQuery):
    chat_id = CallbackQuery.message.chat.id
    if chat_id in AUDIO_CALL:
        text = f"⏸ Paused !"
        await AUDIO_CALL[chat_id].set_audio_pause(True)
    elif chat_id in VIDEO_CALL:
        text = f"⏸ Paused !"
        await VIDEO_CALL[chat_id].set_video_pause(True)
    else:
        text = f"❌ Nothing is Playing !"
    await tgbot.answer_callback_query(
        CallbackQuery.id, text, show_alert=True
    )

@tgbot.on_callback_query(filters.regex("resume_callback"))
async def resume_callbacc(tgbot, CallbackQuery):
    chat_id = CallbackQuery.message.chat.id
    if chat_id in AUDIO_CALL:
        text = f"▶️ Resumed !"
        await AUDIO_CALL[chat_id].set_audio_pause(False)
    elif chat_id in VIDEO_CALL:
        text = f"▶️ Resumed !"
        await VIDEO_CALL[chat_id].set_video_pause(False)
    else:
        text = f"❌ Nothing is Playing !"
    await tgbot.answer_callback_query(
        CallbackQuery.id, text, show_alert=True
    )


@tgbot.on_callback_query(filters.regex("end_callback"))
async def end_callbacc(tgbot, CallbackQuery):
    chat_id = CallbackQuery.message.chat.id
    if chat_id in AUDIO_CALL:
        text = f"⏹️ Stopped !"
        await AUDIO_CALL[chat_id].stop()
        AUDIO_CALL.pop(chat_id)
    elif chat_id in VIDEO_CALL:
        text = f"⏹️ Stopped !"
        await VIDEO_CALL[chat_id].stop()
        VIDEO_CALL.pop(chat_id)
    else:
        text = f"❌ Nothing is Playing !"
    await tgbot.answer_callback_query(
        CallbackQuery.id, text, show_alert=True
    )
    await tgbot.send_message(
        chat_id=CallbackQuery.message.chat.id,
        text=f"✅ **Streaming Stopped & Left The Video Chat !**"
    )
    await CallbackQuery.message.delete()


@tgbot.on_message(filters.command(["play", f"play@{USERNAME}"]) & filters.group & ~filters.edited)
async def stream(tgbot, m: Message):
    msg = await m.reply_text("🔄 `Oynatılıyor ...`")
    chat_id = m.chat.id
    media = m.reply_to_message
    if not media and not ' ' in m.text:
        await msg.edit("❗ Bana Canlı Yayın Bağlantısı / YouTube Video Bağlantısı Gönderin / Video Yayınını Başlatmak İçin Bir Videoyu Yanıtlayın!")

    elif ' ' in m.text:
        text = m.text.split(' ', 1)
        query = text[1]
        if not 'http' in query:
            return await msg.edit("❗ Bana Canlı Yayın Bağlantısı / YouTube Video Bağlantısı Gönderin / Video Yayınını Başlatmak İçin Bir Videoyu Yanıtlayın!")
        regex = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+"
        match = re.match(regex, query)
        if match:
            await msg.edit("🔄 `YouTube Video Akışını Başlatılıyor ...`")
            try:
                meta = ydl.extract_info(query, download=False)
                formats = meta.get('formats', [meta])
                for f in formats:
                    ytstreamlink = f['url']
                link = ytstreamlink
                search = VideosSearch(query, limit=1)
                opp = search.result()["result"]
                oppp = opp[0]
                thumbid = oppp["thumbnails"][0]["url"]
                split = thumbid.split("?")
                thumb = split[0].strip()
            except Exception as e:
                return await msg.edit(f"❌ **Youtube Yükleme hatası !** \n\n`{e}`")
                print(e)

        else:
            await msg.edit("🔄 `Canlı Video Akışını Başlatılıyor ...`")
            link = query
            thumb = "https://telegra.ph/file/3e14128ad5c9ec47801bd.jpg"

        vid_call = VIDEO_CALL.get(chat_id)
        if vid_call:
            await VIDEO_CALL[chat_id].stop()
            VIDEO_CALL.pop(chat_id)
            await sleep(3)

        aud_call = AUDIO_CALL.get(chat_id)
        if aud_call:
            await AUDIO_CALL[chat_id].stop()
            AUDIO_CALL.pop(chat_id)
            await sleep(3)

        try:
            await sleep(2)
            await group_call.join(chat_id)
            await group_call.start_video(link, with_audio=True, repeat=False)
            VIDEO_CALL[chat_id] = group_call
            await msg.delete()
            await m.reply_photo(
               photo=thumb, 
               caption=f"▶️ **Başlatıldı [Video yayını]({query})  {m.chat.title} !**",
               reply_markup=InlineKeyboardMarkup(
               [
                   [   InlineKeyboardButton(
                          text="HydraDev",
                          url = "t.me/HydraDev"
                       ), 
                       InlineKeyboardButton(
                          text="⏸",
                          callback_data="pause_callback",
                       ),
                       InlineKeyboardButton(
                          text="▶️",
                          callback_data="resume_callback",
                       ),
                       InlineKeyboardButton(
                          text="⏹️",
                          callback_data="end_callback",
                       
                       
                       ),
                   ],
               ]),
            )
        except Exception as e:
            await msg.edit(f"❌ **Bir hata oluştu !** \n\nHata: `{e}`")

    elif media.video or media.document:
        await msg.edit("🔄 `Yükleniyor ...`")
        if media.video.thumbs:
            lol = media.video.thumbs[0]
            lel = await tgbot.download_media(lol['file_id'])
            thumb = lel
        else:
            thumb = "https://telegra.ph/file/62e86d8aadde9a8cbf9c2.jpg"
        video = await tgbot.download_media(media)

        vid_call = VIDEO_CALL.get(chat_id)
        if vid_call:
            await VIDEO_CALL[chat_id].stop()
            VIDEO_CALL.pop(chat_id)
            await sleep(3)

        aud_call = AUDIO_CALL.get(chat_id)
        if aud_call:
            await AUDIO_CALL[chat_id].stop()
            AUDIO_CALL.pop(chat_id)
            await sleep(3)

        try:
            await sleep(2)
            await group_call.join(chat_id)
            await group_call.start_video(video, with_audio=True, repeat=False)
            VIDEO_CALL[chat_id] = group_call
            await msg.delete()
            await m.reply_photo(
               photo=thumb,
               caption=f"▶️ **Başladı [Video](https://t.me/HydraDev)!**",
               reply_markup=InlineKeyboardMarkup(
               [
                   [
                       InlineKeyboardButton(
                          text="HydraDev",
                          url = "t.me/HydraDev"
                       ),
                       InlineKeyboardButton(
                          text="⏸",
                          callback_data="pause_callback",
                       ),
                       InlineKeyboardButton(
                          text="▶️",
                          callback_data="resume_callback",
                       ),
                       InlineKeyboardButton(
                          text="⏹️",
                          callback_data="end_callback",
                       ),
                   ],
               ]),
            )
        except Exception as e:
            await msg.edit(f"❌ **Bir hata oluştu !** \n\nHata: `{e}`")

    else:
        await msg.edit(
            "💁🏻‍♂️ Bir YouTube videosu aramak istiyor musunuz??",
            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Evet", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "Hayır ❌", callback_data="close"
                    )
                ]
            ]
        )
    )


@tgbot.on_message(filters.command(["pause", f"pause@{USERNAME}"]) & filters.group & ~filters.edited)
async def pause(_, m: Message):
    chat_id = m.chat.id

    if chat_id in AUDIO_CALL:
        await AUDIO_CALL[chat_id].set_audio_pause(True)
        await m.reply_text("⏸ **Paused Audio Streaming !**")

    elif chat_id in VIDEO_CALL:
        await VIDEO_CALL[chat_id].set_video_pause(True)
        await m.reply_text("⏸ **Paused Video Streaming !**")

    else:
        await m.reply_text("❌ **Noting Is Streaming !**")


@tgbot.on_message(filters.command(["resume", f"resume@{USERNAME}"]) & filters.group & ~filters.edited)
async def resume(_, m: Message):
    chat_id = m.chat.id

    if chat_id in AUDIO_CALL:
        await AUDIO_CALL[chat_id].set_audio_pause(False)
        await m.reply_text("▶️ **Resumed Audio Streaming !**")

    elif chat_id in VIDEO_CALL:
        await VIDEO_CALL[chat_id].set_video_pause(False)
        await m.reply_text("▶️ **Resumed Video Streaming !**")

    else:
        await m.reply_text("❌ **Noting Is Streaming !**")


@tgbot.on_message(filters.command(["stop", f"endstream@{USERNAME}"]) & filters.group & ~filters.edited)
async def endstream(tgbot, m: Message):
    msg = await m.reply_text("🔄 `Durduruluyor ...`")
    chat_id = m.chat.id

    if chat_id in AUDIO_CALL:
        await AUDIO_CALL[chat_id].stop()
        AUDIO_CALL.pop(chat_id)
        await msg.edit("⏹️ **Durduruldu !**")

    elif chat_id in VIDEO_CALL:
        await VIDEO_CALL[chat_id].stop()
        VIDEO_CALL.pop(chat_id)
        await msg.edit("⏹️ **Durduruldu !**")

    else:
        await msg.edit("🤖 **Lütfen Önce Bir Video başlatın !**")


# pytgcalls handlers

@group_call.on_audio_playout_ended
async def audio_ended_handler(_, __):
    await sleep(3)
    await group_call.stop()
    print(f"[INFO] - AUDIO_CALL ENDED !")

@group_call.on_video_playout_ended
async def video_ended_handler(_, __):
    await sleep(3)
    await group_call.stop()
    print(f"[INFO] - VIDEO_CALL ENDED !")
