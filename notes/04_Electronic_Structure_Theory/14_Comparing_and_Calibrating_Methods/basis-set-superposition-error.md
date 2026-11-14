---
id: basis-set-superposition-error
title: Basis-set superposition error and the Boys-Bernardi counterpoise correction - the neon dimer, the water dimer and BH
summary: In a finite atom-centred basis each fragment of a complex borrows the functions of its partner, which makes the interaction energy spuriously attractive (BSSE). The counterpoise correction computes the fragments in the full dimer basis using ghost functions; for variational methods it is always positive. Its importance depends on the bond. For the dispersion-bound Ne₂ (HJO Table 8.23 reproduced here) the correction is as large as the interaction itself and uncorrected Hartree-Fock even binds. For the hydrogen-bonded water dimer the corrected energies converge smoothly as X⁻³ and extrapolate well. For covalent BH it can be neglected.
status: in-progress
kind: theory
level: intermediate
tags: [bsse, counterpoise-correction, ghost-functions, intermolecular-interactions, dispersion, hydrogen-bond, neon-dimer, water-dimer, basis-set-convergence]
prerequisites: [gaussian-basis-sets-and-convergence, rhf, mp2]
related: [radial-basis-functions-slater-and-gaussian, size-consistency, coulomb-cusp-and-helium-expansions]
order: 60
date: 2026-11-04
---

## The error and the correction

**Interaction energy.** $\Delta E_{AB} = E_{AB} - E_A - E_B$ (HJO Eq. 8.5.1), with each energy computed in its own basis.

**Where the error comes from.** In the complex, fragment A can use the functions centred on B, so it is described better than in its isolated calculation. The resulting lowering is not a physical interaction, yet it appears in $\Delta E_{AB}$ as extra attraction: the **basis-set superposition error**. It is unavoidable with atom-centred bases ([[radial-basis-functions-slater-and-gaussian]]), and it vanishes only in a complete basis.

**Counterpoise correction (Boys and Bernardi, HJO ref. 28).** Compute every energy in the full dimer basis. The partner's functions are kept as **ghost functions**, with no nucleus and no electrons:

$$
\Delta E^{\text{CP}}_{AB} = E_{AB} - E^{\text{CP}}_A - E^{\text{CP}}_B,\qquad
\delta^{\text{CP}} = \Delta E^{\text{CP}}_{AB} - \Delta E_{AB} = \big(E_A - E^{\text{CP}}_A\big) + \big(E_B - E^{\text{CP}}_B\big).
$$

**Properties.**

- **Sign.** For variational wave functions (HF, FCI) the ghost basis can only lower a fragment energy, so each bracket is non-negative. For nonvariational models (MP2, CC) positivity is not guaranteed but is expected in practice.
- **Geometry.** The ghost functions sit where the partner is in the complex, at the complex geometry. If the two fragments are not equivalent, each needs its own ghost calculation: three calculations in the dimer basis.
- **Fragment relaxation.** Geometry relaxation of the fragments is a separate (physical) term, not part of BSSE.

**Typical interaction energies (HJO).**

- covalent bonds: 100-500 m$E_h$;
- hydrogen bonds: 1-10 m$E_h$;
- dispersion complexes: 50-500 μ$E_h$.

The BSSE matters most in the last case.

## Neon dimer (dispersion)

**HJO's setup.** The empirical well depth is −134 μ$E_h$ at $R$ = 5.84 bohr, less than a millionth of the total energy. HF alone gives pure repulsion in a complete basis.

!!! example "Ne atom errors and counterpoise corrections, and the Ne₂ interaction at 5.84 bohr (computed for this note)"
    **Single Ne atom.** Errors are relative to HF −128.547094 and MP2 −128.867 $E_h$ (the HF limit plus the R12 valence correlation, −0.320). The CPC is computed with a ghost Ne basis at 5.84 bohr. All values in m$E_h$:

    | Basis | HF error | CPC (HF) | MP2 error | CPC (MP2) |
    |---|---:|---:|---:|---:|
    | cc-pVDZ | 58.318 | 0.040 | 192.7 | 0.048 |
    | cc-pVTZ | 15.232 | 0.069 | 70.8 | 0.098 |
    | cc-pVQZ | 3.624 | 0.031 | 30.0 | 0.057 |
    | cc-pV5Z | 0.324 | 0.003 | 14.1 | 0.011 |
    | aug-cc-pVDZ | 50.744 | 0.018 | 163.8 | 0.061 |
    | aug-cc-pVTZ | 13.821 | 0.022 | 61.2 | 0.044 |
    | aug-cc-pVQZ | 3.338 | 0.008 | 26.0 | 0.024 |

    - **Agreement.** HF columns and CPCs agree with HJO Table 8.23 to the last digit. My MP2 errors are 0.1 m$E_h$ smaller (HJO 192.8, 70.9, 30.1, 14.2, 163.9, 61.3, 26.1), probably from rounding of the quoted −128.867 reference.

    **Dimer interaction energy.** μ$E_h$, raw and counterpoise-corrected; PySCF, frozen-core MP2:

    | Basis | HF raw | HF CP | MP2 raw | MP2 CP |
    |---|---:|---:|---:|---:|
    | cc-pVDZ | −36.6 | 44.0 | −65.0 | 31.6 |
    | cc-pVTZ | −52.7 | 84.3 | −157.0 | 39.2 |
    | cc-pVQZ | 28.0 | 89.5 | −109.4 | 4.0 |
    | cc-pV5Z | 88.1 | 93.2 | −43.9 | −22.4 |
    | aug-cc-pVDZ | 62.7 | 97.9 | −114.6 | 7.4 |
    | aug-cc-pVTZ | 49.6 | 94.1 | −128.4 | −40.8 |
    | aug-cc-pVQZ | 76.3 | 92.8 | −110.5 | −61.7 |

    - **Spurious HF binding.** Uncorrected HF binds (−37 to −53 μ$E_h$) in cc-pVDZ and cc-pVTZ. This is pure BSSE.
    - **HF converges once corrected.** The counterpoise-corrected HF interaction settles at 93-98 μ$E_h$ from aug-cc-pVDZ on, close to HJO's limit of +95(1) μ$E_h$.
    - **MP2 is still unconverged.** Corrected MP2 is still only −62 μ$E_h$ at aug-cc-pVQZ, against HJO's limit of −82(2) μ$E_h$. HJO need doubly augmented sets to saturate it.
    - **Raw MP2 is erratic.** Raw MP2 energies jump between −44 and −157 μ$E_h$ as $X$ changes, so they can look close to the experimental −134 μ$E_h$ only by accident.
    - **Size of the CPC.** The correction (24-98 μ$E_h$ for MP2) is as large as the interaction.

**Higher levels (HJO, quoted).**

- **CCSD and CCSD(T).** The estimated limits at 5.84 bohr are −103(2) μ$E_h$ for CCSD and −132(2) μ$E_h$ for CCSD(T), the latter matching experiment. Triples are essential for dispersion.
- **Spurious HF minima.** HJO's raw d-aug-cc-pVDZ HF curve has two: −73 μ$E_h$ at 6.1 bohr and −14 μ$E_h$ at 8.5 bohr.

## Water dimer (hydrogen bond)

**HJO's results (quoted, not recomputed: the CCSD(T)-optimized dimer geometry is not given in the text).**

- **CPC versus basis error.** The CPCs of the monomers are an order of magnitude smaller than their basis-set errors. They fall by a factor of 2-3 per cardinal number for HF and about 2 for MP2. One set of diffuse functions cuts them by a further order of magnitude for HF and by 2-4 for MP2; a second set does not help.
- **MP2 contribution to the interaction energy** (aug-cc-pVXZ, m$E_h$; HJO Table 8.25):

| | D | T | Q | 5 | DT | TQ | Q5 | R12 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Uncorrected | −2.24 | −2.46 | −2.36 | −2.31 | −2.55 | −2.29 | −2.26 | −2.20 |
| CP corrected | −1.27 | −1.82 | −2.03 | −2.11 | −2.05 | −2.19 | −2.19 | −2.20 |

- **Why the raw energies look good.** They benefit from cancellation between BSSE (too attractive) and the incomplete correlation description (too weak). The corrected energies converge like a correlation energy, as $X^{-3}$, so the two-point formula of [[gaussian-basis-sets-and-convergence]] works on them: (T,Q) is already within 0.01 m$E_h$ of R12. For the raw energies, extrapolation makes (D,T) worse.
- **Basis-set limits** of the total interaction energy: HF −5.6, MP2 −7.8(1), CCSD −7.5(1) and CCSD(T) −7.9(1) m$E_h$, against experiment −8.6 ± 1.1 m$E_h$. Electrostatics dominates, so even HF is qualitatively right.

**Check of the extrapolations.** I recomputed the DT, TQ and Q5 columns from the D-5 rows with $E^\ast_{XY}$. They reproduce −2.55/−2.29/−2.26 (raw) and −2.05/−2.19/−2.19 (CP) within ±0.01, the rounding of the inputs.

## BH (covalent bond)

**HJO's cc-pVXZ results (quoted).** At $R$ = 2.3289 bohr the CPC of B is 0.016/0.007/0.002/0.001 m$E_h$ (HF) and 0.391/0.208/0.086/0.041 m$E_h$ (valence FCI) for D-5.

- **Negligible.** The binding energy is about 131 m$E_h$, and HJO's basis-set limits are 103 (HF) and 135 (valence FCI) m$E_h$. The correction is 0.2-0.3% of the binding energy in cc-pVDZ and is small compared with the changes from one cardinal number to the next, so it can be neglected.
- **No diffuse functions.** None are needed for the covalent bond.

## Summary

| Interaction | Size | BSSE | What to do |
|---|---|---|---|
| Dispersion (Ne₂) | ~0.1 m$E_h$ | as large as the interaction | always correct; vary $X$ and augmentation; use high-level correlation |
| Hydrogen bond (H₂O)₂ | ~10 m$E_h$ | ~10% of the interaction | correct with aug sets, then extrapolate in $X$ |
| Covalent (BH) | ~100 m$E_h$ | < 0.5% | can be neglected |

**Practical advice (HJO).** Run sequences of calculations with and without the correction; the uncorrected energies are useful as a convergence check on the corrected ones.

## Source

Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, Chichester, 2000), Sec. 8.5, pp. 327-335, Eqs. (8.5.1)-(8.5.4), Tables 8.23-8.26, Figs. 8.23-8.27. Ne atom and Ne₂ calculations repeated for this note with PySCF 2.14 (ghost atoms, frozen-core MP2). Water-dimer and BH numbers, HJO's basis-set limits and the CCSD/CCSD(T) Ne₂ estimates are quoted from the book.
