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
