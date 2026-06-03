# WordPress Recommendations — denverstreetspartnership.org

**Date:** 2026-06-03
**Status:** PROPOSAL — **no changes have been made.** Nothing here is done until the team signs off.
**Prepared by:** Ashton (with the website audit + current Google Analytics baseline)

---

## Purpose

We now have WordPress access, so we *can* make fixes — but we won't touch anything
without group agreement. This is the list of recommended changes, why each one
matters, how risky it is, and whether it can be undone. Read it, and approve the
ones you want done. We'll do them one at a time, safely.

Each item was **re-verified on the live site today** (2026-06-03) or is carried
from the May 22 audit and marked as such. The "why" is backed by real Google
Analytics numbers from the 28-day baseline (2026-05-06 → 06-02).

## How we'll make changes safely (so nothing breaks)

- **Back up first.** A full WordPress + database backup before any edit.
- **Child theme, not the core theme.** Edits go in a *child theme* or Divi's
  built-in settings, so a future Divi update can't wipe them.
- **One at a time, verified.** Each change is made, checked on desktop *and*
  mobile, and is reversible. Anything touching donations gets extra testing.
- **Nothing is one-way.** Every item below can be rolled back.

---

## Summary

| # | Recommendation | Why it matters | Effort | Risk | Decision |
|---|---|---|---|---|---|
| 1 | Fix mobile pinch-zoom | 35% of visitors are on mobile; current setting fails accessibility law | Low | Very low | **Approve?** |
| 2 | Give Donate one real URL | Donate traffic is split across 2 URLs and barely engaged | Med | **Medium** (revenue path) | **Approve?** |
| 3 | Fix broken volunteer link | Visitors who click it hit a dead end | Low | Low | **Approve?** |
| 4 | Remove dead analytics tag | Loads on every page, collects nothing since 2024 | Low | Very low | **Approve?** |
| 5 | Update footer copyright | Says "© 2020" — looks abandoned | Low | Very low | **Approve?** |
| 6 | Security hygiene | Hide usernames, close an unused entry point | Low | Low | **Approve?** |
| 7 | Measurement setup | So we can finally see which page drives a donation | Med | Low | Needs GA access |
| 8 | Growth (content) | Repeat what's already working | High | Low | Discuss |

---

## The recommendations

### 1. Fix mobile pinch-zoom  *(confirmed live today)*
**What:** The site currently blocks pinch-to-zoom on phones
(`maximum-scale=1.0, user-scalable=0`). We'd change it to the standard setting
that lets people zoom.
**Why:** **35% of visitors are on mobile** (646 of ~1,820 users last month), and
blocking zoom is a WCAG accessibility failure — a real issue for a public-interest
org. **Effort:** ~10 min. **Risk:** very low; one line, instantly reversible.

### 2. Give Donate a single real URL  *(confirmed live today)*
**What:** Today the homepage opens a donate popup via `?form=donate`, and there's
also a `/donate/` page — two URLs for the same action. We'd pick one canonical
`/donate/` page and redirect the rest to it.
**Why:** Analytics shows donate traffic **split across both URLs**, with the popup
version showing **0.8 seconds** of engagement (people aren't reaching it). One URL
means donations are countable, bookmarkable, and linkable from emails. It's also
the prerequisite for measuring "which page drove a gift."
**Effort:** ~30 min. **Risk: medium — this is the money path,** so it gets a full
backup and click-through test before and after. Reversible.

### 3. Fix the broken volunteer link  *(from May 22 audit — re-verify before fixing)*
**What:** The volunteer call-to-action points at a Mailchimp survey URL that only
works inside an email; on the website it dead-ends. We'd point it at a real signup
page or embedded form. **Why:** Volunteer signups is a stated goal; this link
currently converts no one. **Effort:** ~15 min. **Risk:** low.

### 4. Remove the dead analytics tag  *(confirmed live today)*
**What:** The old Universal Analytics tag (`UA-144848215-2`) still loads on every
page. Google stopped processing its data on **July 1, 2024** — it collects nothing.
We'd remove it. The current analytics (GA4 + Tag Manager) stay untouched.
**Why:** It's a wasted request on every pageview and clutter. **Effort:** ~10 min.
**Risk:** very low — it's already dead; removing it changes no live reporting.

### 5. Update the footer copyright  *(confirmed live today — says "© 2020")*
**What:** Change the footer to the current year, set to update automatically.
**Why:** A 2020 date signals an abandoned site to first-time visitors and funders.
**Effort:** ~5 min. **Risk:** very low.

### 6. Security hygiene  *(from May 22 audit)*
**What:** Hide WordPress usernames from public lookup (`?author=`,
`/wp-json/.../users`) and disable XML-RPC if nothing uses it.
**Why:** The audit found usernames are publicly exposed. Note: the host's firewall
already blocks password-guessing attacks, so this is **cleanup, not an emergency** —
but worth doing. **Effort:** ~30 min total. **Risk:** low (we confirm XML-RPC isn't
needed by Jetpack/mobile first).

### 7. Measurement setup  *(needs Google Analytics edit access — separate from WordPress)*
**What:** Mark donations and form submissions as "conversions" in GA4, and tag the
newsletter/social links so we can see where traffic comes from.
**Why:** Right now GA4 records **zero conversions** — it can't tell us if any page
drives a donation or signup, even though the visit data is fine. The form-submit
events are *already being collected* (14 last month); they just need to be flagged.
**Status:** blocked on someone granting Ashton **Editor** access to the GA4
property — does not require touching WordPress. (Link-tagging tool is already built:
`honnecke.us/utm.html`.)

### 8. Growth — repeat what works  *(content/design, not a quick fix)*
**What:** The single best-performing page last month was
`/colorado-brt-comment-guide/` (444 views, **56 seconds** average engagement) — an
action/comment guide. We'd replicate that format for other campaigns, and surface
recent articles on the homepage (which today leads with "what we do" tiles, not the
blog). **Why:** It's a proven pattern on your own site. **Effort:** higher; this is
a content decision for the team, not a one-line fix.

---

## What needs what

- **Items 1–6:** WordPress access only — ready to go on approval.
- **Item 7:** Google Analytics **Editor** access (pending) — no WordPress needed.
- **Item 8:** A content/communications decision by the team.

## Evidence (live homepage check, 2026-06-03)

```
viewport : width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0   ← blocks zoom
dead UA  : UA-144848215-2 still present
analytics: GT-WFFQB5TW (GA4) + GTM-TZJRKMV (Tag Manager) — both live/good
donate   : ?form=donate still on homepage (dual URL)
footer   : © 2020 Denver Streets Partnership
```

GA baseline backing the "why": `analytics/ga-exports/2026-05-06_to_2026-06-02/`.

---

## The ask

Approve the items you want done (1–6 are low-risk; 2 gets extra care). We'll
back up, make each change in a child theme, verify on mobile and desktop, and
keep every step reversible. **Nothing happens until you say go.**
