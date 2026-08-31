# TO THE DIRECTOR — 31 Aug 2026 — first paint, measured against a throttled load

You asked for the one measurement I can make and you cannot. Here it is, and it does
not support either of our remedies.

**Headline: reordering the hero SVG produces no measurable first-paint improvement
(−14 ms, p=0.49, n=30 per arm). The render-blocking stylesheet is the actual
constraint — removing that round trip cuts FCP by 89% (−962 ms, p<0.001). The
autoplaying media is the second — removing it cuts FCP 40% and total load 5×.**

---

## 0. FIRST, A CORRECTION TO YOUR BYTE MODEL: CLOUDFLARE SERVES BROTLI q4, NOT q11

You measured with `brotli -q 11`. I measured what the origin actually sends.

```
curl -o /dev/null -H 'Accept-Encoding: br'       -w '%{size_download}' https://eqlsource.com/  -> 39,547
curl -o /dev/null -H 'Accept-Encoding: gzip'     -w '%{size_download}' https://eqlsource.com/  -> 40,020
curl -o /dev/null -H 'Accept-Encoding: identity' -w '%{size_download}' https://eqlsource.com/  -> 241,709
```

Brotli **is** served — that answers your open question. But br and gzip land within
**1.2%** of each other, which is the signature of low-quality on-the-fly compression,
not `-q 11` (where brotli normally beats gzip by 15–20%).

Compressing the exact bytes locally identifies the level precisely:

| | live | br q11 | br q5 | **br q4** |
|---|---|---|---|---|
| index.html | **39,547** | 27,281 | 36,693 | **39,562** |
| site.css | **25,335** | 20,554 | 23,521 | **25,321** |

**q4 predicts live within 15 bytes on both files.** Your model's 27,281 understates the
real wire cost of index.html by **45%**.

### What that does to your decisive measurement

Your claim: stripping the 751 repeated attribute strings and the 23,396 redundant
trailing `.0` removes 111,378 raw bytes (46.1% — I reproduce this exactly) and saves
**823 brotli bytes**.

| compression | saving |
|---|---|
| br q11 (your method) | **823 B** — reproduces exactly |
| gzip -9 | 2,810 B |
| **br q4 / q5 (what is served)** | **3,144 B** |

The saving is **3.8× larger** than your figure, because low-quality brotli has a weaker
match window and therefore benefits more from removing literal redundancy. At the served
level that is **~8% of the delivered document**, not 3%.

Your blocking-path breakdown moves too: at q4 the sixteen SVGs are **43.7%** of blocking
bytes (66,191 total), not 39.9% of 48,941.

**Your direction survives — the SVGs are emphatically not 85% of what a reader
downloads, and my original finding was wrong to imply they were. Your magnitudes do
not survive.** None of this changes the conclusion below, which supersedes the byte
argument entirely.

---

## 1. METHOD

Mirrored the live page and every asset it requests (35 files, 2.9 MB) and served them
from a local origin that compresses with **brotli q4** to match production and shares a
**600 kbit/s token bucket** across all connections. Four variants, byte-identical apart
from the change under test, each carrying the same measurement probe:

| | change |
|---|---|
| **A** | as served |
| **B** | `.hero-art` div moved after `.shell` — your proposal |
| **D** | `site.css` inlined, removing the render-blocking request |
| **E** | the two `<video>` elements removed |

FCP and LCP read from `PerformanceObserver` with `buffered:true`. Headless Chromium,
cold profile per run. **Instrument validated first**: median FCP tracks bandwidth
(300 kbit/s → 2,660–5,076 ms; 1,500 → 208–556; 20,000 → 204–208), so it is measuring
transfer rather than virtual time.

I verified your layout claim independently before testing it: `site.css:706`
`.hero-art{position:absolute; … z-index:0}` against `:732` `.hero .shell{position:relative;
z-index:1}`. Both are out of normal flow. Reordering is visually free — you are right.
Byte offsets also reproduce: the h1 moves from **26,703 → 5,046**, an 81% improvement,
against your 26,689 → 5,082.

## 2. RESULT

600 kbit/s. FCP and LCP were identical in every run — the LCP element is a `<p>`, never
the `<h1>`.

| variant | n | median FCP | p75 | stdev | vs A | p (Mann-Whitney) |
|---|---:|---:|---:|---:|---:|---:|
| **A** as-served | 30 | **1,078 ms** | 1,434 | 494 | — | — |
| **B** reordered | 30 | **1,064 ms** | 1,182 | 345 | **−14 ms** | **0.492** |
| **D** css inlined | 15 | **116 ms** | 132 | 54 | **−962 ms** | **<0.001** |
| **E** media removed | 15 | **652 ms** | 668 | 32 | **−426 ms** | **<0.001** |

Full-page load: A 11,614 ms · B 11,578 ms · **E 2,298 ms**.

### Your remedy does not work, and here is why

At n=9 I saw B ahead by 248 ms and nearly reported it as a win. At n=30 that collapses
to **14 ms at p=0.49**. The early signal was noise, and I am reporting it because it is
the kind of result that gets published when someone stops at the first encouraging run.

**Document order only matters when the parser is the constraint. It is not.** Nothing
paints until `site.css` arrives — 25,335 br bytes on a separate round trip — so it makes
no difference whether the h1 sits at byte 5,046 or 26,703. Both are long since parsed by
the time paint is permitted. Your fix is free and harmless and I would still take it for
the variance alone (A's stdev is 1.4× B's), but it is not the fix.

### What actually binds

**The render-blocking stylesheet.** Removing that round trip took FCP from 1,078 ms to
**116 ms — 9.3× faster**, the largest effect measured by a wide margin.

**Caveat, and it matters: D is a mechanism probe, not a recommendation.** Inlining all
87 KB of CSS made full load *worse* (16,352 ms vs 11,614) because it is then
uncacheable and sits in the critical document. The correct version is critical-CSS
inlining — above-the-fold rules in the head, the rest deferred. My test proves what the
bottleneck is; it does not prove that implementation.

**The autoplaying media.** E cuts FCP 40% and total load from 11.6 s to 2.3 s. **2.19 MB
of autoplay video is ~80% of this page's load time**, and neither of us was looking at
it while we argued about 206 KB of path data that compresses 10.6:1.

## 3. WHERE THIS LEAVES F03

Both remedies are wrong.

- **Mine** — delete the SVGs — you refuted on bytes, and I accept it. Your Phase 0
  critique measured a search field I did not propose: you costed inlining the 194,949-byte
  index, then noted in the same message that `search.html` already accepts `?q=` so a
  plain GET form is +121 bytes. That second one is what I meant. The refutation of your
  own critique is in your own message.
- **Yours** — reorder — measured above, no significant effect.
- **The defect is real and we both mislocated it.** Not weight, not order:
  **a render-blocking stylesheet and 2.19 MB of autoplay video.**

Suggested restatement of F03: *the homepage's first paint waits on a separate
stylesheet round trip and competes with 2.19 MB of autoplaying media; the inline SVG
is an authoring and DOM-size cost, not a transfer or paint cost.*

## 4. WHAT I HAVE NOT ESTABLISHED

- **No network latency.** My rig throttles bandwidth only; there is no simulated RTT.
  Real connections add latency per round trip, which would make the render-blocking
  stylesheet **worse** than measured, not better. The direction of that error favours
  my conclusion, which is a reason to distrust it — someone should re-run with real RTT.
- **Not measured against the live origin.** Mirrored bytes, local origin, production
  compression level. Cloudflare's edge, HTTP/2 prioritisation and connection reuse are
  not modelled.
- **One bandwidth.** 600 kbit/s. The ordering effect might appear at bandwidths where
  the parser does bind; I did not sweep.
- **Headless.** No real device, no CPU throttling, no cold DNS/TLS.

Every number above is reproducible: `serve.py` and `measure.sh` are in the scratch
directory and the method is stated in full. The four variant files differ only in the
one change each names.
