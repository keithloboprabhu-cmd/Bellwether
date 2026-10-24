"""The six shock channels: tax, cost, demand, price, financing, government spending.

Each channel type is a pure function `(baseline, params) -> Delta`. `baseline` is a
company's model-ready baseline ($ millions; see model.BASELINE_FIELDS) and `params` are
the already-evaluated numbers from the policy config. Channels never touch the tax rate
on pretax income or compute EPS themselves; that happens once, in model.aggregate(),
so effects can't be double counted.

Sign convention: deltas are changes vs. baseline; `dC` and `dOpex` are cost increases
(they reduce EBIT), `dInt` is an increase in interest expense.
Rates and shares are fractions (0.25 = 25%) unless a param name ends in `_bps`.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, Mapping

FAMILIES = ("tax", "cost", "demand", "price", "financing", "government")


@dataclass
class Delta:
    """Change in one company's P&L (and value) caused by one channel, $ millions."""

    dR: float = 0.0
    dC: float = 0.0
    dOpex: float = 0.0
    dEBIT: float | None = None  # explicit EBIT change; when None, dEBIT = dR − dC − dOpex
    dInt: float = 0.0
    dTaxRate: float = 0.0  # change in effective tax rate (fraction points)
    dNI_direct: float = 0.0  # after-tax items such as tax credits
    dValue_pv: float = 0.0  # PV added to equity value directly (e.g. tax-deferral timing), $M
    dValue_pct: float = 0.0  # direct % change in equity value (REIT NAV, bank capital)
    notes: list[str] = field(default_factory=list)

    @property
    def ebit(self) -> float:
        return self.dR - self.dC - self.dOpex if self.dEBIT is None else self.dEBIT


@dataclass(frozen=True)
class ChannelDef:
    name: str
    family: str
    fn: Callable[[Mapping, Mapping], Delta]
    required: tuple[str, ...]
    optional: tuple[str, ...] = ()
    default_params: Mapping[str, float] = field(default_factory=dict)


CHANNELS: dict[str, ChannelDef] = {}


def channel(name: str, family: str, required: tuple[str, ...], optional: Mapping[str, float] | None = None):
    """Register a channel function under `name` (the `type:` used in policy YAML)."""
    assert family in FAMILIES

    def wrap(fn):
        CHANNELS[name] = ChannelDef(name, family, fn, required, tuple(optional or {}), dict(optional or {}))
        return fn

    return wrap


def run_channel(name: str, b: Mapping, params: Mapping) -> Delta:
    """Run channel `name` with its optional-param defaults filled in."""
    d = CHANNELS[name]
    return d.fn(b, {**d.default_params, **params})


# ============================================================================ 1. TAX


@channel("tax_rate", "tax", required=("d_statutory_rate",), optional={"domestic_income_share": 1.0})
def tax_rate(b, p) -> Delta:
    """Statutory rate change Δτ: t' = t + Δτ × domestic_income_share.

    Only the US-taxed share of income feels a US rate change. The NI effect,
    −PTI' × (t' − t), is applied in aggregation from dTaxRate.
    """
    return Delta(dTaxRate=p["d_statutory_rate"] * p["domestic_income_share"])


@channel("tax_credit", "tax", required=("credit_rate", "base_musd"))
def tax_credit(b, p) -> Delta:
    """Tax credit worth credit_rate × base (capex, R&D or production $M); an after-tax NI item."""
    return Delta(dNI_direct=p["credit_rate"] * p["base_musd"])


@channel("tax_revenue", "tax", required=("rate", "in_scope_share"))
def tax_revenue(b, p) -> Delta:
    """Revenue-based tax (e.g. digital services tax): deductible opex = R × in-scope share × rate."""
    return Delta(dOpex=b["revenue"] * p["in_scope_share"] * p["rate"])


@channel(
    "tax_timing",
    "tax",
    required=("capex_musd", "expensed_share"),
    optional={"statutory_rate": 0.21, "discount_rate": 0.09, "recovery_years": 7},
)
def tax_timing(b, p) -> Delta:
    """Bonus depreciation / full expensing: a timing effect, ≈0 GAAP EPS impact.

    Expensing X now saves τ·X in cash tax this year but forgoes the straight-line
    deductions τ·X/n over the next n years (deferred taxes offset it in GAAP earnings).
    Value = PV of that deferral = τ·X·(1 − AF(n, r)/n), with AF the annuity factor.
    This is computed for one year of capex.
    """
    X = p["capex_musd"] * p["expensed_share"]
    tau, r, n = p["statutory_rate"], p["discount_rate"], int(p["recovery_years"])
    annuity = sum(1 / (1 + r) ** k for k in range(1, n + 1))
    pv = tau * X * (1 - annuity / n)
    return Delta(dValue_pv=pv, notes=[f"timing effect: +${tau * X:,.0f}M cash tax saved this year, ≈0 GAAP EPS"])


# ============================================================================ 2. COST


@channel(
    "cost",
    "cost",
    required=("exposed_cost_share", "shock_pct"),
    optional={"pass_through": 0.0, "elasticity": 0.0, "variable_cost_share": 1.0, "dcost_musd": 0.0},
)
def cost(b, p) -> Delta:
    """Input-cost shock (tariffs, wages, carbon price, compliance).

    exposed = C × exposed_cost_share;  dCost = exposed × shock_pct (+ dcost_musd for $ shocks)
    Firm raises prices by dp = φ·dCost/R; volume falls dQ = −ε·dp.
    dR = R·((1+dp)(1+dQ) − 1);  dC = dCost·(1+dQ) + C·v·dQ  (v = variable cost share)
    """
    R, C = b["revenue"], b["cost_of_revenue"]
    d_cost = C * p["exposed_cost_share"] * p["shock_pct"] + p["dcost_musd"]
    dp = p["pass_through"] * d_cost / R if R else 0.0
    dQ = -p["elasticity"] * dp
    dR = R * ((1 + dp) * (1 + dQ) - 1)
    dC = d_cost * (1 + dQ) + C * p["variable_cost_share"] * dQ
    return Delta(dR=dR, dC=dC)


@channel("domestic_uplift", "cost", required=("domestic_sales_share", "price_uplift"), optional={"flow_through": 1.0})
def domestic_uplift(b, p) -> Delta:
    """Domestic producer behind a tariff wall: prices rise on domestic sales.

    dR = R × domestic_sales_share × price_uplift; a share `flow_through` of it reaches
    EBIT (the rest is absorbed by higher input/scrap costs).
    """
    dR = b["revenue"] * p["domestic_sales_share"] * p["price_uplift"]
    return Delta(dR=dR, dC=dR * (1 - p["flow_through"]))


# ============================================================================ 3. DEMAND


@channel("demand_transfer", "demand", required=("total_transfer_musd", "mpc", "capture_share"), optional={"tilt": 1.0})
def demand_transfer(b, p) -> Delta:
    """Consumer transfer (rebate, stimulus, benefits): spend = total × MPC.

    Each firm captures `capture_share` of new spending (typically its US consumer revenue
    ÷ total PCE, times a `tilt` for categories that gain more or less than average).
    Profit: dEBIT = dR × contribution margin.
    """
    dR = p["total_transfer_musd"] * p["mpc"] * p["capture_share"] * p["tilt"]
    return Delta(dR=dR, dEBIT=dR * b["contribution_margin"])


@channel("demand_price", "demand", required=("dp_consumer", "elasticity", "exposed_revenue_share"))
def demand_price(b, p) -> Delta:
    """Price-induced demand change (sales tax, soda tax, fees): dQ = −ε·dp; dR = R·share·dQ."""
    dR = b["revenue"] * p["exposed_revenue_share"] * (-p["elasticity"] * p["dp_consumer"])
    return Delta(dR=dR, dEBIT=dR * b["contribution_margin"])


@channel("demand_volume", "demand", required=("d_volume", "exposed_revenue_share"))
def demand_volume(b, p) -> Delta:
    """Volume / enrollment shock: dR = R × exposed share × dVolume; dEBIT = dR × cm."""
    dR = b["revenue"] * p["exposed_revenue_share"] * p["d_volume"]
    return Delta(dR=dR, dEBIT=dR * b["contribution_margin"])


# ============================================================================ 4. PRICE


@channel("price", "price", required=("d_price", "exposed_revenue_share"), optional={"offset_share": 0.0})
def price(b, p) -> Delta:
    """Regulated price / reimbursement change: dR = R × exposed share × dPrice.

    dEBIT = dR × (1 − offset_share): firms recoup part of a cut (e.g. MA plans trimming
    benefits) or give back part of a gain.
    """
    dR = b["revenue"] * p["exposed_revenue_share"] * p["d_price"]
    return Delta(dR=dR, dEBIT=dR * (1 - p["offset_share"]))


# ============================================================================ 5. FINANCING


@channel(
    "financing_debt",
    "financing",
    required=("d_rate_bps",),
    optional={"floating_share": 0.3, "maturing_share": 0.0},
)
def financing_debt(b, p) -> Delta:
    """Interest-rate change on non-financial debt: dInt = D × (floating + maturing share) × Δr.

    `maturing_share` reprices the part of fixed-rate debt that rolls over within the year.
    """
    D = b.get("total_debt") or 0.0
    share = min(1.0, p["floating_share"] + p["maturing_share"])
    notes = [] if b.get("total_debt") else ["no debt in baseline; interest effect is zero"]
    return Delta(dInt=D * share * p["d_rate_bps"] / 10_000, notes=notes)


@channel("bank_nii", "financing", required=("d_rate_bps", "nii_sensitivity_per_100bp"))
def bank_nii(b, p) -> Delta:
    """Bank net interest income: dNII = NII × sensitivity per 100 bp × (Δbps / 100).

    NII is part of bank net revenue and, with costs unchanged, drops straight to pretax.
    """
    nii = b.get("net_interest_income") or 0.0
    d = nii * p["nii_sensitivity_per_100bp"] * p["d_rate_bps"] / 100
    return Delta(dR=d, dEBIT=d)


@channel("bank_capital", "financing", required=("cet1_ratio", "d_ratio"), optional={"mm_offset": 0.0})
def bank_capital(b, p) -> Delta:
    """Higher required CET1: more equity against the same earnings.

    ROE' = ROE × ratio / (ratio + Δratio). With a constant P/B-to-ROE relation, equity
    value moves by ROE'/ROE − 1. `mm_offset` (0–1) scales this down for the
    Modigliani–Miller effect: safer banks earn a lower required return.
    No EPS effect (earnings are unchanged; the cost is in returns on equity).
    """
    ratio, dr = p["cet1_ratio"], p["d_ratio"]
    pct = (ratio / (ratio + dr) - 1) * (1 - p["mm_offset"])
    return Delta(dValue_pct=pct, notes=["capital requirement: value effect via ROE, EPS unchanged"])


@channel("reit_nav", "financing", required=("d_10y_bps", "cap_rate"), optional={"cap_rate_beta": 0.5})
def reit_nav(b, p) -> Delta:
    """REIT property values: Δcap = β × Δ10yr; dNAV% ≈ −Δcap / cap_rate."""
    d_cap = p["cap_rate_beta"] * p["d_10y_bps"] / 10_000
    return Delta(dValue_pct=-d_cap / p["cap_rate"])


# ============================================================================ 6. GOVERNMENT


@channel(
    "gov_budget",
    "government",
    required=("gov_revenue_share", "d_budget_pct"),
    optional={"program_relevance": 1.0, "fixed_cost_absorption": 1.0},
)
def gov_budget(b, p) -> Delta:
    """Budget change: dR = R × gov share × program relevance × dBudget%; dEBIT = dR × cm × absorption."""
    dR = b["revenue"] * p["gov_revenue_share"] * p["program_relevance"] * p["d_budget_pct"]
    return Delta(dR=dR, dEBIT=dR * b["contribution_margin"] * p["fixed_cost_absorption"])


@channel(
    "gov_shutdown",
    "government",
    required=("gov_revenue_share", "days"),
    optional={"affected_share": 1.0, "recovery_share": 0.0, "fixed_cost_absorption": 1.0},
)
def gov_shutdown(b, p) -> Delta:
    """Shutdown: dR = −R × gov share × affected share × days/365 × (1 − recovery share)."""
    dR = -b["revenue"] * p["gov_revenue_share"] * p["affected_share"] * p["days"] / 365 * (1 - p["recovery_share"])
    return Delta(dR=dR, dEBIT=dR * b["contribution_margin"] * p["fixed_cost_absorption"])


@channel(
    "gov_cr",
    "government",
    required=("gov_revenue_share", "months_delayed"),
    optional={"new_award_share": 0.1, "fixed_cost_absorption": 1.0},
)
def gov_cr(b, p) -> Delta:
    """Continuing resolution: new-award revenue slips by `months_delayed` (pushed out of the year)."""
    dR = -b["revenue"] * p["gov_revenue_share"] * p["new_award_share"] * p["months_delayed"] / 12
    return Delta(dR=dR, dEBIT=dR * b["contribution_margin"] * p["fixed_cost_absorption"])
