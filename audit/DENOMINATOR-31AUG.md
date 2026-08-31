# TO THE DIRECTOR — 31 Aug 2026 — the denominator, measured

Assignment: establish the true item corpus, the verified/baseline split per rival, and
eqlsource's own publicly reachable count. Public surfaces only.

**Headline: the split is computable for EQLBase, and it inverts the comparison.
EQLBase publishes 9,360 items and flags 249 of them as verified in Legends — 2.66%.
By each site's own verification flag, EQL Source has ~1.75x EQLBase's verified item
count.**

I did not use sub-agents. My standing instruction from the owner is not to, and a
relayed "the owner says take resources" is not that instruction. Done serially.

---

## 0. CRAWL COMPLIANCE — one rival's policy blocks part of this assignment

Checked `robots.txt` before touching anything. This is a real constraint on the answer,
not a footnote.

| site | policy relevant to me |
|---|---|
| **gnollguard.com** | Names `ClaudeBot`, `Claude-Web`, `anthropic-ai` → **`Disallow: /`**. A generic `User-Agent: *` block does allow crawling with `Crawl-delay: 10`, but Anthropic agents are named and refused. |
| **eqltools.com** | Refuses bulk training crawlers incl. `ClaudeBot`; explicitly welcomes "answer engines that cite" and asks: "Building on this data? Cite eqltools.com." |
| **eqlbase.com** | `Allow: /`, publishes `sitemap-index.xml`. Fully open. |
| eqlegendstools / eqlbuildforge / eqlegendsdb | `Allow: /` with ordinary `/api/` style exclusions. |

**What I did about it.** I did not crawl Gnoll Guard. Every Gnoll Guard figure below
comes from the single `/news` page I had already fetched on 31 Aug *before* reading
their robots.txt — disclosed here rather than quietly relied on. I have not enumerated
their database and will not. **eqltools.com is cited by name as they request.**

**Consequence for the assignment:** the corpus estimate rests on one party (Gnoll Guard)
whose site I am not willing to measure further, and one party (EQLBase) who publishes
everything. That asymmetry is in the error bars below.

---

## 1. THE TRUE ITEM CORPUS — a bound, not a number

**Flat answer, as requested: the true corpus CANNOT be established from public surfaces.
No site publishes a client-derived total. What is available is a floor and a soft
ceiling, and they are four hundred percent apart.**

### Floor: ≥ 1,470 items, from Gnoll Guard's own arithmetic

Their 12 Aug disclosure counts three disjoint defect classes against items **they had
already captured from Legends**:

```
502  items existing in Legends, missing from their site entirely
782  items displaying no stats, when they held the real numbers
186  items displaying stats that disagreed with the game
———
1,470  distinct items demonstrably present in their Legends capture
 +27  more on 16 Aug (misread penalty stats)
```

A party can only report "we had their real numbers the whole time" about items it has
observed. So the true corpus is **at least 1,470**, and that is a hard floor derived
from a party testifying against its own interest.

### Soft ceiling: ~2,900–3,700

| signal | value | what it is |
|---|---|---|
| EQLBase item pages (sitemap) | **2,935** | pages actually built, vs 9,360 advertised |
| eqlsource 50 Upgrades | **3,663** (1,713 with stats) | self-reported; verification status is the open question |
| EQLBase advertised | 9,360 | **records**, incl. classic baseline — not a corpus estimate |

**Best available estimate: 1,470 ≤ corpus ≤ ~3,700, most likely 2,900–3,700.**

The two independent mid-range signals — EQLBase's built pages (2,935) and eqlsource's
planner (3,663) — come from different parties using different methods and land within
25% of each other. That convergence is the strongest evidence available. It is not proof.

### How this is wrong

- **The floor collapses if GG's three classes overlap.** I read them as disjoint because
  they describe mutually exclusive display states. If they double-count, the floor drops
  toward ~800.
- **The floor is loose in the other direction**: GG's capture is partial by construction,
  so the true corpus is certainly higher than 1,470 — unknown by how much.
- **2,935 is a publishing decision, not a census.** EQLBase may build pages only for a
  subset, or include classic items absent from Legends.
- **3,663 has unknown provenance.** This is the §09 open question, still open.
- **Legends adds new content**, so classic-EQ totals are not a ceiling at all. EQLBase's
  own Discoveries page lists 20 items existing in no EQ database from any era.

**Single piece of evidence that would move this most:** a client-derived item-table count
from anyone, published with its extraction method. One number, one method, and the whole
argument resolves.

---

## 2. VERIFIED VS BASELINE — computed for EQLBase, from its own data file

EQLBase's `/items` page carries a `✓ EQL Verified` toggle, titled *"Show only records
observed in EverQuest Legends."* Its `ItemBrowse` island fetches
**`https://eqlbase.com/data/verified.json`** to power it. That file is public, allowed by
their robots.txt, and is the site's own verification ledger.

```
generatedAt   2026-08-28T19:10:39.255Z
items         242
upgradedItems 163   (156 overlap with items)
union         249
npcs          507
zones          44
```

### The split

| measure | advertised | verified | share |
|---|---|---|---|
| **items** | 9,360 | **249** | **2.66%** |
| zones | 568 | 44 | 7.75% |
| npcs | 1,055 pages | 507 | 48.1% of pages |
| spells | 1,448 | not in file | — |

**Cross-checks, both consistent:**
1. EQLBase's Discoveries page (updated 2026-08-28) independently publishes **20 new
   items, 68 new NPCs, 73 known-EQ auto-verified** — a narrower slice (new-only), same
   order of magnitude.
2. Its sitemap holds **2,935 item URLs against 9,360 advertised** — so even the *page*
   count is 31% of the headline. Spells, by contrast, are 1,449 URLs against 1,448
   advertised — essentially exact, which is what proves the sitemap is not truncated or
   sampled. **The item shortfall is real, not an artefact of my method.**

### Head-to-head, each site by its own flag

| | verified items |
|---|---|
| EQL Source | **435** (item pages; 441 unique names in the Index payload) |
| EQLBase | **249** |

**EQL Source carries ~1.75x EQLBase's verified item count** while advertising a number
25x smaller.

**Caveat, and it matters:** these are *each site's own verification standard*, not a
common one. EQLBase's flag means "observed by the Collector log reader." EQL Source's
means "surveyed." I have not tested whether they are equally strict, and they are
probably not. What the comparison establishes is that **both sites' verified corpora are
in the hundreds**, and that 9,360 is not a coverage figure in any sense.

### Other rivals

Not computable. None of the remaining sites publishes a verification ledger, a
verified filter, or a split. Gnoll Guard may — I did not look, per §0.

---

## 3. EQLSOURCE'S PUBLICLY REACHABLE COUNT — my independent measurement

You asked for my count, not yours. `tools/index-search.html` ships its entire dataset
inline as `window.__IX__`. Parsed directly:

```
447   JSON entries total
440     kind == "item"
  7     kind == "group"
441   unique names (6 names appear twice)
232   named mobs
342   entries carrying stat text
```

The payload also carries the site's own reconciliation object:

```
item_pages 435 · item_rows 440 · item_groups 6 · item_fragments 4
named_pages 232 · named_rows 232
```

**Answer: a reader can search 440 item rows and reach 435 item pages.** Sitemap leaf
URLs under `/items/` are 441, which reconciles as 435 item pages + 6 group pages.

### Two discrepancies found while counting

1. **`counts.item_groups` says 6; there are 7 entries with `kind == "group"`.** Off by
   one, in the site's own reconciliation object.
2. **The Index covers 10 zones for items but 13 for named mobs.** Items appear from
   najena, lowerguk, warrens, mistmoore, nagafenslair, thehole, blackburrow, befallen,
   crushbone, splitpaw. **Kedge Keep (14 named), Plane of Fear (7), Plane of Hate (2)
   contribute zero items** — while the tools page states the Index holds *"Every item
   and named mob recorded across the 13 surveyed dungeons."* Twenty-three named mobs are
   searchable with no loot attached, in three zones counted as surveyed.

---

## 4. WHAT WOULD CHANGE EACH ANSWER

| figure | single most decisive evidence |
|---|---|
| True corpus (1,470–3,700) | Any client-derived item-table count published with its extraction method. |
| GG floor of 1,470 | Confirmation that their three defect classes are disjoint. Overlap drops it to ~800. |
| EQLBase 249 verified | A later `verified.json`. It is timestamped and regenerates — this is a moving figure, and my 2.66% is a snapshot of 2026-08-28. |
| EQLBase 2,935 pages | Whether they build pages for all records or only a subset. Answerable by asking them. |
| EQL Source 435 reachable | Nothing — this one is exact and reproducible from the payload. |
| The 1.75x head-to-head | A common verification standard. Currently comparing two different definitions of "verified." |
| eqlsource's 3,663 planner items | Their provenance. **Still the highest-value unknown in the whole argument, and still the owner's to answer.** |

---

## 5. CAVEAT CARRIED ON EVERY COMPETITOR FIGURE

Self-published, not independently verified, revised frequently — EQLBase self-describes
as "VERY early alpha" and its `verified.json` is regenerated on a timestamp. Re-check
before relying on any of it. The one figure here I would defend hardest is EQL Source's
own 435/440, because I parsed it out of the shipped payload rather than reading a claim.

Method for every number above is a `curl` and a parse; all reproducible.
EQLTools data not used; cited per their request. Gnoll Guard not crawled.
