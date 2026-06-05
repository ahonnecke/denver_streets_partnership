#!/usr/bin/env python3
"""Report 1 — site overview (sessions / users / engagement / conversions).

Top-level health numbers, staff traffic excluded. See audit §4 "What to pull".

Run:
    python analytics/reports/01_overview.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ga_client import print_table, run_report  # noqa: E402


def main() -> None:
    response = run_report(
        dimensions=["date"],
        metrics=[
            "sessions",
            "totalUsers",
            "engagementRate",
            "conversions",
        ],
        start_date="28daysAgo",
        end_date="yesterday",
        limit=60,
        exclude_internal=False,  # staff-exclusion parked: traffic_type custom dimension not registered
    )
    print_table(response)


if __name__ == "__main__":
    main()
