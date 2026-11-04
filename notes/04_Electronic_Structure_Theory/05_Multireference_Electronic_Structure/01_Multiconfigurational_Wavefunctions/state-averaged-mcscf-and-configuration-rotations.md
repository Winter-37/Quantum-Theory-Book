---
id: state-averaged-mcscf-and-configuration-rotations
title: Exponential rotations in configuration space, state-averaged MCSCF, and how MCSCF removes RHF instabilities (water dissociation, allyl radical)
summary: HJO parametrize configuration space without redundancy. One reference state is reached by exp(−R̂)|0⟩ = cos d|0⟩ − (sin d/d)Σ R_K|K⟩, and an orthogonal-complement basis is built cheaply from the reference coefficients. Several reference states use a product of rank-1 Householder-like operators U_ab. This underlies state-averaged MCSCF, which minimizes Σ w_I E_I in one common orbital set. Valence CASSCF removes the RHF triplet instability in water dissociation and the singlet (B₂) instability of the allyl radical. Recomputed: the parametrization formulas, the rank-1 construction, state-specific versus state-averaged water CASSCF, and HJO's allyl π-CASSCF (occupations 1.907/1.000/0.093, a C₂ᵥ minimum along the antisymmetric stretch).
status: in-progress
kind: theory
level: advanced
tags: [mcscf, casscf, state-averaged-mcscf, exponential-parametrization, householder, symmetry-breaking, rhf-instability, allyl-radical, bond-breaking]
prerequisites: [mcscf-parametrization-gradient-and-hessian, rhf-instabilities-and-multiple-solutions]
related: [mcscf-trust-region-and-augmented-hessian, mcscf-second-order-optimization, mcscf-and-gvb, determinant-strings-and-direct-ci, ci-size-extensivity-and-excitation-levels, electron-correlation]
also: []
date: 2026-11-04
---

## Rotating configuration space exponentially

**General rotations (HJO Sec. 12.6.1).** A unitary transformation of the $m$ configuration states can be written

$$
|\tilde P\rangle = \exp(-\hat S)|P\rangle,\qquad \hat S = \sum_{QR}S_{QR}|Q\rangle\langle R|,\qquad \mathbf S^\dagger = -\mathbf S .
$$

This is the configuration-space analogue of $\exp(-\hat\kappa)$ for orbitals. In practice we only care about rotating one reference state, or a few, and need just *some* convenient basis for the rest.

**A single reference state (HJO Sec. 12.6.2).** Let $\{|0\rangle,|K\rangle\}$ be orthonormal and

$$
\hat R = \sum_{K\ne0}\big(R_K|K\rangle\langle0| - R_K^*|0\rangle\langle K|\big),\qquad d = \Big(\sum_K|R_K|^2\Big)^{1/2}.
$$

Then (HJO Exercise 12.3)

$$
\exp(-\hat R)|0\rangle = \cos d\,|0\rangle - \frac{\sin d}{d}\sum_{K\ne0}R_K|K\rangle .
$$

This reaches any normalized state $C_0|0\rangle + \sum_KC_K|K\rangle$ with $C_0 > 0$: set $R_K = -\dfrac{\arccos C_0}{\sqrt{1 - C_0^2}}\,C_K$, so that $d = \arccos C_0\in[0,\pi]$. That needs $m-1$ parameters, one fewer than the dimension, which removes the normalization redundancy of the projected CI parametrization ([[ci-optimization-newton-and-davidson]]).

**An orthogonal-complement basis (HJO Sec. 12.6.3).** Applying $\exp(-\hat R)$ to every $|K\rangle$ would give a basis, but each vector would be a dense combination of all $m$ configurations.

The cheaper route treats the reference state as a rotation of its leading configuration $|o\rangle$ (largest coefficient, $C_o > 0$). The other configurations then map to

$$
|\tilde m\rangle = |m\rangle - \frac{C_m^*}{1 + C_o}\big(|o\rangle + |0\rangle\big).
$$

Each vector is fixed by one coefficient of the reference state.

**Several reference states (HJO Sec. 12.6.4).** For real states, use the rank-1 operator

$$
\hat U_{ab} = 1 - \frac{(|a\rangle - |b\rangle)(\langle a| - \langle b|)}{1 - \langle a|b\rangle}.
$$

- **Properties.** It is unitary and Hermitian, swaps the normalized states $|a\rangle$ and $|b\rangle$, and leaves everything orthogonal to both unchanged.
- **Construction.** $\hat U_k$ swaps configuration $|k\rangle$ with $\hat U_{k-1}\cdots\hat U_1|0_k\rangle$. The product $\hat U_1\cdots\hat U_n$ maps the first $n$ configurations onto the $n$ reference states and the remaining $m-n$ onto an orthonormal complement.
- **Cost.** The $\hat U_i$ are never built as matrices. Applying them is a sequence of vector updates.
- **Parameter count.** The rotation $\hat R$ (reference-reference plus reference-complement parts) has $2n(m-n) + n^2 - n$ real parameters in the complex case. That is the dimension of the set of $n$ orthonormal states in $m$ dimensions, less one phase each.

!!! example "Checks (computed for this note)"
    - **Single-reference formulas.** The closed form for $\exp(-\hat R)|0\rangle$, the inversion for $R_K$, and the complement formula agree with brute-force matrix exponentials to $10^{-16}$ for random states.
    - **Rank-1 construction.** With $m = 7$ and $n = 3$ random real orthonormal references, it reproduces the references to $2.5\times10^{-16}$, and the product is orthogonal to $6\times10^{-16}$.
    - **Parameter count.** The real-case count $n(m-n) + n(n-1)/2 = 15$ equals $mn - n(n+1)/2$.

## Several states

**Separate optimizations (HJO Sec. 12.7.1).**

- **Method.** Optimize each state on its own, then diagonalize $\mathbf H$ in the small basis of these nonorthogonal MCSCF states.
- **Matrix elements.** They come from the biorthogonal-orbital trick of [[determinant-strings-and-direct-ci]] (HJO Sec. 11.9).
- **Quality.** Each state gets the quality of a single-state calculation.

**State-averaged MCSCF (HJO Sec. 12.7.2).** Use one orbital set for all $n$ states and minimize

$$
E_{\text{av}} = \sum_I w_I\langle I|\hat H|I\rangle,\qquad |I\rangle\to\exp(-\hat\kappa)\exp(-\hat R)|I\rangle ,
$$

with $\hat R$ the multi-reference rotation above. The weights are fixed, usually equal.

- **Advantages.** The states come out orthonormal and noninteracting. Subsequent CI and response treatments are simpler.
- **Cost.** No state has orbitals optimal for itself.
- **Gradient.** ${}^cE^{(1)}_{KI} = -2(w_I - \delta_{K\in\text{ref}}w_K)\langle I|\hat H|K\rangle$. With equal weights, rotations *within* the reference space are redundant. So the reference-space Hamiltonian is diagonalized each iteration, which enforces $\langle I|\hat H|J\rangle = E_I\delta_{IJ}$.

!!! example "State-specific versus state-averaged valence CASSCF: water, cc-pVDZ, two ¹A₁ states, equal weights (computed for this note)"
    **Setup.** Active space (8e, 6o; 3,0,1,2), HOH = 110.565°. Energies in $E_h$.

    | $R_{\text{OH}}$ | SS ground | SA ground | SS 2¹A₁ | SA 2¹A₁ |
    |---|---:|---:|---:|---:|
    | $R_{\text{ref}}$ | −76.077836 | −76.051445 | −75.724459 | −75.716317 |
    | $2R_{\text{ref}}$ | −75.818097 | −75.817600 | −75.788142 | −75.787737 |

    - **At $R_{\text{ref}}$.** The two states want different orbitals. Averaging costs the ground state 26.4 m$E_h$ and the excited state 8.1 m$E_h$.
    - **At $2R_{\text{ref}}$.** The two states are near-degenerate combinations of the same broken-bond configurations. Averaging costs only 0.5 and 0.4 m$E_h$.
    - **Caveat.** State averaging is cheapest exactly where it is most needed: near-degeneracies and avoided crossings.

## MCSCF removes RHF instabilities

**Water dissociation (HJO Sec. 12.8.1).** In the same $C_{2v}$ stretch as the RHF study of [[rhf-instabilities-and-multiple-solutions]]:

- **Instabilities.** The valence CASSCF has no triplet instability, and its response excitation energies show no anomalies.
- **Avoided crossing.** There is one in the lowest excited ¹A₁ state near 3 bohr.
- **Hessian.**
  - Near equilibrium, its lowest eigenvalues are an order of magnitude below RHF's. They come from rotations between weakly occupied active and secondary orbitals.
  - At large separations they come from inactive to nearly doubly occupied rotations.
  - Close-lying triplet spin couplings of the fragments can still give a negative ³A₁ eigenvalue near 4 bohr.

My valence CASSCF ground-state energies (cc-pVDZ) are −76.077836 $E_h$ at $R_{\text{ref}}$ and −75.818097 at $2R_{\text{ref}}$.

**The allyl radical (HJO Sec. 12.8.2).** The ²A₂ RHF state of C₃H₅ has a singlet (B₂) instability. UHF breaks the symmetry into a $C_s$ structure with unequal CC bonds, and CISD on the RHF reference does not cure this ([[ci-size-extensivity-and-excitation-levels]]).

- **Origin.** The singly occupied nonbonding $1a_2$ orbital gains by polarizing toward one CC bond.
- **Cure.** Put all three π orbitals ($1b_1$, $1a_2$, $2b_1$) in a CAS(3,3). The wave function now also contains $1b_1^1 1a_2^1 2b_1^1$ and $1a_2^1 2b_1^2$. The lowest Hessian eigenvalue (B₂) stays positive for all symmetric displacements, and the antisymmetric potential has a $C_{2v}$ minimum.
- **Dynamical correlation.** MRSDCI on this CAS reference lowers the curve by about 370 m$E_h$ but keeps its shape.

!!! example "Allyl π-CASSCF(3,3)/cc-pVDZ at the RHF equilibrium geometry (computed for this note)"
    **Geometry.** CC 2.5980 bohr, CCC 124.48°.

    - **Energy and occupations.** ²A₂ energy −116.493809 $E_h$; π natural occupations 1.907, 1.000, 0.093, exactly HJO's.
    - **No symmetry breaking.** Restarting without symmetry constraints returns the same energy.
    - **Antisymmetric stretch.** At symmetric displacement $\delta = 0.2$: −116.481533 ($\Delta = 0$), −116.480252 ($\Delta = \pm0.1$), −116.475720 ($\Delta = \pm0.2$). The minimum is at $\Delta = 0$, as in HJO Fig. 12.4.

## Source

Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, Chichester, 2000), Secs. 12.6-12.8, pp. 630-643, Eqs. (12.6.1)-(12.7.13), Figs. 12.2-12.4. Recomputed for this note with PySCF 2.14 (CASSCF, state averaging) and my own scripts (`hjo/c12/sacas.py`, `hjo/c12/allylcas.py`, and an inline check of Eqs. 12.6.14, 12.6.16, 12.6.27 and 12.6.37-12.6.46).
