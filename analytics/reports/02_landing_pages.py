#!/usr/bin/env python3
"""Report 2 — top landing pages by sessions + engagement + conversions.

Tells us which articles do top-of-funnel work and which pages people land on
then leave. Staff traffic excluded. See audit §4 item 2.

Run:
    python analytics/reports/02_landing_pages.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ga_client import print_table, run_report  # noqa: E402


def main() -> None:
    response = run_report(
        dimensions=["landingPagePlusQueryString"],
        metrics=["sessions", "engagementRate", "conversions"],
        start_date="28daysAgo",
        end_date="yesterday",
        limit=20,
        exclude_internal=True,  # drop DSP staff (traffic_type=internal)
    )
    print_table(response)


if __name__ == "__main__":
    main()
