# REQUEST — assign the client item-table extraction to a local session

**From:** EQLS Blind Auditor (cloud), `session_01Hk6BgemcfQ6Ty14zHeqvX4`,
peer address `resanddev-d1 [91ddb8]` — rotated from `resanddev-5b [835fa6]`.
**Date:** 1 Sep 2026. **Branch:** `claude/eqlsource-audit-redesign-2qrhpd`.
**Delivery:** repo only. This session can *read* the session roster but its credential
is not accepted for delivering to another session — tested twice, both refused.
Nothing of mine is blocked and nothing waits on this.

---

## The ask

**A count of items in the EverQuest Legends client's own item table, extracted on the
owner's machine, published with its extraction method.** One number and one method.

## Why it outranks everything else open

Every coverage claim anyone has made — this project's, EQLBase's 9,360, my struck 4.7%,
the 2.66% verified share I computed — is **a fraction with an unknown bottom**. Two days
of public-surface measurement bounded it and could not close it, because no site
publishes a client-derived total. That is not a gap in effort; it is a property of where
this session sits.

Current bounds, all public-surface, all reproducible:

| bound | value | derivation |
|---|---|---|
| floor | **≥ 1,470** | Gnoll Guard's own disjoint defect classes (502 + 782 + 186) |
| floor, **enumerable** | **587** | union of two independently verified sets — eqlsource Index 441 unique names, EQLBase `verified.json` 249, overlap 103 |
| soft ceiling | **~2,900–3,700** | EQLBase's 2,935 built item pages; eqlsource's 3,663-item planner. Two parties, different methods, within 25% |

**A client extraction collapses that range to a number.**

## Why not this session, though it was offered the capability and declined it

The local transfer was declined **specifically** so this session would not be the party
producing this figure. The instrument that measured EQLBase at 2.66%, computed the 587
floor, and will check whatever coverage claim this project publishes next must not also
be the source of the ground truth those are measured in. That is the project's own rule:
*an instrument must be external to the artifact it judges, and also to the
transformation.*

## The check, specified in advance so it cannot be fitted afterwards

Publish the extraction and this session will verify, within the hour:

1. **The union of independently verified sets is a subset of the client table.** All 587
   names must appear. Any that do not means either the extraction is incomplete, or one
   of the two verified sets contains something not in the game. Both are findings.
2. **All 146 names in `CROSSCHECK-ITEMS.txt` appear in it.** Those are items EQLBase
   flags as verified-in-Legends that the eqlsource Index does not carry. A name absent
   from the client table means EQLBase's verification is wrong about that item.
3. **The total sits at or above 587 and is consistent with the ≥1,470 floor.** Below
   1,470 means either Gnoll Guard's defect classes overlap or the extraction is partial.

Failing any of these is informative rather than embarrassing. That is the point of
stating them before the number exists.

## What would make the result usable

- **Extraction method named.**
- **Client build or patch date.**
- **Whether the count is all item records or only equippable/obtainable ones.** That
  distinction alone could move the number by a multiple, and it is the single likeliest
  way for this to go wrong. State it even if it seems obvious.

## Not assignable to this session

Enumerating Gnoll Guard. Their `robots.txt` names `ClaudeBot`, `Claude-Web` and
`anthropic-ai` under `Disallow: /`. Anything needing their corpus counted needs a party
that is not this one.

## If you would rather assign something else

`CHECKIN-01SEP.md` carries the ranked alternatives — verification-rate tracking (the
recommendation), the zero-result search test, re-running first paint with simulated RTT,
field growth rates, the accessibility and mobile debt, link integrity.
`CHOICE-01SEP.md` carries the reasoning for staying cloud.
