"""Read numeric inline-XBRL facts and contexts from public SEC filing HTML.

Companyfacts excludes many company-extension and dimensional facts. This reader
retains the exact concept, context, unit, scale and document URL for audit review;
it does not guess which custom tag represents a financial statement line.
"""

from __future__ import annotations

from html.parser import HTMLParser
import math


class InlineFacts(HTMLParser):
    """Collect numeric facts and dimension-aware contexts without third-party parsers."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.contexts = {}
        self.facts = []
        self._context = None
        self._context_id = None
        self._field = None
        self._text = []
        self._numeric = None
        self._number = []

    def handle_starttag(self, tag, attrs):
        """Record context periods, explicit members and numeric-fact attributes."""
        attrs = dict(attrs)
        local = tag.split(":")[-1]
        if local == "context":
            self._context_id = attrs.get("id")
            self._context = {"dimensions": {}}
        elif self._context is not None and local in ("instant", "startdate", "enddate", "explicitmember", "typedmember"):
            self._field = (local, attrs.get("dimension"))
            self._text = []
        if tag == "ix:nonfraction":
            self._numeric, self._number = attrs, []

    def handle_data(self, text):
        """Retain visible numeric and context text verbatim until each element closes."""
        if self._field:
            self._text.append(text)
        if self._numeric is not None:
            self._number.append(text)

    def handle_endtag(self, tag):
        """Finish a context or finite scaled inline number; skip nil/invalid values."""
        local = tag.split(":")[-1]
        if self._field and local == self._field[0]:
            field, dimension = self._field
            value = "".join(self._text).strip()
            if dimension:
                self._context["dimensions"][dimension] = value
            else:
                self._context[field] = value
            self._field = None
        if local == "context" and self._context is not None:
            self.contexts[self._context_id] = self._context
            self._context = None
        if tag == "ix:nonfraction" and self._numeric is not None:
            attrs = self._numeric
            text = "".join(self._number).replace(",", "").replace("\u00a0", "").strip()
            try:
                value = 0. if text in ("—", "–", "-") else float(text.strip("()"))
                value *= 10 ** int(attrs.get("scale", "0"))
                if attrs.get("sign") == "-" or text.startswith("("):
                    value = -value
                if math.isfinite(value) and not attrs.get("xsi:nil"):
                    self.facts.append({"concept": attrs.get("name"), "context": attrs.get("contextref"),
                                       "unit": attrs.get("unitref"), "value": value})
            except (ValueError, OverflowError):
                pass
            self._numeric = None


def parse_inline(html: str) -> InlineFacts:
    """Parse a filing while preserving numeric source locations and dimensional scope."""
    parser = InlineFacts()
    parser.feed(html)
    return parser
