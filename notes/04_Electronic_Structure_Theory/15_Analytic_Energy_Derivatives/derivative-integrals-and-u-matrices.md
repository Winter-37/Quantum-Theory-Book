---
id: derivative-integrals-and-u-matrices
title: Derivative integrals and the U matrices - how MO coefficients and MO integrals respond to a nuclear displacement
summary: The bookkeeping behind every analytic derivative. The response of the MO coefficients is written as ∂C/∂x = C U^x. Differentiating the orthonormality condition gives U^x_pq + U^x_qp + S^x_pq = 0, so only the antisymmetric part of U^x is a genuine unknown. Integrals over moving basis functions split into skeleton (core) derivatives, which hold the MO coefficients fixed, and U-terms. Also covered: which response quantities each derivative order needs (Wigner's 2n+1 rule), the second-order relation ∂U^x/∂y = U^xy − U^y U^x, and the nuclear-repulsion derivatives. Skeleton integrals from PySCF are checked against finite differences, and CPHF U matrices against differentiated canonical MOs, for water.
status: in-progress
kind: derivation
level: advanced
tags: [analytic-derivatives, u-matrix, skeleton-integrals, derivative-integrals, orthonormality, mo-coefficients, 2n+1-rule]
prerequisites: [rhf, gaussian-basis-functions, analytic-gradients-and-force-constants]
related: [cphf-closed-shell, rhf-analytic-gradient, ci-analytic-gradient, orbital-rotations, molecular-properties-and-response, integral-notation]
order: 30
date: 2026-11-07
---

## Notation used in this folder

The gradient notes in this folder (RHF and CI gradients, CPHF, CPCI, Z-vector, RHF Hessian) follow Yamaguchi, Osamura, Goddard and Schaefer (YOGS below), translated into the notebook's notation.

| Quantity | This notebook | YOGS |
|---|---|---|
| Perturbations (nuclear Cartesian coordinates, fields) | $x, y$ | $a, b$ |
| Occupied / virtual / general MOs | $i,j,k,l$ / $a,b,c,d$ / $p,q,r,s,m$ | d.o. / virt. / $i,j,k,l,m$ |
| Atomic orbitals | $\mu,\nu,\lambda,\sigma$ | $\mu,\nu,\rho,\sigma$ |
| MO coefficients | $C_{\mu p}$ (MO $p$ in column $p$) | $C^p_\mu$ |
| Closed-shell density | $P_{\mu\nu} = 2\sum_i C_{\mu i}C_{\nu i}$ | $D_{\mu\nu} = P_{\mu\nu}/2$ |
| Energy-weighted density (RHF) | $W_{\mu\nu} = 2\sum_i\varepsilon_iC_{\mu i}C_{\nu i}$ | $W_{\mu\nu}$ is half of this |
| One- and two-electron RDMs | $D_{pq}$, $d_{pqrs}$ ([[density-matrices-second-quantization]]) | $Q_{pq} = D_{pq}$, $G_{pqrs} = \tfrac12 d_{pqrs}$ |
| CI Lagrangian | $X_{pq} = F_{qp}$, with $F$ the generalized Fock matrix ([[generalized-fock-matrix-and-orbital-hessian]]) | $X_{ij}$ |

Integrals are real and in chemists' notation, $(pq|rs)$ ([[integral-notation]]). All derivatives are total derivatives unless a superscript marks a skeleton derivative (defined below).

## Expansion of the MO coefficients

**Perturbed Hamiltonian.** For two real perturbations $x, y$ (nuclear coordinates, or field components),

$$
\hat H(x,y) = \hat H_0 + x\hat H'_x + y\hat H'_y + \tfrac12x^2\hat H''_{xx} + xy\hat H''_{xy} + \tfrac12y^2\hat H''_{yy} + \cdots
$$

The overlap, one-electron and two-electron AO integrals are expanded in the same way. For a field with field-independent basis functions only $h_{\mu\nu}$ changes; the expansions are kept general.

**The U matrices (YOGS Eqs. 3.5-3.8).** The perturbed MOs are expanded in the unperturbed ones:

$$
\frac{\partial C_{\mu q}}{\partial x} = \sum_p C_{\mu p}U^x_{pq},
\qquad
\frac{\partial^2C_{\mu q}}{\partial x\,\partial y} = \sum_pC_{\mu p}U^{xy}_{pq},
$$

that is, $\partial\mathbf C/\partial x = \mathbf C\mathbf U^x$. The sum over $p$ runs over all MOs, occupied and virtual. $U^x_{pq}$ is the amount of MO $p$ mixed into MO $q$.

**Second-order relation (YOGS Eq. 3.14).** Differentiating $\partial\mathbf C/\partial x = \mathbf C\mathbf U^x$ with respect to $y$ and comparing with the definition of $\mathbf U^{xy}$:

$$
\frac{\partial U^x_{pq}}{\partial y} = U^{xy}_{pq} - \sum_mU^y_{pm}U^x_{mq} .
$$

So the derivative of $\mathbf U^x$ is not $\mathbf U^{xy}$.

## Skeleton (core) derivative integrals

**AO derivatives.** Basis functions move with their nuclei. The overlap derivative is

$$
\frac{\partial S_{\mu\nu}}{\partial x} = \Big\langle\frac{\partial\chi_\mu}{\partial x}\Big|\chi_\nu\Big\rangle + \Big\langle\chi_\mu\Big|\frac{\partial\chi_\nu}{\partial x}\Big\rangle .
$$

- **One-electron integrals.** These also contain the operator derivative $\langle\chi_\mu|\partial\hat h/\partial x|\chi_\nu\rangle$, which is the Hellmann-Feynman term of [[analytic-gradients-and-force-constants]].
- **Two-electron integrals.** These contain only the four basis-function derivatives, because $r_{12}^{-1}$ does not depend on nuclear positions (YOGS Eq. 3.32).
- **Gaussians.** The derivative of a Cartesian Gaussian is a Gaussian with angular momentum one higher and one lower ([[gaussian-basis-functions]]), so derivative integrals cost a small multiple of ordinary integrals.

**Skeleton MO integrals (YOGS Eqs. 3.40, 3.75).** Transform the AO derivatives with the unperturbed coefficients held fixed:

$$
S^x_{pq} = \sum_{\mu\nu}C_{\mu p}C_{\nu q}\frac{\partial S_{\mu\nu}}{\partial x},\qquad
h^x_{pq} = \sum_{\mu\nu}C_{\mu p}C_{\nu q}\frac{\partial h_{\mu\nu}}{\partial x},\qquad
(pq|rs)^x = \sum_{\mu\nu\lambda\sigma}C_{\mu p}C_{\nu q}C_{\lambda r}C_{\sigma s}\frac{\partial(\mu\nu|\lambda\sigma)}{\partial x} .
$$

Second skeleton derivatives ($S^{xy}$, $h^{xy}$, $(pq|rs)^{xy}$) are defined the same way. Skeleton integrals carry the whole AO change and nothing of the MO change. $S^x_{pq}$ is not zero, even though the MOs stay orthonormal.

## Total derivatives of MO integrals

Differentiate $h_{pq} = \sum_{\mu\nu}C_{\mu p}C_{\nu q}h_{\mu\nu}$ with the product rule and insert $\partial\mathbf C/\partial x = \mathbf{CU}^x$ (YOGS Eqs. 3.59, 3.78, and the two-electron analogue in Sec. 3.9):

$$
\frac{\partial S_{pq}}{\partial x} = S^x_{pq} + \sum_m\big(U^x_{mp}S_{mq} + U^x_{mq}S_{pm}\big),
\qquad
\frac{\partial h_{pq}}{\partial x} = h^x_{pq} + \sum_m\big(U^x_{mp}h_{mq} + U^x_{mq}h_{pm}\big),
$$

$$
\frac{\partial(pq|rs)}{\partial x} = (pq|rs)^x + \sum_m\big[U^x_{mp}(mq|rs) + U^x_{mq}(pm|rs) + U^x_{mr}(pq|ms) + U^x_{ms}(pq|rm)\big].
$$

Each index of an MO integral picks up one U-term. In matrix form, $\partial\mathbf h/\partial x = \mathbf h^x + \mathbf U^{x\mathsf T}\mathbf h + \mathbf h\mathbf U^x$.

## Orthonormality: what is really unknown

**First order (YOGS Eq. 3.46).** The MOs stay orthonormal, $S_{pq} = \delta_{pq}$, at every geometry. So $\partial S_{pq}/\partial x = 0$, and with $S_{mq} = \delta_{mq}$:

$$
U^x_{pq} + U^x_{qp} + S^x_{pq} = 0,
\qquad
U^x_{pp} = -\tfrac12S^x_{pp} .
$$

**Consequences.**

- **Symmetric part.** It is fixed by the skeleton overlap: $\tfrac12(U^x_{pq} + U^x_{qp}) = -\tfrac12S^x_{pq}$.
- **Antisymmetric part.** It describes orbital rotation and is the real unknown. It is determined by the variational conditions: by CPHF for an SCF reference ([[cphf-closed-shell]]).
- **Independent and non-independent pairs (YOGS Sec. 10.1).** An RHF energy is invariant to rotations among occupied orbitals and among virtual orbitals. So the variational conditions fix only the occupied-virtual elements $U^x_{ai}$; then $U^x_{ia} = -U^x_{ai} - S^x_{ai}$. The occupied-occupied and virtual-virtual elements are fixed only by a convention:
    - **Canonical orbitals.** Keeping $\mathbf F$ diagonal gives YOGS Eq. 10.26. That formula divides by $\varepsilon_q - \varepsilon_p$, so it fails for degenerate orbitals.
    - **Any other choice** obeying the symmetric constraint. $U^x_{pq} = -\tfrac12S^x_{pq}$ is the simplest.
    - **Invariance.** Energy derivatives of methods invariant to these rotations do not depend on the choice. Wave-function derivatives such as $\partial C_I/\partial x$ do ([[cpci-and-ci-hessian]]).

**Second order (YOGS Eqs. 3.50-3.55, 4.50).** In the same way, $U^{xy}_{pq} + U^{xy}_{qp} + \xi^{xy}_{pq} = 0$. Here $\xi^{xy} = S^{xy} + \eta^{xy}$ collects products of first-order $U$ and $S$ matrices. Its diagonal is

$$
\eta^{xy}_{pp} = 2\sum_m\big(U^x_{pm}U^y_{pm} - S^x_{pm}S^y_{pm}\big),
$$

which is the form used in the RHF Hessian ([[rhf-analytic-hessian]]).

## Nuclear repulsion

With $V_{\text{nn}} = \sum_{A<B}Z_AZ_B/R_{AB}$ (YOGS Sec. 3.10):

$$
\frac{\partial V_{\text{nn}}}{\partial X_A} = -\sum_{B\neq A}Z_AZ_B\frac{X_A - X_B}{R_{AB}^3},
\qquad
\frac{\partial^2V_{\text{nn}}}{\partial X_A\,\partial X_B} = Z_AZ_B\Big[\frac{1}{R_{AB}^3} - \frac{3(X_A - X_B)^2}{R_{AB}^5}\Big]\quad(A\neq B),
$$

with the remaining Cartesian blocks following by symmetry. These are added to the electronic derivatives.

## Which response is needed at which order

**Wigner's 2n+1 rule (YOGS Sec. 2.10).** If the wave-function parameters are variational, knowing them to order $n$ fixes the energy to order $2n+1$. Parameters that are not variational for the energy must be known to the same order as the derivative. That is why a CI built on fixed SCF orbitals needs orbital response already for the gradient.

| Derivative | RHF (orbitals variational) | CI on SCF orbitals | MCSCF (orbitals and CI variational) |
|---|---|---|---|
| $E^x$ | $\mathbf C$ only | $\mathbf U^x$ (or one Z vector) | $\mathbf C$, $C_I$ |
| $E^{xy}$ | $\mathbf U^x$ | $\mathbf U^{xy}$ (or Z) and $\partial C_I/\partial x$ | $\mathbf U^x$, $\partial C_I/\partial x$ |
| $E^{xyz}$ | $\mathbf U^x$ | $\mathbf U^{xyz}$ and $\partial C_I/\partial x$ | $\mathbf U^x$, $\partial C_I/\partial x$ |
| $E^{xyzw}$ | $\mathbf U^{xy}$ | $\mathbf U^{xyzw}$ and $\partial^2C_I/\partial x\partial y$ | $\mathbf U^{xy}$, $\partial^2C_I/\partial x\partial y$ |

This is YOGS Table 2.1, adapted. The CI column is without the Z-vector method; with it, the highest-order $\mathbf U$ in each row is replaced by one Z-vector solve ([[z-vector-method]]).

!!! example "Water: skeleton integrals and U matrices (computed for this note)"
    Water with R(OH) = 1.95 bohr and HOH = 110° (the geometry of [[analytic-gradients-and-force-constants]]). All 9 Cartesian coordinates.

    - **Skeleton AO integrals, 6-31G.** The analytic derivatives (PySCF `int1e_ipovlp`, `int2e_ip1`, `hcore_generator`) agree with central differences of the AO integrals (step $10^{-4}$ bohr) to $9\times10^{-10}$ ($S$), $7\times10^{-9}$ ($h$) and $1\times10^{-9}$ (ERI).
    - **U matrices.** $\mathbf U^x$ was assembled from CPHF (occupied-virtual block), orthonormality (virtual-occupied block) and the canonical condition (occupied-occupied and virtual-virtual blocks). It was compared with $\mathbf C^{\mathsf T}\mathbf S\,\partial\mathbf C/\partial x$ from finite differences of sign-aligned canonical MOs.
        - **STO-3G.** Maximum deviation $2\times10^{-6}$ (step $10^{-4}$).
        - **6-31G, step $10^{-3}$.** Deviation $1.4\times10^{-7}$ in the occupied-virtual block and $3\times10^{-7}$ in the occupied-occupied block, but $2\times10^{-2}$ in the virtual-virtual block. Two virtual orbitals lie only 0.014 $E_h$ apart (1.0568 and 1.0710), so the canonical virtual-virtual elements, which carry $1/(\varepsilon_b - \varepsilon_a)$, are ill-conditioned. This is YOGS's warning about Eq. 10.26 seen in practice. No energy derivative of an RHF or CISD wave function depends on that block.
    - **Orthonormality.** With canonical $\mathbf U^x$, the total $\partial F_{pq}/\partial x$ is diagonal to $10^{-14}$.

## Source

Yamaguchi, Osamura, Goddard and Schaefer, *A New Dimension to Quantum Chemistry: Analytic Derivative Methods in Ab Initio Molecular Electronic Structure Theory* (Oxford University Press, New York, 1994), Ch. 2, Secs. 2.8-2.10 and Table 2.1, pp. 20-27; Ch. 3, Secs. 3.1-3.10, Eqs. (3.1)-(3.127), pp. 29-52; Sec. 10.1, Eq. (10.26), p. 132. Equations read from the page images and converted to the notation above. Computations: PySCF 2.15, scripts `gradients/common.py` and `gradients/rhf_grad_hess.py`.
