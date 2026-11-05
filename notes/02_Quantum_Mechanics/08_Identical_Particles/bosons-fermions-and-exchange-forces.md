---
id: bosons-fermions-and-exchange-forces
title: Bosons, fermions and exchange forces
summary: Identical particles cannot be labelled, so the two-particle state must be symmetric (bosons, integer spin) or antisymmetric (fermions, half-integer spin) under interchange. The Pauli exclusion principle follows. Spectra of two particles in a box, distinguishable versus bosons versus fermions. The "exchange force": ⟨(x₁−x₂)²⟩ shifts by ∓2|⟨x⟩_ab|², pulling bosons together and pushing fermions apart, with no physical force involved. Checked by exact integrals and 2D grids for the infinite well and the oscillator.
status: in-progress
kind: derivation
level: introductory
tags: [identical-particles, bosons, fermions, pauli-exclusion-principle, spin-statistics, exchange-force, exchange-hole, symmetrization, griffiths]
prerequisites: [two-particle-systems-and-reduced-mass, infinite-square-well]
related: [exchange-symmetry-spin-and-symmetrization-principle, slater-determinants, spin-orbitals-and-antisymmetry, helium-atom-independent-particle-model, electron-correlation]
also: []
date: 2026-11-05
---

## Indistinguishability

**The classical intuition fails.** Classically one could label particles: paint one red, or follow both trajectories. Quantum mechanically no label survives a measurement, and electrons are identical in principle. A state that says "particle 1 is in $\psi_a$ and particle 2 in $\psi_b$" makes an unobservable distinction.

**Two non-committal combinations.** For non-interacting particles there are exactly two:

$$
\psi_\pm(\mathbf r_1,\mathbf r_2) = A\left[\psi_a(\mathbf r_1)\psi_b(\mathbf r_2)\pm\psi_b(\mathbf r_1)\psi_a(\mathbf r_2)\right].
$$

Bosons use $+$ (symmetric under $1\leftrightarrow2$) and fermions use $-$ (antisymmetric). For orthonormal $\psi_a$ and $\psi_b$, $A = 1/\sqrt2$. For bosons with $\psi_a = \psi_b$, the state is just $\psi_a(\mathbf r_1)\psi_a(\mathbf r_2)$ (Problem 5.4).

**Spin–statistics connection** (taken as an axiom in non-relativistic quantum mechanics; provable in relativistic quantum field theory):

$$
\text{integer spin} \Rightarrow \text{bosons},\qquad \text{half-integer spin} \Rightarrow \text{fermions}.
$$

**Pauli exclusion principle.** For fermions with $\psi_a = \psi_b$, $\psi_- = 0$: there is no state at all. Two identical fermions cannot occupy the same one-particle state. This is a consequence of antisymmetry, not an extra rule.

## Two particles in an infinite well (Griffiths Example 5.1, Problem 5.5)

**One-particle states.** $\psi_n = \sqrt{2/a}\sin(n\pi x/a)$, with $E_n = n^2K$ and $K = \pi^2\hbar^2/2ma^2$. Ignore spin, or assume both particles are in the same spin state. Enumerating the two-particle states:

| $E/K$ | Distinguishable | Identical bosons | Identical fermions |
|---|---|---|---|
| 2 ($n_1=n_2=1$) | 1 | 1 | 0 (forbidden) |
| 5 ($\{1,2\}$) | 2 | 1 | 1 |
| 8 ($n_1=n_2=2$) | 1 | 1 | 0 |
| 10 ($\{1,3\}$) | 2 | 1 | 1 |
| 13 ($\{2,3\}$) | 2 | 1 | 1 |

**Consequences.**

- The fermion ground state has energy $5K$.
- The boson first excited state is non-degenerate, where distinguishable particles have a two-fold degeneracy.

Spin reopens some of these states; see [[exchange-symmetry-spin-and-symmetrization-principle]].

## Exchange forces

**Distinguishable particles** (orthonormal $\psi_a$ and $\psi_b$):

$$
\langle(x_1-x_2)^2\rangle_d = \langle x^2\rangle_a+\langle x^2\rangle_b-2\langle x\rangle_a\langle x\rangle_b .
$$

**Identical particles.** The cross terms bring in the overlap integral $\langle x\rangle_{ab} = \int x\,\psi_a^*\psi_b\,dx$, and

$$
\langle(x_1-x_2)^2\rangle_\pm = \langle(x_1-x_2)^2\rangle_d \mp 2|\langle x\rangle_{ab}|^2 .
$$

Identical bosons sit *closer* together than distinguishable particles in the same two states, and identical fermions sit *farther* apart.

**Interpretation.** No agency pushes or pulls; Griffiths calls it a "geometrical consequence of the symmetrization requirement". The effect exists only where the wave functions overlap. If $\psi_a$ and $\psi_b$ live in different places, $\langle x\rangle_{ab} = 0$ and antisymmetrization changes nothing measurable. This is why chemistry can ignore electrons in other molecules.

**Spin.** With spin included, it is the *total* state that is antisymmetric. Electrons in a spin-triplet have an antisymmetric spatial part and avoid each other, while singlet pairs have a symmetric spatial part and come closer. This spatial avoidance, the **Fermi hole**, is the origin of the exchange energy in Hartree–Fock and of Hund's first rule.

## Worked examples

!!! example "Infinite well, one particle in $\psi_n$ and one in $\psi_l$ (Griffiths Problem 5.6, $a=1$)"
    $\langle x\rangle_{nl}$ is non-zero only when $n+l$ is odd: $\psi_n$ and $\psi_l$ must have opposite parity about $a/2$.

    | $(n,l)$ | $\langle x\rangle_{nl}$ | $\langle(x_1-x_2)^2\rangle_d$ | Bosons | Fermions |
    |---|---|---|---|---|
    | (1,2) | $-16/9\pi^2$ | 0.103341 | 0.038450 | 0.168232 |
    | (1,3) | 0 | 0.110377 | 0.110377 | 0.110377 |
    | (2,3) | $-48/25\pi^2$ | 0.148373 | 0.072684 | 0.224062 |

    A direct 2D grid integration (801² points) of the (1,2) densities gives 0.10334, 0.03845 and 0.16823.

!!! example "Oscillator, one particle in $\psi_0$ and one in $\psi_1$ (Griffiths Problem 5.7, units $\hbar/m\omega$)"
    **Inputs.** $\langle x^2\rangle_0 = \tfrac12$, $\langle x^2\rangle_1 = \tfrac32$, $\langle x\rangle_{01} = 1/\sqrt2$.

    **Exact results.**

    $$
    \langle(x_1-x_2)^2\rangle = 2\ \text{(distinguishable)},\qquad 1\ \text{(bosons)},\qquad 3\ \text{(fermions)}.
    $$

    A 2D grid reproduces 2.00000, 1.00000 and 3.00000.

    **Close approach.** The probability of being within $|x_1-x_2|<0.5$ is 0.205 (distinguishable), 0.380 (bosons) and **0.030** (fermions). The antisymmetric wave function vanishes on the line $x_1 = x_2$, carving out an exchange hole.

## Source

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Secs. 5.1.1-5.1.2, Eqs. (5.16)-(5.26), Example 5.1; Problems 5.4-5.7; footnotes 3-5. Page numbers are not given because the PDF used is an e-book rendering without print pagination. The tables and the short-distance probabilities are computed answers in `griffiths/ch05_identical.py` (section B). The Fermi-hole and Hartree–Fock remarks are additions.
