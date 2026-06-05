"""Shared GA4 Data API client + helpers for DSP analytics scripts.

Auth + property come from the environment (see analytics/README.md):
    GOOGLE_APPLICATION_CREDENTIALS=~/.config/dsp/ga-key.json
    GA4_PROPERTY_ID=<9-digit number from the GA owner>

All report scripts import run_report() from here so the "exclude staff
(internal) traffic" behaviour is defined in exactly one place.
"""

from __future__ import annotations

import os
import sys

from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Filter,
    FilterExpression,
    Metric,
    RunReportRequest,
)

# Event parameter set by analytics/wp-functions-snippet.php + GTM, and
# registered as an event-scoped custom dimension in GA4. Referenced in the
# Data API as `customEvent:<parameter_name>`.
INTERNAL_TRAFFIC_DIMENSION = "customEvent:traffic_type"
INTERNAL_TRAFFIC_VALUE = "internal"


def _property_path() -> str:
    property_id = os.environ.get("GA4_PROPERTY_ID")
    if not property_id:
        sys.exit(
            "GA4_PROPERTY_ID is not set. Export the 9-digit property ID from "
            "the GA owner, e.g.  export GA4_PROPERTY_ID=123456789"
        )
    return f"properties/{property_id}"


def exclude_internal_filter() -> FilterExpression:
    """Dimension filter that drops events tagged traffic_type=internal.

    Belt-and-suspenders: once GA4's Internal Traffic data filter is *Active*,
    internal hits are already gone at collection time and this is redundant.
    While that filter is in *Testing* (data still collected), this is how the
    report scripts verify staff traffic is being excluded.

    Requires `traffic_type` to be registered as a custom dimension in GA4,
    otherwise customEvent:traffic_type is unknown and the API errors.
    """
    return FilterExpression(
        not_expression=FilterExpression(
            filter=Filter(
                field_name=INTERNAL_TRAFFIC_DIMENSION,
                string_filter=Filter.StringFilter(value=INTERNAL_TRAFFIC_VALUE),
            )
        )
    )


def run_report(
    *,
    dimensions: list[str],
    metrics: list[str],
    start_date: str = "28daysAgo",
    end_date: str = "yesterday",
    limit: int = 25,
    exclude_internal: bool = False,  # requires the traffic_type custom dimension; off until it's registered in GA4
):
    """Run a single GA4 runReport call, excluding staff traffic by default.

    Returns the raw RunReportResponse; callers format it.
    """
    client = BetaAnalyticsDataClient()
    request = RunReportRequest(
        property=_property_path(),
        date_ranges=[DateRange(start_date=start_date, end_date=end_date)],
        dimensions=[Dimension(name=d) for d in dimensions],
        metrics=[Metric(name=m) for m in metrics],
        dimension_filter=exclude_internal_filter() if exclude_internal else None,
        limit=limit,
    )
    return client.run_report(request)


def print_table(response) -> None:
    """Minimal tab-separated dump of a RunReportResponse to stdout."""
    headers = [h.name for h in response.dimension_headers] + [
        h.name for h in response.metric_headers
    ]
    print("\t".join(headers))
    for row in response.rows:
        cells = [v.value for v in row.dimension_values] + [
            v.value for v in row.metric_values
        ]
        print("\t".join(cells))
    if not response.rows:
        print("(no rows — check property ID, date range, and custom dimension)")
