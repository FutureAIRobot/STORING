#####
import os
import logging
import time

from logging.handlers import RotatingFileHandler

APP_ID = 16029596
API_HASH = "8c6b3ce7f23e51dfebbdbe98a0ee674d"
USER_SESSION = os.environ.get("USER_SESSION")
BOT_TOKEN = "6294815862:AAF5jPiTIjJNE6kPcsFK43PL9sWqN8dUfCs"
VERIFY = {}

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "automated.txt",
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
