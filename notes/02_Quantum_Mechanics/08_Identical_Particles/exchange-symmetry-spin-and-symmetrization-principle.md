---
id: exchange-symmetry-spin-and-symmetrization-principle
title: Spin, the exchange operator and the generalized symmetrization principle
summary: With spin, the total (space × spin) state must be antisymmetric for fermions. Singlet spin goes with symmetric space, triplet spin with antisymmetric space. The exchange operator P commutes with H, so exchange symmetry is conserved. The symmetrization axiom extends to N particles, with Slater determinants for non-interacting fermions. Includes counting of N-particle states, why three spin-½ functions admit no totally antisymmetric spin state (and more generally for Z > 2), spin-½ and spin-1 pairs in a box, and the Laughlin function as an example beyond a single determinant.
status: in-progress
kind: theory
level: intermediate
tags: [exchange-operator, symmetrization-principle, spin-statistics, singlet-triplet, slater-determinant, permutation-symmetry, laughlin-wave-function, griffiths]
prerequisites: [bosons-fermions-and-exchange-forces, addition-of-angular-momenta]
related: [slater-determinants, spin-orbitals-and-antisymmetry, spin-adapted-configurations, helium-atom-independent-particle-model]
also: []
date: 2026-11-05
---

## Spin enters the symmetry requirement

**Total state.** The complete one-electron state is $\psi(\mathbf r)\chi$. For two particles, the *whole* state $\psi(\mathbf r_1,\mathbf r_2)\chi(1,2)$ must be antisymmetric for fermions:

$$
\psi(\mathbf r_1,\mathbf r_2)\chi(1,2) = -\psi(\mathbf r_2,\mathbf r_1)\chi(2,1).
$$

**Two-spin-½ pairings.** The singlet is antisymmetric and the triplet states are symmetric ([[addition-of-angular-momenta]]). Hence

$$
\text{symmetric space}\times\text{singlet},\qquad \text{antisymmetric space}\times\text{triplet}.
$$

Two electrons *can* share a spatial orbital, but only in the singlet: Pauli forbids same orbital and same spin. This is the spin-orbital form of the Pauli principle used in quantum chemistry ([[spin-orbitals-and-antisymmetry]]).

## Spectra with spin (Griffiths Problem 5.9)

**Setup.** Two non-interacting particles in an infinite well, energies $E = (n_1^2+n_2^2)K$. Count the allowed (space $\times$ spin) states.

**Spin ½ (fermions).**

- $n_1 = n_2$: only the symmetric spatial state exists, which needs the singlet, giving 1 state.
- $n_1\neq n_2$: the symmetric spatial state with the singlet (1) plus the antisymmetric spatial state with the triplet (3), giving 4 states.

**Spin 1 (bosons).** The total state must be symmetric. Of the 9 two-spin states, 6 are symmetric ($s = 2$ and $s = 0$) and 3 antisymmetric ($s = 1$).

- $n_1 = n_2$: symmetric space with symmetric spin, giving 6 states.
- $n_1\neq n_2$: symmetric space with symmetric spin (6) plus antisymmetric space with antisymmetric spin (3), giving 9 states.

| $E/K$ | Spin ½ (fermions) | Spin 1 (bosons) |
|---|---|---|
| 2 | 1 | 6 |
| 5 | 4 | 9 |
| 8 | 1 | 6 |
| 10 | 4 | 9 |

## The exchange operator

**Definition.** $\hat P|(1,2)\rangle = |(2,1)\rangle$. Since $\hat P^2 = 1$, its eigenvalues are $\pm1$.

**Conservation.** For identical particles ($m_1 = m_2$ and $V(\mathbf r_1,\mathbf r_2) = V(\mathbf r_2,\mathbf r_1)$), $[\hat P,\hat H] = 0$. By the generalized Ehrenfest theorem, $d\langle\hat P\rangle/dt = 0$: a state that starts symmetric or antisymmetric stays so ([[energy-time-uncertainty-principle]]).

**Symmetrization axiom.** For identical particles the state is not merely *allowed* but *required* to be an eigenstate of every pairwise exchange:

$$
|(1,\ldots,i,\ldots,j,\ldots,n)\rangle = \pm|(1,\ldots,j,\ldots,i,\ldots,n)\rangle\quad\text{for every pair } i,j,
$$

with $+$ for bosons and $-$ for fermions.

**Construction.** For non-interacting fermions the antisymmetric product is a **Slater determinant**, with rows indexed by particle and columns by orbital (Problem 5.8, [[slater-determinants]]).

**Beyond one determinant.** Interacting systems generally need sums of determinants. Griffiths's example (Problem 5.11) is the Laughlin wave function of the fractional quantum Hall effect:

$$
\psi = A\prod_{j<k}(z_j-z_k)^q\exp\!\left(-\tfrac12\sum_k|z_k|^2\right),\qquad q\ \text{odd}.
$$

- $q = 1$: a single determinant, the Vandermonde product.
- $q = 3$ with $N = 2$: already a sum of two determinants. No statement of the form "particle in orbital $a$" survives.

This is the configuration-interaction picture of correlation ([[electron-correlation]]).

## Counting and impossibility results

**Three particles in three states** (Problem 5.29). Distinguishable: 27 states. Bosons: 10, the multisets. Fermions: 1, the single determinant.

**No totally antisymmetric spin state for three spin-½ particles** (Problem 5.10). By "bulldozer" algebra, antisymmetry under $1\leftrightarrow2$ and $2\leftrightarrow3$ forces every coefficient to vanish.

- Numerically, the antisymmetrizer $\mathcal A = \frac{1}{3!}\sum_\pi(-1)^\pi\hat\pi$ on $(\mathbb C^2)^{\otimes3}$ has trace 0, so the antisymmetric subspace has dimension 0.
- With three internal states it has dimension 1, as for spin 1.
- In general, $n$ fermions need at least $n$ one-particle states to be antisymmetrized, as the determinant formula shows.

**Consequence for atoms** (Problem 5.12). For $Z>2$ electrons a totally antisymmetric *spin* function is impossible. So no atom with $Z>2$ can have a totally symmetric spatial function: not all electrons can sit in the 1s orbital. This is the root of shell structure ([[periodic-table-and-term-symbols]]).

!!! example "Three electrons in a box (Griffiths Problem 5.10b-c)"
    **Configuration.** The ground state puts two electrons in $\psi_1$ and one in $\psi_2$, with energy $(1+1+4)K = 6K$.

    **Construction.** A Slater determinant built from the spin-orbitals $\psi_1\!\uparrow$, $\psi_1\!\downarrow$, $\psi_2\!\uparrow$ is

    $$
    \Phi(1,2,3) = \frac{1}{\sqrt3}\left[\Phi(1,2)\phi(3)-\Phi(1,3)\phi(2)+\Phi(2,3)\phi(1)\right],
    $$

    where $\Phi(i,j)$ is the $\psi_1\psi_1$ singlet pair and $\phi(i) = \psi_2(x_i)\!\uparrow_i$.

    **Degeneracy.** The ground level is two-fold: the third electron's spin can point up or down.

## Source

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Secs. 5.1.3-5.1.4, Eqs. (5.27)-(5.35); Problems 5.8-5.12, 5.29; footnotes 6-13. Page numbers are not given because the PDF used is an e-book rendering without print pagination. The tables and antisymmetrizer ranks are computed in `griffiths/ch05_identical.py` (section C).
