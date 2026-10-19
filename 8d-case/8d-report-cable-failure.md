# 8D Corrective Action Report — Rack Cable Assembly Intermittent Continuity Failure

> **SYNTHETIC CASE — METHOD DEMONSTRATION ONLY.**
> This entire case is invented for the purpose of demonstrating 8D method,
> structure, and documentation quality. The company, line, part numbers,
> dates, people, quantities, and measurements are fictional. No real
> employer, contract manufacturer, supplier, customer, or production data
> appears anywhere in this document. Any resemblance to a real quality
> event is coincidental. Numbers quoted from the charts in this pack come
> from the synthetic datasets in `../data/` and are labeled as such
> wherever they appear.

| Field | Value (all fictional) |
|---|---|
| 8D report no. | SYN-8D-0001 (example numbering) |
| Date opened | Week 9 of the synthetic production calendar |
| Date closed | Week 26 of the synthetic production calendar |
| Product | Rack-level power/signal cable assembly (harness), fictional part no. CBL-SYN-1042 |
| Process | Terminal crimping -> harness assembly -> routing/labeling -> final electrical test |
| Failure mode | Intermittent open / high contact resistance on crimped terminals |
| Severity | Major (functional). One fictional customer escape is included in the scenario to exercise the escape-analysis path. |
| Team roles | Quality engineer (owner), manufacturing engineer, test engineer, supplier quality engineer, line supervisor, design liaison |

---

## D0 — Symptom and Emergency Response

**Symptom (synthetic scenario).** Final electrical test on the harness line
begins failing finished cable assemblies at a visibly higher rate. The
dominant failure signature is intermittent continuity on two terminal
positions: assemblies pass a static continuity check on retest roughly
half the time, then fail again after handling. In week 9 of the synthetic
FPY series (`../data/fpy_weekly.csv`), weekly first pass yield drops to
84.18%, the lowest point in the 26-week synthetic series, against a
weeks 1–13 synthetic mean of 91.69%.

**Emergency response actions (taken within the scenario, in order):**

1. Line stop on the affected crimp press (Press 2 in the scenario) pending
   assessment; production continues on Press 1 with 100% flex-test added
   (see D3).
2. Same-day notification to the quality owner and manufacturing
   engineering; suspect window defined as all assemblies crimped on
   Press 2 since the last documented die inspection.
3. Shipment hold on all finished goods from the suspect window; no
   suspect product leaves the building after D0.
4. Customer-escape check: traceability review identifies one fictional
   shipment inside the suspect window that had already left. The scenario
   treats this as a customer escape and routes it through the full 8D
   (notification, field containment, and return-and-replace are described
   in D3). All customer details are invented.

**Why an 8D (and not a simple line fix):** the failure is intermittent
(escapes a static test), it crossed the shipping dock once, and the same
crimp process feeds multiple harness part numbers — all three are classic
triggers for a formal 8D rather than a local adjustment.

---

## D1 — Team

| Role | Responsibility in this 8D |
|---|---|
| Quality engineer (champion/owner) | Owns the 8D, containment decisions, closure criteria |
| Manufacturing engineer | Press/die process knowledge, setup and maintenance history |
| Test engineer | Failure signature analysis, test coverage gap analysis (escape point) |
| Supplier quality engineer | Terminal and wire supplier interface, incoming inspection plan changes |
| Line supervisor | Containment execution, sorting labor, line-walk follow-up |
| Design liaison | Drawing/spec interpretation for crimp height and pull-force limits |
| Production control | Traceability, suspect-window definition, shipment hold/release |

All names are omitted on purpose: this is a synthetic case, and role-based
ownership is what the method requires.

---

## D2 — Problem Description

**Problem statement.** Cable assemblies built on Crimp Press 2 exhibit
intermittent open-circuit / high-resistance failures at final electrical
test, at a rate high enough to pull synthetic weekly FPY from a ~92%
baseline down to 84.18% in the worst week, with one fictional customer
escape from the suspect window.

**Failure signature (as defined in the scenario):**

- Continuity resistance on the affected positions measures in-spec when
  the harness is static on the bench, and goes open or high-resistance
  when the cable is flexed near the terminal or thermally cycled.
- Microscopic cross-section of failed terminals (scenario detail) shows
  conductor strand damage at the crimp barrel — strands nicked and
  partially severed — consistent with over-compression.
- Crimp height measurements on suspect terminals trend *below* the
  nominal 1.60 mm example specification used in this pack: the synthetic
  X-bar baseline (subgroups 1–15 of `../data/spc_xbar_crimp.csv`) sits at
  X-double-bar = 1.5696 mm, i.e. the process was centered roughly
  0.03 mm low while nobody was charting it (see D4).

**IS / IS NOT analysis:**

| Dimension | IS | IS NOT |
|---|---|---|
| What | Intermittent continuity / high resistance at crimped terminals; strand damage in cross-section | Connector housing damage; solder defects; wrong-wire or wrong-pin build errors |
| Where | Terminals crimped on Press 2; two high-density positions on the harness | Press 1 terminals (same part number, same operators) |
| When | Suspect window opens after the last die inspection; rate climbs gradually, spikes in week 9 | Present since process launch; present before the die's accumulated cycle count grew |
| Who/which lots | Assemblies from Press 2 in the suspect window; one fictional shipped lot | Other harness part numbers on Press 1; assemblies built after containment |
| How big | Synthetic FPY weeks 1–13 mean 91.69%, worst week 84.18%; daily p-chart baseline defective rate p-bar = 4.16% (synthetic) | Not a total line failure — most assemblies still pass, which is exactly why the mode escaped a static test |

**Extent of condition.** Every assembly in the Press 2 suspect window is
treated as suspect until sorted under D3. Part numbers sharing Press 2,
the same die set, or the same terminal/wire combination are listed for
horizontal deployment in D7.

---

## D3 — Interim Containment Actions (ICA)

Containment is designed around the failure physics: the defect is
*intermittent and motion-sensitive*, so a static re-test is **not** valid
containment. Sorting must provoke the failure.

| # | Containment action | Verification of effectiveness |
|---|---|---|
| C1 | Shipment hold on all suspect-window finished goods; suspect lots physically tagged and segregated | Hold list reconciled against traceability records; zero suspect shipments after D0 |
| C2 | 100% sort of suspect inventory with a **flex/wiggle continuity test**: each circuit monitored continuously while the harness is flexed through its service bend envelope; any dropout = reject | Sort effectiveness check: seeded-defect audit — a small set of known-bad sample units (retained failures) is passed through the sort blind; 100% must be caught before the sort is trusted |
| C3 | Press 2 stopped; production moved to Press 1 with first-article crimp-height verification and cross-section at each setup | First-article records reviewed by quality before each restart |
| C4 | In-process crimp-height measurement added temporarily at 30-minute intervals on the running press, with stop-and-call limits | Temporary check sheet reviewed each shift by the line supervisor |
| C5 | Fictional customer escape: customer notified with the failure description and suspect serial range; field units in the range replaced proactively; returned units routed to failure analysis | Return tracking list; returned units confirmed to show the same signature (closes the loop that the escape is the same failure mode, not a new one) |
| C6 | Upstream containment: terminal and wire lots in the suspect window quarantined at incoming pending the D4 material check | Quarantine tags; lots released only after D4 clears material as a cause |

**Containment exit criteria** (all must hold): root cause verified in D4;
permanent corrective actions in D5 implemented on the running process; the
flex test migrated from a sorting tool into the standard final test (D6);
and two consecutive weeks of synthetic-trend-equivalent monitoring with no
recurrence of the signature. In the synthetic data narrative, containment
lands during week 14 — the FPY series turns up from week 15 onward
(synthetic weeks 15–26 mean FPY 98.56%, vs. 91.69% for weeks 1–13).

**Containment cost note (method point).** 100% sorting is explicitly a
temporary, expensive bridge. The 8D is not allowed to close on containment;
it closes on prevention (D5–D7).

---

## D4 — Root Cause Analysis

Two root causes are required for closure: the **occurrence** root cause
(why the defect was made) and the **escape** root cause (why the existing
controls did not catch it). A third, systemic layer is addressed in D7.

### D4.1 Fishbone (Ishikawa) — occurrence side

```
        Machine                     Method
   - Die wear beyond life      - No in-process crimp-height SPC;
   - Applicator shut-height      first-article check only
     drift after die change    - Die PM interval based on calendar,
   - Press 2 only                not cycle count
              \                 /
               \               /
   Material     \             /     Measurement
   - Terminal     \           /   - Crimp height measured at setup
     hardness lot   \         /      only; no trend data existed
     variation       \       /    - Micrometer not on a calibration-
                        \   /       recall check for this station
                         \ /
   Manpower               X         Environment
   - Setup tech not     /   \     - (No credible environmental
     trained on post-  /     \      contributor identified;
     die-change        /       \     ruled out by Press 1
     verification     /         \    comparison)
                     /           \
        INTERMITTENT CONTINUITY / STRAND DAMAGE AT CRIMP
```

### D4.2 Evidence review — what was ruled in and out

| Candidate cause | Test / evidence in the scenario | Verdict |
|---|---|---|
| Terminal material lot (hardness variation) | Hardness and plating checks on quarantined lots vs. retained good lots; failure rate does not follow material lot, it follows press and die cycle count | Ruled out as primary cause; kept as a monitoring item in the AQL plan |
| Wire lot / strand count error | BOM and strand-count verification on failed vs. good assemblies | Ruled out |
| Operator build error (wrong routing/pinning) | Failed units are pinned and routed correctly; signature is inside the crimp barrel, not the layout | Ruled out |
| Connector housing | Housing inspection on failures: no cracks, latches intact | Ruled out |
| Crimp die wear + shut-height drift (Press 2) | Crimp height centered ~0.03 mm below the 1.60 mm example nominal (synthetic X-bar baseline 1.5696 mm); cross-sections show strand nicking consistent with over-compression; die cycle count beyond its rated life; rate absent on Press 1 with a younger die | **Ruled in — occurrence root cause** |
| Test coverage gap | Final test = static continuity + insulation only. A static test cannot provoke a motion-sensitive intermittent. Retained failed units pass static test ~half the time on retest (scenario detail) | **Ruled in — escape root cause** |

### D4.3 Five Whys — occurrence root cause

1. **Why** do assemblies fail intermittently? — Crimped terminals have
   damaged conductor strands; the joint carries current when undisturbed
   and opens when flexed.
2. **Why** are strands damaged? — The crimp is over-compressed: crimp
   height runs below the example nominal, crushing strands at the barrel.
3. **Why** is crimp height low? — The Press 2 die is worn past its rated
   life and the applicator shut height drifted after the last die change;
   nothing pulled the process back to center.
4. **Why** did the drift go unnoticed? — Crimp height was verified only at
   first article (setup). There was no in-process SPC, so a slow drift
   produced no signal anyone was watching.
5. **Why** was there no in-process control? — The control plan treated
   crimp height as a setup characteristic, not a process characteristic;
   die maintenance was calendar-based rather than cycle-count-based, so
   wear accumulated invisibly between PM events.

**Occurrence root cause (verified):** die wear and post-change shut-height
drift drove crimp height low (over-compression → strand damage), and the
control plan contained no in-process monitoring that could detect the
drift. **Verification action:** in the scenario, the die is replaced, shut
height is re-qualified, and the press is re-run under measurement: crimp
height re-centers on the nominal (synthetic X-bar subgroups 16–25 mean =
1.6007 mm vs. the 1.60 mm example target), cross-sections show no strand
damage, and the intermittent signature disappears from test. A cause is
only "verified" when turning it off turns the failure off — that test is
what this step documents.

### D4.4 Five Whys — escape root cause

1. **Why** did defective assemblies pass final test and one fictional lot
   ship? — The failure is intermittent; units pass a static continuity
   test while undisturbed.
2. **Why** does the test not provoke the failure? — The final test spec
   contains no flex/motion or thermal stress element for crimped joints.
3. **Why** was the test specced that way? — The test was designed against
   build errors (wrong pin, open solder, shorts) — the failure modes of
   the previous product generation — and was never updated when the
   process moved to this crimped-terminal design.
4. **Why** was it never updated? — Design/process changes did not trigger
   a mandatory test-coverage review against the PFMEA detection controls.

**Escape root cause (verified):** final test coverage did not include a
detection control matched to the crimp failure mode; the PFMEA detection
ranking for "intermittent crimp joint" was therefore optimistic, and no
change-management step forced a re-review.

### D4.5 The charts' role in D4 (synthetic data)

- `../charts/spc_xbar_r.png` — the measurement that should have existed.
  Limits computed from baseline subgroups 1–15 (X-double-bar 1.5696 mm,
  R-bar 0.0415 mm, UCL 1.5935 / LCL 1.5456) show a process centered low
  and stable in its wrongness — a centering problem, not a chaos problem.
  Post-action subgroups 16–25 plot *above* the old UCL, which is the
  chart's way of proving the process genuinely moved; the correct response
  is re-baselining after a new stable run (D6), not celebrating.
- `../charts/spc_pchart.png` — daily defective proportion at final test,
  baseline p-bar 4.16% (days 1–20). No baseline point exceeds its 3-sigma
  limit: the process was "in control" at an unacceptable level, which is
  why no alarm fired. The post-action phase (days 21–30, mean 1.37%)
  sits consistently below the center line — a run-rule shift signal.

---

## D5 — Permanent Corrective Actions (PCA), Chosen

Selection criteria applied to every candidate action: does it attack the
verified root cause (not the symptom), is it effective against
intermittency (the escape physics), is it sustainable on a real line, and
can its effectiveness be measured in D6?

| # | Permanent corrective action | Root cause addressed |
|---|---|---|
| P1 | Replace the worn die set; convert die maintenance from calendar-based to **cycle-count-based** PM with a hard life limit and a die-life counter on the press; production cannot run past the limit without quality release | Occurrence (wear) |
| P2 | Post-die-change and post-setup **re-qualification**: first-article crimp height (5 pcs), cross-section, and pull-force test must pass and be signed by quality before production release | Occurrence (shut-height drift) |
| P3 | **In-process SPC on crimp height**: X-bar/R chart, subgroup of 5 every hour, center/limits per the method in `../charts/spc_xbar_r.png`; reaction plan = stop, segregate since last good subgroup, notify quality | Occurrence (drift detection) |
| P4 | **Final test redesign**: continuous-monitoring flex/wiggle test added for all crimped circuits, so the standard test provokes the intermittent mode instead of hoping to catch it statically | Escape |
| P5 | Control plan and PFMEA updated: crimp height reclassified as a process characteristic with SPC; PFMEA detection ranking for intermittent crimp joints corrected to reflect the pre-fix test, and occurrence ranking tied to die-life controls | Systemic link between occurrence and escape |
| P6 | Incoming inspection tightened for terminals per the AQL plan in `../incoming-inspection/aql-sampling-plan.md` (hardness/plating as monitored characteristics, tightened inspection until the supplier history re-earns normal) | Material monitoring (contributing-factor watch) |

**Rejected alternatives, with reasons (method point — an 8D should show
its discards):** 100% cross-section inspection (destructive, cannot scale,
tests the past not the process); relying on pull-force alone (a damaged-
strand crimp can still pull in-spec — pull force is a necessary monitor,
not a sufficient detector for intermittency); operator retraining as the
sole action (the operators were running a drifting process the system
could not see — blaming the last person who touched it would leave every
cause in place).

---

## D6 — Implementation and Validation of PCA

| Action | Implementation evidence (scenario) | Effectiveness validation |
|---|---|---|
| P1 die PM by cycle count | Press fitted with cycle counter; PM work order system updated; die-life limit set from the die maker's rating minus a safety margin | No die exceeds life in the following synthetic quarter; PM compliance audited in line walks |
| P2 re-qualification | Setup sheet revised; quality sign-off gate added before release | Audit of setup records: 100% of die changes in the validation window have complete re-qualification records |
| P3 crimp-height SPC | X-bar/R charting live at the press; operators trained on the reaction plan; limits re-baselined after 25 new stable subgroups (the original baseline was a decentered process and is retired as a historical record, not reused) | Synthetic post-action subgroups center on nominal (mean 1.6007 mm vs. 1.60 mm target); zero strand-damage cross-sections in the validation sample |
| P4 flex test in final test | Test program updated; test time impact measured and absorbed into line takt planning | Seeded-defect challenge repeated against the *standard* test: known-bad units must fail 100% — the same audit that validated containment sorting, now applied to the permanent test |
| P5 control plan / PFMEA | Documents revised and re-released; change notice includes the test-coverage review trigger (D7) | Document audit; PFMEA detection rankings re-scored by the team, not by one person |
| P6 incoming AQL plan | Plan in force for terminal lots (see `../incoming-inspection/`) | Lot acceptance history reviewed monthly |

**Outcome metrics (synthetic, from this pack's datasets):** FPY weekly
mean rises from 91.69% (weeks 1–13) to 98.56% (weeks 15–26); daily
defective proportion at final test falls from a 4.16% baseline p-bar to a
1.37% post-action mean; crimp height re-centers from 1.5696 mm to
1.6007 mm. These are properties of the synthetic scenario, included to
show *which* metrics an 8D closure should report and in what form — they
are not results from any real line.

**Closure gate:** the 8D does not close when actions are implemented; it
closes when the effectiveness window passes — here, the scenario requires
the flex-test challenge at 100%, SPC live with a re-baselined chart, and a
full synthetic quarter with no recurrence of the intermittent signature
and no die-life overruns.

---

## D7 — Prevent Recurrence / Horizontal Deployment

Systemic lessons, applied beyond the one press and one part number:

1. **Every crimp process, every press, every site building harnesses:**
   cycle-count die PM, post-change re-qualification, and hourly crimp-
   height SPC are deployed to all crimp stations, not only Press 2. The
   suspect part-number list from D2 is worked through one by one; each
   gets either the full control set or a documented risk assessment.
2. **Test-coverage review trigger:** any design or process change that
   alters a joint, interface, or material now requires a documented
   review — "does the current final test provoke the failure modes this
   change creates?" — signed by test engineering before release. This is
   the systemic fix for the D4.4 chain.
3. **PFMEA living review:** detection rankings are re-scored whenever a
   test changes or an escape occurs; an escape automatically reopens the
   detection ranking of the escaped mode at its worst credible value
   until re-proven.
4. **Control-plan classification rule:** any characteristic whose failure
   is intermittent, latent, or motion/thermally sensitive is classified
   as a process characteristic requiring in-process monitoring — setup-
   only verification is explicitly insufficient for that class.
5. **Line walks institutionalized:** the checks that would have caught
   the drift (die-life status, SPC chart alive and reacted to, setup
   records complete) are standing items on the line-walk checklist in
   `../line-walk/line-walk-checklist.md`, so prevention is audited by
   routine, not by memory.
6. **Read-across to other intermittent-prone processes:** the same
   "static test cannot catch a dynamic failure" test-coverage question is
   applied to soldered, bolted, and press-fit joints on the line's other
   products.

---

## D8 — Closure and Team Recognition

**Closure checklist (scenario):**

- [x] Occurrence root cause verified by turn-off test (die replaced and
      re-qualified -> signature gone, process re-centered)
- [x] Escape root cause verified (standard final test now fails 100% of
      seeded known-bad units)
- [x] Containment exited by criteria, not by calendar; sorting labor
      released only after P4 was live
- [x] Fictional customer escape closed: notification, replacement, and
      returned-unit confirmation complete
- [x] Control plan, PFMEA, setup sheets, PM system, and incoming
      inspection plan all revised and re-released
- [x] Horizontal deployment list (D7) dispositioned item by item
- [x] Effectiveness window passed with no recurrence

**Recognition.** The team is thanked by role — in particular the test
engineer whose retest data ("passes half the time") was the observation
that reframed the problem from "bad parts" to "intermittent physics," and
the line supervisor whose sort crews kept containment honest. The lesson
the team carries forward, in one sentence: **a process can be perfectly
in control at an unacceptable center, and a test can be perfectly
repeatable while testing for the wrong failure — both charts and tests
must be aimed at the physics of the failure, not at the habit of the
line.**

---

*End of synthetic 8D case. Companion files: `../charts/fpy_trend.png`,
`../charts/spc_pchart.png`, `../charts/spc_xbar_r.png` (all synthetic),
`../incoming-inspection/aql-sampling-plan.md`,
`../line-walk/line-walk-checklist.md`, and the generator script
`../scripts/generate_charts.py` that produces every number quoted here.*
