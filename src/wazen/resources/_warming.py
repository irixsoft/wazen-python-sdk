from __future__ import annotations

from typing import Any

from wazen.resources._base import AsyncResource, SyncResource


class Warming(SyncResource):
    def start(self, session_id: str, *, contacts: list[dict[str, Any]]) -> dict[str, Any]:
        return self._client.request("POST", f"/sessions/{session_id}/warming", body={"contacts": contacts})

    def get_status(self, session_id: str) -> dict[str, Any]:
        return self._client.request("GET", f"/sessions/{session_id}/warming")

    def pause(self, session_id: str) -> dict[str, Any]:
        return self._client.request("POST", f"/sessions/{session_id}/warming/pause")

    def resume(self, session_id: str) -> dict[str, Any]:
        return self._client.request("POST", f"/sessions/{session_id}/warming/resume")

    def cancel(self, session_id: str) -> dict[str, Any]:
        return self._client.request("DELETE", f"/sessions/{session_id}/warming")


class AsyncWarming(AsyncResource):
    async def start(self, session_id: str, *, contacts: list[dict[str, Any]]) -> dict[str, Any]:
        return await self._client.request("POST", f"/sessions/{session_id}/warming", body={"contacts": contacts})

    async def get_status(self, session_id: str) -> dict[str, Any]:
        return await self._client.request("GET", f"/sessions/{session_id}/warming")

    async def pause(self, session_id: str) -> dict[str, Any]:
        return await self._client.request("POST", f"/sessions/{session_id}/warming/pause")

    async def resume(self, session_id: str) -> dict[str, Any]:
        return await self._client.request("POST", f"/sessions/{session_id}/warming/resume")

    async def cancel(self, session_id: str) -> dict[str, Any]:
        return await self._client.request("DELETE", f"/sessions/{session_id}/warming")
