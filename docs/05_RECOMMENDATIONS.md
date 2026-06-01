---
doc_id: 05_RECOMMENDATIONS
title: Recommendations — Sequenced by Impact × Effort
date: 2026-05-06
relates_to:
  - 03_SITE_AUDIT.md
  - 04_SUCCESS_METRICS.md
  - 06_ARCHITECTURE.md
---

# Recommendations

Sequenced into three tiers:

- **Tier 1 — Quick Wins (next ~6 weeks):** content + config changes inside
  WordPress; no architecture work required.
- **Tier 2 — Medium Term (next 1-2 quarters):** template, taxonomy, and
  data-model work; mostly still WordPress, with new plugins or limited
  custom code.
- **Tier 3 — Strategic (next 6-12 months):** introduces the custom backend
  service described in `06_ARCHITECTURE.md`. Enables unified supporter
  identity, supporter portal, and personalization.

Each recommendation has: **what**, **why** (which audit finding / goal),
**effort** (S/M/L), **impact** (S/M/L), **dependencies**.

---

## Tier 1 — Quick Wins

### R1. Clean up sitemap and orphan pages

**What:** Delete or `noindex` the test/orphan pages (`test-full-width`,
`test-filter-page`, `sidewalksold`, empty `event-N` stubs). Set 301
redirects from intuitive-but-404 paths (`/policy/` → `/what-we-do/`,
`/place/` → `/what-we-do/main-streets/`, `/donate/` → current donate URL,
`/news/` → `/blog/`, etc.).

**Why:** G9 (search), site cleanliness signal, IA mismatch finding.

**Effort:** S. **Impact:** M. **Dependencies:** none.

---

### R2. Add topic-interest groups to Mailchimp signup

**What:** Replace the current address-only signup with a form that captures
topic interest groups: Vision Zero, Transit, Sidewalks & Pedestrian Safety,
Bike Infrastructure, Speed Limits / Traffic Calming, Federal Blvd, Colfax,
Colorado Blvd, Other Corridors. Use Mailchimp's native "Groups" feature.
Default behavior: a subscriber with no topic selection still gets the main
newsletter.

**Why:** G3 (per-topic interest). The CSV's own AI insight calls out 2-3×
engagement on topic-segmented sends. The site is the funnel that should
capture this.

**Effort:** S. **Impact:** L. **Dependencies:** none.

---

### R3. Build a real Impact page

**What:** Replace `/our-impact/` with a page that documents quantified
wins, organized by year and by campaign. Each entry: campaign name, year,
outcome, one-line "what this means," link to the campaign page. Ten
priority entries to seed it (from the priority-purposes draft):

- Denver Deserves Sidewalks / Measure 307
- Twenty is Plenty rollout
- Jaywalking decriminalization
- Federal Boulevard tactical urbanism cycles
- Colfax community work / Cloverleaf Oral History
- Bicycling Rewards Program participation
- E-bikes for Deliveries pilot outcomes
- Advocacy Academy graduates
- CU Denver research collaborations
- Coalition member growth

**Why:** G4 (impact). Donor (P4) and Decision-Maker (P9) acquisition lever.

**Effort:** M (research-heavy; pull data from staff). **Impact:** L.
**Dependencies:** none.

---

### R4. Ship a press kit page

**What:** Add `/press/` containing: media contact (named person, email,
phone), executive bios with downloadable headshots, downloadable logo
(SVG + PNG), recent press releases (last 12 months), recent press-ready
quotes by topic, recent press citations.

**Why:** G7 (journalist). Currently a BLOCKER per audit.

**Effort:** S. **Impact:** L. **Dependencies:** none.

---

### R5. Add search + topic filter to Resources page

**What:** Implement Resources page with: full-text search, filter by
topic taxonomy, filter by year, filter by document type. Constraint:
no new SaaS / paid plugins. Free path: **Relevanssi** (free,
open-source) for search relevance, plus native WordPress taxonomy
queries for topic/year/type filters via a small custom template that
reads URL query parameters. If that proves insufficient, escalate to
self-hosted **Meilisearch** or **Typesense** (both free OSS, container-
deployable on the same VM as the backend service from R16).

**Why:** G7 (researcher), G3 (topic). Currently 115 items with no
filtering — unusable.

**Effort:** M. **Impact:** L. **Dependencies:** topic taxonomy (R7).

---

### R6. Surface "Take Action" persistently

**What:** Add a persistent "Take Action" entry point in primary nav (not
buried under "Get Involved"). Include a small badge on every campaign
page showing the current ask.

**Why:** G2 (engagement). The Engaged Advocate (P2) profile is the
highest-conversion segment per the CSV; reduce their click depth.

**Effort:** S. **Impact:** M. **Dependencies:** none.

---

### R7. Define and apply a topic taxonomy

**What:** Create a single canonical topic taxonomy used across blog posts,
projects, resources, and Mailchimp interest groups. Suggested topics:

- Vision Zero / Traffic Safety
- Transit
- Sidewalks & Pedestrian Infrastructure
- Bike & Micromobility
- Transportation Funding
- Speed Limits & Traffic Calming
- Equity & Racial Justice
- Climate & Air Quality
- [Corridor: Federal] [Corridor: Colfax] [Corridor: Colorado] etc.
- [Neighborhood: Montbello] [Neighborhood: Southwest Denver] etc.

Tag historical posts and projects in batches. The taxonomy is the
foundation for R5 (resource filtering), R8 (campaign template), R12
(per-topic landing pages), and R2 (Mailchimp groups).

**Why:** G3, G7, G9. Foundational for several downstream items.

**Effort:** M. **Impact:** L (compounds across other work). **Dependencies:** none.

---

## Tier 2 — Medium Term

### R8. Standardize the campaign-page template

**What:** Codify the Colorado Boulevard page pattern as a reusable
WordPress block / page template. Required sections in order: hero with
one-line problem statement, "By the numbers" data block, "Why this
matters" (educational), "What success looks like," "Where we are now"
(status update), tiered CTAs (low/medium/high), "Join the action team,"
related research / past coverage. Migrate the top 5 existing campaigns
to this template.

**Why:** G1, G2, G4. Audit finding: template exists but is inconsistently
applied.

**Effort:** L. **Impact:** L. **Dependencies:** R7.

---

### R9. Build a "Why" / "Streets 101" content hub

**What:** Add a `/why/` section with five evergreen explainer pages
addressing the five foundational questions:

1. Why reduce car dependency? (with realistic transition framing)
2. Why is highway/road widening counterproductive?
3. How does transit relate to Vision Zero?
4. What does successful transit look like?
5. How does equity intersect with transportation justice?

Each page: 800-1500 words, embedded local data, internal links to
campaign pages, social-shareable visuals. Optimize for the relevant
keyword set (R10).

**Why:** G5. This is also the SEO play (G9): these are the queries
curious residents and journalists actually type.

**Effort:** L (writing-heavy; coordinate with comms staff).
**Impact:** L. **Dependencies:** none.

---

### R10. SEO foundations

**What:**

- Add Schema.org structured data: Organization (root), Article (blog),
  Event (events), NewsArticle (press releases), VideoObject where
  applicable.
- Add OG/Twitter card metadata to every template (likely already partial).
- Audit and rewrite title tags + meta descriptions on top 20 pages
  against the target keyword set in `04_SUCCESS_METRICS.md`.
- Add an `XML-Sitemap` ping on publish (Yoast/RankMath plugin).
- Add proper canonical handling.

**Why:** G9.

**Effort:** M. **Impact:** L. **Dependencies:** R1.

---

### R11. Embed Muster actions inline

**What:** Replace "click out to Muster" links with Muster's embed widget
on the action page and on each campaign page. Goal: action takes <30
seconds without a context switch. Where Muster doesn't fit (e.g., RSVP),
use embedded forms, not Google Forms hand-offs.

**Why:** G2 (frictionless). Audit found Take Action mixes Muster, Google
Forms, and Google Drive PDFs inconsistently.

**Effort:** M. **Impact:** M. **Dependencies:** none.

---

### R12. Per-topic landing pages with their own newsletter feed

**What:** For each major topic in the taxonomy (R7), create a landing
page that aggregates: latest blog posts, current campaigns, past wins,
related research, and a per-topic subscribe button. Wire the subscribe
button to the matching Mailchimp group from R2.

**Why:** G3, G5, G9. Builds topical authority for SEO, gives the
Researcher (P8) and Hyperlocal (P3) profiles a home.

**Effort:** M. **Impact:** L. **Dependencies:** R2, R7.

---

### R13. A11y + performance audit and remediation

**What:** Run Lighthouse and axe-core against the top 20 URLs. Fix
findings. Set up Lighthouse CI to run weekly against the same set with
alerts on regression.

**Why:** G10. Audit caveat: never formally tested; mobile conversion
hypothesis from the CSV suggests room.

**Effort:** M (audit) + L (remediation depending on findings).
**Impact:** M. **Dependencies:** none.

---

### R14. Volunteer signup overhaul

**What:** Replace the single Mailchimp survey with a structured volunteer
intake: time commitment (one-off / weekly / monthly), skill area
(events / data / canvassing / writing / design / Spanish-language
outreach), neighborhood preference, contact preference. Route matches
to the appropriate organizer.

**Why:** G2 (engagement). Audit finding: current volunteer flow is
undifferentiated.

**Effort:** M. **Impact:** M. **Dependencies:** none initially; merges
with backend in R17.

---

### R15. Event calendar that's actually used

**What:** Pick one canonical event surface (likely The Events Calendar
plugin). Migrate event content from campaign-page sub-blocks into
calendar entries with proper structured data (R10). Delete or redirect
the orphan `event-N` stubs.

**Why:** G2 (in-person action), G7 (journalists looking for events),
G9 (event structured data → rich SERP results).

**Effort:** M. **Impact:** M. **Dependencies:** R1.

---

## Tier 3 — Strategic

These items require the backend service in `06_ARCHITECTURE.md`.

### R16. Stand up the custom backend service

**What:** Build the FastAPI/Postgres service described in
`06_ARCHITECTURE.md`. Initial scope: webhook receivers for Mailchimp,
Muster, FundraiseUp; supporter-identity table; tag/event log. Read-only
in v1 — no UI yet, just data unification.

**Why:** G8 (integrations). Foundation for R17-R20.

**Effort:** L. **Impact:** L. **Dependencies:** vendor selection,
hosting decision.

---

### R17. Unified supporter identity & cross-platform reporting

**What:** Resolve supporters across Mailchimp, Muster, FundraiseUp,
Congress applications, and the volunteer database into one canonical
record keyed by email. Backfill historical records. Build cross-platform
reports: "donors who also took an action," "advocates who haven't yet
donated," "Congress members not on the email list."

**Why:** G8. Enables the retention metrics in `04_SUCCESS_METRICS.md`
that are unmeasurable today.

**Effort:** L. **Impact:** L. **Dependencies:** R16.

---

### R18. Supporter portal (passwordless)

**What:** A logged-in (magic-link auth) supporter portal showing:
the actions they've taken, their donation history, their event RSVPs,
their topic interests (editable), their Congress status. Modest: this
is mostly read-only with one form to update topic preferences.

**Why:** G2 (retention), G3. Audit finding: P2 (Engaged Advocate)
has no "what I've done" view today.

**Effort:** L. **Impact:** M. **Dependencies:** R16, R17.

---

### R19. Personalized homepage and campaign widgets

**What:** Inject supporter-state-aware widgets into WordPress pages:
"Welcome back, [first name]. You took 3 actions this year." "Based on
your interest in Vision Zero, here's our current campaign." "You haven't
given since 2024 — want to renew?" Implementation: WordPress requests
a JSON fragment from the backend keyed by a supporter cookie.

**Why:** G1 (current focus tailored to viewer), G2 (right CTA for the
right person), G4 (personalized impact).

**Effort:** L. **Impact:** L. **Dependencies:** R17.

---

### R20. Automated supporter lifecycle journeys

**What:** Backend-triggered automations:

- First gift → "donor" Mailchimp tag → trigger thank-you series.
- 5+ Muster actions → flag for organizer outreach (Congress invite).
- 12 months no engagement → re-engagement series.
- Topic interest declared → first-7-days topic education series.
- Press kit downloaded → log + journalist tag.

**Why:** G2, G3, G8. Drives the retention metrics.

**Effort:** M (per journey). **Impact:** L cumulative.
**Dependencies:** R17.

---

## Sequencing Map

```
Tier 1 (weeks 1-6):
  R1 cleanup ──┐
  R4 press kit ┤
  R6 nav ──────┤
  R3 impact ───┤   (parallel; no deps)
  R2 mc topics ┤
  R7 taxonomy ─┴──────────────┐
                              │
Tier 2 (months 2-6):          ▼
  R5 resources search ◀───────┤
  R8 campaign template ◀──────┤
  R12 topic landings ◀────────┤
  R9 why hub
  R10 SEO ◀── R1
  R11 muster embed
  R13 a11y/perf
  R14 volunteer intake
  R15 events ◀── R1
                              │
Tier 3 (months 6-12):         ▼
  R16 backend ────────┐
  R17 unified ID ◀────┘
  R18 portal ◀── R17
  R19 personalization ◀── R17
  R20 journeys ◀── R17
```

## Vendor / Build vs. Buy Notes

Constraint: **no new SaaS spend.** Existing platforms (Mailchimp, Muster,
FundraiseUp) stay; everything new is free OSS, free-tier, or self-hosted.

- **Stay on WordPress** for content. Migration is high cost / low value.
- **Mailchimp / Muster / FundraiseUp** all have webhook + API support
  sufficient for R16-R20. No need to switch platforms.
- **Custom backend** (R16) is greenfield — small footprint, modern stack.
  See `06_ARCHITECTURE.md`.
- **Search (R5):** Relevanssi (free) for relevance; native WP taxonomy
  queries for filters. Self-hosted Meilisearch or Typesense as escalation
  if needed. SearchWP and FacetWP are paid — ruled out by constraint.
- **SEO plugin (R10):** RankMath free tier or Yoast free tier — both
  cover Schema.org, sitemap, OG tags adequately. No paid upgrade needed.
- **Events (R15):** "The Events Calendar" by StellarWP — free core has
  Schema.org Event support and is sufficient for the use case.
- **A11y monitoring (R13):** Pa11y CI or Lighthouse CI in GitHub Actions;
  free.
- **Accessibility remediation (R13):** budget for a one-time external
  WCAG 2.2 AA audit only if internal capacity is thin. Many local a11y
  contractors offer fixed-fee audits — this is a one-time cost, not a
  recurring SaaS commitment.
- **Analytics (instrumentation):** GA4 free tier; Search Console free;
  Microsoft Clarity free. Not Plausible/Fathom (paid SaaS).
