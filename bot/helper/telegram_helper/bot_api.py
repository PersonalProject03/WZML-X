from aiohttp import ClientSession, ClientTimeout

from ... import LOGGER
from ...core.config_manager import Config


class TelegramBotApi:
    """Async client for Telegram Bot API 10.4+ HTTP methods (HTML Widgets, etc.)."""

    def __init__(self):
        self._session = None

    async def get_session(self):
        if self._session is None or self._session.closed:
            self._session = ClientSession(timeout=ClientTimeout(total=20))
        return self._session

    async def close(self):
        if self._session and not self._session.closed:
            await self._session.close()

    async def call_api(self, method: str, payload: dict):
        if not Config.BOT_TOKEN:
            LOGGER.warning("TelegramBotApi: BOT_TOKEN is missing!")
            return None

        url = f"https://api.telegram.org/bot{Config.BOT_TOKEN}/{method}"
        session = await self.get_session()
        try:
            async with session.post(url, json=payload) as resp:
                data = await resp.json()
                if not data.get("ok"):
                    LOGGER.warning(
                        f"TelegramBotApi [{method}] error: {data.get('description', data)}"
                    )
                return data
        except Exception as e:
            LOGGER.error(f"TelegramBotApi [{method}] failed: {e}", exc_info=True)
            return None

    async def send_widget(
        self,
        chat_id: int | str,
        html: str,
        chat_data: str = None,
    ):
        """Send an interactive HTML Widget message via Bot API 10.4 sendWidget.

        Currently supported by Telegram in private chats (user PM).
        """
        payload = {
            "chat_id": chat_id,
            "html": html,
        }
        if chat_data:
            payload["chat_data"] = chat_data

        return await self.call_api("sendWidget", payload)

    async def edit_widget_data(
        self,
        chat_id: int | str,
        message_id: int,
        chat_data: str,
    ):
        """Update dynamic state inside an existing widget via editMessageWidgetData."""
        payload = {
            "chat_id": chat_id,
            "message_id": message_id,
            "chat_data": chat_data,
        }
        return await self.call_api("editMessageWidgetData", payload)


bot_api = TelegramBotApi()
