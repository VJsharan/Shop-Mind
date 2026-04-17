"""
ShopMind In-Memory Cache.

TTLCache with thread-safe get/set helpers for caching Gemini responses.
Cache keys are SHA256 hashes of query strings to normalize input.
"""

import hashlib
import threading
from typing import Any

from cachetools import TTLCache

_cache: TTLCache = TTLCache(maxsize=256, ttl=300)
_lock: threading.Lock = threading.Lock()


def make_cache_key(raw: str) -> str:
    """Generate a SHA256 cache key from a raw string."""
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def get_cached(key: str) -> Any | None:
    """Thread-safe cache lookup. Returns None on miss."""
    with _lock:
        return _cache.get(key, None)


def set_cached(key: str, value: Any) -> None:
    """Thread-safe cache insert."""
    with _lock:
        _cache[key] = value


def clear_cache() -> None:
    """Clear the entire cache. Used in testing."""
    with _lock:
        _cache.clear()
