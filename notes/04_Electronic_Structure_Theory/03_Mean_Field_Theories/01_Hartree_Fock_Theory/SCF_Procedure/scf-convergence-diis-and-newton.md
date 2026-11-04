---
id: scf-convergence-diis-and-newton
title: Converging Hartree-Fock - Roothaan-Hall iterations, DIIS, integral-direct SCF, Newton trust-region steps, and the SCF method as an approximate Newton method
summary: The Roothaan-Hall equations in the AO basis and why plain fixed-point SCF iterations converge only linearly or not at all. DIIS extrapolation of Fock matrices, integral-direct Fock builds with Coulomb/exchange separation, and Newton's method with a trust region. HJO's analysis treats SCF as Newton's method with the Jacobian approximated by orbital-energy differences, giving a local error-reduction matrix −MW⁻¹. Reproduced: HJO Table 10.4 for water/cc-pVQZ (SCF column to 4×10⁻⁵ E_h, exposing two misprints), the SCF rate 0.43 and the 2R_ref oscillation predicted from the eigenvalues of −MW⁻¹ (−0.654 and −1.553), and Exercise 10.4 on HeH⁺ to every printed digit.
status: in-progress
kind: algorithm
level: advanced
tags: [scf, roothaan-hall, diis, direct-scf, newton-method, trust-region, convergence-rate, fixed-point-iteration, hartree-fock]
prerequisites: [scf-procedure, hartree-fock-csf-parametrization-and-canonical-conditions, generalized-fock-matrix-and-orbital-hessian]
related: [scf-second-order-and-stability, density-based-hartree-fock, heh-plus-minimal-basis-model, multipole-methods-and-integral-screening, rhf-instabilities-and-multiple-solutions]
also: [07_Computational_Methods/Iterative_Solvers, 07_Computational_Methods/Numerical_Optimization]
date: 2026-11-04
---

## Roothaan-Hall in the AO basis

**Equations (HJO Sec. 10.6.1).** Expand the MOs as $\phi_p = \sum_\mu\chi_\mu C_{\mu p}$ and minimize the closed-shell energy under orthonormality using a symmetric multiplier matrix. After an occupied-occupied rotation that makes the multipliers diagonal, this gives

$$
\mathbf f^{\text{AO}}\mathbf C = \mathbf S\mathbf C\boldsymbol\varepsilon,\qquad
f^{\text{AO}}_{\mu\nu} = h_{\mu\nu} + \sum_{\rho\sigma}D^{\text{AO}}_{\rho\sigma}\big(g_{\mu\nu\rho\sigma} - \tfrac12g_{\mu\sigma\rho\nu}\big),\qquad
D^{\text{AO}}_{\rho\sigma} = 2\sum_iC_{\rho i}C_{\sigma i}.
$$

No MO integrals are needed ([[scf-procedure]] works this through for Szabo's HeH⁺).

**The naive SCF iteration.**

1. Build $\mathbf D$ from the current orbitals and $\mathbf f$ from $\mathbf D$.
2. Test the occupied-virtual block of $\mathbf f$ in the MO basis.
3. Diagonalize $\mathbf f$ to get new orbitals, and repeat.

This is a fixed-point iteration $x_{n+1} = f(x_n)$, with no guarantee of convergence.

## DIIS

**Idea (Pulay; HJO Sec. 10.6.2).** Keep the Fock matrices $\mathbf f_i$ and error vectors $\mathbf e_i$ (occupied-virtual MO Fock elements, or equivalently $\mathbf{fDS} - \mathbf{SDf}$) from recent iterations. Diagonalize the combination $\bar{\mathbf f} = \sum_iw_i\mathbf f_i$ instead of the last $\mathbf f$.

**Weights.** They minimize $\lVert\sum_iw_i\mathbf e_i\rVert^2$ subject to $\sum_iw_i = 1$ (so the one-electron part is kept exactly):

$$
\begin{pmatrix}\mathbf B & -\mathbf 1\\ -\mathbf 1^{\mathsf T} & 0\end{pmatrix}\begin{pmatrix}\mathbf w\\ \lambda\end{pmatrix} = \begin{pmatrix}\mathbf 0\\ -1\end{pmatrix},\qquad B_{ij} = \mathbf e_i\cdot\mathbf e_j .
$$

**Caveats.**

- **Linearity assumption.** DIIS assumes that $\mathbf e$ depends linearly on $\mathbf f$, which holds only approximately.
- **History length.** Only a few recent vectors are kept: old ones carry little information and can harm convergence.

## Integral-direct SCF and the Coulomb/exchange split

**Direct SCF (HJO Sec. 10.6.3).** For more than a few hundred basis functions, the AO integrals are recomputed every iteration instead of being stored. This pays off because each integral batch can be screened before it is computed, using the Schwarz bound together with the density elements it will multiply ([[multipole-methods-and-integral-screening]]).

**Splitting the Fock build.** Writing $\mathbf f = \mathbf h + \mathbf J - \tfrac12\mathbf K$ separates two kinds of term:

- **Coulomb, $\mathbf J$:** long-ranged but classical, so multipole and fast-multipole methods can handle it.
- **Exchange, $\mathbf K$:** short-ranged, so it becomes sparse in large systems.

Together these allow linear scaling, but only if diagonalization is also avoided ([[density-based-hartree-fock]]).

## Newton's method with a trust region

**Newton step (HJO Sec. 10.8.1).** Solve $\mathbf E^{(2)}\Delta\boldsymbol\kappa = -\mathbf E^{(1)}$. Close to the minimum this converges quadratically.

**Trust region.** If the step is longer than the trust radius $h$, solve the level-shifted equations $(\mathbf E^{(2)} - \mu\mathbf 1)\Delta\boldsymbol\kappa = -\mathbf E^{(1)}$ with $\mu$ chosen so that $\lVert\Delta\boldsymbol\kappa\rVert = h$. The radius $h$ is updated by comparing predicted and actual energy changes (details in HJO Sec. 12.3).

**Cost.** The Hessian is never built in real calculations. With 100 occupied and 400 virtual orbitals there are 40 000 parameters and about $1.6\times10^9$ Hessian elements. Instead, Hessian-vector products are formed from Fock-like matrices, at about the cost of one SCF iteration each ([[generalized-fock-matrix-and-orbital-hessian]]).

## SCF as an approximate Newton method

**The GBT vector (HJO Sec. 10.9).** Define $\mathbf W(\boldsymbol\kappa)$, whose zero-order term is the gradient and whose first-order term is the Jacobian. At a stationary point the Jacobian equals the Hessian.

**The Fock operator as a model Hamiltonian.** Replacing $\hat H$ by $\hat f$ in $\mathbf W$ and requiring the exact gradient fixes the elements of $\mathbf f$ linking orbitals of different occupation:

$$
f_{nm} = E^{(1)}_{mn}/[2(D_{mm} - D_{nn})].
$$

- **Closed shells.** The remaining elements are fixed by matching the Hessian, and this recovers the usual Fock matrix.
- **Open-shell singlet.** The active-active rotation is non-redundant but $D_{vv} = D_{ww}$, so no Fock matrix can reproduce the gradient. Fock-based SCF cannot describe this state.

**Local convergence (closed shells, canonical orbitals).** The SCF Jacobian is $W_{ai,bj} = 4\delta_{ij}\delta_{ab}(\varepsilon_a - \varepsilon_i)$. The Hessian is $\mathbf W + \mathbf M$, with $\mathbf M$ holding the two-electron terms $4(4g_{aibj} - g_{abij} - g_{ajib})$. Then

$$
\mathbf E^{(1)}_{n+1} = -\mathbf M\mathbf W^{-1}\mathbf E^{(1)}_n + O(\Delta\kappa^2)\qquad(10.9.35).
$$

So the method converges linearly, and diverges if an eigenvalue of $-\mathbf M\mathbf W^{-1}$ has modulus above 1. Because the energy error is quadratic in the gradient, it shrinks by the square of that eigenvalue's modulus.

**Trade-offs (HJO Sec. 10.9.6).**

| | SCF (diagonalize $\mathbf f$) | Newton |
|---|---|---|
| Exact in one step for | noninteracting electrons | a quadratic energy function |
| Global behaviour | periodic in rotations, physically sensible | quadratic model, wrong for large rotations |
| Local rate | linear | quadratic |
| Open-shell CSFs | not always possible | always possible |
| Cost per iteration | one Fock build | 3-6 Fock-like builds |

**HJO's advice.** Start with DIIS and switch to trust-region Newton if DIIS struggles.

## Checks

!!! example "HeH⁺, STO-3G, HJO Exercise 10.4 (computed for this note from HJO's AO integrals)"
    **Setup.** Start from the He 1s function, $R$ = 1.463796 bohr.

    | $n$ | $E_n$ | $E^{(1)}_n$ | $\lvert E^{(1)}_n/E^{(1)}_{n-1}\rvert$ |
    |---:|---:|---:|---:|
    | 1 | −2.77405675 | −0.75730764 | |
    | 2 | −2.83940081 | −0.15531885 | 0.2051 |
    | 3 | −2.84183410 | −0.02513981 | 0.1619 |
    | 4 | −2.84189672 | −0.00389095 | 0.1548 |
    | 5 | −2.84189822 | −0.00059792 | 0.1537 |
    | 8 | −2.84189825 | −0.00000216 | 0.1535 |

    - **Agreement.** Every energy and gradient equals HJO Table 10E.4.4.
    - **Converged result.** The MO is $0.87664739\,s_{\text{He}} + 0.2024759\,s_{\text{H}}$, with $\varepsilon$ = −1.63255844 and −0.17271555 $E_h$.
    - **Predicted rate.** From HJO's MO integrals, $W = 4(\varepsilon_2 - \varepsilon_1) = 5.839372$ and $M = 4(3g_{2121} - g_{2211}) = -0.896157$. So $\lvert M/W\rvert = 0.1535$, exactly the observed asymptotic ratio. The Hessian is $W + M = 4.943215$.

!!! example "Water, cc-pVQZ, from the core-Hamiltonian guess: HJO Table 10.4 recomputed (energy error in $E_h$)"
    **SCF column.** It is reproduced only if the occupations are fixed by symmetry ($3a_1$, $1b_1$, $1b_2$ doubly occupied) instead of by aufbau. With aufbau the second iteration already differs (9.99945 instead of 9.58984), so HJO evidently used symmetry-fixed occupations.

    | $n$ | SCF, $R_{\text{ref}}$ (mine) | HJO | SCF, $2R_{\text{ref}}$ (mine) | HJO |
    |---:|---:|---:|---:|---:|
    | 1 | 16.00647 | 16.00647 | 16.49323 | 16.49326 |
    | 2 | 9.58984 | 9.58984 | 12.73428 | 12.73424 |
    | 3 | 4.61943 | 4.61743 | 6.52430 | 6.52430 |
    | 4 | 5.07609 | 5.07608 | 12.31407 | 12.31403 |
    | 9 | 0.53622 | 0.53622 | 6.39555 | 6.34555 |
    | 16 | 0.00185 | 0.00185 | 12.28261 | 12.28264 |
    | 23 | 0.00000 | 0.00000 | (oscillates) | (oscillates) |

    - **Two misprints.** All other entries agree to $4\times10^{-5}$. I take HJO's 4.61743 (iteration 3) and 6.34555 (iteration 9 at $2R_{\text{ref}}$) to be misprints: the neighbouring entries match, and at $2R_{\text{ref}}$ the iterations settle into a two-cycle (6.39552 ↔ 12.28261) that 6.34555 breaks.
    - **DIIS** ($\mathbf{fDS} - \mathbf{SDf}$ error vectors, 8 kept) reaches $10^{-5}$ $E_h$ after 8 iterations at $R_{\text{ref}}$ and 15 at $2R_{\text{ref}}$, the same counts as HJO. The intermediate values differ, since DIIS details are not specified.
    - **Newton.** My trust-region Newton (exact Hessian, initial radius 0.5, ratio-based updates) converges in 6 and 7 iterations (HJO 8 and 12), with the quadratic final steps HJO describe.

!!! example "Predicting the SCF behaviour from the Hessian (computed for this note)"
    I computed the eigenvalue of $-\mathbf M\mathbf W^{-1}$ with the largest modulus at the converged RHF solutions (water, cc-pVQZ, 550 occupied-virtual rotations):

    | Geometry | Eigenvalue | Predicted energy-error ratio | Observed |
    |---|---:|---:|---|
    | $R_{\text{ref}}$ | −0.654 | 0.428 | 0.43 (e.g. 0.00079/0.00185) |
    | $2R_{\text{ref}}$ | −1.553 | divergent | no convergence; two-cycle |

    The negative sign means the error changes sign each iteration. With a modulus above 1 the iteration cannot settle on the stationary point, and the nonlinear terms lock it into the two-cycle seen in Table 10.4.

**Implementation notes.** My own code (`hjo/c10/conv.py`, `conv_sym.py`, `rate.py`) uses PySCF only for AO integrals and $\mathbf J$/$\mathbf K$ builds. The closed-shell Hessian-vector product is

$$
\sigma_{ai} = 4\big[(\mathbf f_{vv}\boldsymbol\kappa - \boldsymbol\kappa\mathbf f_{oo})_{ai} + \big(\mathbf C_v^{\mathsf T}(2\mathbf J[\mathbf D_\kappa] - \mathbf K[\mathbf D_\kappa])\mathbf C_o\big)_{ai}\big],\qquad
\mathbf D_\kappa = \mathbf C_v\boldsymbol\kappa\mathbf C_o^{\mathsf T} + (\cdot)^{\mathsf T}.
$$

It matches finite differences of the energy to $8\times10^{-5}$, the finite-difference noise. With orbitals updated as $\mathbf C\exp(-\mathbf K)$ and $K_{ai} = \kappa_{ai}$, the gradient is $\partial E/\partial\kappa_{ai} = -4f_{ai}$. HJO's $+4f_{ai}$ corresponds to the opposite sign convention for $\boldsymbol\kappa$.

## Source

Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, Chichester, 2000), Secs. 10.6, 10.8.1 and 10.9, pp. 458-465, 478-480 and 490-496, Eqs. (10.6.1)-(10.6.31), (10.8.1)-(10.8.8), (10.9.1)-(10.9.35), Table 10.4, Exercise 10.4. All calculations were done for this note (PySCF 2.14 for integrals and $\mathbf J$/$\mathbf K$; the SCF, DIIS, Newton and rate analysis are my own code).
