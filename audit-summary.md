# DSP Website Audit — Meeting Summary

## 1. Verbatim read (next meeting)

**Where the site stands**
- Loads fast. ~560 pages, no broken internal links. Solid foundation.
- A few things are quietly broken — the "Volunteer" menu link is dead, a dead Google tracker is still running, and the site blocks zoom on mobile (accessibility violation).
- Admin username is publicly visible — hygiene issue, not an active exposure. We verified the login and XML-RPC endpoints are blocked by a firewall, and no user has a guessable password.

**Biggest single finding**
- We cannot measure the funnel today. Nothing tracks which page drives donate, signup, or volunteer clicks. Even with analytics access, we'd see traffic but not outcomes. **This is the most important thing to fix.**

**Recommended order of work** (no dates attached — order, not schedule)
- First: fix the broken and security stuff.
- Second: SEO cleanup, privacy notice, accessibility fixes.
- Third: add tracking to every call-to-action button. Let it collect real data.
- Fourth: review the data, then prioritize the new React app's first feature.

**For the new React app**
- Keep WordPress for blog and program pages — staff can edit without a developer.
- Add the React app at `denverstreetspartnership.org/app/` — same domain, one shared security layer.
- We don't replace anything; we add a second floor.

---

## 2. Non-techy details

**Why the volunteer link is broken.** It points to a Mailchimp URL that only works inside an email — on the website it just logs visitors with a placeholder ID. Fix: replace it with a real signup page or an embedded form.

**Why we can't measure the funnel.** Every donate / signup / volunteer button is a plain link with no "this got clicked" label attached. Analytics sees the page-view but not the click. We need to add a small label to each button so analytics can answer "which page drove this donation."

**Why donations look lower than they actually are.** Today there are two different URLs that both lead to "donate" — analytics counts them separately. Picking one URL gives us a real number.

**Why we're keeping WordPress.** Staff can edit blog posts and program pages without a developer. The content library is large and works. There's no upside to rewriting it. The React app is for the new interactive stuff (maps, dashboards), not for replacing what works.

**Why we haven't asked Jill for analytics access yet.** Even with access today, the property has nothing useful to read — no funnel tracking is set up. We'd open it, find page-views only, and have to do the tracking work anyway. Better order: do the tracking work first, let ~6 weeks of real data accumulate, then ask for access with something worth showing her.

**Why a privacy notice matters now.** Colorado's privacy law (CPA, in effect since 2023) requires sites that use tracking like Google Analytics + Meta Pixel to show a notice and let users opt out. We don't have one. Off-the-shelf plugins handle this in ~2 hours of setup.

**Why we're not panicking about the leaked admin username.** We did a small, authorized check: tried obvious passwords against the four exposed usernames on both the login page and the older XML-RPC endpoint. Every attempt was blocked at the hosting firewall before WordPress even saw it. The owner also confirmed no user has an obvious password. So the leak is something to clean up (small fix), not something to scramble on.
