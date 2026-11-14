---
id: density-based-hartree-fock
title: Density-based Hartree-Fock theory - idempotent AO density matrices, the exponential parametrization R(X) = exp(−XS) R exp(SX), McWeeny purification and linear-scaling optimization
summary: For large systems HJO replace MO coefficients by the AO density matrix. A closed-shell determinant corresponds exactly to an R with R = Rᵀ, Tr RS = N/2 and RSR = R. Such matrices are moved among themselves by R(X) = exp(−XS) R exp(SX), which is redundant only for occupied-occupied and virtual-virtual X. Truncated expansions are repaired by McWeeny purification R ← 3RSR − 2RSRSR. The energy gradient is a commutator of f, R and S, so SCF and Newton steps need only sparse matrix products and Fock builds, which makes linear scaling possible. All identities were checked numerically on water/6-31G, including quadratic purification and the gradient 4(SRf − fRS) against finite differences.
status: in-progress
kind: theory
level: advanced
tags: [density-matrix, linear-scaling, purification, mcweeny, idempotency, exponential-parametrization, hartree-fock, sparse-matrices]
prerequisites: [scf-convergence-diis-and-newton, basis-orthogonalization, unitary-matrices-exponential-logarithm]
related: [hartree-fock-csf-parametrization-and-canonical-conditions, multipole-methods-and-integral-screening, one-particle-rdm, generalized-fock-matrix-and-orbital-hessian]
order: 60
date: 2026-11-04
---

## Why use the density matrix

**The bottleneck (HJO Sec. 10.7).** Roothaan-Hall diagonalization costs $\mathcal O(n^3)$. In large systems the matrices $\mathbf S$, $\mathbf h$, $\mathbf f$ and the density are sparse, and Fock builds can be made linear-scaling ([[multipole-methods-and-integral-screening]]). What remains is to optimize the energy using only matrix additions and multiplications.

**Energy as a function of the density.** With the scaled AO density $\mathbf R = \mathbf C\boldsymbol\rho\mathbf C^{\mathsf T}$ ($\rho$ = 1 for occupied and 0 for virtual MOs, so $\mathbf D^{\text{AO}} = 2\mathbf R$),

$$
E(\mathbf R) = 2\,\mathrm{Tr}\,\mathbf R\mathbf h + \mathrm{Tr}\,\mathbf R\mathbf G(\mathbf R) + h_{\text{nuc}},\qquad
G_{\mu\nu}(\mathbf A) = \sum_{\rho\sigma}(2g_{\mu\nu\rho\sigma} - g_{\mu\sigma\rho\nu})A_{\rho\sigma}.
$$

## Which matrices are single-determinant densities

**MO basis.** $\boldsymbol\rho$ is a determinant density if and only if it is symmetric, has trace $N/2$, and satisfies $\boldsymbol\rho^2 = \boldsymbol\rho$.

**AO basis.** $\mathbf{RS} = \mathbf C\boldsymbol\rho\mathbf C^{-1}$ is a similarity transform of $\boldsymbol\rho$, so the conditions become

$$
\mathbf R^{\mathsf T} = \mathbf R,\qquad \mathrm{Tr}\,\mathbf{RS} = \tfrac12N,\qquad \mathbf{RSR} = \mathbf R .
$$

All three can be checked with products of sparse matrices, without diagonalizing anything.

**Projectors.** $\mathbf P = \mathbf{RS}$ and $\mathbf Q = \mathbf 1 - \mathbf{RS}$ project onto the occupied and virtual spaces ($\mathbf{PC} = (\mathbf C_{\text{occ}}\ \mathbf 0)$, $\mathbf{PQ} = \mathbf 0$).

## Exponential parametrization

**Moving between valid densities.** For any antisymmetric $\mathbf X$,

$$
\mathbf R(\mathbf X) = \exp(-\mathbf X\mathbf S)\,\mathbf R\,\exp(\mathbf S\mathbf X)
= \mathbf R + [\mathbf R,\mathbf X]_S + \tfrac12[[\mathbf R,\mathbf X]_S,\mathbf X]_S + \cdots,\qquad [\mathbf A,\mathbf X]_S = \mathbf{ASX} - \mathbf{XSA}.
$$

This maps idempotent densities to idempotent densities. It follows from $\exp(\mathbf{SX})\mathbf S = \mathbf S\exp(\mathbf{XS})$, and it is the AO image of $\boldsymbol\rho(\boldsymbol\kappa) = e^{-\boldsymbol\kappa}\boldsymbol\rho\,e^{\boldsymbol\kappa}$ with $\mathbf X = \mathbf C\boldsymbol\kappa\mathbf C^{\mathsf T}$.

**Redundancy.** $\mathbf X$ of the forms $\mathbf{PXP}^{\mathsf T}$ (occupied-occupied) and $\mathbf{QXQ}^{\mathsf T}$ (virtual-virtual) have vanishing $S$-commutators with $\mathbf R$, so they leave $\mathbf R$ unchanged. A general density can therefore be written using only $\mathbf X_{ov} = \mathbf{PXQ}^{\mathsf T} + \mathbf{QXP}^{\mathsf T}$.

## Purification

**The problem.** A truncated BCH series, or any approximate step, gives an $\mathbf R$ that is only nearly idempotent.

**McWeeny's fix.** Minimizing $\mathrm{Tr}[(\mathbf P + \delta\mathbf P)^2 - (\mathbf P + \delta\mathbf P)]^2$ to first order gives the condition $4\mathbf P^3 - 6\mathbf P^2 + 2\mathbf P = \mathbf 0$ (HJO 10.7.57). Turned into a fixed-point iteration:

$$
\mathbf P_{n+1} = 3\mathbf P_n^2 - 2\mathbf P_n^3,\qquad\text{i.e.}\qquad \mathbf R_{n+1} = 3\mathbf R_n\mathbf S\mathbf R_n - 2\mathbf R_n\mathbf S\mathbf R_n\mathbf S\mathbf R_n .
$$

Symmetry and trace need no separate treatment: averaging symmetrizes, and idempotency forces an integer trace.

**Convergence.**

- **Local.** If $\mathbf R_n = \mathbf R_\infty + \boldsymbol\tau$, the idempotency error after one step is $O(\tau^2)$: quadratic convergence.
- **Global.** On each eigenvalue the map is $x\to3x^2 - 2x^3$, with stationary points at 0 and 1 and an unstable fixed point at ½. Starting values in $(0,\tfrac12)$ go to 0 and in $(\tfrac12,1)$ go to 1. Anything in $\big(\tfrac{1-\sqrt3}2,\tfrac{1+\sqrt3}2\big)$ converges to 0 or 1, though not always to the nearer one.

## Energy, gradient and the density-based SCF step

**Gradient.** Expanding $E(\mathbf X)$ to second order, the gradient with respect to the independent $X_{\mu\nu}$ ($\mu>\nu$) is the antisymmetric matrix built from $\mathbf{SRf} - \mathbf{fRS}$, with $\mathbf f = \mathbf h + \mathbf G(\mathbf R)$. At convergence $\mathbf{fRS} = \mathbf{SRf}$, which in the MO basis reads $\mathbf f\boldsymbol\rho = \boldsymbol\rho\mathbf f$: the Fock and density matrices commute.

**Density-based SCF (HJO Secs. 10.7.9-10.7.10).** Solving the Roothaan-Hall equations for fixed $\mathbf f_n$ is equivalent to minimizing $E_0(\mathbf X) = 2\,\mathrm{Tr}\,\mathbf R(\mathbf X)\mathbf f_n$, the sum of occupied orbital energies. That minimization can be done:

- **by second order**, iterating the linear equations $[\mathbf f\mathbf R\mathbf S]_A = [\mathbf f\mathbf X\mathbf S\mathbf R\mathbf S]_A - [[\mathbf f\mathbf R\mathbf S]_S\mathbf X\mathbf S]_A$ (HJO 10.7.106; $[\cdot]_S$ and $[\cdot]_A$ are the symmetric and antisymmetric parts);
- **or by conjugate gradients.**

Either way, it produces the same SCF sequence as diagonalization, and DIIS still applies.

**Newton in the density formulation (HJO Sec. 10.8.2).** The Hessian times a trial matrix $\mathbf b$ needs only matrix products plus one Fock-like build $\mathbf G([\mathbf R\mathbf S\mathbf b]_S)$. Second-order optimization also scales linearly.

**Where linear scaling comes from.**

1. All matrices become sparse, with a linearly growing number of non-negligible elements. This includes the density matrix, whose elements between distant AOs vanish.
2. Fock builds scale linearly: FMM for the Coulomb part, and density sparsity for exchange.
3. Every optimization step is a sparse product or sum.

!!! example "Numerical checks, water/6-31G at HJO's reference geometry (computed for this note)"
    $\mathbf R$ is the converged RHF density. $\mathbf X = 0.1(\mathbf A - \mathbf A^{\mathsf T})$ with $\mathbf A$ random normal.

    - **Validity of $\mathbf R(\mathbf X)$.** Symmetry error $2\times10^{-16}$; $\mathrm{Tr}\,\mathbf{RS} - 5 = 9\times10^{-16}$; idempotency error $4\times10^{-16}$.
    - **Redundancy.** $\mathbf R(\mathbf{PXP}^{\mathsf T}) - \mathbf R$ and $\mathbf R(\mathbf{QXQ}^{\mathsf T}) - \mathbf R$ are both $4\times10^{-16}$.
    - **BCH series (scale 0.01).** The errors after 1, 2 and 3 terms are $6.3\times10^{-3}$, $1.0\times10^{-4}$ and $1.3\times10^{-5}$. Halving $\mathbf X$ divides the 2-term error by 8 ($O(X^3)$). The ½ in front of the double commutator is required: without it the error stays at $6\times10^{-3}$. My OCR text had lost the ½, but the page image shows it.
    - **Purification.** Starting from the 2-term BCH density at scale 0.1, the idempotency error $\max\lvert\mathbf{RSR} - \mathbf R\rvert$ goes 0.446, 0.238, 0.141, 0.048, $5.2\times10^{-3}$, $5.8\times10^{-5}$. The trace returns to 5.0000 (4.99999 after five steps). This is slow far away and quadratic close in.
    - **Scalar map.** It starts converging to 0 or 1 inside the range above. Just outside it, from −0.37, it still converges, but to 1, not to the nearer 0. From 1.37 it converges to 0.
    - **Gradient.** $\partial E/\partial X_{\mu\nu}$ by central differences equals $4(\mathbf{SRf} - \mathbf{fRS})_{\mu\nu}$ to $3\times10^{-9}$, at a non-stationary pure density and with my sign convention for $\mathbf X$. At the converged density $\lvert\mathbf{fRS} - \mathbf{SRf}\rvert = 3\times10^{-7}$.

## Source

Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, Chichester, 2000), Secs. 10.7 and 10.8.2, pp. 465-478 and 480-481, Eqs. (10.7.1)-(10.7.107) and (10.8.9)-(10.8.15), Fig. 10.1. HJO's references [8] (McWeeny) and [9, 11-15] are not re-checked here. Checks computed for this note with NumPy, SciPy and PySCF 2.14 (`hjo/c10/dens.py`).
