from __future__ import annotations

from typing import Any

from wazen._core._http_client import AsyncHttpClient
from wazen.resources import (
    AsyncAccount,
    AsyncApiKeys,
    AsyncChannels,
    AsyncContacts,
    AsyncGroups,
    AsyncMessages,
    AsyncSessions,
    AsyncWarming,
    AsyncWebhooks,
)

_DEFAULT_BASE_URL = "https://wazen.dev/api/v1"
_DEFAULT_TIMEOUT = 30


class AsyncWazen:
    """Wazen API client (asynchronous)."""

    sessions: AsyncSessions
    messages: AsyncMessages
    contacts: AsyncContacts
    groups: AsyncGroups
    channels: AsyncChannels
    warming: AsyncWarming
    webhooks: AsyncWebhooks
    account: AsyncAccount
    api_keys: AsyncApiKeys

    def __init__(
        self,
        api_key: str,
        *,
        base_url: str = _DEFAULT_BASE_URL,
        timeout: float = _DEFAULT_TIMEOUT,
    ) -> None:
        if not api_key or not isinstance(api_key, str):
            raise ValueError("API key is required. Pass your Wazen API key as the first argument.")

        self._client = AsyncHttpClient(api_key, base_url, timeout)

        self.sessions = AsyncSessions(self._client)
        self.messages = AsyncMessages(self._client)
        self.contacts = AsyncContacts(self._client)
        self.groups = AsyncGroups(self._client)
        self.channels = AsyncChannels(self._client)
        self.warming = AsyncWarming(self._client)
        self.webhooks = AsyncWebhooks(self._client)
        self.account = AsyncAccount(self._client)
        self.api_keys = AsyncApiKeys(self._client)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> AsyncWazen:
        return self

    async def __aexit__(self, *args: Any) -> None:
        await self.close()
