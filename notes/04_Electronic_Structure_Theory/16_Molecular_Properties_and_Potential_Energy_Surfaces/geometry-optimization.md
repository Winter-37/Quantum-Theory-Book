---
id: geometry-optimization
title: Geometry optimization - Newton-Raphson steps from analytic gradients and force constants, compared with steepest descent
summary: Stationary points of the Born-Oppenheimer surface satisfy g = 0. Truncating E(u) at second order and setting its derivative to zero gives the Newton step u = −½M⁻¹V₁ (J-S Eq. 5.55), i.e. −H⁻¹g, which converges quadratically near the solution. Translations and rotations must be projected out of the Cartesian Hessian, and the number of negative Hessian eigenvalues classifies the stationary point. An RHF/STO-3G water optimization converges in four Newton steps to Szabo's geometry; steepest descent contracts by a fixed factor 1 − λ_min per step.
status: in-progress
kind: algorithm
level: intermediate
tags: [geometry-optimization, newton-raphson, steepest-descent, hessian, stationary-points, potential-energy-surface, quasi-newton]
prerequisites: [analytic-gradients-and-force-constants, born-oppenheimer-approximation]
related: [mcscf-second-order-optimization, scf-second-order-and-stability, hf-closed-shell-basis-set-trends]
order: 10
date: 2026-11-03
---

## The problem

**Goal.** Within the Born-Oppenheimer approximation ([[born-oppenheimer-approximation]]), the electronic energy plus nuclear repulsion is a potential energy surface $E(\mathbf R)$. Minima are equilibrium structures; first-order saddle points are transition states. Both satisfy

$$
\mathbf g(\mathbf R) = \nabla_{\mathbf R}E = 0 .
$$

**Classification.** At a stationary point, the eigenvalues of the Hessian $\mathbf H = \nabla\nabla^{\mathsf T}E$, after removing translations and rotations, decide its type:

- all positive: minimum;
- one negative: transition state;
- $k$ negative: saddle point of order $k$.

The same logic as for the orbital Hessian of an SCF solution ([[scf-second-order-and-stability]]).

## Newton-Raphson

**Step.** Truncate the energy at second order in the displacement ([[analytic-gradients-and-force-constants]]):

$$
E(\mathbf u) = E_0 + \mathbf u^{\mathsf T}\mathbf V_1 + \mathbf u^{\mathsf T}\mathbf M\mathbf u .
$$

Setting $\partial E/\partial\mathbf u = 0$ gives $\mathbf V_1 + 2\mathbf M\mathbf u = 0$ (J-S Eq. 5.53), hence

$$
\mathbf u = -\tfrac12\mathbf M^{-1}\mathbf V_1 = -\mathbf H^{-1}\mathbf g,
$$

since $\mathbf V_1 = \mathbf g$ and $2\mathbf M = \mathbf H$ (J-S Eq. 5.55). Recompute $\mathbf g$ and $\mathbf H$ at the new geometry and repeat.

**Convergence.** Newton's method converges quadratically near a stationary point: $|\mathbf g_{k+1}|\approx C|\mathbf g_k|^2$. It is the nuclear analogue of second-order MCSCF optimization ([[mcscf-second-order-optimization]]). It also converges to the stationary point of whatever character is nearest, so it can find saddle points as easily as minima.

**Practical points.**

- **Projection.** In Cartesian coordinates $\mathbf H$ has six zero eigenvalues (five for linear molecules) from overall translation and rotation, so it cannot be inverted directly. Project these modes out of $\mathbf g$ and $\mathbf H$ and invert in the remaining $3N - 6$ dimensional space. Internal coordinates avoid the issue.
- **Hessian cost.** An analytic Hessian needs the orbital response for all $3N$ displacements. Practical optimizers therefore use **quasi-Newton** methods: start from an approximate Hessian and update it from successive gradients (BFGS being the usual choice), with trust-radius or line-search control far from the minimum (general knowledge, not in J-S).
- **Steepest descent** ($\mathbf u = -s\,\mathbf g$) needs only gradients. Near the minimum the error along each Hessian eigenvector contracts by $1 - s\lambda_i$ per step. The slowest direction contracts by $1 - s\lambda_{\min}$, and stability requires $s < 2/\lambda_{\max}$.

!!! example "Water, RHF/STO-3G, from R(OH) = 1.95 bohr and HOH = 110° (computed for this note)"
    Newton steps with the analytic Cartesian Hessian, translations and rotations projected out.

    | Step | $E$ (hartree) | $|\mathbf g|$ | R(OH) (bohr) | HOH (°) |
    |---:|---:|---:|---:|---:|
    | 0 | −74.95705413 | 8.03 × 10⁻² | 1.9500 | 110.00 |
    | 1 | −74.96580330 | 1.41 × 10⁻² | 1.8576 | 99.84 |
    | 2 | −74.96590116 | 2.60 × 10⁻⁴ | | |
    | 3 | −74.96590119 | 8.42 × 10⁻⁸ | | |
    | 4 | | 8.24 × 10⁻¹⁴ | 1.8697 | 100.03 |

    - **Quadratic convergence.** $|\mathbf g_{k+1}|/|\mathbf g_k|^2$ = 2.2, 1.3, 1.2 over the first three steps; the last step reaches the numerical noise floor.
    - **Result.** The converged geometry agrees with Szabo's STO-3G values (1.871 bohr, 100.0°; Tables 3.20-3.21) to 0.001 bohr and 0.03°.
    - **Minimum.** The three internal Hessian eigenvalues are 0.27, 1.158 and 1.489 hartree/bohr² at convergence (0.253, 0.878, 1.255 at the start), all positive.

    **Steepest descent** with $s = 1$ bohr²/hartree from the same start:

    | Step | 0 | 5 | 10 | 20 | 30 |
    |---|---:|---:|---:|---:|---:|
    | $|\mathbf g|$ | 8.03 × 10⁻² | 1.37 × 10⁻² | 2.88 × 10⁻³ | 1.24 × 10⁻⁴ | 5.33 × 10⁻⁶ |

    The gradient shrinks by 0.730 per step from step 5 onward, which is $1 - s\lambda_{\min} = 1 - 0.27$. It needs 30 steps to reach the accuracy Newton reached in about 2.5.

## Source

Jørgensen and Simons, *Second Quantization-Based Methods in Quantum Chemistry* (Academic Press, New York, 1981), Ch. 5, Sec. G, pp. 113-115, Eqs. (5.41), (5.51)-(5.55). Comparison geometry from Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996; reprint of the revised first edition, McGraw-Hill, 1989), Sec. 3.7.3, p. 202, Tables 3.20-3.21. Quasi-Newton methods, projection and the steepest-descent analysis are general knowledge. Water calculations with PySCF 2.14.
