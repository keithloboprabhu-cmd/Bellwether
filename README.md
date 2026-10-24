# PolicyShock — Industry Policy Impact Simulator

Simulate how a policy change (tariffs, tax changes, rate moves, Medicare rates…) hits the revenue, margins,
EPS and implied value of 60 real US companies, using their latest SEC filings.

**Status:** milestone M1 (data layer) complete. Live link: _coming at deploy (M4)_.

## Run locally
```bash
uv venv --python 3.11 .venv
uv pip install --python .venv/bin/python -r requirements.txt
.venv/bin/streamlit run app.py
.venv/bin/python -m pytest -q
```
The app runs entirely from committed snapshots in `data/snapshots/`, with no keys needed.
`scripts/refresh_data.py` rebuilds them from SEC EDGAR, FRED and yfinance.

## Data
- **SEC EDGAR** XBRL company facts: baseline financials for FY2008→latest (free, keyless)
- **FRED** (keyless CSV): fed funds, 10-yr Treasury, mortgage rate, CPI, unemployment, real GDP
- **yfinance**: latest closes, with a committed fallback snapshot

Refreshed every weekday by GitHub Actions. See [METHODOLOGY.md](METHODOLOGY.md).

## Team
Keith LoboPrabhu. Built with [Claude Code](https://claude.com/claude-code).

_Educational project for Duke FMKT 256. Not investment advice._
