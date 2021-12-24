# Agora - UserBot
# Copyright (C) 2021 Professor-OS
#
# This file is a part of < https://github.com/Professor-OS/Agora-Bot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/Professor-OS/Agora-Bot/blob/main/LICENSE/>.

from pyAgora import *
from pyAgora.functions.helper import *
from pyAgora.misc import owner_and_sudos
from pyAgora.misc._assistant import asst_cmd, callback, in_pattern
from telethon import Button, custom

from plugins import ATRA_COL
from strings import get_languages, get_string, language

OWNER_NAME = agora_bot.me.first_name
OWNER_ID = agora_bot.me.id

AST_PLUGINS = {}


async def setit(event, name, value):
    try:
        udB.set(name, value)
    except BaseException:
        return await event.edit("`Something Went Wrong`")


def get_back_button(name):
    return [Button.inline("« Bᴀᴄᴋ", data=f"{name}")]
