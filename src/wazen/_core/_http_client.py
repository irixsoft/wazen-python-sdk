from __future__ import annotations

from typing import Any

import httpx

from wazen._core._errors import WazenApiError, WazenNetworkError, WazenTimeoutError
from wazen._core._types import PaginatedResponse
from wazen._version import __version__

_USER_AGENT = f"wazen-python/{__version__}"


def _filter_none(d: dict[str, Any]) -> dict[str, Any]:
    return {k: v for k, v in d.items() if v is not None}


def _build_query(params: dict[str, Any] | None) -> dict[str, str] | None:
    if not params:
        return None
    filtered = {k: str(v) for k, v in params.items() if v is not None}
    return filtered or None


def _handle_response(response: httpx.Response) -> dict[str, Any]:
    try:
        body = response.json()
    except Exception:
        raise WazenApiError(
            f"Unexpected response format (HTTP {response.status_code})",
            response.status_code,
            "INTERNAL_ERROR",
        )

    if not body.get("success"):
        error = body.get("error", {})
        meta = body.get("meta", {})
        raise WazenApiError(
            message=error.get("message", "Unknown error"),
            status_code=response.status_code,
            error_code=error.get("code", "INTERNAL_ERROR"),
            request_id=meta.get("request_id", ""),
            details=error.get("details"),
        )

    return body


class SyncHttpClient:
    def __init__(self, api_key: str, base_url: str, timeout: float) -> None:
        self._timeout = timeout
        self._client = httpx.Client(
            base_url=base_url,
            timeout=timeout,
            headers={
                "Authorization": f"Bearer {api_key}",
                "Accept": "application/json",
                "User-Agent": _USER_AGENT,
            },
        )

    def request(
        self,
        method: str,
        path: str,
        *,
        body: dict[str, Any] | None = None,
        query: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        body = _handle_response(self._execute(method, path, body=body, query=query))
        return body["data"]

    def request_paginated(
        self,
        method: str,
        path: str,
        *,
        query: dict[str, Any] | None = None,
    ) -> PaginatedResponse:
        body = _handle_response(self._execute(method, path, query=query))
        pagination = body.get("meta", {}).get("pagination", {})
        return PaginatedResponse(data=body["data"], pagination=pagination)

    def request_list(
        self,
        method: str,
        path: str,
        *,
        query: dict[str, Any] | None = None,
    ) -> list[dict[str, Any]]:
        body = _handle_response(self._execute(method, path, query=query))
        return body["data"]

    def close(self) -> None:
        self._client.close()

    def _execute(
        self,
        method: str,
        path: str,
        *,
        body: dict[str, Any] | None = None,
        query: dict[str, Any] | None = None,
    ) -> httpx.Response:
        json_body = _filter_none(body) if body else None
        params = _build_query(query)
        try:
            return self._client.request(method, path, json=json_body, params=params)
        except httpx.TimeoutException:
            raise WazenTimeoutError(self._timeout)
        except httpx.HTTPError as exc:
            raise WazenNetworkError(exc)


class AsyncHttpClient:
    def __init__(self, api_key: str, base_url: str, timeout: float) -> None:
        self._timeout = timeout
        self._client = httpx.AsyncClient(
            base_url=base_url,
            timeout=timeout,
            headers={
                "Authorization": f"Bearer {api_key}",
                "Accept": "application/json",
                "User-Agent": _USER_AGENT,
            },
        )

    async def request(
        self,
        method: str,
        path: str,
        *,
        body: dict[str, Any] | None = None,
        query: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        body = _handle_response(
            await self._execute(method, path, body=body, query=query)
        )
        return body["data"]

    async def request_paginated(
        self,
        method: str,
        path: str,
        *,
        query: dict[str, Any] | None = None,
    ) -> PaginatedResponse:
        body = _handle_response(await self._execute(method, path, query=query))
        pagination = body.get("meta", {}).get("pagination", {})
        return PaginatedResponse(data=body["data"], pagination=pagination)

    async def request_list(
        self,
        method: str,
        path: str,
        *,
        query: dict[str, Any] | None = None,
    ) -> list[dict[str, Any]]:
        body = _handle_response(await self._execute(method, path, query=query))
        return body["data"]

    async def close(self) -> None:
        await self._client.aclose()

    async def _execute(
        self,
        method: str,
        path: str,
        *,
        body: dict[str, Any] | None = None,
        query: dict[str, Any] | None = None,
    ) -> httpx.Response:
        json_body = _filter_none(body) if body else None
        params = _build_query(query)
        try:
            return await self._client.request(
                method, path, json=json_body, params=params
            )
        except httpx.TimeoutException:
            raise WazenTimeoutError(self._timeout)
        except httpx.HTTPError as exc:
            raise WazenNetworkError(exc)
