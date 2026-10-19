# quality-systems-pack

A documentation-style work sample demonstrating production quality
engineering method: a complete 8D corrective-action case, SPC
(statistical process control) charts, an FPY (first pass yield) trend,
an AQL incoming-inspection sampling plan, and a line-walk checklist.

It was built as a skills demonstration for a Production Quality
Engineer application context (rack-level hardware manufacturing). It
shows *method* — how an 8D is structured and closed, how control charts
are computed and read, how a Z1.4 sampling plan is chosen and honestly
interpreted, and how a line walk keeps those controls alive.

## Honesty boundary — read this first

- **Everything in this pack is synthetic.** The case, the company
  context, the part numbers, the dates, and every single data point are
  invented for method demonstration. This is stated again in every
  document and in the title of every chart.
- **No real data appears anywhere.** No employer, contract
  manufacturer, supplier, customer, or production-line data was used,
  copied, or paraphrased. The documents were written clean-room, from
  general quality-engineering knowledge (8D discipline, SPC per
  standard textbook practice, ANSI/ASQ Z1.4 sampling logic).
- **No number in this pack is a real result.** The FPY percentages, the
  defect rates, and the crimp-height measurements are outputs of the
  seeded generator script in `scripts/`. They demonstrate what an 8D
  closure report should quote and in what form; they must never be
  cited as anyone's actual line performance — not in a resume, not in
  an interview, not anywhere.
- The pack demonstrates familiarity with the *methods*. It does not
  claim employment history, certifications, or results.

## Contents

```
quality-systems-pack/
├── README.md                        <- this file
├── VERIFICATION.md                  <- how the pack was built & checked
├── 8d-case/
│   └── 8d-report-cable-failure.md   <- complete D0-D8 case (synthetic):
│                                       rack cable assembly intermittent
│                                       continuity failure; fishbone,
│                                       two 5-Why chains (occurrence +
│                                       escape), containment, PCA,
│                                       validation, horizontal deployment
├── incoming-inspection/
│   └── aql-sampling-plan.md         <- ANSI/ASQ Z1.4 plan: logic, code
│                                       letters, worked Ac/Re table,
│                                       defect classes, switching rules,
│                                       destructive-test special plan
├── line-walk/
│   └── line-walk-checklist.md       <- ready-to-use gemba checklist
│                                       (Markdown tables, 27 items in
│                                       6 sections + action log)
├── scripts/
│   └── generate_charts.py           <- the one generator for all data
│                                       and charts (fixed seed = 42)
├── data/                            <- synthetic datasets (CSV)
│   ├── fpy_weekly.csv               <- 26 weeks: units, first-pass, FPY%
│   ├── spc_pchart_daily.csv         <- 30 days: n, defectives, p, limits
│   └── spc_xbar_crimp.csv           <- 25 subgroups x 5 crimp heights
└── charts/                          <- generated charts (PNG)
    ├── fpy_trend.png
    ├── spc_pchart.png
    └── spc_xbar_r.png
```

## Reproduce the charts

Requirements: Python 3 with `numpy` and `matplotlib`.

```bash
cd quality-systems-pack
python3 scripts/generate_charts.py
```

That one command regenerates every CSV in `data/` and every PNG in
`charts/`, deterministically: the random seed is fixed (42), and the
script prints a summary of each dataset (means, control limits,
out-of-control checks). Two consecutive runs produce identical output;
see `VERIFICATION.md` for the recorded run.

## How the pieces fit together

The pack is one coherent (fictional) story, deliberately:

1. The **8D case** opens when FPY falls — the fall is what the **FPY
   trend chart** shows.
2. Root-cause work identifies crimp-height drift that nobody was
   charting — the **X-bar/R chart** is the control that was missing,
   and the **p-chart** shows why no alarm fired (an in-control process
   running at an unacceptable center/level).
3. The corrective actions include tightening incoming inspection —
   specified in the **AQL plan** — and institutionalizing the audit of
   all of it in the **line-walk checklist**.

## Method references (general knowledge, for the reader)

- 8D: the Ford-originated Eight Disciplines problem-solving structure
  (D0–D8), as taught in standard quality-engineering references.
- SPC constants and chart construction: Montgomery, *Introduction to
  Statistical Quality Control* (A2/D3/D4 for n = 5: 0.577 / 0 / 2.574).
- Sampling: ANSI/ASQ Z1.4, *Sampling Procedures and Tables for
  Inspection by Attributes* — work from the licensed current edition
  for any real adoption; the tables here are worked examples.
