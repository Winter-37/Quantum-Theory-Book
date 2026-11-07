---
id: cpci-and-ci-hessian
title: Coupled-perturbed CI (CPCI) and the CI Hessian
summary: Differentiating the CI eigenvalue equation with its normalization constraint gives the first-order CPCI equations, (H − E + 2CCᵀ) ∂C/∂x = −(∂H/∂x − ∂E/∂x) C. The matrix is nonsingular, and ∂H/∂x already contains the CPHF orbital response. The CI Hessian is then Σ C C ∂²H/∂x∂y − 2 (∂C/∂x)ᵀ(H − E)(∂C/∂y), with the CPCI term negative semidefinite. ∂C/∂x depends on the convention for the occupied-occupied and virtual-virtual orbital response; the energy derivatives do not. Verified for CISD on water against finite-difference CI vectors (4×10⁻⁷) and finite differences of the analytic gradient.
status: in-progress
kind: derivation
level: advanced
tags: [cpci, coupled-perturbed-ci, ci-hessian, configuration-interaction, second-derivatives, wave-function-response]
prerequisites: [ci-analytic-gradient, cphf-closed-shell, derivative-integrals-and-u-matrices]
related: [z-vector-method, rhf-analytic-hessian, ci-optimization-newton-and-davidson, molecular-properties-and-response]
order: 100
date: 2026-11-07
---

Notation: [[derivative-integrals-and-u-matrices]] and [[ci-analytic-gradient]]. Here $I,J,K$ label configurations, $\mathbf H$ is the CI matrix in the (geometry-dependent) MO basis, $E = E_{\text{el}}$, and $x, y$ are nuclear coordinates.

## First-order CPCI

**Conditions (YOGS Eqs. 12.1-12.7).** The CI vector satisfies $\sum_J(H_{IJ} - \delta_{IJ}E)C_J = 0$ and $\sum_IC_I^2 = 1$. YOGS combine them with a multiplier $\theta$, chosen as $\theta = 1$:

$$
\sum_JC_J\Big\{H_{IJ} - \delta_{IJ}\Big(E + 1 - \sum_KC_K^2\Big)\Big\} = 0 .
$$

At the solution the bracket is just $\mathbf H - E$. Its derivative also carries the derivative of the normalization.

**Differentiate (YOGS Eqs. 12.8-12.11).** Using $\sum_KC_K\,\partial C_K/\partial x = 0$ to rewrite the normalization term:

$$
\sum_J\big(H_{IJ} - \delta_{IJ}E + 2C_IC_J\big)\frac{\partial C_J}{\partial x} = -\sum_J\Big(\frac{\partial H_{IJ}}{\partial x} - \delta_{IJ}\frac{\partial E}{\partial x}\Big)C_J,
$$

that is,

$$
\big(\mathbf H - E\mathbf 1 + 2\mathbf C\mathbf C^{\mathsf T}\big)\frac{\partial\mathbf C}{\partial x} = -\Big(\frac{\partial\mathbf H}{\partial x} - \frac{\partial E}{\partial x}\mathbf 1\Big)\mathbf C .
$$

**Properties.**

- **Nonsingular.** $\mathbf H - E$ is singular along $\mathbf C$. The added $2\mathbf{CC}^{\mathsf T}$ lifts that eigenvalue from 0 to 2 and leaves the rest of the spectrum ($E_n - E_0 > 0$ for the ground state) unchanged. So the equations "do not suffer from a singularity" (YOGS).
- **Normalization included.** Projecting onto $\mathbf C$ gives $2\,\mathbf C\cdot\partial\mathbf C/\partial x = -\mathbf C^{\mathsf T}(\partial\mathbf H/\partial x)\mathbf C + \partial E/\partial x = 0$, by the CI gradient formula. So $\mathbf C\cdot\partial\mathbf C/\partial x = 0$ is built in (YOGS Eq. 12.12).
- **Dimension.** The CI dimension, one system per perturbation.
- **Ordering.** The gradient $\partial E/\partial x$ and the CPHF $\mathbf U^x$ must be known first.

**The right-hand side.** $\partial\mathbf H/\partial x$ is the *total* derivative. YOGS write it as $H^x_{IJ} + 2\sum_{pq}U^x_{pq}X^{IJ}_{pq}$ (Eq. 12.14), with "bare" Lagrangians $X^{IJ}$ built from the coupling constants. A simpler route: $\mathbf H$ is linear in the MO integrals, so

$$
\frac{\partial\mathbf H}{\partial x} = \mathbf H\big[\dot{\mathbf h}^x, \dot{\mathbf g}^x\big],
\qquad
\dot{\mathbf h}^x = \mathbf h^x + \mathbf U^{x\mathsf T}\mathbf h + \mathbf h\mathbf U^x,
$$

where $\dot{\mathbf g}^x$ is the four-index analogue ([[derivative-integrals-and-u-matrices]]). In practice, run the CI σ-routine with derivative integrals in place of integrals, without building $\partial\mathbf H/\partial x$ explicitly.

**Convention dependence.** $\partial\mathbf C/\partial x$ describes how the coefficients change in a moving orbital basis. So it depends on how that basis moves, including the occupied-occupied and virtual-virtual parts of $\mathbf U^x$, which RHF leaves undetermined.

- **Canonical $\mathbf U^x$.** Gives the derivative of the CI vector expressed in canonical orbitals.
- **Other conventions.** Give different, equally valid vectors.
- **Energy derivatives.** For a CI invariant under those rotations, energy derivatives do not depend on the choice.

## The CI Hessian

**Differentiate the gradient (YOGS Eqs. 6.73-6.79).** Start from $\partial E/\partial x = \mathbf C^{\mathsf T}(\partial\mathbf H/\partial x)\mathbf C$:

$$
\frac{\partial^2E}{\partial x\,\partial y} = \mathbf C^{\mathsf T}\frac{\partial^2\mathbf H}{\partial x\,\partial y}\mathbf C + 2\frac{\partial\mathbf C^{\mathsf T}}{\partial y}\Big(\frac{\partial\mathbf H}{\partial x} - \frac{\partial E}{\partial x}\Big)\mathbf C .
$$

This is not manifestly symmetric. Replace $(\partial\mathbf H/\partial x - \partial E/\partial x)\mathbf C$ by $-(\mathbf H - E)\,\partial\mathbf C/\partial x$, using the CPCI equations and $\mathbf C\cdot\partial\mathbf C = 0$:

$$
\boxed{\;\frac{\partial^2E}{\partial x\,\partial y} = \sum_{IJ}C_IC_J\frac{\partial^2H_{IJ}}{\partial x\,\partial y} - 2\sum_{IJ}\frac{\partial C_I}{\partial x}\big(H_{IJ} - \delta_{IJ}E\big)\frac{\partial C_J}{\partial y}\;}
$$

**The two terms.**

- **Frozen-coefficient term.** It contains everything the orbitals contribute: skeleton second derivatives, $\mathbf U^x\mathbf U^y$ products, and $\mathbf U^{xy}$.
    - YOGS write it out in Eqs. 6.80-6.81 with bare quantities $X^{IJ}$, $X^{IJx}$, $Y^{IJ}_{pqrs}$.
    - The $\mathbf U^{xy}$ part is handled either by second-order CPHF or by the Z vector, $2\sum U^{xy}_{pq}X_{pq} \to \mathbf z\cdot\mathbf B^{xy} + \ldots$ ([[z-vector-method]]).
- **CPCI term.** $\mathbf H - E$ is positive semidefinite for the ground state, so $-2\,(\partial\mathbf C/\partial x)^{\mathsf T}(\mathbf H - E)(\partial\mathbf C/\partial y)$ is negative semidefinite. Letting the CI coefficients relax lowers every curvature, as orbital relaxation does in [[rhf-analytic-hessian]].

**Second-order CPCI (YOGS Sec. 12.2).** Differentiating once more gives the same matrix $\mathbf H - E + 2\mathbf{CC}^{\mathsf T}$ acting on $\partial^2\mathbf C/\partial x\partial y$ (Eq. 12.21). It is needed for fourth derivatives, not for the Hessian (2n+1 rule).

## Worked example

!!! example "CISD, water, STO-3G, R(OH) = 1.95 bohr, HOH = 110° (computed for this note)"
    141 determinants, 9 coordinates. $\mathbf U^x$ is canonical, from CPHF plus YOGS Eq. 10.26.

    | Check | Result |
    |---|---|
    | $\mathbf C^{\mathsf T}(\partial\mathbf H/\partial x)\mathbf C + V^x_{\text{nn}}$ vs Z-vector gradient | $9\times10^{-16}$ |
    | $\mathbf C\cdot\partial\mathbf C/\partial x$ from CPCI | $1.5\times10^{-15}$ |
    | CPCI $\partial\mathbf C/\partial x$ vs finite differences of CI vectors in sign-aligned canonical orbitals (step $10^{-4}$) | $3.6\times10^{-7}$ (largest element 0.344) |
    | Same, with $-\tfrac12\mathbf S^x$ for the occupied-occupied and virtual-virtual blocks of $\mathbf U^x$ | $\partial\mathbf C/\partial x$ changes by up to 0.299; $\partial E/\partial x$ changes by less than $10^{-12}$ |
    | CI Hessian (boxed formula) vs central differences of the analytic CISD gradient | $4.2\times10^{-7}$ (largest element 0.654) |

    - **How the frozen-coefficient term was obtained.** By central differences of $\mathbf C_0^{\mathsf T}(\partial\mathbf H/\partial x)(R)\,\mathbf C_0$, with $\mathbf C_0$ held fixed and the orbitals (canonical, sign-aligned) and $\mathbf U^x$ recomputed at each displaced geometry. The CPCI term is analytic.
    - **Size of the CPCI term.** For the O $z$,$z$ element, frozen-coefficient 0.51431 plus CPCI −0.07028 gives 0.44403 $E_h$/bohr². Elements of the CPCI term reach 1.54, larger than any element of the total Hessian. CI relaxation is not a small correction.
    - **Sign.** The CPCI term's eigenvalues are all $\le 0$ (lowest −2.70), as the boxed formula requires.

## Source

Yamaguchi, Osamura, Goddard and Schaefer, *A New Dimension to Quantum Chemistry* (Oxford University Press, New York, 1994), Ch. 12, Secs. 12.1-12.2, Eqs. (12.1)-(12.31), pp. 166-170; Ch. 6, Secs. 6.6-6.7, Eqs. (6.61)-(6.87), pp. 92-96. Equations read from the page images. The evaluation of $\partial\mathbf H/\partial x$ as $\mathbf H$ built from total MO-integral derivatives, and the remark on convention dependence of $\partial\mathbf C/\partial x$, are my own, verified numerically. Computations: PySCF 2.15, `gradients/cpci.py`, `gradients/ci_grad.py`.
