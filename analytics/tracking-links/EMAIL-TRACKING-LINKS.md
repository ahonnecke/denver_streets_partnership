# How to add tracking links to DSP emails

**For:** Adrianne & Jill · **Time per link:** ~1 minute once you've done a couple.

This is how we answer "which email drove this donation / signup?" Right now we
can't — every email link is untagged, so Google Analytics sees the traffic but
not where it came from. Tracking links fix that.

---

## The idea in one picture

```
Email link:   denverstreetspartnership.org/go/spring-donate
        302 →  <real donate page>?utm_source=newsletter&utm_medium=email&utm_campaign=spring-2026
```

You put a short, branded link (`/go/spring-donate`) in the email. It bounces
through our own website, which quietly tacks on tracking tags and sends the
person to the real destination. They never notice. We get the data.

**Two kinds of links, handled slightly differently:**

| Link goes to… | What to do |
|---|---|
| **Our own website** (a page on denverstreetspartnership.org) | Just add the tracking tags — no redirect needed. |
| **Somewhere else** (donate processor, petition, action page) | Make a `/go/...` redirect so our site can count the click before handing off. |

The **Link Builder tool** (`link-builder.html`) figures out which case you're in
and gives you the exact links to use. Open it by double-clicking the file.

---

## Naming rules (read this once — it matters)

Google Analytics treats `Newsletter`, `newsletter`, and `news letter` as three
**different** sources. Inconsistent names shred the reports. So we standardize:

| Tag | What it means | Always use |
|---|---|---|
| `utm_source` | where the link lives | `newsletter` (for the regular email) |
| `utm_medium` | the channel | `email` (always, for email) |
| `utm_campaign` | which send / what it's about | `spring-2026`, `donate-yearend`, `legislative-alert` — lowercase, hyphens, no spaces |
| `utm_content` | *(optional)* which button, for A/B | `header-button`, `footer-link` |

Rules: **all lowercase, hyphens instead of spaces, no punctuation.** The Link
Builder enforces this for you, but use the same `utm_campaign` for every link in
the same email so they group together.

---

## Step by step

### 1. Build the tracked link
1. Open `link-builder.html` (double-click — it runs in your browser, nothing to install).
2. Paste the **destination** (where you want people to end up).
3. Type the **campaign** name (e.g. `spring-2026`). Leave source/medium as the defaults.
4. Click **Build**. You get:
   - the **redirect target** (destination + tracking tags), and
   - a suggested short link like `/go/spring-donate`.

### 2. Create the redirect (off-site links only)
*On-site links skip this — paste the tagged link straight into the email.*

1. Log into WordPress → **Pretty Links** (left menu).
2. **Add New Link.**
   - **Target URL** = the *redirect target* from the builder (the long one with the tags).
   - **Pretty Link** = the short slug, e.g. `go/spring-donate`.
   - **Redirection type** = **302 (Temporary)** — important, so we can re-point it later.
3. **Update.** Your link is now `denverstreetspartnership.org/go/spring-donate`.

### 3. Put it in the email
Use the **short** `/go/...` link as the button/link in the email. Done.

### 4. Log it
Add one row to `tracked-links-log.csv` (or the shared Google Sheet) so we have a
record and don't reinvent slugs. The builder gives you a ready-to-paste row.

---

## Before your first send — confirm two things in the email tool

We're not 100% sure which email platform is in use; check these wherever you
send from (Mailchimp, Constant Contact, etc.):

1. **Click tracking** — leave it **ON**. It counts opens/clicks inside the email
   tool and is separate from (and stacks fine with) our `/go/` redirects.
2. **Automatic UTM / "Google Analytics link tracking"** — if your email tool has
   a setting that *auto-adds* `utm_` tags, turn it **OFF**, or it will double-tag
   our links and break the reports. We add the tags ourselves. **Pick one source
   of tags, not both.**

---

## Where the results show up

- **Click counts per link** → Pretty Links dashboard in WordPress (immediate).
- **What people did after clicking** (signed up? donated?) → Google Analytics,
  under Traffic acquisition / by `Session campaign`. On-site destinations show
  the full funnel; off-site ones (e.g. an external donate processor) show the
  click but not the dollar unless that processor feeds our analytics.

---

## One-time setup (whoever admins WordPress, not Adrianne/Jill)

- Install **Pretty Links** (free tier is enough). Alternative: the **Redirection**
  plugin — same idea, fewer click stats.
- Set the plugin's **default redirect type to 302 (Temporary)** so campaign links
  stay re-pointable.
- Reserve the `/go/` prefix for these links so they're easy to find and audit.
