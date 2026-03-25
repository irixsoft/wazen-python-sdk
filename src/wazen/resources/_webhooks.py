from __future__ import annotations

from typing import Any

from wazen._core._types import PaginatedResponse
from wazen.resources._base import AsyncResource, SyncResource, _filter_none


class Webhooks(SyncResource):
    def create(self, *, url: str, events: list[str], session_id: str | None = None) -> dict[str, Any]:
        body = _filter_none({"url": url, "events": events, "session_id": session_id})
        return self._client.request("POST", "/webhooks", body=body)

    def list(self, *, page: int | None = None, limit: int | None = None) -> PaginatedResponse:
        return self._client.request_paginated("GET", "/webhooks", query={"page": page, "limit": limit})

    def update(
        self,
        webhook_id: str,
        *,
        url: str | None = None,
        events: list[str] | None = None,
        enabled: bool | None = None,
        retry_config: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        body = _filter_none({"url": url, "events": events, "enabled": enabled, "retry_config": retry_config})
        return self._client.request("PUT", f"/webhooks/{webhook_id}", body=body)

    def delete(self, webhook_id: str) -> dict[str, Any]:
        return self._client.request("DELETE", f"/webhooks/{webhook_id}")

    def test(self, webhook_id: str, *, event_type: str | None = None) -> dict[str, Any]:
        body = _filter_none({"event_type": event_type})
        return self._client.request("POST", f"/webhooks/{webhook_id}/test", body=body or None)

    def get_logs(self, webhook_id: str) -> list[dict[str, Any]]:
        return self._client.request_list("GET", f"/webhooks/{webhook_id}/logs")


class AsyncWebhooks(AsyncResource):
    async def create(self, *, url: str, events: list[str], session_id: str | None = None) -> dict[str, Any]:
        body = _filter_none({"url": url, "events": events, "session_id": session_id})
        return await self._client.request("POST", "/webhooks", body=body)

    async def list(self, *, page: int | None = None, limit: int | None = None) -> PaginatedResponse:
        return await self._client.request_paginated("GET", "/webhooks", query={"page": page, "limit": limit})

    async def update(
        self,
        webhook_id: str,
        *,
        url: str | None = None,
        events: list[str] | None = None,
        enabled: bool | None = None,
        retry_config: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        body = _filter_none({"url": url, "events": events, "enabled": enabled, "retry_config": retry_config})
        return await self._client.request("PUT", f"/webhooks/{webhook_id}", body=body)

    async def delete(self, webhook_id: str) -> dict[str, Any]:
        return await self._client.request("DELETE", f"/webhooks/{webhook_id}")

    async def test(self, webhook_id: str, *, event_type: str | None = None) -> dict[str, Any]:
        body = _filter_none({"event_type": event_type})
        return await self._client.request("POST", f"/webhooks/{webhook_id}/test", body=body or None)

    async def get_logs(self, webhook_id: str) -> list[dict[str, Any]]:
        return await self._client.request_list("GET", f"/webhooks/{webhook_id}/logs")
