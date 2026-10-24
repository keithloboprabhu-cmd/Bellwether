# Methodology

PolicyShock is a **first-order, partial-equilibrium** model for education. It is not investment advice.
This document is kept in sync with the code; section numbers follow the engine modules.

## 1. Data

### 1.1 Baseline financials (SEC EDGAR)
Source: `data.sec.gov/api/xbrl/companyfacts` (all XBRL facts per filer), keyless, with a declared
User-Agent and throttled to 8 requests/second (SEC limit: 10).

Rules (`src/policyshock/data/baseline.py`):
- Only 10-K / 10-K/A / 10-KT facts. Income-statement items must cover **350–380 days**, which drops quarterly facts.
- A fiscal year is identified by its **period-end date** and labelled with that calendar year
  (Walmart's year ending 31 Jan 2026 = FY2026, matching the company's own convention).
- **Restatements:** when several 10-Ks report the same period, the most recently filed value wins.
  The *first* 10-K reporting the period is kept as that year's source link.
- **Tag fallback chains** are applied per year (companies change tags over time); the tag used is recorded.
- Derived values are always flagged:
  - Cost of revenue: `Revenue − GrossProfit`, else `CostsAndExpenses − SG&A − R&D`, else
    `Revenue − EBIT − SG&A − R&D` (only if SG&A or R&D exists; otherwise left missing rather than echoing the EBIT margin).
  - Operating income: `PretaxIncome + InterestExpense` when `OperatingIncomeLoss` isn't tagged.
  - Total debt: the largest available complete-debt measure (partial tags can only understate).
- **Effective tax rate** = tax / pretax income, clamped to [0%, 40%] (40% rather than 35% so pre-TCJA years
  aren't distorted). If pretax income ≤ 0 or tax is missing, 21% is used and flagged.
- **Company templates:** banks use net revenue and net interest income (no cost of revenue; EBIT = pretax income);
  managed-care insurers' cost of revenue = product costs + medical claims incurred; REITs use property operating costs.
- Per-share history is as reported in the latest filing covering each year and is **not split-adjusted across years**.
  Backtests therefore compare tax rates and margins, not EPS levels.

Known limitations: firms that report costs by nature (UPS, FDX, DAL, GD) get a cost of revenue close to total
operating costs, so their contribution margin ≈ operating margin, which understates operating leverage
in demand shocks. Some debt totals (GM, DE) aren't in the standard taxonomy and are flagged.

### 1.2 Prices and valuation
Latest close from yfinance, with a committed snapshot (`data/snapshots/prices.csv`, refreshed every weekday) as fallback.
Market cap = price × cover-page shares outstanding (diluted weighted shares for multi-class issuers whose
class-level counts aren't in companyfacts). P/E = price / diluted EPS, only when EPS > 0.

### 1.3 Macro series (FRED)
Keyless `fredgraph.csv` endpoint: DFF, DGS10, MORTGAGE30US, CPIAUCSL, UNRATE, GDPC1.

### 1.4 Refresh
`.github/workflows/refresh.yml` runs `scripts/refresh_data.py` every weekday and commits changed snapshots,
so newly filed 10-Ks, prices and macro data reach the app without manual work.

## 2. Engine
_To be written in milestone M2._
