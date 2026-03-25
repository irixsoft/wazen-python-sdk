from __future__ import annotations

from typing import Any

from wazen._core._types import PaginatedResponse
from wazen.resources._base import AsyncResource, SyncResource


class ApiKeys(SyncResource):
    def create(self, *, name: str) -> dict[str, Any]:
        return self._client.request("POST", "/api-keys", body={"name": name})

    def list(self, *, page: int | None = None, limit: int | None = None) -> PaginatedResponse:
        return self._client.request_paginated("GET", "/api-keys", query={"page": page, "limit": limit})

    def revoke(self, key_id: str) -> dict[str, Any]:
        return self._client.request("DELETE", f"/api-keys/{key_id}")


class AsyncApiKeys(AsyncResource):
    async def create(self, *, name: str) -> dict[str, Any]:
        return await self._client.request("POST", "/api-keys", body={"name": name})

    async def list(self, *, page: int | None = None, limit: int | None = None) -> PaginatedResponse:
        return await self._client.request_paginated("GET", "/api-keys", query={"page": page, "limit": limit})

    async def revoke(self, key_id: str) -> dict[str, Any]:
        return await self._client.request("DELETE", f"/api-keys/{key_id}")
