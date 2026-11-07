---
id: ci-analytic-gradient
title: The CI analytic gradient - CI coefficients drop out, orbital response does not
summary: For a CI wave function on fixed SCF orbitals, variationality in the CI space removes ∂C_I/∂x from the gradient (Hellmann-Feynman in the CI space). The orbitals are fixed by the SCF, not by the CI, so their response stays. Result: dE/dx = Σ D h^x + ½ Σ d (pq|rs)^x + 2 Σ U^x_pq X_pq. Here X_pq = F_qp is the generalized Fock matrix, and only its antisymmetric part (the CI orbital gradient) couples to the CPHF solution. The AO form uses a CI energy-weighted density. Verified for determinant CISD on water (STO-3G) against finite differences and PySCF to 2×10⁻⁹. Dropping the orbital response gives an error of 2×10⁻⁴ E_h/bohr.
status: in-progress
kind: derivation
level: advanced
tags: [analytic-gradients, configuration-interaction, cisd, lagrangian, generalized-fock, orbital-response, rdm]
prerequisites: [derivative-integrals-and-u-matrices, rhf-analytic-gradient, cphf-closed-shell, density-matrices-second-quantization, generalized-fock-matrix-and-orbital-hessian]
related: [z-vector-method, cpci-and-ci-hessian, lagrangian-for-nonvariational-energies, cisd, hellmann-feynman-and-virial-theorems]
order: 70
date: 2026-11-07
---

Notation: [[derivative-integrals-and-u-matrices]]. Here $I,J$ label CI configurations (determinants or CSFs), $p,q,r,s,m$ are general MOs, $i$ occupied and $a$ virtual in the SCF reference, and $x$ is a nuclear coordinate.

## CI energy in terms of density matrices

**Energy (YOGS Eqs. 6.1-6.8).** With $\Psi = \sum_IC_I\Phi_I$ and $\sum_IC_I^2 = 1$:

$$
E_{\text{el}} = \sum_{IJ}C_IC_JH_{IJ},\qquad
H_{IJ} = \sum_{pq}Q^{IJ}_{pq}h_{pq} + \sum_{pqrs}G^{IJ}_{pqrs}(pq|rs).
$$

The coupling constants $Q^{IJ}$, $G^{IJ}$ depend only on the configurations, not on the geometry. Contracting with $C_IC_J$ gives the density matrices of [[density-matrices-second-quantization]], with YOGS's $Q = D$ and $G = \tfrac12d$:

$$
E_{\text{el}} = \sum_{pq}D_{pq}h_{pq} + \frac12\sum_{pqrs}d_{pqrs}(pq|rs),
\qquad D_{pq} = \langle a^\dagger_{p\sigma}a_{q\sigma}\rangle,\quad d_{pqrs} = \langle a^\dagger_{p\sigma}a^\dagger_{r\tau}a_{s\tau}a_{q\sigma}\rangle,
$$

with spin summed. **Variational condition:** $\sum_J(H_{IJ} - \delta_{IJ}E_{\text{el}})C_J = 0$.

## The CI coefficients drop out

**Hellmann-Feynman in the CI space (YOGS Eqs. 6.11-6.16).** Differentiate $E = \mathbf C^{\mathsf T}\mathbf H\mathbf C$:

$$
\frac{\partial E_{\text{el}}}{\partial x} = 2\sum_{IJ}\frac{\partial C_I}{\partial x}H_{IJ}C_J + \sum_{IJ}C_IC_J\frac{\partial H_{IJ}}{\partial x}
= 2E_{\text{el}}\sum_I\frac{\partial C_I}{\partial x}C_I + \sum_{IJ}C_IC_J\frac{\partial H_{IJ}}{\partial x}.
$$

The first term vanishes because the derivative of the normalization gives $\sum_IC_I\,\partial C_I/\partial x = 0$. So

$$
\frac{\partial E_{\text{el}}}{\partial x} = \sum_{IJ}C_IC_J\frac{\partial H_{IJ}}{\partial x}.
$$

YOGS call this "deceptively simple". $\partial H_{IJ}/\partial x$ is a total derivative: it contains the change of the MOs, which are not variational for the CI energy.

## The orbital response does not

**MO-integral derivatives (YOGS Eqs. 6.17-6.24).** Insert the MO-integral derivatives of [[derivative-integrals-and-u-matrices]]. Use the index symmetries of $D$, $d$ and the integrals to collect all four $U$-terms of the two-electron part into one:

$$
\frac{\partial E_{\text{el}}}{\partial x} = \sum_{pq}D_{pq}h^x_{pq} + \frac12\sum_{pqrs}d_{pqrs}(pq|rs)^x + 2\sum_{pq}U^x_{pq}X_{pq},
$$

$$
X_{pq} = \sum_mD_{qm}h_{pm} + \sum_{mrs}d_{qmrs}(pm|rs) = F_{qp}.
$$

$\mathbf X$ is YOGS's CI Lagrangian matrix. It is the transpose of the generalized Fock matrix $F_{mn} = \sum_qD_{mq}h_{nq} + \sum_{qrs}d_{mqrs}g_{nqrs}$ of [[generalized-fock-matrix-and-orbital-hessian]].

**Reduce to independent pairs (YOGS Eqs. 6.29-6.37, symmetrized).** Write $U^x = K^x - \tfrac12S^x$, so that $K^x$ is antisymmetric by orthonormality. Then

$$
2\sum_{pq}U^x_{pq}X_{pq} = 2\sum_{p>q}K^x_{pq}\big(X_{pq} - X_{qp}\big) - \sum_{pq}S^x_{pq}W_{pq},
\qquad W_{pq} = \tfrac12(X_{pq} + X_{qp}).
$$

- **The coupling.** $X_{pq} - X_{qp} = F_{qp} - F_{pq}$ is minus half the CI orbital gradient $E^{(1)}_{pq} = 2(F_{pq} - F_{qp})$. The orbital response couples to the gradient only through the extent to which the CI energy is *not* stationary in the orbitals.
- **MCSCF.** That gradient vanishes, and the gradient needs no response (as for RHF).
- **Which pairs remain.** Only pairs with $X_{pq}\neq X_{qp}$ need CPHF.
    - **CISD with all electrons correlated.** Invariant to occupied-occupied and virtual-virtual rotations, so only the occupied-virtual $K^x_{ai} = U^x_{ai} + \tfrac12S^x_{ai}$ survives.
    - **Frozen core.** Core-valence occupied pairs also enter, so canonical $U^x_{ij}$ is needed (YOGS Eq. 10.26).

**Final gradient (cf. YOGS Eq. 6.37).**

$$
\frac{\mathrm dE}{\mathrm dx} = \sum_{\mu\nu}D^{\text{AO}}_{\mu\nu}\frac{\partial h_{\mu\nu}}{\partial x}
+ \frac12\sum_{\mu\nu\lambda\sigma}d^{\text{AO}}_{\mu\nu\lambda\sigma}\frac{\partial(\mu\nu|\lambda\sigma)}{\partial x}
- \sum_{\mu\nu}W^{\text{AO}}_{\mu\nu}\frac{\partial S_{\mu\nu}}{\partial x}
+ 2\sum_{ai}K^x_{ai}\big(X_{ai} - X_{ia}\big) + \frac{\partial V_{\text{nn}}}{\partial x},
$$

with $D^{\text{AO}} = \mathbf C\mathbf D\mathbf C^{\mathsf T}$, $W^{\text{AO}} = \mathbf C\mathbf W\mathbf C^{\mathsf T}$, and $d^{\text{AO}}$ back-transformed on all four indices.

- **YOGS's version.** YOGS keep $U^x_{pq}$ instead of $K^x_{pq}$ in the last term and absorb the difference into an unsymmetrized $W$ (their Eq. 6.35). The two forms are equal.
- **Reduction to RHF.** For a single closed-shell determinant, $\mathbf X$ is symmetric with $X_{ij} = 2F^{\text{RHF}}_{ij}$ and $X_{ai} = 0$. The formula reduces to [[rhf-analytic-gradient]].

## Cost and the way out

**As written,** the last term needs $\mathbf U^x$ for all $3N$ coordinates: $3N$ CPHF solves, each costing about as much as an SCF. This was the bottleneck of early CI gradients.

**Z-vector method (Handy and Schaefer, 1984).** Since $\mathbf U^x = \mathbf M^{-1}\mathbf B^x$, the term $\mathbf L\cdot\mathbf U^x$ equals $(\mathbf M^{-1}\mathbf L)\cdot\mathbf B^x$. One linear solve, independent of $x$, replaces all $3N$ ([[z-vector-method]]). The same idea in Lagrangian form is [[lagrangian-for-nonvariational-energies]].

## Worked example

!!! example "Determinant CISD, water, STO-3G, R(OH) = 1.95 bohr, HOH = 110° (computed for this note)"
    **Setup.**

    - **Space.** RHF orbitals, all 10 electrons correlated. The 141 determinants with at most double excitations, out of 441.
    - **Energies.** $E_{\text{CISD}} = -75.0149224747$ $E_h$, identical to PySCF's CISD; $E_{\text{RHF}} = -74.9570541297$ $E_h$.
    - **RDM energy check.** $\sum Dh + \tfrac12\sum dg$ reproduces $E$ to $3\times10^{-14}$.
    - **Antisymmetric part of $\mathbf X$.** Occupied-occupied $2\times10^{-15}$, virtual-virtual $2\times10^{-19}$ (rotation invariance), occupied-virtual up to $1.0\times10^{-3}$.

    | Gradient ($E_h$/bohr) | $O_z$ | $H_{1y}$ | $H_{1z}$ | max deviation from FD |
    |---|---:|---:|---:|---:|
    | Central finite differences of $E_{\text{CISD}}$ (step $10^{-4}$) | 0.037471 | 0.026928 | −0.018735 | — |
    | Eq. 6.23 with 9 CPHF solutions $\mathbf U^x$ | 0.037471 | 0.026928 | −0.018735 | $1.6\times10^{-9}$ |
    | Z vector, one solve ([[z-vector-method]]) | 0.037471 | 0.026928 | −0.018735 | $1.6\times10^{-9}$ |
    | PySCF CISD gradient | 0.037471 | 0.026928 | −0.018735 | $2.9\times10^{-9}$ |
    | Orbital response dropped ($K^x = 0$, $W$ kept) | 0.037281 | 0.027001 | −0.018641 | $1.9\times10^{-4}$ |
    | RHF gradient, for comparison | −0.012562 | 0.055724 | 0.006281 | $5.0\times10^{-2}$ |

    - **Dropping the response.** The error is $2\times10^{-4}$ $E_h$/bohr, small here because the CISD orbital gradient is small (a near-Brillouin case). It is still of the order of typical force-convergence thresholds, so a geometry optimized without it would stop at the wrong place. The error grows with stronger correlation and with frozen-core or multireference CI, where the orbital gradient is larger.
    - **Correlation.** It changes the gradient qualitatively at this stretched, wide-angle geometry: the sign of the $O_z$ component flips.

## Source

Yamaguchi, Osamura, Goddard and Schaefer, *A New Dimension to Quantum Chemistry* (Oxford University Press, New York, 1994), Ch. 6, Secs. 6.1-6.4, Eqs. (6.1)-(6.48), pp. 83-90. Equations read from the page images. The identification $X = F^{\mathsf T}$ with the notebook's generalized Fock matrix and the symmetrized form with $K^x$ are my own restatements, both checked numerically. Z-vector reference: N. C. Handy and H. F. Schaefer III, *J. Chem. Phys.* **81**, 5031 (1984), doi:10.1063/1.447489. Computations: PySCF 2.15 (integrals, RHF, `fci` string routines for the determinant CISD), `gradients/ci_grad.py`.
