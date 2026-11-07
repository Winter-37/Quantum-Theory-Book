---
id: mcscf-parametrization-gradient-and-hessian
title: The MCSCF wave function - exp(−κ̂)(|0⟩ + P̂|c⟩) parametrization, gradient and Hessian blocks, redundant rotations in CAS and RAS, stationary points and root flipping, and the structure of the Hessian
summary: HJO combine the Hartree-Fock orbital rotation and the projected CI parametrization into one MCSCF state. The resulting gradient has a CI part 2⟨i|P̂Ĥ|0⟩ and an orbital part ⟨0|[E⁻pq, Ĥ]|0⟩, and the Hessian has four blocks with rank-1 gradient terms. The parametrization is redundant only along the reference vector. All intraspace rotations are redundant in CASSCF and RASSCF. The orbital gradient comes from the inactive and active Fock matrices and the Q matrix, and Hessian-vector products from transition densities and one-index-transformed integrals. HJO's H₂/cc-pVDZ CASSCF Hessian (Table 12.1) is reproduced exactly: eigenvalues 0.000, 0.064, 0.189, 2.960, 3.611, 8.599 E_h, E = −1.14690814 E_h, occupations 1.976/0.024.
status: in-progress
kind: theory
level: advanced
tags: [mcscf, casscf, rasscf, orbital-rotation, redundant-parameters, electronic-hessian, generalized-fock-matrix, root-flipping, generalized-brillouin-theorem]
prerequisites: [generalized-fock-matrix-and-orbital-hessian, ci-optimization-newton-and-davidson, mcscf-and-gvb]
related: [mcscf-trust-region-and-augmented-hessian, mcscf-second-order-optimization, state-averaged-mcscf-and-configuration-rotations, hartree-fock-csf-parametrization-and-canonical-conditions, natural-orbitals]
order: 30
date: 2026-11-04
---

## The model

**Wave function (HJO Sec. 12.1).** A CI expansion whose orbitals are optimized at the same time as its coefficients:

$$
|\boldsymbol\kappa,\mathbf c\rangle = \exp(-\hat\kappa)\,\frac{|0\rangle + \hat P|c\rangle}{\sqrt{1 + \langle c|\hat P|c\rangle}},\qquad \hat P = 1 - |0\rangle\langle0|,\qquad \hat\kappa = \sum_{p>q}\kappa_{pq}\hat E^-_{pq}.
$$

This is HF's orbital parametrization ([[hartree-fock-csf-parametrization-and-canonical-conditions]]) combined with CI's projected one ([[ci-optimization-newton-and-davidson]]).

**Configuration spaces.**

- **CAS.** Inactive orbitals doubly occupied, active orbitals free, secondary orbitals empty.
- **RAS.** RAS1 has a hole limit, RAS2 is free, RAS3 has an electron limit.

**What is routine (as of HJO's writing).** Several hundred orbitals, of which 50-100 inactive and 10-20 active. CAS spaces up to about 12-14 electrons in as many orbitals (millions of determinants), and larger active spaces with RAS restrictions.

**Practical caveats.**

- **Not black-box.** Optimization is harder than for any other model in HJO: the problem is strongly nonlinear, has many local solutions, and couples orbitals strongly to configurations. The converged state must always be inspected.
- **Static correlation only.** MCSCF captures static correlation. Dynamical correlation needs a subsequent multireference treatment.

## Gradient and Hessian

**Energy.** With $\boldsymbol\lambda = (\mathbf c,\boldsymbol\kappa)$, the energy is $E = W(\mathbf c,\boldsymbol\kappa)/S(\mathbf c)$. Here $S = 1 + \langle c|\hat P|c\rangle$ does not depend on $\boldsymbol\kappa$. The orbitals and integrals are re-transformed every iteration so that the expansion point is always $\boldsymbol\lambda = 0$.

**Gradient (HJO 12.2.26-12.2.27).**

$$
{}^cE^{(1)}_i = 2\langle i|\hat P\hat H|0\rangle = 2\langle i|\hat H|0\rangle - 2c_i^{(0)}E^{(0)},\qquad
{}^oE^{(1)}_{pq} = \langle0|[\hat E^-_{pq},\hat H]|0\rangle .
$$

**Hessian (HJO 12.2.28-12.2.30).**

$$
{}^{cc}E^{(2)}_{ij} = 2\langle i|\hat P(\hat H - E^{(0)})\hat P|j\rangle,\qquad
{}^{oc}E^{(2)}_{pq,i} = 2\langle i|\hat P[\hat E^-_{pq},\hat H]|0\rangle,\qquad
{}^{oo}E^{(2)}_{pq,rs} = \tfrac12(1 + P_{pq,rs})\langle0|[\hat E^-_{pq},[\hat E^-_{rs},\hat H]]|0\rangle .
$$

**Redundancy along $\boldsymbol\xi^{(0)} = (\mathbf c^{(0)},\mathbf 0)$.** $\mathbf E^{(1)}\cdot\boldsymbol\xi^{(0)} = 0$ and $\mathbf E^{(2)}\boldsymbol\xi^{(0)} = \mathbf 0$. So the Hessian always has one zero eigenvalue, and the second-order energy is invariant to adding $\alpha\boldsymbol\xi^{(0)}$.

**Rank-1 split.** $\mathbf E^{(2)} = \mathbf K^{(2)} - \bar{\mathbf E}^{(1)}\boldsymbol\xi^{(0)\mathsf T} - \boldsymbol\xi^{(0)}\bar{\mathbf E}^{(1)\mathsf T}$.

- $\mathbf K^{(2)}$ contains no projector.
- $\bar{\mathbf E}^{(1)}$ is the gradient with its orbital part doubled.
- The rank-1 terms vanish at convergence.

## Redundant orbital rotations

**A practical test (HJO Sec. 12.2.6).** Exact redundancy criteria for a nonlinear parametrization are awkward. To first order, $\hat E^-_{pq}$ is redundant if

$$
\hat E^-_{pq}|0\rangle = \sum_ic_i|i\rangle + \sum_{rs\ne pq}\kappa_{rs}\hat E^-_{rs}|0\rangle .
$$

It usually suffices to check whether $\hat E^-_{pq}|0\rangle$ lies in the CI space.

**Consequences.**

- **CASSCF.** Inactive-inactive and secondary-secondary rotations are redundant. So are active-active rotations: $\hat E^-_{vw}|0\rangle$ stays inside the CAS.
- **RASSCF.** Every intraspace rotation (RAS1-RAS1, RAS2-RAS2, RAS3-RAS3) is redundant.
- **Interspace rotations.** These are (presumably) needed; exceptions arise only from special symmetry (HJO Exercise 12.1).
- **The two-electron open shells revisited.** The open-shell triplet is a CAS(2,2) wave function of triplet symmetry, so its active-active rotation is redundant. The open-shell singlet is not a CAS (a singlet CAS(2,2) has three configurations), so its rotation is needed.

## Stationary points and root flipping

**Stationarity.** The conditions ${}^cE^{(1)} = 0$ and ${}^oE^{(1)} = 0$ are the MCSCF generalized Brillouin theorem. They hold automatically for redundant rotations, and for symmetry-breaking rotations if the state is nondegenerate.

- **Degenerate states.** Symmetry-breaking orbital gradients may be nonzero and must be excluded by hand.
- **Configuration gradient.** Its elements of other symmetries always vanish.

**Hessian signature.** The $K$th state should have $K-1$ negative Hessian eigenvalues. Symmetry restrictions control this only in the totally symmetric block, so symmetry-breaking instabilities can survive as in RHF ([[rhf-instabilities-and-multiple-solutions]]).

**Root flipping.** Normally the negative eigenvalues sit in the CI block ${}^{cc}\mathbf E^{(2)}$, and the energy is then an upper bound. When the counts differ between ${}^{cc}\mathbf E^{(2)}$ and $\mathbf E^{(2)}$, this is called root flipping. It need not be fatal, but it often signals that a larger configuration space is needed.

## Gradient and Hessian-vector products in practice

**Orbital gradient (HJO Sec. 12.5.1).** $2(F_{mn} - F_{nm})$, with the generalized Fock matrix assembled from ${}^{\text I}\mathbf F$, ${}^{\text A}\mathbf F$ and $\mathbf Q$ ([[generalized-fock-matrix-and-orbital-hessian]]). Only active-only two-electron densities are needed.

**Configuration gradient.** A direct CI step in the active space, using ${}^{\text I}\mathbf F$ and the inactive energy $E_I = \sum_i(h_{ii} + {}^{\text I}F_{ii})$.

**Hessian times a trial vector $(\mathbf c,\boldsymbol\kappa)$ (HJO Sec. 12.5.2).** Each block reduces to a known operation:

- **CI-CI:** a CI σ, $2\langle i|\hat H - E^{(0)}|c\rangle$;
- **CI-orbital:** a CI σ with the one-index-transformed Hamiltonian, $2\langle i|\hat H^\kappa|0\rangle$, where $\hat H^\kappa = [\hat\kappa,\hat H]$;
- **orbital-CI:** an orbital gradient built from symmetrized transition densities $\langle0|\hat E_{pq}|c\rangle + \langle c|\hat E_{pq}|0\rangle$;
- **orbital-orbital:** an orbital gradient with $\hat H^\kappa$, plus a small commutator correction.

**Inner iterations (HJO Sec. 12.5.3).**

- **Accuracy.** In the local region the linear-equation residual must be $\lesssim$ (gradient)² to preserve quadratic convergence. In the global region about 0.1 × gradient is enough.
- **Trial vectors.** Pure-CI and pure-orbital trial vectors are generated separately, mostly orbital ones, since the orbitals are harder to converge.

## The structure of the Hessian: H₂

!!! example "HJO Table 12.1 recomputed: CASSCF(2,2)/cc-pVDZ, H₂ at 1.40 bohr (computed for this note)"
    **Wave function.** Active $1\sigma_g$, $1\sigma_u$. Configurations $|1\sigma_g^2\rangle$, $|1\sigma_u^2\rangle$ with coefficients 0.99405 and −0.10890. Nonredundant totally symmetric rotations: $1\sigma_g\to2\sigma_g, 3\sigma_g$ and $1\sigma_u\to2\sigma_u, 3\sigma_u$. Orbitals canonicalized (PySCF's diagonalization of the Fock blocks, as HJO recommend for diagonal dominance).

    **Hessian.** Built by finite differences of $E(\mathbf c,\boldsymbol\kappa)$ in exactly HJO's parametrization ($E_h$):

    | | $c_{g^2}$ | $c_{u^2}$ | $g\to2g$ | $g\to3g$ | $u\to2u$ | $u\to3u$ |
    |---|---:|---:|---:|---:|---:|---:|
    | $c_{g^2}$ | 0.037 | 0.337 | 0.026 | 0.050 | −0.015 | 0.013 |
    | $c_{u^2}$ | 0.337 | 3.075 | 0.240 | 0.455 | −0.136 | 0.119 |
    | $1\sigma_g\to2\sigma_g$ | | | 3.489 | −0.164 | −0.044 | 0.037 |
    | $1\sigma_g\to3\sigma_g$ | | | | 8.556 | −0.017 | −0.066 |
    | $1\sigma_u\to2\sigma_u$ | | | | | 0.072 | 0.007 |
    | $1\sigma_u\to3\sigma_u$ | | | | | | 0.194 |

    - **Agreement.** The eigenvalues are 0.000, 0.064, 0.189, 2.960, 3.611 and 8.599, all equal to HJO's. The energy is −1.14690814 $E_h$ and the natural occupations are 1.976/0.024.
    - **Signs.** The coupling elements match HJO's (−0.026, −0.050, −0.015, 0.013; −0.240, −0.455, −0.136, 0.119) up to the sign of each $\sigma_g$ rotation, which depends on orbital phase.
    - **CI block.** Its diagonal is 0.037 and 3.075 (HJO: 3.08), and its nonzero eigenvalue 3.112 (HJO: 3.11). It suggests a $1\sigma_g^2\to1\sigma_u^2$ excitation energy of about 1.55 $E_h$.

**How to read the Hessian (HJO).**

- **CI block.** It is roughly $2(\mathbf H - E^{(0)})$, with a near-zero element for the dominant configuration.
- **Orbital rotations** between orbitals of very different occupation ($1\sigma_g$ to secondary) are stiff. Those between similar occupations ($1\sigma_u$, occupation 0.024, to secondary) are soft. Softness here does not mean a low-lying state.
- **CI-orbital coupling.** It is small but comparable to the soft orbital elements. Neglecting it can slow convergence badly.

## Source

Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, Chichester, 2000), Secs. 12.1-12.2 and 12.5.1-12.5.4, pp. 598-610 and 621-628, Eqs. (12.1.1)-(12.2.61) and (12.5.1)-(12.5.36), Table 12.1. Recomputed for this note with PySCF 2.14 and my own finite-difference Hessian in HJO's parametrization (`hjo/c12/h2cas.py`).
