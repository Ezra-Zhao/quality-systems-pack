# Line Walk Checklist — Rack Cable Assembly Line

> **TEMPLATE / METHOD DEMONSTRATION.**
> A ready-to-use line walk (gemba walk) checklist format for a cable
> assembly line, written as an example. Station names, limits, and part
> numbers are illustrative — replace them with the real line's values at
> adoption. Mark each item OK / NG / N-A, and give every NG an action,
> an owner, and a due date in the follow-up table at the end. A walk
> that produces no actions for a month is not evidence of a perfect
> line; it is evidence the walk has gone stale.

**Walk header (fill in every walk):**

| Field | Entry |
|---|---|
| Date / shift | |
| Line / cell | Cable assembly (example) |
| Walk leader | |
| Participants (quality / ME / production) | |
| Product(s) running | |
| Last walk's open actions reviewed? (Y/N) | |

**Cadence (example):** quality-led walk weekly; supervisor walk each
shift start; management gemba monthly. Findings feed the action table;
closure is verified at the next walk, not by email assertion.

---

## A. Incoming material & supermarket

| # | Check item | Standard / what "good" looks like | Method | OK | NG | N/A | Notes |
|---|---|---|---|---|---|---|---|
| A1 | Quarantine area integrity | Rejected/held lots physically segregated, tagged, and matching the hold list | Eyes + hold list | | | | |
| A2 | Lot traceability at point of use | Opened reels/boxes carry lot ID; no untraceable material at stations | Sample 3 stations | | | | |
| A3 | FIFO rotation | Oldest lot in front and in use first | Eyes | | | | |
| A4 | Terminal/wire storage condition | Reels undamaged, ends protected, no kinks or crushed insulation | Eyes | | | | |
| A5 | Inspection status visible | Material at line is released material only (status label present) | Sample 3 lots | | | | |

## B. Crimping stations

| # | Check item | Standard / what "good" looks like | Method | OK | NG | N/A | Notes |
|---|---|---|---|---|---|---|---|
| B1 | Die life status | Die cycle counter within life limit; no press running past limit without quality release | Read counter vs. limit sheet | | | | |
| B2 | Setup qualification record | Last die change / setup has complete first-article record: crimp height (5 pcs), cross-section, pull force, quality sign-off | Audit record vs. production log timing | | | | |
| B3 | Crimp-height SPC alive | X-bar/R chart current (subgroup within the last hour), plotted, and in the operator's handwriting/system — not back-filled | Read chart timestamps | | | | |
| B4 | Reaction plan followed | Any out-of-control point on the chart has a documented reaction (stop, segregate since last good subgroup, notify) | Pick the most recent signal, trace it | | | | |
| B5 | Crimp height measurement tool | Micrometer present, zero-checked, calibration sticker in date | Eyes + zero check | | | | |
| B6 | Applicator / press condition | No visible die damage, no excessive lubricant or debris in crimp zone, guards in place | Eyes | | | | |
| B7 | Scrap discipline | Crimp scrap and cut-off terminals in the red bin, not the work surface or floor | Eyes | | | | |

## C. Harness assembly & routing

| # | Check item | Standard / what "good" looks like | Method | OK | NG | N/A | Notes |
|---|---|---|---|---|---|---|---|
| C1 | Work instruction currency | Station copy matches the released revision; no handwritten unofficial edits | Compare revision vs. document system | | | | |
| C2 | Routing per build board / fixture | Cables follow the fixture path; bend radii respected; no improvised routing | Watch one full build | | | | |
| C3 | Cable mapping / labeling | Labels match the build's mapping table; label placement consistent | Sample 3 finished units vs. mapping | | | | |
| C4 | Connector seating | Connectors fully latched; tug check performed per instruction | Watch + sample tug | | | | |
| C5 | Protection of finished runs | Completed harnesses not draped over edges, stacked under weight, or contacting sharp metal | Eyes | | | | |
| C6 | ESD & handling | ESD controls in place where the product requires them; operators following them, not just equipped | Eyes | | | | |

## D. Test

| # | Check item | Standard / what "good" looks like | Method | OK | NG | N/A | Notes |
|---|---|---|---|---|---|---|---|
| D1 | Test program revision | Running program matches the released test spec revision, including the flex/wiggle continuity step for crimped circuits | Read program ID vs. spec | | | | |
| D2 | Seeded-defect challenge currency | Most recent known-bad challenge passed (standard test catches seeded intermittent defects 100%); date within the required interval | Review challenge log | | | | |
| D3 | Fail handling | Failed units tagged with failure data, segregated, and entering the failure-analysis loop — not retested into passing | Trace 2 failed units end to end | | | | |
| D4 | Retest policy | "Pass on retest" is not an acceptance path for intermittent signatures; retest rules posted and followed | Interview operator + review logs | | | | |
| D5 | FPY data integrity | Test results auto-logged; daily FPY/p-chart updated from system data, not hand-carried numbers | Compare chart vs. system extract | | | | |

## E. Packing & shipping

| # | Check item | Standard / what "good" looks like | Method | OK | NG | N/A | Notes |
|---|---|---|---|---|---|---|---|
| E1 | Shipment hold compliance | No held lot in the ship area; hold list posted and current | Hold list vs. staged pallets | | | | |
| E2 | Packaging protection | Harnesses coiled/packed to spec; connectors capped where required; no compression damage | Open 1 packed unit | | | | |
| E3 | Label & traceability match | Box label, serial range, and paperwork agree | Sample 2 boxes | | | | |

## F. Workplace, safety & system health

| # | Check item | Standard / what "good" looks like | Method | OK | NG | N/A | Notes |
|---|---|---|---|---|---|---|---|
| F1 | 5S at stations | Only current-build material at the station; tools shadow-boarded; aisles clear | Eyes | | | | |
| F2 | Safety | Press guards and two-hand/presence controls functional; no defeated interlocks; PPE in use | Eyes + function check where safe | | | | |
| F3 | Andon / escalation works | Operators can state the stop-and-call triggers and the last time escalation was used — and it was honored | Interview 2 operators | | | | |
| F4 | Boards tell the truth | Line board (output / FPY / top defects / actions) is current to today and matches system data | Compare board vs. data | | | | |
| F5 | Previous actions verified | Last walk's due actions are actually in place on the floor, not just marked closed | Re-check each due item physically | | | | |

---

## Follow-up action table (every NG lands here)

| # | Finding (item ref.) | Action | Owner | Due | Verified closed (date / by) |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |

## Walk close-out

- Top risk seen today (one sentence):
- What improved since the last walk (be specific):
- What the next walk must re-check first:

---

*Design note: items B1–B4, D1–D4, and E1 exist because of the failure
pattern worked through in the synthetic 8D case in this pack
(`../8d-case/8d-report-cable-failure.md`) — die life, in-process SPC
with a real reaction plan, a final test that provokes intermittent
failures, and hold discipline are the four controls whose absence let
that (fictional) escape happen. On a real line, the checklist should
grow the same way: every escape adds a permanent walk item.*
