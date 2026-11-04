---
id: hjo-calibration-structures-and-dipoles
title: Calibrating the standard models against experiment (HJO 15.1-15.5) - apparent, basis-set and intrinsic errors; bond distances, bond angles and dipole moments for 20 small molecules; recomputed bond lengths for HF, N₂, CO and F₂ and the CCSD(T)/cc-pCVQZ structure of water
summary: HJO compare HF, MP2, MP3, MP4, CISD, CCSD, CCSD(T) and CCSDT with experiment for 20 closed-shell first-row molecules, separating apparent, basis-set, N-electron and intrinsic errors. Bonds lengthen with better correlation and shorten with bigger basis sets. The CC hierarchy converges smoothly (intrinsic bond-length errors about −3, −0.8 and −0.2 pm for HF, CCSD and CCSD(T)), while the MP series oscillates and CISD and MP3 are poor. CCSD(T)/cc-pCVQZ matches experiment to 0.1-0.2 pm and 0.1-0.2°, and to about 0.01 D for dipoles; it refutes the H₂O₂ experiment and fails only for ozone. Recomputed: HJO Table 15.5 for HF, N₂, CO and F₂ in cc-pVDZ (HF, CCSD, CCSD(T), CCSDT) and cc-pVTZ (HF, CCSD, CCSD(T)), all digits but one matching, and water at CCSD(T)/cc-pCVQZ, 95.71 pm and 104.23° (HJO 95.7 pm, 104.2°).
status: in-progress
kind: comparison
level: intermediate
tags: [benchmarking, calibration, bond-lengths, bond-angles, dipole-moments, ccsd-t, mp2, basis-set-convergence, error-statistics]
prerequisites: [perturbative-triples-cc2-cc3, coupled-cluster-hierarchy-and-size-extensivity]
related: [hjo-calibration-energies-atomization-reactions-barriers, hf-closed-shell-basis-set-trends, standard-models-h2-and-water, moller-plesset-and-coupled-cluster-perturbation-theory]
also: [04_Electronic_Structure_Theory/15_Benchmarking_and_Validation/06_Convergence_and_Error_Analysis]
date: 2026-11-04
---

## The sample and the kinds of error

**The molecules (HJO Sec. 15.1).** H₂, CH₂ (¹A₁), CH₄, H₂O, NH₃, HF, N₂, F₂, CO, HCN, HNC, C₂H₂, C₂H₄, CH₂O, HNO, N₂H₂, HOF, H₂O₂, CO₂ and O₃: all closed-shell, first row only.

**How single-reference are they?** HJO judge this from CCSD(T)/cc-pVQZ natural occupations (Table 15.2):

- **Negligible static correlation.** H₂, CH₄, NH₃, HF and H₂O: highest virtual occupation below 0.03.
- **Noticeable static correlation.** F₂, HNO, N₂H₂ and HOF: above 0.09.
- **Strong static correlation.** O₃: 0.218.

**Kinds of error (HJO Sec. 15.2.1).**

- **Apparent error.** The deviation from the exact answer (FCI in a complete basis).
- **Its two parts.** A *basis-set error* (the same model in a complete basis) and an *N-electron error* (FCI in the same basis).
- **Intrinsic error.** The N-electron error in the complete-basis limit.
- **Cancellation.** The two errors often have opposite signs. That allows fortuitous cancellation, as for CISD/cc-pVDZ, the 1970s success.
- **Balance.** A *balanced* calculation is one whose basis-set error is small compared with the model's intrinsic error. A larger basis then buys nothing.

**Statistics (HJO Sec. 15.2.2).** HJO report the mean error $\bar\Delta$, the standard deviation $\Delta_{\text{std}}$, the mean absolute error $\bar\Delta_{\text{abs}}$ and the maximum $\Delta_{\max}$. They visualize them as normal distributions $\exp[-(P - \bar\Delta)^2/2\Delta_{\text{std}}^2]$.

## Bond distances

**Patterns (HJO Secs. 15.3.2-15.3.5).**

- **Basis.** cc-pVDZ → cc-pVTZ shortens bonds by about 0.8 pm (HF) and 1.6 pm (correlated). cc-pVTZ → cc-pVQZ shortens them by only about 0.1 pm.
- **Model ordering.** For every basis, bonds lengthen in the order HF < CISD < MP3 < CCSD < MP2 < CCSD(T) < MP4. HF bonds are always too short and MP4 bonds always too long.
- **Mean errors at cc-pVQZ.** CISD −1.7, MP3 −1.2 and CCSD(T) −0.1 pm. At cc-pVDZ, CISD (+0.3) and MP3 (+0.5) look good only by cancellation.
- **Best at cc-pVTZ.** MP2 (−0.12 pm) and CCSD(T) (+0.01 pm), again partly by cancellation; both get slightly worse at cc-pVQZ.
- **Maximum errors at cc-pVQZ.**
  - HF 8.5 and MP2 1.7 pm, both for F₂.
  - MP3 4.2, MP4 1.5, CCSD 3.0 and CISD 5.7 pm, all for O₃.
  - CCSD(T) only 0.6 pm, for $R_{\text{OO}}$ in H₂O₂.
- **A rationale (HJO Fig. 15.5).**
  - Introducing the doubles at the MP2 level stretches bonds; relaxing them (MP3, CCSD, CISD) contracts them again.
  - Introducing the triples (MP4, CCSD(T)) stretches them; relaxing the triples (CCSDT) contracts them slightly.
  - CCSD(T)/cc-pVQZ benefits from cancellation between neglected triples relaxation and basis incompleteness on one side, and neglected quadruples on the other.

!!! example "HJO Table 15.5 recomputed: equilibrium bond lengths (pm), all electrons correlated (computed for this note)"
    **Method.** Quartic fits to five points spaced 0.75 pm around the minimum. CCSDT is PySCF's `rccsdt`. HJO values in parentheses where they differ.

    | Molecule | Model | cc-pVDZ | cc-pVTZ |
    |---|---|---:|---:|
    | HF | HF | 90.15 | 89.79 |
    | | CCSD | 91.87 | 91.41 |
    | | CCSD(T) | 91.96 | 91.62 |
    | | CCSDT | 91.97 | |
    | N₂ | HF | 107.73 | 106.71 |
    | | CCSD | 111.23 | 109.36 |
    | | CCSD(T) | 111.84 | 110.06 |
    | | CCSDT | 111.80 | |
    | CO | HF | 111.01 | 110.45 |
    | | CCSD | 113.79 | 112.56 |
    | | CCSD(T) | 114.41 | 113.25 |
    | | CCSDT | 114.43 (114.44) | |
    | F₂ | HF | 134.76 (134.77) | 132.89 (132.91) |
    | | CCSD | 143.18 | 139.23 |
    | | CCSD(T) | 145.75 | 141.36 |
    | | CCSDT | 145.76 | |

    - **Agreement.** Every other entry equals HJO's to 0.01 pm. The 0.01-0.02 pm differences are at the level of fit and convergence noise.
    - **Triples.** Even at cc-pVDZ, the full CCSDT triples change bond lengths by at most 0.04 pm relative to (T), here for N₂.

**Higher levels (HJO Secs. 15.3.6-15.3.7).**

- **(T) versus full triples.** (T) overestimates the full-triples effect by 0.4% (HF) to 9.6% (N₂). The CCSDT − CCSD(T) differences are nearly the same at cc-pVTZ and cc-pVQZ, which lets HJO estimate CCSDT/cc-pV5Z.
- **CCSDT/cc-pVQZ.** Mean absolute deviation from experiment 0.11 pm.
- **Core correlation (MP2).** It shortens bonds by about 0.2 pm. All-electron cc-pVTZ overestimates this, especially for bonds to H (worst 0.48 pm, CH in HCN). Add core corrections from cc-pCV(X−1)Z calculations.

**Final structures (HJO Sec. 15.3.9, Table 15.7, CCSD(T)/cc-pCVQZ).** 22 of 29 bonds lie within 0.1 pm of experiment. The exceptions:

- **HNO.** The experiment gives only $R_0$.
- **O₃.** The bond is 0.6 pm too short; the molecule is multiconfigurational.
- **H₂O₂.** 0.5-0.6 pm off; HJO blame the experiment for this nonrigid molecule.

## Bond angles

**Patterns (HJO Sec. 15.4).** Angles follow the same patterns as bonds.

- **Intrinsic errors.** About 1.6° for HF, 0.4° for CCSD and probably 0.1-0.2° for CCSD(T).
- **Basis requirement.** At least cc-pVTZ for correlated models.
- **Outlier.** H₂O₂ (calculated HOO 100.0°, experiment 102.3°), again blamed on the experiment.

!!! example "Water at CCSD(T)/cc-pCVQZ (cc-pVQZ on H), all electrons (computed for this note)"
    **Method.** A 3 × 3 grid fit (±0.4 pm, ±1°).

    **Result.** $R_e$ = 95.714 pm and $\theta_e$ = 104.23°, against HJO Tables 15.7 and 15.9 (95.7 pm, 104.2°) and experiment (95.78 pm, 104.5°). $E$ = −76.420968 $E_h$.

    **The linear form.** Optimized at the same level: $R$ = 93.18 pm, $E$ = −76.369247 $E_h$. The barrier to linearity is therefore 135.8 kJ/mol, which is exactly HJO's CCSD(T)/cc-pCVQZ entry in Table 15.37 ([[hjo-calibration-energies-atomization-reactions-barriers]]).

## Dipole moments

**Findings (HJO Sec. 15.5).**

- **Basis.** Augmented sets are essential; aug-cc-pVTZ usually suffices. The correlation treatment matters more than the cardinal number.
- **Typical errors.** HF 0.1-0.2 D, MP2 0.05 D, CCSD 0.04 D and CCSD(T) under 0.01 D.
- **Experimental equilibrium values.** These exist only for CO, NH₃, HF and H₂O. All but NH₃ are reproduced to 0.01 D. For NH₃ the experiment says 1.56 D and CCSD(T) 1.52 D, which HJO attribute to the experimental analysis.

## Source

Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, Chichester, 2000), Secs. 15.1-15.5, pp. 817-840, Eqs. (15.2.1)-(15.2.6), Tables 15.1-15.11, Figs. 15.1-15.8. Recomputed for this note with PySCF 2.14 (`hjo/c15/bonds.py`, `hjo/c15/water.py`). Experimental values and HJO's statistics are quoted.
