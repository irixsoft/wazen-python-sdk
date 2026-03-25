from __future__ import annotations

from typing import Any

from wazen.resources._base import AsyncResource, SyncResource


class Account(SyncResource):
    def get(self) -> dict[str, Any]:
        return self._client.request("GET", "/account")

    def get_usage(self) -> dict[str, Any]:
        return self._client.request("GET", "/usage")


class AsyncAccount(AsyncResource):
    async def get(self) -> dict[str, Any]:
        return await self._client.request("GET", "/account")

    async def get_usage(self) -> dict[str, Any]:
        return await self._client.request("GET", "/usage")
