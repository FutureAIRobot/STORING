from pyrogram import Client, filters
import time
from bot.importss import Robot
# app = Client("my_bot")

# Channel IDs
source_channel_id = -1001903118077  # replace with source channel id
destination_channel_id = -1001925773305  # replace with destination channel id

# Forward messages every 5 minutes
@Robot.on_message(filters.private)
async def forward_messages(client, message):
    while True:
        try:
            # Retrieve 5 media messages from source channel
            messages = await client.get_history(
                chat_id=source_channel_id,
                limit=5,
                media_filter="photo | video | document"
            )

            # Forward messages to destination channel
            for message in messages:
                if message.photo:
                    await client.send_photo(
                        chat_id=destination_channel_id,
                        photo=message.photo.file_id,
                        caption=message.caption.text
                    )
                elif message.video:
                    await client.send_video(
                        chat_id=destination_channel_id,
                        video=message.video.file_id,
                        caption=message.caption.text
                    )
                elif message.document:
                    await client.send_document(
                        chat_id=destination_channel_id,
                        document=message.document.file_id,
                        caption=message.caption.text
                    )
            # Wait for 5 minutes before next iteration
            time.sleep(300)
        except Exception as e:
            print(e)


