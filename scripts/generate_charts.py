#!/usr/bin/env python3
"""
generate_charts.py -- quality-systems-pack chart generator

Generates ALL charts and data files in this pack from SYNTHETIC data only.
No real factory, supplier, employer, or customer data is used anywhere.
Every data point is simulated with a fixed random seed so the whole chain
is reproducible with one command:

    python3 scripts/generate_charts.py

Outputs:
    data/fpy_weekly.csv            weekly first-pass-yield (synthetic)
    data/spc_pchart_daily.csv      daily defective counts for a p-chart (synthetic)
    data/spc_xbar_crimp.csv        crimp-height subgroups for X-bar/R charts (synthetic)
    charts/fpy_trend.png           FPY trend chart
    charts/spc_pchart.png          p-chart (proportion defective)
    charts/spc_xbar_r.png          X-bar and R charts (crimp height)

The scenario behind the numbers matches the synthetic 8D case in
8d-case/8d-report-cable-failure.md: a rack cable-assembly failure mode
(wrong pin retention / intermittent continuity) that is contained around
week 14 of the FPY series, after which yield improves.
"""

import csv
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

SEED = 42
ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
CHART_DIR = ROOT / "charts"
DATA_DIR.mkdir(parents=True, exist_ok=True)
CHART_DIR.mkdir(parents=True, exist_ok=True)

SYNTH_TAG = "SYNTHETIC DATA - method demonstration only, not real production data"

rng = np.random.default_rng(SEED)


# ---------------------------------------------------------------- FPY trend
def build_fpy():
    """26 weeks of synthetic first-pass yield for rack cable assemblies.

    Weeks 1-13: process running with the latent failure mode present,
    true first-pass probability drifts around 0.90-0.94 with a bad week 9.
    Week 14: 8D containment + corrective action lands (see 8D case, D3/D5).
    Weeks 15-26: true first-pass probability around 0.975-0.99.
    """
    weeks = np.arange(1, 27)
    units = rng.integers(180, 261, size=26)
    true_p = np.concatenate(
        [
            rng.normal(0.920, 0.012, size=8),   # weeks 1-8
            [0.862],                            # week 9: escape cluster week
            rng.normal(0.925, 0.012, size=4),   # weeks 10-13
            [0.948],                            # week 14: containment in place
            rng.normal(0.982, 0.006, size=12),  # weeks 15-26 after fix
        ]
    )
    true_p = np.clip(true_p, 0.80, 0.995)
    passed = rng.binomial(units, true_p)
    fpy = passed / units * 100.0

    path = DATA_DIR / "fpy_weekly.csv"
    with path.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["week", "units_tested", "first_pass_units", "fpy_percent"])
        for wk, n, p, y in zip(weeks, units, passed, fpy):
            w.writerow([int(wk), int(n), int(p), f"{y:.2f}"])

    fig, ax = plt.subplots(figsize=(10, 4.6))
    ax.plot(weeks, fpy, marker="o", linewidth=1.8, markersize=4, color="#1f6fb2")
    ax.axhline(95.0, color="#c0392b", linestyle="--", linewidth=1.2,
               label="Illustrative target 95% (example only)")
    ax.axvline(14.5, color="#555555", linestyle=":", linewidth=1.2)
    ax.annotate("Synthetic 8D corrective action\nlands after week 14 (D5)",
                xy=(15.3, 88.5), fontsize=8, color="#333333")
    ax.set_xlabel("Production week (synthetic calendar)")
    ax.set_ylabel("First pass yield (%)")
    ax.set_ylim(82, 100.5)
    ax.set_xticks(weeks[::2])
    ax.grid(True, alpha=0.3)
    ax.legend(loc="lower right", fontsize=8)
    ax.set_title("FPY Trend - Rack Cable Assemblies (Weekly)\n" + SYNTH_TAG,
                 fontsize=10)
    fig.tight_layout()
    out = CHART_DIR / "fpy_trend.png"
    fig.savefig(out, dpi=150)
    plt.close(fig)

    pre = fpy[:13].mean()
    post = fpy[14:].mean()
    return {
        "file": str(path.relative_to(ROOT)),
        "chart": str(out.relative_to(ROOT)),
        "weeks": 26,
        "total_units": int(units.sum()),
        "mean_fpy_weeks_1_13": round(float(pre), 2),
        "mean_fpy_weeks_15_26": round(float(post), 2),
        "min_week": int(weeks[int(np.argmin(fpy))]),
        "min_fpy": round(float(fpy.min()), 2),
    }


# ---------------------------------------------------------------- p-chart
def build_pchart():
    """30 production days of synthetic cable-assembly final-test results.

    Subgroup = one day of finished cable assemblies checked at final test.
    Days 1-20 form the baseline phase (control limits computed from them);
    days 21-30 are plotted against the same limits to show the process
    shift after the 8D corrective action.
    """
    days = np.arange(1, 31)
    n = rng.integers(110, 141, size=30)
    true_p = np.concatenate(
        [rng.normal(0.046, 0.006, size=20), rng.normal(0.016, 0.004, size=10)]
    )
    true_p = np.clip(true_p, 0.004, 0.08)
    defectives = rng.binomial(n, true_p)
    phat = defectives / n

    base_n, base_d = n[:20], defectives[:20]
    pbar = base_d.sum() / base_n.sum()
    sigma = np.sqrt(pbar * (1 - pbar) / n)
    ucl = np.minimum(pbar + 3 * sigma, 1.0)
    lcl = np.maximum(pbar - 3 * sigma, 0.0)

    path = DATA_DIR / "spc_pchart_daily.csv"
    with path.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["day", "sample_size_n", "defectives", "p_hat",
                    "ucl", "center_line_pbar", "lcl"])
        for d, ni, di, ph, u, l in zip(days, n, defectives, phat, ucl, lcl):
            w.writerow([int(d), int(ni), int(di), f"{ph:.4f}",
                        f"{u:.4f}", f"{pbar:.4f}", f"{l:.4f}"])

    fig, ax = plt.subplots(figsize=(10, 4.6))
    ax.plot(days, phat * 100, marker="o", linewidth=1.6, markersize=4,
            color="#1f6fb2", label="Daily % defective (synthetic)")
    ax.plot(days, ucl * 100, color="#c0392b", linestyle="--", linewidth=1.1,
            label="UCL (from days 1-20 baseline)")
    ax.plot(days, np.full(30, pbar * 100), color="#2e7d32", linewidth=1.2,
            label="Center line p-bar (baseline)")
    ax.plot(days, lcl * 100, color="#c0392b", linestyle="--", linewidth=1.1,
            label="LCL (from days 1-20 baseline)")
    ax.axvline(20.5, color="#555555", linestyle=":", linewidth=1.2)
    ax.annotate("Post-action phase\n(same baseline limits)",
                xy=(21, (pbar + 0.035) * 100), fontsize=8, color="#333333")
    out_of_control = [int(d) for d, ph, u, l in zip(days, phat, ucl, lcl)
                      if ph > u or ph < l]
    for d in out_of_control:
        ax.plot(d, phat[d - 1] * 100, marker="o", markersize=11,
                markerfacecolor="none", markeredgecolor="#c0392b",
                markeredgewidth=1.6)
    ax.set_xlabel("Production day (synthetic calendar)")
    ax.set_ylabel("Defective (%)")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper right", fontsize=8)
    ax.set_title("SPC p-Chart - Cable Assembly Final Test, Proportion Defective\n"
                 + SYNTH_TAG, fontsize=10)
    fig.tight_layout()
    out = CHART_DIR / "spc_pchart.png"
    fig.savefig(out, dpi=150)
    plt.close(fig)

    return {
        "file": str(path.relative_to(ROOT)),
        "chart": str(out.relative_to(ROOT)),
        "subgroups": 30,
        "baseline_pbar_percent": round(float(pbar * 100), 2),
        "out_of_control_days": out_of_control,
        "post_action_mean_percent": round(float(phat[20:].mean() * 100), 2),
    }


# ---------------------------------------------------------------- X-bar / R
# Standard control-chart constants for subgroup size n = 5
# (standard SPC constant table, e.g. Montgomery, Introduction to
# Statistical Quality Control): A2 = 0.577, D3 = 0 (no lower limit
# tabulated for n <= 6), D4 = 2.574.
A2, D3, D4 = 0.577, 0.0, 2.574


def build_xbar_r():
    """25 subgroups x 5 crimp-height measurements (mm), synthetic.

    Crimp height is the classic cable-termination process variable:
    it is what the 8D case identifies as drifting when the crimp press
    die wears. Nominal target in this example: 1.60 mm.
    Subgroups 1-15 run with a slightly low, drifting process mean;
    subgroups 16-25 run after die replacement and setup re-qualification.
    Control limits are computed from subgroups 1-15 (baseline phase).
    """
    subgroups = np.arange(1, 26)
    pre = rng.normal(1.575, 0.018, size=(15, 5)) - np.linspace(0, 0.012, 75).reshape(15, 5)
    post = rng.normal(1.602, 0.014, size=(10, 5))
    data = np.vstack([pre, post])
    xbar = data.mean(axis=1)
    r = data.max(axis=1) - data.min(axis=1)

    xbarbar = xbar[:15].mean()
    rbar = r[:15].mean()
    x_ucl = xbarbar + A2 * rbar
    x_lcl = xbarbar - A2 * rbar
    r_ucl = D4 * rbar
    r_lcl = D3 * rbar

    path = DATA_DIR / "spc_xbar_crimp.csv"
    with path.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["subgroup", "m1_mm", "m2_mm", "m3_mm", "m4_mm", "m5_mm",
                    "xbar_mm", "range_mm"])
        for i, row in enumerate(data):
            w.writerow([int(subgroups[i])] + [f"{v:.3f}" for v in row]
                       + [f"{xbar[i]:.4f}", f"{r[i]:.4f}"])

    fig, axes = plt.subplots(2, 1, figsize=(10, 6.4), sharex=True)
    ax = axes[0]
    ax.plot(subgroups, xbar, marker="o", linewidth=1.6, markersize=4,
            color="#1f6fb2")
    ax.axhline(x_ucl, color="#c0392b", linestyle="--", linewidth=1.1, label="UCL")
    ax.axhline(xbarbar, color="#2e7d32", linewidth=1.2, label="Center line")
    ax.axhline(x_lcl, color="#c0392b", linestyle="--", linewidth=1.1, label="LCL")
    ax.axhline(1.60, color="#7b1fa2", linestyle=":", linewidth=1.2,
               label="Nominal target 1.60 mm (example spec)")
    ax.axvline(15.5, color="#555555", linestyle=":", linewidth=1.2)
    ax.set_ylabel("X-bar (mm)")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="lower left", fontsize=8, ncol=4)
    ax.set_title("SPC X-bar Chart - Crimp Height, Cable Termination (n=5)\n"
                 + SYNTH_TAG, fontsize=10)

    ax = axes[1]
    ax.plot(subgroups, r, marker="s", linewidth=1.6, markersize=4,
            color="#1f6fb2")
    ax.axhline(r_ucl, color="#c0392b", linestyle="--", linewidth=1.1, label="UCL")
    ax.axhline(rbar, color="#2e7d32", linewidth=1.2, label="Center line (R-bar)")
    ax.axhline(r_lcl, color="#c0392b", linestyle="--", linewidth=1.1, label="LCL")
    ax.axvline(15.5, color="#555555", linestyle=":", linewidth=1.2)
    ax.set_xlabel("Subgroup (baseline = 1-15, post-action = 16-25)")
    ax.set_ylabel("Range R (mm)")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper right", fontsize=8, ncol=3)
    ax.set_title("SPC R Chart - Crimp Height", fontsize=10)

    fig.tight_layout()
    out = CHART_DIR / "spc_xbar_r.png"
    fig.savefig(out, dpi=150)
    plt.close(fig)

    return {
        "file": str(path.relative_to(ROOT)),
        "chart": str(out.relative_to(ROOT)),
        "subgroups": 25,
        "subgroup_size": 5,
        "baseline_xbarbar_mm": round(float(xbarbar), 4),
        "baseline_rbar_mm": round(float(rbar), 4),
        "xbar_ucl_mm": round(float(x_ucl), 4),
        "xbar_lcl_mm": round(float(x_lcl), 4),
        "post_action_xbar_mean_mm": round(float(xbar[15:].mean()), 4),
    }


def main():
    print("quality-systems-pack chart generation")
    print("seed:", SEED)
    print("note:", SYNTH_TAG)
    for name, builder in [("FPY", build_fpy), ("P-CHART", build_pchart),
                          ("XBAR-R", build_xbar_r)]:
        result = builder()
        print(f"\n[{name}]")
        for k, v in result.items():
            print(f"  {k}: {v}")
    print("\nDone. All data is synthetic; see README.md honesty section.")


if __name__ == "__main__":
    main()
