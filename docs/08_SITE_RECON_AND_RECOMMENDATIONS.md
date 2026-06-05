# Site Recon & Recommendations — Denver Streets Partnership (consolidated)

**Status: RECON.** This is findings + recommended changes across WordPress *and*
Google Analytics, pulled into one place. **Nothing on the site has been changed.**

Goal: fix denverstreetspartnership.org. Step 1 is knowing the current state — that's
this document. Execution happens only after sign-off on specific items.

Sources consolidated here: the May-22 audit (`denver-streets-audit.md`), the GA4
baseline (`analytics/ga-exports/2026-05-06_to_2026-06-02/`), a live homepage
re-check (2026-06-03), and `docs/07_WORDPRESS_RECOMMENDATIONS.md`.

---

## Part 1 — What we found (recon)

### A. Traffic & behavior (GA4, 28-day baseline)
*Verified from CSV exports, 2026-05-06 → 06-02.*

- **~2,450 sessions/mo.** Channels: **Direct 55%** (1,352), Organic Search 33% (821, best engagement), Referral 184, Organic Social 62, **Email 12**, Unassigned 18.
- **Devices: 63% desktop, 35% mobile, ~1% tablet.**
- **Conversions configured: zero.** Every report shows 0 key events — GA can't currently attribute *any* outcome (donation, signup, volunteer).
- **But enhanced measurement is on** and already collecting a partial funnel: `form_submit` 14, `form_start` 98, `scroll` 906, `click` 377, `file_download` 38. These exist; they're just not flagged as conversions.
- **Top pages:** `/` (632 views), **`/colorado-brt-comment-guide/` (444, 56s avg)** — a comment/action guide and the clear standout — `/what-we-do/colorado-boulevard/` (357), `/about/` (217), `/get-involved/contact/` (134).
- **Donate is weak:** `/donate/` 49 views @ **0.8s** engagement + `/donate` 5 — split across two URLs, barely engaged.

### B. Technical state (live homepage re-check 2026-06-03 + audit)
*"Confirmed" = verified on the live site on 2026-06-03. "Audit" = from May-22, not re-verified.*

- **Confirmed:** viewport blocks pinch-zoom (`maximum-scale=1.0, user-scalable=0`).
- **Confirmed:** dead `UA-144848215-2` tag still loading every pageview (no data since 2024-07-01).
- **Confirmed:** GA4 `GT-WFFQB5TW` + GTM `GTM-TZJRKMV` both live and healthy.
- **Confirmed:** donate served at two URLs (`/donate/` and `?form=donate` modal).
- **Confirmed:** footer reads "© 2020".
- **Audit:** broken volunteer link (Mailchimp survey URL that only works in email); WordPress usernames publicly enumerable; XML-RPC open; below-the-fold images not lazy-loaded. (Host firewall already blocks brute-force, so the security items are hygiene, not emergency.)

### C. The through-line
Healthy top-of-funnel (traffic + SEO + one great action page), but the site **can't measure outcomes** (no conversions) and **can't attribute campaigns** (untagged links → 55% Direct hides newsletter/social). The donate path is both the weakest engagement surface and the least measurable.

---

## Part 2 — Recommended changes (prioritized, both domains)

Ordered by impact × low-risk-fast. **Status** flags what each needs before it can happen.

| # | Change | Domain | Why | Effort | Risk | Status / blocker |
|---|---|---|---|---|---|---|
| 1 | Fix mobile pinch-zoom viewport | WP | 35% mobile; accessibility (WCAG) fail | Low | Very low | Needs **group sign-off** |
| 2 | Remove dead UA tag | WP | Wasted request every pageview | Low | Very low | Group sign-off |
| 3 | Footer year (auto) | WP | "© 2020" reads abandoned | Low | Very low | Group sign-off |
| 4 | Tag newsletter + social links | GA/process | Recover the 55% Direct into real attribution | Low | None | **Ready now** — Mailchimp setting + the tagger (`honnecke.us/utm.html`); no access needed |
| 5 | Mark `form_submit` (+donate) as conversions | GA | First-ever outcome measurement; data already collected | Low | Low | Needs **GA admin grant** *or* skip — see note |
| 6 | Donate → single canonical `/donate/` URL | WP | Splits traffic now; 0.8s engagement; un-measurable | Med | **Med (revenue path)** | Group sign-off + extra testing |
| 7 | Fix broken volunteer link | WP | Currently dead-ends a stated goal | Low | Low | Group sign-off |
| 8 | Security hygiene (user-enum, XML-RPC) | WP | Usernames exposed; unused entry point | Low | Low | Group sign-off (not urgent) |
| 9 | Replicate the BRT comment-guide format; surface blog on homepage | Content | Repeat the one page that demonstrably works | High | Low | Team content decision |

**Note on #5 (GA conversions):** marking events as conversions requires a GA Administrator action we haven't been able to complete (the granted role isn't Administrator, and a programmatic workaround is blocked by Google's OAuth policy — both verified, not assumed). This is **optional**: the baseline and any future analysis work fine via manual CSV export, which needs no grant. Pursue the admin grant only if re-runnable automation becomes worth one round-trip.

---

## Part 3 — Where things actually stand

- **Done:** GA baseline captured; link-tagger built + hosted; WP recommendations written, PDF'd, and distributed to the team.
- **Waiting on the team:** sign-off on which WP items (1–3, 6–8) to execute.
- **Waiting on no one:** item 4 (link tagging) is ready; GA analysis continues via manual export.
- **Parked by choice:** GA programmatic access and conversion-marking (need an admin action; not worth chasing now).

When items get approved, execution rule stands: **child theme, full backup first, one at a time, verified on mobile + desktop, every change reversible.**
