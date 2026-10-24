# PolicyShock — conventions for Claude Code

Streamlit app simulating first-order policy impacts on 60 real companies (Duke FMKT 256).
Full spec: the build prompt the team pasted at project start; summary in README.md.

## Hard rules
- **No paid APIs or services, ever. No LLM calls at runtime.** Data: SEC EDGAR (keyless),
  FRED fredgraph CSV (keyless), yfinance (unofficial, wrapped). Narratives are templates.
- **Never invent data or citations.** Unsourced assumptions use `source: estimate` + a one-line `rationale`.
- Ask before adding a dependency not in requirements.txt.
- Keep METHODOLOGY.md in sync with the engine; docstrings on every module and public function.

## Layout
- `src/policyshock/` — library code (`data/`, `engine/`, `policies/`, `narrative/`, `company/`, `macro/`, `backtests/`, `ui/`)
- `app.py`, `pages/` — Streamlit entry points; each adds `src/` to `sys.path`
- `config/` — YAML: industries, exposure definitions, exposures, policies, macro shocks
- `data/snapshots/` — committed data the app reads on cold start (rebuilt by `scripts/refresh_data.py`)
- `data/cache/` — raw EDGAR responses (git-ignored)

## Commands
```bash
.venv/bin/python -m pytest -q                  # tests
.venv/bin/streamlit run app.py                 # app on :8501
.venv/bin/python scripts/refresh_data.py       # rebuild all snapshots (≈1 min)
.venv/bin/python scripts/make_fixtures.py      # regenerate parser test fixtures
```

## Data notes
- Universe changes vs. the original spec: ATGE → **CVSA** (Adtalem renamed Covista, Jan 2026);
  XOM re-registered under a holding-company CIK in 2026, so `predecessor_ciks: [34088]` merges its history.
- Company `kind` (standard / bank / reit / managed_care) picks the income-statement template.
- Flags on a fiscal year mean a value was derived or defaulted; the Data page shows them.

## Adding a policy
Drop a YAML in `config/policies/<industry>/` (schema in `src/policyshock/policies/schema.py`).
No code changes should be needed; the smoke test runs it on every company in the industry.
