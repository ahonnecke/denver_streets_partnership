#!/usr/bin/env python3
"""Report 3 — source/medium -> landing page -> conversions.

Tells us where traffic comes from and what each channel converts at. Staff
traffic excluded. See audit §4 item 3.

Run:
    python analytics/reports/03_source_medium.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ga_client import print_table, run_report  # noqa: E402


def main() -> None:
    response = run_report(
        dimensions=["sessionSourceMedium", "landingPagePlusQueryString"],
        metrics=["sessions", "conversions"],
        start_date="28daysAgo",
        end_date="yesterday",
        limit=50,
        exclude_internal=True,  # drop DSP staff (traffic_type=internal)
    )
    print_table(response)


if __name__ == "__main__":
    main()
