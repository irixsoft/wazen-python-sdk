from __future__ import annotations

from typing import Any

from wazen._core._types import PaginatedResponse
from wazen.resources._base import AsyncResource, SyncResource, _filter_none


class Sessions(SyncResource):
    def create(self, *, phone_number: str | None = None) -> dict[str, Any]:
        body = _filter_none({"phone_number": phone_number})
        return self._client.request("POST", "/sessions", body=body or None)

    def list(self, *, page: int | None = None, limit: int | None = None) -> PaginatedResponse:
        return self._client.request_paginated("GET", "/sessions", query={"page": page, "limit": limit})

    def get(self, session_id: str) -> dict[str, Any]:
        return self._client.request("GET", f"/sessions/{session_id}")

    def delete(self, session_id: str) -> dict[str, Any]:
        return self._client.request("DELETE", f"/sessions/{session_id}")

    def restart(self, session_id: str) -> dict[str, Any]:
        return self._client.request("POST", f"/sessions/{session_id}/restart")

    def get_qr(self, session_id: str) -> dict[str, Any]:
        return self._client.request("GET", f"/sessions/{session_id}/qr")

    def factory_reset(self, session_id: str) -> dict[str, Any]:
        return self._client.request("POST", f"/sessions/{session_id}/factory-reset")


class AsyncSessions(AsyncResource):
    async def create(self, *, phone_number: str | None = None) -> dict[str, Any]:
        body = _filter_none({"phone_number": phone_number})
        return await self._client.request("POST", "/sessions", body=body or None)

    async def list(self, *, page: int | None = None, limit: int | None = None) -> PaginatedResponse:
        return await self._client.request_paginated("GET", "/sessions", query={"page": page, "limit": limit})

    async def get(self, session_id: str) -> dict[str, Any]:
        return await self._client.request("GET", f"/sessions/{session_id}")

    async def delete(self, session_id: str) -> dict[str, Any]:
        return await self._client.request("DELETE", f"/sessions/{session_id}")

    async def restart(self, session_id: str) -> dict[str, Any]:
        return await self._client.request("POST", f"/sessions/{session_id}/restart")

    async def get_qr(self, session_id: str) -> dict[str, Any]:
        return await self._client.request("GET", f"/sessions/{session_id}/qr")

    async def factory_reset(self, session_id: str) -> dict[str, Any]:
        return await self._client.request("POST", f"/sessions/{session_id}/factory-reset")
