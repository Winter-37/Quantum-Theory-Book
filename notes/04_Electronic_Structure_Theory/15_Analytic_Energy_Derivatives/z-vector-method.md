---
id: z-vector-method
title: The Z-vector method (Handy-Schaefer) - one perturbation-independent linear solve replaces 3N CPHF solves
summary: A correlated gradient on SCF orbitals contains L·U^x with U^x = M⁻¹B^x from CPHF. Moving the inverse onto the perturbation-independent side gives L·U^x = z·B^x with Mᵀz = L, so one CPHF-sized solve serves every nuclear coordinate and every one-electron property. Folding z into the densities gives the relaxed one-particle density and a modified energy-weighted density, so the gradient is a plain contraction of AO derivative integrals. For second derivatives z removes U^xy but not U^x. Verified for CISD on water, where the relaxed dipole also matches the Lagrangian note exactly.
status: in-progress
kind: algorithm
level: advanced
tags: [z-vector, handy-schaefer, relaxed-density, orbital-response, cphf, analytic-gradients, lagrangian]
prerequisites: [ci-analytic-gradient, cphf-closed-shell]
related: [lagrangian-for-nonvariational-energies, cpci-and-ci-hessian, rhf-analytic-hessian, molecular-properties-and-response, derivative-integrals-and-u-matrices]
order: 80
date: 2026-11-07
---

Notation: [[derivative-integrals-and-u-matrices]] and [[cphf-closed-shell]]. Here $i,j,k,l$ are occupied, $a$ virtual and $p,q$ general MOs. $\mathbf M$ is the CPHF matrix and $\mathbf B^x$ the CPHF right-hand side, so that $\mathbf{MU}^x = \mathbf B^x$.

## The idea

**The bottleneck.** From [[ci-analytic-gradient]], the orbital-response part of a CI gradient is

$$
2\sum_{ai}K^x_{ai}(X_{ai} - X_{ia}) = \sum_{ai}L_{ai}\big(U^x_{ai} + \tfrac12S^x_{ai}\big),
\qquad L_{ai} = 2(X_{ai} - X_{ia}).
$$

$\mathbf L$ depends on the CI density but not on $x$. $\mathbf U^x$ depends on $x$ but not on the CI. Computing $\mathbf U^x$ for each of the $3N$ coordinates costs $3N$ CPHF solves.

**The trick (YOGS Eqs. 18.7-18.14).** Since $\mathbf U^x = \mathbf M^{-1}\mathbf B^x$,

$$
\mathbf L^{\mathsf T}\mathbf U^x = \mathbf L^{\mathsf T}\mathbf M^{-1}\mathbf B^x = \mathbf z^{\mathsf T}\mathbf B^x,
\qquad
\mathbf M^{\mathsf T}\mathbf z = \mathbf L .
$$

- **One solve.** The **Z vector** is obtained from one linear system of CPHF dimension, independent of the perturbation. Every gradient component then costs only the dot product $\mathbf z\cdot\mathbf B^x$, built from skeleton integrals.
- **Symmetry.** For closed-shell RHF $\mathbf M$ is symmetric, so $\mathbf M^{\mathsf T}\mathbf z = \mathbf M\mathbf z$. For other references the transpose matters (YOGS Eq. 18.24).
- **YOGS's convention.** YOGS write $\mathbf A^{\mathsf T}\mathbf Z = \mathbf X$ with their sign convention for $\mathbf A$; the content is the same.

**Gradient with the Z vector.**

$$
\frac{\mathrm dE}{\mathrm dx} = \sum_{pq}D_{pq}h^x_{pq} + \frac12\sum_{pqrs}d_{pqrs}(pq|rs)^x - \sum_{pq}W_{pq}S^x_{pq} + \frac12\sum_{ai}L_{ai}S^x_{ai} + \sum_{ai}z_{ai}B^x_{ai} + \frac{\partial V_{\text{nn}}}{\partial x}.
$$

**Why it is general (YOGS Sec. 18.1, Eq. 18.23).** Any energy whose only non-variational parameters are SCF orbitals has a response term of the form $\sum\mathbf L\cdot\mathbf U^p$, for any perturbation $p$. So the same $\mathbf z$ gives nuclear gradients, dipole moments, and any other first-order property.

- **Other non-variational methods.** For MP2 or coupled cluster, the amplitudes are also non-variational. They get their own multipliers, the $\Lambda$ equations, and $\mathbf L$ then depends on those multipliers.
- **Lagrangian formulation.** [[lagrangian-for-nonvariational-energies]] states the same construction as Lagrange multipliers for $F_{ai} = 0$. $\mathbf z$ is the vector of those multipliers, up to sign and normalization conventions.

## Relaxed densities: the practical form

**What $\mathbf z\cdot\mathbf B^x$ contains.** Write $\mathbf B^x$ from [[cphf-closed-shell]] term by term:

$$
\sum_{ai}z_{ai}B^x_{ai} = -\sum_{ai}z_{ai}F^x_{ai} + \sum_{ai}z_{ai}\varepsilon_iS^x_{ai} + \sum_{kl}S^x_{kl}\,c_{kl},
\qquad c_{kl} = \sum_{ai}z_{ai}\big[2(ai|kl) - (ak|il)\big].
$$

Define the symmetric matrix $\tilde z_{ai} = \tilde z_{ia} = \tfrac12z_{ai}$ (zero elsewhere) and $Z_{\mu\nu} = (\mathbf C\tilde{\mathbf z}\mathbf C^{\mathsf T})_{\mu\nu}$. Collecting terms gives a gradient formula with no MO-coefficient derivatives at all:

$$
\begin{aligned}
\frac{\mathrm dE}{\mathrm dx} ={}& \sum_{\mu\nu}\big(D^{\text{AO}} - Z\big)_{\mu\nu}\frac{\partial h_{\mu\nu}}{\partial x}
+ \frac12\sum d^{\text{AO}}_{\mu\nu\lambda\sigma}\frac{\partial(\mu\nu|\lambda\sigma)}{\partial x}
- \sum_{\mu\nu\lambda\sigma}Z_{\mu\nu}P_{\lambda\sigma}\Big[\frac{\partial(\mu\nu|\lambda\sigma)}{\partial x} - \frac12\frac{\partial(\mu\lambda|\nu\sigma)}{\partial x}\Big]\\
&- \sum_{\mu\nu}W'^{\text{AO}}_{\mu\nu}\frac{\partial S_{\mu\nu}}{\partial x} + \frac{\partial V_{\text{nn}}}{\partial x}.
\end{aligned}
$$

The modified energy-weighted density, in the MO basis, is

$$
W'_{pq} = W_{pq} - \tfrac12\big(z_{ai}\varepsilon_i + \tfrac12L_{ai}\big)\ \text{in the } ai \text{ and } ia \text{ blocks},
\qquad
W'_{kl} = W_{kl} - \tfrac12(c_{kl} + c_{lk}),
$$

and $W'^{\text{AO}} = \mathbf CW'\mathbf C^{\mathsf T}$.

- **Relaxed density.** $\mathbf D - \tilde{\mathbf z}$ is the **relaxed (response) one-particle density**. Any one-electron property computed with it equals the analytic derivative of the CI energy, orbital relaxation included.
- **Separable two-particle term.** The $Z\otimes P$ term adds a separable piece to the two-particle density.
- **In practice.** Codes build $D'$, $d'$ and $W'$ once and then loop over derivative integrals exactly as in [[rhf-analytic-gradient]].
- **Status.** The arrangement of $W'$ above is my own bookkeeping (YOGS stop at Eq. 18.14). It is verified numerically below.

## Algorithm

1. **Reference calculations.** SCF, then CI. Build $\mathbf D$, $\mathbf d$ and $\mathbf X = \mathbf F^{\mathsf T}$, then $\mathbf L$ and $\mathbf W$. Cost: one CI-density evaluation.
2. **Z vector.** Solve $\mathbf M\mathbf z = \mathbf L$ iteratively, as one CPHF right-hand side.
3. **Densities.** Build $\mathbf D - \tilde{\mathbf z}$, the separable $Z\otimes P$ term and $W'$, and back-transform to the AO basis.
4. **Contraction.** One pass over first-derivative AO integrals contracted with the densities. Its cost is about that of one RHF gradient, plus the back-transformation of $\mathbf d$.

The CI part costs about as much as one energy calculation, and the orbital-response part about one CPHF solve. Before 1984 the response part cost $3N$ CPHF solves.

## Second derivatives (YOGS Sec. 18.2)

**Terms in the CI Hessian.** It contains $2\sum_{pq}U^{xy}_{pq}X_{pq}$, which normally needs second-order CPHF for all $3N(3N+1)/2$ pairs. By the same trick,

$$
2\sum_{pq}U^{xy}_{pq}X_{pq} \to \mathbf z^{\mathsf T}\mathbf B^{xy} + (\text{overlap terms}),
$$

with the *same* $\mathbf z$ (YOGS Eqs. 18.35-18.40).

**What remains.** The terms bilinear in $\mathbf U^x$, $\mathbf U^y$ and the CPCI term in $\partial C_I/\partial x$ still need all $3N$ first-order solutions ([[cpci-and-ci-hessian]]). The Z vector removes the highest-order response, not all of it. Handy and Schaefer's abstract states this: for second and third CI derivatives only first-order coupled-perturbed equations are needed.

**Electric fields (YOGS Eqs. 18.15-18.22, 18.41-18.50).** For a uniform field with field-independent basis functions, $S^F = 0$ and $\mathbf B^F_{ai} = -(r_k)_{ai}$ ([[cphf-closed-shell]]).

- **Dipole.** The relaxed dipole is $\mathbf z\cdot\mathbf B^F$ plus the expectation value, the same as using the relaxed density.
- **Polarizability.** The Z vector removes the second-order CPHF solutions $\mathbf U^{FG}$ from it.

## Worked example

!!! example "CISD, water, STO-3G (computed for this note)"
    Determinant CISD on RHF orbitals, all electrons correlated, as in [[ci-analytic-gradient]]. CPHF dimension $5\times2 = 10$.

    | Route to the 9 gradient components | CPHF solves | max deviation from finite differences ($E_h$/bohr) |
    |---|---:|---:|
    | Explicit $\mathbf U^x$ (YOGS Eq. 6.23) | 9 | $1.6\times10^{-9}$ |
    | $\mathbf z\cdot\mathbf B^x$ (Eq. 18.14 form above) | 1 | $1.6\times10^{-9}$ |
    | Relaxed densities $D'$, $Z\otimes P$, $W'$, AO contraction only | 1 | $1.6\times10^{-9}$ |

    **Dipole from the same $\mathbf z$.** Field $F$ along the $C_2$ axis, perturbation $h \to h + Fz$, origin at O. In each case the quantity is $\mathrm dE/\mathrm dF$, which is minus the electronic dipole component.

    | Geometry | Unrelaxed $\sum D z$ | Relaxed $\sum(D - \tilde z)z$ | Finite field (RHF re-optimized, $\pm10^{-4}$) |
    |---|---:|---:|---:|
    | R = 1.95 bohr, 110° | 1.660745 | 1.660273 | 1.660273 |
    | R = 1.809 bohr, 104.52° | 1.577728 | 1.576961 | 1.576961 (from the Lagrangian note) |

    The second row reproduces, digit for digit, the unrelaxed and Lagrangian values of [[lagrangian-for-nonvariational-energies]], which were computed independently with HJO's multipliers. The Z vector and the Lagrange multipliers are the same object. (The 1.809 bohr, 104.52° geometry reproduces that note's numbers. I took it to be Szabo's water geometry, which that note uses.)

## Source

Yamaguchi, Osamura, Goddard and Schaefer, *A New Dimension to Quantum Chemistry* (Oxford University Press, New York, 1994), Ch. 18, Secs. 18.1-18.2, Eqs. (18.1)-(18.53), pp. 355-362. Equations read from the page images. Original paper: N. C. Handy and H. F. Schaefer III, "On the evaluation of analytic energy derivatives for correlated wave functions", *J. Chem. Phys.* **81**, 5031 (1984), doi:10.1063/1.447489. I have not read the paper itself; its content is stated as in YOGS and its abstract. The relaxed-density bookkeeping ($D - \tilde z$, $Z\otimes P$, $W'$) is my own and verified numerically. Computations: PySCF 2.15, `gradients/ci_grad.py`, `gradients/szabo_dip.py`.
