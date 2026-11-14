---
id: electron-correlation
title: Electron correlation and the correlation energy
summary: The correlation energy is the difference between the exact nonrelativistic energy and the Hartree-Fock limit; within a finite basis, full CI minus Hartree-Fock defines the basis-set correlation energy. What a single determinant misses (opposite-spin correlation, static near-degeneracy), and how the correlation energy of H2 converges with basis set.
status: in-progress
kind: theory
level: introductory
tags: [correlation-energy, electron-correlation, hartree-fock-limit, full-ci, basis-set-convergence]
prerequisites: [rhf, excited-determinants]
related: [h2-minimal-basis-correlation-analysis, full-ci, cisd, h2-dissociation-rhf-uhf, slater-determinants, coulomb-cusp-and-helium-expansions]
order: 10
date: 2026-11-03
---

## Definition

The **correlation energy** is

$$
E_{\text{corr}} = \mathcal E_0 - E_0^{\text{HF limit}} ,
$$

where $\mathcal E_0$ is the exact nonrelativistic Born-Oppenheimer ground-state energy and $E_0^{\text{HF limit}}$ is the Hartree-Fock energy in a complete basis. Because the Hartree-Fock energy is a variational upper bound, $E_{\text{corr}} < 0$.

**In a finite basis**, the **basis-set correlation energy** is

$$
E_{\text{corr}}(\text{basis}) = \mathcal E_0^{\text{FCI}}(\text{basis}) - E_0^{\text{HF}}(\text{basis}),
$$

where full CI ([[full-ci]]) is exact within the $N$-electron space spanned by that basis.

- It is the benchmark against which every approximate correlation method in the same basis is judged.
- It tends to the true $E_{\text{corr}}$ as the basis becomes complete.

## What a single determinant misses

**Opposite-spin pairs.** A Slater determinant correlates same-spin electrons through antisymmetry (the Fermi hole), but treats opposite-spin electrons as independent ([[slater-determinants]]). The pair density of a determinant does not vanish when two opposite-spin electrons coincide. The exact one does dip there (the Coulomb hole), and the exact wave function has a cusp in $r_{12}$ at coalescence.

**Two qualitatively different situations.** This is a useful language, not a sharp division:

- **Dynamic correlation.** The determinant is a good zeroth-order description and correlation is a sum of many small contributions, mainly from double excitations. Example: H$_2$ near equilibrium, where the Hartree-Fock coefficient in the full CI wave function is about 0.99.
- **Static (nondynamic) correlation.** Two or more determinants are nearly degenerate and must enter with comparable weight. Example: H$_2$ at dissociation, where the doubly excited determinant reaches equal weight with Hartree-Fock ([[full-ci]], [[h2-dissociation-rhf-uhf]]). This is the regime of multiconfigurational methods ([[mcscf-and-gvb]]).

## Size and importance

Correlation energies are a small fraction of total energies, about 1% for first-row molecules. They are, however, of the same order as chemical bond energies and reaction energies, and they are essential for:

- dissociation energies,
- the ordering of ionized states (Szabo's N$_2$ example in [[koopmans-theorem]]),
- weak interactions,
- small dipole moments such as that of CO ([[population-analysis]]).

!!! example "Basis-set convergence of the H₂ correlation energy (R = 1.4 bohr)"
    Full CI and RHF computed with PySCF 2.14. For two electrons, full CI is the same as CISD. Energies in hartree:

    | Basis | $K$ | $E_{\text{HF}}$ | $E_{\text{FCI}}$ | $E_{\text{corr}}$ |
    |---|---:|---:|---:|---:|
    | STO-3G | 2 | −1.116714 | −1.137276 | −0.020562 |
    | 6-31G | 4 | −1.126743 | −1.151679 | −0.024936 |
    | 6-31G** | 10 | −1.131284 | −1.165153 | −0.033869 |
    | cc-pVDZ | 10 | −1.128709 | −1.163399 | −0.034689 |
    | cc-pVTZ | 28 | −1.132961 | −1.172335 | −0.039374 |
    | cc-pVQZ | 60 | −1.133459 | −1.173796 | −0.040337 |

    **Hartree-Fock converges fast.** It changes by only 0.5 mHa from TZ to QZ.

    **The correlation energy converges slowly.** It still changes by 1 mHa from TZ to QZ. The approach to the complete-basis limit goes roughly as $X^{-3}$ in the cardinal number $X$. This is a consequence of the $r_{12}$ cusp, which products of one-electron functions represent poorly.

    The 6-31G** value is the one Szabo quotes (Sec. 4.5). Higher-quality basis sets are not in Szabo.

## Source

Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996; reprint of the revised first edition, McGraw-Hill, 1989), Ch. 4 introduction, pp. 231-232, Eq. (4.1); Sec. 4.1, p. 234 (basis-set correlation energy). The dynamic/static terminology, the cusp argument and the $X^{-3}$ convergence are standard material not taken from Szabo. Numbers computed for this note.
