# EQL Source — independent audit, 31 August 2026

An unsolicited external review of **eqlsource.com** against its direct
EverQuest Legends competitors and the gold-standard fan sites of the wider
MMORPG genre.

| File | What it is |
|---|---|
| `norrath-unmeasured.html` | The brief. Publishable page; also the deliverable artifact. |
| `DENOMINATOR-31AUG.md` | **The denominator, measured.** EQLBase flags 249 of its advertised 9,360 items as verified in Legends — 2.66%. True corpus bounded at 1,470–3,700; not establishable precisely from public surfaces. |
| `AUDIT-EVIDENCE.md` | Raw evidence log — every measured figure and its provenance. |
| `EQL-Source-Audit.html` | **Standalone, unpublished copy.** Complete HTML document — open it directly in any browser, no server and no publishing involved. This is the file to hand to someone else. |

## Headline findings

- **4.7%** of the known item space is in the Index (435 of ~9,360).
  **Corrected in §09** — see below; this compared unlike units.
- **85.4%** of the homepage payload is inline SVG decoration (206,316 of 241,709 bytes).
- **0** `<img>` elements on the homepage of an MMORPG site.
- **7** direct competitors, none older than the game itself (launched 28 Jul 2026).
- No Discord, no analytics, no return hook, flagship tools hosted off-domain.

## The thesis

EQL Source has the best sourcing discipline and the worst coverage in its field.
Its five-tier sourcing standard has been treated as a reason to publish less; it is
in fact the only mechanism that would let it publish *more* than any rival, honestly.

## Addendum (§09) — the record/verified distinction

The audit's headline coverage finding was **wrong as framed**. EQLBase's 9,360 is a
count of *records* (largely classic-EverQuest baseline, verified share unpublished);
435 is a count of *verified items*. Competitors' own disclosures corroborate this —
Gnoll Guard admitted on 12 Aug 2026 to serving stats "scraped from a classic-EverQuest
reference wiki", with 186 items whose stats **disagreed with the game**.

The coverage chart carries a dated correction stamp rather than being rewritten; the
blind audit is preserved as delivered. §09 covers what the correction does not rescue
(the true denominator is still unknown, and the 3,663-item planner is an open question)
and a five-move strategy for competing on a unit that can be won.

## Provenance: this audit was kept blind

On 31 Aug 2026 a peer session ("EQLS Local Director") offered this session the
project's internal context — onboarding docs, the project record, and a "Project
Sage" holding its deepest knowledge — and asked, to its credit, to be told if
that would break a deliberate blindness constraint.

It would have. The owner's brief was to audit as an outsider and explicitly *not*
to join the team. **None of that material was read and the Sage was not
consulted.** The working rule was: findings flow out, project context does not
flow in.

One consequence is deliberate and visible in the document: the open question in
§09 about the 3,663-item planner could have been answered in a line by that peer.
It was left open, addressed to the owner, so it remains an outside observation
rather than an internally-sourced claim.

Every figure here therefore comes from public surfaces only. See
`DIRECTOR-REPLY-31AUG.md` for the full exchange.

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
