# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#

# EpicUserBot - ErdemBey - Midy- ByMisakiMey
#

""" UserBot yardım komutu """

from userbot.cmdhelp import CmdHelp
from userbot import cmdhelp
from userbot import CMD_HELP
from userbot.asisstant.events import epic
from userbot import OWNER_ID

# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value
LANG = get_value("__epic")

# ████████████████████████████████ #

@epic(incoming=True, from_users=OWNER_ID, pattern="^/[Ee]pic")
async def epic(event):
    """ /epic komutun """
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.reply(str(CMD_HELP[args]))
        else:
            await event.reply(LANG["NEED_PLUGIN"])
    else:
        string = ""
        sayfa = [sorted(list(CMD_HELP))[i:i + 5] for i in range(0, len(sorted(list(CMD_HELP))), 5)]
        
        for i in sayfa:
            string += f'`🔻⇝ `'
            for sira, a in enumerate(i):
                string += "`" + str(a)
                if sira == i.index(i[-1]):
                    string += "`"
                else:
                    string += "`, "
            string += "\n"
        await event.reply(LANG["NEED_MODULE"] + '\n\n' + string)