---
id: hjo-calibration-energies-atomization-reactions-barriers
title: Calibrating the standard models for energetics (HJO 15.6-15.10) - total energies and their contributions, two-point X⁻³ extrapolation, atomization energies, isogyric reaction enthalpies and conformational barriers, with water's atomization energy and barrier to linearity recomputed
summary: For 20 first-row molecules, HF supplies more than 99% of the total energy. Valence doubles give 70-80% of the correlation energy, core doubles about 20% and triples 2-5%. Correlation converges as X⁻³, so two-point extrapolation E_XY = E_HF + (X³E_X − Y³E_Y)/(X³ − Y³) cuts the basis error about tenfold. Extrapolated CCSD(T) gives atomization energies within 1-2 kJ/mol of experiment, except O₃ (−10.7 kJ/mol, a CCSD(T) failure) and HOF (an experimental error). Isogyric reaction enthalpies reach about 2 kJ/mol without extrapolation, and conformational barriers about 1 kJ/mol. Recomputed for water: the barrier to linearity agrees with HJO Table 15.37 to 0.1 kJ/mol in all 21 entries I ran (HF, MP2, CCSD and CCSD(T) in five basis sets, plus 135.8 kJ/mol at CCSD(T)/cc-pCVQZ). The CCSD(T) atomization energy is 943.3 (cc-pCVTZ), 963.5 (cc-pCVQZ) and 974.7 kJ/mol (TQ-extrapolated), against HJO's pcV(56)Z 975.5 and experiment 975.3.
status: in-progress
kind: comparison
level: intermediate
tags: [benchmarking, calibration, basis-set-extrapolation, atomization-energies, reaction-enthalpies, conformational-barriers, ccsd-t, core-correlation, water]
prerequisites: [hjo-calibration-structures-and-dipoles, perturbative-triples-cc2-cc3]
related: [hf-closed-shell-basis-set-trends, standard-models-h2-and-water, moller-plesset-and-coupled-cluster-perturbation-theory, coupled-cluster-hierarchy-and-size-extensivity]
order: 50
date: 2026-11-04
---

## Total energies

**Setup (HJO Sec. 15.6.1).** HF, MP2, CCSD and CCSD(T) energies at the CCSD(T)/cc-pCVQZ geometries; UHF-based for the atoms. Valence calculations go up to cc-pV6Z and all-electron ones up to cc-pCV5Z.

- **"cc-pcV6Z".** cc-pV6Z plus a core correction, all-electron cc-pCV5Z minus valence cc-pV5Z.
- **Remaining errors.** HF at cc-pV6Z is within about 0.1 m$E_h$ of the limit. Correlation at that level is still about 10 m$E_h$ off.

**Extrapolation.** For cardinal numbers $X < Y$:

$$
E_{XY} = E_{\text{HF}}^Y + \frac{X^3E^{\text{cor}}_X - Y^3E^{\text{cor}}_Y}{X^3 - Y^3}.
$$

- **Accuracy.** cc-pCV(56)Z is within about 1 m$E_h$ of the R12 limit.
- **Linearity.** The formula is linear in the energies, so it can be applied before or after forming energy differences.

**Contributions (HJO Secs. 15.6.2 and 15.6.7).**

- **Correlation per electron.** About −37 m$E_h$ in the molecules and −30 in the atoms. It ranges from H₂ (−20.4) through CH₄ and CH₂ (−30) to F₂ (−42.0) and O₃ (−44.4).
- **Atoms versus molecules.** Open-shell atoms are less correlated than the closed-shell molecules: N −26.3 against N₂ −39.2 m$E_h$ per electron.
- **Bonded by correlation.** For O₃ and F₂ the HF energy actually *rises* on bonding (+3.8 and +3.3 m$E_h$).
- **Shares of the total.** HF is more than 99.5% of the total energy. Correlation splits into valence doubles 70-80%, core doubles about 20%, and triples 2-5% (O₃) with a negligible core part.
- **Other corrections.**
  - The zero-point vibrational energy (about +0.03%) is comparable to the triples but opposite in sign.
  - Scalar relativity (about 0.05%) largely cancels in chemistry.

!!! example "Water, all-electron CCSD(T) at its CCSD(T)/cc-pCVQZ geometry (computed for this note; $E_h$)"
    | | cc-pCVTZ | cc-pCVQZ | (TQ) extrapolated | HJO cc-pcV(56)Z |
    |---|---:|---:|---:|---:|
    | $E_{\text{HF}}$ | −76.057347 | −76.064933 | | −76.0674 (cc-pV6Z) |
    | $E_{\text{cor}}$ | −0.332441 | −0.356035 | −0.373252 | |
    | $E_{\text{CCSD(T)}}$ | −76.389788 | −76.420968 | −76.438185 | −76.439 |

    The TQ extrapolation recovers the cc-pCVQZ shortfall to within about 1 m$E_h$ of HJO's best value.

## Atomization energies

**Findings (HJO Sec. 15.7).** The errors are dominated by correlation, and HF fails badly: it gives negative atomization energies for F₂ (−155) and O₃ (−238 kJ/mol).

**CCSD(T) errors against experiment** (mean / mean absolute, kJ/mol; HJO Table 15.23):

| Basis | Unextrapolated | Extrapolated |
|---|---|---|
| cc-pCVTZ | −34.9 / 34.9 | (DT) −16.2 / 16.2 |
| cc-pCVQZ | −14.3 / 14.3 | (TQ) −1.1 / 2.6 |
| cc-pCV5Z / (56) | −7.4 / 7.4 | (56) −0.9 / 1.4 |

- **Best results (Table 15.28).** Extrapolated CCSD(T) is typically within 1-2 kJ/mol of experiment; F₂ is 2.3 kJ/mol off.
- **O₃.** −10.7 kJ/mol, a genuine CCSD(T) failure from missing connected quadruples in this multiconfigurational case.
- **HOF.** 662.9 against 674.9(42) kJ/mol; HJO attribute the gap to the experiment.
- **Core correlation.** It can be estimated from all-electron cc-pCV(X−1)Z calculations.

!!! example "Water atomization energy $D_e$, all-electron CCSD(T), UHF-CCSD(T) atoms (computed for this note; kJ/mol)"
    | cc-pCVTZ | cc-pCVQZ | cc-pCV(TQ)Z | HJO cc-pcV6Z | HJO cc-pcV(56)Z | Experiment |
    |---:|---:|---:|---:|---:|---:|
    | 943.3 | 963.5 | 974.7 | 972.7 | 975.5 | 975.3(2) |

    - **Without extrapolation.** The errors (−32.0 and −11.8) are close to HJO's sample means for these bases.
    - **With extrapolation.** A cheap TQ extrapolation (−0.6) beats HJO's unextrapolated sextuple-zeta number.

## Reaction enthalpies

**Isogyric reactions (HJO Sec. 15.8).** Reactions that conserve the number of unpaired electrons are much easier than atomizations.

- **HF level.** Mean absolute error 16%; the order of exothermicity is right for all but two reactions.
- **Correlated levels.** MP2 and CCSD reduce the error to about 4% (14-15 kJ/mol), and CCSD(T) to about 1% (2 kJ/mol).
- **Outliers.** Only the reactions involving O₃ (R17, −11.1 kJ/mol) and HOF are significantly off.
- **Basis.** cc-pCVQZ suffices; even cc-pCV(DT)Z is useful, and the triples can be computed in cc-pCVTZ.
- **Vibrations.** Zero-point corrections often exceed the correlation corrections and must be included.

## Conformational barriers

**Water's barrier to linearity (HJO Sec. 15.9.1).**

- **Experiment.** The electronic part of the barrier is 131.2 kJ/mol.
- **HJO's estimate.** HF limit 134.5, valence correlation −1.1(2) and core correlation −1.2, giving 132.2(2) kJ/mol, 1 kJ/mol above experiment.
- **Correlation sign.** The correlation correction changes sign with cardinal number, which makes the basis-set limit hard to pin down.

!!! example "HJO Table 15.37 recomputed: electronic barrier to linearity of water (kJ/mol; computed for this note)"
    **Geometries.** My CCSD(T)/cc-pCVQZ optimized bent and linear structures (95.71 pm / 104.23° and 93.18 pm). Valence sets correlate the valence electrons only; core-valence sets correlate all electrons.

    | Basis | HF | MP2 | CCSD | CCSD(T) |
    |---|---:|---:|---:|---:|
    | cc-pVDZ | 146.0 | 150.2 | 152.3 | 153.4 |
    | cc-pVTZ | 137.7 | 139.0 | 141.2 | 141.9 |
    | cc-pVQZ | 135.7 | 134.3 | 136.8 | 137.0 |
    | cc-pCVDZ | 145.6 | 150.0 | 152.0 | 153.2 |
    | cc-pCVTZ | 137.8 | 137.9 | 140.2 | 140.9 |
    | cc-pCVQZ | | | | 135.8 |

    - **Agreement.** All 21 numbers equal HJO's to 0.1 kJ/mol.
    - **Correlation sign.** The correlation correction is positive in small bases and turns negative only from quadruple-zeta onward, as HJO show in Fig. 15.19.

**Other barriers (HJO Secs. 15.9.2-15.9.3, quoted).** NH₃ inversion: calculated 21.1 against experimental 21.2 kJ/mol (electronic). Ethane torsion: 11.5 against 11.4 kJ/mol.

## HJO's conclusions

**CCSD(T) as a peer of experiment (HJO Sec. 15.10).** For small first-row molecules, CCSD(T) with a large basis matches the best experiments:

- bond lengths to 0.1-0.2 pm and angles to 0.1-0.2°;
- equilibrium dipoles to 0.01-0.02 D;
- atomization energies to 1-2 kJ/mol;
- reaction enthalpies to about 2 kJ/mol;
- barriers to about 1 kJ/mol;
- van der Waals interaction energies within the experimental uncertainty (Ne₂ −132 against −134 µ$E_h$; water dimer −7.9 against −8.6(11) m$E_h$; HJO Sec. 8.5).

It refutes some experiments (H₂O₂ structure, HOF atomization energy) and fails only where static correlation is strong (O₃).

**Outlook.** Density-functional methods are cheaper but cannot be systematically improved. Heavier elements need relativistic treatments.

## Source

Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, Chichester, 2000), Secs. 15.6-15.10, pp. 840-882, Eq. (15.6.3), Tables 15.12-15.39, Figs. 15.9-15.19. Recomputed for this note with PySCF 2.14 (`hjo/c15/water.py`, `hjo/c15/barrier.py`, `hjo/c15/atomz.py`). Experimental values and HJO's statistics are quoted.
