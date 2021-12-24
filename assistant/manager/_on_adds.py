# Agora - UserBot
# Copyright (C) 2021 Professor-OS
#
# This file is a part of < https://github.com/Professor-OS/Agora-Bot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/Professor-Agora/Agora-Bot/blob/main/LICENSE/>.

from . import *
from telethon import events


@asst.on(events.ChatAction(func= lambda x: x.user_added))
async def dueha(e):
    user = await e.get_user()
    if not user.is_self:
        return
    sm = udB.get("ON_MNGR_ADD")
    if sm == "OFF":
        return
    if not sm:
        sm = "Thanks for Adding me :)"
    await e.reply(sm, link_preview=False)
