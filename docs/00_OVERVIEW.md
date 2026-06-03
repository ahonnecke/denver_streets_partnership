---
doc_id: 00_OVERVIEW
title: DSP Website Evaluation — Overview & Index
audience: DSP staff, board, web vendor
date: 2026-05-06
status: draft
source_inputs:
  - Quarterly_Engagement_Tracking-Sheet1.csv (Q1 2026 email/advocacy metrics)
  - Live audit of denverstreetspartnership.org (homepage, sitemap, key sections)
  - Priority Purposes draft dated May 5, 2026
---

# Overview

This evaluation answers four questions for the Denver Streets Partnership (DSP)
website at `denverstreetspartnership.org`:

1. **Who is the site for?** — distinct user profiles with jobs-to-be-done.
2. **What should the site achieve?** — measurable goals tied to those profiles.
3. **How well does the current site perform?** — audit against the goals.
4. **What should change?** — recommendations sequenced by impact × effort,
   plus a target architecture (WordPress retained for content, with a heavier
   custom backend for supporter identity, integrations, and personalization).

## Document Index

| File | Purpose |
|---|---|
| `01_USER_PROFILES.md` | Nine distinct user profiles with jobs-to-be-done and primary CTAs |
| `02_GOALS.md` | Ten measurable goals derived from priority purposes + profiles |
| `03_SITE_AUDIT.md` | Findings from live audit, mapped to goals; what works, what doesn't |
| `04_SUCCESS_METRICS.md` | KPI framework: acquisition, engagement, conversion, retention, authority, operational |
| `05_RECOMMENDATIONS.md` | Prioritized improvements: quick wins, medium-term, strategic |
| `06_ARCHITECTURE.md` | Target architecture: WP-as-CMS + custom backend for identity/integrations |

## TL;DR

**What works**

- Clear mission framing ("Streets are for people"; human dignity as guiding principle).
- Strong individual campaign template (Colorado Blvd: tiered CTAs, crash data,
  "What success looks like" section).
- Solid email program: 8,343 subscribers, 27% newsletter open rate
  (just under 28% civic benchmark), 443 advocacy actions in Q1 2026.
- WordPress sitemap is healthy and indexable (~73 pages, 247 projects).

**What doesn't**

- `/our-impact/` page is qualitative-only — no quantified wins, no year-over-year,
  no campaign archive of outcomes. The org's track record is its strongest
  acquisition/donation asset and it is not on the site.
- Email signup captures address but not topic interest. The CSV's own AI
  insight calls out that segmented sends to topic-engaged supporters get
  2-3× engagement; the site is not feeding that segmentation.
- Resources page is a flat list of 115 items with no search, filter, or
  topic taxonomy — unusable for journalists or researchers.
- Information architecture has drift: nav implies `/policy/` and `/place/`
  but those 404; actual paths are `/what-we-do/[name]`. Orphan/test pages
  (`test-full-width`, `test-filter-page`, `sidewalksold`, multiple empty
  `event-N` stubs) are in the live sitemap.
- No press kit, no per-topic subscribe, no supporter "what I've done" view,
  no central event calendar that's not stub data.
- Integrations are siloed: Mailchimp, Muster, FundraiseUp, plus ad-hoc
  Google Drive/Forms — no shared supporter identity across them.

**What's recommended (sequenced)**

- **Now (weeks):** clean orphan pages; add topic-interest groups to Mailchimp
  signup; build a real Impact page with quantified wins; ship a press kit;
  add search/filter to Resources.
- **Next quarter:** topic taxonomy across blog/projects/resources with per-topic
  subscribe; standardize campaign-page template; embed Muster actions inline
  rather than offsite hand-off.
- **Next year:** add a custom backend service alongside WordPress that owns
  supporter identity and stitches Mailchimp/Muster/FundraiseUp/Congress data
  into one supporter record. WordPress stays as the content CMS; the backend
  serves personalized widgets and powers a supporter portal.

See `05_RECOMMENDATIONS.md` and `06_ARCHITECTURE.md` for detail.

## Constraints

- **No new SaaS spend.** Recommendations stick to existing platforms
  (Mailchimp, Muster, FundraiseUp), free/free-tier tools, and self-hosted
  software. The turnkey-nonprofit-CRM fork in `06_ARCHITECTURE.md` is
  ruled out by this constraint; only the build path is live.
- WordPress stays. Migration is out of scope.

## Caveats

- **Google Analytics — UI access obtained; first baseline captured 2026-06-03.**
  Real numbers now live in
  `analytics/ga-exports/2026-05-06_to_2026-06-02/` (see its `README.md`).
  Traffic / landing / page / device baselines are no longer
  hypothesis-driven. Still pending: programmatic (API) access, and any
  *configured conversions* — zero exist today, so outcome/conversion rows
  in `04_SUCCESS_METRICS.md` stay "unknown" until conversion events are set up.
- Search Console access status: TBD. Recommend setting up alongside GA.
- The audit was a content/IA/integration review, not a code or accessibility
  audit. A WCAG 2.2 AA conformance pass is recommended as a follow-up
  (see `05_RECOMMENDATIONS.md`, R13).
- Email engagement data is from `Quarterly_Engagement_Tracking-Sheet1.csv`
  Q1 2026 (as of 4/07/26). Site-side engagement data lands when GA does.
