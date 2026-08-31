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
