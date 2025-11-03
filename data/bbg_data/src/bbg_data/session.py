"""
Bloomberg API session management.

This module provides a context-managed wrapper around Bloomberg API sessions,
handling connection lifecycle, service access, and error handling.
"""

import logging
from collections.abc import Iterator
from contextlib import contextmanager
from typing import Any

import blpapi

from bbg_data.enums import ServiceType

logger = logging.getLogger(__name__)


class BloombergSessionError(Exception):
    """Raised when Bloomberg session operations fail."""

    pass


class BloombergSession:
    """
    Manages a Bloomberg API session with automatic resource cleanup.

    This class provides a high-level interface to the Bloomberg API,
    handling session lifecycle and service management.

    Example:
        >>> with BloombergSession() as session:
        ...     service = session.get_service(ServiceType.REFDATA)
        ...     # Use service for requests
    """

    def __init__(
        self,
        host: str = "localhost",
        port: int = 8194,
        timeout_ms: int = 5000,
    ) -> None:
        """
        Initialize Bloomberg session configuration.

        Args:
            host: Bloomberg API host (default: localhost for desktop terminal)
            port: Bloomberg API port (default: 8194)
            timeout_ms: Connection timeout in milliseconds

        Note:
            Session is not started until entering context manager or calling start()
        """
        self.host = host
        self.port = port
        self.timeout_ms = timeout_ms
        self._session: blpapi.Session | None = None
        self._services: dict[ServiceType, blpapi.Service] = {}

    def start(self) -> None:
        """
        Start the Bloomberg session.

        Raises:
            BloombergSessionError: If session fails to start
        """
        if self._session is not None:
            logger.warning("Session already started")
            return

        session_options = blpapi.SessionOptions()
        session_options.setServerHost(self.host)
        session_options.setServerPort(self.port)

        self._session = blpapi.Session(session_options)

        if not self._session.start():
            raise BloombergSessionError(
                f"Failed to start Bloomberg session at {self.host}:{self.port}. "
                "Ensure Bloomberg Terminal is running."
            )

        logger.info("Bloomberg session started successfully")

    def stop(self) -> None:
        """Stop the Bloomberg session and clean up resources."""
        if self._session is not None:
            self._session.stop()
            self._session = None
            self._services.clear()
            logger.info("Bloomberg session stopped")

    def get_service(self, service_type: ServiceType) -> blpapi.Service:
        """
        Get or open a Bloomberg service.

        Args:
            service_type: Type of service to open

        Returns:
            Bloomberg service object

        Raises:
            BloombergSessionError: If session not started or service fails to open
        """
        if self._session is None:
            raise BloombergSessionError("Session not started. Call start() first.")

        # Return cached service if already opened
        if service_type in self._services:
            return self._services[service_type]

        # Open the service
        if not self._session.openService(service_type.value):
            raise BloombergSessionError(f"Failed to open service: {service_type.value}")

        service = self._session.getService(service_type.value)
        self._services[service_type] = service
        logger.debug(f"Opened service: {service_type.value}")

        return service

    def send_request(
        self,
        request: blpapi.Request,
        identity: Any | None = None,
    ) -> None:
        """
        Send a request to Bloomberg.

        Args:
            request: Bloomberg request object
            identity: Optional authorization identity

        Raises:
            BloombergSessionError: If session not started
        """
        if self._session is None:
            raise BloombergSessionError("Session not started")

        self._session.sendRequest(request, identity=identity)

    def next_event(self, timeout_ms: int | None = None) -> blpapi.Event:
        """
        Get the next event from the session.

        Args:
            timeout_ms: Timeout in milliseconds (uses session default if None)

        Returns:
            Next Bloomberg event

        Raises:
            BloombergSessionError: If session not started
        """
        if self._session is None:
            raise BloombergSessionError("Session not started")

        timeout = timeout_ms if timeout_ms is not None else self.timeout_ms
        return self._session.nextEvent(timeout)

    def __enter__(self) -> "BloombergSession":
        """Context manager entry."""
        self.start()
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        """Context manager exit."""
        self.stop()


@contextmanager
def session(
    host: str = "localhost",
    port: int = 8194,
    timeout_ms: int = 5000,
) -> Iterator[BloombergSession]:
    """
    Context manager for Bloomberg sessions.

    Args:
        host: Bloomberg API host
        port: Bloomberg API port
        timeout_ms: Connection timeout in milliseconds

    Yields:
        Active Bloomberg session

    Example:
        >>> from bbg_data.session import session
        >>> from bbg_data.enums import ServiceType
        >>>
        >>> with session() as bbg:
        ...     service = bbg.get_service(ServiceType.REFDATA)
        ...     # Use service
    """
    bbg_session = BloombergSession(host=host, port=port, timeout_ms=timeout_ms)
    try:
        bbg_session.start()
        yield bbg_session
    finally:
        bbg_session.stop()
