import logging
logger = logging.getLogger(__name__)
from AutoForward import MAINCHANNEL_ID
import asyncio
from pyrogram import Client, filters


@Client.on_message(filters.channel)
async def forward(client, message):
    # Forwarding the messages to the channel
   try:
      for id in MAINCHANNEL_ID:
         from_channel, to_channel = id.split(":")
         if message.chat.id == int(from_channel):
#           func = message.copy if False else message.forward
            await message.copy(int(to_channel))
            print("Forwarded a message from", from_channel, "to", to_channel)
            await asyncio.sleep(1)
   except Exception as e:
      logger.exception(e)