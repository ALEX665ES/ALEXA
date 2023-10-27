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

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import config
from ALEXA import BOT_USERNAME

close_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="❰𝗖𝗹𝗼𝘀𝗲❱", callback_data="close")]]
)


buttons = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="❰𝙊𝙬𝙣𝙚𝙧❱", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="❰𝙂𝙧𝙤𝙪𝙥❱", url=config.SUPPORT_CHAT),
        ]
    ]
)


pm_buttons = [
    [
        InlineKeyboardButton(
            text="𝗔𝗱𝗱 𝗠𝗲 𝗧𝗼 𝗜𝗻 𝗬𝗼𝘂𝗿 𝗚𝗿𝗼𝘂𝗽",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [InlineKeyboardButton(text="❰𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨❱", callback_data="ALEX_help")],
    [
        InlineKeyboardButton(text="❰𝗖𝗵𝗮𝗻𝗻𝗲𝗹❱", url=config.SUPPORT_CHANNEL),
        InlineKeyboardButton(text="❰𝗦𝘂𝗽𝗽𝗼𝗿𝘁❱", url=config.SUPPORT_CHAT),
    ],
    [
        InlineKeyboardButton(text="❰𝗢𝘄𝗻𝗲𝗿❱", user_id=config.OWNER_ID),
    ],
]


gp_buttons = [
    [
        InlineKeyboardButton(
            text="𝗔𝗱𝗱 𝗠𝗲 𝗧𝗼 𝗜𝗻 𝗬𝗼𝘂𝗿 𝗚𝗿𝗼𝘂𝗽",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [
        InlineKeyboardButton(text="𝗥𝗲𝗽𝗼𝘀𝗶𝘁𝗼𝗿𝘆", url=f"https://github.com/ALEX665ES/ALEXA"),
    ],
]


helpmenu = [
    [
        InlineKeyboardButton(
            text="𝘽𝙤𝙩𝙪𝙨𝙚𝙧",
            callback_data="ALEX_cb help",
        ),

        InlineKeyboardButton(text="𝙎𝙪𝙙𝙤𝙪𝙨𝙚𝙧", callback_data="ALEX_cb sudo"),
    ],    
    [   InlineKeyboardButton(text="⚡ 𝗥𝗲𝗽𝗼𝘀𝗶𝘁𝗼𝗿𝘆 ⚡", url=f"https://github.com/ALEX665ES/ALEXA"),
    ],
    [
        InlineKeyboardButton(text="𝗕𝗮𝗰𝗸", callback_data="ALEX_home"),
        InlineKeyboardButton(text="𝗖𝗹𝗼𝘀𝗲", callback_data="close"),
    ],
]


help_back = [
 [
        InlineKeyboardButton(text="𝗕𝗮𝗰𝗸", callback_data="ALEX_help"),
        InlineKeyboardButton(text="𝗖𝗹𝗼𝘀𝗲", callback_data="close"),
    ],
]
