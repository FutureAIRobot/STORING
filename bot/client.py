from . import API_HASH, APP_ID, LOGGER, \
    USER_SESSION

from pyrogram import Client, enums, __version__


class AutoUser(Client):    
    def __init__(self):
        super().__init__(
            name="autobot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={
                "root": "AutoForward/plugins"
            },
            workers=200,
            session_string=USER_SESSION,
            sleep_threshold=10
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        user_details = await self.get_me()
        self.set_parse_mode(enums.ParseMode.HTML)
        self.LOGGER(__name__).info(
            f"@{user_details.username}  started! "
        )

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("User stopped. Bye.")
