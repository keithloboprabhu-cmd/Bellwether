"""Scenario ⇄ URL encoding so every scenario is a shareable deep link.

The whole scenario is one query parameter `s`: base64url(zlib(JSON)). Keys are short to
keep links compact:
    m  mode ("industry")    i  industry slug     p  policy id
    in user inputs          a  edited assumptions {key: [low, base, high]}
    c  enabled components (list)
"""

from __future__ import annotations

import base64
import json
import zlib


def encode(state: dict) -> str:
    raw = json.dumps(state, separators=(",", ":"), sort_keys=True).encode()
    return base64.urlsafe_b64encode(zlib.compress(raw, 9)).decode().rstrip("=")


def decode(token: str) -> dict:
    """Inverse of encode(); returns {} for a malformed token rather than raising."""
    try:
        pad = "=" * (-len(token) % 4)
        return json.loads(zlib.decompress(base64.urlsafe_b64decode(token + pad)))
    except Exception:
        return {}
