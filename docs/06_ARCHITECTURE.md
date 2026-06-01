---
doc_id: 06_ARCHITECTURE
title: Target Architecture — WordPress + Custom Backend
date: 2026-05-06
relates_to:
  - 05_RECOMMENDATIONS.md
constraints: |
  - Keep WordPress as the content management system (no migration)
  - Linux-first hosting; container-based deployment preferred
  - Continue using Mailchimp, Muster, FundraiseUp; do not switch platforms
  - Small staff team; system must be operable without a full-time engineer
  - NO NEW SaaS SPEND. Free OSS, free tiers, and self-hosted only.
    Existing paid platforms stay; nothing new is added to the SaaS bill.
---

# Target Architecture

## Principle

WordPress stays. It runs the content (pages, blog, projects, resources,
events). It is the right tool for that job and the staff already know it.

The new piece is a **small custom backend service** that owns the things
WordPress is bad at: cross-platform supporter identity, integration
plumbing, automation triggers, and personalization.

The backend talks to WordPress, not through it. WordPress fetches small
JSON fragments from the backend at render time (or via JavaScript at view
time) to inject personalized widgets. The backend never touches the WP
database directly.

```
                  ┌──────────────┐
   denver visitor │   browser    │
                  └──────┬───────┘
                         │
               ┌─────────┴─────────┐
               │                   │
               ▼                   ▼
       ┌──────────────┐    ┌──────────────┐
       │  WordPress   │    │  Backend API │
       │  (content)   │◀──▶│  (identity,  │
       │              │    │  integrations)│
       └──────┬───────┘    └──────┬───────┘
              │                   │
              ▼                   ▼
       ┌──────────────┐    ┌──────────────┐
       │   MariaDB    │    │  Postgres    │
       │  (WP core)   │    │ (supporters) │
       └──────────────┘    └──────────────┘
                                  │
              ┌───────────────────┼───────────────────┐
              ▼                   ▼                   ▼
       ┌────────────┐      ┌────────────┐      ┌────────────┐
       │  Mailchimp │      │   Muster   │      │FundraiseUp │
       └────────────┘      └────────────┘      └────────────┘
```

---

## Backend Responsibilities

### 1. Supporter identity (canonical)

A `supporters` table keyed on email (lowercased, normalized). Each row
links to:

- Mailchimp member ID + topic-group memberships
- Muster supporter ID + action history
- FundraiseUp donor ID + gift history
- Volunteer profile (skills, availability, neighborhood)
- Denver Streets Congress membership status
- Tags (donor, advocate, journalist, partner, etc.)
- Source attribution (first-touch UTM, signup page, referrer)

Resolution rule: email is the canonical identifier. New events for
unknown emails create new supporter rows; subsequent events for the
same email merge into that row. Manual merge tool for edge cases.

### 2. Integration hub (webhooks + scheduled syncs)

Each external platform sends webhooks to the backend on events:

- Mailchimp: subscribe, unsubscribe, profile update, group change.
- Muster: action taken, action customized, supporter added.
- FundraiseUp: donation completed, recurring gift created/canceled.
- WordPress (custom forms): volunteer signup, Fix My Street submission,
  Congress application, contact form.

For platforms without webhooks (or to backfill), nightly pull syncs.

### 3. Personalization API

Read-only JSON endpoints called by WordPress (server-side or via JS):

- `GET /api/visitor/me` — given a supporter cookie, return display name,
  topic interests, last action date, donor status, suggested CTA.
- `GET /api/widgets/recommended-campaign?supporter=...` — returns the
  current campaign most aligned with the supporter's interests.
- `GET /api/impact/summary?campaign=...` — for the Impact page (R3),
  returns quantified outcome data.
- `GET /api/topic/landing?topic=vision-zero` — feeds the per-topic
  landing pages (R12).

Cookie-based identification with a magic-link login for the supporter
portal (R18). For anonymous visitors, all endpoints degrade gracefully
to non-personalized defaults.

### 4. Automation engine

Event-driven workflow runner. Triggered by webhook receipt; matches
against a small DSL of journey definitions; calls platform APIs to
execute actions.

Example journey:

```yaml
name: first_gift_thank_you
trigger:
  event: fundraiseup.donation.completed
  condition: supporter.lifetime_gifts == 1
actions:
  - mailchimp.tag.add: donor
  - mailchimp.tag.add: first_time_donor
  - mailchimp.journey.start: thank_you_series
  - log.event: first_gift
```

Start with 3-5 high-value journeys (R20). Don't build a journey builder
UI; YAML files in the repo are sufficient at this scale.

### 5. Form processing

Custom forms (Fix My Street submissions, volunteer intake, Congress
applications, press contact) post to the backend, which:

- Validates and stores the submission.
- Routes to the right Mailchimp tag / list / Muster outreach.
- Notifies the right staff member by email (or Slack webhook).
- Triggers any matching journey.

### 6. Reporting / dashboards

Cross-platform queries that no single platform can answer:

- "Show me all donors who haven't taken an action this quarter."
- "Show me the top 50 advocates who are not yet donors."
- "Show me topic-interest distribution by neighborhood."
- "Show me the supporter funnel: subscriber → action-taker → donor →
  recurring donor → Congress member."

Light dashboard UI (Metabase or Grafana pointed at Postgres) for staff.
No custom dashboard build needed in v1.

---

## Stack Recommendation

| Layer | Choice | Why |
|---|---|---|
| Backend language | Python 3.12 + FastAPI | Small team friendliness; async I/O for webhooks; type hints reduce bugs |
| Database | Postgres 16 | Relational fit for supporter data; JSON columns for platform metadata |
| Background jobs | Celery + Redis (or `arq`) | Webhook retries, scheduled syncs |
| Hosting | Single Linux VM (Hetzner / DigitalOcean) running Docker Compose | Simplest operable; the load profile here is small |
| TLS / CDN | Cloudflare in front of both WP and backend | Free tier sufficient; gives DDoS / bot mitigation |
| Auth (supporter portal) | Magic links via existing transactional email; sessions in HTTP-only cookies | No password storage; accessible to non-technical users |
| Auth (staff portal) | OIDC via Google Workspace if DSP uses it; otherwise magic link with allowlist | Matches existing org auth |
| Observability | Self-hosted Loki + Promtail (logs) and Prometheus + Grafana (metrics), running on the same VM. No hosted observability SaaS. | No-SaaS constraint; sufficient for this scale |
| CI/CD | GitHub Actions (free tier for public/non-profit OSS, or 2000 free minutes/mo for private); deploy via `docker compose pull && up -d` over SSH | No Kubernetes, no fancy GitOps |

**Why not Node:** either is fine. Python is recommended only because the
data-shaping work (CSV reports, ad-hoc analytics, Mailchimp segment
generation) reads more naturally in Python and is closer to the staff's
existing CSV-based reporting.

**Why not headless WordPress:** considered and rejected. Going headless
forces the staff to learn a new editing interface or maintain a separate
frontend. The proposed split (WP renders content; backend serves
fragments) preserves the existing editing workflow.

**Why not a turnkey CRM (EveryAction, Salesforce NPSP, ActionNetwork):**
**Ruled out by the no-SaaS constraint.** These products run $5K-$30K/year
for nonprofits at this scale, all paid SaaS subscriptions. The build
path described in this document is the path forward. (Considerations
that would have favored a turnkey CRM if cost weren't a constraint:
faster time-to-value, vendor-managed integrations, no on-call
ownership. Considerations that argued against even before the
constraint: lock-in, awkward fit with the personalization in R19 and
the journey logic in R20, and forced replacement of platforms DSP
already runs successfully.)

---

## Data Model (Sketch)

```sql
-- supporters: canonical record
CREATE TABLE supporters (
  id              uuid PRIMARY KEY,
  email           citext UNIQUE NOT NULL,
  first_name      text,
  last_name       text,
  address         text,
  council_district text,
  neighborhood    text,
  created_at      timestamptz NOT NULL DEFAULT now(),
  first_touch     jsonb,        -- utm, referrer, page
  metadata        jsonb         -- platform-specific blobs
);

-- platform_links: which IDs this supporter has on each platform
CREATE TABLE platform_links (
  supporter_id   uuid REFERENCES supporters(id),
  platform       text NOT NULL,  -- 'mailchimp' | 'muster' | 'fundraiseup' | 'wp'
  external_id    text NOT NULL,
  metadata       jsonb,
  PRIMARY KEY (supporter_id, platform)
);

-- topic_interests: which topics a supporter has declared
CREATE TABLE topic_interests (
  supporter_id   uuid REFERENCES supporters(id),
  topic          text NOT NULL,
  source         text NOT NULL,   -- where they declared it
  declared_at    timestamptz NOT NULL,
  PRIMARY KEY (supporter_id, topic)
);

-- events: the supporter activity log
CREATE TABLE events (
  id            bigserial PRIMARY KEY,
  supporter_id  uuid REFERENCES supporters(id),
  type          text NOT NULL,    -- 'donation' | 'action_taken' | 'page_view' | ...
  source        text NOT NULL,    -- which platform/system
  payload       jsonb,
  occurred_at   timestamptz NOT NULL,
  ingested_at   timestamptz NOT NULL DEFAULT now()
);
CREATE INDEX events_supporter_time ON events (supporter_id, occurred_at DESC);
CREATE INDEX events_type_time      ON events (type, occurred_at DESC);

-- tags: free-form labels on supporters
CREATE TABLE supporter_tags (
  supporter_id  uuid REFERENCES supporters(id),
  tag           text NOT NULL,
  applied_by    text NOT NULL,    -- 'auto:journey:first_gift' | 'staff:adrienne' | ...
  applied_at    timestamptz NOT NULL DEFAULT now(),
  PRIMARY KEY (supporter_id, tag)
);
```

This is a minimum-viable schema. Add `donations`, `volunteer_shifts`, etc.,
as separate tables once the v1 event log proves insufficient for the
needed queries.

---

## Security & Privacy

- **PII handling:** supporter records contain home addresses. Encrypt
  Postgres at rest (host-level disk encryption is sufficient).
- **TLS everywhere:** Cloudflare → backend → Postgres, all TLS.
- **Webhook verification:** every webhook receiver verifies the platform's
  signature header. Reject unsigned requests.
- **Rate limiting:** at Cloudflare and at FastAPI middleware.
- **Backups:** nightly logical Postgres dumps to off-host storage,
  encrypted; 30-day retention; quarterly restore drill.
- **Access control:** staff dashboard is allowlist-protected; production
  database has only the application user; admin access via SSH with key
  auth only.
- **Privacy policy:** update the published policy to disclose
  cross-platform supporter identification, the supporter portal, and
  retention rules. Provide a self-service deletion path (the backend's
  "forget me" endpoint cascades a removal across platforms).
- **GDPR / CCPA:** treat as if applicable even though the user base is
  primarily Denver — supporter portal needs export and delete options.

---

## What This Architecture Does *Not* Do

- It does not replace Mailchimp / Muster / FundraiseUp. They remain the
  systems of record for their domain. The backend is a unifier, not a
  replacement.
- It does not host the content. WordPress remains canonical for pages,
  blog posts, projects, resources, events.
- It does not run the donation flow. FundraiseUp's checkout is still
  used; the backend just receives the webhook and unifies the record.
- It does not include a full custom CRM UI in v1. Staff continue to
  manage supporters in each platform's existing UI, with the backend
  dashboard for cross-platform queries.

---

## Operational Footprint

Constraint: **no new SaaS spend.** Costs below are IaaS (servers,
storage, transactional email pay-per-use) — not SaaS subscriptions.

- One Linux VM (4 vCPU / 16GB RAM is plenty for this load) at
  Hetzner / DigitalOcean: ~$40-50/mo. IaaS, not SaaS.
- Cloudflare free tier (DNS, TLS, basic DDoS, caching). Free.
- Transactional email: AWS SES at usage rates (~$0.10 per 1000 emails)
  — typical DSP volume puts this under $5/mo, often under $1. SES is
  pay-per-use IaaS with no monthly minimum. Confirm this fits the
  no-SaaS interpretation before adopting; alternative is to use the
  existing Mailchimp transactional sending where supported, or a
  self-hosted SMTP relay (more work, no recurring cost).
- Backups: nightly logical Postgres dumps to off-host storage. Object
  storage at <$2/mo (Backblaze B2 / Hetzner Storage Box / S3 Glacier
  pricing tier).
- Total infrastructure: well under $60/mo at this scale.

- Engineering: estimate 1 part-time engineer (or a 3-4 month engagement
  with a contractor) to build v1 (R16, R17). Maintenance after that is
  light — webhook adapters, occasional journey updates, Postgres
  upgrades — well under 5 hours/week steady state. Volunteer / pro-bono
  engineering capacity is a viable path at this scale; a paid contractor
  is the alternative if internal capacity is unavailable.
