# Bellwether — Industry Policy Impact Simulator

Simulate how a policy change (tariffs, tax changes, rate moves, Medicare rates…) hits the revenue, margins,
EPS and implied value of 203 real US companies, using their latest SEC filings.

**Status:** Python engine, Streamlit interface (Industry simulator, Full Market with 10 macro shocks, Backtests,
Methodology, Data, About) and tactical web console implemented. The Streamlit app is ready for Streamlit Community
Cloud (`app.py`, `requirements.txt`, `.streamlit/config.toml`); no public deployment yet. The web console does not
have a Full Market view yet.

## Tactical console interface

The new interface lives in `web/`; the existing Streamlit app remains available.
The attached interface brief is preserved as [UI_SPEC.md](UI_SPEC.md). The existing
Python engine and `METHODOLOGY.md` govern calculations; no separate `SPEC.md` was supplied.

```bash
cd web
npm ci
npm run build
cd ..
PYTHONPATH=src .venv/bin/python -m policyshock.ui.api
```

Open `http://127.0.0.1:8787` and `/styleguide`. For frontend development, run the
Python server and `npm run dev` in `web/` in a second terminal. The development
proxy uses the same Python calculations and committed snapshots. The local preview
adapter uses Python's standard library and adds no Python dependencies.

The web console uses an OLED black/amber HUD, collapsible utility rail and ordered
industry → policy → parameters → execution controls. Results link a Canvas Field,
exposure scatter and company inspector to a dense financial grid with projected
values, percentage changes, filed EPS sparklines and scenario whiskers. Drivers
and Sources retain model attribution, sensitivities and provenance. CSS motion
includes a brief initialization scan, actual request elapsed time and fast state
transitions, with reduced-motion support and a motion toggle. Company profiles use
short editing stages and financial groups.

See [design/TACTICAL_CONSOLE.md](design/TACTICAL_CONSOLE.md) for the current design
contract. Historical checkpoint reports remain in `design/reviews/`. Full Market
web UI and broadly editable policy assumptions remain separate product work.

```bash
cd web && npm run build && npm test
# From the repository root:
.venv/bin/python -m pytest -q tests/test_instrument_api.py
```

## Run locally
```bash
uv venv --python 3.11 .venv
uv pip install --python .venv/bin/python -r requirements.txt
.venv/bin/streamlit run app.py
.venv/bin/python -m pytest -q
```
The app runs entirely from committed snapshots in `data/snapshots/`, with no keys needed.
`scripts/refresh_data.py` rebuilds them from SEC EDGAR, FRED and yfinance.

## Company coverage and user profiles

Each industry has 20–30 selected public issuers (203 total: 20 in nine industries,
23 in Financial Services), spanning documented business subsectors. SEC issuer names,
CIKs, annual filings and public prices were fetched from APIs. This is a curated
teaching sample, not a statistically representative or complete market index.
See `data/snapshots/sample_coverage.json` for the added companies and sampling strata.

Run an industry scenario, then choose **Model a company**. Search the SEC directory
for a public issuer, including one outside the sample, or start a blank profile.
Review missing financial fields and enter the selected policy's exposures. Peer
estimates are an explicit opt-in. Company results use the existing Python engine,
show a P&L bridge, ranges, sensitivity and reference-company comparisons. JSON
profile import/export preserves inputs; custom financials are excluded from share URLs.
Profiles remain in browser memory until exported and are not saved to the server.

The APIs cannot supply every policy exposure or private-company financials.
Expanded-sample exposures are labeled peer estimates with a rationale; structural
scope exclusions are explicit. Unavailable values in new company lookups remain
blank for review. Foreign issuers without supported US-GAAP annual 10-K facts and
private companies can use manual entry. No paid APIs, new Python dependencies or
runtime LLM calls were added.

`PYTHONPATH=src .venv/bin/python scripts/expand_universe.py --activate` rebuilds the
expanded selection from the public APIs. Then rebuild GDP betas (the regular
`scripts/refresh_data.py` also refreshes all configured companies and betas).

## Data
- **SEC EDGAR** XBRL company facts: baseline financials for FY2008→latest (free, keyless)
- **FRED** (keyless CSV): fed funds, 10-yr Treasury, mortgage rate, CPI, unemployment, real GDP
- **yfinance**: latest closes, with a committed fallback snapshot

Refreshed every weekday by GitHub Actions. See [METHODOLOGY.md](METHODOLOGY.md).

## Team
Keith LoboPrabhu.

### Current data and historical validation

The web server refreshes Yahoo five-minute quotes every five minutes, FRED hourly,
and supported SEC annual statements every six hours. The Data page shows provider
status, observation dates, latest annual inputs and on-demand Yahoo/TTM company
metrics. Cached/committed fallbacks remain visible during provider failures. These
free sources may be delayed; annual statements and macro releases update on their
own schedules. Live cache files are ignored and never rewrite committed backtest
histories.

Backtests now cover all ten industries. The headline is a pooled **directional hit
rate**, with sample counts, all exclusions, sector scores and per-case magnitude
errors. Six sector cases share the TCJA episode; these are retrospective replays
with current exposures, not independent out-of-sample forecast validation. See
METHODOLOGY §3 and §8 for selection rules, source provenance and refresh semantics.

### Full policy audit

Run `.venv/bin/python scripts/audit_policies.py` after policy/exposure changes.
The generated [policy audit](design/reviews/POLICY_AUDIT.md) covers all 66 industry
policies and 10 macro shocks, with company scope, valid input boundaries, accounting,
scenario bounds and remaining estimate/coverage limitations. Economic review entries
live in `config/policy_review.yaml` and are enforced by the normal test suite.

With the local console running, `.venv/bin/python scripts/audit_running_console.py`
also checks every policy/input boundary against API-fed baselines, including exact
company coverage, independent scope/directions and attribution.
