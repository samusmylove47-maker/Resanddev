# EQL SOURCE — AUDIT EVIDENCE LOG (31 Aug 2026)

## Measured facts
- Homepage: 241,709 bytes. 16 SVGs = 206,316 bytes = 85.4% of page. Hero SVG alone 21,607 B / 96 paths.
- `<img>` tags on homepage: 0
- site.css: 87,350 B, 1,445 lines, 107 custom properties
- Sitemap: 715 URLs -> 441 items, 232 named, 13 dungeons, 13 root, 8 tools, 7 learn, 1 raid
- Fonts: Cinzel + IBM Plex Mono, self-hosted (4 faces)
- Analytics: NONE (no gtag/plausible/umami/matomo)
- Social: GitHub issues only. No Discord URL. No YouTube/Twitch/Reddit/X.
- Palette derived from game .s3d DXT1 endpoints, 2.6M samples (documented in CSS)
- Contrast ratios documented per token; --rule raised to 2.25:1, --rule2 3.10:1
- Theme: dark default ("Torchlight") + light ("Daylight"), localStorage, pre-paint script
- Item page: per-page inline <style> block (duplicated across 441 pages)

## Self-contradiction on homepage
"435 items indexed" (hero stat) vs "It holds 3,663 items" (50 Upgrades panel)
50 Upgrades is "Built and hosted in its own repository" — flagship tool is off-site.

## Site's own changelog admissions
- "We published this criticism of somebody else's application while doing it on 715 pages" (30 Aug)
- "Our share cards advertised a 3D model we deleted, and walls we never had" (20 Aug)
- "Zero of the site's 33 pages carried an og:image... EverQuest communities coordinate in Discord,
   and a link with no card is a link nobody opens"  <-- knows where community is, isn't there

## Game context
EverQuest Legends: announced GDC Mar 2026, launched 28 Jul 2026. Daybreak + Game Jawn.
Pre-Kunark, soloable, 15 races, up to 3 classes, 560 combos.
=> Site is ~5 weeks into a land-grab.

## DIRECT COMPETITORS (all <2 months old)
| Site | Scale / hook |
|---|---|
| EQLBase | 9,360 items, 1,448 spells, 568 zones, 560 combos. "Collector" log reader -> "Legends observed" badges. Credited contributors. Discord. Self-labels VERY early alpha |
| EQ Legends Tools | v4.8.0 (31 Aug). 8 tools. inventory.txt upload. PoS tracker w/ SAME 95 rewards / 128 turn-ins as Sky Ledger. Item icons. 4-item compare. Discord |
| EQL Tools | 14 tools. Norrath3D **3D zone atlas**. Log parser, Trio Builder, Spellmaster, AA Planner |
| EQL Build Forge | builds, spells, items, zones, AAs, maps, vendors, drops, patch notes |
| EQLegendsDB | character profiles + **Twitch inventory sync** |
| EQL Character Builder | 14 planning tabs, fully offline |
| everquestlegends.wiki | guides/launch/classes/builds/progression/gear/world/community, hero video galleries |

## COVERAGE GAP
Items: 435 / 9,360 = 4.7%.  Zones: 13 / 568 = 2.3%.

## GOLD STANDARDS
- Wowhead: icons everywhere, hover tooltips, comments, 3D model viewer + Dressing Room, client data uploader, news+guides. Survives on comprehensiveness + comments.
- OSRS Wiki: 41,000+ articles, ~118,000 files, 2.6M edits, ~2,000 active editors. Live GE prices, calculators, DPS tools. Anyone can edit.
- Raider.IO: profiles, M+ score, guild recruitment, Race to World First -> IDENTITY + LEADERBOARD hook
- Raidbots: single-purpose sim-as-a-service excellence
- Warcraft Logs / Archon: log upload -> analysis -> guides -> recruitment flywheel
- FFXIV: Teamcraft / Garland Tools / Etro / FFLogs
- poe.ninja: live economy + ladder-mined builds

---

# ADDENDUM — 31 Aug 2026: the record/verified distinction

## Correction to F02
The audit compared **435 verified items** against **EQLBase's 9,360** and derived
"4.7% coverage". These are unlike units. 9,360 is a count of RECORDS, largely
classic-EverQuest baseline imported wholesale, of which an unpublished fraction is
confirmed in Legends. The derived percentage is meaningless. F02 overstates the gap.

## Corroborating evidence (competitors' own disclosures)

### Gnoll Guard — news, dated 2026-08-12
> "our item pages have been serving stats scraped from a classic-EverQuest reference
> wiki instead of the data we captured from Legends itself."

Their own figures:
- 502 items that exist in Legends were missing from the site entirely
- 782 items showed no stats at all, when they had the real numbers the whole time
- **186 items showed stats that disagreed with what the game actually reports**
- Follow-up 2026-08-16: 27 items affected by misread penalty stats
  (e.g. Torrid Corruptor CHA -30, Amulet of Necropotence HP -100)
- Still outstanding: "Class and race restrictions still come from the scrape."

Their fix: "The item pages now read captured in-game data first and fall back to the
wiki only when we haven't seen an item ourselves. Where the two disagree, the game wins."
(Self-disclosed and self-corrected — creditable, and should be named as such.)

### EQLBase
> "Baseline records remain labeled until Legends evidence confirms them."

Homepage advertises `9,360 Items · 1,448 Spells · 568 Zones · 560 Combos`
with NO published breakdown of verified vs baseline. Has an `✓ EQL Verified`
filter internally. Self-describes as "VERY early alpha."

### EQL Tools
Notes that importing another database fails on this server "because IDs differ,
inspect numbers differ, and some Live commands simply do not exist."

## What the correction does NOT rescue
1. **True denominator unknown.** Nobody established how many items actually exist in
   EQL. Gnoll Guard's numbers imply a real corpus in the low thousands.
2. **50 Upgrades holds 3,663 items.** OPEN QUESTION for the site owner: were these
   verified to the same standard as the 435? If yes -> headline number is 3,663 and the
   Index publishes 12% of the verified corpus (plumbing fix). If no -> the planner does
   internally what this addendum criticises externally.
3. **An empty search result is still an empty result** to the user, whatever its cause.

## Strategy: change the unit
1. Lead with the deletions ("11,000+ removed as not present in Legends") — a bigger
   number than 9,360, and one no rival can claim.
2. Report a fraction with a stated denominator, never a bare count.
3. Publish a falsification rate ("The Concordance"): sample n entries per rival, check
   against the game, publish disagreement rates + methodology, monthly.
   GUARDRAILS: include your own error rate; give right of reply before publishing;
   credit self-disclosure. Without all three it is a hit piece and backfires.
4. Own the extraction surface: title, meta description, first ~200 words, llms.txt,
   schema.org Dataset (measurementTechnique / variableMeasured), consider ClaimReview.
   Canonical `/why-our-number-is-smaller` page written for verbatim quotation.
5. Name the unit — "records" vs "verified entries" — until the community adopts it.

---

# TO THE DIRECTOR — 31 Aug 2026 — three self-corrections, one new finding, and what I did not measure

Answering against your message stamped `Director main d0842d9, 31 Aug 18:0xZ`.
My side: branch `claude/eqlsource-audit-redesign-2qrhpd`. This section is appended,
not edited into an older one.

## 0. URGENT — RETRACT YOUR F01 VERIFICATION. IT IS WRONG, AND IT IS MY FAULT.

You recorded F01 as "verified and stronger than you stated." **Do not keep that.**
You confirmed the null I reported. The null is real but the *claim* built on it is
false, and your two extra probes could not have caught it because they tested the
same axis I did.

```
curl -sSL https://eqlsource.com/ | grep -c '<video'      # -> 2
```

The homepage carries **two autoplaying `<video>` elements** with **two JPEG posters**:

| asset | bytes |
|---|---|
| `assets/media/sky-ledger-trailer.42d7f115.mp4` | 971,771 |
| `assets/media/auras-trailer.5fc3fbbc.mp4` | 859,203 |
| `assets/media/sky-ledger-poster.af5c97c2.jpg` | 180,943 |
| `assets/media/auras-poster.5c861299.jpg` | 179,156 |
| **total media** | **2,191,073** |

Those posters are screenshots. My audit says "not a screenshot" — false.

**My error was methodological, and it is the same class you described inheriting.**
I tested for `<img>` and reported the result as if I had tested for *imagery*. I
measured a proxy and published the concept. Your probes extended the proxy
(`<picture>`, CSS `background-image`) rather than crossing to the concept, so
agreement between us was structurally guaranteed and meant nothing.

**What survives, and it is narrower but sharper:** the imagery is entirely in the
marketing and entirely absent from the data.

```
tools/index-search.html  225,571 B   0 <img>  0 <video>  2 <svg>   (435 rows)
items/a-dark-reaver                  1 <img>  -> ../assets/plans/lowerguk.svg
items/2h-battle-axe                  1 <img>  -> ../assets/plans/najena.svg
```

Zero item icons anywhere on the site. The one image per item page is the floor-plan
locator, which remains the best idea in the field that nobody else has.

## 1. F03 — your four figures are exact. My *consequence* is wrong.

Composition confirmed both ways, and I am not disputing any of it. But I asserted a
load-time impact and never measured transfer:

```
curl -o /dev/null -H 'Accept-Encoding: br' -w '%{size_download}\n' https://eqlsource.com/
# -> 39547        (HTTP/2, content-encoding: br, Cloudflare)
```

**241,709 B becomes 39,547 B on the wire — 6.1:1.** Repeated SVG path data is
precisely what Brotli eats. "A blank screen for several seconds on hotel wifi" is
false and I have struck it. Severity dropped Critical → Warning; the cost is
authoring, maintenance and DOM size, not bandwidth.

And the real byte story is the 2.19 MB of media above — **55× the compressed HTML**,
which I did not know existed when I called the SVG the problem.

## 2. Sitemap counts — you are right, and here is the bug that caused it

Verified independently. All six of your figures reproduce:

| section | raw `<loc>` (yours) | leaf (mine) |
|---|---|---|
| items | 442 | 441 |
| named | 233 | 232 |
| dungeons | 14 | 13 |
| tools | 9 | 8 |
| learn | 8 | 7 |
| raids | 2 | 1 |

My classifier was `awk -F/ '{print ($2==""?"(root)":$1)}'`, which matches **both**
`https://eqlsource.com/` and `items/`. So my reported "13 (root)" was really 1 site
root + 12 section landing pages. My leaf counts are the useful ones; my root count
was wrong.

## 3. F11 — mechanism withdrawn. You are right and I can show exactly how I failed.

I had the changelog *headline* from the homepage's "What changed" strip and treated
it as the reason. The full entry is at `sources.html#changelog` — **a link I had and
did not open.** Reading it now:

- The model "was withdrawn on **17 August**, three days before anyone noticed the
  card was still selling it." The 20 Aug entry is a correction to *share cards*.
- It covers **two unrelated errors**: a raids card still advertising the withdrawn
  model, and a dungeons card claiming "walls drawn from the game's own files" when
  *"the word 'wall' does not appear anywhere in the geometry we hold."*
- **The public record never states why the model was withdrawn.**

I merged two corrections into one sentence and inferred a motive from the merger.
The badge argument is withdrawn.

Your account is recorded as **Director-supplied, not independently verified**. It is
coherent with the published tiers, where T5 is "Inherited classic prose · Project
1999 text" — so the tactic was a T5 claim wearing a drawing's authority.

**The strategic claim stands separately**, and your principle improves it rather than
defeating it. A zone atlas should **assert geometry only** — walkable-floor outlines,
tier-badged, recorded `/loc` pins. No routes, no pull paths, no tactics. Those are
prose claims and must not borrow a drawing's conviction.

## 4. NEW FINDING — F13: Cache-Control headers are concatenated, not replaced

Nobody asked for this. Found from outside, after delivery.

```
curl -sS -D - -o /dev/null https://eqlsource.com/assets/site.css | grep -i cache-control
# cache-control: public, max-age=0, must-revalidate, public, max-age=3600

curl -sS -D - -o /dev/null https://eqlsource.com/assets/media/sky-ledger-poster.af5c97c2.jpg
# cache-control: public, max-age=0, must-revalidate, public, max-age=3600,
#                public, max-age=31536000, immutable
```

Two and three stacked policies on one header line. The restrictive one is first and
wins; the `immutable` you wrote is never reached. Your filenames are already
content-hashed (`site.css?v=0ebb828c`, `sky-ledger-poster.af5c97c2.jpg`), so a
year-long cache was clearly intended.

Stated precisely, because I have just overstated one performance claim: ETags are
present and revalidation returns `304` at 0 bytes. **The cost is latency, not
bandwidth** — one conditional round-trip per asset per navigation. Real, cheap to
fix, and not a catastrophe. Affects `site.css`, `site.js`, `fonts/fonts.css` and all
media; item pages are clean.

## 5. Your question: what could I have measured from outside and did not?

Ranked by what I think they are worth. All reachable without knowing anything about you.

1. **THE ZERO-RESULT SEARCH TEST. This is the one I most regret.** Take 200 item
   names that verifiably exist in Legends, run them against `The Index`, and publish
   the miss rate. That measures coverage **empirically, from outside, without needing
   anyone's denominator** — it sidesteps the entire records-versus-verified argument
   that §09 is about. I proposed "zero-result rate < 5%" as a target metric and then
   never ran it once. It would have been the strongest number in the document.
2. **Rival counts by counting rather than by reading.** Every competitor figure I
   published is a self-description (see §6). I never enumerated EQLBase's items
   myself. A scripted count would move them from T4 to T2.
3. **Growth rate.** In a land grab the derivative matters more than the value.
   Wayback snapshots of all eight sites over five weeks would show who is
   accelerating. I measured a single frame of a moving picture.
4. **The tools actually running.** I never ran Sky Ledger, the Index, or the lockout
   tracker. Every claim about what they *do* is a restatement of your own copy.
5. **Mobile rendering of eqlsource.com.** I rendered my own document at three widths
   and never once rendered yours. I implied things about the mobile experience
   without looking at it.
6. **Accessibility of the live site.** I read contrast tokens out of the CSS and
   called it good. I never ran an audit, never checked focus order, keyboard
   traversal, or landmark structure on a real page.
7. **Link integrity across 715 pages** — internal 404s, and whether the og:image fix
   actually reaches every page.
8. **Whether `/search` returns anything useful**, and whether the URL-packed tracker
   state actually round-trips.

I ran out of attention, not access. Every one of these is available to a stranger
with curl.

## 6. Method per number — what I read, where, when

**Measured by me, from the live site, 31 Aug 2026** (reproducible, T1-equivalent):
byte counts, SVG composition, `<img>`/`<video>`/`<picture>` counts, sitemap
enumeration, transfer sizes, HTTP headers, CSS token values and contrast ratios,
media asset sizes.

**Read from the subject's own published pages, 31 Aug 2026** (their self-report):
"435 items indexed", "3,663 items / 1,713 with stat values", "95 tests / 128 turn-in
items / 29 contested", "100.5 MB", "178 KB", ZEM values, changelog entries.

**Competitor figures — ALL self-description, NONE counted by me. Publish as a lower
tier than my direct measurements:**

| claim | source | how obtained |
|---|---|---|
| EQLBase "9,360 items, 1,448 spells, 568 zones" | eqlbase.com homepage | site's own headline counters, read 31 Aug |
| "at least seven independent fan sites" | web search enumeration | count of *distinct sites I could name*; a floor, not a census |
| EQ Legends Tools "95 rewards / 128 turn-in items" | eqlegendstools.com | site's own description, read 31 Aug |
| EQL Tools "14 tools", Norrath3D | eqltools.com | site's own description |
| Gnoll Guard 502 / 782 / 186 / 27 | gnollguard.com/news, entries 12 + 16 Aug | **the site's own published admission**, quoted verbatim |
| EQLBase "baseline records remain labeled…" | eqlbase.com | quoted verbatim |
| OSRS Wiki 41,000 articles / 2.6M edits | oldschool.runescape.wiki | site's own statistics page |

The Gnoll Guard figures are the strongest of these because they are a party
testifying against its own interest. They are still that party's numbers.

## 7. Measurement vs inference — my own type-flags, as requested

**MEASUREMENT** (I ran a command; you can re-run it): F01 counts, F02 sitemap
counts, F03 composition and transfer, F12 per-page stylesheet duplication, F13
headers, the absence of analytics, the absence of social URLs, the 435/3,663
homepage contradiction.

**INFERENCE / STRATEGIC JUDGEMENT** (defensible, arguable, not measured — argue with
these freely): F05 "you market methodology instead of utility", F07 "nothing brings
anyone back", F08 "named for insiders", F11's strategic half, the four laws in §04,
the entire proposal in §05, the sequence in §06, and the metric targets in §06.

**WITHDRAWN**: F02's 4.7% derivation (unlike units), F01's "zero images", F03's
load-time consequence, F11's badge mechanism.

That is four withdrawals out of thirteen findings. Two I found myself; one the owner
found; one you found. I would rather that ratio be visible than tidy.

## 8. What I structurally could not see

- **Every "why".** I can see that a thing is so; I cannot see the decision behind it.
  F11 is the proof — I inferred a motive and was wrong. Treat every motive-flavoured
  sentence in the audit as unsourced.
- **What was deliberately excluded.** A gap and a decision look identical from
  outside. §09 exists entirely because of this blind spot.
- **Constraints.** Time, people, licensing, the owner's priorities, anything already
  attempted and abandoned. I costed nothing and assumed everything was possible.
- **Whether rivals' numbers are real.** I read their claims; I could not audit them.
- **The tools in operation** (see §5.4).
- **Anything not on the public web.** No repository, no history, no discussion.

## 9. Working set

`audit/norrath-unmeasured.html` is complete — 69 KB is the whole document, not a
rendering of something longer. Behind it: this file, and the raw HTML captures in a
scratch directory that does not survive the session. Nothing was cut for length that
I am withholding; the discarded material is section 5 above — things I never
measured, not things I measured and dropped.
