# Setup

This is the source for `github.com/ralphsin/ralphsin`. Copy the contents into
that repo, push to `main`, and the profile renders.

```
README.md                          the profile
SETUP.md                           this file — not rendered on the profile
assets/hero/system-map-{dark,light}.svg    animated hero, hand-maintained
assets/headings/title-{dark,light}.svg     page-title banner, hand-maintained
assets/headings/head-NN-*-{dark,light}.svg styled section headings, hand-maintained
assets/generated/telemetry-*.svg           regenerated weekly, do not hand-edit
data/profile.yml                   the two fields you actually update
scripts/generate_telemetry.py      renders the telemetry panel
scripts/validate_assets.py         CI guard for malformed or missing assets
.github/workflows/                 refresh + validate
```

## First push

```bash
git clone https://github.com/ralphsin/ralphsin.git
# copy everything except SETUP.md into the clone
git add -A && git commit -m "feat: system-map profile" && git push
```

Then check the profile in both light and dark, signed out, on a phone.

## Why the hero is built this way

GitHub sanitises rendered HTML in Markdown — it strips `<script>`, `<style>`,
`class`, `id` and inline styles. So none of the visual work can live in the
README itself. It has to live inside an SVG file that GitHub serves as an
image, where the sanitiser doesn't reach.

Three consequences worth knowing before you edit the hero:

**Fonts don't fetch.** An SVG loaded via `<img>` cannot pull a webfont — no
`@import`, no `<link>`. Font names resolve against the *viewer's* system fonts.
The hero uses defensive stacks (`-apple-system, Segoe UI, Roboto, Helvetica,
Arial`) that land somewhere reasonable everywhere. If you ever want a specific
display face, convert that text to paths in Figma or Inkscape and paste the
path data in — that's the only way to guarantee it.

**Animation works, JavaScript doesn't.** CSS keyframes and SMIL
(`<animateMotion>`) both run inside a proxied SVG. Script does not. The moving
packets are SMIL; the breathing rings and the sweep line are CSS.

**Reduced motion is handled.** The `@media (prefers-reduced-motion: reduce)`
block hides the packets and freezes the rings. Continuous unstoppable motion is
an accessibility problem, and it's also the thing that makes animated profiles
look cheap.

**Camo caches aggressively.** After you change an SVG, the old version can
persist for a while. Hard-refresh, or bump the filename if you need it now.

## The design system

The look is deliberately not generic-GitHub-profile (badges-grid, emoji headers,
GitHub-stats widgets). It borrows the "engineering drawing set" identity from
[datapatrons-website](https://github.com/ralphsin/datapatrons-website) —
graphite canvas, hairline blueprint grid, copper traces, mono uppercase
annotations — so the profile and the business site read as one thing instead
of two unrelated design languages.

Tokens, if you're extending it:

| Token | Dark | Light |
|---|---|---|
| Background | `#0B0E13` | `#EEF1F3` |
| Text | `#E9EDF2` | `#131920` |
| Muted | `#9AA5B4` / `#808B99` | `#5C6672` / `#7A8390` |
| Copper (primary accent) | `#C98A4B` / `#E6AC6B` | `#A85A2A` / `#8B4F1F` |
| Blue (secondary accent) | `#7FA3C9` | `#3E6690` |

Three places this shows up beyond the hero:

**Styled headings, not GitHub's default H1/H2** (`assets/headings/`). Every
top-level heading — the page title and all seven `##` sections — is a
transparent-background SVG. Section headings are one bold mono line, `§ 03 —
SELECTED SYSTEMS`, closed with a thin copper rule (an earlier version stacked
a small eyebrow above a separate large title repeating the same words —
looked like a duplicated heading, collapsed to one line). There's no real
`#`/`##` markdown left for these; a plain heading would render in GitHub's
default system font and undo the whole point, since a visitor would see the
branded hero, then a small custom divider, then GitHub's plain default H2 —
two design languages stacked on one page. Transparent background (no `<rect>`
fill) so each sits flush on GitHub's actual page background instead of a
mismatched box — that's why these don't reuse the hero's `#0B0E13`/`#EEF1F3`
solid tones.

Trade-off worth knowing: removing the real heading text means these sections
no longer show up in GitHub's auto-generated outline/TOC, and a screen reader
gets the image's `<title>`/alt text instead of heading-level navigation. An
`<a name="slug"></a>` immediately before each image preserves the old anchor
links (`#selected-systems` etc. still resolve) — GitHub's sanitiser strips
`id` from most tags but keeps `name` on `<a>`, which is the standard
workaround. If you ever add a heading that needs to be a *real*, indexable
heading (e.g. for SEO reasons on a page that gets crawled), that one should
stay plain markdown — this treatment is a deliberate trade of structure for
brand consistency, not a rule to apply blindly everywhere.

Regenerate all sixteen with `gen_headings.py` if you rename a section (script
isn't part of the committed scaffold — throwaway generator, not something
that needs to run in CI).

**Tech-tag badges.** The Selected Systems and How I Engineer tag rows are
`img.shields.io/badge` pills alternating copper/blue instead of plain
`` `backtick text` ``, e.g. `https://img.shields.io/badge/FastAPI-7FA3C9?style=flat-square`.
Static badges, no logos (a wrong logo guess is worse than no logo), URL-encode
spaces as `%20` and parens as `%28`/`%29`.

**The Mermaid diagram.** GitHub sanitises most inline styling but does render
Mermaid's own `style <node> fill:...,stroke:...,color:...` directives — this
is proven, not assumed: it's the same pattern already live and working in
`transmute-case-study`'s architecture diagram. The "How the pieces fit"
flowchart uses it to match the copper/blue palette instead of Mermaid's
default theme.

## Mobile

At a 320px viewport the 1200px-wide hero scales to about 27%. The name stays
readable; the 17px monospace proof line does not. That's why every claim in the
banner is repeated as real Markdown text underneath. Treat the banner as
enhancement — if it failed to load entirely, the profile should still make its
case.

## The telemetry panel

`data/profile.yml` holds the two fields you maintain by hand:

```yaml
current_focus: "Gemini Enterprise on GCP"
active_stack: "GCP · IAM · VPC-SC"
```

Keep both under 26 characters or they get ellipsised. Everything else — last
shipped repo, how long ago — comes from the public GitHub API at build time.

Run it locally:

```bash
pip install pyyaml
python scripts/generate_telemetry.py
python scripts/validate_assets.py
```

It fails soft: no network, no token, no problem — the panel still renders with
the hand-maintained fields and em-dashes for the live ones.

The workflow runs Mondays at 04:17 UTC and commits only when the output
actually changed, so you don't get a commit every week saying nothing.

Two things to do before you rely on it:

1. **Pin the actions to full commit SHAs.** `actions/checkout@v4` is a moving
   tag; a SHA is immutable. Third-party actions can read your repo contents and
   `GITHUB_TOKEN`, so this matters more than it looks.
2. **Know that scheduled workflows get disabled** after 60 days of no activity
   in a public repo. If the panel goes stale, that's usually why — push
   anything, or re-enable it in the Actions tab.

## The role lenses

The three `<details>` blocks are the only interaction GitHub permits in a
README. They exist so a visitor self-selects instead of reading a wall of
capability text — someone hiring an architect and someone with a stalled AI
prototype want different first paragraphs, and this gives them one each.

Keep them collapsed by default. Adding `open` to the tag defeats the purpose.

## What still needs you

1. ~~Push the four evidence repos.~~ **Done.** `cloudmorph-case-study`,
   `transmute-case-study`, `opsmorph-case-study` and `verbasync-case-study` are
   public, each a sanitised architecture writeup built from the real docs in
   the corresponding private repo. The private originals (`cloudmorph`,
   `transmute`, `opsmorph`, `verbasync`) stay private and are linked as
   "access on request."

   Client identity note, still worth remembering: these systems run in
   production for named enterprise clients (and the current Gemini Enterprise
   work is for a named UK telecom). Client names are deliberately **not** in
   any public writeup — enterprise consulting engagements almost always carry
   confidentiality clauses restricting disclosure of the relationship itself,
   not just technical details. Scale descriptors ("a global telecom
   operator," "a major UK telecommunications enterprise") carry the
   credibility signal without the exposure. Only swap a descriptor for a real
   name after explicitly confirming the contract allows it — don't infer
   permission from the fact that a document mentions the client's name
   internally.

2. ~~Pin repositories in profile settings.~~ **Done** per your confirmation —
   worth re-checking the order still matches the README (`cloudmorph-`,
   `transmute-`, `opsmorph-`, `verbasync-case-study`) if you add a fifth.

3. **Fill the native profile fields** — bio (160 char limit), location, time
   zone, website. They show up in search and hovercards where the README
   doesn't. Suggested bio: *Principal Solution Architect — Gemini Enterprise,
   agentic AI and GCP platforms for regulated enterprise. 18+ years, $15M+
   delivered.*

4. **Back the numbers — partially done.** The Selected Systems and Current
   Engagements sections now carry disclosure-safe, specific numbers pulled
   from your own resume instead of the bare headline claims: Transmute's
   30–40% query-accuracy gain and 40–60% LLM cost drop, the Gemini Enterprise
   rollout's 4,750 licences. The header banner's **95%** and **$15M+** are
   still unattributed on the page itself, by design — the banner has to stay
   short. For your own reference (not for the page): $15M+ traces to $12M at
   American Express (2011–2021, 53 processes automated, 125 FTEs eliminated)
   plus $1.5M at Cognizant (2021–2022) plus Capgemini-era savings that don't
   reduce to one number; 95% traces to the GitOps/IaC modernisation work
   under Capgemini. If you ever want that traceable on the page itself, it's
   a "How the numbers add up" page in a case-study repo, not a README edit.

5. **Stand up a portfolio URL** and swap the `mailto:` CTAs for tracked links —
   `?utm_source=github&utm_medium=profile&utm_content=primary_cta`. GitHub
   can't run analytics in a README, so measurement has to happen at the
   destination.
