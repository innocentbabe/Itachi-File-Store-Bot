import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", ""))
  API_HASH = os.environ.get("API_HASH", "")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", ""))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "MoneyKamalo.com")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "9972ace070bae89fbb76f073d56e41e5c458c302")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", ""))
  DATABASE_URL = os.environ.get("DATABASE_URL", "")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""
**𝖳𝗁𝗂𝗌 𝖨𝗌 𝖠 𝖯𝖾𝗋𝗆𝖺𝗇𝖾𝗇𝗍 𝖥𝗂𝗅𝖾 𝖲𝖺𝗏𝖾𝗋 𝖡𝗈𝗍.**

➜ 𝖲𝖾𝗇𝖽 𝖬𝖾 𝖠𝗇𝗒 𝖥𝗂𝗅𝖾 𝖳𝗈 𝖦𝖾𝗍 𝖲𝗁𝖺𝗋𝖾𝖺𝖻𝗅𝖾 𝖫𝗂𝗇𝗄.
➜ 𝖶𝗈𝗋𝗄𝗌 𝖨𝗇 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 𝖳𝗈𝗈.
➜ 𝖠𝗏𝗈𝗂𝖽 **𝖢𝗈𝗉𝗒𝗋𝗂𝗀𝗁𝗍 𝖨𝗇𝖿𝗋𝗂𝗇𝗀𝖾𝗆𝖾𝗇𝗍.**

★ 𝗔𝗯𝗼𝘂𝘁 𝗙𝗶𝗹𝗲 𝗦𝗮𝘃𝗲𝗿

๏ **𝖡𝗈𝗍 𝖭𝖺𝗆𝖾** ➜ [𝖥𝗂𝗅𝖾 𝖲𝖺𝗏𝖾𝗋](https://t.me/{BOT_USERNAME})
๏ **𝖫𝖺𝗇𝗀𝗎𝖺𝗀𝖾** ➜ [𝖯𝗒𝗍𝗁𝗈𝗇](https://www.python.org)
๏ **𝖫𝗂𝖻𝗋𝖺𝗋𝗒** ➜ [𝖯𝗒𝗋𝗈𝗀𝗋𝖺𝗆](https://docs.pyrogram.org)

𒊹 𝗝𝗼𝗶𝗻 ☞ @Infinity_Backup
𒊹 𝗢𝘄𝗻𝗲𝗿 ☞ @DRDIC

"""
  ABOUT_DEV_TEXT = f"""
๏ 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿 ➜ [𝖨𝗍𝖺𝖼𝗁𝗂 𝖴𝖼𝗁𝗂𝗁𝖺](https://telegram.me/DRDIC)
 
"""
  HOME_TEXT = """
𝖧𝖾𝗒 , [{}](tg://user?id={})\n\n𝖳𝗁𝗂𝗌 𝖨𝗌 𝖠 𝖯𝖾𝗋𝗆𝖺𝗇𝖾𝗇𝗍 **𝖥𝗂𝗅𝖾 S𝖺𝗏𝖾𝗋 𝖡𝗈𝗍.**

๏ 𝗛𝗼𝘄 𝗧𝗼 𝗨𝘀𝗲 𝗕𝗼𝘁 ?
➜ 𝖲𝖾𝗇𝖽 𝖬𝖾 𝖠𝗇𝗒 𝖥𝗂𝗅𝖾 𝖠𝗇𝖽 𝖨𝗍 𝖶𝗂𝗅𝗅 𝖡𝖾 𝖴𝗉𝗅𝗈𝖺𝖽𝖾𝖽 𝖨𝗇 𝖬𝗒 𝖣𝖺𝗍𝖺𝖻𝖺𝗌𝖾 𝖠𝗇𝖽 𝖸𝗈𝗎 𝖶𝗂𝗅𝗅 𝖦𝖾𝗍 𝖳𝗁𝖾 𝖥𝗂𝗅𝖾 𝖫𝗂𝗇𝗄.

๏ 𝗕𝗲𝗻𝗲𝗳𝗶𝘁𝘀 ?
➜ 𝖨𝖿 𝖸𝗈𝗎 𝖧𝖺𝗏𝖾 𝖠 𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 𝖮𝗋 𝖠𝗇𝗒 𝖢𝗈𝗉𝗒𝗋𝗂𝗀𝗁𝗍 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 𝖳𝗁𝖾𝗇 𝖨𝗍 𝖨𝗌 𝖴𝗌𝖾𝖿𝗎𝗅 𝖥𝗈𝗋 𝖣𝖺𝗂𝗅𝗒 𝖴𝗌𝖺𝗀𝖾.
➜ 𝖸𝗈𝗎𝗋 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 𝖶𝗂𝗅𝗅 𝖡𝖾 𝖲𝖺𝖿𝖾 𝖥𝗋𝗈𝗆 **𝖢𝗈𝗉𝗒𝗋𝗂𝗀𝗁𝗍 𝖨𝗇𝖿𝗋𝗂𝗇𝗀𝖾𝗆𝖾𝗇𝗍** 𝖨𝗌𝗌𝗎𝖾𝗌.
"""
