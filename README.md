# AIAI Website Concept Lab

Created 2026-06-11 by Claude (Fable 5) at Adam's request, over one extended session.
Nine standalone website concepts for adventuresinai.co.uk plus one data pipeline.
**Nothing in this folder touches `Website/` or `Website-deploy/` (the live site), and
nothing publishes anywhere. All builds are local-only until Adam decides otherwise.**

Audience for this file: Adam and the agent team (Bee, Q, Mel, Gav, Luna, Kieran).
It is written so any agent can operate, extend or critique the lab without session context.

---

## 1. Quick start

```bash
# Option A — just open the hub in a browser:
open ~/projects/aiai/Tests/index.html

# Option B — serve it (required only if you want fetch()-style testing):
cd ~/projects/aiai/Tests && python3 -m http.server 8765   # → http://localhost:8765
```

Everything works over `file://`. Internet is needed for Google Fonts (all concepts) and
the Tailwind CDN (Concept 1 only). All other concepts are dependency-free hand-written
HTML/CSS/JS in a single `index.html` per folder.

---

## 2. The concepts (in creation order)

| # | Folder | Concept | One-line brief |
|---|--------|---------|----------------|
| 1 | `site-1-spectrum/` | **Full Spectrum** | Current brand identity kept (navy/cream/sage/gold, Tailwind CDN); copy/structure rebuilt around three audience doors (small/local → growing → enterprise) mapped to the three service tiers. |
| 2 | `site-2-organism/` | **The Organism** | Adam's standout favourite. Dark bioluminescent canvas neural field that reacts to the cursor (leans in from afar, recoils up close), breathing headline gradient, heartbeat dividers, blur-awakening sections, cursor halo, scroll filament. Copy reframed biologically (senses / digests / grows). |
| 2A | `site-2a-organism-daybreak/` | **Organism · Daybreak** | Friendlier flowing-colour variant: warm cream page, four large watercolour blooms (coral/lavender/sky/butter) drifting on 38–56s blur loops, coral/violet particles. |
| 2B | `site-2b-organism-aurora/` | **Organism · Aurora** | Twilight variant: indigo night with three aurora ribbons (teal/pink/gold) drawn each frame on a 360×200 canvas scaled up behind `blur(46px)` — silky movement, near-zero cost. |
| 3 | `site-3-clarity/` | **Clarity** | Minimal-trend build: floating pill nav, one cobalt accent, oversized type, bento stat grid, numbered steps, hover service rows, accordion FAQ, sticky mobile CTA. Shortest copy. |
| 4 | `site-4-machine/` | **The Machine That Builds It** | Terminal boot where the agent team "wakes", sections assemble wireframe→painted with stamps, ops-feed dock narrates the section in view + idle chatter. Evidence ledger, hover-to-declassify stats, decision trail. |
| 4A | `site-4a-machine-workshop/` | **Machine · Open Workshop** | Same mechanics, welcoming room: warm plum-charcoal, blueprint grid drifting on a 70s loop, three breathing lamplight pools, ~90 rising embers that drift toward the cursor. "KETTLE ON" register. |
| 5 | `site-5-greenhouse/` | **The Greenhouse** (Organism × Machine synthesis) | Germination boot (pulsing seed), sections grow from seed-outline to glass panel ("GROWN ✓"), an SVG vine grows down the left edge with scroll and sprouts a node at each section, firefly field, potting-bench feed, seasons = Sow/Grow/Prune/Harvest. |
| 6 | `site-6-beat-the-machine/` | **Beat the Machine** (playable argument) | 30-second inbox-triage game (details §4). |
| 7 | `site-7-machine-live/` | **The Machine, Live** (real data) | Concept 4A driven by an allowlist extraction of Luna's real reports (details §5). |

Hub: `index.html` (cards for all of the above). Shared logos: `assets/img/`
(copies from `Website-deploy/assets/img/`, referenced as `../assets/img/...`).

---

## 3. Ground rules every concept obeys

- **Statistics**: only the verified set from the live site — 95% zero-value pilots (MIT NANDA),
  80% UK non-adoption + £78bn gap (DSIT), 3.3% Copilot adoption (Yahoo Finance),
  53% data-privacy blocker (Cloudera). No new numbers may be invented.
- **Voice**: nothing from the Brand Bible "Messages We Never Use" list, even in concept pieces.
- **Honesty**: real systems and cadences only (email triage every 30 min, Sunday 03:00 synthesis…).
  Where data shows a flaw (amber health check, late brief), the concepts *display* it.
- **CTAs** point at the live site contact page / hello@adventuresinai.co.uk. Test pages never
  collect form data themselves.
- Every page carries a fixed "Concept N" badge linking back to the hub and a footer note that
  it is not the live site.
- `prefers-reduced-motion` is respected everywhere (canvases freeze, boots skip, builds pre-built).
- All pages were verified in headless Chrome via `agent-browser` (zero console errors at sign-off).

---

## 4. Concept 6 — Beat the Machine (how the game works)

Single file: `site-6-beat-the-machine/index.html`. No dependencies, no network calls.

- **Fiction**: visitor runs "Hartley's Hire & Supplies" (invented Yorkshire firm). 24 invented
  emails — `EMAILS` array at the top of the inline script; each has a ground-truth category
  (`critical|action|info|noise`) and flags (`scam`, `esc`, `late`).
- **Round 1 (human)**: 30s timer; one email at a time; sort via buttons or keys `1–4`/`C A I N`;
  queue refills faster than most people can sort (by design). Deal order is shuffled per play
  but constrained: a critical lands in the first 4, the scam never lands first, the `late`
  email (burst pipe) is inserted ~82% through the deck.
- **Engineered moments**: HMRC-phishing email that *looks* urgent (most players file it
  Critical/Action); burst-pipe emergency arriving at peak overwhelm (most never see it).
- **Round 2 (machine)**: same 24 cascade into four columns in 1.8s; scam chip flagged
  "quarantined", criticals "pinged your phone".
- **Verdict**: personalised callouts driven by what actually happened (fooled by scam /
  caught it / missed the pipe / misfiled it), score board, one closing paragraph, replay.
- **Paths & hooks**: "I'd rather just watch" button = demo mode (machine round + generic
  verdict). URL param `?t=N` (5–30) shortens the round for demos/testing,
  e.g. `index.html?t=10`. `aria-live` announces new emails for screen readers.

---

## 5. Concept 7 — The Machine, Live (data pipeline runbook)

Folder: `site-7-machine-live/` → `extract_pulse.py`, `index.html`, generated `pulse.json` + `pulse.js`.

### Decision record (2026-06-11, Adam + Claude)
- **Source: `~/Desktop/Luna Daily Reports/`** (morning brief, evening recap, health check,
  plus neo-* / openclaw-news counted for cadence).
- **`~/Desktop/Claude Oversight Reports/` is explicitly EXCLUDED and must never feed a public
  page** — it contains launchd service maps, open-port findings, login history and risk
  assessments. Do not "improve" this pipeline by adding it.

### How the extractor works
```bash
python3 ~/projects/aiai/Tests/site-7-machine-live/extract_pulse.py            # extract + write
python3 ~/projects/aiai/Tests/site-7-machine-live/extract_pulse.py --dry-run  # print only
```
1. **Allowlist only.** Every output field is a number (regex-captured digits), a count of
   files/emoji, a file-mtime timestamp, or a hardcoded label. There is *no code path* that
   copies free text from a report. The full schema is whatever you see in `pulse.json` —
   that file is the complete universe of exposable data.
2. **Deny-scan over the output** (belt and braces): email addresses, account-ID shapes,
   IPs, filesystem paths, ports/endpoints, credential-ish words, plus `DENY_NAMES` (people,
   clients, vendors, projects — list at the top of the script; **extend it whenever a new
   client or sensitive project appears**). Any hit → prints the reason, leaves the previous
   `pulse.json` untouched, exits 1.
3. Writes both `pulse.json` (for inspection/CI) and `pulse.js` (`window.AIAI_PULSE = …`,
   so the page works over `file://` without CORS issues).

### How the page consumes it
- `<script src="pulse.js">`; if absent/unloadable → **sample mode** with a peach
  "SAMPLE DATA — FEED OFFLINE" stamp and adjusted copy. Never errors.
- If `generated` is older than **36 hours** → amber "PULSE STALE — LAST Xh AGO" stamp;
  the page admits staleness rather than pretending.
- Data drives: brief gauges, recap triage bars, health traffic-lights (ambers warm a
  background lamp), the 7-day shift log with real filing times (a morning brief filed
  ≥ 09:00 is highlighted and triggers the "we show our own lateness" callout),
  reports-per-day chart, boot lines, ops-feed lines, and ember count
  (`30 + reports_this_week × 4`, capped 110).
- The "What leaves the machine" section on the page publishes the data contract to visitors.

### Refresh cadence & production path (NOT yet done — needs Adam's go)
- Locally: re-run the extractor whenever you like; it's idempotent and read-only on sources.
- To make the live site live: add a launchd job that runs the extractor after Luna's evening
  recap (e.g. 21:15), then commits `pulse.json`/`pulse.js` into `Website-deploy/` and pushes
  (Cloudflare Pages auto-deploys). **Do not set this up without Adam's explicit approval** —
  he is evaluating data exposure locally first.

---

## 6. Verification & maintenance notes for agents

- Verify any change with: `cd Tests && python3 -m http.server 8765`, then `agent-browser`
  (installed globally; `agent-browser open … / screenshot / console`). Check console is clean.
- Each concept is fully self-contained — copy a folder to fork a variant; update the hub
  `index.html` card grid and this README table when you do.
- Kieran: the claims worth auditing are all in §3; the game's emails (§4) are fiction and
  must stay obviously fictional; §5's deny-list is the security-critical surface.
- Session history and Adam's reactions are in Claude's memory
  (`project_aiai_concept_lab.md`) and the `Claude/` transcripts folder.
