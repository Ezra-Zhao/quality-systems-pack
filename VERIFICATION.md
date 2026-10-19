# VERIFICATION — how this pack was generated and checked

All data and charts in this pack are **synthetic** (see README.md,
"Honesty boundary"). This file records the actual build-time verification
of the generator chain, so a reviewer can confirm the pack is
reproducible and that the numbers quoted in the documents match the
datasets.

## Environment

- Python 3.12.3
- numpy 1.26.4, matplotlib 3.6.3
- Command: `python3 scripts/generate_charts.py` (run from the pack root)

## Run output (actual, captured at build time)

```
quality-systems-pack chart generation
seed: 42
note: SYNTHETIC DATA - method demonstration only, not real production data

[FPY]
  file: data/fpy_weekly.csv
  chart: charts/fpy_trend.png
  weeks: 26
  total_units: 5817
  mean_fpy_weeks_1_13: 91.69
  mean_fpy_weeks_15_26: 98.56
  min_week: 9
  min_fpy: 84.18

[P-CHART]
  file: data/spc_pchart_daily.csv
  chart: charts/spc_pchart.png
  subgroups: 30
  baseline_pbar_percent: 4.16
  out_of_control_days: []
  post_action_mean_percent: 1.37

[XBAR-R]
  file: data/spc_xbar_crimp.csv
  chart: charts/spc_xbar_r.png
  subgroups: 25
  subgroup_size: 5
  baseline_xbarbar_mm: 1.5696
  baseline_rbar_mm: 0.0415
  xbar_ucl_mm: 1.5935
  xbar_lcl_mm: 1.5456
  post_action_xbar_mean_mm: 1.6007
```

Exit code 0; no errors or warnings. The script was run twice
consecutively and the console output was identical across runs
(fixed seed 42, deterministic generation).

## File checksums (md5, at build time)

```
eca3ac080f834d355f07a2fe7b602026  data/fpy_weekly.csv
cc5b4858741b3de2b532a61cacf44e4e  data/spc_pchart_daily.csv
ee78c2767a8feb8c09a9fe57ed2e7ccf  data/spc_xbar_crimp.csv
48ae9e1b54a1fd4128a5ae09c5bbe675  charts/fpy_trend.png
f5b7c0247cb6e43185ddc72eed5b79fd  charts/spc_pchart.png
25088542cef430c3cb9965d683622a53  charts/spc_xbar_r.png
```

## Cross-checks performed

1. **Document numbers vs. datasets.** Every number quoted in the 8D
   report was taken from the run summary above and spot-checked against
   the CSVs: FPY weeks 1–13 mean 91.69%, worst week 9 at 84.18%,
   weeks 15–26 mean 98.56%; p-chart baseline p-bar 4.16% and
   post-action mean 1.37%; X-bar baseline X-double-bar 1.5696 mm,
   R-bar 0.0415 mm, UCL 1.5935 / LCL 1.5456 mm, post-action mean
   1.6007 mm. No other numbers appear as "results" anywhere in the
   pack.
2. **Chart rendering.** The PNGs were visually inspected after
   generation: titles carry the synthetic-data label, axes and legends
   are legible, control-limit lines and annotations render as intended.
3. **Chart-construction method.**
   - p-chart limits: p-bar from baseline days 1–20; per-subgroup
     3-sigma limits using each day's own n (limits step with n, as
     they should for a p-chart). Interpretation note recorded in the
     8D: no baseline point breaches a 3-sigma limit, and the
     post-action signal is a run (all points below the center line),
     not limit breaches — the pack says exactly this and does not
     exaggerate the chart.
   - X-bar/R limits: X-double-bar +/- A2 * R-bar and D3/D4 * R-bar
     with the standard n = 5 constants (A2 = 0.577, D3 = 0,
     D4 = 2.574), computed from baseline subgroups 1–15 only.
     Post-action subgroups plotting above the old UCL is the expected
     signature of a real process shift and is described as such.
   - FPY: binomial draws around a scripted true-yield profile (dip in
     week 9, step improvement after week 14) — the mechanism is
     documented in the generator's docstrings, so a reviewer can see
     exactly how the synthetic story was encoded.
4. **AQL table values.** The code letters, sample sizes, and Ac/Re
   values in `incoming-inspection/aql-sampling-plan.md` follow
   ANSI/ASQ Z1.4 Tables I and II-A (General Inspection Level II,
   single sampling, normal inspection) for lot ranges 281–10,000 and
   AQLs 0.65 / 1.0 / 2.5. The document itself instructs the reader to
   confirm against the licensed current edition and to follow arrow
   rules where they apply.

## Known limitations

- PNG byte-for-byte identity across *different* machines is not
  guaranteed (matplotlib/font rendering can vary); the CSV datasets
  and console summary are the deterministic artifacts.
- The AQL worked table covers four lot-size rows; a production
  adoption would extend it to the operation's full lot-size range
  directly from the standard.
- The 8D is a narrative case: its "verification" steps are described
  in-scenario, not executed — that is inherent to a synthetic method
  demonstration and is labeled as such throughout.
