import logging
from logging.handlers import RotatingFileHandler

# Bot Configuration
LOG_FILE_NAME = "bot.log"
PORT = '5010'
OWNER_ID = 7560349494

MSG_EFFECT = 5046509860389126442

SHORT_URL = "Arolink.com" # shortner url 
SHORT_API = "4134296f6ba51789996b73ae880bf798671b6d9b" # shortner API
SHORT_TUT = "https://t.me/AnimeWorld_07/18" # shortner tutorial link

# Bot Configuration
SESSION = "Anime_Filestore"
TOKEN = "8917264519:AAESWD4MDrUoXnnizKUVp0TRjoUr6iyYf3w" # Bot token
API_ID = "34822566" # API ID
API_HASH = "3ab7815d50c6baec0e564742eee75b33" # API HASH
WORKERS = 5

DB_URI = "mongodb+srv://thilakff007:0U8T4Aiaoqmje2UD@shadow.vetq4tn.mongodb.net/?appName=Shadow" # MongoDB URI
DB_NAME = "thilakff007"

FSUBS = FSUBS = [
    [-1003809869259, True, 10],
    [-1003811620185, True, 10],
    [-1003321209759, True, 10],
    [-1003899748028, True, 10]
] # Force Subscription Channels [channel_id, request_enabled, timer_in_minutes]
# Database Channel (Primary)
DB_CHANNEL =  -1003580590124  # just put channel id dont add ""
# Multiple Database Channels (can be set via bot settings)
# DB_CHANNELS = {
#     "": {"name": "Primary DB", "is_primary": True, "is_active": True},
#     "": {"name": "Secondary DB", "is_primary": False, "is_active": True}
# }
# Auto Delete Timer (seconds)
AUTO_DEL = 800
# Admin IDs
ADMINS = [7560349494]
# Bot Settings
DISABLE_BTN = True
PROTECT = True # For content protection stops message forwarding and copying from the bot and same goes for the screenshot

# Messages Configuration
MESSAGES = {
    "START": "<b>›› ʜᴇʏ!! {mention}× sᴇɴᴘᴀɪ 🎊\n</b><blockquote><b>ᴜɴʟᴏᴄᴋ ᴛʜᴇ ᴇɴɪɢᴍᴀ ᴏꜰ ᴏɴɢᴏɪɴɢ ᴀɴɪᴍᴇ ᴡʜᴇʀᴇ ᴅᴇsɪʀᴇ ʟɪɴɢᴇʀs ʙᴇʏᴏɴᴅ ᴇᴠᴇʀʏ ꜰʀᴀᴍᴇ, ᴅʀᴀᴡɪɴɢ ʏᴏᴜ ɪɴᴛᴏ ᴀ ʀᴇᴀʟᴍ ᴏꜰ ʜɪᴅᴅᴇɴ ꜰᴀɴᴛᴀsɪᴇs ᴀɴᴅ sɪʟᴇɴᴛ ᴏʙsᴇssɪᴏɴs.</b></blockquote>\n<blockquote>››ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href='https://t.me/Twilight_chaos'>彡 KL 彡</a></blockquote>",
    "FSUB": "<blockquote>›› ʜᴇʏ {mention}× sᴇɴᴘᴀɪ 🎊</blockquote>\n<blockquote><b>ʏᴏᴜʀ ғɪʟᴇ ɪs ʀᴇᴀᴅʏ ‼️ ʟᴏᴏᴋs ʟɪᴋᴇ ʏᴏᴜ ʜᴀᴠᴇɴ'ᴛ sᴜʙsᴄʀɪʙᴇᴅ ᴛᴏ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ʏᴇᴛ, sᴜʙsᴄʀɪʙᴇ ɴᴏᴡ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ғɪʟᴇs</b></blockquote>",
    "ABOUT": "<b>›› ғᴏʀ ᴍᴏʀᴇ: <a href='https://t.me/AnimeWorld_07'>Cʟɪᴄᴋ ʜᴇʀᴇ</a>\n<blockquote expandable>›› ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ: <a href='https://t.me/AnimeWorld_07'>Animeworld_07</a> \n›› ᴏᴡɴᴇʀ: @Twilight_chaos\n›› ʟᴀɴɢᴜᴀɢᴇ: <a href='https://docs.python.org/3/'>Pʏᴛʜᴏɴ 3</a> \n›› ʟɪʙʀᴀʀʏ: <a href='https://docs.pyrogram.org/'>Pʏʀᴏɢʀᴀᴍ ᴠ2</a> \n›› ᴅᴀᴛᴀʙᴀsᴇ: <a href='https://www.mongodb.com/docs/'>Mᴏɴɢᴏ ᴅʙ</a> \n›› ᴅᴇᴠᴇʟᴏᴘᴇʀ: @Twilight_chaos</b></blockquote>",
    "CHANNELS":"<b>›› ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ: <a href='https://t.me/Animeworld_07'>Animeworld</a>\n<blockquote expandable>›› ᴍᴏᴠɪᴇs: <a href='https://t.me/Animeworld_07'>ᴀɴɪ_ᴍᴏᴠɪᴇ's ᴍᴀɴɪᴀ</a>\n›› ᴀɴɪᴍᴇ ᴇᴅɪᴛᴢ: <a href='https://t.me/Animeworld_07'>ᴀɴɪᴍᴇ'ᴢ ᴇᴅɪᴛ'ᴢ</a>\n›› ᴀᴅᴜʟᴛ ᴄʜᴀɴɴᴇʟs: <a href='https://t.me/Hamine_flix'>𝖧𝖺𝗇𝗂𝗆𝖾 𝖥𝗅𝗂𝗑</a>\n›› ᴍᴀɴʜᴡᴀ ᴄʜᴀɴɴᴇʟ: <a href='https://t.me/pornwhaa_flix'>ᴘᴏʀɴʜᴡᴀ ғʟɪx</a>\n›› ᴄᴏᴍᴍᴜɴɪᴛʏ: <a href='https://t.me/Animewolrd_07'>Animeworld_07</a>\n›› ᴅᴇᴠᴇʟᴏᴘᴇʀ: @Twilight_chaos</b></blockquote>",
    "REPLY": "<b>ғᴜᴄᴋ ᴏғғ ʙɪᴛᴄʜ !!!</b>",
    "SHORT_MSG": "<blockquote><b>✧ TOKEN EXPIRED</b></blockquote>\n<blockquote>›› ᴘʟᴇᴀsᴇ ᴠᴇʀɪғʏ ᴛᴏ ʀᴇɢᴀɪɴ ᴀᴄᴄᴇss ᴛᴏ ᴛʜᴇ ғɪʟᴇs\n›› ᴠᴀʟɪᴅ ᴄʀᴇᴅɪᴛs: 5 ᴄʀᴇᴅɪᴛs</blockquote>\n────────────────────────\n<blockquote>›› ᴡʜᴀᴛ ɪs ᴀ ᴛᴏᴋᴇɴ?</blockquote>\n<blockquote>≡  ᴇᴀᴄʜ ᴀᴅ ʙʏᴘᴀss ʀᴇᴡᴀʀᴅ ʏᴏᴜ ᴡɪᴛʜ 5 ᴄʀᴇᴅɪᴛs.ᴏɴᴇ ᴄʀᴇᴅɪᴛ ɪs ᴄᴏɴsᴜᴍᴇᴅ ᴘᴇʀ ғɪʟᴇ/ʟɪɴᴋ ᴀᴄᴄᴇss.</blockquote>",
    "START_PHOTO": "https://ibb.co/ch6kvnMf",
    "FSUB_PHOTO": "https://ibb.co/C5q41g1C",
    "SHORT_PIC": "https://ibb.co/XxMhdhDs",
    "SHORT": "https://ibb.co/mC9H5kmF",
    "SHORT_VERIFY": "https://ibb.co/rGg6R2q6",
    "PREMIUM_PLANS_PIC": "https://ibb.co/8Dzq5n9G",
    "QR_PAYMENT_PIC": "https://kommodo.ai/i/gZnrUPIfAqO5hcIkziCZ"
}

def LOGGER(name: str, client_name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    formatter = logging.Formatter(
        f"[%(asctime)s - %(levelname)s] - {client_name} - %(name)s - %(message)s",
        datefmt='%d-%b-%y %H:%M:%S'
    )
    file_handler = RotatingFileHandler(LOG_FILE_NAME, maxBytes=50_000_000, backupCount=10)
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger
