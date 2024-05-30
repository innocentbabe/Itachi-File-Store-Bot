import asyncio
from typing import (
    Union
)
from configs import Config
from pyrogram import Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message


async def get_invite_link(bot: Client, chat_id: Union[str, int]):
    try:
        invite_link = await bot.create_chat_invite_link(chat_id=chat_id)
        return invite_link
    except FloodWait as e:
        print(f"Sleep of {e.value}s caused by FloodWait ...")
        await asyncio.sleep(e.value)
        return await get_invite_link(bot, chat_id)


async def handle_force_sub(bot: Client, cmd: Message):
    if Config.UPDATES_CHANNEL and Config.UPDATES_CHANNEL.startswith("-100"):
        channel_chat_id = int(Config.UPDATES_CHANNEL)
    elif Config.UPDATES_CHANNEL and (not Config.UPDATES_CHANNEL.startswith("-100")):
        channel_chat_id = Config.UPDATES_CHANNEL
    else:
        return 200
    try:
        user = await bot.get_chat_member(chat_id=channel_chat_id, user_id=cmd.from_user.id)
        if user.status == "kicked":
            await bot.send_message(
                chat_id=cmd.from_user.id,
                text="𝖲𝗈𝗋𝗋𝗒 𝖲𝗂𝗋 𝖸𝗈𝗎 𝖠𝗋𝖾 𝖡𝖺𝗇𝗇𝖾𝖽 𝖳𝗈 𝖴𝗌𝖾 𝖬𝖾 𝖢𝗈𝗇𝗍𝖺𝖼𝗍 𝖬𝗒 [**𝖮𝖶𝖭𝖤𝖱**](https://t.me/DRDIC).",
                disable_web_page_preview=True
            )
            return 400
    except UserNotParticipant:
        try:
            invite_link = await get_invite_link(bot, chat_id=channel_chat_id)
        except Exception as err:
            print(f"Unable to do Force Subscribe to {Config.UPDATES_CHANNEL}\n\nError: {err}")
            return 200
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="➜ **𝖯𝗅𝖾𝖺𝗌𝖾 𝖩𝗈𝗂𝗇 𝖬𝗒 𝖴𝗉𝖽𝖺𝗍𝖾𝗌 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 𝖳𝗈 𝖴𝗌𝖾 𝖬𝖾.**\n\n"
                 "๏ **𝖣𝗎𝖾 𝖳𝗈 𝖮𝗏𝖾𝗋𝗅𝗈𝖺𝖽 ,** 𝖮𝗇𝗅𝗒 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 𝖬𝖾𝗆𝖻𝖾𝗋𝗌 𝖢𝖺𝗇 𝖴𝗌𝖾 𝖡𝗈𝗍.",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🤖 𝖩𝗈𝗂𝗇 𝖴𝗉𝖽𝖺𝗍𝖾𝗌 𝖢𝗁𝖺𝗇𝗇𝖾𝗅", url=invite_link.invite_link)
                    ],
                    [
                        InlineKeyboardButton("🔄 𝖱𝖾𝖿𝗋𝖾𝗌𝗁 🔄", callback_data="refreshForceSub")
                    ]
                ]
            )
        )
        return 400
    except Exception:
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="**𝖲𝗈𝗆𝖾𝗍𝗁𝗂𝗇𝗀 𝖶𝖾𝗇𝗍 𝖶𝗋𝗈𝗇𝗀.** 𝖢𝗈𝗇𝗍𝖺𝖼𝗍 𝖬𝗒 [**𝖮𝖶𝖭𝖤𝖱**](https://t.me/DRDIC).",
            disable_web_page_preview=True
        )
        return 200
    return 200
