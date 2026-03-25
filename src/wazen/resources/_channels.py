from __future__ import annotations

from typing import Any

from wazen.resources._base import AsyncResource, SyncResource, _filter_none


class Channels(SyncResource):
    def create(self, session_id: str, *, name: str, description: str | None = None) -> dict[str, Any]:
        body = _filter_none({"name": name, "description": description})
        return self._client.request("POST", f"/sessions/{session_id}/channels", body=body)

    def lookup(self, session_id: str, *, jid: str | None = None, invite: str | None = None) -> dict[str, Any]:
        return self._client.request("GET", f"/sessions/{session_id}/channels", query={"jid": jid, "invite": invite})

    def get(self, session_id: str, channel_id: str) -> dict[str, Any]:
        return self._client.request("GET", f"/sessions/{session_id}/channels/{channel_id}")

    def update(self, session_id: str, channel_id: str, *, name: str | None = None, description: str | None = None) -> dict[str, Any]:
        body = _filter_none({"name": name, "description": description})
        return self._client.request("PUT", f"/sessions/{session_id}/channels/{channel_id}", body=body)

    def delete(self, session_id: str, channel_id: str) -> dict[str, Any]:
        return self._client.request("DELETE", f"/sessions/{session_id}/channels/{channel_id}")

    def send_message(self, session_id: str, channel_id: str, *, type: str, content: str | None = None, media_url: str | None = None) -> dict[str, Any]:
        body = _filter_none({"type": type, "content": content, "media_url": media_url})
        return self._client.request("POST", f"/sessions/{session_id}/channels/{channel_id}/messages", body=body)

    def list_messages(self, session_id: str, channel_id: str, *, count: int | None = None, since: int | None = None, after: int | None = None) -> list[dict[str, Any]]:
        return self._client.request_list("GET", f"/sessions/{session_id}/channels/{channel_id}/messages", query={"count": count, "since": since, "after": after})

    def react(self, session_id: str, channel_id: str, message_id: str, *, reaction: str | None = None) -> dict[str, Any]:
        body = _filter_none({"reaction": reaction}) if reaction is not None else None
        return self._client.request("POST", f"/sessions/{session_id}/channels/{channel_id}/messages/{message_id}/react", body=body)

    def follow(self, session_id: str, channel_id: str) -> dict[str, Any]:
        return self._client.request("POST", f"/sessions/{session_id}/channels/{channel_id}/follow")

    def unfollow(self, session_id: str, channel_id: str) -> dict[str, Any]:
        return self._client.request("DELETE", f"/sessions/{session_id}/channels/{channel_id}/follow")

    def mute(self, session_id: str, channel_id: str) -> dict[str, Any]:
        return self._client.request("POST", f"/sessions/{session_id}/channels/{channel_id}/mute")

    def unmute(self, session_id: str, channel_id: str) -> dict[str, Any]:
        return self._client.request("DELETE", f"/sessions/{session_id}/channels/{channel_id}/mute")


class AsyncChannels(AsyncResource):
    async def create(self, session_id: str, *, name: str, description: str | None = None) -> dict[str, Any]:
        body = _filter_none({"name": name, "description": description})
        return await self._client.request("POST", f"/sessions/{session_id}/channels", body=body)

    async def lookup(self, session_id: str, *, jid: str | None = None, invite: str | None = None) -> dict[str, Any]:
        return await self._client.request("GET", f"/sessions/{session_id}/channels", query={"jid": jid, "invite": invite})

    async def get(self, session_id: str, channel_id: str) -> dict[str, Any]:
        return await self._client.request("GET", f"/sessions/{session_id}/channels/{channel_id}")

    async def update(self, session_id: str, channel_id: str, *, name: str | None = None, description: str | None = None) -> dict[str, Any]:
        body = _filter_none({"name": name, "description": description})
        return await self._client.request("PUT", f"/sessions/{session_id}/channels/{channel_id}", body=body)

    async def delete(self, session_id: str, channel_id: str) -> dict[str, Any]:
        return await self._client.request("DELETE", f"/sessions/{session_id}/channels/{channel_id}")

    async def send_message(self, session_id: str, channel_id: str, *, type: str, content: str | None = None, media_url: str | None = None) -> dict[str, Any]:
        body = _filter_none({"type": type, "content": content, "media_url": media_url})
        return await self._client.request("POST", f"/sessions/{session_id}/channels/{channel_id}/messages", body=body)

    async def list_messages(self, session_id: str, channel_id: str, *, count: int | None = None, since: int | None = None, after: int | None = None) -> list[dict[str, Any]]:
        return await self._client.request_list("GET", f"/sessions/{session_id}/channels/{channel_id}/messages", query={"count": count, "since": since, "after": after})

    async def react(self, session_id: str, channel_id: str, message_id: str, *, reaction: str | None = None) -> dict[str, Any]:
        body = _filter_none({"reaction": reaction}) if reaction is not None else None
        return await self._client.request("POST", f"/sessions/{session_id}/channels/{channel_id}/messages/{message_id}/react", body=body)

    async def follow(self, session_id: str, channel_id: str) -> dict[str, Any]:
        return await self._client.request("POST", f"/sessions/{session_id}/channels/{channel_id}/follow")

    async def unfollow(self, session_id: str, channel_id: str) -> dict[str, Any]:
        return await self._client.request("DELETE", f"/sessions/{session_id}/channels/{channel_id}/follow")

    async def mute(self, session_id: str, channel_id: str) -> dict[str, Any]:
        return await self._client.request("POST", f"/sessions/{session_id}/channels/{channel_id}/mute")

    async def unmute(self, session_id: str, channel_id: str) -> dict[str, Any]:
        return await self._client.request("DELETE", f"/sessions/{session_id}/channels/{channel_id}/mute")
