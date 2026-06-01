---
doc_id: 04_SUCCESS_METRICS
title: Success Metrics Framework
date: 2026-05-06
relates_to:
  - 02_GOALS.md
  - 03_SITE_AUDIT.md
baseline_source: |
  Quarterly_Engagement_Tracking-Sheet1.csv (Q1 2026, as of 4/07/26).
  Site-side metrics (GA, Search Console) are not currently available;
  recommended instrumentation is part of this framework.
---

# Success Metrics Framework

Six metric categories, each with: definition, current baseline (where known),
target, and which goals (G1-G10) the category serves. All targets are
12-month targets unless noted.

Set up tooling first (see `Instrumentation Stack` at the bottom). Without
it, most of these are unmeasurable.

---

## 1. Acquisition

**What it measures:** How people find the site.

| Metric | Baseline | 12-mo Target | Serves |
|---|---|---|---|
| Total monthly site visits | unknown | establish baseline + 25% | G1, G9 |
| Organic search % of traffic | unknown | ≥40% | G9 |
| Top 20 keyword rankings | unknown | ≥10 in top-3 SERP positions | G9 |
| Referrers from press citations | unknown | ≥5 distinct outlets/quarter | G7 |
| Direct traffic share | unknown | establish baseline | G1 |
| Social referral share | unknown | ≥10% | G1 |

**Target keyword set (suggested):**
"speed limit Denver," "sidewalk repair Denver," "Denver bike infrastructure,"
"Colfax BRT," "Vision Zero Denver," "report dangerous intersection Denver,"
"Twenty is Plenty Denver," "Denver transportation funding," "fix my street
Denver," "[corridor] Denver" for each main corridor.

---

## 2. Engagement

**What it measures:** Whether people actually read/use what they find.

| Metric | Baseline | 12-mo Target | Serves |
|---|---|---|---|
| Pages per session | unknown | ≥2.5 | G1, G5 |
| Avg session duration | unknown | ≥1:30 | G5 |
| Scroll depth on campaign pages | unknown | ≥60% reach "what success looks like" | G2, G4 |
| Blog readthrough rate | unknown | ≥40% finish a post | G5, G9 |
| Returning visitor rate | unknown | ≥30% | G1, G2 |
| Resource library searches/mo | n/a (not built) | ≥200 | G3, G7, G8 |
| Fix My Street Guide completions | unknown | ≥50/mo | G6 |

---

## 3. Conversion

**What it measures:** People taking the action they came to take.

### Email / newsletter

| Metric | Baseline (Q1 2026) | 12-mo Target | Serves |
|---|---|---|---|
| New newsletter signups / quarter | 312 net growth | ≥500 net growth/qtr | G2, G3 |
| % new signups selecting ≥1 topic | 0% (not offered) | ≥70% | G3 |
| Newsletter avg open rate | 26.8% | ≥30% (vs civic benchmark 28%) | G2 |
| Newsletter avg click rate | 1.7% | ≥2.5% | G2 |
| Unsubscribe rate | 0.3% (per Mailchimp insight) | hold ≤0.4% | G2 |

### Advocacy actions (Muster)

| Metric | Baseline (Q1 2026) | 12-mo Target | Serves |
|---|---|---|---|
| Total advocacy actions taken / quarter | 443 | ≥600 | G2 |
| Avg emails sent per action | 111 | ≥150 | G2 |
| Customization rate | 53.7% | ≥60% | G2 |
| Advocacy email open rate | 20.1% | ≥25% | G2 |
| Advocacy email click rate | 1.5% | ≥2.0% | G2 |

### Donations (FundraiseUp)

| Metric | Baseline | 12-mo Target | Serves |
|---|---|---|---|
| Donations / quarter | unknown | establish baseline + 20% | G2, G4 |
| Recurring donor count | unknown | establish baseline + 30% | G2, G4 |
| Donor retention year-over-year | unknown | ≥60% | G2, G4 |
| Avg gift size | unknown | establish baseline | G4 |
| Donate page → completed gift conversion | unknown | ≥35% | G2 |

### Volunteer & Congress

| Metric | Baseline | 12-mo Target | Serves |
|---|---|---|---|
| Volunteer signups / quarter | unknown | establish baseline | G2 |
| Active volunteers (acted in 90d) | unknown | establish baseline | G2 |
| Denver Streets Congress applications/qtr | unknown | establish baseline | G2 |
| Action-team join rate from campaign pages | unknown | ≥3% of campaign visitors | G2 |

---

## 4. Retention & Supporter Lifecycle

**What it measures:** Whether engaged supporters stay engaged and progress
between profiles.

| Metric | Baseline | 12-mo Target | Serves |
|---|---|---|---|
| Email subscribers retained 12mo | unknown | ≥75% | G3 |
| % subscribers who took ≥1 action in 12mo | unknown | ≥40% | G2 |
| % action-takers who became donors | unknown | establish baseline | G4, G8 |
| % donors who took ≥1 action | unknown | establish baseline | G4, G8 |
| Avg topics per subscriber | 0 (not implemented) | ≥1.8 | G3 |
| Profile-progression rate (P1 → P2 → P4) | not measurable today | requires unified ID (G8) | G8 |

The last row is the strategic metric. Profile progression requires
unified supporter identity — see `06_ARCHITECTURE.md`.

---

## 5. Authority & Reach

**What it measures:** Whether DSP is the trusted source on Denver streets.

| Metric | Baseline | 12-mo Target | Serves |
|---|---|---|---|
| Unique press citations / quarter | unknown | ≥15 | G7 |
| Backlinks from .gov / .edu | unknown | ≥10 | G7, G9 |
| Backlinks from local media | unknown | ≥30 | G7, G9 |
| Resource library citations (academic) | unknown | establish baseline | G7 |
| Social follower growth (each platform) | unknown | ≥15% YoY | G1 |
| Press kit downloads / quarter | n/a (not built) | ≥30 | G7 |
| Speaker/panel requests via site | unknown | establish baseline | G7 |

---

## 6. Operational Health

**What it measures:** The site itself is healthy.

| Metric | Baseline | 12-mo Target | Serves |
|---|---|---|---|
| Pages 404'ing in sitemap | several (audit) | 0 | G9 |
| Orphan / test pages indexed | several (audit) | 0 | G9 |
| Mobile Lighthouse Performance | unknown | ≥85 | G10 |
| Mobile Lighthouse Accessibility | unknown | 100 | G10 |
| LCP (largest contentful paint) | unknown | ≤2.5s p75 mobile | G10 |
| INP (interaction to next paint) | unknown | ≤200ms p75 | G10 |
| Uptime | unknown | ≥99.9% | G2 |
| WordPress core/plugin currency | unknown | 0 critical CVEs unpatched >7d | G10 |
| Broken outbound links | unknown | <1% of total | G9 |
| Form submission success rate | unknown | ≥99% | G2 |

---

## Reporting Cadence

- **Weekly (Slack/email digest):** new signups, advocacy actions taken,
  donations.
- **Monthly (1-page exec):** all conversion metrics + top-3 acquisition
  trends.
- **Quarterly (board-facing):** full dashboard, overlaid with the existing
  CSV format. Maintain the current CSV-style reporting; layer site-side
  metrics on top.
- **Annually:** retention cohort analysis, profile-progression analysis,
  goal review.

---

## Instrumentation Stack

Constraint: **no new SaaS spend.** Free tools and free tiers only.
Required to make this framework measurable:

1. **Web analytics: GA4 (free).** Access is incoming. Once active, set up
   conversion events for every CTA listed under G2 in `02_GOALS.md`.
   Backfill the "unknown" baseline rows above on first review.
2. **Search Console (free):** verify domain ownership; set up keyword and
   page-performance reports. Recommend doing this alongside GA setup.
3. **Heatmap / session replay (optional):** Microsoft Clarity (free, no
   sampling cap, includes session replay) is the recommended choice.
   Useful for one-time UX audits and form drop-off analysis.
4. **A11y / performance monitoring:** Lighthouse CI or Pa11y CI in
   GitHub Actions (free), scheduled weekly against the top 20 URLs.
5. **Uptime:** UptimeRobot free tier (50 monitors, 5-min interval) is
   sufficient.
6. **Mailchimp:** already in place. Continue current CSV reporting; add
   topic-group breakdown once G3 is implemented.
7. **Muster:** continue using built-in metrics. Stream events into the
   custom backend (see `06_ARCHITECTURE.md`) for cross-platform analysis.
8. **FundraiseUp:** export donations to the custom backend for unified
   supporter view.
9. **Custom backend dashboards:** Metabase (free OSS) or Grafana (free
   OSS) pointed at the backend Postgres. Self-hosted on the same VM as
   the backend service.

---

## What Not to Measure (At First)

- **Vanity metrics:** raw social impressions, raw page views without
  context, "engagement rate" averaged across all content.
- **Time-on-page on resources:** people downloading PDFs and leaving is
  success, not failure.
- **Bounce rate on the homepage:** if a Curious Newcomer reads the mission
  and bounces having decided "yes I support this," that's a win — pair
  bounce with subscribe rate before drawing conclusions.
