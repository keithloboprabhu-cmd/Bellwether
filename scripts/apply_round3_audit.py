"""Round-3 credibility audit: replace material peer priors and close coverage gaps.

Three kinds of change, all data (no engine code):

1. CORRECTIONS replace "Explicit modeling prior" exposures that were copied from an
   unlike peer (e.g. QCOM inheriting NVIDIA's China share, Kroger a general-merchandise
   import share) and fill sentinels of newly admitted issuers. They are merged into
   config/company_exposure_overrides.yaml and applied in place by
   scripts/apply_exposure_audit.py, so regeneration cannot undo them.
2. NEW_KEYS define exposures for the channels/policies added in this round and give a
   value for every company in the industry (scope zeros carry a reason).
3. COVERAGE moves each affected pair into the right status group in
   config/policy_company_coverage.yaml and keeps config/policy_review.yaml in sync.

Primary values cite the committed 10-K XBRL facts in reports/evidence/filings.json;
everything else is `source: estimate` with a company-specific rationale and range.
Idempotent. Run: PYTHONPATH=src .venv/bin/python scripts/apply_round3_audit.py
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from policyshock.config import CONFIG_DIR, load_universe  # noqa: E402

FILINGS = {  # committed 10-K documents (reports/evidence/filings.json source_url)
    "LRCX": "https://www.sec.gov/Archives/edgar/data/707549/000070754926000037/lrcx-20260628.htm",
    "ISRG": "https://www.sec.gov/Archives/edgar/data/1035267/000103526726000011/isrg-20251231.htm",
    "MDT": "https://www.sec.gov/Archives/edgar/data/1613103/000161310326000027/mdt-20260424.htm",
    "MO": "https://www.sec.gov/Archives/edgar/data/764180/000076418026000017/mo-20251231.htm",
    "ALL": "https://www.sec.gov/Archives/edgar/data/899051/000089905126000014/all-20251231.htm",
    "MET": "https://www.sec.gov/Archives/edgar/data/1099219/000109921926000010/met-20251231.htm",
    "PGR": "https://www.sec.gov/Archives/edgar/data/80661/000008066126000012/pgr-20251231.htm",
    "TRV": "https://www.sec.gov/Archives/edgar/data/86312/000008631226000010/trv-20251231.htm",
    "V": "https://www.sec.gov/Archives/edgar/data/1403161/000140316125000058/v-20250930.htm",
}


def est(v, lo, hi, why, url=None):
    """An explained company-specific estimate."""
    return dict(value=float(v), low=float(lo), high=float(hi), source="estimate", source_url=url,
                rationale="Company-specific estimate (audit round 3): " + why, applicable=True)


def primary(v, lo, hi, what, ticker):
    """A value computed from committed 10-K XBRL facts."""
    return dict(value=round(float(v), 4), low=round(float(lo), 4), high=round(float(hi), 4),
                source="SEC 10-K XBRL (reports/evidence/filings.json)", source_url=FILINGS[ticker],
                rationale=what, applicable=True)


def scope0(why):
    """A reviewed model boundary: the channel does not reach this business."""
    return dict(value=0.0, low=0.0, high=0.0, source="estimate", source_url=None, applicable=True,
                rationale="Company-specific scope estimate: " + why + " This is a model boundary, not a reported zero measurement.")


def gap(why):
    """Inactive sentinel: missing coverage, never a measured zero."""
    return dict(value=0.0, low=0.0, high=0.0, applicable=False, source="estimate", source_url=None,
                rationale="UNQUANTIFIED sentinel, not a measured zero. " + why)


# ------------------------------------------------------------------ 1. corrections of existing keys
CORRECTIONS = {
    # --- consumer: import shares copied from WMT/COST/TGT onto unlike businesses
    "KR": {"us_import_share_of_cogs": est(0.10, 0.05, 0.16, "Kroger's cost of sales is dominated by fresh food, grocery and pharmacy; most US food spending is domestically produced (imports are roughly a sixth of US food by value) and general merchandise is a small share of sales. Replaces a WMT/COST/TGT general-merchandise prior.")},
    "DG": {"us_import_share_of_cogs": est(0.17, 0.10, 0.25, "Consumables (mostly US-made branded and private-label staples) are about four-fifths of Dollar General sales; seasonal, home and apparel lines are largely imported. Replaces a WMT/COST/TGT prior.")},
    "SBUX": {"us_import_share_of_cogs": est(0.07, 0.04, 0.12, "Starbucks' modeled cost of revenue ($31.9B) includes store labor and occupancy, so the imported share is small: green coffee for US stores plus some merchandise and equipment. Replaces a 0.27 retailer prior that implied about $8.6B of imports.")},
    "PEP": {"us_consumer_revenue_share": est(0.57, 0.52, 0.62, "PepsiCo's North America beverage and food divisions are a little under three-fifths of net revenue (FY2025 segment reporting), slightly less for the US alone. Replaces a 0.70 WMT/COST/NKE prior.")},
    "KO": {"us_consumer_revenue_share": est(0.35, 0.30, 0.40, "Coca-Cola's North America operating segment is roughly a third of net operating revenue; the rest is international bottling and concentrate sales. Replaces a 0.70 retailer prior.")},
    "PG": {"us_consumer_revenue_share": est(0.47, 0.43, 0.50, "Procter & Gamble reports US net sales at a little under half of the total. Replaces a 0.70 retailer prior.")},
    # --- consumer additions (were sentinels)
    "MO": {
        "us_consumer_revenue_share": est(0.95, 0.90, 1.0, "Altria sells only in the US; revenue reaches consumers through wholesalers and retailers. Low end allows for excise collected in revenue.", FILINGS["MO"]),
        "snap_grocery_spend_share": scope0("SNAP benefits cannot buy tobacco (7 U.S.C. 2012(k) eligible foods)."),
        "us_sweetened_beverage_revenue_share": scope0("Altria sells no beverages."),
    },
    "PM": {
        "us_consumer_revenue_share": est(0.08, 0.06, 0.11, "PMI's US business (Swedish Match ZYN, cigars and IQOS) is a high-single-digit share of net revenue; the rest is international."),
        "snap_grocery_spend_share": scope0("SNAP benefits cannot buy tobacco."),
        "us_sweetened_beverage_revenue_share": scope0("PMI sells no beverages."),
    },
    "MDLZ": {
        "us_consumer_revenue_share": est(0.25, 0.22, 0.28, "Mondelez's North America segment (mostly the US) is about a quarter of net revenue."),
        "snap_grocery_spend_share": scope0("Manufacturer: SNAP redemptions are captured by grocery retailers, consistent with PEP/KO/PG."),
        "us_sweetened_beverage_revenue_share": scope0("Mondelez sells no US beverages."),
    },
    "TSN": {
        "us_consumer_revenue_share": est(0.85, 0.75, 0.92, "Tyson's sales are overwhelmingly US retail and foodservice demand; international is a small share. Foodservice sales still reach US consumers through restaurants."),
        "snap_grocery_spend_share": scope0("Manufacturer: SNAP redemptions are captured by grocery retailers."),
        "us_sweetened_beverage_revenue_share": scope0("Tyson sells no beverages."),
    },
    "SYY": {
        "us_consumer_revenue_share": est(0.78, 0.70, 0.82, "Sysco's US Foodservice and SYGMA segments are roughly four-fifths of sales; international is the rest. Restaurant demand follows consumer spending."),
        "snap_grocery_spend_share": scope0("SNAP benefits cannot buy restaurant meals (outside the limited Restaurant Meals Program)."),
    },
    "PFGC": {
        "us_consumer_revenue_share": est(0.97, 0.90, 1.0, "Performance Food Group operates in the US (foodservice, Vistar and Core-Mark convenience); small Canadian convenience operations."),
        "snap_grocery_spend_share": scope0("Distributor: SNAP redemptions are captured by retailers."),
    },
    # --- TMT: China shares copied from NVIDIA onto unlike chipmakers
    "QCOM": {
        "us_import_share_of_cogs": est(0.05, 0.02, 0.15, "Qualcomm is fabless and ships mostly to handset and device makers that assemble in Asia, so little of its product is imported into the US by Qualcomm; device-level tariffs reach it only through demand. Replaces an NVIDIA prior (0.45)."),
        "greater_china_revenue_share": est(0.45, 0.35, 0.50, "Qualcomm reports revenue by customer headquarters; China (incl. Hong Kong) was roughly 45% in recent 10-Ks. Replaces an NVIDIA prior (0.091)."),
        "restricted_chip_china_share": est(0.0, 0.0, 0.02, "Mobile SoCs are not covered by the advanced-computing export rules; Huawei licences were already revoked before the baseline."),
    },
    "AMD": {
        "us_import_share_of_cogs": est(0.25, 0.10, 0.40, "Data-center GPUs and CPUs sold to US cloud customers are imported; client and gaming chips go mostly to Asian PC and console assemblers. Replaces an NVIDIA prior (0.45)."),
        "greater_china_revenue_share": est(0.22, 0.15, 0.28, "AMD has reported China (incl. Hong Kong) at around a fifth to a quarter of revenue, much of it to PC/ODM assemblers. Replaces an NVIDIA prior."),
        "restricted_chip_china_share": est(0.03, 0.01, 0.06, "MI308 sales to China required licences from 2025; restricted data-center revenue is a low-single-digit share."),
    },
    "INTC": {
        "greater_china_revenue_share": est(0.28, 0.20, 0.30, "Intel's 10-K reports China (by billing location) at roughly 27–29% of revenue in recent years, largely PC assemblers. Replaces an NVIDIA prior (0.091)."),
        "restricted_chip_china_share": est(0.01, 0.0, 0.03, "Only a small share (Gaudi and some data-center parts) is subject to advanced-computing controls."),
    },
    "LRCX": {
        "greater_china_revenue_share": primary(7859.811 / 23232.4, 0.27, 0.42, "FY2026 10-K revenue by region: China $7,860M of $23,232M total (33.8%); range covers FY2024–26 and end-customer vs ship-to differences.", "LRCX"),
        "restricted_chip_china_share": est(0.03, 0.01, 0.06, "Advanced-node equipment sales to listed Chinese fabs already need licences; a further tightening (e.g. affiliate rules) is estimated at a low-single-digit share of revenue.", FILINGS["LRCX"]),
    },
    "AMAT": {
        "greater_china_revenue_share": est(0.30, 0.25, 0.37, "Applied Materials reported China at about 37% of FY2024 revenue and lower since; equipment export controls are the relevant restriction."),
        "restricted_chip_china_share": est(0.03, 0.01, 0.06, "Sales to restricted Chinese fabs beyond existing licences; management has sized further rule changes at a low-single-digit share of revenue."),
    },
    "TXN": {
        "greater_china_revenue_share": est(0.20, 0.15, 0.25, "Texas Instruments sells broadly to Chinese industrial and automotive customers (around a fifth of revenue); China opened an anti-dumping probe into US analog chips in 2025."),
        "restricted_chip_china_share": scope0("Analog and embedded chips are not covered by advanced-computing export controls."),
    },
    "DELL": {"us_import_share_of_cogs": gap("Dell imports most US-sold hardware, but it is a thin-margin OEM facing an industry-wide cost; the policy's single pass-through range (calibrated for chip designers and platforms) would dominate the result (about -80% EPS at defaults), so no number is published until an OEM-specific pass-through is sourced.")},
    "HPQ": {"us_import_share_of_cogs": gap("HP imports nearly all US-sold PCs and printers, but as a thin-margin OEM its result would be driven by the generic pass-through assumption (about -70% EPS at defaults); left unquantified until an OEM-specific pass-through is sourced.")},
    "ANET": {"us_import_share_of_cogs": est(0.55, 0.30, 0.75, "The Americas are roughly four-fifths of Arista's revenue; switches are contract-manufactured outside the US. Low end allows for USMCA-qualifying Mexican production if exempted.")},
    "TMUS": {
        "us_import_share_of_cogs": est(0.25, 0.15, 0.35, "Like Verizon, handset purchases (all imported) are about a third of T-Mobile's cost of revenue, and customs value is below the carrier's handset cost."),
        "us_users_m": est(110, 90, 135, "T-Mobile serves about 140M connections; unique US people are fewer (tablets, IoT, second lines), following the Verizon convention."),
    },
    "INTU": {
        "us_users_m": est(100, 70, 140, "TurboTax, Credit Karma and QuickBooks serve on the order of 100M US consumers and small businesses."),
        "us_digital_ad_revenue_share": est(0.11, 0.06, 0.13, "Credit Karma's personalized credit and loan offers (about a ninth of revenue) depend on targeting with consumer data, so they are exposed like targeted advertising."),
    },
    # --- industrials addition (were sentinels)
    "GEV": {
        "ind_steel_share_of_cogs": est(0.08, 0.04, 0.12, "Wind towers and nacelles, gas-turbine casings and forgings, and transformer cores (grain-oriented electrical steel) make GE Vernova a heavier steel user than aerospace peers (0.03) but lighter than Caterpillar (0.15)."),
        "ind_infrastructure_capture_share": est(0.004, 0.001, 0.008, "Only the grid share of a broad infrastructure program reaches GE Vernova (transformers, switchgear, grid software); roughly a tenth of outlays are grid, a third of that is equipment, and GE Vernova is one of several large suppliers."),
        "ind_us_qre_musd": est(600, 350, 900, "FY2025 R&D expense was $1,197M (XBRL ResearchAndDevelopmentExpense); about half is assumed US-performed and qualifying. Not a disclosed credit base."),
        "ind_us_pretax_income_share": dict(value=0.271, low=0.028, high=0.514, source="SEC 10-K XBRL income-tax note (domestic/foreign pretax income)", source_url="https://www.sec.gov/Archives/edgar/data/1996810/000199681026000015/0001996810-26-000015-index.htm",
                                           rationale="Average of tagged years used by the Full Market tax shock; FY2025 domestic pretax was $78M of $2,828M and FY2024 $1,285M of $2,498M, so the range is wide.", applicable=True),
        "govcon_defense_intel_share": scope0("GE Vernova sells power-generation, wind and grid equipment; defense and intelligence sales are not a reported business."),
    },
    # --- public sector: shares copied from GD (primes) or a BAH/CACI median (services)
    **{t: {"govcon_us_gov_share": est(g, *gr, why), "govcon_defense_intel_share": est(d, *dr, why), "govcon_civilian_share": est(c, *cr, why)}
       for t, (g, gr, d, dr, c, cr, why) in {
        "LMT": (0.73, (0.70, 0.76), 0.69, (0.65, 0.73), 0.04, (0.02, 0.06), "Lockheed Martin reports roughly three-quarters of sales from the US government (FMS included), almost all DoD; NASA and other civil work is small. Replaces a GD prior."),
        "NOC": (0.86, (0.83, 0.89), 0.82, (0.78, 0.86), 0.04, (0.02, 0.06), "Northrop Grumman reports about 85% of sales to the US government, overwhelmingly DoD and intelligence; NASA is a small civil share. Replaces a GD prior."),
        "RTX": (0.45, (0.42, 0.48), 0.43, (0.40, 0.46), 0.02, (0.01, 0.03), "RTX reports a little under half of sales from the US government (Raytheon, military engines, Collins defense); commercial aerospace is the rest. Replaces a GD prior."),
        "HII": (0.97, (0.95, 0.99), 0.94, (0.90, 0.97), 0.03, (0.01, 0.05), "Huntington Ingalls builds Navy and Coast Guard ships; nearly all revenue is US government, mostly the Navy. Replaces a GD prior."),
        "OSK": (0.22, (0.15, 0.30), 0.12, (0.08, 0.18), 0.10, (0.05, 0.12), "Oshkosh's defense segment is a minority of sales and its USPS delivery-vehicle contract is federal but non-defense; access equipment and vocational trucks are commercial. Replaces a GD prior."),
        "KTOS": (0.70, (0.65, 0.75), 0.68, (0.63, 0.73), 0.02, (0.0, 0.04), "Kratos sells drones, satellites and hypersonics mainly to DoD; about seven-tenths of revenue is US government."),
        "AVAV": (0.62, (0.55, 0.70), 0.60, (0.53, 0.68), 0.02, (0.0, 0.04), "AeroVironment sells small drones and loitering munitions mostly to DoD; international sales (incl. Ukraine aid via FMS) vary."),
        "BWXT": (0.75, (0.70, 0.80), 0.68, (0.62, 0.74), 0.07, (0.04, 0.10), "BWX Technologies' naval nuclear components (funded through DOE Naval Reactors for the Navy) dominate; DOE environmental and NNSA work is non-defense civil."),
        "TXT": (0.22, (0.18, 0.26), 0.21, (0.17, 0.25), 0.01, (0.0, 0.02), "Textron's US-government sales (Bell military, Textron Systems) are about a fifth of revenue; Textron Aviation and industrial products are commercial. Replaces a GD prior."),
        "MRCY": (0.75, (0.65, 0.85), 0.73, (0.63, 0.83), 0.02, (0.0, 0.04), "Mercury Systems sells defense electronics mostly as a subcontractor to US primes on DoD programs."),
        "VSEC": (0.05, (0.02, 0.10), 0.04, (0.01, 0.08), 0.01, (0.0, 0.02), "VSE has sold most of its federal and defense services business and is now mainly an aviation and fleet aftermarket distributor. Replaces a GD prior (0.68)."),
        "KBR": (0.55, (0.45, 0.62), 0.45, (0.35, 0.52), 0.10, (0.06, 0.14), "KBR's Mission Technology Solutions (about two-thirds of revenue) serves DoD, NASA and UK defence; Sustainable Technology Solutions is commercial. Replaces a BAH/CACI median."),
        "ICFI": (0.50, (0.42, 0.56), 0.06, (0.03, 0.10), 0.44, (0.36, 0.50), "ICF earns about half its revenue from US federal agencies, mostly civilian (HHS, USAID, EPA, DOE), plus state/local and commercial clients; defense is small. Replaces a BAH/CACI median (0.71 defense)."),
        "TTEK": (0.22, (0.15, 0.30), 0.06, (0.03, 0.10), 0.16, (0.10, 0.22), "Tetra Tech's US federal work (USAID, EPA, DoD environmental) is about a fifth of revenue after 2025 USAID cuts; most revenue is state/local, commercial and international. Replaces a BAH/CACI median."),
       }.items()},
    # --- transport
    "LUV": {"tl_domestic_passenger_revenue_share": est(0.93, 0.88, 0.97, "Southwest flies an almost entirely domestic network (near-international routes to Mexico and the Caribbean are a few percent of capacity); passenger revenue is most of total revenue. Replaces a Delta prior (0.564).")},
    # --- healthcare devices: import shares copied from PFE/LLY
    "TMO": {"us_import_share_of_cogs": est(0.12, 0.06, 0.20, "About half of Thermo Fisher's revenue is North American and much of it is made in large US plants; imports come from European and Asian sites. Replaces a PFE/LLY drug prior (0.30).")},
    "ABT": {"us_import_share_of_cogs": est(0.15, 0.08, 0.25, "The US is about two-fifths of Abbott's sales; nutrition and diagnostics are largely US-made, while devices come from Ireland, Costa Rica and Asia. Replaces a PFE/LLY prior (0.30).")},
    "MDT": {"us_import_share_of_cogs": est(0.20, 0.12, 0.30, "FY2026 10-K: US revenue $18,103M of $36,364M (49.8%); much US-sold product is made in Ireland, Mexico and other non-US plants (Puerto Rico is domestic). Replaces a PFE/LLY prior (0.30).", FILINGS["MDT"])},
    "ISRG": {"us_import_share_of_cogs": est(0.25, 0.15, 0.35, "FY2025 10-K: US revenue $6,816M of $10,065M (67.7%). Systems are built in California but instruments and accessories (about 60% of revenue) are largely made in Mexicali, Mexico; USMCA exemptions are ignored in this hypothetical.", FILINGS["ISRG"])},
    "CAH": {"us_import_share_of_cogs": est(0.012, 0.006, 0.02, "Cardinal Health's medical products and distribution segment (about 5% of revenue) sources Cardinal-brand gloves, gowns and consumables largely from Asia, roughly $3B of cost; pharmaceutical distribution purchases domestically at manufacturer prices.")},
    "COR": {"us_import_share_of_cogs": est(0.003, 0.0, 0.008, "Cencora is overwhelmingly pharmaceutical distribution bought domestically; only small specialty and animal-health products are imported.")},
    "MCK": {"us_import_share_of_cogs": est(0.005, 0.0, 0.01, "McKesson's medical-surgical business distributes some imported supplies; pharmaceutical distribution is domestic purchasing.")},
}

# ------------------------------------------------------------------ 2. new exposure keys
NEW_DEFS = [
    dict(key="fs_investment_income_revenue_share", label="Investment income share of revenue", unit="fraction",
         help="Net investment income (insurers) or interest on corporate cash and float (payments) ÷ total revenue; the base that reprices when rates move. Banks use the NII channel instead.", min=0.0, max=1.0),
    dict(key="fs_investment_income_sens_per_100bp", label="Investment income change per +100bp (12 months)", unit="number",
         help="Fractional change in that investment income in the first 12 months after a parallel +100bp move (reinvestment and floating-rate share ÷ portfolio yield, net of credited rates).", min=0.0, max=1.0),
    dict(key="grad_private_loan_gain_share", label="Revenue gain from replacing capped federal graduate loans", unit="fraction",
         help="Steady-state revenue gain, as a share of current revenue, if all above-cap graduate borrowers moved to the company's private loans.", min=0.0, max=1.0),
    dict(key="us_combustible_tobacco_revenue_share", label="US cigarette and cigar revenue share", unit="fraction",
         help="Share of total revenue from cigarettes and cigars sold in the US by this manufacturer (the base a federal cigarette excise reaches).", min=0.0, max=1.0),
    dict(key="us_oral_nicotine_revenue_share", label="US oral nicotine and smokeless revenue share", unit="fraction",
         help="Share of total revenue from nicotine pouches, moist snuff and other oral products sold in the US.", min=0.0, max=1.0),
]

INSURER = {  # ticker → (revenue share, sensitivity) as exposure dicts
    "ALL": (primary(3449 / 67685, 0.045, 0.056, "2025 10-K: net investment income $3,449M of $67,685M revenue.", "ALL"),
            est(0.07, 0.04, 0.10, "Short-duration P&C portfolio: roughly a quarter to a third reprices within a year (maturities, new cash, floating and short-term holdings); at a ~4% portfolio yield that is ~7% of investment income per 100bp.", FILINGS["ALL"])),
    "TRV": (primary(3959 / 48828, 0.075, 0.087, "2025 10-K: net investment income $3,959M of $48,828M revenue.", "TRV"),
            est(0.055, 0.03, 0.08, "P&C portfolio with ~4-year duration: about a fifth reprices per year at a ~4% yield, ~5.5% of investment income per 100bp.", FILINGS["TRV"])),
    "PGR": (primary(3549 / 87671, 0.035, 0.046, "2025 10-K: net investment income $3,549M (supplementary insurance information) of $87,671M revenue.", "PGR"),
            est(0.09, 0.05, 0.13, "Progressive runs a short-duration, fast-growing portfolio, so more of it reprices within a year than at most P&C peers.", FILINGS["PGR"])),
    "MET": (primary(22559 / 77084, 0.27, 0.31, "2025 10-K: net investment income $22,559M of $77,084M revenue.", "MET"),
            est(0.015, 0.005, 0.03, "Life insurer general accounts are long duration (under a tenth reinvests per year), floating-rate assets are partly hedged and part of any yield change is credited to policyholders, so the net first-year effect is about 1-2% of investment income per 100bp.", FILINGS["MET"])),
    "PRU": (est(0.30, 0.25, 0.34, "Prudential's net investment income is roughly three-tenths of revenue (life and retirement general account); not taken from the committed filings."),
            est(0.015, 0.005, 0.03, "Long-duration life general account, with hedging and crediting-rate offsets as at MetLife.")),
    "AIG": (est(0.14, 0.10, 0.18, "Post-Corebridge AIG is a P&C insurer whose net investment income is roughly a seventh of revenue; not taken from the committed filings."),
            est(0.06, 0.03, 0.09, "P&C portfolio repricing similar to Travelers and Allstate.")),
    "V": (primary(791 / 40000, 0.015, 0.025, "FY2025 10-K: interest and dividend investment income $791M against $40,000M revenue.", "V"),
          est(0.23, 0.15, 0.30, "Cash and short-term investments reprice within the year; at a ~4.3% yield a 100bp move changes the income by about a quarter.", FILINGS["V"])),
}
FS_GAPS = {"MA": "Mastercard's interest income on cash is not separated in the committed filings.",
           "PYPL": "Interest on customer balances is material but not separated in the committed filings.",
           "SNEX": "StoneX's interest income on client balances is material but its net sensitivity is not disclosed in the committed data.",
           "BLK": "BlackRock's cash yield is immaterial to fee revenue and is not separated in the committed data.",
           "SPGI": "S&P Global's interest income on cash is immaterial and not separated in the committed data."}


def new_values(uni) -> dict[str, dict[str, dict]]:
    """industry → ticker → new-key exposures, covering every company."""
    out: dict[str, dict[str, dict]] = {}
    fs = out.setdefault("financial_services", {})
    for t in uni.industry("financial_services").tickers:
        c = uni.company(t)
        if t in INSURER:
            share, sens = INSURER[t]
            fs[t] = {"fs_investment_income_revenue_share": share, "fs_investment_income_sens_per_100bp": sens}
        elif c.kind == "bank":
            fs[t] = {k: scope0("Banks' rate effect is modeled through the 10-K NII sensitivity channel; adding portfolio income here would double count.")
                     for k in ("fs_investment_income_revenue_share", "fs_investment_income_sens_per_100bp")}
        else:
            fs[t] = {k: gap(FS_GAPS[t]) for k in ("fs_investment_income_revenue_share", "fs_investment_income_sens_per_100bp")}
    ed = out.setdefault("education", {})
    for t in uni.industry("education").tickers:
        ed[t] = {"grad_private_loan_gain_share": est(0.10, 0.04, 0.25, "Sallie Mae is the largest private student lender; ending Grad PLUS and capping federal graduate loans moves several billion dollars a year of borrowing to private lenders. At full uptake that could add on the order of 5–25% to SLM's revenue over time, after credit losses, funding costs and competitors' share; the range is wide.")
                 if t == "SLM" else scope0("Not a lender; schools' lost enrollment is modeled in the other channel.")}
    cr = out.setdefault("consumer_retail", {})
    for t in uni.industry("consumer_retail").tickers:
        if t == "MO":
            cr[t] = {"us_combustible_tobacco_revenue_share": primary(20485 / 23279, 0.85, 0.90, "2025 10-K segment revenue: smokeable products $20,485M of $23,279M (88%), including excise collected.", "MO"),
                     "us_oral_nicotine_revenue_share": primary(2802 / 23279, 0.11, 0.13, "2025 10-K segment revenue: oral tobacco products $2,802M of $23,279M (12%).", "MO")}
        elif t == "PM":
            cr[t] = {"us_combustible_tobacco_revenue_share": est(0.01, 0.005, 0.02, "PMI sells cigars (Swedish Match) but almost no cigarettes in the US."),
                     "us_oral_nicotine_revenue_share": est(0.06, 0.04, 0.09, "ZYN and other Swedish Match oral products in the US are roughly 5–9% of PMI net revenue.")}
        elif t in ("WMT", "COST", "KR", "DG", "DLTR", "PFGC"):
            cr[t] = {k: gap("Sells or distributes tobacco, but the tobacco share of revenue and margin is not disclosed in the committed data; retailer/distributor lost sales are not modeled.")
                     for k in ("us_combustible_tobacco_revenue_share", "us_oral_nicotine_revenue_share")}
        else:
            cr[t] = {k: scope0("Does not make or sell tobacco products in the US (Target stopped selling tobacco in 1996).") if t == "TGT" else scope0("Does not make or sell tobacco products.")
                     for k in ("us_combustible_tobacco_revenue_share", "us_oral_nicotine_revenue_share")}
    return out


def main() -> None:
    """Write corrections, new exposures, definitions and coverage; then apply overrides."""
    uni = load_universe()
    # 1. overrides → canonical exposure files
    ov_path = CONFIG_DIR / "company_exposure_overrides.yaml"
    ov = yaml.safe_load(ov_path.read_text())
    for t, vals in CORRECTIONS.items():
        ov["companies"].setdefault(t, {}).update(vals)
    ov_path.write_text(yaml.safe_dump(ov, sort_keys=False, width=105))
    subprocess.run([sys.executable, str(ROOT / "scripts/apply_exposure_audit.py")], check=True)
    # 2. definitions + values for new keys
    dpath = CONFIG_DIR / "exposure_definitions.d" / "audit_round3.yaml"
    dpath.write_text("# Generated by scripts/apply_round3_audit.py\n" + yaml.safe_dump({"exposures": NEW_DEFS}, sort_keys=False, width=105))
    for slug, companies in new_values(uni).items():
        p = CONFIG_DIR / "exposures" / f"{slug}_audit_round3.yaml"
        p.write_text("# Generated by scripts/apply_round3_audit.py\n" + yaml.safe_dump({"industry": slug, "companies": companies}, sort_keys=False, width=105))
    # 3. coverage + review
    cov_path, rev_path = CONFIG_DIR / "policy_company_coverage.yaml", CONFIG_DIR / "policy_review.yaml"
    cov, rev = yaml.safe_load(cov_path.read_text()), yaml.safe_load(rev_path.read_text())
    pol = cov["policies"]

    def move(key, tickers, status, reason, direction=None):
        groups = pol[key]["groups"]
        for g in groups:
            g["tickers"] = [t for t in g["tickers"] if t not in tickers]
        target = next((g for g in groups if g["status"] == status and (status != "included" or g.get("reason") == reason or reason is None)), None)
        if target is None:
            target = dict(status=status, tickers=[], reason=reason)
            if direction:
                target["default_direction"] = direction
            groups.append(target)
        target["tickers"] += [t for t in tickers if t not in target["tickers"]]
        pol[key]["groups"] = [g for g in groups if g["tickers"]]

    inc = lambda key: next(g["reason"] for g in pol[key]["groups"] if g["status"] == "included")  # noqa: E731
    # fed rate: insurers + Visa now included via the investment-income channel
    k = "financial_services/fed_rate_change"
    move(k, ["ALL", "TRV", "PGR", "MET", "PRU", "AIG", "V"], "included",
         "Rate moves reprice insurer portfolios and corporate cash; a default rate cut lowers investment income.",
         dict(metric="dR", sign=-1))
    move(k, ["MA", "PYPL", "SNEX", "BLK", "SPGI"], "unquantified",
         "Interest income on cash or client balances exists but its sensitivity is not separated in the committed data. Missing exposure is not evidence of no impact.")
    # borrowing caps: SLM gains
    k = "education/student_loan_borrowing_caps"
    move(k, ["SLM"], "included", "Private student lenders gain graduate borrowing displaced from capped federal loans.", dict(metric="dR", sign=1))
    # TMT
    for k, ts in [("tmt/chip_export_controls", ["AMAT", "LRCX", "TXN"]), ("tmt/semiconductor_tariffs", ["ANET", "TMUS"]), ("tmt/data_privacy_mandate", ["INTU", "TMUS"]), ("tmt/digital_services_tax", ["INTU"])]:
        move(k, ts, "included", inc(k))
    for k in ["industrials/steel_tariffs", "industrials/infrastructure_spending", "industrials/rd_credit_expansion", "industrials/corporate_tax_rate_change"]:
        move(k, ["GEV"], "included", inc(k))
    move("industrials/corporate_tax_rate_change", ["CLF"], "conditional",
         "Baseline pretax loss: a statutory rate change has no current-tax effect until US income turns positive; deferred-tax remeasurement is not modeled.")
    move("industrials/defense_procurement_increase", ["GEV"], "outside_scope", "No material defense or intelligence revenue.")
    move("tmt/semiconductor_tariffs", ["DELL", "HPQ"], "unquantified",
         "Thin-margin hardware OEM: results would be dominated by the generic pass-through assumption; an OEM-specific pass-through is not sourced. Missing exposure is not evidence of no impact.")
    # consumer demand-side policies for the six additions
    for k in ["consumer_retail/consumer_tax_rebate", "consumer_retail/sales_tax_change"]:
        move(k, ["MDLZ", "MO", "PM", "TSN", "SYY", "PFGC"], "included", inc(k))
    move("consumer_retail/snap_benefit_change", ["MDLZ", "MO", "PM", "TSN", "SYY", "PFGC"], "outside_scope",
         "SNAP redemptions are captured by grocery retailers; manufacturers, distributors and tobacco are outside the benefit's direct reach.")
    move("consumer_retail/sweetened_beverage_tax", ["MDLZ", "MO", "PM", "TSN"], "outside_scope",
         "Company sells no covered US beverages.")
    # new policies
    tick_cr = uni.industry("consumer_retail").tickers
    pol["consumer_retail/tobacco_excise_increase"] = dict(
        references=["https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section5701&num=0&edition=prelim"],
        groups=[dict(status="included", tickers=["MO", "PM"], reason="A higher excise raises shelf prices and cuts US tobacco volume.", default_direction=dict(metric="dR", sign=-1)),
                dict(status="unquantified", tickers=[t for t in ("WMT", "COST", "KR", "DG", "DLTR", "PFGC") if t in tick_cr], reason="Sells or distributes tobacco, but the tobacco share is not disclosed in the committed data. Missing exposure is not evidence of no impact."),
                dict(status="outside_scope", tickers=[t for t in tick_cr if t not in ("MO", "PM", "WMT", "COST", "KR", "DG", "DLTR", "PFGC")], reason="Does not make or sell tobacco products.")])
    tick_hc = uni.industry("healthcare").tickers
    dev = ["TMO", "ABT", "MDT", "ISRG", "CAH", "COR", "MCK"]
    pol["healthcare/medical_device_tariffs"] = dict(
        references=["https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title19-section1862&num=0&edition=prelim"],
        groups=[dict(status="included", tickers=dev, reason="Device makers and medical-products distributors pay tariffs on imported devices and supplies.", default_direction=dict(metric="dNI", sign=-1)),
                dict(status="outside_scope", tickers=[t for t in tick_hc if t not in dev], reason="Drugmakers, insurers and hospitals: drug tariffs are a separate policy and hospitals' higher supply costs are not modeled. J&J MedTech imports are not separated from its drug supply.")])
    rr = rev["reviews"]
    rr["financial_services/fed_rate_change"]["expect"].append(dict(ticker="MET", metric="dR", sign=-1))
    r = rr["education/student_loan_borrowing_caps"]
    r["unaffected"] = [t for t in r.get("unaffected", []) if t != "SLM"]
    r["expect"].append(dict(ticker="SLM", metric="dR", sign=1))
    rr["consumer_retail/tobacco_excise_increase"] = dict(rationale="A higher excise cuts US cigarette volume; non-tobacco firms are unaffected.",
                                                         expect=[dict(ticker="MO", metric="dR", sign=-1)], unaffected=["TGT", "NKE", "KO"])
    rr["healthcare/medical_device_tariffs"] = dict(rationale="Device importers pay the tariff; drugmakers are covered elsewhere.",
                                                   expect=[dict(ticker="MDT", metric="dNI", sign=-1), dict(ticker="ISRG", metric="dNI", sign=-1)], unaffected=["PFE", "UNH", "HCA"])
    cov_path.write_text(yaml.safe_dump(cov, sort_keys=False, width=105))
    rev_path.write_text(yaml.safe_dump(rev, sort_keys=False, width=105))
    print("round-3 corrections applied")


if __name__ == "__main__":
    main()
