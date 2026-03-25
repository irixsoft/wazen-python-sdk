from __future__ import annotations

from typing import Any

from wazen._core._types import PaginatedResponse
from wazen.resources._base import AsyncResource, SyncResource, _filter_none


class Messages(SyncResource):
    def send(
        self,
        session_id: str,
        *,
        to: str,
        type: str,
        content: str | None = None,
        media_url: str | None = None,
        media_base64: str | None = None,
    ) -> dict[str, Any]:
        body = _filter_none({
            "to": to,
            "type": type,
            "content": content,
            "media_url": media_url,
            "media_base64": media_base64,
        })
        return self._client.request("POST", f"/sessions/{session_id}/messages", body=body)

    def list(
        self,
        session_id: str,
        *,
        page: int | None = None,
        limit: int | None = None,
        direction: str | None = None,
        type: str | None = None,
    ) -> PaginatedResponse:
        return self._client.request_paginated(
            "GET",
            f"/sessions/{session_id}/messages",
            query={"page": page, "limit": limit, "direction": direction, "type": type},
        )

    def get(self, session_id: str, message_id: str) -> dict[str, Any]:
        return self._client.request("GET", f"/sessions/{session_id}/messages/{message_id}")


class AsyncMessages(AsyncResource):
    async def send(
        self,
        session_id: str,
        *,
        to: str,
        type: str,
        content: str | None = None,
        media_url: str | None = None,
        media_base64: str | None = None,
    ) -> dict[str, Any]:
        body = _filter_none({
            "to": to,
            "type": type,
            "content": content,
            "media_url": media_url,
            "media_base64": media_base64,
        })
        return await self._client.request("POST", f"/sessions/{session_id}/messages", body=body)

    async def list(
        self,
        session_id: str,
        *,
        page: int | None = None,
        limit: int | None = None,
        direction: str | None = None,
        type: str | None = None,
    ) -> PaginatedResponse:
        return await self._client.request_paginated(
            "GET",
            f"/sessions/{session_id}/messages",
            query={"page": page, "limit": limit, "direction": direction, "type": type},
        )

    async def get(self, session_id: str, message_id: str) -> dict[str, Any]:
        return await self._client.request("GET", f"/sessions/{session_id}/messages/{message_id}")
