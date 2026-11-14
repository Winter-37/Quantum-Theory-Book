---
id: standard-models-h2-and-water
title: The standard models compared against full CI - H₂ in cc-pVQZ and water in cc-pVDZ from equilibrium to dissociation (HF, UHF, CASSCF, CI, CC, MP)
summary: HJO's survey of the standard models, with full CI in a fixed basis as the reference. H₂/cc-pVQZ - full CI energies, natural occupations and Hartree-Fock weights, and the RHF, UHF, two-configuration MCSCF and MP2 curves (RHF overbinds by a factor 2.4; MP2, MP3, MP4 cross the FCI curve at 9.5, 6.4 and 5.2 bohr; MP50 diverges beyond 5 bohr). Water/cc-pVDZ at R_ref, 2R_ref, 2.5R_ref and 8R_ref - RHF, UHF, valence CASSCF, MP2, CISD, CCSD and CCSD(T) recomputed against HJO's full-CI energies. The CI hierarchy converges at even orders, CC uniformly, and the MP series oscillates at stretched geometries (also computed to 15th order in 6-31G).
status: in-progress
kind: comparison
level: intermediate
tags: [benchmark, full-ci, hartree-fock, uhf, casscf, cisd, ccsd, ccsd-t, mp2, mp-series, dissociation, water, h2]
prerequisites: [full-ci, rhf, uhf, mcscf-and-gvb, cisd, coupled-cluster-doubles, mp2]
related: [h2-minimal-basis-correlation-analysis, h2-dissociation-rhf-uhf, size-consistency, linked-cluster-theorem, perturbation-theory-second-quantization, natural-orbitals, hf-closed-shell-basis-set-trends, upper-bounds-and-interlacing]
order: 20
date: 2026-11-04
---

## Two expansions

**The two axes.** Every model expands the wave function twice:

- an **orbital (one-electron) basis**, which converges slowly because of the cusp;
- an **$N$-electron model** inside the resulting Fock space, from a single determinant up to full CI.

The exact answer needs both to be complete. HJO study the $N$-electron axis in isolation by comparing models with full CI (FCI) in one fixed basis. The basis axis is treated in their Chapters 6-8.

**FCI size.** $N_{\text{det}} = \binom MN$ for $N$ electrons in $M$ spin orbitals. Water in cc-pVDZ (24 orbitals, 10 electrons, $A_1$, $M_S = 0$) already has 451 681 246 determinants (HJO). I did not attempt that calculation: the water FCI energies below are HJO's.

## H₂ in cc-pVQZ

**FCI analysis (HJO Table 5.4).**

!!! example "FCI natural occupations and Hartree-Fock weight (computed for this note; agree with HJO to all printed digits)"
    | R (bohr) | $E_{\text{FCI}}$ | $W_{\text{HF}}$ | $1\sigma_g$ | $1\sigma_u$ | $2\sigma_g$ | $1\pi_u$ (each) |
    |---:|---:|---:|---:|---:|---:|---:|
    | 1.4 | −1.173796 | 0.9820 | 1.9643 | 0.0199 | 0.0061 | 0.0043 |
    | 4.0 | −1.015724 | 0.7445 | 1.5162 | 0.4804 | 0.0015 | 0.0008 |
    | 15.0 | −0.999891 | 0.4750 (HJO 0.4751) | 1.0000 | 1.0000 | 0 | 0 |

    - **Equilibrium.** FCI/cc-pVQZ gives $R_e = 1.4019$ bohr and $D_e = 173.91$ m$E_h$ (HJO: 1.402 bohr, 173.9 m$E_h$; experiment 1.401 bohr and 458.0 kJ/mol).
    - **Correlating orbitals at equilibrium.** $1\sigma_u$ gives left-right correlation, $2\sigma_g$ radial correlation (a radial node) and $1\pi_u$ angular correlation (nodal planes through the axis).
    - **At dissociation.** $1\sigma_g$ and $1\sigma_u$ become degenerate with one electron each: dynamical correlation disappears and static correlation takes over ([[h2-minimal-basis-correlation-analysis]]).

**The models along the curve (HJO Table 5.6).**

!!! example "H₂/cc-pVQZ total energies (computed for this note; identical to HJO's table)"
    | R (bohr) | FCI | RHF | UHF | MCSCF (2 config.) | MP2 |
    |---:|---:|---:|---:|---:|---:|
    | 1.4 | −1.173796 | −1.133459 | −1.133459 | −1.151978 | −1.166573 |
    | 4.0 | −1.015724 | −0.911164 | −1.002786 | −1.013026 | −0.968012 |
    | 15.0 | −0.999891 | −0.747191 | −0.999891 | −0.999891 | −1.169828 |
    | 100.0 | −0.999891 | −0.718827 | −0.999891 | −0.999891 | −4.034127 |

    - **RHF.** It overbinds: $D_e = 414.6$ m$E_h$ in the supermolecule approach, 2.4 times FCI. With separate atomic calculations ($E_{\text{H}} = -0.4999$) one gets 133.6 m$E_h$ (77%), but intermediate distances cannot be handled that way.
    - **RHF at 100 bohr.** −0.718827 is close to the covalent-ionic average $\tfrac12[2E(\text{H}) + E(\text{H}^-)] = -0.7367$ (with $E(\text{H}^-) = -0.4735$). It is slightly higher because the molecular $1\sigma_g$ orbital is not optimal for both fragment types.
    - **UHF.** Correct at dissociation, but it coincides with RHF up to the instability point and is spin-contaminated in between.
    - **MP2 on RHF** diverges as $R$ grows.

    UHF at large $R$ required an atom-localized starting guess, and RHF required symmetry ($A_{1g}$ occupation); default guesses converge to higher solutions.

**Convergence of the MP series (HJO Fig. 5.20).** The restricted MP series was computed to 50th order by an exact Rayleigh-Schrödinger recursion in the full two-electron space.

!!! example "H₂/cc-pVQZ, $E_{\text{MP}n} - E_{\text{FCI}}$ (computed for this note)"
    | R (bohr) | MP2 | MP4 | MP10 | MP20 | MP50 |
    |---:|---:|---:|---:|---:|---:|
    | 2.0 | +0.01093 | +0.00164 | $+3.0\times10^{-6}$ | $-2\times10^{-9}$ | $2\times10^{-16}$ |
    | 4.0 | +0.04771 | +0.01188 | $-1.3\times10^{-3}$ | $-9.6\times10^{-5}$ | $8.5\times10^{-8}$ |
    | 5.0 | +0.06699 | +0.00352 | $+5.5\times10^{-3}$ | $+2.6\times10^{-3}$ | $+1.2\times10^{-3}$ |
    | 6.0 | +0.07145 | −0.02774 | +0.0328 | −0.0402 | +7.07 |
    | 8.0 | +0.04067 | −0.12169 | −0.700 | +37.5 | $+2.4\times10^7$ |

    - **Crossings.** MP2, MP3 and MP4 cross the FCI curve at 9.5, 6.4 and 5.16 bohr, and MP4 rises above it again at 13.16 bohr. These are exactly HJO's values (9.5, 6.4, 5.2, 13.2).
    - **Divergence.** The series converges up to about 5 bohr and diverges beyond 5-6 bohr, where $1\sigma_g$ and $1\sigma_u$ approach degeneracy.

## Water in cc-pVDZ

**Geometry.** $R_{\text{ref}} = 1.84345$ bohr, HOH = 110.565°, both OH bonds stretched together. HJO's full-CI energies (quoted) are −76.241860, −75.951665, −75.917985 (−75.917991 in their Table 5.5) and −75.910300 $E_h$ at $R_{\text{ref}}$, $2R_{\text{ref}}$, $2.5R_{\text{ref}}$ and $8R_{\text{ref}}$.

**FCI structure (HJO Table 5.5, quoted).**

- **Hartree-Fock weight.** 0.941, 0.589, 0.337 and 0.000 at the four distances.
- **Dissociation.** As the bonds stretch, the bonding $3a_1$ and $1b_2$ lose occupation to the antibonding $4a_1$ and $2b_2$. At $8R_{\text{ref}}$ these four orbitals are singly occupied, describing two H atoms and O($^3P$). The configuration that dominates at equilibrium does not contribute at all in the dissociation limit.

!!! example "Single-reference models and CASSCF, cc-pVDZ (computed for this note; $E - E_{\text{FCI}}$ in $E_h$ using HJO's FCI)"
    | Model | $R_{\text{ref}}$ | $2R_{\text{ref}}$ | $2.5R_{\text{ref}}$ | $8R_{\text{ref}}$ |
    |---|---:|---:|---:|---:|
    | RHF | 0.217821 | 0.363954 | 0.448227 (lowest solution) | 0.517022 |
    | UHF | 0.217821 | 0.157997 | 0.126787 | 0.119577 |
    | CASSCF (8e, 3,0,1,2) | 0.164024 | 0.133568 | 0.126316 | 0.124230 |
    | MP2 | 0.013131 | 0.054730 | (see note) | −0.397636 |
    | CISD | 0.012023 | 0.072015 | | |
    | CCSD | 0.003744 | 0.022032 | | |
    | CCSD(T) | 0.000658 | −0.003820 | | |

    - **Agreement.** Every entry that HJO tabulate agrees to $10^{-6}$ (RHF 0.217822, CASSCF 0.164025 and CISD 0.012024 in HJO, from rounding of the total energies).
    - **Exceptions.** At $2.5R_{\text{ref}}$ HJO quote the **upper** RHF solution (−75.441244) and the MP2 energy based on it (−75.849661). PySCF found a lower RHF solution, −75.469758, so those two entries differ by construction. UHF at $8R_{\text{ref}}$ (−75.790723, $\langle\hat S^2\rangle = 2.004$) was found by following the UHF solution outward from $2R_{\text{ref}}$; a direct start converges to a much higher solution.
    - **CASSCF natural occupations** of the six active orbitals (HJO Table 5.8, reproduced exactly):
        - $R_{\text{ref}}$: 1.9994, 1.9991, 1.9780, 1.9768, 0.0235, 0.0232;
        - $2R_{\text{ref}}$: 1.9995, 1.9990, 1.5840, 1.5162, 0.4866, 0.4147;
        - $8R_{\text{ref}}$: 2, 2, 1, 1, 1, 1.

**Binding energies (supermolecule, $R_{\text{ref}}\to8R_{\text{ref}}$).**

| Model | Binding energy (m$E_h$) | Why |
|---|---:|---|
| FCI | 331.6 | reference |
| RHF | 630.8 | neglects the static correlation of the fragments |
| UHF | 233.3 | neglects the dynamical correlation of the bonding pairs |
| RHF, separate atoms | 237.9 | as UHF ($E(\text{O},{}^3P) = -74.7875$, $E(\text{H}) = -0.4993$) |

The RHF, UHF and FCI values follow from the table above (630.761, 233.316 and 331.560 m$E_h$); the separate-atom value is HJO's.

**CI hierarchy (HJO Table 5.9; CISD recomputed, higher levels quoted).**

| | RHF | CISD | CISDT | CISDTQ | CISDTQ5 | CISDTQ56 |
|---|---:|---:|---:|---:|---:|---:|
| $R_{\text{ref}}$ | 0.217822 | 0.012024 | 0.009043 | 0.000327 | 0.000139 | 0.000003 |
| $2R_{\text{ref}}$ | 0.363954 | 0.072015 | 0.056094 | 0.005817 | 0.002234 | 0.000074 |

- **Truncate at even orders.** Contributions drop from level $2n$ to $2n + 1$ but are comparable for $2n + 1$ and $2n + 2$. At $R_{\text{ref}}$ the doubles give −205.8 m$E_h$, triples −3.0, quadruples −8.7 and quintuples −0.2 m$E_h$.
- **Stretched bonds.** CISD recovers 94.5% of the correlation energy at $R_{\text{ref}}$ and only 80.2% at $2R_{\text{ref}}$.
- **Multireference CI (MRSDCI) from the valence CAS** is 0.004425 and 0.003208 above FCI (HJO Table 5.10, quoted): uniform along the curve and about 40 times better than CASSCF.

**CC hierarchy (HJO Table 5.11; CCSD recomputed, higher levels quoted).**

| | CCSD | CCSDT | CCSDTQ | CCSDTQ5 |
|---|---:|---:|---:|---:|
| $R_{\text{ref}}$ | 0.003744 | 0.000493 | 0.000019 | 0.000003 |
| $2R_{\text{ref}}$ | 0.022032 | −0.001405 | −0.000446 | |

- **Uniform convergence.** Each level improves on the previous one, not just the even ones, because $e^{\hat T}$ supplies the important higher excitations as products. CCSD beats CISDT, and CCSDT nearly matches CISDTQ5.
- **Below FCI.** At $2R_{\text{ref}}$ CCSDT and CCSDTQ fall below FCI: CC energies are not variational.
- **CCSD(T)** (computed here; HJO show it only graphically, Fig. 15.18). At $R_{\text{ref}}$ the perturbative triples recover 95% of the full CCSDT triples correction (0.003086 of 0.003251). At $2R_{\text{ref}} = 3.69$ bohr they overshoot to −0.003820, consistent with HJO's statement that CCSD(T) degrades beyond about 3.5 bohr.

**MP series (HJO Table 5.12, cc-pVDZ, quoted; own 6-31G series computed to 15th order).**

| Order | cc-pVDZ $R_{\text{ref}}$ | cc-pVDZ $2R_{\text{ref}}$ | 6-31G $R_{\text{ref}}$ | 6-31G $2R_{\text{ref}}$ |
|---|---:|---:|---:|---:|
| RHF | 0.217822 | 0.363954 | 0.138225 | 0.301231 |
| MP2 | 0.013131 | 0.054730 | 0.008141 | 0.052885 |
| MP3 | 0.006439 | 0.069096 | 0.006699 | 0.070113 |
| MP4 | 0.001069 | 0.016046 | 0.001317 | 0.016320 |
| MP5 | 0.000511 | 0.016686 | 0.000601 | 0.015496 |
| MP6 | 0.000130 | 0.004300 | 0.000186 | 0.004078 |
| MP7 | 0.000067 | 0.000626 | 0.000089 | −0.000723 |
| MP8 | 0.000014 | −0.000475 | 0.000024 | −0.000638 |
| MP9 | 0.000011 | −0.002065 | 0.000014 | −0.002683 |
| MP10 | −0.000001 | −0.001652 | 0.000003 | −0.001649 |
| MP12 | 0.000000 | −0.001130 | 0.000000 | −0.001091 |
| MP15 | 0.000000 | −0.000146 | 0.000000 | −0.000100 |

- **Same pattern in both bases.** Smooth, monotonic convergence at equilibrium; at $2R_{\text{ref}}$ MP3 is worse than MP2, the series overshoots below FCI from about 7th-8th order, and it creeps back slowly.
- **Checks.** The 6-31G FCI energies are −76.122305 and −75.874641 $E_h$, and my cc-pVDZ MP2 values reproduce HJO's.
- **Unrestricted MP** (HJO, figures only) dissociates correctly but has a pronounced hump and a kink where it separates from the restricted curve. It is not a uniform description either.

## Lessons (HJO's summary, with the numbers above)

1. **RHF** is adequate where one configuration dominates. Without static correlation it is wrong at dissociation, and the error depends strongly on how the dissociation energy is computed.
2. **UHF** dissociates correctly but misses the dynamical correlation of the bonding pairs, and its intermediate region is poor (spin contamination).
3. **CASSCF** treats static correlation uniformly. The active space can be chosen from FCI or MP2 natural occupations by looking for gaps: valence 0.0278 versus non-valence 0.0179 in water (HJO, quoted). Its dynamical-correlation error stays large (0.12-0.16 $E_h$).
4. **Truncated CI** converges at even excitation levels and is not size-extensive. MRSDCI is the most uniform model of all.
5. **CC** converges faster and more uniformly than CI. CCSD(T) is the practical standard near equilibrium, but restricted CC deteriorates as the RHF weight falls.
6. **MP2** is cheap, size-extensive and good near equilibrium. Higher orders do not converge unconditionally.

## Source

Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, Chichester, 2000), Ch. 5, Secs. 5.1 and 5.3-5.8, pp. 142-146 and 162-196, Tables 5.4-5.12, Figs. 5.9-5.20. Recomputed for this note with PySCF 2.14: everything for H₂, and RHF, UHF, CASSCF, MP2, CISD, CCSD and CCSD(T) for water, plus the 6-31G MP series. Water full-CI energies, CISDT and higher, CCSDT and higher, MRSDCI and the cc-pVDZ MP series beyond MP2 are quoted from HJO.
