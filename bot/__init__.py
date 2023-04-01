import os
import logging
import time

from logging.handlers import RotatingFileHandler

APP_ID = 16029596
API_HASH = "8c6b3ce7f23e51dfebbdbe98a0ee674d"
USER_SESSION = "BQAsshTCdlhCzCsw3kNaQ6xzvjsSGzK-AaBIWCI1d2gv7rqRXrrwvcNeU57el76Qwx1sBDjEsH3lfuO21eQVOTgjvUqIBQYLySgL20rmyuGVeKCZCkLnhFQRAMqB_zs88wY0L6uB4WV30tjurbZChVJZkLpJfavqQRTGy1jVUi1WskhWehAijqIvM_RfYjHa8B4XwZ6waSExqjjuCcFlPOFzkU_CkslBVR8bE7h6ExQa1u6ycZ2mwIQAvsRVYU6SLc3kBGYPDqCpVK5q8pOmYqCqLC07j_V9g3GSETLH3MUdcbESTSwzLUCMnuwV_v7guCtepxuBUEA4p1AL3P71Sb1CAAAAAUdFtW4A"
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
