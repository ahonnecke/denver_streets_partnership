#!/usr/bin/env python3
"""Deterministic GA access check — no GA UI involved.

Asks the GA4 Admin API which accounts/properties the *current credentials* can
read, and prints the Property ID. Uses, in order:

  1. a service-account key, if GOOGLE_APPLICATION_CREDENTIALS points at one, else
  2. your own Google login (application-default credentials) — i.e. your gmail.

So to check what YOUR gmail can see, run it with GOOGLE_APPLICATION_CREDENTIALS
unset, after:
  gcloud auth application-default login \
    --scopes=https://www.googleapis.com/auth/analytics.readonly,https://www.googleapis.com/auth/cloud-platform
"""
import os

import google.auth
from google.oauth2 import service_account
from google.analytics.admin import AnalyticsAdminServiceClient

SCOPES = ["https://www.googleapis.com/auth/analytics.readonly"]


def credentials_and_identity():
    key = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    if key and os.path.exists(key):
        creds = service_account.Credentials.from_service_account_file(key, scopes=SCOPES)
        return creds, f"service account ({creds.service_account_email})"
    creds, _ = google.auth.default(scopes=SCOPES)
    return creds, "your Google login (application-default credentials)"


def main() -> None:
    creds, who = credentials_and_identity()
    print(f"Authenticated as: {who}\n")

    client = AnalyticsAdminServiceClient(credentials=creds)
    summaries = list(client.list_account_summaries())

    if not summaries:
        print("RESULT: this identity can see 0 GA4 properties (no access).")
        return

    print("RESULT: access works. Properties this identity can read:\n")
    for acc in summaries:
        print(f"Account: {acc.display_name}  ({acc.account})")
        for p in acc.property_summaries:
            print(f"  {p.display_name}    PROPERTY ID = {p.property.split('/')[-1]}")
    print("\nPut the Property ID into analytics/env.sh (GA4_PROPERTY_ID=...).")


if __name__ == "__main__":
    main()
