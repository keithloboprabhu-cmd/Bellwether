"""Number formatting used by the UI and the template narratives.

Inputs are model units: $ in millions, rates as fractions. Signed helpers use a true
minus sign (−) so negative numbers read cleanly in prose.
"""

from __future__ import annotations

MINUS = "−"


def _sign(x: float, signed: bool) -> str:
    if x < 0:
        return MINUS
    return "+" if signed and x > 0 else ""


def money(musd: float | None, signed: bool = False) -> str:
    """$ millions → '$1.2B', '$340M', '$12.5M', '−$2.3B'."""
    if musd is None:
        return "n/m"
    a = abs(musd)
    if a >= 1_000_000:
        body = f"${a / 1_000_000:.2f}T"
    elif a >= 1_000:
        body = f"${a / 1_000:.1f}B"
    elif a >= 10:
        body = f"${a:,.0f}M"
    else:
        body = f"${a:.1f}M"
    return _sign(musd, signed) + body


def pct(x: float | None, signed: bool = False, digits: int | None = None) -> str:
    """Fraction → percent: 0.021 → '2.1%' (or '+2.1%').

    One decimal by default; two when |x| < 1% so small effects don't print as 0.0%.
    """
    if x is None:
        return "n/m"
    if digits is None:
        digits = 2 if 0 < abs(x) < 0.01 else 1
    return _sign(x, signed) + f"{abs(x) * 100:.{digits}f}%"


def bps(x: float | None, signed: bool = True) -> str:
    """Basis points as an integer: −340.2 → '−340 bps'."""
    if x is None:
        return "n/m"
    return _sign(round(x), signed) + f"{abs(round(x)):,} bps"


def per_share(x: float | None, signed: bool = True) -> str:
    if x is None:
        return "n/m"
    return _sign(x, signed) + f"${abs(x):.2f}"


def number(x: float | None, unit: str = "") -> str:
    """Plain value with its unit, trimming trailing zeros: 0.60 fraction → '0.6'."""
    if x is None:
        return "n/m"
    s = f"{x:,.4f}".rstrip("0").rstrip(".")
    return f"{s} {unit}".strip() if unit and unit not in ("fraction", "number", "multiple") else s
