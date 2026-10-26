"""Vercel entrypoint for the existing same-origin Bellwether JSON API."""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import yfinance as yf

from policyshock.config import CACHE_DIR
from policyshock.data.live import service
from policyshock.ui.api import Handler

yf.set_tz_cache_location(str(CACHE_DIR / "yfinance"))
# Vercel may freeze an instance immediately after the response. Refresh work is
# joined within requests; importing the function never starts network workers.
service.active = True
service.request_driven = True


class handler(Handler):
    """Reuse the validated local HTTP contract without starting a listening server."""

