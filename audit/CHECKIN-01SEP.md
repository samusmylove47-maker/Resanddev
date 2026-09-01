# TO THE DIRECTOR — 1 Sep 2026 — check-in, one result, and a request for work

Nothing is blocked. The first-paint result is delivered (`FIRSTPAINT-31AUG.md`), the
denominator result is delivered (`DENOMINATOR-31AUG.md`), and F03's remedy question is
answered against measurement rather than either of our inferences.

I am asking for an assignment. Below is a down payment on the denominator work you said
was the more important of the two, then a ranked list of what I am positioned to do that
you are not, then the ask.

---

## DOWN PAYMENT — two independently verified item sets overlap by only 17.5%

You asked me not to volunteer numbers about your tree, so this is computed from two
public payloads and nothing else.

```
A   eqlsource.com Index (window.__IX__)          441 unique names
B   eqlbase.com /data/verified.json              249 verified names
A ∩ B   verified independently by both           103
A \ B   only EQL Source has                      338
B \ A   only EQLBase has                         146   (2 were fuzzy near-misses; both
                                                        proved genuinely DIFFERENT items,
                                                        so all 146 stand as real misses)
A ∪ B   distinct items verified by ≥1 party      587
```

Overlap is **41.4% of the smaller set**; Jaccard **17.5%**.

### Why this matters more than the individual counts

**1. A better floor on the corpus, from evidence rather than inference.** My previous
floor of ≥1,470 was derived from Gnoll Guard's defect arithmetic — a bound on a number,
not a set. **587 is a bound built from actual named, independently verified items**, and
unlike the 1,470 it is enumerable. Both floors stand; this one is enumerable and checkable name by name.

**2. The two verification efforts are complementary, not duplicative.** An 82.5%
non-overlap means the field is not converging on the same corpus from different
directions — it is covering different parts of it. Nobody is close to done, and the
true corpus is comfortably above either party's total.

**3. 146 concrete names.** `CROSSCHECK-ITEMS.txt` in this directory lists every item
EQLBase flags as verified that the Index does not carry.

**The caveat is load-bearing and I want it read before the list is acted on:**
`verified.json` carries no per-item zone. An unknown share of those 146 sit in zones
eqlsource has never surveyed, where absence is correct and not a defect. **It is a
cross-check worklist, not a defect list.** Turning it into one requires zone attribution
I do not have.

---

## WHAT I AM POSITIONED TO DO THAT YOU ARE NOT

Ranked by what I think the project gets per unit of work. All public-surface, all
robots-compliant, none requiring me to learn anything about you.

**1. Verification-rate tracking — the derivative, not the value.**
`verified.json` is timestamped (`generatedAt`) and regenerates. Sampling it on a
schedule yields **EQLBase's verification velocity in items per day**. In a land grab
the derivative decides the outcome and the snapshot does not: 249 verified is a
different competitive fact if it was 240 last week versus 40 last week. Nobody has this
number, including EQLBase, and it compounds in value the earlier the series starts.
**This is the one I would pick.**

**2. The zero-result search test, properly.**
The measurement I flagged as my biggest regret. I now have a ground-truth set — the 146
above plus the 103 confirmed hits give a real test corpus with known-correct answers.
Run it against the Index and publish a true miss rate, empirically, from outside, with
no denominator required.

**3. Re-run first paint with simulated RTT.**
My rig throttled bandwidth only. The missing latency would make the render-blocking
stylesheet penalty **worse**, which favours the conclusion I published — and that is
precisely why someone should attack it. I would rather break my own result than have it
break later.

**4. Field growth rates via Wayback.**
Snapshots of all eight sites over five weeks. Same argument as (1), applied to the
whole field instead of one rival.

**5. Live-site accessibility and mobile.**
I criticised the mobile experience and read contrast tokens out of the stylesheet
without ever rendering eqlsource.com at a phone width or running an audit against a real
page. That is an unpaid debt in the original document.

**6. Link integrity across 715 pages** — internal 404s, and whether the og:image fix
actually reaches every page. Dull, cheap, and the kind of thing that is quietly wrong.

### What I cannot do, so you do not assign it
Enumerate Gnoll Guard. Their robots.txt names `ClaudeBot`, `Claude-Web` and
`anthropic-ai` under `Disallow: /`. Any assignment that needs their corpus counted needs
someone who is not me. eqltools.com likewise refuses bulk crawling while welcoming
citation, so I can cite them but not harvest them.

---

## THE ASK

Pick one, or name something better — you can see the project and I deliberately cannot.
What would help most is work where **being outside is the qualification rather than the
limitation**, because that is the only thing I have that the rest of the project does
not. The three times this instrument has earned its keep were all of that shape: the
`<video>` elements two internal checks could not see, the `verified.json` split, and the
group-versus-item population that overturned a published ruling.

If the honest answer is that nothing needs an outside instrument right now, say that.
Idle is a better outcome than manufactured work.
