"""Turn a change in EPS into an implied share-price change (constant-multiple method).

    permanent  → dP = dEPS × P/E            (the market capitalises a lasting change)
    one_time   → dP = dEPS                  (a one-off bump is worth roughly itself)
    years:N    → dP = dEPS × AF(N, r)       (PV of N years of the change, r = 9% default)

When P/E isn't meaningful (EPS ≤ 0) a permanent change has no implied price ("n/m").
"""

from __future__ import annotations

DEFAULT_DISCOUNT_RATE = 0.09


def annuity_factor(years: int, rate: float = DEFAULT_DISCOUNT_RATE) -> float:
    """PV of $1 a year for `years` years, first payment in one year."""
    return sum(1 / (1 + rate) ** k for k in range(1, years + 1))


def earnings_multiple(persistence: str, pe: float | None, rate: float = DEFAULT_DISCOUNT_RATE) -> float | None:
    """$ of value per $1 of annual EPS change, or None when not meaningful."""
    if persistence == "permanent":
        return pe if (pe is not None and pe > 0) else None
    if persistence == "one_time":
        return 1.0
    if persistence.startswith("years:"):
        return annuity_factor(int(persistence.split(":")[1]), rate)
    raise ValueError(f"unknown persistence {persistence!r}")


def persistence_label(persistence: str) -> str:
    if persistence == "permanent":
        return "permanent (valued at the current P/E)"
    if persistence == "one_time":
        return "one-time (valued at roughly its own size)"
    n = int(persistence.split(":")[1])
    return f"lasting {n} year{'s' if n != 1 else ''} (PV at {DEFAULT_DISCOUNT_RATE:.0%})"
