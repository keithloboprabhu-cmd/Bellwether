"""Aggregate channel deltas into a company's shocked P&L, EPS and implied value.

    dEBIT = Σ channel dEBIT                 (each channel: dR − dC − dOpex, or its own dEBIT)
    dPTI  = dEBIT − dInt
    t'    = t + Σ dTaxRate                  (clamped to [0, 1])
    dNI   = [(PTI + dPTI)(1 − t') − PTI(1 − t) + Σ dNI_direct] × parent share

dNI is computed against the *model's* baseline PTI·(1 − t), not reported NI, so a
zero shock always gives exactly zero (reported NI also contains minority interests,
discontinued ops, etc.). The total splits exactly into per-channel pieces:

    dNI = Σ_c (dEBIT_c − dInt_c)(1 − t')  +  PTI·(t − t')  +  Σ_c dNI_direct_c

with the PTI·(t − t') term assigned to the channels that changed the tax rate. Each
piece is valued with its own channel's persistence (valuation.py), then summed.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from policyshock.engine.channels import Delta
from policyshock.engine.valuation import DEFAULT_DISCOUNT_RATE, earnings_multiple

# Baseline fields a policy expression may reference as baseline.<field>.
BASELINE_FIELDS = {
    "revenue",
    "cost_of_revenue",
    "contribution_margin",
    "operating_income",
    "interest_expense",
    "pretax_income",
    "effective_tax_rate",
    "net_income",
    "diluted_shares",
    "eps_diluted",
    "total_debt",
    "da",
    "net_interest_income",
    "total_assets",
    "shares_outstanding",
    "price",
    "pe",
    "market_cap",
}


@dataclass
class ChannelOutcome:
    """One channel's effect on one company, ready for display and attribution."""

    label: str
    family: str
    persistence: str
    delta: Delta
    dNI: float = 0.0
    dP: float | None = 0.0
    exposure_refs: tuple[str, ...] = ()  # exposure keys this channel's params use (for reasons)


@dataclass
class CompanyResult:
    ticker: str
    name: str
    role: str
    baseline: dict
    dR: float
    dC: float
    dOpex: float
    dEBIT: float
    dInt: float
    dPTI: float
    tax_rate: float
    tax_rate_new: float
    dNI: float
    dEPS: float
    dEPS_pct: float | None  # None when baseline EPS ≤ 0 (n/m)
    dP: float | None  # implied $ per share; None when n/m
    dP_pct: float | None
    d_mcap: float | None  # $M
    d_margin_bps: float | None
    outcomes: list[ChannelOutcome] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)

    @property
    def dominant(self) -> ChannelOutcome | None:
        """The channel with the largest value effect per share (EPS effect when value is n/m)."""
        if not self.outcomes:
            return None
        S = self.baseline["diluted_shares"]
        return max(self.outcomes, key=lambda o: abs(o.dP) if o.dP is not None else abs(o.dNI / S))

    def family_dNI(self) -> dict[str, float]:
        out: dict[str, float] = {}
        for o in self.outcomes:
            out[o.family] = out.get(o.family, 0.0) + o.dNI
        return out

    @property
    def rank_value(self) -> float:
        """Ranking key for winners/losers: implied price %, falling back to dEPS %."""
        if self.dP_pct is not None:
            return self.dP_pct
        return self.dEPS_pct if self.dEPS_pct is not None else 0.0


def aggregate(
    b: dict,
    outcomes: list[ChannelOutcome],
    role: str = "neutral",
    discount_rate: float = DEFAULT_DISCOUNT_RATE,
) -> CompanyResult:
    """Combine channel outcomes for one company (mutates outcomes' dNI / dP)."""
    R, EBIT = b["revenue"], b["operating_income"]
    PTI, t = b["pretax_income"], b["effective_tax_rate"]
    S = b["diluted_shares"]
    eps, price, pe = b.get("eps_diluted"), b.get("price"), b.get("pe")
    shares_out = b.get("shares_outstanding") or S

    d = [o.delta for o in outcomes]
    dR = sum(x.dR for x in d)
    dEBIT = sum(x.ebit for x in d)
    dInt = sum(x.dInt for x in d)
    dPTI = dEBIT - dInt
    d_tax = sum(x.dTaxRate for x in d)
    t_new = min(max(t + d_tax, 0.0), 1.0)
    direct = sum(x.dNI_direct for x in d)
    # parent_share < 1 when minority partners own part of consolidated profit (see scenarios.py)
    ps = b.get("parent_share", 1.0)
    dNI = ((PTI + dPTI) * (1 - t_new) - PTI * (1 - t) + direct) * ps

    # exact per-channel attribution (see module docstring)
    rate_effect = PTI * (t - t_new)
    for o in outcomes:
        share = (o.delta.dTaxRate / d_tax) if d_tax else 0.0
        o.dNI = ((o.delta.ebit - o.delta.dInt) * (1 - t_new) + o.delta.dNI_direct + rate_effect * share) * ps

    # valuation: each piece at its own persistence, plus direct value effects
    dP: float | None = 0.0
    for o in outcomes:
        mult = earnings_multiple(o.persistence, pe, discount_rate)
        piece = 0.0
        if o.dNI:
            piece = None if mult is None else (o.dNI / S) * mult
        if piece is not None:
            if o.delta.dValue_pv:
                piece += o.delta.dValue_pv / shares_out
            if o.delta.dValue_pct and price is not None:
                piece += o.delta.dValue_pct * price
        o.dP = piece
        dP = None if (dP is None or piece is None) else dP + piece
    if price is None:
        dP = None

    dEPS = dNI / S
    eps_pct = dEPS / eps if (eps is not None and eps > 0) else None
    dP_pct = dP / price if (dP is not None and price) else None
    margin_bps = None
    if R and R + dR:
        margin_bps = ((EBIT + dEBIT) / (R + dR) - EBIT / R) * 10_000

    notes = [n for x in d for n in x.notes]
    if eps is not None and eps <= 0:
        notes.append("baseline EPS ≤ 0: ΔEPS % and P/E-based value are not meaningful")
    return CompanyResult(
        ticker=b["ticker"],
        name=b["name"],
        role=role,
        baseline=b,
        dR=dR,
        dC=sum(x.dC for x in d),
        dOpex=sum(x.dOpex for x in d),
        dEBIT=dEBIT,
        dInt=dInt,
        dPTI=dPTI,
        tax_rate=t,
        tax_rate_new=t_new,
        dNI=dNI,
        dEPS=dEPS,
        dEPS_pct=eps_pct,
        dP=dP,
        dP_pct=dP_pct,
        d_mcap=None if dP is None else dP * shares_out,
        d_margin_bps=margin_bps,
        outcomes=outcomes,
        notes=notes,
    )
