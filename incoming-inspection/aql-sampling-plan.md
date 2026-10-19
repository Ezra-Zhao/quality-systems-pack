# Incoming Inspection Sampling Plan — Cable Assembly Components (AQL)

> **METHOD DEMONSTRATION — EXAMPLE PLAN.**
> This is a worked example of how an incoming-inspection sampling plan is
> structured and justified, written for a fictional rack cable-assembly
> operation. The standard referenced (ANSI/ASQ Z1.4) is real and the
> sampling logic, code letters, sample sizes, and acceptance numbers
> below follow its published tables; the part numbers, suppliers, lot
> sizes, and defect classifications are illustrative examples. No real
> supplier or employer material is used.

---

## 1. Scope

Applies to incoming lots of the components that feed rack cable assembly:

| Component family (examples) | Why it is inspected |
|---|---|
| Crimp terminals (loose piece and reeled) | Crimp quality is decided here first: material hardness, plating, and barrel geometry drive crimp integrity downstream |
| Wire / cable (spooled) | Conductor strand count and gauge, insulation integrity |
| Connector housings and latches | Fit, latch retention, molding defects |
| Cable ties, labels, heat-shrink, hardware kits | Completeness and legibility (minor characteristics) |

Finished assemblies are **not** covered by this plan — they get 100%
electrical test on the line. Sampling is for incoming material, where
100% inspection is uneconomical and, for destructive tests (crimp pull
force, cross-section), impossible.

## 2. Standard basis and sampling logic

- **Standard:** ANSI/ASQ Z1.4, *Sampling Procedures and Tables for
  Inspection by Attributes* (the ASQ adoption of ISO 2859-1 / the former
  MIL-STD-105 lineage).
- **Scheme:** single sampling, **General Inspection Level II** (the
  standard's default level when no other level is justified), **normal
  inspection** at plan start, with the standard's switching rules
  (Section 5) governing movement to tightened or reduced inspection.
- **How a plan is read (the logic, step by step):**
  1. Determine the **lot size** N (units in the lot as presented for
     inspection — one delivery, one part number, one supplier lot).
  2. From Z1.4 Table I, lot size + General Level II gives a **sample
     size code letter**.
  3. From Table II-A (single sampling, normal inspection), the code
     letter gives the **sample size n**; the row/column intersection
     with the chosen **AQL** gives the acceptance number **Ac** and
     rejection number **Re**.
  4. Draw n units **randomly** from across the lot (not from the top of
     one box), inspect them against the defect classification in
     Section 4, count defectives per class.
  5. **Accept** the lot for a defect class if defectives <= Ac;
     **reject** (disposition per Section 7) if defectives >= Re. A lot
     must pass every class to be accepted.
- **AQL meaning, stated honestly:** the AQL (Acceptable Quality Limit)
  is the worst *process average* percent defective that is considered
  acceptable for the purposes of the sampling scheme — it is **not** a
  promise that an accepted lot contains no defectives, and it is not a
  per-lot guarantee. Lots near the AQL are accepted most of the time by
  design; the protection against a *bad* lot comes from the operating
  characteristic (OC) curve and from the switching rules over many lots.
  Any plan that quotes an AQL without this caveat is misrepresenting the
  standard.

## 3. Code letters and worked sample plans (General Level II, normal)

Code letters from Z1.4 Table I for the lot sizes this operation sees,
and the corresponding Table II-A plans for the AQLs chosen in Section 4:

| Lot size N | Code letter | Sample size n | Critical AQL 0.65 → Ac/Re | Major AQL 1.0 → Ac/Re | Minor AQL 2.5 → Ac/Re |
|---|---|---|---|---|---|
| 281 – 500 | H | 50 | 0 / 1 | 1 / 2 | 3 / 4 |
| 501 – 1,200 | J | 80 | 1 / 2 | 2 / 3 | 5 / 6 |
| 1,201 – 3,200 | K | 125 | 2 / 3 | 3 / 4 | 7 / 8 |
| 3,201 – 10,000 | L | 200 | 3 / 4 | 5 / 6 | 10 / 11 |

Notes on reading this table:

- Where a table cell in Z1.4 contains an arrow, the standard directs you
  to the first plan in the arrow's direction (different n and Ac/Re).
  The four rows above are stated without arrow adjustments; if a chosen
  AQL/code-letter combination lands on an arrow in the current edition
  of the standard, the arrow governs — always work from the licensed
  current edition of Z1.4, not from memory or from this example.
- Destructive characteristics (crimp pull force, cross-section) cannot
  use these attribute sample sizes economically; they follow the special
  plan in Section 6.
- Reels and spools: the "unit" for terminals on a reel is one terminal;
  sampling points must be spread along the reel (start / middle / end
  and across at least two reels per lot when the lot has several),
  because within-reel position is a real variation source.

## 4. Defect classification and AQL assignment (example)

| Class | AQL | Definition | Examples for cable components |
|---|---|---|---|
| Critical | 0.65 (with Ac = 0 intent at small n; see note) | Defect that can defeat the part's function or create a safety/escape risk downstream | Wrong terminal part or alloy; missing plating on contact surface; conductor strand count wrong; insulation damage exposing conductor |
| Major | 1.0 | Defect likely to cause a line failure, a rework, or reduced service life | Crimp barrel dimension out of tolerance; terminal hardness out of spec; housing latch cracked; wire gauge out of tolerance; insulation nicks not exposing conductor |
| Minor | 2.5 | Cosmetic or convenience defect that does not affect function | Label print smudge; minor housing flash; tie-wrap color variation; packaging count label error |

Note on critical defects: an AQL of 0.65 still mathematically accepts
occasional lots containing a critical defective. For characteristics
classified critical **and** detectable only destructively or by test,
this plan therefore pairs sampling with the line-side controls (100%
final electrical test, first-article qualification) rather than
pretending the sampling plan alone provides zero-defect protection.
Where a critical characteristic can be screened non-destructively at
reasonable cost, screen 100% and use sampling only as an audit.

## 5. Switching rules (Z1.4 scheme discipline)

| Transition | Rule (summary of the standard) |
|---|---|
| Normal -> Tightened | 2 of 5 (or fewer) consecutive lots rejected on original inspection |
| Tightened -> Normal | 5 consecutive lots accepted under tightened inspection |
| Normal -> Reduced | Preceding 10 lots all accepted under normal inspection, total defectives within the standard's limit number, production steady, and quality authority approves |
| Reduced -> Normal | A lot is rejected, or production becomes irregular/delayed, or other conditions warrant |
| Discontinuation | If 10 consecutive lots remain on tightened inspection, sampling under the scheme is suspended pending corrective action by the supplier |

In the context of the synthetic 8D case in this pack: the terminal
supplier starts on **tightened** inspection after the escape, and earns
its way back to normal only through the 5-consecutive-acceptance rule —
seniority and past relationship do not substitute for the rule.

## 6. Special plan — destructive and variable characteristics

| Characteristic | Method | Example frequency | Acceptance basis |
|---|---|---|---|
| Crimp pull force | Destructive pull test on samples crimped with the lot's terminals on the production applicator | 5 pcs per incoming terminal lot, plus at every applicator setup | Each result >= the example minimum pull force for the wire gauge (per the terminal maker's published spec for the actual part — insert real spec at adoption); any single result below minimum = lot hold and investigation, not a statistical average argument |
| Crimp height / cross-section | Micrometer + sectioning of setup samples | At setup qualification only (process control, tracked by SPC — see the 8D case) | Within the drawing tolerance for the terminal/wire combination |
| Terminal hardness / plating thickness | Supplier certificate of conformance, verified by periodic lab audit | CoC every lot; independent verification quarterly or on any lot rejection | CoC values within the material spec; verification result must agree |

## 7. Lot disposition

| Outcome | Disposition |
|---|---|
| Accept (all classes) | Release to stock; inspection record filed with lot traceability |
| Reject | Lot quarantined and tagged; supplier notified with defect data and photos; disposition = return to supplier, or 100% sort at supplier's cost where sorting can actually detect the defect, or use-as-is **only** with a written deviation approved by quality and design — never for critical defects |
| Repeated rejects | Switching rule applies automatically (Section 5); supplier corrective action (8D) requested after the second rejection of the same defect class within a quarter |

## 8. Records

Each lot's record keeps: lot identification and supplier lot number,
code letter, n, AQLs applied, defectives found per class, Ac/Re,
decision, inspector, date, and the switching-rule state in force.
Records are the input to supplier scorecards and to the monthly review
that decides whether any AQL or inspection level needs to change.

---

*Companion files: the 8D case that motivates the tightened-inspection
starting state (`../8d-case/8d-report-cable-failure.md`) and the line-walk
checklist that audits whether incoming holds and quarantine tags are
actually in force (`../line-walk/line-walk-checklist.md`).*
