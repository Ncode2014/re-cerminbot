# Suggested by - @d0n0t (https://github.com/code-rgb/USERGE-X/issues/9)
# Copyright (C) 2020 BY - GitHub.com/code-rgb [TG - @deleteduser420]
# All rights reserved.

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot import app
from bot.helper import post_to_telegraph, runcmd, safe_filename
from bot.helper.telegram_helper.bot_commands import BotCommands


@app.on_message(filters.command(BotCommands.MediaInfoCommand))
async def mediainfo(client, message):
    reply = message.reply_to_message
    if not reply:
        await message.reply_text(
            "Balas ke Media dulu (hanya file/media telegram) bukan website"
        )
        return
    process = await message.reply_text("`Memproses...`")
    x_media = None
    available_media = (
        "audio",
        "document",
        "photo",
        "sticker",
        "animation",
        "video",
        "voice",
        "video_note",
        "new_chat_photo",
    )
    for kind in available_media:
        x_media = getattr(reply, kind, None)
        if x_media is not None:
            break
    if x_media is None:
        await process.edit_text("Membalas Format Media yang Valid")
        return
    media_type = str(type(x_media)).split("'")[1]
    file_path = safe_filename(await reply.download())
    output_ = await runcmd(f'mediainfo "{file_path}"')
    out = output_[0] if len(output_) != 0 else None
    body_text = f"""
<h2>JSON</h2>
<pre>{x_media}</pre>
<br>

<h2>DETAILS</h2>
<pre>{out or 'Not Supported'}</pre>
"""
    title = "re-mirrorbot Mediainfo"
    text_ = media_type.split(".")[-1].upper()
    link = post_to_telegraph(title, body_text)
    markup = InlineKeyboardMarkup([[InlineKeyboardButton(text=text_, url=link)]])
    await process.edit_text("ℹ️ <b>INFO MEDIA</b>", reply_markup=markup)
