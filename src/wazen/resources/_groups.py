from __future__ import annotations

from typing import Any

from wazen.resources._base import AsyncResource, SyncResource, _filter_none


class Groups(SyncResource):
    def list(self, session_id: str) -> list[dict[str, Any]]:
        return self._client.request_list("GET", f"/sessions/{session_id}/groups")

    def create(self, session_id: str, *, subject: str, participants: list[str]) -> dict[str, Any]:
        return self._client.request("POST", f"/sessions/{session_id}/groups", body={"subject": subject, "participants": participants})

    def get(self, session_id: str, group_id: str) -> dict[str, Any]:
        return self._client.request("GET", f"/sessions/{session_id}/groups/{group_id}")

    def update(self, session_id: str, group_id: str, *, subject: str | None = None, description: str | None = None) -> dict[str, Any]:
        body = _filter_none({"subject": subject, "description": description})
        return self._client.request("PUT", f"/sessions/{session_id}/groups/{group_id}", body=body)

    def leave(self, session_id: str, group_id: str) -> dict[str, Any]:
        return self._client.request("DELETE", f"/sessions/{session_id}/groups/{group_id}")

    def manage_participants(self, session_id: str, group_id: str, *, action: str, participants: list[str]) -> dict[str, Any]:
        return self._client.request("POST", f"/sessions/{session_id}/groups/{group_id}/participants", body={"action": action, "participants": participants})

    def update_settings(
        self,
        session_id: str,
        group_id: str,
        *,
        setting: str | None = None,
        ephemeral: int | None = None,
        member_add_mode: str | None = None,
        join_approval: str | None = None,
    ) -> dict[str, Any]:
        body = _filter_none({"setting": setting, "ephemeral": ephemeral, "member_add_mode": member_add_mode, "join_approval": join_approval})
        return self._client.request("PUT", f"/sessions/{session_id}/groups/{group_id}/settings", body=body)

    def send_message(self, session_id: str, group_id: str, *, type: str, content: str | None = None, media_url: str | None = None) -> dict[str, Any]:
        body = _filter_none({"type": type, "content": content, "media_url": media_url})
        return self._client.request("POST", f"/sessions/{session_id}/groups/{group_id}/messages", body=body)

    def get_invite(self, session_id: str, group_id: str) -> dict[str, Any]:
        return self._client.request("GET", f"/sessions/{session_id}/groups/{group_id}/invite")

    def revoke_invite(self, session_id: str, group_id: str) -> dict[str, Any]:
        return self._client.request("DELETE", f"/sessions/{session_id}/groups/{group_id}/invite")

    def get_requests(self, session_id: str, group_id: str) -> list[dict[str, Any]]:
        return self._client.request_list("GET", f"/sessions/{session_id}/groups/{group_id}/requests")

    def manage_requests(self, session_id: str, group_id: str, *, participants: list[str], action: str) -> dict[str, Any]:
        return self._client.request("POST", f"/sessions/{session_id}/groups/{group_id}/requests", body={"participants": participants, "action": action})

    def get_invite_info(self, session_id: str, *, code: str) -> dict[str, Any]:
        return self._client.request("GET", f"/sessions/{session_id}/groups/invite-info", query={"code": code})

    def join(self, session_id: str, *, code: str) -> dict[str, Any]:
        return self._client.request("POST", f"/sessions/{session_id}/groups/join", body={"code": code})


class AsyncGroups(AsyncResource):
    async def list(self, session_id: str) -> list[dict[str, Any]]:
        return await self._client.request_list("GET", f"/sessions/{session_id}/groups")

    async def create(self, session_id: str, *, subject: str, participants: list[str]) -> dict[str, Any]:
        return await self._client.request("POST", f"/sessions/{session_id}/groups", body={"subject": subject, "participants": participants})

    async def get(self, session_id: str, group_id: str) -> dict[str, Any]:
        return await self._client.request("GET", f"/sessions/{session_id}/groups/{group_id}")

    async def update(self, session_id: str, group_id: str, *, subject: str | None = None, description: str | None = None) -> dict[str, Any]:
        body = _filter_none({"subject": subject, "description": description})
        return await self._client.request("PUT", f"/sessions/{session_id}/groups/{group_id}", body=body)

    async def leave(self, session_id: str, group_id: str) -> dict[str, Any]:
        return await self._client.request("DELETE", f"/sessions/{session_id}/groups/{group_id}")

    async def manage_participants(self, session_id: str, group_id: str, *, action: str, participants: list[str]) -> dict[str, Any]:
        return await self._client.request("POST", f"/sessions/{session_id}/groups/{group_id}/participants", body={"action": action, "participants": participants})

    async def update_settings(
        self,
        session_id: str,
        group_id: str,
        *,
        setting: str | None = None,
        ephemeral: int | None = None,
        member_add_mode: str | None = None,
        join_approval: str | None = None,
    ) -> dict[str, Any]:
        body = _filter_none({"setting": setting, "ephemeral": ephemeral, "member_add_mode": member_add_mode, "join_approval": join_approval})
        return await self._client.request("PUT", f"/sessions/{session_id}/groups/{group_id}/settings", body=body)

    async def send_message(self, session_id: str, group_id: str, *, type: str, content: str | None = None, media_url: str | None = None) -> dict[str, Any]:
        body = _filter_none({"type": type, "content": content, "media_url": media_url})
        return await self._client.request("POST", f"/sessions/{session_id}/groups/{group_id}/messages", body=body)

    async def get_invite(self, session_id: str, group_id: str) -> dict[str, Any]:
        return await self._client.request("GET", f"/sessions/{session_id}/groups/{group_id}/invite")

    async def revoke_invite(self, session_id: str, group_id: str) -> dict[str, Any]:
        return await self._client.request("DELETE", f"/sessions/{session_id}/groups/{group_id}/invite")

    async def get_requests(self, session_id: str, group_id: str) -> list[dict[str, Any]]:
        return await self._client.request_list("GET", f"/sessions/{session_id}/groups/{group_id}/requests")

    async def manage_requests(self, session_id: str, group_id: str, *, participants: list[str], action: str) -> dict[str, Any]:
        return await self._client.request("POST", f"/sessions/{session_id}/groups/{group_id}/requests", body={"participants": participants, "action": action})

    async def get_invite_info(self, session_id: str, *, code: str) -> dict[str, Any]:
        return await self._client.request("GET", f"/sessions/{session_id}/groups/invite-info", query={"code": code})

    async def join(self, session_id: str, *, code: str) -> dict[str, Any]:
        return await self._client.request("POST", f"/sessions/{session_id}/groups/join", body={"code": code})
