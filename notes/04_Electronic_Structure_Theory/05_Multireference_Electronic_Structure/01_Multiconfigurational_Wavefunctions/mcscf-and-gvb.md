---
id: mcscf-and-gvb
title: MCSCF and generalized valence bond wave functions
summary: In MCSCF both CI coefficients and orbitals of a short multiconfigurational expansion are optimized. For H2 the two-configuration MCSCF wave function is identical to the GVB (self-consistent Heitler-London) wave function with nonorthogonal orbitals. Proof of the equivalence and computed H2/6-31G** results showing correct dissociation.
status: in-progress
kind: theory
level: intermediate
tags: [mcscf, gvb, tcscf, valence-bond, static-correlation, multiconfigurational]
prerequisites: [full-ci, natural-orbitals]
related: [standard-models-h2-and-water, h2-dissociation-rhf-uhf, electron-correlation, minimal-basis-h2-model, mcscf-second-order-optimization]
also: []
date: 2026-11-03
---

## MCSCF

**Ansatz.** A short CI expansion

$$
|\Psi_{\text{MCSCF}}\rangle = \sum_I c_I\,|\Psi_I\rangle,
$$

in which **both** the coefficients $c_I$ and the orthonormal orbitals in the configurations $|\Psi_I\rangle$ are varied to minimize the energy. With one closed-shell determinant it reduces to Hartree-Fock.

**Why it helps.** Canonical Hartree-Fock orbitals are not the best orbitals for a short CI. MCSCF finds the optimal ones variationally, without first computing a large CI as in the natural-orbital route ([[natural-orbitals]]).

**Cost.** The stationarity conditions are much more involved than the Roothaan equations, because orbitals and coefficients are coupled. Szabo only refers to reviews for the general theory.

## Two-configuration MCSCF for H₂

The simplest MCSCF for H$_2$ uses two closed-shell configurations:

$$
|\Psi_{\text{MCSCF}}\rangle = C_A|\psi_A\bar\psi_A\rangle + C_B|\psi_B\bar\psi_B\rangle,
\qquad
\psi_i = \sum_\mu C_{\mu i}\phi_\mu ,
$$

with $\langle\psi_A|\psi_A\rangle = \langle\psi_B|\psi_B\rangle = 1$, $\langle\psi_A|\psi_B\rangle = 0$, and $C_A^2 + C_B^2 = 1$.

In a minimal basis $\psi_A$, $\psi_B$ are fixed by symmetry, so this is the full CI of [[full-ci]]. In a larger basis it lies above full CI but below any two-configuration CI built from canonical orbitals.

## Generalized valence bond

**Heitler-London (valence bond) wave function.** It uses the nonorthogonal atomic orbitals $\phi_1$, $\phi_2$ ($\langle\phi_1|\phi_2\rangle = S_{12}$):

$$
|\Psi_{\text{VB}}\rangle = \big[2(1+S_{12}^2)\big]^{-1/2}\big[\phi_1(1)\phi_2(2) + \phi_2(1)\phi_1(2)\big]\,2^{-1/2}\big[\alpha(1)\beta(2) - \beta(1)\alpha(2)\big].
$$

**GVB** (Goddard and co-workers) keeps this form but replaces $\phi_1$, $\phi_2$ by nonorthogonal orbitals $u$, $v$ ($\langle u|v\rangle = S$), expanded in a basis and optimized variationally. It is the self-consistent version of valence bond theory and dissociates correctly to open-shell fragments.

## Equivalence of GVB and two-configuration MCSCF (Szabo Ex. 4.9)

Set

$$
u = (a^2+b^2)^{-1/2}(a\psi_A + b\psi_B),
\qquad
v = (a^2+b^2)^{-1/2}(a\psi_A - b\psi_B),
$$

with orthonormal $\psi_A$, $\psi_B$ and real $a, b$.

**Normalization and overlap.**

$$
\langle u|u\rangle = \langle v|v\rangle = 1,
\qquad
S = \langle u|v\rangle = \frac{a^2 - b^2}{a^2 + b^2}.
$$

**The spatial part.**

$$
u(1)v(2) + v(1)u(2) = \frac{2}{a^2+b^2}\big[a^2\psi_A(1)\psi_A(2) - b^2\psi_B(1)\psi_B(2)\big].
$$

Its squared norm is $4(a^4+b^4)/(a^2+b^2)^2$. This equals $2(1+S^2)$, so the GVB normalization constant is consistent. The GVB wave function becomes

$$
|\Psi_{\text{GVB}}\rangle = (a^4+b^4)^{-1/2}\Big[a^2|\psi_A\bar\psi_A\rangle - b^2|\psi_B\bar\psi_B\rangle\Big],
$$

which is the two-configuration MCSCF form with

$$
C_A = \frac{a^2}{\sqrt{a^4+b^4}},
\qquad
C_B = -\frac{b^2}{\sqrt{a^4+b^4}} .
$$

**Conclusion.** The two wave functions are identical given the same basis. The GVB picture (two overlapping, singly occupied, nonorthogonal orbitals) and the MCSCF picture (a closed shell plus a doubly excited correction) describe the same function.

**Limits.**

- **Dissociation.** As $R\to\infty$, $C_B\to-C_A$, so $b\to a$ and $S\to0$. $u$ and $v$ become the two atomic orbitals.
- **United atom.** As $R\to0$, $b\to0$ and $S\to1$: one doubly occupied orbital.

!!! example "H₂, 6-31G**: two-configuration MCSCF (= GVB) versus full CI"
    PySCF 2.14 CASSCF with 2 electrons in 2 active orbitals. The CAS space also contains the open-shell singlet $\psi_A\psi_B$, but it is ungerade and cannot mix, so this is exactly the two-configuration MCSCF. Correlation energies relative to RHF in the same basis, in hartree:

    | $R$ (bohr) | MCSCF(2,2) | Full CI | Fraction |
    |---:|---:|---:|---:|
    | 1.4 | −0.0183 | −0.0339 | 54% |
    | 2.0 | −0.0294 | −0.0389 | 76% |
    | 3.0 | −0.0614 | −0.0640 | 96% |
    | 5.0 | −0.1559 | −0.1560 | 100% |

    At equilibrium this reproduces Szabo's quoted GVB result ($-0.0183$ vs full CI $-0.0339$, 54%). The two-configuration wave function captures the **static** correlation that grows on dissociation. Beyond about 3 bohr it is essentially full CI. Near equilibrium most of the correlation is **dynamic** and is missed ([[electron-correlation]]).

    Szabo contrasts this with second-order perturbation theory from a UHF reference: better near equilibrium, but deteriorating towards the UHF curve at large $R$.

## Source

Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996; reprint of the revised first edition, McGraw-Hill, 1989), Sec. 4.5, pp. 258-261, Eqs. (4.47)-(4.52), Fig. 4.4, Ex. 4.9. Numbers computed for this note.
