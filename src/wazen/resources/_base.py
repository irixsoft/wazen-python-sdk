from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from wazen._core._http_client import AsyncHttpClient, SyncHttpClient


def _filter_none(d: dict[str, Any]) -> dict[str, Any]:
    return {k: v for k, v in d.items() if v is not None}


class SyncResource:
    def __init__(self, client: SyncHttpClient) -> None:
        self._client = client


class AsyncResource:
    def __init__(self, client: AsyncHttpClient) -> None:
        self._client = client
