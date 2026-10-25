"""Plain-English explanations built from computed results (no LLM, no network).

Every number in the text comes from the scenario object. Sentences, in order:
1. What the policy does (config `description`, or `narrative.what`, plus the user's inputs)
2. Main driver: the channel with the largest share of the industry's Δ net income, and
   its key assumption
3. Winners and losers: the long and short with their result and dominant exposure
4. Biggest uncertainty: the top tornado driver and how far it swings the result
5. Caveat: persistence, plus one relevant out-of-scope item (and a thin-base-year note
   when a huge % change mostly reflects a small denominator)
A config's `narrative.extra` adds one policy-specific sentence.
"""

from __future__ import annotations

from policyshock.engine.expressions import references
from policyshock.engine.model import CompanyResult
from policyshock.engine.sensitivity import Analysis
from policyshock.engine.valuation import persistence_label
from policyshock.narrative import formatting as f

OUT_OF_SCOPE = {
    "tax": "how companies respond over time, such as shifting where profits are booked",
    "cost": "second-round competitive responses such as rivals' pricing or switching suppliers",
    "demand": "feedback through the wider economy, such as multiplier effects on other spending",
    "price": "how rivals and customers respond after the change",
    "financing": "general-equilibrium effects such as currency moves or the Fed's reaction",
    "government": "timing within the year, such as when delayed awards actually land",
}


def value_text(v: float | None, unit: str) -> str:
    """Format a value in its declared unit for prose."""
    if v is None:
        return "n/m"
    u = unit.lower()
    if u.startswith("usd") and "billion" in u:
        return f"${v:,g}B"
    if u.startswith("usd") and "million" in u:
        return f"${v:,g}M"
    if u in ("millions", "million"):
        return f"{v:,g} million"
    if u == "fraction":
        return f.pct(v, digits=0) if abs(v) >= 0.1 else f.pct(v)
    if u in ("percent", "%"):
        return f"{v:g}%".replace("-", f.MINUS)
    if u in ("percentage points", "pts", "pp"):
        return f"{v:+g} pts"
    if u == "bps":
        return f.bps(v)
    if u in ("usd", "$"):
        return f"${v:,.0f}"
    if u in ("usd_m", "$m"):
        return f.money(v)
    return f"{f.number(v)} {unit}".strip()


# First words that are proper nouns and must keep their capital mid-sentence.
PROPER = {
    "Medicare", "Medicaid", "Fed", "Federal", "Pell", "Title", "Section", "Strait", "China", "Chinese",
    "Nucor", "Grad", "Treasury", "American", "Social", "Congress", "Brent", "Hormuz", "OPEC",
}


def lower_first(txt: str) -> str:
    """'Tariff on…' → 'tariff on…', but keep proper nouns ('Medicare…') and acronyms ('US…')."""
    if not txt:
        return txt
    first = txt.split()[0].strip("(,")
    if txt[1:2].isupper() or first in PROPER:
        return txt
    return txt[:1].lower() + txt[1:]


def metric_text(c: CompanyResult) -> str:
    """The metric companies are ranked on: implied Δprice when available, else ΔEPS."""
    if c.dP_pct is not None and c.dEPS_pct is not None and abs(c.dP_pct - c.dEPS_pct) < 5e-4:
        return f"EPS and implied price {f.pct(c.dEPS_pct, signed=True)}"
    if c.dP_pct is not None:
        return f"implied share price {f.pct(c.dP_pct, signed=True)}, EPS {f.pct(c.dEPS_pct, signed=True)}"
    if c.dEPS_pct is not None:
        return f"EPS {f.pct(c.dEPS_pct, signed=True)}"
    return f"net income {f.money(c.dNI, signed=True)}"


def company_reason(c: CompanyResult, reg, skip_label: str | None = None) -> str:
    """Deterministic one-line reason: dominant channel plus that channel's exposure values.

    With `skip_label`, a channel already named in the text is replaced by its exposures only.
    """
    dom = c.dominant
    if dom is None:
        return "no direct exposure"
    bits = []
    for key in dom.exposure_refs:
        d = reg.exposure_defs[key]
        v = reg.exposures[c.ticker][key].value
        bits.append(f"{lower_first(d.label)} {value_text(v, d.unit)}")
    if skip_label and dom.label == skip_label and bits:
        return "; ".join(bits)
    return lower_first(dom.label) + (f" ({'; '.join(bits)})" if bits else "")


def _main_channel(an: Analysis) -> tuple[str, str, float]:
    """(label, family, share of total |ΔNI|) of the channel moving industry ΔNI the most."""
    by_label: dict[str, list] = {}
    for c in an.base.companies:
        for o in c.outcomes:
            by_label.setdefault(o.label, [o.family, 0.0])[1] += o.dNI
    if not by_label:
        return "", "", 0.0
    total = sum(abs(v) for _, v in by_label.values()) or 1.0
    label, (family, v) = max(by_label.items(), key=lambda kv: abs(kv[1][1]))
    return label, family, abs(v) / total


def _key_assumption(an: Analysis, label: str):
    """The first assumption the main channel depends on (directly or via derived values)."""
    pol = an.base.policy
    spec = next((c for c in pol.channels if (c.label or c.type) == label), None)
    if spec is None:
        return None
    seen: list[str] = []

    def walk(expr):
        for ns, key in references(expr):
            if ns == "assumption" and key not in seen:
                seen.append(key)
            elif ns == "derived" and key in pol.derived:
                walk(pol.derived[key])

    for v in spec.params.values():
        walk(v)
    for key in seen:
        a = pol.assumption(key)
        if a.uncertain:
            return a, an.base.assumptions.get(key, a.base)
    return None


def _inputs_text(pol, inputs: dict) -> str:
    parts = [f"{lower_first(u.label)} of {value_text(inputs.get(u.key), u.unit)}" for u in pol.user_inputs if inputs.get(u.key) is not None]
    return ", ".join(parts)


def _thin_base(an: Analysis) -> str | None:
    """Flag a huge % change that mostly reflects a thin base-year pretax margin."""
    worst = None
    for c in an.base.companies:
        b = c.baseline
        if c.dEPS_pct is None or not b.get("revenue"):
            continue
        margin = b["pretax_income"] / b["revenue"]
        if abs(c.dEPS_pct) >= 0.25 and 0 < margin < 0.03:
            if worst is None or abs(c.dEPS_pct) > abs(worst[0].dEPS_pct):
                worst = (c, margin)
    if worst:
        c, m = worst
        return f"{c.ticker}'s large percentage partly reflects a thin FY{c.baseline['fiscal_year']} pretax margin ({f.pct(m)})."
    return None


MAX_WORDS = 200


def explain(an: Analysis, reg) -> str:
    """Industry-mode explanation, 120–200 words where possible.

    If a long policy description pushes the text past 200 words, only its first sentence is used.
    """
    # Trim in stages: (1) first sentence of the description, (2) also drop the summary
    # sentence, which the five-part order doesn't require.
    for level in (0, 1, 2, 3):
        text = _explain(an, reg, level)
        if len(text.split()) <= MAX_WORDS:
            return text
    return text


def _first_sentence(txt: str) -> str:
    head, sep, _ = txt.partition(". ")
    return head + "." if sep else txt


def _explain(an: Analysis, reg, level: int) -> str:
    pol = an.base.policy
    t = an.base.totals()
    s: list[str] = []

    # 1. What the policy does
    what = (pol.narrative.what if pol.narrative and pol.narrative.what else pol.description).strip()
    try:
        what = what.format(**an.base.inputs)
    except (KeyError, IndexError, ValueError):
        pass
    if level >= 1:
        what = _first_sentence(what)
    inputs = _inputs_text(pol, an.base.inputs)
    s.append(what if what.endswith(".") else what + ".")
    if inputs:
        s.append(f"This scenario uses a {inputs}.")
    if level < 2:
        s.append(
        f"Across the {len(an.base.companies)} companies, revenue changes by {f.money(t['d_revenue'], signed=True)} "
        f"and earnings per share by {f.pct(t['d_eps_pct'], signed=True)} "
        f"(range {f.pct(an.industry_low.totals()['d_eps_pct'], signed=True)} to {f.pct(an.industry_high.totals()['d_eps_pct'], signed=True)})."
    )

    # 2. Main driver
    label, family, share = _main_channel(an)
    if label:
        if share > 0.97:
            line = f"All of the effect runs through {lower_first(label)}"
        else:
            line = f"Most of the effect ({f.pct(share, digits=0)} of the net-income change) runs through {lower_first(label)}"
        ka = _key_assumption(an, label)
        if ka and level < 3:
            a, v = ka
            line += f"; we assume a {lower_first(a.label)} of {value_text(v, a.unit)}"
        s.append(line + ".")

    # 3. Winners and losers
    if an.long and an.short:
        def why(c):
            r = company_reason(c, reg, skip_label=label)
            return f"with {r}" if (label and c.dominant and c.dominant.label == label) else f"mainly through {r}"

        s.append(
            f"The most helped company is {an.long.name} ({metric_text(an.long)}), {why(an.long)}; "
            f"the most hurt is {an.short.name} ({metric_text(an.short)}), {why(an.short)}."
        )
        if an.low_conviction:
            s.append("Their ranges overlap, so the long/short call is low conviction.")
    elif an.long or an.short:
        c = an.long or an.short
        s.append(f"Only {c.name} is materially affected ({metric_text(c)}), mainly through {company_reason(c, reg, skip_label=None)}.")

    # 4. Biggest uncertainty
    if an.tornado:
        b = an.tornado[0]
        name = "industry EPS" if an.metric == "d_eps_pct" else "industry value"
        rng = f" from {value_text(b.driver.low, b.driver.unit)} to {value_text(b.driver.high, b.driver.unit)}" if b.driver.low is not None else (" across exposure bounds" if level >= 3 else " across each company's low and high values")
        s.append(
            f"The biggest uncertainty is the {lower_first(b.driver.label)}: moving it{rng} shifts {name} "
            f"between {f.pct(min(b.low_value, b.high_value), signed=True)} and {f.pct(max(b.low_value, b.high_value), signed=True)}."
        )

    # policy-specific sentence
    if pol.narrative and pol.narrative.extra:
        s.append(pol.narrative.extra.strip())

    # 5. Caveat
    caveat = f"The change is treated as {persistence_label(pol.persistence)}"
    if family in OUT_OF_SCOPE:
        caveat += f", and the model leaves out {OUT_OF_SCOPE[family]}"
    s.append(caveat + ".")
    thin = _thin_base(an)
    if thin:
        s.append(thin)
    return " ".join(s)


def explain_market(an, reg, names: dict[str, str]) -> str:
    """Full Market explanation: shock → transmission paths → sector winners/losers → uncertainty → caveat.

    Trimmed in stages (shorter description, then no shock-specific note) to stay within MAX_WORDS.
    """
    for level in (0, 1, 2):
        text = _explain_market(an, names, level)
        if len(text.split()) <= MAX_WORDS:
            return text
    return text


def _explain_market(an, names: dict[str, str], level: int) -> str:
    from policyshock.macro.aggregate import industry_metric

    shock = an.base.shock
    t = an.base.totals()
    desc = shock.description.strip()
    s: list[str] = [desc if level == 0 else _first_sentence(desc)]
    inputs = _inputs_text(shock, an.base.inputs)
    if inputs:
        s.append(f"This scenario uses a {inputs}.")
    lo, hi = an.market_low.totals()[an.metric], an.market_high.totals()[an.metric]
    s.append(
        f"Across the {sum(len(i.companies) for i in an.base.industries.values())}-company sample (cap-weighted), earnings per share change by {f.pct(t['cw_d_eps_pct'], signed=True)} "
        f"and implied market value by {f.money(t['d_mcap'], signed=True)} ({f.pct(t['d_mcap_pct'], signed=True)}); "
        f"the range on the headline measure is {f.pct(lo, signed=True)} to {f.pct(hi, signed=True)}."
    )
    movers = sorted(an.base.industries.items(), key=lambda kv: abs(sum(c.dNI for c in kv[1].companies)), reverse=True)
    paths = []
    for slug, r in movers[:2]:
        eff = shock.industry_effects[slug]
        if eff.effect == "none" or abs(sum(c.dNI for c in r.companies)) < 1e-6:
            continue
        reason = eff.reason or "its direct exposure"
        paths.append(f"{names[slug]}, where {lower_first(reason).rstrip('.')}")
    if paths:
        s.append("The main transmission paths run through " + "; and ".join(paths) + ".")
    if an.long_industry and an.short_industry:
        s.append(
            f"The most helped sector is {names[an.long_industry]} ({f.pct(industry_metric(an.base.industries[an.long_industry]), signed=True)} value) "
            f"and the most hurt is {names[an.short_industry]} ({f.pct(industry_metric(an.base.industries[an.short_industry]), signed=True)}), "
            f"which is the sector pair trade."
        )
    if an.tornado:
        b = an.tornado[0]
        s.append(
            f"The biggest uncertainty is the {lower_first(b.driver.label)}, which moves the headline between "
            f"{f.pct(min(b.low_value, b.high_value), signed=True)} and {f.pct(max(b.low_value, b.high_value), signed=True)}."
        )
    if shock.narrative and shock.narrative.extra and level < 2:
        s.append(shock.narrative.extra.strip())
    s.append(
        f"This is a first-order, partial-equilibrium sum of direct effects, treated as {persistence_label(shock.persistence)}; "
        "knock-on effects (the Fed's reaction, spending and supply-chain feedback) are left out unless switched on as labelled components."
    )
    return " ".join(s)
