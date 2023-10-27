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
from pyrogram.types import Message

from ALEXA import app, pytgcalls
from ALEXA.Helpers import admin_check, close_key, is_streaming, stream_on


@app.on_message(filters.command(["resume"]) & filters.group)
@admin_check
async def res_str(_, message: Message):
    try:
        await message.delete()
    except:
        pass

    if await is_streaming(message.chat.id):
        return await message.reply_text("𝘿𝙞𝙙 𝙔𝙤𝙪 𝙍𝙚𝙢𝙚𝙢𝙗𝙚𝙧 𝙏𝙝𝙖𝙩 𝙮𝙤𝙪 𝙋𝙖𝙪𝙨𝙚𝙙 𝙏𝙝𝙚 𝙎𝙩𝙧𝙚𝙖𝙢 ?")
    await stream_on(message.chat.id)
    await pytgcalls.resume_stream(message.chat.id)
    return await message.reply_text(
        text=f"𝙎𝙩𝙧𝙚𝙖𝙢 𝙍𝙚𝙨𝙪𝙢𝙚𝙙\n│ \n└𝘽𝙮 : {message.from_user.mention} 🥀",
        reply_markup=close_key,
    )
