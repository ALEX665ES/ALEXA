# MIT License
#
# Copyright (c) 2023 ALEX665ES 
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

from pyrogram import filters
from pyrogram.enums import ChatType, ParseMode
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtubesearchpython.__future__ import VideosSearch

import config
from ALEXA import BOT_MENTION, BOT_NAME, app
from ALEXA.Helpers import gp_buttons, pm_buttons
from ALEXA.Helpers.dossier import *


@app.on_message(filters.command(["start"]) & ~filters.forwarded)
@app.on_edited_message(filters.command(["start"]) & ~filters.forwarded)
async def ALEX_st(_, message: Message):
    if message.chat.type == ChatType.PRIVATE:
        if len(message.text.split()) > 1:
            cmd = message.text.split(None, 1)[1]
            if cmd[0:3] == "inf":
                m = await message.reply_text("🔎")
                query = (str(cmd)).replace("info_", "", 1)
                query = f"https://www.youtube.com/watch?v={query}"
                results = VideosSearch(query, limit=1)
                for result in (await results.next())["result"]:
                    title = result["title"]
                    duration = result["duration"]
                    views = result["viewCount"]["short"]
                    thumbnail = result["thumbnails"][0]["url"].split("?")[0]
                    channellink = result["channel"]["link"]
                    channel = result["channel"]["name"]
                    link = result["link"]
                    published = result["publishedTime"]
                searched_text = f"""
➻ **𝗧𝗿𝗮𝗰𝗸 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻** 

📌 **𝙏𝙞𝙩𝙡𝙚 :** {title}

⏳ **𝘿𝙪𝙧𝙖𝙩𝙞𝙤𝙣 :** {duration} 𝙈𝙞𝙣
👀 **𝙑𝙞𝙚𝙬𝙨 :** `{views}`
⏰ **𝙋𝙪𝙗𝙡𝙞𝙨𝙝𝙚𝙙 𝙊𝙣 :** {published}
🔗 **𝙇𝙞𝙣𝙠 :** [ᴡᴀᴛᴄʜ ᴏɴ ʏᴏᴜᴛᴜʙᴇ]({link})
🎥 **𝘾𝙝𝙖𝙣𝙣𝙚𝙡 :** [{channel}]({channellink})

💖 𝙎𝙚𝙖𝙧𝙘𝙝 𝙋𝙤𝙬𝙚𝙧𝙚𝙙 𝘽𝙮 ⚡︎ {BOT_NAME}"""
                key = InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(text="𝙔𝙤𝙪𝙏𝙪𝙗𝙚", url=link),
                            InlineKeyboardButton(
                                text="𝙂𝙧𝙤𝙪𝙥", url=config.SUPPORT_CHAT
                            ),
                        ],
                    ]
                )
                await m.delete()
                return await app.send_photo(
                    message.chat.id,
                    photo=thumbnail,
                    caption=searched_text,
                    parse_mode=ParseMode.MARKDOWN,
                    reply_markup=key,
                )
        else:
            await message.reply_photo(
                photo=config.START_IMG,
                caption=PM_START_TEXT.format(
                    message.from_user.first_name,
                    BOT_MENTION,
                ),
                reply_markup=InlineKeyboardMarkup(pm_buttons),
            )
    else:
        await message.reply_photo(
            photo=config.START_IMG,
            caption=START_TEXT.format(
                message.from_user.first_name,
                BOT_MENTION,
                message.chat.title,
                config.SUPPORT_CHAT,
            ),
            reply_markup=InlineKeyboardMarkup(gp_buttons),
        )
