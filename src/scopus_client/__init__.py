"""Async Scopus Client to interact with their HTTP interface. Includes automatic retry and API keys swapping."""

from .scopus_client import (
    InvalidStringError,
    OutOfAPIKeysError,
    Page,
    ScopusClient,
    TooManyJSONDecodeErrors,
    TooManyKeyErrors,
    TooManyScopusInternalErrors,
)

__all__ = [
    "ScopusClient",
    "OutOfAPIKeysError",
    "Page",
    "InvalidStringError",
    "TooManyJSONDecodeErrors",
    "TooManyKeyErrors",
    "TooManyScopusInternalErrors",
]
