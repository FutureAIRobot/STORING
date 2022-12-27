# @Lx_0988
import os, re, logging, time,
from logging.handlers import RotatingFileHandler
from os import environ

id_pattern = re.compile(r'^.\d+$')


APP_ID = 26686963
API_HASH = "7cce2717e7e89eb534b7da973926f6c4"
USER_SESSION = "BQA_dDbo5YV_gEoau0uKvk2BRMMA8DxV-G1afVq-n1WxLu8CUyrts8Ppu2zeQjfA99nD5LY2rXDJPT-Eeb3Wu83mT89b5aUKFaLurWVDzXgakGIw3ZiyiQ8XpRH7cSNcnfx-uKsnZypskEJE2F7E4I_do7hYFTEikxoagyx0mXOEWe_4nZvjOL9fy239Cjs3GXImfHTDPGrIziMfJy9L3GQ68xzRj9r0DYV9TvtxMI8gens-JjrOWgn4rYjo4dBIlT6wR0YB5_vBCTe2Uzzashl5gKguihyNGRRykHcCL_8MN4Ns3FW1yVk3PtTzDi3p-4A8kKJ1nGzR45rUI3I7BIzsAAAAAWC3LdcA"
BOT_TOKEN = "5955626700:AAHp0E01f71kJbcCgF2KWvsCfJmQ2tbADaA"
CHANNEL_IDS = [int(ch) if id_pattern.search(ch) else ch for ch in environ['CHANNEL_IDS'].split()]

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
