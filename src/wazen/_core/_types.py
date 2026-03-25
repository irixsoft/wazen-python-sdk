from __future__ import annotations

from typing import Any


class PaginatedResponse:
    """Paginated list response with data and pagination metadata."""

    def __init__(self, data: list[dict[str, Any]], pagination: dict[str, Any]) -> None:
        self.data = data
        self.pagination = pagination

    def __repr__(self) -> str:
        return (
            f"PaginatedResponse(data=[...{len(self.data)} items], "
            f"pagination={self.pagination})"
        )
