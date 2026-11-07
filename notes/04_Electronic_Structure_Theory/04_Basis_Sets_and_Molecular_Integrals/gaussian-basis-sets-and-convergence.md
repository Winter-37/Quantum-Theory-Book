---
id: gaussian-basis-sets-and-convergence
title: Gaussian basis sets and their convergence - STO-kG, even-tempered and contracted sets, ANOs, correlation-consistent sets and X⁻³ extrapolation
summary: How practical Gaussian basis sets are built (STO-kG fits, energy-optimized primitives, even-tempered exponents, segmented and general contractions, polarization functions, atomic natural orbitals, the correlation-consistent cc-pVXZ, aug-cc-pVXZ and cc-pCVXZ hierarchies) and how energies converge in them. HJO's Ne, N₂ and H₂O tables were recomputed - Hartree-Fock errors that fall almost exponentially with the cardinal number X, valence MP2 and CCSD correlation energies that converge as X⁻³ - and two-point X⁻³ extrapolation from (Q,5) reproduces the R12 basis-set limits to about 1 mE_h.
status: in-progress
kind: theory
level: intermediate
tags: [basis-sets, gaussian-type-orbitals, contracted-gaussians, even-tempered, atomic-natural-orbitals, correlation-consistent, cc-pvxz, basis-set-extrapolation, basis-set-convergence, mp2, ccsd]
prerequisites: [radial-basis-functions-slater-and-gaussian, gaussian-basis-functions, coulomb-cusp-and-helium-expansions]
related: [pople-basis-sets, basis-set-superposition-error, hf-closed-shell-basis-set-trends, mp2, coupled-cluster-doubles, natural-orbitals, solid-harmonics-angular-basis]
order: 50
date: 2026-11-04
---

## Gaussians for Hartree-Fock

**STO-kG.** Each STO is fitted by least squares with $k$ Gaussians. Fits for $\zeta = 1$ scale to any exponent as $\alpha\to\zeta^2\alpha$. In STO-3G the $2s$ and $2p$ functions share exponents ([[pople-basis-sets]]).

- **Fit quality.** HJO's STO-3G $1s$ (Table 8.1) has overlap 0.99983 with the $\zeta = 1$ STO (computed for this note).
- **Limitation.** The fit is only as good as the STO it copies. The single $2p$ STO is a poor carbon $2p$ orbital.

**Energy-optimized primitives.** Huzinaga's carbon (9s5p) set (HJO Table 8.2) is optimized directly for the HF energy. Optimizing exponents is a nonlinear problem with many minima, and it has to be redone for every atom.

**Even-tempered sets.** The optimized exponents are close to a geometric sequence:

$$
\alpha_k = \alpha\beta^{\,k-1},\qquad k = 1,2,\dots
$$

!!! example "Even-tempered fit of the Huzinaga (9s5p) exponents (computed for this note)"
    A least-squares fit of $\ln\alpha_k$ against $k$ gives $\alpha_s = 0.1364$, $\beta_s = 3.381$ and $\alpha_p = 0.1041$, $\beta_p = 3.503$, identical to HJO Eqs. (8.2.12)-(8.2.13).

    - **Two numbers per $l$.** These replace 9 and 5 optimized exponents.
    - **Systematic.** The set is extended by adding terms and approaches completeness as $\beta\to1$ with the range growing ([[radial-basis-functions-slater-and-gaussian]]).

**Contraction.** Core orbitals need tight primitives that hardly change in molecules, so primitives are combined with fixed coefficients into **contracted GTOs**: $\chi = \sum_kd_k\,g_k$.

- **Segmented contractions** (e.g. Dunning's [3s2p] from (9s5p), HJO Table 8.3) use each primitive in one contracted function only.
- **General contractions** let every contracted function use all primitives (e.g. the occupied atomic orbitals themselves). They are more accurate per function but need integral codes that exploit shared primitives.
- **Split valence** (6-31G and the like) keeps the outer valence primitives free, so the valence shell can expand or contract in the molecule.

**Polarization functions.** Functions of higher $l$ than the occupied atomic orbitals (d on C, N, O; p on H) describe the distortion of atoms in bonds. HJO show they matter more for structure than energy: the 6-31G HOH angle is 111.6°, 6-31G* gives 105.6° and 6-31G** 106.1°, against the HF limit of 106.3° (HJO Table 8.16, quoted).

## Gaussians for correlated calculations

**Correlation needs different functions.** Correlation is dominated by short-range, high-$l$ functions that overlap the occupied orbitals strongly (compact, not diffuse; [[coulomb-cusp-and-helium-expansions]]).

**Atomic natural orbitals (ANOs).**

- **Construction.** Diagonalize the one-particle density matrix of a correlated atomic calculation; keep the natural orbitals with the largest occupations ([[natural-orbitals]]).
- **Pattern.** Occupation numbers fall in groups: the first correlating $p$, $d$ (and $s$) orbitals have similar occupations, then the next group, and so on. Natural truncation points therefore add one function of each $l$ at a time. HJO report that [3s2p1d] recovers about 85% of the carbon correlation energy and [4s3p2d1f] about 95% (quoted), and that the incremental energies follow the same pattern as the occupations.

**Correlation-consistent sets (Dunning).** The cc-pVXZ sets add correlating functions in groups that lower the energy by similar amounts. For first-row atoms (HJO Table 8.13):

| $X$ | cc-pVXZ | $N_v$ | cc-pCVXZ adds | $N_{cv}$ | aug-cc-pVXZ adds | $N_{\text{aug}}$ |
|---|---|---:|---|---:|---|---:|
| D | [3s2p1d] | 14 | 1s1p | 18 | 1s1p1d | 23 |
| T | [4s3p2d1f] | 30 | 2s2p1d | 43 | 1s1p1d1f | 46 |
| Q | [5s4p3d2f1g] | 55 | 3s3p2d1f | 84 | 1s1p1d1f1g | 80 |
| 5 | [6s5p4d3f2g1h] | 91 | 4s4p3d2f1g | 145 | 1s1p1d1f1g1h | 127 |

These counts use spherical harmonics, and they agree with the basis sizes PySCF reports for Ne (14, 30, 55, 91).

**Three families.**

- **cc-pVXZ** correlates the valence electrons. The highest $l$ equals $X$, and it is built from HF orbitals plus correlating shells, like the principal expansion of helium.
- **cc-pCVXZ** adds tight functions for core-core and core-valence correlation.
- **aug-cc-pVXZ** adds one diffuse function per $l$, for anions, polarizabilities and weak interactions ([[basis-set-superposition-error]]).

!!! example "Carbon ³P with cc-pVXZ (HJO Table 8.12 versus my ROHF)"
    | Basis | HJO $E_{\text{HF}}$ | My ROHF |
    |---|---:|---:|
    | cc-pVDZ | −37.682391 | −37.682418 |
    | cc-pVTZ | −37.686662 | −37.686708 |
    | cc-pVQZ | −37.688234 | −37.688298 |
    | cc-pV5Z | −37.688571 | −37.688643 |

    - **Why mine are lower.** My ROHF energies are 0.03-0.07 m$E_h$ lower. My 5Z value even lies below HJO's HF limit (−37.688619), because my D₂h calculation occupies $p_x$ and $p_y$ and breaks spherical symmetry. HJO's energies are for symmetry-restricted (spherical) orbitals.
    - **Same convergence pattern.** Errors relative to HJO's HF limit (−37.688619) fall by factors of 3.2, 5.1 and 8 from D to 5.

## Convergence: Hartree-Fock

**HF errors (my calculations).** I recomputed HJO Table 8.16 at the experimental geometries (N₂ $R$ = 1.0977 Å; H₂O $R$ = 0.9572 Å, angle 104.52°). The table gives errors in m$E_h$ relative to the numerical HF energies (Ne −128.547094, N₂ −108.9931881) and, for water, the cc-pV6Z energy −76.067401.

| Basis | Ne | N₂ | H₂O |
|---|---:|---:|---:|
| STO-3G | 1942.57 | 1497.29 | 1104.47 |
| 6-31G | 73.22 | 125.42 | 83.40 |
| 6-311G | 24.54 | 99.02 | 58.01 |
| 6-31G* | 73.22 | 51.32 | 58.27 |
| 6-31G** | 73.22 | 51.32 | 44.75 |
| 6-311G** | 24.54 | 23.76 | 20.95 |
| cc-pVDZ | 58.32 | 39.06 | 40.60 |
| cc-pVTZ | 15.23 | 9.72 | 10.23 |
| cc-pVQZ | 3.62 | 2.10 | 2.57 |
| cc-pV5Z | 0.32 | 0.42 | 0.31 |

- **Agreement.** Every entry agrees with HJO to 0.01 m$E_h$ (HJO: N₂ 125.43, 2.11, 0.43).
- **Polarization and atoms.** Polarization functions do nothing for atomic Ne, which has no polarizing environment (6-31G = 6-31G* = 6-31G**), but they help N₂ greatly.
- **Rate.** From cc-pVTZ on, each step in $X$ cuts the error by a factor of 4-11 (Ne 4.2 then 11; N₂ 4.6 then 5.0; H₂O 4.0 then 8.3). The convergence is roughly exponential (compare Ne: 58, 15, 3.6, 0.32).

## Convergence: correlation energy

**Correlation energies (my calculations).** Frozen-core valence MP2 and CCSD correlation energies in m$E_h$, HJO Table 8.18 recomputed:

| Basis | Ne MP2 | Ne CCSD | N₂ MP2 | N₂ CCSD | H₂O MP2 | H₂O CCSD |
|---|---:|---:|---:|---:|---:|---:|
| 6-31G | −113.4 | −114.3 | −236.4 | −225.8 | −127.8 | −134.4 |
| 6-31G** | −150.3 | −152.2 | −305.3 | −308.3 | −194.6 | −203.8 |
| 6-311G** | −209.0 | −210.6 | −326.4 | −326.3 | −217.4 | −224.9 |
| cc-pVDZ | −185.5 | −189.0 | −306.3 | −309.3 | −201.6 | −211.2 |
| cc-pVTZ | −264.3 | −266.3 | −373.7 | −371.9 | −261.5 | −267.4 |
| cc-pVQZ | −293.6 | −294.7 | −398.7 | −393.1 | −282.8 | −286.0 |
| cc-pV5Z | −306.2 | −305.5 | −409.1 | (−400.6) | −291.5 | (−292.4) |
| HJO cc-pV6Z | −311.8 | −309.9 | −413.8 | −403.7 | −295.2 | −294.9 |
| HJO R12 limit | −320(1) | −316(1) | −421(2) | −408(2) | −300(1) | −298(1) |

- **Sources.** All my values equal HJO's to 0.1 m$E_h$ (N₂ cc-pVQZ MP2: HJO −398.8). Values in parentheses and the last two rows are quoted from HJO, not computed: I did not run CCSD in cc-pV5Z for N₂ and H₂O, and PySCF has no cc-pV6Z set.
- **Pople sets.** 6-311G** can beat cc-pVDZ in absolute terms but belongs to no hierarchy.
- **Slow convergence.** Even cc-pV5Z misses 10-14 m$E_h$, far more than its HF error.

**Two-point extrapolation (HJO Sec. 8.4.3).** If the cc-pVXZ correlation energies behave like the helium principal expansion, $E_X\approx E_\infty - AX^{-3}$. Two energies fix both parameters:

$$
E^\ast_{XY} = \frac{X^3E_X - Y^3E_Y}{X^3 - Y^3},\qquad A_{XY} = \frac{E_X - E_Y}{X^{-3} - Y^{-3}} .
$$

!!! example "X⁻³ extrapolation of valence MP2 correlation energies (computed for this note, m$E_h$)"
    | Pair | Ne | N₂ | H₂O |
    |---|---:|---:|---:|
    | (D,T) | −297.5 | −402.1 | −286.7 |
    | (T,Q) | −315.0 | −416.9 | −298.3 |
    | (Q,5) | −319.4 | −420.0 | −300.6 |
    | HJO (5,6) | −319.5 | −420.3 | −300.3 |
    | R12 | −320(1) | −421(2) | −300(1) |

    - **Extrapolation beats the raw energies.** The (Q,5) extrapolation is within about 1 m$E_h$ of the R12 limits, whereas the raw cc-pV5Z energies are 9-14 m$E_h$ short. Even (T,Q) is better than raw 5Z.
    - **HJO's statistics (quoted).** Over their test set, the mean absolute deviations from R12 are 0.4, 0.9, 2.0 and 13.5 m$E_h$ for $E_{56}$, $E_{45}$, $E_{34}$ and $E_{23}$. Pairs including cc-pVDZ are not useful.
    - **HF part.** Extrapolate only the correlation energy. The HF energy converges faster than $X^{-3}$ and is taken from the largest basis (or extrapolated exponentially).

## Binding energies

**HJO's finding (Sec. 8.4.4, quoted).** Errors in molecular and atomic energies largely cancel. For a given $X$, the error in the binding energy is about as large as the error in the molecular energy at $X + 1$. Examples:

- **N₂ (HF).** Molecular error 39.06/9.72/2.11/0.43 m$E_h$ versus binding-energy error −14.0/−2.6/−0.6/−0.3 m$E_h$ for D-5.
- **BH (valence FCI).** Binding-energy errors −9.5, −2.6, −0.9 and −0.5 m$E_h$.

The correlating functions of the atom-optimized cc-pVXZ sets therefore serve molecules well.

## Source

Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, Chichester, 2000), Secs. 8.1-8.4, pp. 287-327, Eqs. (8.2.11)-(8.4.9), Tables 8.1-8.3, 8.12-8.13, 8.16, 8.18, 8.21-8.22. Table values read from the text extraction and page images. Recomputed for this note with PySCF 2.14: Ne, N₂ and H₂O HF energies, frozen-core MP2 and CCSD (CCSD through cc-pVQZ, plus cc-pV5Z for Ne), carbon ROHF, the even-tempered fit and the STO-3G overlap. The cc-pV6Z, R12 and CCSD/cc-pV5Z values for N₂ and H₂O, and HJO's extrapolation statistics, are quoted.
