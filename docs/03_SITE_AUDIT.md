---
doc_id: 03_SITE_AUDIT
title: Site Audit — Findings Mapped to Goals
date: 2026-05-06
audit_method: |
  Live fetch of homepage, /about/, /what-we-do/, /our-impact/, /blog/,
  /resources/, /get-involved/, /get-involved/stand-up-show-up/,
  /get-involved/email-signup/, /what-we-do/colorado-boulevard/, plus the
  WordPress sitemap index. No GA/Search Console access; no a11y or
  performance audit performed.
relates_to:
  - 02_GOALS.md
  - 05_RECOMMENDATIONS.md
---

# Site Audit Findings

Findings are organized by goal (G1-G10 from `02_GOALS.md`). Each finding
has a severity tag:

- **WORKS** — current state meets the goal.
- **GAP** — current state partially meets the goal; visible deficit.
- **BLOCKER** — current state actively blocks the goal.

## Site Map At-a-Glance

WordPress, with custom post types: `page` (~73), `post` (blog), `project`
(~247), `location`, `event`. Sitemap is healthy and indexed. Inferred plugins
/ integrations from page content:

- **Mailchimp** — newsletter and volunteer survey forms.
- **Muster** — petitions / advocacy actions (with some Google Forms fallbacks).
- **FundraiseUp** — donation widget (inferred from external integration list).
- **Social** — Facebook, X/Twitter (LinkedIn, Instagram, Bluesky in priority
  list but not visible in homepage footer).
- **Design vendor** — interr0bang.com (footer credit).

## Top-Level Information Architecture

Header nav (homepage):

- About → Strategic Framework, Staff, Advisory Board, Contact
- What We Do → Policy, Place
- News → Blog, Press, Resources
- Get Involved → Email Subscribe, Take Action, Volunteer, Work with Us,
  Fix My Street Guide, Denver Streets Congress
- Donate (button)

**Mismatch:** "Policy" and "Place" appear in nav but `/policy/` and
`/place/` return 404. Actual content lives under `/what-we-do/[campaign]`.
Either the nav links or the URL structure needs to be reconciled.

---

## G1 — Establish identity and current focus

**WORKS**

- Tagline "Streets are for people" is unambiguous.
- Homepage hero leads with one current campaign (Colorado Boulevard BRT).
  This is the right pattern.
- Mission statement is plainly worded: "advocate for the cultural and
  systemic changes necessary to reduce our city's unsustainable dependence
  on cars."

**GAP**

- The hero campaign is the only "current initiative" surfaced above the
  fold. Other live campaigns from the homepage's lower sections (Vision
  Zero, Twenty is Plenty, transit) are introduced as evergreen issue areas,
  not as current campaigns with current asks.
- No "What we're doing this month/quarter" panel anchored in time.

---

## G2 — Frictionless engagement

**WORKS**

- Donate button is persistent in nav.
- Tiered CTAs on the Colorado Blvd campaign page are well designed:
  petition (low), survey (low), open house (medium), action team (high).
  This is the template for other campaigns.

**GAP**

- "Take Action" page (`/get-involved/stand-up-show-up/`) lists four
  campaigns with mixed conversion patterns: some go to Muster, some to
  Google Forms, some to Google Drive PDFs. Inconsistent.
- No persistent supporter "what I've done" view — repeat advocates
  can't see their own history, which is a known retention lever.
- Volunteer signup is a Mailchimp survey form; not differentiated by
  opportunity type, time commitment, or skill.

**BLOCKER**

- Email signup at `/get-involved/email-signup/` does not capture topic
  interest at the form level. The only segmentation is geographic
  (address). Per the CSV's own AI insight, topic-segmented sends get
  2-3× the engagement of full-list sends. The funnel is throwing away
  segmentation data at the entry point.

---

## G3 — Per-topic interest expression

**BLOCKER**

- No per-topic subscribe option found anywhere on the site.
- No taxonomy visible on the blog or projects archive: posts and
  projects have no topic tags surfaced to readers; no per-topic RSS
  feed; no per-topic landing pages.
- The Resources page lists 115 items grouped by document type (Letter,
  Report, etc.) but **not by topic** — a researcher can't filter to
  "everything you've published on Vision Zero."

---

## G4 — Quantified impact documentation

**BLOCKER**

- `/our-impact/` is qualitative-only. Quote from the page:
  *"We measure our impact in conversations had, neighbors partnered
  with, and people empowered to advocate."*
  This is fine as framing but is the entire substance of the page. No
  numbers, no year list, no campaign archive, no policy-win timeline.

- Specific wins that should be documented are scattered or missing:

  | Win | Evidence on site? |
  |---|---|
  | Denver Deserves Sidewalks (Measure 307) | Mentioned on `/what-we-do/` as a victory; no dedicated outcome page |
  | Twenty is Plenty rollout | Has a `/what-we-do/twenty-is-plenty/` page; outcome data unclear |
  | Jaywalking decriminalization | Multiple project links to news coverage; no DSP-authored outcome summary |
  | Bicycling Rewards Program | Has a page; participation numbers not surfaced |
  | E-bikes for Deliveries | Has a page; outcome data unclear |
  | Advocacy Academy | Has a page; graduate count, alumni outcomes unclear |
  | CU Denver studies / East Colfax Parking study / Cloverleaf Oral History | Not surfaced as a research portfolio |

---

## G5 — Movement education ("why")

**GAP**

- Educational framing exists in pieces (mission statement, Vision Zero
  page, Colorado Blvd "what success looks like" section).
- No central "Why this matters" / "Streets 101" hub. The five foundational
  questions from the priority-purposes draft (benefits of reducing car
  dependency, why road widening is bad, transit ↔ Vision Zero, what
  successful transit looks like, equity intersection) are not addressed
  as evergreen explainers.
- Missed SEO opportunity: these are exactly the queries a curious resident
  or journalist would type into Google.

---

## G6 — Resident self-service toolkit

**WORKS**

- Fix My Street Guide exists at `/get-involved/fix-my-street-guide/`.
- Address-based newsletter targeting is implemented (per signup page
  copy).

**GAP**

- Fix My Street Guide is buried — discoverable only via the "Get Involved"
  submenu, not from a homepage tile or an issue-page sidebar.
- No "find your council district" / "find your representatives" lookup
  on the site. (Could integrate with civicdb or the city API.)
- No per-corridor or per-neighborhood landing pages aggregating "what's
  happening on YOUR street" for the hyperlocal resident profile (P3).

---

## G7 — Press & researcher resource

**BLOCKER**

- No press kit page found. The audit could not find: media contact,
  executive bios with downloadable headshots, downloadable logo, recent
  press-ready quotes, or a press release archive.
- Press releases exist (visible in project URLs as
  `/project/press-release-...`) but are co-mingled with general projects
  and not surfaced as a distinct press archive.
- `/our-impact/press/` exists as a path but was not deeply audited
  (recommend follow-up review).

**GAP**

- Resources page has 115 items but no search, no topic filter, no year
  filter. Unusable as a research portfolio.
- No citation metadata (recommended citation, DOI/URL, publication date)
  on resource items.

---

## G8 — Integration with engagement platforms

**GAP**

- Each platform works individually, but supporter identity is not unified.
  A donor in FundraiseUp is not identifiable as the same person who took
  three Muster actions and is on the Mailchimp list.
- No webhook-driven automations visible (e.g., "donor tag added to
  Mailchimp record on first gift," "advocate-of-the-month list built
  from Muster action count").
- Ad-hoc Google Forms / Google Drive links inside otherwise-Muster flows
  break the funnel and lose data.

**Note:** The fix here is `06_ARCHITECTURE.md`, not a content change.

---

## G9 — Search discoverability

**WORKS**

- WordPress sitemap is healthy and indexable: 13 sitemap files covering
  posts, pages, projects, locations, events, and taxonomies. ~247 project
  posts give the domain content depth.
- Many recent project URLs are press citations of DSP — good outbound
  link signal.

**GAP / BLOCKER**

- Test/orphan pages live in the sitemap: `test-full-width`,
  `test-filter-page`, `sidewalksold`, `event-2`, `event-4`, `event-7`,
  `event-8`, `event-9`, `event-11`. These dilute crawl budget and signal
  neglect.
- URL drift: `/policy/`, `/place/`, `/our-work/`, `/take-action/`,
  `/donate/`, `/news/` all 404 despite being intuitive guesses (and in
  some cases referenced by nav language). No 301 redirects observed.
- No structured data (Schema.org Organization, Article, Event,
  NewsArticle) confirmed in the audit. Without it, blog posts and event
  pages miss rich-result eligibility.
- "What We Do" categorization mixes evergreen topic pages with
  campaign-specific pages with neighborhood pages — diffuses topical
  authority that should concentrate on a small set of high-value pages.

---

## G10 — Accessibility & performance

**Audit caveat:** Not formally tested. A WCAG 2.2 AA audit and a
Lighthouse mobile run on the top 10 pages are recommended.

**Hypotheses worth testing:**

- The CSV reports mobile is 14-15% of email clicks vs. desktop's 77-82%
  — unusually low mobile engagement for a civic audience. While email
  client behavior explains some of this, the *site-side* mobile UX
  (form length on signup, mobile petition flow, donate page mobile
  performance) likely contributes. Worth measuring.
- Embedded Mailchimp/Muster/FundraiseUp widgets are common a11y weak
  spots — keyboard traps, missing labels, poor color contrast, missing
  ARIA attributes are typical issues with vendor-embedded forms.

---

## Cross-Cutting Findings (Not Goal-Specific)

### Content drift

The site has accumulated stale paths, orphan event stubs, "old" page
suffixes (`/sidewalksold/`), and duplicated patterns (e.g., a
`micro-grants` page under `/what-we-do/` and a separate `/microgrants/`
page at the root). This is normal for a long-running WordPress site
but compounds as crawl/IA debt over time.

### Single voice / single author

All blog posts are attributed to "DSP" as a single author. This is a
choice, but it removes attribution credibility (P7 Journalist quote
sourcing; P8 Researcher citation) and team-building visibility.

### No event calendar that's actually used

The `/events/` post type has placeholder entries (`event-2`, `event-4`,
etc.) but no live calendar surface. Event promotion appears to live in
campaign pages and the newsletter, not on a calendar.

### Strong campaign template, inconsistently applied

The Colorado Boulevard page is a model campaign page: tiered CTAs,
crash data, clear "what success looks like," coalition framing,
visual diagrams. This template is **not** uniformly applied to other
campaigns (Vision Zero, Twenty is Plenty, sidewalks, Federal, Colfax).
Reapplying the template across existing campaigns is a high-leverage
quick win.

---

## Severity Summary

| Goal | Status | Severity |
|---|---|---|
| G1 Identity | Mostly works | minor GAP |
| G2 Engagement | Works for some, breaks for others | GAP + 1 BLOCKER |
| G3 Topic tracking | Not implemented | BLOCKER |
| G4 Impact documentation | Aspirational text only | BLOCKER |
| G5 Education | Scattered, no hub | GAP |
| G6 Resident toolkit | Exists, undiscoverable | GAP |
| G7 Press/researcher | No press kit | BLOCKER |
| G8 Integrations | Siloed | GAP |
| G9 SEO | Healthy fundamentals, IA debt | GAP |
| G10 A11y/perf | Untested | UNKNOWN — audit recommended |
