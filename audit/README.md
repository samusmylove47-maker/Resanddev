# EQL Source — independent audit, 31 August 2026

An unsolicited external review of **eqlsource.com** against its direct
EverQuest Legends competitors and the gold-standard fan sites of the wider
MMORPG genre.

| File | What it is |
|---|---|
| `norrath-unmeasured.html` | The brief. Publishable page; also the deliverable artifact. |
| `AUDIT-EVIDENCE.md` | Raw evidence log — every measured figure and its provenance. |

## Headline findings

- **4.7%** of the known item space is in the Index (435 of ~9,360).
- **85.4%** of the homepage payload is inline SVG decoration (206,316 of 241,709 bytes).
- **0** `<img>` elements on the homepage of an MMORPG site.
- **7** direct competitors, none older than the game itself (launched 28 Jul 2026).
- No Discord, no analytics, no return hook, flagship tools hosted off-domain.

## The thesis

EQL Source has the best sourcing discipline and the worst coverage in its field.
Its five-tier sourcing standard has been treated as a reason to publish less; it is
in fact the only mechanism that would let it publish *more* than any rival, honestly.

## Method

All eqlsource.com figures were measured directly against the live site on
31 Aug 2026 — payload from the served HTML, page inventory from `sitemap.xml`,
design tokens from `assets/site.css`. Competitor figures are as published by each
site on that date and are **not** independently verified; re-check before acting.

## Verification performed on the brief itself

- Every text token ≥4.5:1 and every rule ≥2.3:1 / ≥3.05:1 in **both** themes,
  solved numerically (`contrast.py`), not chosen by eye.
- Rendered and inspected in Chromium at 1300px, 880px and mobile widths, in both themes.
- Charts render correctly with animation disabled — no entrance animation that
  could understate a value.
