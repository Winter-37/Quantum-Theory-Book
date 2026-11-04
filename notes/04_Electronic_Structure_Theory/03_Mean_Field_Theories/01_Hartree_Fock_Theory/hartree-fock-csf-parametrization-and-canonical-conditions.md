---
id: hartree-fock-csf-parametrization-and-canonical-conditions
title: Hartree-Fock theory in second quantization - exp(−κ̂) parametrization of CSFs, redundant rotations, the generalized Brillouin theorem, and canonical versus variational conditions
summary: HJO build restricted Hartree-Fock as the optimization of one configuration state function (CSF) under exp(−κ̂). Which rotations are redundant (inactive-inactive, virtual-virtual, and active-active for triplets but not open-shell singlets) decides the variables. The gradient and Hessian are expectation values of commutators. Stationarity is the generalized Brillouin theorem. The Fock operator is defined so that its occupied-virtual block is the gradient and its diagonal gives ionization and attachment energies. The canonical conditions use all n(n−1)/2 rotations, the variational ones only OV. Checked on water: ⟨Φ̂⟩ = −V_ee and singlet minus triplet = 2(ai|ia).
status: in-progress
kind: derivation
level: advanced
tags: [hartree-fock, rhf, csf, orbital-rotation, redundant-parameters, generalized-brillouin-theorem, fock-operator, canonical-orbitals, size-extensivity, hund-rule, fluctuation-potential]
prerequisites: [orbital-rotations, second-quantized-operators, spin-adapted-configurations, brillouin-theorem]
related: [hartree-fock-equations, fock-operator, scf-convergence-diis-and-newton, generalized-fock-matrix-and-orbital-hessian, size-consistency, koopmans-theorem, rhf-instabilities-and-multiple-solutions]
also: [04_Electronic_Structure_Theory/00_Foundations_of_Quantum_Chemistry/08_Second_Quantization]
date: 2026-11-04
---

## The wave function as a rotated CSF

**What RHF optimizes (HJO Sec. 10.1).** The RHF state is one configuration state function, $|\text{CSF}\rangle = \sum_iC_i|i\rangle$. The determinants share one orbital configuration, and their coefficients are fixed by spin symmetry ([[spin-adapted-configurations]]).

**Orbital labels.**

- **Inactive** $i, j, k, l$: doubly occupied in every determinant.
- **Active** $v, w, x, y$: partially occupied.
- **Virtual (secondary)** $a, b, c, d$: unoccupied.

**Examples (with $\hat A_c^\dagger$ the core string of inactive pairs).**

- **Closed shell:** $\hat A_c^\dagger|\text{vac}\rangle$.
- **Triplet, two open orbitals:** $\hat Q^{1,M\dagger}_{vw}\hat A_c^\dagger|\text{vac}\rangle$, for example $a^\dagger_{v\alpha}a^\dagger_{w\alpha}\hat A^\dagger_c|\text{vac}\rangle$ for $M = 1$.
- **Open-shell singlet:** $\frac1{\sqrt2}(a^\dagger_{v\alpha}a^\dagger_{w\beta} - a^\dagger_{v\beta}a^\dagger_{w\alpha})\hat A^\dagger_c|\text{vac}\rangle$.

**Transforming the state.** A real, spin-preserving orbital rotation transforms the state as

$$
|\text{CSF}(\boldsymbol\kappa)\rangle = \exp(-\hat\kappa)|\text{CSF}\rangle,\qquad
\hat\kappa = \sum_{p>q}\kappa_{pq}\hat E^-_{pq},\qquad \hat E^-_{pq} = \hat E_{pq} - \hat E_{qp}
$$

([[orbital-rotations]]). Keeping the spatial symmetry means keeping only the $\hat E^-_{pq}$ with $p$ and $q$ in the same irreducible representation.

## Redundant rotations

**Definition (HJO 10.1.10).** HJO call $\kappa_{pq}$ redundant if $\hat E^-_{pq}|\text{CSF}\rangle = 0$. Such a rotation is not needed even to first order. If the redundant operators form a group, dropping them loses nothing to any order.

| Rotation | Closed shell | Two-open-shell triplet | Two-open-shell singlet |
|---|---|---|---|
| inactive-inactive | redundant | redundant | redundant |
| virtual-virtual | redundant | redundant | redundant |
| inactive-virtual | needed | needed | needed |
| inactive-active, active-virtual | — | needed | needed |
| active-active ($v\leftrightarrow w$) | — | **redundant** | **needed** |

**Why the open-shell cases differ.** $[\hat E^-_{vw},\hat Q^{S,M\dagger}_{vw}] = \hat Q^{S,M\dagger}_{ww} - \hat Q^{S,M\dagger}_{vv}$. The triplet pair operator is antisymmetric in its orbital labels, so this vanishes for $S = 1$ but not for the singlet.

**Why redundancy matters in practice.** At a stationary point the Hessian rows and columns of redundant parameters vanish, making the Hessian singular. Newton-type optimizers must therefore drop them. HJO's Exercise 10.2 shows that setting them to zero keeps the new orbitals as close as possible (largest overlap) to the old ones.

## Energy expansion, gradient and Hessian

**Expansion.** The BCH expansion of $E(\boldsymbol\kappa) = \langle\text{CSF}|e^{\hat\kappa}\hat He^{-\hat\kappa}|\text{CSF}\rangle$ ([[baker-campbell-hausdorff]]) gives, at $\boldsymbol\kappa = \mathbf 0$ and for a real wave function,

$$
E^{(1)}_{pq} = 2\langle\text{CSF}|[\hat E_{pq},\hat H]|\text{CSF}\rangle,\qquad
E^{(2)}_{pq,rs} = (1 + P_{pq,rs})\langle\text{CSF}|[\hat E_{pq},[\hat E^-_{rs},\hat H]]|\text{CSF}\rangle .
$$

The gradient is antisymmetric in $pq$. At a stationary point the Jacobi identity removes a term proportional to the gradient:

$$
E^{(2)}_{pq,rs} = 2\langle\text{HF}|[\hat E_{pq},[\hat E^-_{rs},\hat H]]|\text{HF}\rangle - 2\langle\text{HF}|[\hat E_{pq},[\hat E_{rs},\hat H]]|\text{HF}\rangle\qquad(10.2.8).
$$

Explicit closed-shell forms and their numerical check are in [[generalized-fock-matrix-and-orbital-hessian]].

## The generalized Brillouin theorem

**Statement.** Stationarity, $E^{(1)}_{pq} = 0$, reads $\langle\text{HF}|\hat H\hat E_{pq}|\text{HF}\rangle = \langle\text{HF}|\hat H\hat E_{qp}|\text{HF}\rangle$. Each single excitation is exactly balanced by its de-excitation.

**Explicit forms.**

- **From an inactive orbital, or into a virtual one:** $\langle\text{HF}|\hat H|i\to p\rangle = 0$ and $\langle\text{HF}|\hat H|p\to a\rangle = 0$.
- **Between active orbitals:** only the balance $\langle\text{HF}|\hat H|v\to w\rangle = \langle\text{HF}|\hat H|w\to v\rangle$ is required.

**Closed shells.** Only the first type exists, which is the ordinary Brillouin theorem ([[brillouin-theorem]]).

## Size-extensivity, and why the HF weight vanishes

**Extensivity.** For noninteracting closed-shell fragments, the product of the fragment HF states is stationary, and its energy is $E_A + E_B$. The exponential parametrization makes HF size-extensive automatically.

**A large-system paradox (HJO Eqs. 10.2.29-10.2.31).** If each monomer's exact state has HF weight $C_{\text{HF}}^2 < 1$, then for $m$ noninteracting monomers the HF weight is $C_{\text{HF}}^{2m}\to0$. Yet every monomer, and so the energy per monomer, is described equally well.

- **Why there is no contradiction.** The wave function is multiplicatively separable. The energy is additively separable: the Hamiltonian is a sum of local terms, and each term sees one monomer only.
- **Consequence.** A near-zero HF overlap in a crystal says nothing about the quality of HF energies (compare the Szabo version in [[size-consistency]]).

## The Fock operator and the canonical conditions

**What HJO require of the Fock operator $\hat f = \sum_{pq}f_{pq}\hat E_{pq}$ (Sec. 10.3).**

1. A diagonal Fock matrix must imply the variational conditions $\langle\text{cs}|[\hat E_{ai},\hat H]|\text{cs}\rangle = 0$.
2. Without electron interaction, $\hat f$ must reduce to $\hat h$.

**HJO's choice.** Rewriting the gradient as an anticommutator suggests

$$
f_{pq} = \tfrac12\sum_\sigma\langle\text{cs}|[a^\dagger_{q\sigma},[a_{p\sigma},\hat H]]_+|\text{cs}\rangle
\quad\Longrightarrow\quad
f_{pq} = h_{pq} + \sum_i(2g_{pqii} - g_{piiq})\qquad(10.3.24).
$$

**Not unique.** Any two-electron term added to the occupied-occupied or virtual-virtual blocks satisfies both requirements equally well. HJO justify their choice through the diagonal elements:

- **Occupied:** $f_{ii} = E^{\text{HF}} - E(\text{electron removed from }i)$.
- **Virtual:** $f_{aa} = E(\text{electron added to }a) - E^{\text{HF}}$.

These are the Koopmans energies of [[koopmans-theorem]].

**Two ways to fix the orbitals (HJO Sec. 10.3.5).**

| Condition | Rotations used | Number of parameters | What it fixes |
|---|---|---:|---|
| Variational: $f_{ai} = 0$ | occupied-virtual only | $OV$ | the occupied space |
| Canonical: $f_{pq} = \delta_{pq}\varepsilon_p$ | all | $n(n-1)/2$ | also the orbitals within each space |

- **What the wave function needs.** Only the occupied/virtual split matters. Any orbitals that block-diagonalize $\mathbf f$ give the same HF state.
- **Large systems.** The variational conditions are the efficient target there (density-based methods, [[density-based-hartree-fock]]).
- **Self-consistency.** The canonical equations are pseudo-eigenvalue equations: $\mathbf f$ depends on its own eigenvectors, and the iteration is a fixed-point scheme ([[scf-convergence-diis-and-newton]]).

## Orbital energies, the HF energy and the fluctuation potential

**Orbital energies.**

$$
\varepsilon_i = h_{ii} + \sum_{j\ne i}(2g_{iijj} - g_{ijji}) + g_{iiii},\qquad
\varepsilon_a = h_{aa} + \sum_j(2g_{aajj} - g_{ajja}).
$$

- **Occupied:** the electron in $\phi_i$ interacts with the other $N-1$ electrons.
- **Virtual:** the electron in $\phi_a$ interacts with all $N$ electrons.

**HF energy.** Closed-shell densities are $D_{ij} = 2\delta_{ij}$ and $d_{ijkl} = 4\delta_{ij}\delta_{kl} - 2\delta_{il}\delta_{kj}$. Hence

$$
E^{\text{HF}} = 2\sum_ih_{ii} + \sum_{ij}(2g_{iijj} - g_{ijji}) + h_{\text{nuc}} .
$$

**Fluctuation potential.** Write $\hat H = \hat f + \hat\Phi + h_{\text{nuc}}$ with $\hat\Phi = \hat g - \hat V$.

- **First-order picture.** $E^{\text{HF}} = 2\sum_i\varepsilon_i + \langle\hat\Phi\rangle + h_{\text{nuc}}$: the HF energy is the sum of orbital energies corrected to first order in $\hat\Phi$.
- **Size of the correction.** Since $2\sum_i\varepsilon_i$ counts the electron repulsion twice, $\langle\hat\Phi\rangle = -V_{ee}$. This is not a small correction.

**Hund's rule for one excitation (HJO Eqs. 10.4.21-10.4.23).** With canonical orbitals,

$$
{}^1E_{ai} = E^{\text{HF}} + \varepsilon_a - \varepsilon_i + 2g_{aiia} - g_{aaii},\qquad
{}^3E_{ai} = E^{\text{HF}} + \varepsilon_a - \varepsilon_i - g_{aaii}.
$$

The splitting $2g_{aiia} = 2(ai|ia)$ is an exchange integral, positive because the ERI matrix is positive definite ([[multipole-methods-and-integral-screening]]). So the singlet lies above the triplet.

!!! example "Water, RHF/cc-pVDZ at HJO's reference geometry (computed for this note)"
    **Geometry.** $R_{\text{OH}}$ = 1.84345 bohr, HOH = 110.565°.

    - **Energies.** $E^{\text{HF}} = -76.024039$, $2\sum_i\varepsilon_i = -47.227167$, $h_{\text{nuc}} = 9.009355$, $V_{ee} = 37.806224$ $E_h$.
    - **Fluctuation potential.** $\langle\hat\Phi\rangle = E^{\text{HF}} - 2\sum_i\varepsilon_i - h_{\text{nuc}} = -37.806226$ $E_h$, equal to $-V_{ee}$ to rounding.
    - **HOMO→LUMO** ($1b_1\to4a_1$): ${}^1E = -75.676890$, ${}^3E = -75.700433$; the difference 0.023543 $E_h$ equals $2(ai|ia)$.
    - **Determinant checks.** The $M = 1$ triplet determinant gives exactly ${}^3E$. The single determinant $i_\alpha\to a_\alpha$ gives $-75.688661$, the mean of ${}^1E$ and ${}^3E$, as it should for an equal singlet-triplet mixture.

## Source

Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, Chichester, 2000), Secs. 10.1-10.4, pp. 433-453, Eqs. (10.1.1)-(10.4.28), Exercises 10.2-10.3. The numbers were computed for this note with PySCF 2.14.
