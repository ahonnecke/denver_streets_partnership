# Denver Streets Partnership — Site Audit & Infra Plan

**Audited:** denverstreetspartnership.org
**Date:** 2026-05-22
**Method:** HTTP probes of homepage, primary nav pages, a sample article, sitemap, robots, REST API, login endpoints, and external link targets. No Lighthouse / no JS-rendered DOM yet — recommend a follow-up with WebPageTest or Lighthouse CI plus a session of the live Google Analytics data once we have access.

---

## TL;DR

Solid WordPress + Divi site that loads fast over HTTP (~0.7s TTFB) and has a clean sitemap with 560+ URLs all returning 200. But it has accumulated the usual WP/Divi entropy: duplicate/empty meta tags, three overlapping analytics installs (one of them — Universal Analytics — has been dead since July 2024), a viewport that blocks zoom (WCAG fail), a stale footer copyright, leaked admin username, and no privacy / cookie notice in a Colorado-CPA jurisdiction.

**Security verified 2026-05-22:** ModSecurity on the host blocks brute-force POSTs against both `wp-login.php` and `xmlrpc.php` (32 attempts across both surfaces, all returned 406 before WP saw them). Owner confirmed no user has a trivially-guessable password. The username leak is still real but is hygiene rather than active exposure.

None of that is on fire. But before bolting a React app on the side, fix the hygiene issues first — otherwise the new app inherits the same SEO / a11y / privacy posture.

---

## 1. What the Site Does Well

| Area | Observation |
|---|---|
| **Uptime / performance** | All probed pages return HTTP 200 in 0.7–0.9s. Server is Apache behind nginx page-cache (`x-nginx-cache: WordPress`). No degradation under sequential requests. |
| **Sitemap + crawlability** | `wp-sitemap.xml` is healthy, 13 sub-sitemaps, **560 URLs** total (170 posts, 73 pages, 247 projects, 58 events, 12 locations). All 243 page+post URLs return 200 — zero internal dead links in the indexed corpus. |
| **Permalink structure** | Clean `/slug/` permalinks (no `?p=` or date-prefixed URLs). Good for SEO. |
| **Content depth** | Substantial library of programs (Twenty is Plenty, Vision Zero, Complete Streets, Colfax, Federal Blvd, Sidewalks, Transit, etc.) and an active blog. Article structure is consistent (1 H1, CTAs at end). |
| **Image alt text** | 100% of homepage `<img>` tags have `alt` attributes. |
| **Multiple languages** | Spanish landing pages exist (`/transit-town-halls-spanish/`, `/programa-bicycling-rewards/`). |
| **Mobile-first viewport** | Has a viewport meta — though see issue #4 below. |
| **Open Graph + Twitter cards** | Present on every page (basic; see issues). |

---

## 2. What It Doesn't Do Well

### 2a. HTML hygiene / SEO

| # | Issue | Evidence | Impact |
|---|---|---|---|
| H1 | **Duplicate `<meta name="description">` — empty one first** | Line 5: `<meta name="description" content="" />` then a populated one on line 7. Most parsers take the *first* one. | The site is broadcasting an **empty description** to search engines and social previews. |
| H2 | **Homepage has zero `<h1>` tags** | `grep -c '<h1' home.html` = 0 | SEO + screen-reader: the page has no semantic top-level heading. |
| H3 | **About page has 4 `<h1>` tags** | `grep -c '<h1' page_about_.html` = 4 | Diluted heading hierarchy; should be exactly one. |
| H4 | **Viewport blocks user zoom** (WCAG 1.4.4 fail) | `<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0" />` | **Accessibility violation.** Users with low vision can't pinch-zoom on mobile. |
| H5 | **WordPress version disclosed** | `<meta name="generator" content="WordPress 7.0" />` | Helps attackers target known-vuln versions. |
| H6 | **Stale `<meta itemtype="article" />` and `og:type=article`** site-wide | Every page declares itself as an article, including non-article pages. | Schema.org + OG metadata is wrong for landing pages. |
| H7 | **Footer copyright says "2020"** | Line 791: `All contents © 2020 Denver Streets Partnership` | Looks abandoned. |
| H8 | **Footer designer link is broken-ish** | `<a href="http://lnterrobang.com/" target="blank">interr0bang.com</a>` — link text disagrees with href (lowercase L vs I/0), `http://` not `https://`, `target="blank"` (literal window name, not new tab), missing `rel="noopener noreferrer"`. Both domains resolve to the same Squarespace site, so users get there, but it's sloppy on multiple axes. | Looks unmaintained. Security-wise, `target="blank"` without `rel="noopener"` is a tabnabbing risk. |
| H9 | **"Volunteer" link in main nav points to Mailchimp survey with a literal merge-tag URL** | `https://us15.list-manage.com/survey?u=...&id=...&e=*%7CUNIQID%7C*` (= `*\|UNIQID\|*`). Merge tags only resolve inside Mailchimp emails — on the web they stay as the literal string. | The survey will record visitors with `*\|UNIQID\|*` as their identifier instead of a real one. **Probably the cleanest single-instance bug to fix.** |
| H10 | **Mixed http:// and https:// outbound links** | `http://denvergov.org/...`, `http://bit.ly/dsp-emails`, `http://lnterrobang.com/`, `http://www.denvergov.org/maps/...` | http:// links may trigger mixed-content warnings on https sites; bit.ly returns 406 to some User-Agents. |
| H11 | **Bit.ly dependency chain** | 6 `bit.ly/` links in nav-adjacent content. One (`bit.ly/dsp-emails`) returns 406. | If a bit.ly account ever changes or the service has an outage, 6 important links break silently. |
| H12 | **Test/old pages indexed in sitemap** | `/test-full-width/`, `/test-filter-page/`, `/what-we-do/sidewalksold/`, `/2020-bike-lanes/`, `/event-2/`. | SEO noise; competing pages for ranking signals. |
| H13 | **Twitter URL not updated to x.com** | Outbound link to `twitter.com/BikeWalkBus` | Twitter redirects, but stale. |
| H14 | **Two slightly-different forms of Instagram / Facebook URLs in one page** | `instagram.com/bikewalkbus` and `www.instagram.com/bikewalkbus/`; FB with and without trailing slash. | Cosmetic, but indicates inconsistent template editing. |
| H15 | **Trailing-slash inconsistency on internal anchors** | `/about#staff` vs `/about/#staff`; `/what-we-do#policy` vs `/what-we-do/#policy` — both on the homepage. | Each version generates a redirect or duplicate cache entry. |
| H16 | **Mixed absolute/relative links in articles** | One article uses both `href="/contact"` and `href="https://denverstreetspartnership.org/get-involved/contact/"` | Cosmetic; makes future domain migrations harder. |
| H17 | **"Back to blog" button on articles points to `/our-impact/blog/`** which 301-redirects to `/blog/` | Article template button | Every article click takes an unnecessary redirect hop. |

### 2b. Accessibility

- **No "skip to main content" link** (WCAG 2.4.1). With screen-readers, users tab through the full nav on every page.
- **Zero `aria-label` attributes** on the homepage. Icon-only buttons (hamburger, social, etc.) are unlabeled.
- **Viewport disables zoom** (see H4) — top a11y priority.

### 2c. Performance

| Metric | Home | About | Blog | Article |
|---|---|---|---|---|
| HTML size | 164 KB | 175 KB | 281 KB | 184 KB |
| Stylesheets | 19 | 19 | 19 | 19 |
| External JS | 26 | 26 | 31 | 26 |
| Lazy-loaded `<img>` | 1 of 4 | — | — | — |

- **19 stylesheets** is a Divi/Plugin sprawl problem. WPForms ships 5 CSS files even on pages that don't have a form.
- **Font Awesome loaded twice** (local + `use.fontawesome.com` CDN with v7.1.0). Pick one.
- **Google Fonts blocking load**: `Roboto + Roboto Slab` with 18 weight variants. Trim to the 3-4 weights actually used; switch to `font-display: swap` (already done) and use `preconnect`.
- Only 1 of 4 homepage images uses `loading="lazy"`. Below-the-fold images should all be lazy.

### 2d. Funnel visibility — **the org currently cannot answer "which page drives donations"**

I crawled every primary page and grepped for the standard tracking-link patterns. The findings:

| Check | Result | Implication |
|---|---|---|
| **UTM parameters on outbound links** | **0** matches site-wide | Mailchimp / Stripe / etc. all receive "direct" traffic — origin invisible. |
| **UTM parameters on internal cross-page links** | **0** matches | Can't distinguish "donate clicked from article" vs "from header" vs "from footer". |
| **`data-gtm-*` / `data-event` attributes on buttons** | **0** | No declarative event-tagging for GTM to fire on. |
| **Inline `gtag('event', ...)` calls** | **0** | No on-page custom events. |
| **`dataLayer.push({event:...})` (beyond GTM init)** | **0** | No GTM events being pushed manually. |
| **Multiple URLs for the same conversion** | `/donate/` and `/?form=donate` both exist | One funnel, two destinations — data gets split. |
| **Mailchimp `track/click?...&e=<hash>` URLs on public webpages** | **2** instances (in `/get-involved/email-signup/`) | These are *email-rewritten* tracker URLs. On the public web they attribute every click to one (random) email recipient. Pollutes Mailchimp campaign reports. |

**Bottom line:** GA4 is installed and collecting page-views, but the org has zero ability to see *which page drove a conversion* because no link is tagged and no button-click event fires. The whole post-pageview funnel is dark.

This isn't a "your analytics need work" — it's a "your analytics aren't measuring the four goals you said the site has."

### 2d-bis. What to change for funnel visibility — concrete recommendations

These five changes will give the org real funnel data within ~2 weeks of GA4 collection:

1. **One canonical donate URL.** Pick `/donate/`, kill `/?form=donate`, or vice versa. Add a 301 from the loser to the winner. Now "Donate page views" is a single number.
2. **Tag every CTA link with UTMs** using a documented convention:
   - `utm_source = denverstreetspartnership` (always — this is *internal* attribution, not paid media)
   - `utm_medium = header|footer|article-cta|sidebar|inline-link|home-banner`
   - `utm_campaign = donate|newsletter|congress|volunteer|stand-up`
   - Example: `https://denverstreetspartnership.org/donate/?utm_source=denverstreetspartnership&utm_medium=article-cta&utm_campaign=donate`
   - Why use UTMs on *internal* links: GA4 doesn't natively let you compare "donations sourced from the header" vs "donations sourced from articles." UTMs do. Caveat: this overwrites session source, so apply consistently or you'll re-attribute true external traffic. Safer alternative if that worries you → set up **GA4 custom events** with a `cta_location` parameter instead (option 3 below). Pick *one* approach, not both.
3. **Add GA4 events for every CTA click via GTM.** Three events cover the four goals:
   - `cta_click` with parameters `{ cta_location, cta_target, page_path }` — fires on Donate, Newsletter, Volunteer, Congress, Stand-Up buttons.
   - `form_start` and `form_submit` with `{ form_id }` — fires on WPForms and any embedded form.
   - `outbound_click` with `{ destination_host }` — fires on links leaving the domain.
   - Set up the donate `form_submit` (or the Stripe/GiveButter return URL) as a **GA4 Conversion**. Now you have a funnel: `article_view → cta_click → form_start → form_submit`.
4. **Remove the Mailchimp `track/click?...e=...` URLs from public pages.** Those are subscriber-scoped tracker links that only make sense inside emails. On the website, link directly to the destination URL (whatever the tracker was redirecting to). To recover destinations: in Mailchimp, open the campaign that generated the link, find the original URL behind the tracker.
5. **Document the measurement plan in a single Google Sheet** — one row per CTA, columns: `where it lives`, `UTM string`, `GA4 event`, `GA4 conversion?`, `owner`. Without this, every theme update will erase tagging silently.

### 2d-ter. Analytics — three trackers, one is dead

```
<script src=".../gtag/js?id=GT-WFFQB5TW"></script>      ← GA4 / Google Tag (live, via Site Kit)
<script src=".../gtag/js?id=UA-144848215-2"></script>   ← Universal Analytics (DEAD since 2024-07-01)
<script>...GTM-TZJRKMV...</script>                       ← Google Tag Manager (live)
```

- **UA-144848215-2 is Universal Analytics**, which Google stopped processing data for on July 1, 2024. The script still loads on every page (a network request per page-view) but receives no data. **Remove the UA snippet.**
- Both GA4 (GT-…) and GTM are loaded directly in the page rather than GA4 going *through* GTM. That's fine but is two separate tracking implementations to keep in sync. Recommendation: route GA4 *through* GTM and keep one config surface.

### 2e. Security posture

| # | Issue | Evidence | Severity |
|---|---|---|---|
| S1 | **WP REST API exposes 4 usernames including `admin`** | `GET /wp-json/wp/v2/users` returns: `admin`, `curt`, `dsp`, `dsp2` (Jill Locantore) | **High.** Combined with no rate-limit header on `wp-login.php`, this is a brute-force target. |
| S2 | **User enumeration via `?author=N`** | `?author=1` 301-redirects to `/author/admin/` — confirms ID 1 = `admin` | **High.** |
| S3 | ~~`xmlrpc.php` exposed~~ **Reclassified Low** — verified 2026-05-22 | Endpoint discovered via pingback link header. 16-attempt probe via `wp.getUsersBlogs` (plus a `system.listMethods` probe) returned 406 on every POST. ModSecurity blocks XML-RPC POSTs at the WAF, same as wp-login. Pingback-DDoS-amplification surface also blocked by extension. | **Low** (was Medium). Still disable it if no remote app needs it — defense in depth, ~10 min. |
| S4 | ~~`wp-login.php` reachable with no obvious CAPTCHA / 2FA / rate-limit header~~ **Reclassified Low** — verified 2026-05-22 | A 16-attempt classic-password probe against all 4 usernames returned 406 on every POST. Host's ModSecurity rules block automated logins before WP sees them. Owner separately confirmed no user has username-as-password. | **Low** (was Medium). Still: rename `admin`, add 2FA, disable XML-RPC. |
| S5 | **Zero security headers** | No `Strict-Transport-Security`, `Content-Security-Policy`, `X-Frame-Options`, `X-Content-Type-Options`, `Referrer-Policy`, `Permissions-Policy` on responses | **Medium.** |
| S6 | **WP version disclosed** | See H5 | **Low.** |

### 2f. Privacy / compliance

- **No privacy policy link, no cookie consent banner.** GA4 + GTM are tracking visitors, and Colorado Privacy Act (CPA, effective 2023-07) requires opt-out for sale/share of personal data and a clear privacy notice for residents.
- Meta Pixel domain verification meta tag is present (`facebook-domain-verification`), suggesting Meta Pixel may be in use via GTM — increases CPA scope.
- **Recommendation**: install a consent management plugin (e.g., Complianz, CookieYes — both have WP/GTM integrations) and add a `/privacy/` page linked from footer.

---

## 3. Site Goals & Funnel — How They Match Reality

You named four goals. Here's what the site actually does for each:

| Goal | Current state | Gap |
|---|---|---|
| **Drive visitors to articles** (top of funnel) | Strong: 170 indexed posts; clean permalinks; blog index reachable from main nav. Recent posts visible. | The homepage doesn't surface latest articles above the fold (homepage emphasizes "what we do" tiles, not blog). Consider a "Latest from the blog" strip on home. |
| **Drive visitors to CTAs** (sign-up form, vote, etc.) | OK: dedicated `/get-involved/email-signup/`, `/get-involved/stand-up-show-up/`, `/get-involved/contact/`. Articles end with CTAs to those pages. | (1) **Volunteer link is broken** (H9 above). (2) The donate flow uses a query param (`?form=donate`) that renders the same homepage with a modal — not deep-linkable, not bookmarkable, not analytics-friendly. Give donate its own URL. (3) No A/B testing / per-CTA conversion tracking visible. |
| **Drive visitors to donations** | A "Donate" button is in the global header, footer, and articles. | Donate button on homepage uses `target="blank"` (non-standard), no `rel="noopener"`. The query-param modal pattern makes it impossible to measure "what page drove the donation start". |
| **Articles convert readers** (bottom of funnel) | Articles have multiple CTAs: Newsletter, Stand Up Show Up, Congress, Donate, Contact. Decent variety. | (1) CTA placement is end-of-article only — readers who bounce mid-article see no CTA. (2) No event tracking visible on CTA clicks (no `data-gtm-*` attributes spotted). (3) Mixed relative/absolute links inside articles (H16) make GA cross-domain tracking less reliable. |

### Funnel observations from a single sample article (`/our-next-evolution/`)

- 1 H1 ✓
- 5 outbound CTAs (newsletter, stand-up, congress, donate, contact) ✓
- "Back to blog" button hits a 301 redirect — fixable (H17)
- No newsletter-inline form (only a link out to the signup page) — measurable conversion loss
- No social-share buttons in the markup (may be JS-injected; couldn't verify without rendering)

---

## 4. Priority List

Ordered by **impact × ease**. Each is small enough to ship in a single PR / WP admin session.

### P0 — Most urgent (security + a11y + broken)

1. **Fix the volunteer link** (H9) — replace Mailchimp survey URL with a real page or a Mailchimp signup form embed. *15 min in WP admin.*
2. **Remove zoom-blocking viewport** (H4) — change to `<meta name="viewport" content="width=device-width, initial-scale=1">`. Often in Divi theme options or `header.php`. *5 min.*
3. **Remove dead UA-144848215-2 tracker** (§2d) — delete the snippet from theme/Site Kit. *5 min.*
4. **Block user enumeration** (S1, S2) — add `wp-config.php`/`functions.php` filter to deny `/wp-json/wp/v2/users` for unauthenticated requests; disable `?author=` lookups. *20 min.* (Wordfence and iThemes Security have toggles for both.) Still worth doing as hygiene; brute-force urgency dropped after WAF verification (S4).
5. **Disable XML-RPC** (S3) — if no remote app needs it (Jetpack, mobile app), drop it via plugin or `.htaccess`. *10 min.* Not protected by the login WAF; separate attack surface.

> **Note (2026-05-22):** Login brute-force was de-prioritized after a 16-attempt probe confirmed ModSecurity blocks automated POSTs at 406, and the owner confirmed no user has a trivial password. The 5 items above are still the right starting set — just don't lose sleep over wp-login itself.

### P1 — Ship this sprint (SEO + hygiene)

6. **Delete the empty `<meta name="description">` and `<meta name="keywords">`** (H1) — find the duplicate source (probably theme `header.php` + an SEO plugin both emitting tags). *30 min.*
7. **Add a single H1 to every page, including homepage** (H2, H3) — Divi sections often default to H2. *1–2 hr template work.*
8. **Update footer copyright to dynamic year** (H7) — `&copy; <?php echo date('Y'); ?>`. *5 min.*
9. **Fix `target="blank"` → `target="_blank" rel="noopener noreferrer"`** site-wide (H8). *Find-replace in DB; 30 min.*
10. **Add a privacy policy page + consent banner** (§2f) — Complianz or CookieYes plugin. *2 hr setup + lawyer review.*
11. **Add security headers** (S5) — HSTS, X-Content-Type-Options, Referrer-Policy, Permissions-Policy. Easiest via `.htaccess` or hosting CDN. *30 min.*
12. **Add "Skip to main content" link** (§2b). *30 min in theme.*
13. **Audit and remove indexed test pages** (H12) — `/test-full-width/`, `/test-filter-page/`, `/what-we-do/sidewalksold/`. Either delete or noindex. *30 min.*

### P2 — Performance polish (do alongside the P1 batch)

14. **Stop loading WPForms CSS on pages without forms** — there's a WPForms setting for this. *15 min.*
15. **Pick one Font Awesome source** (local OR CDN, not both). *15 min.*
16. **Trim Google Fonts variants** to the 3–4 actually used; preconnect to fonts.googleapis.com. *30 min.*
17. **Add `loading="lazy"` to below-the-fold images** (Divi has a global toggle). *15 min.*
18. **Give donate flow a real URL** like `/donate/` instead of `?form=donate`. Makes it linkable + measurable in GA4. *30 min.*

### P3 — Analytics / measurement

19. **Route GA4 through GTM** rather than running both in parallel (§2d).
20. **Add GA4 events for CTA clicks** (newsletter signup, donate-start, donate-complete, congress-signup) — set up via GTM. Measure funnel.
21. **In Google Analytics, create funnel reports**: Article → Email Signup, Article → Donate, Home → Donate, Home → Email Signup. Compare to traffic volume to identify the weakest step.
22. **Exclude staff/internal traffic** so DSP staff page-views don't inflate the numbers (§2d-quater). Tag logged-in WP users with `traffic_type=internal`, register it as a custom dimension, and activate the GA4 Internal Traffic data filter.

### 2d-quater. Excluding staff (internal) traffic

GA4 excludes internal traffic in **two parts**, and the filter alone does nothing — you must also *tag* the traffic:

1. **Tag staff hits** with the event parameter `traffic_type = internal`.
2. **Activate the Internal Traffic data filter** (GA4 → Admin → Data Settings → Data Filters), which drops anything tagged that way.

For DSP, "staff" = logged-in WordPress users (they edit posts), so tag by **login state**, not by IP — IP filtering misses remote/home/mobile staff and breaks on dynamic IPs.

**Implementation (login-based, recommended):**

1. Emit login state into the dataLayer before GTM fires — WP child theme `functions.php` or a code-snippets plugin. Snippet lives in `analytics/wp-functions-snippet.php`.
2. In GTM: create Data Layer Variable `dlv.traffic_type`, then on the GA4 Configuration/Event tag add field `traffic_type = {{dlv.traffic_type}}`. (Requires GA4 routed through GTM — item 19.)
3. Register `traffic_type` as a **custom dimension** (GA4 → Admin → Custom definitions → Create custom dimension, event-scoped, parameter `traffic_type`). Needed so query scripts can filter/verify on it.
4. Activate the **Internal Traffic** data filter in **Testing** mode first (creates an evaluable dimension without dropping data), verify staff hits show as internal, then flip to **Active**.

**Caveats:**
- The data filter is **not retroactive** — do this *before* the ~6-week data-collection window starts.
- Leave it in **Testing** for a few days before going **Active**; Active is hard to undo cleanly.
- IP-based fallback (only if staff share a known office IP): GA4 → Admin → Data Streams → web stream → Configure tag settings → *Show all* → **Define internal traffic** → rule `traffic_type = internal` for the IP range. Weak for a small/remote nonprofit; use login-based as primary.

Query scripts in `analytics/` exclude `traffic_type=internal` at query time as belt-and-suspenders (and as the verification path while the filter is in Testing). Once the data filter is **Active**, query-side exclusion is redundant but harmless.

---

## 5. Infrastructure Plan — Adding a "Heavier" App Alongside WordPress

You said: *"adding a new heavier site that has heavier apps (maps, backend, etc) and will probably leave the wp site up, and add a react site or whatever for the new stuff."*

### 5a. Recommended split

Don't replace WordPress. Keep WP for the content corpus (560 URLs, easy non-dev editing, the org's existing workflow). Bolt the React app on at a **subpath** behind the same domain.

```
denverstreetspartnership.org/              → WordPress (existing, hosted on current provider)
denverstreetspartnership.org/app/*         → React app (new — maps, dashboards, interactive tools)
denverstreetspartnership.org/api/*         → Backend API for the React app (Vercel Functions / serverless)
admin.denverstreetspartnership.org         → (optional) protected admin / report builder
```

Subpath, not subdomain, because:
- Domain authority stays unified (better SEO).
- Cookies / auth tokens can be scoped to the root domain.
- Users perceive it as one site.
- No CORS gymnastics.

### 5b. Hosting + routing

The cleanest pattern given the constraint "leave WP up": put a **reverse proxy / edge router** in front of both origins and route by path prefix.

```
                ┌───────────────────────────────────────────────────────┐
                │  Cloudflare (or Vercel Edge / AWS CloudFront)         │
                │  - DNS                                                │
                │  - TLS termination                                    │
                │  - WAF + rate-limit (helps fix S3, S4)                │
                │  - Path-based routing:                                │
                │    /         → WP origin                              │
                │    /blog,    → WP origin                              │
                │    /wp-*     → WP origin                              │
                │    /app/*    → React origin (Vercel)                  │
                │    /api/*    → Functions origin (Vercel / Fluid)      │
                └────────────┬──────────────────────┬───────────────────┘
                             │                      │
              ┌──────────────▼─────────┐  ┌─────────▼──────────────────┐
              │  WordPress origin      │  │  Vercel project            │
              │  (current hosting)     │  │  - Next.js App Router      │
              │  - Divi theme         │  │  - React Server Components │
              │  - WPForms            │  │  - Routes:                 │
              │  - Events Manager     │  │    /app/maps/*             │
              │  - Site Kit (GA4)     │  │    /app/dashboard/*        │
              │  - REST API          │  │    /api/* (Fluid Functions)│
              └────────────┬─────────┘  └─────────┬──────────────────┘
                           │                      │
                           │                      ├─→ PostGIS / Supabase (maps, geo)
                           │                      ├─→ Vercel Blob (uploads, photos)
                           │                      ├─→ Mailchimp API (newsletter)
                           │                      ├─→ Donation processor (Stripe / GiveButter)
                           │                      └─→ GA4 (shared property)
                           │
                           └─→ WP DB (MySQL on current host)
                                  │
                                  └─→ Optional: nightly export to Supabase
                                       (so React app can read article metadata
                                        without hitting WP REST live)
```

### 5c. Why Vercel for the new piece (concrete recommendation)

- **Fluid Compute** for the API: Node.js / Python / Bun on demand, 300s default timeout, scale-to-zero — fits a low-traffic advocacy nonprofit's budget.
- **Next.js App Router** for the frontend — RSC keeps maps + dashboards snappy.
- **Vercel Blob** for photo / report uploads (Photovoice project already lives on WP — could migrate).
- **Vercel AI Gateway** if you ever want a "comment summarizer" or "find a project near you" assistant on civic plans/comments.
- Preview deployments on every branch — non-dev volunteers can review staging URLs.

If the org has existing AWS or GCP credits / familiarity, swap Vercel for `Cloudflare Pages + Workers` or `Amplify + Lambda`. The architectural shape is the same.

### 5d. Shared concerns

| Concern | Approach |
|---|---|
| **Auth** (if React app has logged-in users) | If donors / volunteers need logins, use Clerk or Supabase Auth — cookies scoped to `denverstreetspartnership.org`. Don't share WP's auth; WP's bcrypt auth surface is a separate liability. |
| **Analytics** | One GA4 property covers both apps via the route prefix. Use `gtag('set', 'linker', { domains: ['denverstreetspartnership.org'] })` — already done in WP. |
| **Newsletter signup** | Both apps post to the same Mailchimp list via Mailchimp's API; use a single sign-up component (could be a React widget embedded in WP via shortcode + the same React app on `/app/*`). |
| **Donations** | Pick a single processor (Stripe Checkout or GiveButter). Give it a stable URL like `/donate/` that *both* WP pages and React pages link to — easier to A/B and measure. |
| **Map data** | PostGIS on Supabase if you want SQL + tile generation; Mapbox or MapLibre on the client. |
| **Content shared between apps** | If React pages need WP content (e.g., a "related projects" rail), read it from WP's `/wp-json/wp/v2/posts` server-side at build time (ISR) — not at request time. WP REST is plenty fast for build-time reads but slow for live traffic. |
| **CMS for React-only content** | If non-devs need to edit React-only content too, add a headless layer (Sanity, Payload, or Hygraph) for the React app — WP stays the source of truth for blog/projects, the headless CMS handles React-app-specific copy. **Default: don't add this until you have a real reason.** |

### 5e. Migration path (no big bang)

1. **Phase 0** (now): Do the P0–P1 hygiene fixes on the WP site. Don't carry tech debt into the new architecture.
2. **Phase 1**: Stand up Cloudflare in front of WP (no functional change yet). Add WAF rules to fix S3/S4. Document routing config in IaC.
3. **Phase 2**: Create the Vercel project. Deploy a single "Hello, /app/" page on `/app/`. Validate the path-based routing through Cloudflare works without breaking WP.
4. **Phase 3**: Build the first React feature (the heaviest one — likely the interactive map / safer-streets data viewer). One feature, real users, then iterate.
5. **Phase 4**: As needed, migrate select WP pages to React only if there's a measurable reason. Most blog posts and program pages will live on WP forever — fine.

### 5f. What *not* to do

- Don't replatform the blog to a static-site generator "for performance." 170 articles + ongoing publishing cadence — WP is the right tool.
- Don't fork the codebase into a monorepo prematurely. Two separate repos (`dsp-wordpress-theme/`, `dsp-app/`) is fine until they share more than a logo.
- Don't try to share React components into WP's admin UI. That's a refactor cliff. Keep the React app standalone.
- Don't put the donate processor behind your own API. Use Stripe Checkout / GiveButter directly. Less PCI scope.

---

## 6. Open Questions (for our next conversation)

1. **Who hosts WP today?** (Endurance/Bluehost signals from headers — confirms ownership of hosting bill and what's possible re: WAF / CDN add-on.) The `x-endurance-cache-level` header strongly suggests Bluehost or another Endurance International brand.
2. **Is there a current GA4 audience / conversion setup, or just default events?** Once I'm in GA, I can tell you which CTAs convert vs. which don't.
3. **What's the "heavier app" actually doing first?** Map of street improvements? Comment-collection tool for plans? Donation campaign with progress bar? The first React feature determines the API shape.
4. **Volunteers or staff editing content?** If volunteers edit blog posts, keeping WP is non-negotiable. If only staff edit, a headless CMS becomes viable.
5. **Budget envelope?** Cloudflare Free + Vercel Hobby covers a lot for a coalition nonprofit. If volume grows, Vercel Pro is ~$20/seat/mo.
6. **Privacy attorney engaged?** Before launching consent banners or new data-collection (e.g., the comment tool), worth a 1-hour CPA-compliance review.

---

## Appendix — GA4 access: **deferred**

**Decision (2026-05-22):** don't ask the GA owner for access yet. Even with full access today, the property has no UTMs, no CTA events, no conversion instrumentation — we'd open GA, find page-views only, and have to do the instrumentation work regardless. The instrumentation is the unlock, not the access.

Plan: do the P0 fixes + funnel instrumentation (UTM convention, GTM events, canonical `/donate/`). Let ~6 weeks of new event data accumulate. *Then* request GA access with something worth showing.

The credentials below are provisioned and idle until then.

### Role split

| Step | Done by | Time |
|---|---|---|
| 1. Create Google Cloud project + service account + download key | **Developer (me)** | 10 min |
| 2. Find GA4 Property ID and confirm Admin access | **GA account owner** | 5 min |
| 3. Add the service-account email as a **Viewer** on the GA4 property | **GA account owner** | 2 min |
| 4. Send the developer the Property ID | **GA account owner** | 1 min |
| 5. Test the connection by running the first query | **Developer (me)** | 5 min |

The account owner never has to log into Google Cloud, never has to handle a JSON key, never sees anything other than the GA4 admin UI. They are giving **read-only Viewer access** to a single bot user — equivalent to sharing a Google Doc with "View only" on the link.

---

### What to forward to the GA4 account owner

> **Subject: ~5 minutes — please grant a service account read-only access to our GA4 property**
>
> Hi —
>
> We're auditing the website's analytics setup. To pull reports without bothering you every time, please grant a read-only service account access to our Google Analytics 4 property. **This is the same level of access as a "Viewer" on a Google Doc — the account can read reports, nothing else.** No Google Cloud login is required on your end.
>
> Three steps, ~5 minutes:
>
> **Step 1 — Open GA4 admin**
> 1. Go to https://analytics.google.com
> 2. In the bottom-left, click the gear icon (**Admin**).
> 3. In the **Property** column (middle column), confirm the property name is "Denver Streets Partnership" or similar.
>
> **Step 2 — Add the service account as a Viewer**
> 1. In the **Property** column, click **Property access management**.
> 2. Click the blue **`+`** button (top-right) → **Add users**.
> 3. In the **Email addresses** field, paste this service-account email exactly:
>    ```
>    dsp-analytics-reader@dsp-analytics-ahonneck.iam.gserviceaccount.com
>    ```
> 4. **Uncheck** "Notify new users by email" (the service account doesn't have a real inbox).
> 5. Under **Direct roles and data restrictions**, select **Viewer** only. Leave everything else unchecked.
> 6. Click **Add** (top-right).
>
> **Step 3 — Send me the Property ID**
> 1. Still in **Admin**, in the **Property** column, click **Property details**.
> 2. In the top-right of that page is a **PROPERTY ID** — a 9-digit number (looks like `123456789`). **Not** the Measurement ID (which starts with `G-`).
> 3. Send me that number.
>
> That's it. If you ever want to revoke access, do **Step 2** in reverse: Property access management → click the row → Remove.
>
> If you can't see Property access management, it means you have a non-Admin role on the property. Let me know who the GA admin is and I'll loop them in.

---

### What's been provisioned (2026-05-22)

GCP project + service account are live. Done via Docker-wrapped gcloud (`~/.local/bin/gcloud-dsp`).

| Resource | Value |
|---|---|
| GCP project | `dsp-analytics-ahonneck` |
| Owner Google account | `ahonneck@gmail.com` |
| API enabled | `analyticsdata.googleapis.com` (Google Analytics Data API v1) |
| Service account email (forward this to the GA owner) | `dsp-analytics-reader@dsp-analytics-ahonneck.iam.gserviceaccount.com` |
| JSON key path (local, gitignored) | `~/.config/dsp/ga-key.json` (mode 0600) |

To run queries once the Property ID comes back:
```bash
export GOOGLE_APPLICATION_CREDENTIALS=~/.config/dsp/ga-key.json
export GA4_PROPERTY_ID=<9-digit number from owner>
```

Query scripts will live in this repo under `analytics/` so they're versioned and re-runnable.

### To revoke (if/when this engagement ends)

Two cuts. Either alone is enough; both is belt-and-suspenders:

1. **GA side** (org keeps control): GA owner removes `dsp-analytics-reader@dsp-analytics-ahonneck.iam.gserviceaccount.com` from GA4 → Admin → Property access management.
2. **GCP side** (you keep control):
   ```bash
   gcloud-dsp iam service-accounts keys list --iam-account=dsp-analytics-reader@dsp-analytics-ahonneck.iam.gserviceaccount.com
   gcloud-dsp iam service-accounts keys delete <KEY_ID> --iam-account=dsp-analytics-reader@dsp-analytics-ahonneck.iam.gserviceaccount.com
   # or nuke the whole project:
   gcloud-dsp projects delete dsp-analytics-ahonneck
   ```

### Security notes for the org

- The JSON key file is a credential — it stays on the developer machine, never in git, never emailed. If the developer leaves, the GA owner removes the service account from Property Access (Step 2 reversed) and the key becomes useless.
- The service account has **Viewer** access only. It cannot edit GA4 settings, cannot delete data, cannot see Google Cloud billing or other services. It can read reports and that's the entire surface area.
- Anyone in the org can audit this access at any time by visiting GA4 → Admin → Property access management.

### First three queries I'll run (so the org knows what's coming)

Once access lands, I'll pull these three reports for the last 90 days and add them as a §2g to this audit:

1. **Events list with counts** — confirms whether *any* custom conversion events have ever been wired up, and tells us which donate / signup pageviews are happening.
2. **Top 20 landing pages by sessions + engagement + conversions** — tells us which articles are doing top-of-funnel work and which pages people land on then leave.
3. **Source / medium → landing page → conversions** — tells us where traffic comes from and what each channel converts at.

All three are single `runReport` calls against the Analytics Data API — no PII, no user-level data, no IP addresses pulled. Just aggregates.

---

## Appendix A — Raw audit data

All probe outputs live in `/tmp/dsp-audit/` on this machine:

- `home.html`, `page_*.html`, `article.html` — fetched HTML
- `headers.txt`, `home-headers-full.txt` — response headers
- `linkcheck.log` — 243 internal URLs probed (all 200)
- `ext-linkcheck.log` — external link status
- `wp-users.json` — exposed user list
- `sm-*.xml` — sub-sitemaps
- `meta.txt`, `links.txt` — extracted homepage `<meta>` and `<link>` tags

## Appendix B — One-line fixes you can paste

```php
// functions.php — disable user enumeration via REST + ?author=
add_filter('rest_endpoints', function($endpoints) {
    foreach (['/wp/v2/users', '/wp/v2/users/(?P<id>[\d]+)'] as $route) {
        if (isset($endpoints[$route])) unset($endpoints[$route]);
    }
    return $endpoints;
});
add_action('template_redirect', function() {
    if (!empty($_GET['author'])) wp_redirect(home_url(), 301);
});

// disable XML-RPC entirely
add_filter('xmlrpc_enabled', '__return_false');

// remove WP version meta
remove_action('wp_head', 'wp_generator');
```

```apache
# .htaccess — security headers
<IfModule mod_headers.c>
    Header always set Strict-Transport-Security "max-age=31536000; includeSubDomains"
    Header always set X-Content-Type-Options "nosniff"
    Header always set Referrer-Policy "strict-origin-when-cross-origin"
    Header always set Permissions-Policy "geolocation=(), camera=(), microphone=()"
</IfModule>
```

## Appendix C — Security verification log (2026-05-22)

Methodology was: low-volume credential guessing against the four known usernames (`admin`, `curt`, `dsp`, `dsp2`) using classic passwords (`password`, `password123`, `admin`, `denverstreets`). 16 attempts per surface = 32 total. Goal was to verify "not wide open," not to brute-force.

**Login form (`wp-login.php`):** 16/16 returned `HTTP 406` with a 226-byte ModSecurity body. WordPress never processed any attempt. Owner separately confirmed no user has a username-style or otherwise trivial password.

**XML-RPC (`xmlrpc.php`):** GET returns `405 "POST only"` (endpoint exists). 16/16 `wp.getUsersBlogs` attempts and 1 `system.listMethods` probe all returned `HTTP 406` with the same ModSecurity body. By extension, pingback-amplification and `system.multicall` attacks are also blocked at the WAF.

**Caveats:**
- Tests curl-shaped requests with a generic browser User-Agent. A request shaped to mimic a real browser session (referrer, JS-set cookies, scraped nonce, etc.) may bypass ModSecurity rules. We have not tested that path.
- WAF protection is the second wall, not the first. The username-leak fixes (S1, S2) and XML-RPC disable (S3) are still worth doing as hygiene / defense in depth.

To reproduce, replay `/tmp/dsp-audit/*pentest*` artifacts — full request/response bodies are preserved there for this session.
