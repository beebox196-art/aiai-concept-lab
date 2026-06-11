# AIAI Website Concept Lab — 4 Variations

Created 2026-06-11 by Claude (Fable 5) at Adam's request. Four standalone look-and-feel
concepts for adventuresinai.co.uk. **Nothing here touches `Website/` or `Website-deploy/`.**

## How to view

Open `Tests/index.html` in a browser — it's a hub linking to all four. Or serve the folder:

```bash
cd ~/projects/aiai/Tests && python3 -m http.server 8765
# → http://localhost:8765
```

(Everything works over `file://` too; fonts and Tailwind CDN for Concept 1 need internet.)

## The four concepts

| # | Folder | Concept | Brief |
|---|--------|---------|-------|
| 1 | `site-1-spectrum/` | **Full Spectrum** | Current visual identity kept (navy/cream/sage/gold, Tailwind). Copy, tone and structure reworked to address the full spectrum of business owners — three audience "doors" (small/local → growing → enterprise) mapped to the three service tiers. |
| 2 | `site-2-organism/` | **The Organism** | The site as a living thing: canvas neural field that senses and reacts to the cursor (leans in, recoils when crowded), breathing headline gradient, heartbeat dividers, sections that "awaken" from blur, custom cursor halo, scroll filament. Copy reframed biologically (senses / digests / grows; a day in the organism's life). |
| 2A | `site-2a-organism-daybreak/` | **Organism · Daybreak** | (Added 2026-06-11 on Adam's request for a friendlier flowing-colour version.) Same living field in a warm daylight palette: cream page with four large watercolour blooms (coral/lavender/sky/butter) drifting on 38–56s loops, warm coral/violet particles, gradient stat numbers. |
| 2B | `site-2b-organism-aurora/` | **Organism · Aurora** | (Same request.) Soft twilight indigo with three northern-lights ribbons (teal/pink/gold) drawn on a low-res canvas behind a 46px blur, flowing continuously behind the neural field. Gentler than the original abyss, still nocturnal-magical. |
| 3 | `site-3-clarity/` | **Clarity** | Current minimal-design trends: floating pill nav, one accent colour (cobalt), oversized Inter Tight type, bento stat grid, numbered steps, hover service rows, accordion FAQ, sticky mobile CTA. Shortest copy of the four. |
| 4 | `site-4-machine/` | **The Machine That Builds It** | The wildcard. Boot sequence where the agent team wakes, then the page assembles itself (wireframe → painted, stamps snap on) while a live ops-feed dock narrates whichever section you're viewing, plus idle chatter. Evidence ledger, hover-to-declassify stats, decision trail. The medium proves the "we run our own AI team" message. |
| 4A | `site-4a-machine-workshop/` | **Machine · Open Workshop** | (Added 2026-06-11 on Adam's request for an active, welcoming background.) Same boot/assembly/ops-feed mechanics, re-set in a warm workshop: deep plum-charcoal, blueprint grid drifting diagonally on a 70s loop, three breathing lamplight pools (amber/peach/violet), and ~90 rising embers that twinkle and drift toward the cursor ("moths to lamplight"). Copy warmed to match: /welcome, "WORKSHOP OPEN", "KETTLE ON" stamp. |
| 6 | `site-6-beat-the-machine/` | **Beat the Machine** (playable argument) | (Added 2026-06-11 — Adam picked "things to play, not read" from my stretch list.) A 30-second inbox-triage game: 24 fictional-but-plausible emails for a Yorkshire hire firm, sorted Critical/Action/Info/Noise by tap or keys 1–4 while more keep arriving. Engineered moments: an HMRC-phishing trap that looks urgent, and a burst-pipe emergency dealt ~82% through the deck when the player is overwhelmed. Then the machine sorts the same 24 in 1.8s (scam quarantined, criticals "pinged your phone") and the verdict screen personalises callouts to what the player actually fooled/missed. "Watch instead" demo path, `?t=N` test hook for a shorter round, aria-live announcements. |
| 5 | `site-5-greenhouse/` | **The Greenhouse** (finale) | (Added 2026-06-11 — Adam asked for an aggregation of Organism + Machine.) The synthesis metaphor: a machine built to grow living things. Germination boot (pulsing seed + crew lines), sections grow from dashed seed-outlines into glass panels ("GROWN ✓ / IN BLOOM"), an SVG vine grows down the left edge with scroll and sprouts a lit node+bud at each section, cursor-reactive firefly field (organism behaviour, workshop warmth), potting-bench ops feed, planting-record ledger, stats hidden under hover-away leaves, and the engagement gates reframed as seasons (Sow/Grow/Prune/Harvest). Palette: greenhouse night (#0d1714), leaf, pollen, lamp amber, bloom pink. |

## Shared ground rules applied

- All statistics restricted to the verified set from the live site (95% MIT NANDA, 80%/£78bn DSIT, 3.3% Yahoo Finance, 53% Cloudera).
- No phrases from the Brand Bible "Messages We Never Use" list, even in the free-form concepts.
- Real systems/cadences only (email triage every 30 min, Sunday 3am synthesis, etc.).
- CTAs point at the live site's contact page / hello@adventuresinai.co.uk.
- Each page carries a fixed "Concept N/4" badge linking back to the hub, and a footer note that it is not the live site.
- `prefers-reduced-motion` respected on all animated concepts (2 and 4 degrade to static).

## Assets

`assets/img/` contains copies of the wordmark/badge PNGs and favicon from `Website-deploy/assets/img/` — referenced as `../assets/img/...` from each concept folder.
