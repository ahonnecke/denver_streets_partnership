# Project Narrative — DSP Website Engagement

Living log of the Denver Streets Partnership website work: what's been done, where
things stand, and what's next. Current status at top; chronological log at the bottom.

*Last updated: 2026-06-05*

---

## The ask

Jill: *"How do we fix the website?"* → *"Let's look in GA first."*
Working goal: **make the website work, and make its performance measurable.** Staff
(Jill, Adrienne) are non-technical. The `denver_streets_partnership` repo is the
planning/analytics workspace — not the website's code (the site is WordPress + Divi).

## Where things stand

**Done**
- First **GA4 baseline** captured and committed → `analytics/ga-exports/2026-05-06_to_2026-06-02/`.
- **UTM link-tagger** built and hosted → `honnecke.us/utm.html`. Email-vs-social tagging decided.
- **WordPress Recommendations report** written, exported to PDF (`docs/exports/`), and **distributed to the team**.

**Unblocked**
- **GA4 Admin granted to Ashton.** Clears the biggest dependency — conversion setup and programmatic access are now self-serve.

**Pending on others**
- Group **sign-off** on which WordPress fixes to do (report is out).

## Next steps

**Google Analytics — do now (Admin granted):**
1. **Mark conversions.** Flag `form_submit` (14/mo, already being collected) and a donate action as **key events** (GA4 Admin → Key events). This is the first time GA can attribute outcomes — the core gap.
2. ~~Enable programmatic access.~~ **DONE** — service account granted Viewer; property ID `453687299`; all three `analytics/reports/*.py` pull live data (`source analytics/env.sh && .venv/bin/python analytics/reports/01_overview.py`).
3. **Stand up CTA conversion events** (donate, newsletter, volunteer, congress) per G2 in `02_GOALS.md` — via GTM.
4. **Backfill** the "unknown" baseline rows in `04_SUCCESS_METRICS.md` from the snapshot.

**Attribution / tracking links:**
5. Turn **on** Mailchimp's GA link tracking (email); hand Adrienne/Jill the tagger for **social**. Use the same `utm_campaign` name across both so GA groups them.

**WordPress — on group approval only (no edits without sign-off):**
6. Execute approved items in a **child theme**, backed up, one at a time: viewport → donate single-URL (careful, revenue path) → volunteer link → remove dead UA → footer year → security hygiene. See `docs/07_WORDPRESS_RECOMMENDATIONS.md`.

**Growth — team content decision:**
7. Replicate the `/colorado-brt-comment-guide/` action-guide format (the top page); surface latest articles on the homepage.

---

## Log (in order)

1. **Looked at GA.** Got UI access; captured the first GA4 baseline (5 CSV exports → `analytics/ga-exports/`). Findings: ~2,450 sessions/mo; **55% Direct** (inflated by untagged email/social); Organic Search 33% with best engagement; **35% mobile**; donate is the weak point (dual URL, 0.8s engagement); `/colorado-brt-comment-guide/` is the standout page (444 views, 56s); **enhanced measurement is on** (`form_submit` already firing) but **zero conversions configured**. Corrected an earlier overstatement: GA's traffic data *is* usable — what's missing is *configured conversions* and *campaign attribution*, not a broken GA.
2. **Built attribution tooling.** Hosted the UTM link-tagger (`analytics/tracking-links/link-builder.html` → `honnecke.us/utm.html`). Decision: **Mailchimp's built-in GA tracking for email, the tagger for social** (don't double-tag).
3. **Got WordPress access.** Re-verified the audit findings on the live homepage (viewport blocks zoom, dead UA loading, `?form=donate` dual URL, footer © 2020). Wrote `docs/07_WORDPRESS_RECOMMENDATIONS.md` — proposal only, no site changes; all fixes reversible, child-theme, one at a time.
4. **Distributed the WP report** to the team (email + Slack; PDF + blurb). Asked Jill for GA Admin.
5. **GA4 Admin granted.** Conversion config + programmatic access now self-serve → see Next steps.
6. **Programmatic read-only access working.** Service account added as Viewer; property `453687299`; the report scripts pull live data — manual CSV export no longer required. (gmail-OAuth route abandoned: Google blocks the shared gcloud client from the analytics scope on consumer accounts.)

## Context
- Trackers on site: GA4 `GT-WFFQB5TW` + GTM `GTM-TZJRKMV` (both live), dead `UA-144848215-2` (remove).
- Baseline data window: **2026-05-06 → 06-02** — the one date that's load-bearing here (it's the period the numbers describe).
- Hosting for the tagger: the honnecke.us Linode (`/home/ahonnecke/www/honnecke/`); `pixelstub.com` is Cloudflare elsewhere — don't deploy there.

---

## Artifacts
- GA baseline: `analytics/ga-exports/2026-05-06_to_2026-06-02/` (+ its README)
- Link tagger: `analytics/tracking-links/` (live: `honnecke.us/utm.html`)
- WP report: `docs/07_WORDPRESS_RECOMMENDATIONS.md` + `docs/exports/` (PDF, blurb)
- Stubbed GA API scripts: `analytics/` (blocked until step 2 above)
