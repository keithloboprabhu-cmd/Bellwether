"""Build per-company annual baselines from SEC XBRL company facts.

For each fiscal year (identified by its period-end date) we pick every line item by
walking a tag fallback chain, recording which tag was used and any data-quality flags.

Parsing rules (see METHODOLOGY.md, "Data"):
- Only 10-K / 10-K/A facts. Duration items must span 350–380 days (a full fiscal
  year), which drops the quarterly facts that some 10-Ks also carry.
- Restatements: when several filings report the same period end, the most recently
  filed value wins. The *first* 10-K reporting that period is kept as the source link.
- The fallback chain is applied per fiscal year, because companies change tags over
  time (e.g. `SalesRevenueNet` → `RevenueFromContractWithCustomerExcludingAssessedTax`).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date

# Tag chains, tried in order. All are us-gaap unless prefixed "dei:".
REVENUE_TAGS = [
    "Revenues",
    "RevenueFromContractWithCustomerExcludingAssessedTax",
    "SalesRevenueNet",
    "RevenuesNetOfInterestExpense",
    # utilities (NEE) tag regulated + unregulated operating revenue separately
    "RegulatedAndUnregulatedOperatingRevenue",
    "RevenueFromContractWithCustomerIncludingAssessedTax",
    # pre-ASC 606 service/goods revenue tags (e.g. BAH before FY2018)
    "SalesRevenueServicesNet",
    "SalesRevenueGoodsNet",
]
# Banks: total net revenue first. Contract-revenue tags cover only fee income (AXP tags $41B
# of discount/fee revenue that way vs $72B total revenues net of interest expense).
BANK_REVENUE_TAGS = ["RevenuesNetOfInterestExpense", "Revenues"]

COST_TAGS = [
    "CostOfRevenue",
    "CostOfGoodsAndServicesSold",
    "CostOfGoodsSold",
    # REIT property operating costs
    "CostOfRealEstateRevenue",
    "DirectCostsOfLeasedAndRentedPropertyOrEquipment",
]
OPINC_TAGS = ["OperatingIncomeLoss"]
INTEREST_TAGS = ["InterestExpense", "InterestExpenseNonoperating", "InterestExpenseDebt"]
PRETAX_TAGS = [
    "IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest",
    "IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments",
]
TAX_TAGS = ["IncomeTaxExpenseBenefit"]
# Income tax note: pretax income split by jurisdiction (domestic share drives US tax-rate effects).
PRETAX_DOMESTIC_TAGS = ["IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic"]
PRETAX_FOREIGN_TAGS = ["IncomeLossFromContinuingOperationsBeforeIncomeTaxesForeign"]
NCI_INCOME_TAGS = ["NetIncomeLossAttributableToNoncontrollingInterest"]
NET_INCOME_TAGS = ["NetIncomeLoss", "NetIncomeLossAvailableToCommonStockholdersBasic", "ProfitLoss"]
EPS_TAGS = ["EarningsPerShareDiluted", "EarningsPerShareBasicAndDiluted"]
DILUTED_SHARES_TAGS = ["WeightedAverageNumberOfDilutedSharesOutstanding"]
GROSS_PROFIT_TAGS = ["GrossProfit"]
COSTS_AND_EXPENSES_TAGS = ["CostsAndExpenses"]
# Managed-care insurers tag medical costs separately from product costs (pharmacy etc.).
CLAIMS_TAGS = [
    "PolicyholderBenefitsAndClaimsIncurredNet",
    "PolicyholderBenefitsAndClaimsIncurredHealthCare",
    "BenefitsLossesAndExpenses",
]
SGA_TAGS = ["SellingGeneralAndAdministrativeExpense", "GeneralAndAdministrativeExpense"]
RND_TAGS = ["ResearchAndDevelopmentExpense", "ResearchAndDevelopmentExpenseExcludingAcquiredInProcessCost"]
DA_TAGS = ["DepreciationDepletionAndAmortization", "DepreciationAndAmortization", "DepreciationAmortizationAndAccretionNet"]
NII_TAGS = ["InterestIncomeExpenseNet", "InterestIncomeExpenseAfterProvisionForLoanLoss"]
ASSETS_TAGS = ["Assets"]
# Debt is an instant (balance-sheet) item. LongTermDebt usually includes the current portion.
DEBT_TAGS = ["LongTermDebt", "LongTermDebtAndCapitalLeaseObligations", "DebtLongtermAndShorttermCombinedAmount"]
DEBT_NONCURRENT_TAGS = ["LongTermDebtNoncurrent", "LongTermDebtAndCapitalLeaseObligationsNoncurrent"]
DEBT_CURRENT_TAGS = ["LongTermDebtCurrent", "LongTermDebtAndCapitalLeaseObligationsCurrent"]

ANNUAL_FORMS = {"10-K", "10-K/A", "10-KT"}
DEFAULT_TAX_RATE = 0.21
TAX_RATE_CLAMP = (0.0, 0.40)  # 40% (not 35%) so pre-TCJA years aren't distorted


@dataclass
class Fact:
    value: float
    tag: str
    end: str
    filed: str
    accn: str
    cik: int | None = None


@dataclass
class FiscalYear:
    """One fiscal year of baseline financials, $ in millions and shares in millions."""

    period_end: str
    fiscal_year: int
    items: dict[str, float | None] = field(default_factory=dict)
    tags: dict[str, str] = field(default_factory=dict)
    flags: list[str] = field(default_factory=list)
    source_accn: str | None = None
    source_filed: str | None = None
    source_cik: int | None = None

    def to_dict(self) -> dict:
        return {
            "period_end": self.period_end,
            "fiscal_year": self.fiscal_year,
            "items": self.items,
            "tags": self.tags,
            "flags": self.flags,
            "source_accn": self.source_accn,
            "source_filed": self.source_filed,
            "source_cik": self.source_cik,
        }


def _days(start: str, end: str) -> int:
    return (date.fromisoformat(end) - date.fromisoformat(start)).days


def _facts_for(facts: dict, tag: str, unit: str) -> list[dict]:
    ns, _, name = tag.rpartition(":")
    ns = ns or "us-gaap"
    return facts.get("facts", {}).get(ns, {}).get(name, {}).get("units", {}).get(unit, [])


def annual_series(facts: dict, tag: str, unit: str = "USD", instant: bool = False) -> dict[str, Fact]:
    """Return {period_end: Fact} for one tag, keeping full-year 10-K values only.

    Duration facts must cover 350–380 days; instant facts are taken as-is. For each
    period end the latest-filed value wins (captures restatements).
    """
    out: dict[str, Fact] = {}
    for f in _facts_for(facts, tag, unit):
        if f.get("form") not in ANNUAL_FORMS:
            continue
        if instant:
            if "start" in f:
                continue
        else:
            if "start" not in f or not 350 <= _days(f["start"], f["end"]) <= 380:
                continue
        prev = out.get(f["end"])
        if prev is None or f["filed"] > prev.filed:
            out[f["end"]] = Fact(float(f["val"]), tag, f["end"], f["filed"], f["accn"])
    return out


def first_filing_for_period(facts: dict, tags: list[str], unit: str = "USD") -> dict[str, tuple[str, str, int | None]]:
    """Map period_end → (accession, filed, cik) of the earliest 10-K reporting that period.

    That earliest filing is the 10-K *for* that fiscal year (later ones are comparatives).
    """
    out: dict[str, tuple[str, str, int | None]] = {}
    for tag in tags:
        for f in _facts_for(facts, tag, unit):
            if f.get("form") not in ANNUAL_FORMS or "start" not in f:
                continue
            if not 350 <= _days(f["start"], f["end"]) <= 380:
                continue
            prev = out.get(f["end"])
            if prev is None or f["filed"] < prev[1]:
                out[f["end"]] = (f["accn"], f["filed"], f.get("_cik"))
    return out


def _chain(facts: dict, tags: list[str], unit: str = "USD", instant: bool = False) -> dict[str, Fact]:
    """Apply a fallback chain per period end: the first tag with a value wins."""
    merged: dict[str, Fact] = {}
    for tag in tags:
        for end, fact in annual_series(facts, tag, unit, instant).items():
            merged.setdefault(end, fact)
    return merged


def _near(series: dict[str, Fact], end: str, tolerance_days: int = 7) -> Fact | None:
    """Look up an instant fact at (or within a few days of) a fiscal period end."""
    if end in series:
        return series[end]
    for e, fact in series.items():
        if abs(_days(e, end)) <= tolerance_days:
            return fact
    return None


def fiscal_year_label(period_end: str) -> int:
    """Fiscal year label = calendar year of the period end (e.g. WMT FY ending Jan-2025 → 2025).

    Exception: years ending in the first week of January (52/53-week calendars such as
    FDX/DAL don't, but some retailers do) belong to the prior year.
    """
    d = date.fromisoformat(period_end)
    return d.year - 1 if (d.month == 1 and d.day <= 7) else d.year


def build_baseline(
    facts: dict, kind: str = "standard", min_year: int = 2008, cost_basis: str = "reported"
) -> list[FiscalYear]:
    """Parse company facts into a list of FiscalYear records, newest first.

    `kind` is "standard", "bank", "reit" or "managed_care" (config/industries.yaml).
    `cost_basis="total_costs_less_overhead"` sets cost of revenue = CostsAndExpenses − SG&A/G&A
    − R&D − D&A, for companies whose tagged cost of revenue omits large variable costs
    (Booz Allen reports subcontractor "billable expenses" on a separate, custom-tagged line). Values are
    converted to $ millions / millions of shares. EPS stays in $ per share.
    """
    M = 1e6
    rev = _chain(facts, BANK_REVENUE_TAGS if kind == "bank" else REVENUE_TAGS)
    cost = _chain(facts, COST_TAGS)
    opinc = _chain(facts, OPINC_TAGS)
    interest = _chain(facts, INTEREST_TAGS)
    pretax = _chain(facts, PRETAX_TAGS)
    tax = _chain(facts, TAX_TAGS)
    pt_dom = _chain(facts, PRETAX_DOMESTIC_TAGS)
    pt_for = _chain(facts, PRETAX_FOREIGN_TAGS)
    ni = _chain(facts, NET_INCOME_TAGS)
    nci = _chain(facts, NCI_INCOME_TAGS)
    eps = _chain(facts, EPS_TAGS, unit="USD/shares")
    dil = _chain(facts, DILUTED_SHARES_TAGS, unit="shares")
    gp = _chain(facts, GROSS_PROFIT_TAGS)
    cae = _chain(facts, COSTS_AND_EXPENSES_TAGS)
    claims = _chain(facts, CLAIMS_TAGS)
    sga = _chain(facts, SGA_TAGS)
    rnd = _chain(facts, RND_TAGS)
    da = _chain(facts, DA_TAGS)
    nii = _chain(facts, NII_TAGS)
    assets = _chain(facts, ASSETS_TAGS, instant=True)
    debt = _chain(facts, DEBT_TAGS, instant=True)
    debt_nc = _chain(facts, DEBT_NONCURRENT_TAGS, instant=True)
    debt_c = _chain(facts, DEBT_CURRENT_TAGS, instant=True)
    sources = first_filing_for_period(facts, REVENUE_TAGS + NET_INCOME_TAGS)

    years: list[FiscalYear] = []
    # A fiscal year exists if we have net income for a full-year period. Companies on 52/53-week
    # calendars sometimes tag the same year with two period ends a day or two apart (DE: Oct 31
    # vs Nov 1); keep the one from the most recent filing and drop the near-duplicate.
    ends: list[str] = []
    for end in sorted(ni, key=lambda e: ni[e].filed, reverse=True):
        if all(abs(_days(end, kept)) > 10 for kept in ends):
            ends.append(end)
    for end in sorted(ends, reverse=True):
        fy = FiscalYear(period_end=end, fiscal_year=fiscal_year_label(end))
        if fy.fiscal_year < min_year:
            continue
        if end in sources:
            fy.source_accn, fy.source_filed, fy.source_cik = sources[end]

        def put(key: str, fact: Fact | None, scale: float = M) -> float | None:
            if fact is None:
                fy.items[key] = None
                return None
            fy.items[key] = fact.value / scale
            fy.tags[key] = fact.tag
            return fy.items[key]

        R = put("revenue", rev.get(end))
        put("net_income", ni.get(end))
        put("nci_income", nci.get(end))
        put("eps_diluted", eps.get(end), scale=1)
        S = put("diluted_shares", dil.get(end))
        put("interest_expense", interest.get(end))
        put("da", da.get(end))
        put("total_assets", _near(assets, end))
        # raw cost components, kept so cross-year comparisons can use one consistent cost definition
        put("costs_and_expenses", cae.get(end))
        put("sga", sga.get(end))
        put("rnd", rnd.get(end))
        put("gross_profit", gp.get(end))
        put("pretax_domestic", pt_dom.get(end))
        put("pretax_foreign", pt_for.get(end))
        PTI = put("pretax_income", pretax.get(end))
        T = put("income_tax", tax.get(end))
        EBIT = put("operating_income", opinc.get(end))
        C = put("cost_of_revenue", cost.get(end))

        # --- total debt: the largest of the complete-debt measures available. Partial tags
        # (e.g. MAR tags a $23M item as LongTermDebt) can only understate, so max is safest.
        candidates: list[tuple[float, str]] = []
        for tag_fact in (_near(debt, end),):
            if tag_fact is not None:
                candidates.append((tag_fact.value, tag_fact.tag))
        nc, cur = _near(debt_nc, end), _near(debt_c, end)
        if nc is not None:
            candidates.append((nc.value + (cur.value if cur else 0.0), nc.tag + (f" + {cur.tag}" if cur else "")))
        lt_cl = annual_series(facts, "LongTermDebtAndCapitalLeaseObligations", instant=True)
        lt_cl_cur = annual_series(facts, "LongTermDebtAndCapitalLeaseObligationsCurrent", instant=True)
        a, b = _near(lt_cl, end), _near(lt_cl_cur, end)
        if a is not None:
            candidates.append((a.value + (b.value if b else 0.0), a.tag + (f" + {b.tag}" if b else "")))
        if candidates:
            val, tag = max(candidates)
            fy.items["total_debt"] = val / M
            fy.tags["total_debt"] = tag
        else:
            fy.items["total_debt"] = None
            if kind != "bank":  # banks use NII sensitivity, not debt × Δr
                fy.flags.append("total debt not found; assumed 0 for financing shocks")

        # --- bank template: NII, and pretax income stands in for EBIT
        if kind == "bank":
            put("net_interest_income", nii.get(end))
            if EBIT is None and PTI is not None:
                fy.items["operating_income"] = PTI
                fy.tags["operating_income"] = "= pretax income (bank template)"
            fy.items["cost_of_revenue"] = None
            fy.tags.pop("cost_of_revenue", None)
            if fy.items.get("net_interest_income") is None:
                fy.flags.append("net interest income not found")
        else:
            # --- operating income fallback: pretax + interest (needed by the cost fallbacks)
            if EBIT is None and PTI is not None:
                EBIT = PTI + (fy.items.get("interest_expense") or 0.0)
                fy.items["operating_income"] = EBIT
                fy.tags["operating_income"] = "= PretaxIncome + InterestExpense"
                fy.flags.append("operating income derived from pretax income + interest")
            # --- managed care: cost of revenue = product costs + medical claims
            cl = claims.get(end)
            if kind == "managed_care" and cl is not None:
                fy.items["cost_of_revenue"] = (C or 0.0) + cl.value / M
                fy.tags["cost_of_revenue"] = (f"{fy.tags['cost_of_revenue']} + " if C is not None else "") + cl.tag
                C = fy.items["cost_of_revenue"]
            # --- opt-in: variable costs = total costs less overhead (see docstring)
            ce_ = cae.get(end)
            if cost_basis == "total_costs_less_overhead" and ce_ is not None and R is not None:
                s_, r_ = sga.get(end), rnd.get(end)
                overhead = sum(x.value / M for x in (s_, r_) if x) + (fy.items.get("da") or 0.0)
                fy.items["cost_of_revenue"] = ce_.value / M - overhead
                fy.tags["cost_of_revenue"] = "= CostsAndExpenses − SG&A/G&A − R&D − D&A (config cost_basis)"
                C = fy.items["cost_of_revenue"]
            # --- cost of revenue fallbacks
            if C is None and R is not None:
                g, ce = gp.get(end), cae.get(end)
                s_, r_ = sga.get(end), rnd.get(end)
                opex = (s_.value / M if s_ else 0.0) + (r_.value / M if r_ else 0.0)
                if g is not None:
                    fy.items["cost_of_revenue"] = R - g.value / M
                    fy.tags["cost_of_revenue"] = "= Revenue − GrossProfit"
                elif ce is not None:
                    fy.items["cost_of_revenue"] = ce.value / M - opex
                    fy.tags["cost_of_revenue"] = "= CostsAndExpenses − SG&A − R&D"
                    fy.flags.append("cost of revenue derived (CostsAndExpenses − SG&A − R&D)")
                elif EBIT is not None and opex > 0:
                    fy.items["cost_of_revenue"] = R - EBIT - opex
                    fy.tags["cost_of_revenue"] = "= Revenue − OperatingIncome − SG&A − R&D"
                    fy.flags.append("cost of revenue derived (Revenue − EBIT − SG&A − R&D)")
                else:
                    fy.flags.append("cost of revenue not found; engine uses industry default margin")

        # --- pretax fallback: NI + tax
        if PTI is None and T is not None and fy.items.get("net_income") is not None:
            PTI = fy.items["net_income"] + T
            fy.items["pretax_income"] = PTI
            fy.tags["pretax_income"] = "= NetIncome + IncomeTax"
            fy.flags.append("pretax income derived (NI + tax)")

        # --- effective tax rate, clamped; default 21% if PTI ≤ 0 or tax missing
        if PTI is not None and PTI > 0 and T is not None:
            raw = T / PTI
            lo, hi = TAX_RATE_CLAMP
            fy.items["effective_tax_rate_raw"] = raw
            fy.items["effective_tax_rate"] = min(max(raw, lo), hi)
            if not lo <= raw <= hi:
                fy.flags.append(f"effective tax rate {raw:.1%} clamped to [{lo:.0%}, {hi:.0%}]")
        else:
            fy.items["effective_tax_rate_raw"] = None
            fy.items["effective_tax_rate"] = DEFAULT_TAX_RATE
            fy.flags.append("pretax income ≤ 0 or tax missing; tax rate set to 21%")

        # --- EPS / shares consistency
        if S is None and fy.items.get("eps_diluted") and fy.items.get("net_income"):
            fy.items["diluted_shares"] = fy.items["net_income"] / fy.items["eps_diluted"]
            fy.tags["diluted_shares"] = "= NetIncome / EPS diluted"
            fy.flags.append("diluted shares derived from NI / EPS")

        if fy.items.get("eps_diluted") is None and fy.items.get("net_income") is not None and fy.items.get("diluted_shares"):
            fy.items["eps_diluted"] = fy.items["net_income"] / fy.items["diluted_shares"]
            fy.tags["eps_diluted"] = "= NetIncome / diluted shares"
            fy.flags.append("diluted EPS derived from NI / diluted shares")

        if R is None:
            fy.flags.append("revenue not found")
        years.append(fy)
    return years


def shares_outstanding(facts: dict) -> dict | None:
    """Latest cover-page shares outstanding (dei:EntityCommonStockSharesOutstanding), millions.

    Multi-class issuers (GOOGL, META) report one fact per class in the same filing;
    those are summed. Returns {"value", "date", "accn", "classes"} or None.
    """
    rows = _facts_for(facts, "dei:EntityCommonStockSharesOutstanding", "shares")
    if not rows:
        return None
    latest_filed = max(r["filed"] for r in rows)
    same = [r for r in rows if r["filed"] == latest_filed]
    latest_end = max(r["end"] for r in same)
    same = [r for r in same if r["end"] == latest_end]
    return {
        "value": sum(float(r["val"]) for r in same) / 1e6,
        "date": latest_end,
        "accn": same[0]["accn"],
        "classes": len(same),
    }
