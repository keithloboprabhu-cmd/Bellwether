"""Build reviewed financial supplements from saved primary filing facts.

Concept and segment selections below were reviewed against the annual statement
or note, not inferred from a similar company. Unresolved debt stays missing.
"""

from pathlib import Path
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from policyshock.config import ROOT
from policyshock.data import store


def main() -> None:
    """Write period-bound source records for exact reviewed filing line items."""
    evidence = json.loads((ROOT / "reports/evidence/filings.json").read_text())
    output = {}

    def record(ticker, key, concepts, member=None, rationale=None):
        e = evidence[ticker]
        selected = []
        for concept in concepts:
            options = [f for f in e["facts"] if f["concept"] == concept
                       and (f.get("instant") == e["period_end"] or f.get("enddate") == e["period_end"])
                       and ((not f.get("dimensions")) if member is None else member in f.get("dimensions", {}).values())]
            if not options:
                raise ValueError(f"{ticker}: source fact missing: {concept}/{member}")
            selected.append(options[0])
        value = sum(f["value"] for f in selected) / 1e6
        company = store.load_baselines()["companies"][ticker]
        entry = output.setdefault(str(company["cik"]), {"ticker": ticker, "period_end": e["period_end"], "items": {}})
        entry["items"][key] = {"value": value, "source_url": e["source_url"], "accessed": e["accessed"],
            "document_location": " + ".join(f'{f["concept"]} context={f["context"]}' for f in selected),
            "rationale": rationale or "Reported annual filing line; normalized to USD millions without a peer estimate."}
        return value

    record("F", "total_debt", ["us-gaap:DebtLongtermAndShorttermCombinedAmount"], "f:CompanyExcludingFordCreditMember",
           "Financing channel uses Ford industrial debt, excluding Ford Credit; finance leases are included in the disclosed debt basis.")
    record("F", "finance_arm_debt", ["us-gaap:DebtLongtermAndShorttermCombinedAmount"], "f:FordCreditMember")
    record("GM", "total_debt", ["gm:DebtandFinanceLeaseLiabilities"], "gm:AutomotiveMember",
           "Financing channel uses automotive debt and finance leases, excluding GM Financial asset-financing debt.")
    record("GM", "finance_arm_debt", ["us-gaap:LongTermDebt"], "gm:GmFinancialMember")
    record("TXT", "total_debt", ["us-gaap:LongTermDebt"], "txt:ManufacturingGroupMember",
           "Financing channel uses Manufacturing Group debt; finance business debt is recorded separately.")
    record("TXT", "finance_arm_debt", ["us-gaap:LongTermDebt"], "txt:FinanceGroupMember")
    record("PCAR", "finance_arm_debt", ["pcar:CommercialPaperBankLoansAndTermDebtAtCarryingValue"], "pcar:FinancialServicesMember")
    pcar = output[str(store.load_baselines()["companies"]["PCAR"]["cik"])]
    pcar["items"]["total_debt"] = {**pcar["items"]["finance_arm_debt"], "value": 0.,
        "document_location": "2025 10-K MD&A, Cash Commitments, p.27; Note J, Borrowings and Credit Arrangements, pp.56–57",
        "rationale": "The filing states all borrowing/term-debt commitments relate to Financial Services; industrial borrowings are zero on that disclosed basis. Finance leases remain separately disclosed."}
    # Deere's supplemental consolidating balance sheet is not numerically tagged.
    # Transcription checked in the actual 2025 10-K, p.43, 2025 columns.
    de = evidence["DE"]
    for key, value, description in [
        ("total_debt", 414 + 1 + 8756, "Equipment Operations: short-term borrowings 414 + securitization 1 + long-term 8,756"),
        ("finance_arm_debt", 13382 + 6595 + 34788, "Financial Services: short-term borrowings 13,382 + securitization 6,595 + long-term 34,788"),
    ]:
        output.setdefault("315189", {"ticker": "DE", "period_end": de["period_end"], "items": {}})["items"][key] = {
            "value": value, "source_url": de["source_url"], "accessed": de["accessed"],
            "document_location": "2025 10-K p.43, Supplemental Consolidating Data, 2025 column; " + description,
            "rationale": "Industrial financing channel excludes financial-services funding; use the separate disclosed equipment-operations balance."}
    for ticker, concepts, member in [
        ("O", ["us-gaap:NotesPayable", "o:RevolvingCreditFacilityAndCommercialPaper", "us-gaap:SecuredDebt"], None),
        ("EQIX", ["us-gaap:DebtInstrumentCarryingAmount"], None),
        ("DLR", ["us-gaap:DebtInstrumentCarryingAmount"], "dlr:DigitalRealtyTrustLPMember"),
        ("ESS", ["us-gaap:SecuredDebt", "us-gaap:UnsecuredDebt"], None),
        ("MAA", ["us-gaap:SecuredDebt", "us-gaap:UnsecuredDebt"], None),
        ("EXR", ["us-gaap:LongTermDebt"], "exr:TermDebtMember"),
        ("ULTA", ["us-gaap:ShortTermBorrowings"], None),
        ("FC", ["us-gaap:NotesPayableCurrent"], None),
        ("MRCY", ["us-gaap:SecuredLongTermDebt"], None),
        ("LINC", ["us-gaap:FinanceLeaseLiabilityCurrent", "us-gaap:FinanceLeaseLiabilityNoncurrent"], None),
    ]:
        record(ticker, "total_debt", concepts, member,
               "Reviewed interest-bearing borrowing/finance-lease line(s); operating lease liabilities are disclosed separately and not repriced as floating-rate loans.")
    # Only explicitly reported expense bases. These include fixed operating costs;
    # no claim is made that the resulting margin is an incremental contribution margin.
    for ticker, concepts in [
        ("KR", ["us-gaap:CostOfGoodsAndServiceExcludingDepreciationDepletionAndAmortization"]),
        ("PGR", ["us-gaap:SupplementaryInsuranceInformationBenefitsClaimsLossesAndSettlementExpense"]),
        ("THC", ["us-gaap:LaborAndRelatedExpense", "us-gaap:SuppliesExpense", "us-gaap:OtherCostAndExpenseOperating"]),
        ("UHS", ["us-gaap:LaborAndRelatedExpense", "us-gaap:SuppliesExpense", "us-gaap:OtherCostAndExpenseOperating"]),
        ("NEE", ["nee:FuelPurchasedPowerAndInterchangeExpense", "us-gaap:UtilitiesOperatingExpenseMaintenanceAndOperations"]),
        ("XPO", ["us-gaap:LaborAndRelatedExpense", "xpo:PurchasedTransportation", "us-gaap:OperatingCostsAndExpenses"]),
        ("SAIA", ["us-gaap:LaborAndRelatedExpense", "saia:PurchasedTransportation", "saia:FuelOperatingExpensesAndSupplies"]),
        ("CSX", ["us-gaap:LaborAndRelatedExpense", "us-gaap:FuelCosts", "us-gaap:OtherCostAndExpenseOperating"]),
        ("LUV", ["us-gaap:LaborAndRelatedExpense", "us-gaap:FuelCosts", "us-gaap:OtherCostAndExpenseOperating"]),
    ]:
        record(ticker, "cost_of_revenue", concepts, rationale=(
            "Insurer cost base is incurred policy losses and settlement expense, not merchandise COGS." if ticker == "PGR" else
            "Reported direct operating-cost base; includes fixed costs, so demand-margin sensitivity remains an estimate requiring review."))
    for ticker, e in evidence.items():
        if "facts" not in e:
            continue
        cik = str(store.load_baselines()["companies"][ticker]["cik"])
        # Keep lease obligations separate from borrowings.
        for key, concept in [("operating_lease_liabilities", "us-gaap:OperatingLeaseLiability"), ("finance_lease_liabilities", "us-gaap:FinanceLeaseLiability")]:
            try:
                record(ticker, key, [concept])
            except ValueError:
                pass
        shares = [f for f in e["facts"] if f["concept"] == "dei:EntityCommonStockSharesOutstanding"]
        if shares:
            date = max(f.get("instant", "") for f in shares)
            current = {f["context"]: f for f in shares if f.get("instant") == date}
            by_class = [f for f in current.values() if any("ClassOfStockAxis" in k for k in f.get("dimensions", {}))]
            selected = by_class or [f for f in current.values() if not f.get("dimensions")][:1]
            if selected:
                entry = output.setdefault(cik, {"ticker": ticker, "period_end": e["period_end"], "items": {}})
                entry["shares_outstanding"] = {"value": sum(f["value"] for f in selected) / 1e6,
                    "date": date, "classes": len(selected), "accn": store.load_baselines()["companies"][ticker]["years"][0]["source_accn"],
                    "source_url": e["source_url"], "accessed": e["accessed"],
                    "document_location": "; ".join(f'{f["concept"]} context={f["context"]}' for f in selected)}
    path = ROOT / "data/snapshots/statement_supplements.json"
    path.write_text(json.dumps(output, indent=2) + "\n")
    print(f"{len(output)} issuers; {sum(len(x['items']) for x in output.values())} sourced items")


if __name__ == "__main__":
    main()
