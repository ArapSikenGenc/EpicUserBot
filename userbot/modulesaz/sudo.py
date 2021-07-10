# HydraDev Erdem Bey ByMisakimey

from telethon import events

import asyncio
from userbot import SUDO_ID
from userbot.cmdhelp import CmdHelp
from userbot.events import register

@register(incoming=True, from_users=SUDO_ID, pattern="^.salive$")
async def _(q):
    await q.client.send_message(q.chat_id,"`Seni Seviyorum❤️ Epic Çalışıyor...`")

CmdHelp('sudo').add_command(
    'sudoekle', None, 'Mesajına cevap verdiğiniz kullanıcını botunuzda admin yapar.'
    ).add_command(
    'salive', None, 'SUDOnun aktif olup olmadığını kontrol eder.'
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
