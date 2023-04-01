import os, asyncio
from pyrogram.errors import FloodWait
from pyrogram import Client, filters, enums
 

# MaxplayHD Series 
@Client.on_message(filters.chat(-1001855566600) & (filters.media))
async def forward(bot, update):
    try:      
        await bot.copy_message(
            chat_id=-1001239233167, 
            from_chat_id=-1001855566600, 
            message_id=update.id, 
            caption=update.caption,             
            parse_mode=enums.ParseMode.MARKDOWN                     
        )
    except FloodWait as e:
        await asyncio.sleep(e.value)


# MaxplayHD Movies 
@Client.on_message(filters.chat(-1001523497898) & (filters.media))
async def forward(bot, update):
    try:      
        await bot.copy_message(
            chat_id=-1001239233167, 
            from_chat_id=-1001523497898, 
            message_id=update.id, 
            caption=update.caption,
            parse_mode=enums.ParseMode.MARKDOWN                     
        )
    except FloodWait as e:
        await asyncio.sleep(e.value)


# New Movies 1stOnTG
@Client.on_message(filters.chat(-1001936111628) & (filters.media))
async def forward(bot, update):
    try:      
        await bot.copy_message(
            chat_id=-1001239233167, 
            from_chat_id=-1001936111628, 
            message_id=update.id, 
            caption=update.caption,
            parse_mode=enums.ParseMode.MARKDOWN                     
        )
    except FloodWait as e:
        await asyncio.sleep(e.value)
