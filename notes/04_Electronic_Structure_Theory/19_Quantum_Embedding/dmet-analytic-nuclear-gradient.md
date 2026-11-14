---
id: dmet-analytic-nuclear-gradient
title: Analytic nuclear gradient of one-shot DMET - a Lagrangian with multipliers for the solver, the chemical potential and the global mean field
summary: The DMET energy depends on R through the AO integrals, the global HF orbitals, the bath (built from the HF density), the Löwdin orthogonalization and the impurity solutions, and it is not variational in any of the last four. Li et al. (2023) add each defining condition to the energy with a multiplier - λ for the solver equations, z for the electron-number condition, α for the HF equations - so the gradient becomes a contraction of densities with derivative integrals. Structure of the multiplier equations, the auxiliary RDMs, where the overlap enters, the HF and FCI special cases, and checks.
status: in-progress
kind: derivation
level: advanced
tags: [DMET, analytic-gradients, lagrangian, z-vector, cphf, chemical-potential, auxiliary-rdm]
prerequisites: [dmet-energy-functionals-and-chemical-potential, lagrangian-for-nonvariational-energies, z-vector-method, cphf-closed-shell, cpci-and-ci-hessian]
related: [rhf-analytic-gradient, derivative-integrals-and-u-matrices, geometry-optimization]
order: 50
date: 2026-11-08
---

Notation: Li et al. 2023 throughout, mapped to this notebook. $c=\{c_I\}$ are the impurity solutions (CI vectors for FCI), $C$ the global MO coefficients, $A$ the AO integrals (one- and two-electron, overlap). $X(\mu,c,C,A)=0$ are the solver equations, $M(C,A)=0$ the HF equations, $N(c)=\operatorname{tr}\Gamma'$ the assembled electron count. Embedding orbitals carry a tilde in Li et al.; here they are $p,q,r,t$.

## Why the gradient is not Hellmann-Feynman

$E_{\rm DMET}$ (either functional of [[dmet-energy-functionals-and-chemical-potential]]) depends on $R$ through

$$
\frac{dE}{dR} = \frac{\partial E}{\partial c}\frac{dc}{dR} + \frac{\partial E}{\partial C}\frac{dC}{dR} + \frac{\partial E}{\partial A}\frac{dA}{dR}
\qquad\text{(Li et al., Eq. 8)} .
$$

- **Solver response.** $E$ is not $\langle c_I|\hat H_I|c_I\rangle$, so $\partial E/\partial c\neq 0$ even for an exact solver, as for MP2 or CI on non-variational energies ([[lagrangian-for-nonvariational-energies]]).
- **Orbital response.** The bath comes from the global HF density, so $E$ depends on $C$ through the LO → embedding transformation, and $C$ is not variational for $E$.
- **Basis response.** The Löwdin matrix $S^{-1/2}$ depends on $R$ through the overlap, so the AO → LO transformation responds too.
- **Cost if done directly.** $dc/dR$ and $dC/dR$ for each of $3N_{\rm atom}$ coordinates: $3N_{\rm atom}$ CPHF and CP-solver solves.

## The Lagrangian

Add each defining condition with a multiplier (Li et al., Eq. 12):

$$
\mathcal L = E_{\rm DMET} - z\big(N(c)-N_{\rm elec}\big) - \lambda^\dagger X(\mu,c,C,A) - \alpha^\dagger M(C,A).
$$

Stationarity in $z,\lambda,\alpha$ gives back the DMET equations. Stationarity in $\mu$, $c$ and $C$ fixes the multipliers:

$$
(\lambda_0\ \ z_0)\begin{pmatrix}\partial X/\partial c & \partial X/\partial\mu\\ \partial N/\partial c & 0\end{pmatrix}
= \big(\partial E/\partial c\ \ \ 0\big),
\qquad
\alpha_0^\dagger = \Big(\frac{\partial E}{\partial C} - \lambda_0^\dagger\frac{\partial X}{\partial C}\Big)\Big(\frac{\partial M}{\partial C}\Big)^{-1}
$$

(Li et al., Eqs. 13-14). Then $\mathcal L = E$ and

$$
\frac{dE}{dR} = \frac{\partial E}{\partial A}\frac{dA}{dR} - \lambda_0^\dagger\frac{\partial X}{\partial A}\frac{dA}{dR} - \alpha_0^\dagger\frac{\partial M}{\partial A}\frac{dA}{dR}
\qquad\text{(Eq. 16)} .
$$

**Order of the solves.**

1. **$\lambda$ and $z$.** The block system couples all fragments only through the scalar $z$. Writing $\lambda_I = \lambda_I^{(E)} - z\lambda_I^{(N)}$, each fragment needs two solves with $\partial X_I/\partial c_I$ (one with source $\partial E/\partial c_I$, one with $\partial N/\partial c_I$), and $z$ follows from the $\mu$ row. This is the Lagrangian form of the chain rule $z = (\partial E/\partial\mu)/(\partial N/\partial\mu)$, checked numerically in [[dmet-energy-functionals-and-chemical-potential]].
2. **Without $\mu$.** $\lambda_0^\dagger = (\partial E/\partial c)(\partial X/\partial c)^{-1}$ is block diagonal: one independent solve per fragment (Eq. 15).
3. **$\alpha$.** One global CPHF solve with the RHF orbital Hessian, the [[z-vector-method]] for the bath's dependence on the mean field.

## Auxiliary RDMs: what the solver contributes

Define $\mathcal L_{\rm emb} = E_{\rm DMET} - \lambda_0^\dagger X$. Its derivative with respect to anything $Y$ (MO coefficients or integrals) has the form of densities contracted with Hamiltonian derivatives (Li et al., Eq. 17):

$$
\frac{\partial\mathcal L_{\rm emb}}{\partial Y} = \Gamma^I_{qp}w^I_{pq}\frac{\partial h'^I_{pq}}{\partial Y} + D^I_{qp}\frac{\partial h^I_{pq}}{\partial Y}
+ \tfrac12\big(w^I_{pqrt}\Gamma^I_{pqrt} + D^I_{pqrt}\big)\frac{\partial (pq|rt)_I}{\partial Y},
$$

$$
D_{pq} = -\lambda_0^\dagger\frac{\partial X}{\partial h_{pq}},\qquad D_{pqrt} = -2\lambda_0^\dagger\frac{\partial X}{\partial(pq|rt)} .
$$

All solver-specific detail lives in the auxiliary RDMs $D$.

- **FCI solver.** $X = (H-E)c$ with normalization. Then $\lambda$ solves a CP-CI equation of the form of [[cpci-and-ci-hessian]] in the embedding space, and $D$ are symmetrized transition densities between $\lambda$ and $c$ (Li et al., Appendix A.2).
- **HF solver.** $X$ is the embedding Brillouin condition, $\lambda$ solves an embedding CPHF equation, and $D$ follows from it (Appendix A.1).

## Where the overlap enters

- **Skeleton terms.** Choosing $Y$ = AO one- and two-electron integrals gives contractions with derivative integrals, as in any correlated gradient.
- **Löwdin orthogonalization.** The LOs are $X = S^{-1/2}$ applied to the AOs, and the LO density is $S^{1/2}\gamma S^{1/2}$. Both depend on $S$, so the gradient picks up an $S$-derivative of matrix functions. For $f(S) = V f(\Lambda)V^{\mathsf T}$ the adjoint is $V[\Phi\circ(V^{\mathsf T}BV)]V^{\mathsf T}$ with divided differences $\Phi_{kl} = (f(\lambda_k)-f(\lambda_l))/(\lambda_k-\lambda_l)$, finite at degenerate eigenvalues. Li et al. treat the overlap terms in Appendix D, with the orbital-transformation derivatives in Appendix B.
- **IAOs instead of Löwdin.** If the LOs depend on the mean-field solution, the AO → LO step also enters the CPHF equation.

## Checks used by Li et al.

- **HF solver, atomic fragments, water trimer (6-31G\*\*).** DMET equals global HF to $10^{-11}$, so its gradient must equal the HF gradient; mean absolute error below $10^{-8}$ a.u.
- **FCI solver, water trimer (STO-3G).** Analytic versus finite-difference gradients, with and without $\mu$ fitting; the deviation decreases with the displacement until the response-equation tolerance is reached (Fig. 1a).
- **H$_{10}$ ring dissociation.** Numerically integrating the analytic gradient reproduces the directly computed DMET energies to $10^{-6}\ E_h$ (Fig. 1b).
- **Applications.** Diels-Alder reaction (6-31G, FCI fragments, D3 correction): structures, NEB transition state and numerical Hessian. Proton transport in a protonated water tetramer by DMET-driven MD.

## Worked example

!!! example "The mean-field limit as a gradient check"
    Distorted H$_6$ ring (STO-3G, atom 0 moved 0.1 Å along $x$, atom 2 moved $-0.07$ Å along $y$), three H$_2$ fragments, HF solver. Script: `dmet_mini.py`.

    - **Finite difference of DMET-HF**, $h = 10^{-3}$ bohr: $\partial E/\partial x_0 = 0.0428594650\ E_h$/bohr.
    - **PySCF RHF analytic gradient**: $0.0428594775$. The difference, $1.2\times10^{-8}$, is the $O(h^2)$ truncation error of the central difference.
    - **With the FCI solver** ($\mu = 0$) the same component is $0.02700808$: correlation changes this force by 37%, and only the full Lagrangian gradient reproduces it.
    - **μ coupling.** The chain-rule check for $z$ is in [[dmet-energy-functionals-and-chemical-potential]] (agreement $1.3\times10^{-8}$).

## Source

- C. Li, J. Yang, X. Zhang, G. K.-L. Chan, *J. Chem. Phys.* **158**, 134105 (2023), doi:10.1063/5.0142961. Sec. II.B, Eqs. 8-17; Appendices A (HF and FCI solvers), B (orbital-transformation gradient), C (CPHF part), D (overlap); Sec. III (validation and applications). Reference implementation: github.com/MoleOrbitalHybridAnalyst/DMET-preview.
- The divided-difference formula is standard matrix calculus.
