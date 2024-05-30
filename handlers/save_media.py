import asyncio
import requests
import string
import random
from configs import Config
from pyrogram import Client
from pyrogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from pyrogram.errors import FloodWait
from handlers.helpers import str_to_b64

def generate_random_alphanumeric():
    """Generate a random 8-letter alphanumeric string."""
    characters = string.ascii_letters + string.digits
    random_chars = ''.join(random.choice(characters) for _ in range(8))
    return random_chars

def get_short(url):
    rget = requests.get(f"https://{Config.SHORTLINK_URL}/api?api={Config.SHORTLINK_API}&url={url}&alias={generate_random_alphanumeric()}")
    rjson = rget.json()
    if rjson["status"] == "success" or rget.status_code == 200:
        return rjson["shortenedUrl"]
    else:
        return url

    
async def forward_to_channel(bot: Client, message: Message, editable: Message):
    try:
        __SENT = await message.forward(Config.DB_CHANNEL)
        return __SENT
    except FloodWait as sl:
        if sl.value > 45:
            await asyncio.sleep(sl.value)
            await bot.send_message(
                chat_id=int(Config.LOG_CHANNEL),
                text=f"#FloodWait:\nGot FloodWait of `{str(sl.value)}s` from `{str(editable.chat.id)}` !!",
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("Ban User", callback_data=f"ban_user_{str(editable.chat.id)}")]
                    ]
                )
            )
        return await forward_to_channel(bot, message, editable)


async def save_batch_media_in_channel(bot: Client, editable: Message, message_ids: list):
    try:
        message_ids_str = ""
        for message in (await bot.get_messages(chat_id=editable.chat.id, message_ids=message_ids)):
            sent_message = await forward_to_channel(bot, message, editable)
            if sent_message is None:
                continue
            message_ids_str += f"{str(sent_message.id)} "
            await asyncio.sleep(2)
        SaveMessage = await bot.send_message(
            chat_id=Config.DB_CHANNEL,
            text=message_ids_str,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("Delete Batch", callback_data="closeMessage")
            ]])
        )
        share_link = f"https://telegram.me/{Config.BOT_USERNAME}?start=InfinityRobots_{str_to_b64(str(SaveMessage.id))}"
        short_link = get_short(share_link)
        await editable.edit(
            f"**𝖡𝖺𝗍𝖼𝗁 𝖥𝗂𝗅𝖾𝗌 𝖲𝗍𝗈𝗋𝖾𝖽 𝖨𝗇 𝖬𝗒 𝖣𝖺𝗍𝖺𝖻𝖺𝗌𝖾**\n\n𝖧𝖾𝗋𝖾 𝖨𝗌 𝖳𝗁𝖾 𝖯𝖾𝗋𝗆𝖺𝗇𝖾𝗇𝗍 𝖫𝗂𝗇𝗄 𝖮𝖿 𝖸𝗈𝗎𝗋 𝖥𝗂𝗅𝖾𝗌: <code>{short_link}</code> \n\n"
            f"Just Click The Link To Get Your Files!",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("𝖲𝗁𝖺𝗋𝖾𝖺𝖻𝗅𝖾 𝖫𝗂𝗇𝗄", url=share_link),
                  InlineKeyboardButton("𝖲𝗁𝗈𝗋𝗍𝗇𝖾𝗋", url=short_link)]]
            ),
            disable_web_page_preview=True
        )
        await bot.send_message(
            chat_id=int(Config.LOG_CHANNEL),
            text=f"#BATCH_SAVE:\n\n[{editable.reply_to_message.from_user.first_name}](tg://user?id={editable.reply_to_message.from_user.id}) Got Batch Link!",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("𝖲𝗁𝖺𝗋𝖾𝖺𝖻𝗅𝖾 𝖫𝗂𝗇𝗄", url=short_link),
                                                InlineKeyboardButton("𝖲𝗁𝗈𝗋𝗍𝗇𝖾𝗋", url=share_link)]])
        )
    except Exception as err:
        await editable.edit(f"Something Went Wrong!\n\n**Error:** `{err}`")
        await bot.send_message(
            chat_id=int(Config.LOG_CHANNEL),
            text=f"#ERROR_TRACEBACK:\nGot Error from `{str(editable.chat.id)}` !!\n\n**Traceback:** `{err}`",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("Ban User", callback_data=f"ban_user_{str(editable.chat.id)}")]
                ]
            )
        )


async def save_media_in_channel(bot: Client, editable: Message, message: Message):
    try:
        forwarded_msg = await message.forward(Config.DB_CHANNEL)
        file_er_id = str(forwarded_msg.id)
        await forwarded_msg.reply_text(
            f"#PRIVATE_FILE:\n\n[{message.from_user.first_name}](tg://user?id={message.from_user.id}) Got File Link!",
            disable_web_page_preview=True)
        share_link = f"https://telegram.me/{Config.BOT_USERNAME}?start=InfinityRobots_{str_to_b64(file_er_id)}"
        short_link = get_short(share_link)
        await editable.edit(
            "**𝖸𝗈𝗎𝗋 𝖥𝗂𝗅𝖾 𝖲𝗍𝗈𝗋𝖾𝖽 𝖨𝗇 𝖬𝗒 𝖣𝖺𝗍𝖺𝖻𝖺𝗌𝖾**\n\n"
            f"𝖧𝖾𝗋𝖾 𝖨𝗌 𝖳𝗁𝖾 𝖯𝖾𝗋𝗆𝖺𝗇𝖾𝗇𝗍 𝖫𝗂𝗇𝗄 𝖮𝖿 𝖸𝗈𝗎 𝖥𝗂𝗅𝖾: <code>{short_link}</code> \n\n"
            "𝖩𝗎𝗌𝗍𝖻𝖢𝗅𝗂𝖼𝗄 𝖳𝗁𝖾 𝖫𝗂𝗇𝗄 𝖳𝗈 𝖦𝖾𝗍 𝖸𝗈𝗎𝗋 𝖥𝗂𝗅𝖾.",
            reply_markup=InlineKeyboardMarkup(
               [[InlineKeyboardButton("𝖲𝗁𝖺𝗋𝖾𝖺𝖻𝗅𝖾 𝖫𝗂𝗇𝗄", url=share_link),
                  InlineKeyboardButton("𝖲𝗁𝗈𝗋𝗍𝗇𝖾𝗋", url=short_link)]]
            ),
            disable_web_page_preview=True
        )
    except FloodWait as sl:
        if sl.value > 45:
            print(f"Sleep of {sl.value}s caused by FloodWait ...")
            await asyncio.sleep(sl.value)
            await bot.send_message(
                chat_id=int(Config.LOG_CHANNEL),
                text="#FloodWait:\n"
                     f"Got FloodWait of `{str(sl.value)}s` from `{str(editable.chat.id)}` !!",
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("Ban User", callback_data=f"ban_user_{str(editable.chat.id)}")]
                    ]
                )
            )
        await save_media_in_channel(bot, editable, message)
    except Exception as err:
        await editable.edit(f"𝖲𝗈𝗆𝖾𝗍𝗁𝗂𝗇𝗀 𝖶𝖾𝗇𝗍 𝖶𝗋𝗈𝗇𝗀!\n\n**𝖤𝗋𝗋𝗈𝗋:** `{err}`")
        await bot.send_message(
            chat_id=int(Config.LOG_CHANNEL),
            text="#ERROR_TRACEBACK:\n"
                 f"Got Error from `{str(editable.chat.id)}` !!\n\n"
                 f"**Traceback:** `{err}`",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("Ban User", callback_data=f"ban_user_{str(editable.chat.id)}")]
                ]
            )
        )
