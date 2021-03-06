# Implement By https://github.com/jusidama18
# Based on this https://github.com/DevsExpo/FridayUserbot/blob/master/plugins/heroku_helpers.py

from pyrogram import filters
from bot import app, OWNER_ID, bot
from bot.helper import check_heroku


@app.on_message(filters.command(['reboot', f'reboot@{bot.username}']) & filters.user(OWNER_ID))
@check_heroku
async def gib_restart(client, message, hap):
    msg_ = await message.reply_text("**[HEROKU] - Memulai ulang**")
    hap.restart()


@app.on_message(filters.command(['shutdown', f'shutdown@{bot.username}']) & filters.user(OWNER_ID))
@check_heroku
async def shutdown(client, message, app_):
    msg_ = await message.reply_text(
        "**[HEROKU] - Matikan**\n\n**NOTE: Anda perlu mengaktifkan manual dari Heroku untuk menggunakan bot ini lagi.**")
    app_.process_formation()["web"].scale(0)
