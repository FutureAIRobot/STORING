# @Lx0988
import logging, asyncio
logger = logging.getLogger(__name__)
from AutoForward import FROMCHANNEL_ID
from pyrogram import Client, filters, enums
from pyrogram.errors import FloodWait

media_filter = filters.document | filters.video | filters.audio
 
@Client.on_message(filters.channel & media_filter)
async def forward(client, update):
    try:      
        await asyncio.sleep(600)
        await client.copy_message(
            chat_id=-1001641840781,
            from_chat_id=update.chat.id,
            message_id=update.id,
            caption=update.caption,
            parse_mode=enums.ParseMode.MARKDOWN
        )

    except FloodWait as e:
        await asyncio.sleep(e.value)

"""
@Client.on_message(filters.chat(-1001846691219) & filters.group & media_filter)
async def forward(client, update):
    try:      
        await asyncio.sleep(20)
        await client.copy_message(
            chat_id=-1001862738079,
            from_chat_id=-1001846691219,
            message_id=update.id,
            caption=update.caption,
            parse_mode=enums.ParseMode.MARKDOWN
        )

    except FloodWait as e:
        await asyncio.sleep(e.value)
"""
