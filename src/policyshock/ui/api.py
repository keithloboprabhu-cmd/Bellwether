"""Snapshot and public-company HTTP adapter for the Instrument UI; all math stays in Python.

Run ``PYTHONPATH=src .venv/bin/python -m policyshock.ui.api`` after building web/.
Industry scenarios use committed snapshots; explicit company lookup uses public APIs.
"""

from __future__ import annotations

import hashlib
import json
import math
import mimetypes
from functools import lru_cache
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

from pydantic import ValidationError
import pandas as pd

from policyshock.config import CONFIG_DIR, ROOT, SNAPSHOT_DIR, load_universe
from policyshock.company.profiles import CompanyProfile, lookup_company, peer_exposures, run_company, search_companies
from policyshock.data import fred, live, prices, store
from policyshock.engine.scenarios import prepare_baselines
from policyshock.engine.simulate import simulate
from policyshock.narrative.templates import company_reason
from policyshock.policies.loader import registry
from policyshock.policies.coverage import coverage_result

DIST = ROOT / "web" / "dist"
MAX_BODY = 65_536


def clean_json(value):
    """Convert non-finite snapshot values into explicit missing JSON values."""
    if isinstance(value, float) and not math.isfinite(value):
        return None
    if isinstance(value, dict):
        return {k: clean_json(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [clean_json(v) for v in value]
    return value


@lru_cache(maxsize=1)
def versions() -> dict:
    """Identify exact current engine/config and committed data contents."""
    def digest(paths):
        h = hashlib.sha256()
        for path in sorted(paths):
            h.update(str(path.relative_to(ROOT)).encode())
            h.update(path.read_bytes())
        return h.hexdigest()[:16]

    return {
        "model": digest([*CONFIG_DIR.rglob("*.yaml"), *(ROOT / "src/policyshock/engine").glob("*.py"), *(ROOT / "src/policyshock/company").glob("*.py"), *(ROOT / "src/policyshock/data").glob("*.py")]),
        "data": digest(SNAPSHOT_DIR.glob("*.*")),
    }


def catalog() -> dict:
    """Return validated configuration and actual committed snapshot coverage."""
    u, reg = load_universe(), registry()
    return {
        "industries": [{"id": i.slug, "name": i.name, "count": len(i.tickers),
                        "companies": [{"ticker": c.ticker, "name": c.name, "subsector": c.subsector} for c in i.companies],
                        "policies": [p.model_dump() for p in reg.industry_policies(i.slug)]} for i in u.industries],
        "company_count": len(u.all_tickers), "meta": store.load_meta(), "versions": versions(), "data_status": live.service.status(),
        "exposure_definitions": {k: v.model_dump() for k, v in reg.exposure_defs.items()},
    }


def projected_metrics(c) -> dict:
    """Pair the engine's absolute deltas with explicit starting and projected values.

    Net income uses the model baseline; EPS uses stated starting EPS. Percentages
    on nonpositive earnings bases and undefined P/E valuation remain unavailable.
    """
    b = c.baseline
    model_ni = b["pretax_income"] * (1 - c.tax_rate) * b.get("parent_share", 1.0)
    def pair(base, delta, pct=None, supplied=False):
        return {"baseline": base, "projected": base + delta if base is not None and delta is not None else None,
                "delta": delta, "percent": pct if supplied else delta / base if base is not None and base > 0 and delta is not None else None}
    return {
        "revenue": pair(b.get("revenue"), c.dR),
        "operating_income": pair(b.get("operating_income"), c.dEBIT),
        "net_income": pair(model_ni, c.dNI),
        "eps": pair(b.get("eps_diluted"), c.dEPS, c.dEPS_pct, True),
        "price": pair(b.get("price"), c.dP, c.dP_pct, True),
    }


def calculate(payload: dict) -> dict:
    """Validate an industry or company request and serialize one engine result."""
    if not isinstance(payload, dict) or set(payload) - {"industry", "policy", "inputs", "versions", "company"}:
        raise ValueError("Use industry, policy and numeric inputs from the policy configuration.")
    ind, pid = payload.get("industry"), payload.get("policy")
    if not isinstance(ind, str) or not isinstance(pid, str):
        raise ValueError("Choose an industry and a compatible policy.")
    try:
        pol = registry().policy(ind, pid)
    except KeyError as exc:
        raise ValueError("This policy is unavailable for the selected industry. Choose another policy.") from exc
    captured = live.service.capture() if live.service.active else None
    supplied_versions = payload.get("versions")
    if supplied_versions is not None and (not isinstance(supplied_versions, dict) or set(supplied_versions) != {"model", "data"} or not all(isinstance(v, str) for v in supplied_versions.values())):
        raise ValueError("Provide model and data version identifiers as strings.")
    if supplied_versions and (supplied_versions != versions() if not captured else supplied_versions.get("model") != versions()["model"]):
        raise ValueError("This link uses a different model or data version. Return home to run it with current snapshots.")
    inputs = payload.get("inputs", {})
    if not isinstance(inputs, dict) or set(inputs) - {x.key for x in pol.user_inputs}:
        raise ValueError("The scenario contains unsupported input fields. Choose a policy again.")
    inputs = pol.default_inputs() | inputs
    for item in pol.user_inputs:
        value = inputs[item.key]
        if isinstance(value, bool) or not isinstance(value, (float, int)) or not math.isfinite(value):
            raise ValueError(f"{item.label}: enter a finite number in {item.unit}.")
        if (item.min is not None and value < item.min) or (item.max is not None and value > item.max):
            raise ValueError(f"{item.label}: enter a value between {item.min:g} and {item.max:g} {item.unit}.")
    # A single immutable capture serves the entire calculation; historical tests
    # continue using committed records. User profiles retain their stated inputs.
    profile = CompanyProfile.model_validate(payload["company"]) if "company" in payload else None
    if profile and profile.industry != ind:
        raise ValueError("The company profile's industry must match the scenario industry.")
    live_kw = {} if not captured else {"baselines": prepare_baselines(pd.DataFrame(live.service.baseline_rows(load_universe().industry(ind).tickers, captured))), "macro": fred.macro_context(captured["macro"])}
    reference = simulate(ind, pid, inputs=inputs, prices_df=captured["prices"] if captured else prices.load_snapshot(), **live_kw)
    an = run_company(profile, pid, inputs, **({"macro": live_kw["macro"]} if captured else {})) if profile else reference
    subject_id = an.base.companies[0].ticker if profile else None
    if profile:
        an.envelopes.update(reference.envelopes)
    reg = registry()
    companies = []
    for c in [*an.base.companies, *(reference.base.companies if profile else [])]:
        envelope = an.envelopes[c.ticker]
        exposure_cfg = profile.exposures if profile and c.ticker == subject_id else reg.exposures[c.ticker]
        reason = (c.dominant.label if c.dominant else "No directly modeled channel") if c.ticker == subject_id else company_reason(c, reg, skip_label=c.dominant.label if c.dominant else None)
        if pol.exposure_keys and all(not exposure_cfg[k].applicable for k in pol.exposure_keys):
            reason = "This policy has no directly modeled exposure for this company; other economic effects are not covered."
        coverage = coverage_result(pol, c, inputs, exposure_cfg, custom=c.ticker == subject_id)
        if coverage['status'] != 'modeled':
            reason = coverage['reason']
        companies.append({
            "id": c.ticker, "name": c.name, "eps": c.dEPS_pct,
            "is_custom": c.ticker == subject_id,
            "display_ticker": (profile.ticker or "Custom") if c.ticker == subject_id else c.ticker,
            "low": envelope.low.dEPS_pct, "high": envelope.high.dEPS_pct,
            "value_low": envelope.low.dP_pct, "value_high": envelope.high.dP_pct,
            "value": c.dP_pct, "revenue": c.dR, "margin": c.d_margin_bps,
            "dEPS": c.dEPS, "dNI": c.dNI, "market_value": c.d_mcap,
            "dEBIT": c.dEBIT, "dPTI": c.dPTI, "tax_rate": c.tax_rate, "tax_rate_new": c.tax_rate_new,
            "reason": reason, "notes": c.notes, "coverage": coverage,
            "baseline": c.baseline,
            "metrics": projected_metrics(c),
            "history": [] if c.ticker == subject_id else [
                {"year": y["fiscal_year"], "eps": y["items"].get("eps_diluted")}
                for y in reversed((captured["companies"].get(c.ticker, {}).get("years", store.company_years(c.ticker)) if captured else store.company_years(c.ticker))[:8])
            ],
            "channels": [{"label": o.label, "family": o.family, "dNI": o.dNI,
                          "dValue": o.dP * (c.baseline.get("shares_outstanding") or c.baseline["diluted_shares"]) if o.dP is not None and c.baseline.get("price") is not None else None} for o in c.outcomes],
            "exposures": [{"key": key, "label": reg.exposure_defs[key].label,
                           "unit": reg.exposure_defs[key].unit, **exposure_cfg[key].model_dump()}
                          for key in pol.exposure_keys],
        })
    totals = an.base.totals()
    bounds = [an.industry_low.totals()["d_eps_pct"], an.industry_high.totals()["d_eps_pct"]]
    value_bounds = [an.industry_low.totals()["d_mcap_pct"], an.industry_high.totals()["d_mcap_pct"]]
    if profile:
        subject = an.base.companies[0]
        totals["d_eps_pct"] = subject.dEPS_pct
        bounds = [an.envelopes[subject_id].low.dEPS_pct, an.envelopes[subject_id].high.dEPS_pct]
        value_bounds = [an.envelopes[subject_id].low.dP_pct, an.envelopes[subject_id].high.dP_pct]
    channels = {}
    channel_values = {}
    for c in companies[:1] if profile else companies:
        for o in c["channels"]:
            channels[o["label"]] = channels.get(o["label"], 0) + o["dNI"]
            before = channel_values.get(o["label"], 0)
            channel_values[o["label"]] = before + o["dValue"] if before is not None and o["dValue"] is not None else None
    dominant = max(channels, key=lambda k: abs(channels[k]), default=None)
    unquantified = bool(pol.exposure_keys) and all(
        e["value"] == 0 and e["high"] == 0 for c in companies for e in c["exposures"]
    )
    return clean_json({
        "industry": ind, "industry_name": load_universe().industry(ind).name,
        "mode": "company" if profile else "industry", "subject_id": subject_id,
        "profile": profile.model_dump(mode="json") if profile else None,
        "policy": pol.model_dump(), "inputs": inputs, "totals": totals,
        "range": bounds, "value_range": value_bounds,
        "coverage_notice": "No quantified direct exposure in this sample. Enter a company with a supported exposure to model this policy." if unquantified else None,
        "companies": companies, "long": reference.long.ticker if reference.long else None,
        "short": reference.short.ticker if reference.short else None,
        "notes": reference.notes, "low_conviction": reference.low_conviction,
        "exposure_estimates": any(e["source"] == "estimate" and e.get("applicable", True) for c in companies for e in c["exposures"]),
        "dominant": dominant, "channels": [{"label": k, "dNI": v, "dValue": channel_values[k]} for k, v in channels.items()],
        "tornado": [{"key": b.driver.key, "label": b.driver.label, "unit": b.driver.unit,
                     "input_low": b.driver.low, "input_high": b.driver.high,
                     "result_low_input": b.low_value, "result_high_input": b.high_value,
                     "span": b.swing} for b in an.tornado],
        "tornado_metric": an.metric, "versions": {**versions(), **({"data": captured["data_version"]} if captured else {})}, "meta": store.load_meta(),
        "data_status": captured["status"] if captured else live.service.status(),
        "captured_at": captured["captured_at"] if captured else None,
        "data_update_notice": "Scenario rerun with current data; the shared link's data version differs." if captured and supplied_versions and supplied_versions.get("data") != captured["data_version"] else None,
    })


class Handler(BaseHTTPRequestHandler):
    """Same-origin JSON API and static frontend, bound to localhost by default."""

    def send_json(self, value, status=200):
        """Send finite UTF-8 JSON without caching mutable calculation responses."""
        body = json.dumps(clean_json(value), allow_nan=False).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        try:
            self.wfile.write(body)
        except (BrokenPipeError, ConnectionResetError):
            pass  # the browser canceled an older request

    def do_GET(self):
        """Serve actual configuration, sources, methodology or built local assets."""
        path = urlsplit(self.path).path
        try:
            if path == "/api/catalog":
                return self.send_json(catalog())
            if path == "/api/live":
                captured = live.service.capture()
                return self.send_json({"status": captured["status"], "macro": captured["macro"], "captured_at": captured["captured_at"]})
            if path == "/api/company/metrics":
                ticker = parse_qs(urlsplit(self.path).query).get("ticker", [""])[0]
                return self.send_json(live.service.company_metrics(ticker))
            if path == "/api/company/search":
                query = parse_qs(urlsplit(self.path).query).get("q", [""])[0]
                return self.send_json({"companies": search_companies(query)})
            if path == "/api/methodology":
                return self.send_json({"text": (ROOT / "METHODOLOGY.md").read_text()})
            if path == "/api/data":
                captured = live.service.capture()
                return self.send_json({"rows": clean_json(live.service.baseline_rows(load_universe().all_tickers, captured)), "status": captured["status"], "macro": captured["macro"]})
            if path == "/api/backtests":
                from policyshock.backtests.suite import report
                return self.send_json(report())
            if path.startswith("/api/"):
                return self.send_json({"error": "This endpoint is unavailable."}, 404)
            asset = (DIST / path.lstrip("/")).resolve()
            if not asset.is_relative_to(DIST.resolve()):
                return self.send_json({"error": "Invalid path."}, 400)
            if not asset.is_file():
                if Path(path).suffix:
                    return self.send_json({"error": "Asset not found."}, 404)
                asset = DIST / "index.html"
            if not asset.exists():
                return self.send_json({"error": "Build the frontend first: cd web && npm run build"}, 503)
            body = asset.read_bytes()
            self.send_response(200)
            self.send_header("Content-Type", mimetypes.guess_type(asset.name)[0] or "application/octet-stream")
            self.send_header("Content-Length", str(len(body)))
            self.send_header("X-Content-Type-Options", "nosniff")
            self.end_headers()
            self.wfile.write(body)
        except (ValueError, KeyError) as exc:
            self.send_json({"error": str(exc)}, 422)
        except Exception:
            self.log_error("Failed to read committed data")
            self.send_json({"error": "Committed data could not be loaded. Check the snapshots and retry."}, 500)

    def do_POST(self):
        """Reject oversized or invalid scenarios before calculating results."""
        path = urlsplit(self.path).path
        if path not in {"/api/scenario", "/api/company/lookup", "/api/company/peers", "/api/company/validate", "/api/live/refresh"}:
            return self.send_json({"error": "This endpoint is unavailable."}, 404)
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if not 0 < length <= MAX_BODY:
                return self.send_json({"error": "Scenario or company profile must be valid JSON smaller than 64 KiB."}, 413)
            body = json.loads(self.rfile.read(length))
            if not isinstance(body, dict):
                raise ValueError("Provide a JSON object.")
            if path == "/api/live/refresh":
                return self.send_json(live.service.refresh(), 202)
            if path == "/api/company/lookup":
                return self.send_json(lookup_company(body["ticker"], body["industry"]))
            if path == "/api/company/peers":
                return self.send_json({"exposures": peer_exposures(body["industry"], body["policy"], body["revenue"])})
            if path == "/api/company/validate":
                return self.send_json(CompanyProfile.model_validate(body).model_dump(mode="json"))
            self.send_json(calculate(body))
        except ValidationError as exc:
            messages = []
            for error in exc.errors(include_url=False, include_input=False):
                location = " / ".join(str(k).replace("_", " ") for k in error["loc"])
                message = error["msg"].removeprefix("Value error, ")
                messages.append(f"{location}: {message}" if location else message)
            self.send_json({"error": "; ".join(messages)}, 422)
        except (ValueError, TypeError, KeyError) as exc:
            self.send_json({"error": str(exc)}, 422)
        except Exception:
            self.send_json({"error": "The snapshot calculation failed. Your previous result is retained. Retry or choose another policy."}, 500)


def main():
    """Launch the local Instrument server with a configurable port."""
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=8787)
    parser.add_argument("--host", default="127.0.0.1")
    args = parser.parse_args()
    catalog()  # validate config before accepting requests
    server = ThreadingHTTPServer((args.host, args.port), Handler)
    live.service.start()
    print(f"Bellwether: http://{args.host}:{args.port}", flush=True)
    server.serve_forever()


if __name__ == "__main__":
    main()
