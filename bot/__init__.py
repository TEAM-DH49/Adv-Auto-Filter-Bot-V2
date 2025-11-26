# (c) @AlbertEinsteinTG
import os
import logging
import time

from logging.handlers import RotatingFileHandler

from .translation import Translation

# --- FINAL HARDCODED CREDENTIALS ---

# APP_ID: Naya value seedha number hona chahiye (Integer)
APP_ID = 24526878

# API_HASH
API_HASH = "8cf44b8723e10b16e7de441352c8a6f5"

# BOT_TOKEN
BOT_TOKEN = "8417458619:AAGN__toEHkjMdflB0_f4mrniVnguxjGMiY"

# DB_URI (MongoDB Link - Yehi woh variable hai jo use ho raha hai)
DB_URI = "mongodb+srv://dinesh:Dinesh1234@cluster0.f9mlvaf.mongodb.net/?retryWrites=true&w=majority"

# USER_SESSION (Optional, isse blank rehne do)
USER_SESSION = "" 

VERIFY = {}
# --- END OF HARDCODED CREDENTIALS ---

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "autofilterbot.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

start_uptime = time.time()


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
