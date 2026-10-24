from policyshock.narrative import formatting as f
from policyshock.ui.state import decode, encode


def test_roundtrip():
    s = {"m": "industry", "i": "consumer_retail", "p": "import_tariffs", "in": {"tariff_pct": 25}, "a": {"pass_through": [0.3, 0.5, 0.9]}}
    assert decode(encode(s)) == s


def test_bad_token():
    assert decode("not-a-token!!") == {}


def test_formatting():
    assert f.money(1234.5) == "$1.2B"
    assert f.money(-2_300, signed=True) == "−$2.3B"
    assert f.money(12.34) == "$12M"
    assert f.pct(0.021, signed=True) == "+2.1%"
    assert f.pct(-0.0049, signed=True) == "−0.49%"
    assert f.pct(-0.049, signed=True) == "−4.9%"
    assert f.bps(-340.2) == "−340 bps"
    assert f.pct(None) == "n/m"
