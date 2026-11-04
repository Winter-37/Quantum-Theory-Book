---
id: exact-wave-function-properties-and-symmetry
title: What an approximate wave function should inherit from the exact one - the HJO checklist, symmetry-closed variational spaces and the symmetry dilemma
summary: HJO list ten properties of the exact electronic wave function that guide the design of approximate models, from particle number and antisymmetry to size-extensivity, spin and point-group symmetry, the cusps, exponential decay and gauge invariance. A linear variational space yields eigenfunctions of a symmetry operator if it is closed under that operator, e.g. complete orbital configurations for S². Nonlinear models must impose symmetry in the parametrization, which can raise the energy (the symmetry dilemma). A HeH⁺ example shows the spin contamination caused by dropping one determinant.
status: in-progress
kind: theory
level: intermediate
tags: [exact-wave-function, symmetry, spin-symmetry, symmetry-dilemma, variational-space, cusp, size-extensivity]
prerequisites: [variational-principle, genealogical-coupling]
related: [size-consistency, upper-bounds-and-interlacing, uhf, h2-dissociation-rhf-uhf, scf-second-order-and-stability, orbital-rotations, hellmann-feynman-and-virial-theorems]
also: [04_Electronic_Structure_Theory/00_Foundations_of_Quantum_Chemistry/05_Variational_Principle]
date: 2026-11-04
---

## Characteristics of the exact wave function (HJO Sec. 4.1)

Approximations should keep as many properties of the exact solution as practical. Many of them are eigenvalue conditions $\hat A|0\rangle = a|0\rangle$ with $[\hat A,\hat H] = 0$.

| # | Property of the exact state | How models handle it |
|---|---|---|
| 1 | Eigenfunction of $\hat N$ | automatic in $F(M,N)$ |
| 2 | Antisymmetric | automatic in second quantization (N-representability is nontrivial in density-functional theory) |
| 3 | Square-integrable (bound states) | automatic with Gaussian orbitals |
| 4 | Variational: $\delta E = 0$ for all variations | built into HF, MCSCF, CI; not CC or MP |
| 5 | Size-extensive: additive energy for noninteracting parts | HF, CC, MP yes; truncated CI no ([[size-consistency]]) |
| 6 | Eigenfunction of $\hat S^2$, $\hat S_z$ | CSFs or complete configurations ([[genealogical-coupling]]) |
| 7 | Point-group irrep ($\hat L^2$, $\hat L_z$ for atoms; $\hat L_z$ for linear molecules) | symmetry-adapted orbitals |
| 8 | Electronic Coulomb cusp at $r_{12} = 0$ (and nuclear cusp) | not reproduced by determinant expansions: slow basis convergence (HJO Ch. 7) |
| 9 | Density decays as $\exp(-2\sqrt{2I}\,r)$ | only through a flexible outer basis |
| 10 | Gauge behaviour under electromagnetic potentials | needed for unambiguous magnetic properties |

Properties 1-3 are imposed without thought; 4-7 are design choices; 8-10 matter in special situations. The cusp (8) is the main obstacle to high accuracy. Variationality (4) and size-extensivity (5) are hard to have together. (The decay exponent in row 9 is the standard form for the density, general knowledge; HJO state exponential decay governed by the first ionization potential $I$.)

## Symmetry in linear variational spaces

**The issue.** $[\hat A,\hat H] = 0$ for exact operators does not make the **matrices** $\mathbf A$ and $\mathbf H$ commute in a finite basis.

**Sufficient condition (HJO Sec. 4.4).** If the variational space is **closed** under $\hat A$ (every $\hat A|i\rangle$ lies in the space), then $\mathbf A\mathbf H = \mathbf H\mathbf A$, the eigenvectors of $\mathbf H$ can be chosen as eigenvectors of $\mathbf A$, and the approximate states are eigenfunctions of the exact operator.

**For $\hat S^2$.** $\hat S^2|\text{det}\rangle$ stays inside the determinant's orbital configuration. Therefore include all or none of the determinants of each configuration. Determinants are automatically $\hat S_z$ eigenfunctions, and in an Abelian point group with symmetry-adapted orbitals they have definite spatial symmetry.

!!! example "Breaking spin symmetry by dropping one determinant (computed for this note)"
    HeH⁺, STO-3G, $R = 1.4632$ bohr, the four $M = 0$ determinants of two orbitals.

    | Space | Energies (hartree) | $\langle\hat S^2\rangle$ |
    |---|---|---|
    | All four determinants | −2.851466, −2.041772, −1.820826, −0.496317 | 0, 2, 0, 0 |
    | $|2\alpha1\beta\rangle$ removed, $|1\alpha2\beta\rangle$ kept | −2.851320, −1.928504, −0.534184 | 0.0002, 0.9766, 0.0232 |

    - **With the open-shell pair broken up, no state is a spin eigenfunction.** The middle state is half singlet, half triplet.
    - **Bounds still hold.** The ground energy rises only slightly, as Cauchy's theorem requires ([[upper-bounds-and-interlacing]]).

## Nonlinear models: imposing symmetry, and its price

**Stationarity is not enough.** For nonlinear parametrizations the stationary conditions do not guarantee symmetry. It must be imposed through the parametrization, e.g. orbital rotations $\exp(-\hat\kappa)$ containing only totally symmetric singlet excitation operators ([[orbital-rotations]]).

**The symmetry dilemma (Löwdin's term, as cited by HJO).** A symmetry-restricted variational minimum lies at or above the unrestricted one. Imposing the correct symmetry may therefore **raise** the energy. RHF versus UHF for stretched H₂ is the standard case: UHF is lower and dissociates correctly but is spin-contaminated ([[h2-dissociation-rhf-uhf]], [[uhf]]). Whether broken symmetry is acceptable depends on the property sought; HJO return to this for RHF instabilities (Sec. 10.10).

## Source

Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, Chichester, 2000), Sec. 4.1, pp. 107-111, Eqs. (4.1.1)-(4.1.17); Sec. 4.4, pp. 135-137, Eqs. (4.4.1)-(4.4.12). The HeH⁺ example was computed for this note with PySCF 2.14.
