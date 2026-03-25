from __future__ import annotations

from typing import Any

from wazen.resources._base import AsyncResource, SyncResource


class Contacts(SyncResource):
    def check(self, session_id: str, *, phone: str) -> dict[str, Any]:
        return self._client.request("POST", f"/sessions/{session_id}/contacts/check", body={"phone": phone})

    def bulk_check(self, session_id: str, *, phones: list[str]) -> dict[str, Any]:
        return self._client.request("POST", f"/sessions/{session_id}/contacts/bulk-check", body={"phones": phones})


class AsyncContacts(AsyncResource):
    async def check(self, session_id: str, *, phone: str) -> dict[str, Any]:
        return await self._client.request("POST", f"/sessions/{session_id}/contacts/check", body={"phone": phone})

    async def bulk_check(self, session_id: str, *, phones: list[str]) -> dict[str, Any]:
        return await self._client.request("POST", f"/sessions/{session_id}/contacts/bulk-check", body={"phones": phones})
