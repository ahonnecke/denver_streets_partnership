# DSP analytics

Versioned, re-runnable GA4 Data API queries for denverstreetspartnership.org,
**with DSP staff traffic excluded**. See `denver-streets-audit.md` §2d-quater
and §4.

GA4 property: `GT-WFFQB5TW` (via Site Kit) · GTM container: `GTM-TZJRKMV`.

## Status: stubs — not yet runnable

Blocked on two things, both noted inline:
1. **Property ID** — the 9-digit number from the GA owner (Jill). The email
   requesting Viewer access for the service account is in the audit doc.
2. **`traffic_type` custom dimension** registered in GA4 (step 3 below) — the
   report scripts filter on `customEvent:traffic_type`, which errors until the
   dimension exists.

## Excluding staff (internal) traffic — the mechanism

Two parts; the filter alone does nothing, you must also tag the traffic.

1. **Tag staff hits** — `analytics/wp-functions-snippet.php` pushes
   `traffic_type=internal` to the dataLayer for logged-in WP users (DSP staff),
   `external` for everyone else.
2. **Forward to GA4 via GTM** — Data Layer Variable `dlv.traffic_type` →
   GA4 tag field `traffic_type = {{dlv.traffic_type}}`.
3. **Register the custom dimension** — GA4 → Admin → Custom definitions →
   Create custom dimension → event-scoped, parameter name `traffic_type`.
4. **Activate the data filter** — GA4 → Admin → Data Settings → Data Filters →
   Internal Traffic → **Testing** first, verify, then **Active**.

The Python scripts also exclude `traffic_type=internal` at query time
(`ga_client.exclude_internal_filter`) — redundant once the data filter is
Active, but it's the verification path while the filter is in Testing.

Tag by **login**, not IP: DSP staff are remote/dynamic-IP, so IP rules miss them.

## Setup

```bash
cd analytics
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
export GOOGLE_APPLICATION_CREDENTIALS=~/.config/dsp/ga-key.json   # mode 0600
export GA4_PROPERTY_ID=<9-digit number from owner>

python reports/01_overview.py        # sessions / users / engagement / conversions
python reports/02_landing_pages.py   # top 20 landing pages
python reports/03_source_medium.py   # source/medium -> landing page -> conversions
```

## Files

| File | Purpose |
|---|---|
| `wp-functions-snippet.php` | WP snippet — tag logged-in staff as internal |
| `ga_client.py` | Shared client + `exclude_internal` filter (single source of truth) |
| `reports/01_overview.py` | Top-level health numbers |
| `reports/02_landing_pages.py` | Landing-page performance |
| `reports/03_source_medium.py` | Acquisition → conversion |

The service-account key is **never** committed (`.gitignore` blocks `*.json`).
Lives at `~/.config/dsp/ga-key.json`, mode 0600.
