# GA4 baseline snapshot — 2026-05-06 → 2026-06-02 (28 days)

**Property:** Denver Streets Partnership (GA4 `GT-WFFQB5TW`).
**Source:** manual CSV exports from the GA4 UI (no programmatic access yet — see repo `analytics/` + memory `ga-access-state`).
**Why this exists:** first real baseline for the "unknown" rows in `docs/04_SUCCESS_METRICS.md`. Recommendations were hypothesis-driven until now; these are the numbers.

## Files
| File | GA4 report |
|---|---|
| `traffic-acquisition_channel-group.csv` | Acquisition → Traffic acquisition (channel) |
| `pages-and-screens.csv` | Engagement → Pages and screens |
| `landing-pages.csv` | Engagement → Landing page |
| `events.csv` | Engagement → Events |
| `tech-overview.csv` | Tech overview (device/OS/browser) |

## Baseline numbers (28 days)

**Traffic — ~2,450 sessions.** Channels: Direct **1,352 (55%)**, Organic Search **821 (33%, best engagement** 0.61 rate / 45s), Referral 184, Organic Social 62, **Email 12**, Unassigned 18.
→ The 55% Direct is *inflated by untagged email/social* collapsing into it. Real newsletter/social impact is hidden here — this is the evidence for link tagging.

**Events — enhanced measurement is ON and already capturing a partial funnel:** `page_view` 3,558 · `scroll` 906 · `click` 377 · `form_start` 98 · `file_download` 38 · **`form_submit` 14**.
→ Forms are already tracked automatically. **But "Key events" (conversions) = 0 on every report — nothing is *marked* as a conversion.** The data exists; it's just not designated. Marking `form_submit` (and a donate event) as key events is the cheapest next win.

**Top pages (views):** `/` 632 · **`/colorado-brt-comment-guide/` 444 (56s avg — a CTA/comment guide that works)** · `/what-we-do/colorado-boulevard/` 357 · `/about/` 217 · `/get-involved/contact/` 134 · `/events/` 128. Donate: `/donate/` 49 @ **0.8s** + `/donate` 5 — dual URL, modal/query-param problem from the audit.

**Top landing pages (sessions):** `/` 487 · `/colorado-brt-comment-guide` 375 · `/what-we-do/colorado-boulevard` 244 · `(not set)` 163 · `/events` 98. `/donate` as a landing page: 33 sessions @ 2.9s (bounces).

**Devices:** desktop **1,150 (63%)** · mobile **646 (35%)** · tablet 25. OS: Windows 796, iOS 484, Mac 274, Android 187.
→ 35% mobile makes the audit's mobile zoom/viewport fix matter.

## Adding future snapshots
New export set → new sibling folder named by its date range (`YYYY-MM-DD_to_YYYY-MM-DD/`). Keep each window self-contained so trends are comparable.
