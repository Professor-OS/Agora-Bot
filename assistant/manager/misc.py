# Agora - UserBot
# Copyright (C) 2021 Professor-OS
#
# This file is a part of < https://github.com/Professor-OS/Agora-Bot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/Professor-OS/Agora-Bot/blob/main/LICENSE/>.


import aiohttp
import random
from pyAgora.dB import SHAAN
from . import *


@agora_cmd(pattern="decide", type="manager")
async def dheh(e):
    text = ["Yes", "NoU", "Maybe", "IDK"]
    text = random.choice(text)
    ri = e.id
    if e.is_reply:
        ri = e.reply_to_msg_id
    await e.client.send_message(e.chat_id, text, reply_to=ri)

@agora_cmd(pattern="echo ?(.*)", type=["manager"])
async def oqha(e):
    match = e.pattern_match.group(1)
    if match:
        text = match
        reply_to = e
    elif e.is_reply:
        text = (await e.get_reply_message()).text
        reply_to = e.reply_to_msg_id
    else:
        return await eor(e, "What to Echo?", time=5)
    await e.client.send_message(e.chat_id, text, reply_to=reply_to)


@agora_cmd(pattern="kickme$", type=["manager"], allow_all=True)
async def doit(e):
    if e.sender_id in DEVLIST:
        return await eod(e, "`I will Not Kick You, my Developer..`")
    try:
        await e.client.kick_participant(e.chat_id, e.sender_id)
    except Exception as Fe:
        return await eor(e, str(Fe), time=5)
    await eor(e, "Yes, You are right, get out.", time=5)


@agora_cmd(pattern="joke$", type=["manager"])
async def do_joke(e):
    e = await e.get_reply_message() if e.is_reply else e
    link = "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&type=single"
    async with aiohttp.ClientSession() as ses:
        async with ses.get(link) as out:
            out = await out.json()
    await e.reply(out["joke"])
