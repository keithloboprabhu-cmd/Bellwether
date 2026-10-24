"""Shared HTTP helpers: a polite rate limiter and retry-with-backoff GET.

SEC fair-access rules allow at most 10 requests/second and require a descriptive
User-Agent with a contact email; we throttle to 8/s to stay safely under the limit.
"""

from __future__ import annotations

import os
import threading
import time

import requests

DEFAULT_SEC_USER_AGENT = "PolicyShock Duke FMKT256 keith.loboprabhu@duke.edu"


def get_secret(name: str, default: str | None = None) -> str | None:
    """Read a setting from the environment, then Streamlit secrets, then `default`."""
    if os.environ.get(name):
        return os.environ[name]
    try:
        import streamlit as st

        if name in st.secrets:
            return str(st.secrets[name])
    except Exception:  # no secrets file, or not running under Streamlit
        pass
    return default


class RateLimiter:
    """Allow at most `rate` calls per second across threads (simple spacing limiter)."""

    def __init__(self, rate: float):
        self.min_interval = 1.0 / rate
        self._last = 0.0
        self._lock = threading.Lock()

    def wait(self) -> None:
        with self._lock:
            now = time.monotonic()
            sleep_for = self._last + self.min_interval - now
            if sleep_for > 0:
                time.sleep(sleep_for)
            self._last = time.monotonic()


def get_with_retry(
    url: str,
    *,
    headers: dict | None = None,
    params: dict | None = None,
    limiter: RateLimiter | None = None,
    retries: int = 4,
    timeout: float = 30,
) -> requests.Response:
    """GET `url`, retrying 429/5xx and network errors with exponential backoff.

    Raises the last error if every attempt fails; 4xx other than 429 fail immediately.
    """
    last_exc: Exception | None = None
    for attempt in range(retries + 1):
        if limiter:
            limiter.wait()
        try:
            resp = requests.get(url, headers=headers, params=params, timeout=timeout)
            if resp.status_code == 429 or resp.status_code >= 500:
                raise requests.HTTPError(f"HTTP {resp.status_code} for {url}", response=resp)
            resp.raise_for_status()
            return resp
        except requests.HTTPError as exc:
            status = exc.response.status_code if exc.response is not None else None
            if status is not None and status < 500 and status != 429:
                raise
            last_exc = exc
        except requests.RequestException as exc:
            last_exc = exc
        time.sleep(min(2**attempt, 16))
    assert last_exc is not None
    raise last_exc
