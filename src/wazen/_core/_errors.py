from __future__ import annotations


class WazenApiError(Exception):
    """Raised when the Wazen API returns an error response."""

    def __init__(
        self,
        message: str,
        status_code: int,
        error_code: str,
        request_id: str = "",
        details: object = None,
    ) -> None:
        super().__init__(message)
        self._message = message
        self.status_code = status_code
        self.error_code = error_code
        self.request_id = request_id
        self.details = details

    @property
    def message(self) -> str:
        return self._message

    def __repr__(self) -> str:
        return (
            f"WazenApiError(status_code={self.status_code}, "
            f"error_code={self.error_code!r}, message={self._message!r})"
        )


class WazenTimeoutError(Exception):
    """Raised when a request exceeds the configured timeout."""

    def __init__(self, timeout: float) -> None:
        super().__init__(f"Request timed out after {timeout}s")


class WazenNetworkError(Exception):
    """Raised when a network error prevents the request from completing."""

    def __init__(self, cause: Exception | None = None) -> None:
        msg = str(cause) if cause else "Network request failed"
        super().__init__(msg)
        self.__cause__ = cause
