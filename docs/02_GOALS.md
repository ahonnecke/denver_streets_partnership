---
doc_id: 02_GOALS
title: Website Goals
date: 2026-05-06
relates_to:
  - 01_USER_PROFILES.md
  - 03_SITE_AUDIT.md
  - 04_SUCCESS_METRICS.md
notes: |
  Goals are derived by translating each "Priority Purpose" from the May 5 draft
  into a measurable, profile-anchored objective. Each goal lists the profiles
  it serves and links to the metric category that measures it.
---

# Website Goals

Ten goals. Each is intended to be measurable (see `04_SUCCESS_METRICS.md`)
and tied to specific user profiles (see `01_USER_PROFILES.md`).

Goals are ranked by criticality, not order of work. See `05_RECOMMENDATIONS.md`
for execution sequence.

---

## G1 — Establish identity and current focus within 30 seconds

**What:** A first-time visitor must understand (a) what DSP is, (b) what they
do generally, and (c) what they are working on right now — within 30 seconds
of arrival, on any device.

**Serves profiles:** P1 (Newcomer), P3 (Hyperlocal), P9 (Decision-Maker).

**Measured by:** Bounce rate on homepage; scroll-depth to first campaign
section; click-through to a campaign page or subscribe.

**Acceptance test:** Show the homepage to five Denver residents who have
never heard of DSP. After 30 seconds, ≥4 can correctly state the mission
in one sentence and name at least one current campaign.

---

## G2 — Make every engagement mode frictionless and discoverable

**What:** The seven engagement modes (donate, subscribe, online action,
in-person action, volunteer, Denver Streets Congress, topic tracking) must
each be reachable in ≤2 clicks from any page, with clear next-step language.

**Serves profiles:** P2, P3, P4, P5, P6.

**Measured by:** Conversion rate per engagement mode; click-depth from
landing page to conversion; mobile vs. desktop conversion gap.

**Acceptance test:** From a cold visit on mobile, a user can complete a
newsletter signup, a donation, and a Muster action each in ≤90 seconds.

---

## G3 — Enable per-topic interest expression and tracking

**What:** Visitors must be able to declare interest in specific issue areas
(e.g., Vision Zero, transit, sidewalks, a specific corridor) and receive
content scoped to those interests.

**Serves profiles:** P2, P3, P6, P8.

**Measured by:** Percentage of new signups who select ≥1 topic interest;
open and click rates on topic-segmented sends vs. full-list sends; topic
distribution across the subscriber base.

**Why this is high-priority:** The CSV's own Mailchimp AI insight reports
that segmented sends to topic-engaged supporters yield **2-3× higher
engagement** than full-list sends. The site is the funnel that captures
this segmentation; today it does not.

---

## G4 — Document impact with quantified, year-over-year evidence

**What:** Visitors must be able to see specific, dated outcomes from DSP's
work — policy wins, place-based projects, programs, research — across the
organization's history. Generalized "we measure impact in conversations had"
language is insufficient for donors, journalists, and decision-makers.

**Serves profiles:** P4 (Donor), P7 (Journalist), P9 (Decision-Maker), P1
(Newcomer credibility check).

**Measured by:** Existence of a quantified Impact page with year-over-year
data; donor conversion uplift after Impact page redesign; press citations
of DSP impact data.

**Examples to surface:**
- Denver Deserves Sidewalks (Measure 307 victory) — votes, dollars unlocked,
  timeline.
- Twenty is Plenty — number of speed-limit signs installed, corridors
  affected.
- Federal/Colfax/Colorado place-based work — community engagement counts,
  policy outcomes.
- Programs — Bicycling Rewards / E-bikes for Deliveries participation
  numbers; Advocacy Academy graduates.
- Research — CU Denver studies, East Colfax Parking Management study,
  Cloverleaf Oral History.

---

## G5 — Educate on the "why" of the movement

**What:** Visitors must be able to find clear, non-jargon answers to the
foundational questions that support culture change:

- What are the benefits of reducing car dependency? Is it realistic?
- Why is highway/road widening bad?
- How does transit relate to Vision Zero?
- What does successful transit look like?
- How does equity and racial justice intersect with transportation?

**Serves profiles:** P1 (Newcomer), P3 (Hyperlocal turning advocate), P7
(Journalist), P9 (Decision-Maker).

**Measured by:** Existence of evergreen "Why" / "101" content hub; search
traffic landing on educational pages; time on page; outbound clicks to
campaign action from educational pages.

---

## G6 — Equip residents with self-service advocacy tools

**What:** A resident with a specific neighborhood concern must be able to
self-serve: identify their elected officials, find DSP's prior work on
their corridor, and take their first advocacy step without staff
intervention.

**Serves profiles:** P3 (Hyperlocal).

**Measured by:** Fix My Street Guide page views and completions;
geo-segmented signup rate; conversions on neighborhood-specific landing
pages.

---

## G7 — Function as a press and researcher resource

**What:** A journalist on deadline or a researcher on a project must be
able to find: media contact, executive bios with headshots, recent press
releases and quotes, downloadable research, position statements, and
historical letters to officials.

**Serves profiles:** P7 (Journalist), P8 (Researcher).

**Measured by:** Existence of a press kit page; press citation count;
resource library download counts; media inquiry conversion.

---

## G8 — Integrate cleanly with engagement platforms

**What:** Mailchimp (email), Muster (advocacy), FundraiseUp (donations),
and social channels must work as a unified supporter journey, not as
disconnected silos. A supporter who donates should be findable in the
email list with a "donor" tag; a supporter who takes 5 advocacy actions
should be elevated for volunteer or Congress outreach.

**Serves profiles:** All — but this is mostly invisible infrastructure.

**Measured by:** Cross-platform supporter ID coverage; cohort analysis
(donors who also took an action; advocates who also donated); reduction
in duplicate / mismatched supporter records.

**Note:** This goal requires the backend work in `06_ARCHITECTURE.md`.

---

## G9 — Be discoverable via search

**What:** When a Denver resident searches for "speed limit Denver,"
"sidewalk repair Denver," "report dangerous intersection Denver," or
"Colfax BRT," DSP should appear on page 1 of organic results with a
relevant landing page.

**Serves profiles:** P1 (Newcomer), P3 (Hyperlocal), P8 (Researcher).

**Measured by:** Organic search traffic; ranking position on a target
keyword set; click-through rate from SERP; bounce rate on search-landed
pages.

**Current barriers (audit findings):**
- Test/orphan pages in sitemap (`test-full-width`, `test-filter-page`,
  `sidewalksold`, multiple empty `event-N` stubs) dilute crawl budget and
  signal site neglect.
- Navigation references paths (`/policy/`, `/place/`) that 404; actual
  paths use `/what-we-do/[name]`. URL drift hurts both search and IA.
- No structured data (Schema.org Organization, Article, Event) visible
  in the audit.

---

## G10 — Be accessible and performant

**What:** The site must meet WCAG 2.2 AA conformance and load fast on
mobile networks. Per the CSV, 14-15% of email clicks are mobile — a
stable but underperforming segment that may be limited by mobile UX, not
just behavior.

**Serves profiles:** All. P3 (Hyperlocal) and P5 (Volunteer) skew mobile.

**Measured by:** axe-core / Lighthouse accessibility score; LCP, INP,
CLS on key templates; mobile conversion rate vs. desktop.

**Audit caveat:** A formal a11y/performance audit was not in scope for
this evaluation. Recommended as a follow-up (see `05_RECOMMENDATIONS.md`).

---

## Goal Coverage Check

Each Priority Purpose from the May 5 draft maps to ≥1 goal:

| Priority Purpose | Covered by |
|---|---|
| Convey what DSP does generally + current initiatives | G1 |
| Donate | G2 |
| Subscribe to e-newsletter | G2, G3 |
| Take online action | G2 |
| Take in-person action | G2 |
| Volunteer | G2 |
| Join Denver Streets Congress | G2, G6 |
| Track specific issue areas | G3 |
| Document successes & impact | G4 |
| Communicate movement ideas / "why" | G5 |
| Resource for residents advocating | G6 |
| Resource for journalists | G7 |
| Integrate with Mailchimp/Muster/FundraiseUp/social | G8 |
| (implied) Search discoverability | G9 |
| (implied) Accessibility & mobile | G10 |
