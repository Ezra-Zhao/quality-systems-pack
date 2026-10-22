# ISO 9001:2015 Mapping — My Floor Actions to Clauses

Purpose: interview preparation for assembler / production roles that list
"ISO 9001 knowledge" (Atomic Machines Manufacturing Assembler JD names it
explicitly). This is a translation table, not a certification claim:
**I do not hold ISO 9001 certification, and no employer of mine is claimed
here to be ISO 9001 certified.** What I have is floor practice that follows
the same controls the standard names. This file maps that practice, clause
by clause, so I can speak the standard's language about work I actually do.

## Honesty boundary — read this first (same rule as the pack README)

- Two kinds of evidence appear below, and they are tagged on every row:
  - **[Real]** — an action from my actual jobs: Product Engineer (PE) at
    a Tier-1 server ODM (L11/L12 rack-scale server builds, from May 2026) and
    Data Center Infrastructure Engineer at a data-center operator (about
    1,000-rack facility, from Sep 2025).
  - **[Method]** — method demonstrated in this pack. The pack's case, data,
    and numbers are **synthetic** (see README "Honesty boundary"): the 8D
    case is an invented cable-crimp scenario, the FPY / SPC figures are
    generator outputs. They prove I can run the method and write it up;
    they are **not** results from any line I worked on, and I never quote
    them in an interview as my results.
- Interview rule that follows from the above: when a row is tagged
  [Method], I say "in a work sample I built to demonstrate the method…",
  not "on my line we…".

## How to use this file

Each row is: **my action → ISO 9001:2015 clause → how I say it in an
interview** (English line, ready to use). Rows are grouped by the four
areas the Atomic Machines JD names: material verification, defect
reporting, WIP / production records, and document control. A fifth group
covers the supporting clauses (competence, audit, improvement) that an
interviewer may probe next.

---

## Block 1 — Material verification （物料核验）

JD wording: "verify completeness of material to be assembled per the
procedure; visually inspect components and finished units."

| # | My action | ISO 9001:2015 clause | How I say it in an interview |
|---|---|---|---|
| 1.1 | [Real] Before starting a build at the ODM, I verify material completeness against the build package — parts, cables, labels — and I do not start on incomplete or wrong material. At the data-center operator I check replacement hardware against the ticket / work order before a swap. | **8.4.1** Control of externally provided processes, products and services; **8.5.1** Control of production (controlled conditions include availability of documented information and suitable materials) | "Before I build, I verify the kit against the build package. That is incoming control at the point of use — clause 8.4 thinking applied at my station: wrong or incomplete material stops at me, it does not get built in." |
| 1.2 | [Method] In the pack's incoming-inspection plan (`incoming-inspection/aql-sampling-plan.md`), lots are sampled per ANSI/ASQ Z1.4, General Inspection Level II; defects are classified Critical (AQL 0.65) / Major (1.0) / Minor (2.5); acceptance is by Ac/Re per defect class, and a lot must pass every class. | **8.4.2** Type and extent of control; **8.6** Release of products and services | "I have worked through how a Z1.4 sampling plan is actually read — code letter from lot size, sample size, Ac/Re by AQL and defect class — and why an AQL is a process-average concept, not a promise that a lot is defect-free. I wrote that plan as a method sample." |
| 1.3 | [Method] Rejected or held lots are quarantined, tagged, and physically segregated; the line-walk checklist (`line-walk/line-walk-checklist.md`, items A1/A5) audits that only released material is at the line and that the hold list matches what is actually segregated. | **8.4.2**; **8.7.1** Control of nonconforming outputs (identification and segregation) | "A reject is not a note in a system — it is a tagged lot in a segregated area, and the line walk checks the physical state against the hold list." |
| 1.4 | [Method] Destructive and variable characteristics (crimp pull force, cross-section, hardness / plating via certificate of conformance with periodic lab verification) are handled by a special plan, because attribute sampling cannot cover them; measurement tools at the station are zero-checked with calibration in date (line-walk item B5). | **7.1.5** Monitoring and measuring resources (calibration / traceability); **8.4.2** | "Sampling has limits. For a crimp, the destructive tests and the measurement system itself — calibrated micrometer, in-date sticker — are part of the control, which is clause 7.1.5." |
| 1.5 | [Real] Lot / build traceability is kept as I work: cable mapping and label specifications tie each build to its package revision, and finished units are checked against the mapping before sign-off (line-walk items A2/C3 mirror this habit). | **8.5.2** Identification and traceability | "I keep identification with the unit as it moves — labels and cable maps match the build record, so any unit can be traced back to what went into it." |

**Block 1 coverage check:** incoming verification at point of use (1.1),
sampling method (1.2), quarantine of rejects (1.3), measurement control
(1.4), traceability (1.5). All five are actions above, none is aspirational.

## Block 2 — Defect identification and reporting （缺陷上报）

JD wording: "identify and report defective parts."

| # | My action | ISO 9001:2015 clause | How I say it in an interview |
|---|---|---|---|
| 2.1 | [Real] When a build fails at the ODM, I debug it on the floor and isolate the failure to the cable, connector, or component level. I report the defective part with build-floor evidence — what failed, where, under what test — instead of building over it or swapping parts at random. | **8.7.1** Control of nonconforming outputs (identify, document, prevent unintended use); **8.5.1** | "My rule is: never build over a defect. I isolate it to cable, connector, or component, and I report it with evidence, so quality is deciding on facts, not on my opinion." |
| 2.2 | [Real] At the data-center operator, faults are worked through tickets (about 10 per day): intake, localization, resolution, and a written record the next shift can act on. I rewrote the fault-diagnosis SOPs; typical network-cable fault localization went from about 20 minutes to about 5 minutes (MTTR −75%). | **8.7.2** Documented information on nonconformities (description, actions taken, concessions, deciding authority); **9.1.1** Monitoring and measurement | "Every fault leaves a record — what it was, what I did, what closed it. That written trail is what let me rewrite the diagnosis SOP and cut cable-fault localization from about twenty minutes to about five." |
| 2.3 | [Method] The pack's 8D case (`8d-case/8d-report-cable-failure.md`) runs the full D0–D8 discipline on an intermittent crimp failure: containment first (shipment hold, segregation, a sort that provokes the intermittent failure instead of a static re-test, seeded-defect audit of the sort itself), then separate occurrence and escape root causes (two 5-Why chains plus fishbone), permanent corrective actions, validation, and horizontal deployment. | **10.2.1 / 10.2.2** Nonconformity and corrective action (react, evaluate root cause, implement, verify effectiveness, retain documented evidence) | "I built a full 8D as a method sample — synthetic case, and I say so. What it shows is that I know containment is not correction: you hold and sort first, you find why it happened and why it escaped, and the 8D only closes when effectiveness is verified." |
| 2.4 | [Method] In that 8D, the escape root cause is treated as seriously as the occurrence cause: the final test was static, the failure was motion-sensitive, so the test could not catch it — the fix includes redesigning the test and correcting the PFMEA detection ranking. | **10.2.1**; **6.1** Actions to address risks and opportunities | "A defect that ships is two failures: the one that made it and the one that let it through. I always ask both questions." |
| 2.5 | [Real] Fixes are written back into the work instructions and SOPs the same day, so the same failure does not recur for the next builder (see also Block 4). Reporting is therefore not a dead end — it changes the controlled document. | **10.3** Continual improvement; **10.2.1(f)** Update risks, and if necessary the management system / documents | "When I report a defect, the loop closes the same day: the instruction changes, so the next person cannot repeat the failure the same way." |

**Block 2 coverage check:** identify + document + segregate (2.1, 2.2),
structured corrective action (2.3), escape analysis (2.4), feedback into
documents (2.5).

## Block 3 — WIP and production records （在制品与生产记录）

JD wording: "ensure work-in-progress (WIP) counts and records at the
station are accurate; keep the workstation clean and organized."

| # | My action | ISO 9001:2015 clause | How I say it in an interview |
|---|---|---|---|
| 3.1 | [Real] My stated working standard at the ODM (and the standard in my application resume) is accurate WIP counts and build records at my station, and a clean, organized workstation — only current-build material at the station. The line-walk checklist (items F1/F4) audits exactly this: station state and a line board that matches system data. | **8.5.1** Control of production and service provision; **7.1.3** Infrastructure / work environment | "WIP accuracy is a control, not housekeeping. If the count at my station is wrong, traceability and every downstream decision built on it are wrong." |
| 3.2 | [Method] FPY is tracked weekly and charted (`data/fpy_weekly.csv`, `charts/fpy_trend.png`): first-pass yield by week, read as a trend, with the worst week investigated rather than averaged away. (Synthetic data — method only.) | **9.1.1**; **9.1.3** Analysis and evaluation | "I track first-pass yield as a trend, not a monthly average. Averages hide the week that went wrong; the trend tells you when to go and look." |
| 3.3 | [Method] SPC is run on the characteristic that decides quality — in the pack, crimp height on an X-bar/R chart (subgroup of 5, hourly) and a p-chart for daily defectives — each with a written reaction plan: stop, segregate since the last good subgroup, notify quality (line-walk items B3/B4 check the chart is alive and the reaction plan was actually followed). (Synthetic data — method only.) | **9.1.1**; **8.5.1** (monitoring activities under controlled conditions) | "A control chart nobody reacts to is decoration. In my sample, every out-of-control signal has a reaction plan — stop, segregate back to the last good subgroup, call quality — and the line walk verifies the reaction happened." |
| 3.4 | [Method] Every lot inspection keeps its own record: lot ID, code letter, sample size, AQLs applied, defectives per class, Ac/Re, decision, inspector, date, and the switching-rule state in force (`incoming-inspection/aql-sampling-plan.md`, Section 8). Records feed supplier scorecards and a monthly review. | **8.6** (evidence of conformity with acceptance criteria, traceable to who authorised release); **7.5.3** Control of documented information | "A release decision I cannot reconstruct later did not happen. Each lot record carries the plan that was applied and who decided, so the decision is auditable months later." |
| 3.5 | [Real] Build and ticket records are completed as the work happens, not reconstructed at shift end: Data-center tickets are logged end to end (repairs, root cause, parts used), and ODM build records are verified against the package before sign-off. | **8.5.1**; **8.5.2** | "I write the record while I do the work. End-of-shift reconstruction is how counts drift and handovers fail." |

**Block 3 coverage check:** WIP / station discipline (3.1), yield trend
(3.2), in-process SPC with reaction plan (3.3), release and inspection
records (3.4), contemporaneous recording habit (3.5).

## Block 4 — Document control （文件控制）

JD wording: "follow assembly procedures and work instructions; read
visual aids and mechanical / electrical drawings."

| # | My action | ISO 9001:2015 clause | How I say it in an interview |
|---|---|---|---|
| 4.1 | [Real] I author and maintain the POC build documentation used at workstations across the ODM factory floor: assembly process flow, cable routing and cable mapping, label specifications. The documents are written so a multilingual operator workforce can execute them without ambiguity. | **7.5.2** Creating and updating documented information (identification, format, review and approval); **8.5.1(a)** Availability of documented information defining characteristics and activities | "I sit on both sides of a work instruction: I write the build documents the floor assembles from, and I build from documents myself. Unclear instructions come back to me as line stops — so I write, and read, like it matters." |
| 4.2 | [Real] When a build failure traces back to an instruction, the instruction is corrected and re-issued the same day — the floor never keeps working to a version known to be wrong, and fixes from debug go into the document, not into verbal tradition. | **7.5.3** Control of documented information (distribution, changes, version control); **8.5.6** Control of changes | "A known-wrong instruction still on the floor is a defect waiting for its next unit. My fixes go into the controlled document the same day, so there is one current version and everyone builds to it." |
| 4.3 | [Method] The line-walk checklist makes document currency an audited item, not an assumption: item C1 compares the station copy's revision against the released revision and flags handwritten unofficial edits; item D1 does the same for the test program versus the test spec. | **7.5.3**; **9.2** Internal audit (habit, at line level) | "On a line walk I check the paper itself: station copy revision against the released revision. Handwritten edits on a work instruction are a finding, every time." |
| 4.4 | [Method] In the 8D case, closure requires the control plan, PFMEA, setup sheets, PM system, and incoming plan to be revised and **re-released** — a corrective action is not complete while the governing documents still describe the old process (D6/D8 checklists). | **10.2.1(f)**; **7.5.3**; **8.5.6** | "An 8D is not closed when the press is fixed. It closes when the control plan, the PFMEA, and the setup sheet describe the new process — otherwise the old process is what the next shift runs." |
| 4.5 | [Real] I read and work to visual aids, cable maps, and mechanical / electrical drawings as the normal input to a build, including precise component and connector placement against the drawing — and I flag a drawing / instruction conflict to engineering instead of resolving it silently at the station. | **8.5.1**; **7.5.3** | "If the drawing and the instruction disagree, I stop and raise it. Quietly picking one is how undocumented process changes are born." |

**Block 4 coverage check:** creating documents (4.1), change and version
control (4.2), currency audits (4.3), document update as part of
corrective-action closure (4.4), working to the released revision (4.5).

## Block 5 — Supporting clauses an interviewer may probe

| # | My action | ISO 9001:2015 clause | How I say it in an interview |
|---|---|---|---|
| 5.1 | [Real] I mentor and onboard new hires on the floor at the data-center operator and design build instructions for a multilingual workforce — competence is built deliberately, including making the instruction itself carry part of the training load. | **7.2** Competence; **7.3** Awareness; **7.4** Communication | "I onboard new hires myself, and I write instructions a new operator can succeed with across a language barrier. That is clause 7.2 done at floor level." |
| 5.2 | [Method] The line walk is run on a cadence (quality-led weekly, supervisor each shift start, management monthly in the example), every finding gets an owner and a due date, and closure is verified physically at the next walk — not by email assertion. | **9.2** Internal audit; **9.1.3** | "My line walk produces actions with owners and dates, and the next walk verifies them on the floor. A walk that finds nothing for a month has gone stale — the checklist itself says that." |
| 5.3 | [Method] Process lesson from the SPC work: a process can be *in control* at an *unacceptable* center (the pack's p-chart baseline), and a test can be perfectly repeatable while testing for the wrong failure. Both readings drive action — re-center the process, redesign the test — rather than reassurance. | **6.1** Risks and opportunities; **10.3** Continual improvement | "The two sentences I carry from SPC work: in control is not the same as good, and repeatable is not the same as right. Both charts and tests have to be aimed at the physics of the failure." |
| 5.4 | [Real] First-time-right is my working standard across both jobs: verify before building, catch the defect at my station, keep the record accurate. I describe it as a standard I hold myself to — not as a measured line result, because I do not quote numbers I cannot source. | **5.1 / Clause 0.2 principles** — customer focus and the process approach, as personal working principles | "I will not quote you a yield number for my line, because I do not publish numbers I cannot source. What I can describe, step by step, is the discipline that produces yield — and show you the method sample I built." |

---

## Honest positioning — microscope work and glovebox （显微装配 / 手套箱）

The JD lists glovebox experience and small-part work under a microscope
as **plus items**, not requirements. My honest position, which is also my
interview answer:

- **What is my trade:** precision assembly at rack and component scale —
  complete L11/L12 server systems, cable assemblies and harness routing to
  a cable map, connector seating, torque-controlled fastening to spec,
  label placement to spec, in a ~1,000-rack data-center environment as
  well. Connector-level precision, bend radii, seating verification, and
  working to a drawing are daily work, done by hand, at volume.
- **What I do not claim:** I have **not** done production assembly under a
  microscope, and I have **not** worked in a glovebox. MEMS-scale parts
  (sub-millimetre) are a different scale from rack-scale precision, and I
  will not blur that line in an interview.
- **What I am doing about it:** studying MEMS packaging basics to
  conversational level (about 2 hours of theory, per my preparation plan)
  so I understand the process language; the honest framing is the one in
  my gap analysis: **"rack-level precision assembly is my trade;
  microscope-scale work is what I am adding."**
- **What transfers, stated without inflation:** steady-hand connector and
  terminal work, crimping discipline, ESD and handling care, working to a
  visual aid without improvising, and the habit of stopping on a defect
  instead of forcing a part. Transfer is a claim about habits, not about
  scale experience — the scale itself I would learn on their floor, the
  way I have come up to speed on new hardware in both of my current roles.

Interview line: "Glovebox and microscope work — I have not done those,
and I would rather tell you that plainly. What I do every day is
precision hand assembly at rack and connector scale, to a drawing, with
torque and inspection discipline. The habits transfer; the scale is new,
and I am studying the theory now so I arrive able to talk about it
honestly."

---

*Companion files in this pack: `8d-case/8d-report-cable-failure.md`,
`incoming-inspection/aql-sampling-plan.md`,
`line-walk/line-walk-checklist.md`, `data/` and `charts/` (all synthetic,
as labelled there), and `README.md` for the pack's honesty boundary, which
this file inherits.*
