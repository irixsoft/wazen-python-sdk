from __future__ import annotations

from typing import Any

from wazen._core._http_client import SyncHttpClient
from wazen.resources import (
    Account,
    ApiKeys,
    Channels,
    Contacts,
    Groups,
    Messages,
    Sessions,
    Warming,
    Webhooks,
)

_DEFAULT_BASE_URL = "https://wazen.dev/api/v1"
_DEFAULT_TIMEOUT = 30


class Wazen:
    """Wazen API client (synchronous)."""

    sessions: Sessions
    messages: Messages
    contacts: Contacts
    groups: Groups
    channels: Channels
    warming: Warming
    webhooks: Webhooks
    account: Account
    api_keys: ApiKeys

    def __init__(
        self,
        api_key: str,
        *,
        base_url: str = _DEFAULT_BASE_URL,
        timeout: float = _DEFAULT_TIMEOUT,
    ) -> None:
        if not api_key or not isinstance(api_key, str):
            raise ValueError("API key is required. Pass your Wazen API key as the first argument.")

        self._client = SyncHttpClient(api_key, base_url, timeout)

        self.sessions = Sessions(self._client)
        self.messages = Messages(self._client)
        self.contacts = Contacts(self._client)
        self.groups = Groups(self._client)
        self.channels = Channels(self._client)
        self.warming = Warming(self._client)
        self.webhooks = Webhooks(self._client)
        self.account = Account(self._client)
        self.api_keys = ApiKeys(self._client)

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> Wazen:
        return self

    def __exit__(self, *args: Any) -> None:
        self.close()
