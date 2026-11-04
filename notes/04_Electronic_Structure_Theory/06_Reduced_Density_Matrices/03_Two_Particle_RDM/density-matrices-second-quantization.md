---
id: density-matrices-second-quantization
title: One- and two-electron density matrices in second quantization - occupation and pair-occupation numbers, bounds, orbital and spin densities
summary: Expectation values of any one- and two-electron operator need only D_PQ = ⟨a†_P a_Q⟩ and d_PQRS = ⟨a†_P a†_R a_S a_Q⟩. Both are Hermitian and positive semidefinite. Diagonal elements are occupation numbers 0 ≤ ω_P ≤ 1 summing to N and pair occupations 0 ≤ ω_PQ ≤ min(ω_P, ω_Q) summing to N(N−1)/2, with Schwarz bounds on off-diagonal elements. For a single ON vector the two-electron density factorizes into one-electron densities. Spin-free orbital densities D_pq = ⟨E_pq⟩, d_pqrs = ⟨e_pqrs⟩ (0 ≤ ω_p ≤ 2), the spin-density matrix with trace M, and the coordinate densities. All properties checked on full-CI water and H₂O⁺.
status: in-progress
kind: theory
level: intermediate
tags: [rdm, two-particle-rdm, density-matrix, occupation-numbers, pair-occupation, spin-density, second-quantization]
prerequisites: [one-particle-rdm, second-quantized-operators, spin-tensor-operators]
related: [natural-orbitals, full-ci, population-analysis, slater-condon-rules, electron-correlation]
also: [04_Electronic_Structure_Theory/06_Reduced_Density_Matrices/02_One_Particle_RDM, 04_Electronic_Structure_Theory/06_Reduced_Density_Matrices/04_Spin_Resolved_RDMs, 04_Electronic_Structure_Theory/06_Reduced_Density_Matrices/08_RDM_Based_Energy_Expressions]
date: 2026-11-04
---

## Densities determine all expectation values

For a Hermitian operator with one- and two-electron parts, $\hat\Omega = \sum_{PQ}\Omega_{PQ}a_P^\dagger a_Q + \tfrac12\sum_{PQRS}\Omega_{PQRS}a_P^\dagger a_R^\dagger a_Sa_Q + \Omega_0$, and a normalized state $|0\rangle = \sum_{\mathbf k}C_{\mathbf k}|\mathbf k\rangle$:

$$
\langle0|\hat\Omega|0\rangle = \sum_{PQ}\bar D_{PQ}\Omega_{PQ} + \frac12\sum_{PQRS}\bar d_{PQRS}\Omega_{PQRS} + \Omega_0,
\qquad
\bar D_{PQ} = \langle0|a_P^\dagger a_Q|0\rangle,\quad \bar d_{PQRS} = \langle0|a_P^\dagger a_R^\dagger a_Sa_Q|0\rangle .
$$

(HJO's index order: the pair $PQ$ belongs to electron 1, $RS$ to electron 2, matching the integrals $g_{PQRS} = (PQ|RS)$. PySCF's `make_rdm2` uses the same order. Bars mark spin-orbital densities.)

## The one-electron density matrix

**Properties.**

- **Hermitian:** $\bar D_{PQ} = \bar D_{QP}^*$, symmetric for real states.
- **Positive semidefinite:** each element is an inner product of the $(N-1)$-electron states $a_Q|0\rangle$ and $a_P|0\rangle$.
- **Occupation numbers:** $\omega_P = \bar D_{PP} = \langle0|\hat N_P|0\rangle = \lVert\hat N_P|0\rangle\rVert^2$. Since $\hat N_P$ is a projector, $\hat N_P|0\rangle = \sum_{\mathbf k}k_PC_{\mathbf k}|\mathbf k\rangle$ is the part of the state with $\phi_P$ occupied, so $0\le\omega_P\le1$.
- **Trace:** $\operatorname{Tr}\bar{\mathbf D} = \langle0|\hat N|0\rangle = N$.
- **Schwarz bound:** $|\bar D_{PQ}|\le\sqrt{\omega_P\omega_Q}$.
- **Single ON vector:** $\bar D_{PQ} = \delta_{PQ}k_P$, diagonal and idempotent.

**Natural spin orbitals.** Diagonalizing $\bar{\mathbf D} = \mathbf U\boldsymbol\eta\mathbf U^\dagger$ gives occupations $0\le\eta_P\le1$ summing to $N$ ([[natural-orbitals]], [[one-particle-rdm]]).

## The two-electron density matrix

**Redundancy.** Anticommutation gives $\bar d_{PQRS} = -\bar d_{RQPS} = -\bar d_{PSRQ} = \bar d_{RSPQ}$, so elements with $P = R$ or $Q = S$ vanish (Pauli). The independent elements form the matrix

$$
\bar T_{PQ,RS} = \langle0|a_P^\dagger a_Q^\dagger a_Sa_R|0\rangle = \bar d_{PRQS},\qquad P>Q,\ R>S,
$$

of dimension $M(M-1)/2$.

**Properties (parallel to the one-electron case).**

- **Hermitian and positive semidefinite:** elements are inner products of $(N-2)$-electron states.
- **Pair occupations:** $\omega_{PQ} = \bar T_{PQ,PQ} = \langle0|\hat N_P\hat N_Q|0\rangle$, the weight of the part of $|0\rangle$ with $\phi_P$ and $\phi_Q$ **both** occupied. Each projector can only reduce the norm, so

$$
0\le\omega_{PQ}\le\min(\omega_P,\omega_Q)\le1,\qquad \sum_{P>Q}\omega_{PQ} = \tfrac12N(N-1).
$$

  The Schwarz inequality gives the weaker bound $\omega_{PQ}\le\sqrt{\omega_P\omega_Q}$.
- **Picture:** $\bar{\mathbf D}$ distributes $N$ electrons over $M$ spin orbitals; $\bar{\mathbf T}$ distributes $N(N-1)/2$ pairs over $M(M-1)/2$ spin-orbital pairs.

**Single ON vector: no correlation.** $\bar T_{PQ,RS} = \delta_{PR}\delta_{QS}k_Pk_Q$. Pair occupations are products of occupations, and the two-electron density follows from the one-electron density ($\bar d_{PQRS} = \bar D_{PQ}\bar D_{RS} - \bar D_{PS}\bar D_{RQ}$, the Hartree-Fock factorization). A correlated state has a $\bar{\mathbf T}$ that is neither diagonal nor obtainable from $\bar{\mathbf D}$. The difference is the cumulant (general knowledge; tree folder 07_Density_Cumulants).

**Coordinate representation.** With $\gamma_1(\mathbf x_1,\mathbf x_1')$ and $\gamma_2(\mathbf x_1,\mathbf x_2,\mathbf x_1',\mathbf x_2')$ the reduced density matrices of first quantization,

$$
\gamma_1(\mathbf x_1,\mathbf x_1') = \sum_{PQ}\bar D_{PQ}\phi_P^*(\mathbf x_1')\phi_Q(\mathbf x_1),\qquad
\gamma_2(\mathbf x_1,\mathbf x_2,\mathbf x_1',\mathbf x_2') = \tfrac12\sum_{PQRS}\bar d_{PQRS}\phi_P^*(\mathbf x_1')\phi_Q(\mathbf x_1)\phi_R^*(\mathbf x_2')\phi_S(\mathbf x_2).
$$

The second-quantization definitions, expectation values of excitation operators, are much simpler than the integrals over $N - 1$ or $N - 2$ coordinates.

## Spin-free (orbital) densities

**Definitions.** For singlet operators ([[spin-tensor-operators]]), $\hat\Omega = \sum_{pq}\Omega_{pq}E_{pq} + \tfrac12\sum_{pqrs}\Omega_{pqrs}e_{pqrs}$, so

$$
D_{pq} = \langle0|E_{pq}|0\rangle,\qquad d_{pqrs} = \langle0|e_{pqrs}|0\rangle = \langle0|E_{pq}E_{rs} - \delta_{rq}E_{ps}|0\rangle = \sum_{\sigma\tau}\langle0|a_{p\sigma}^\dagger a_{r\tau}^\dagger a_{s\tau}a_{q\sigma}|0\rangle .
$$

In terms of spin-orbital densities, $D_{pq} = \bar D_{p\alpha,q\alpha} + \bar D_{p\beta,q\beta}$, and $d_{pqrs}$ is the sum of the four spin blocks $\alpha\alpha\alpha\alpha$, $\beta\beta\beta\beta$, $\alpha\alpha\beta\beta$ and $\beta\beta\alpha\alpha$.

**Symmetries.** $D_{pq} = D_{qp}^*$ and $d_{pqrs} = d_{rspq} = d_{qpsr}^* = d_{srqp}^*$. The antisymmetries $\bar d_{PQRS} = -\bar d_{RQPS}$ of the spin-orbital density are **lost**: integrating over spin forces the first two indices (and the last two) to carry the same spin.

**Bounds.** $\omega_p = D_{pp}$ and $\omega_{pq} = d_{ppqq}$ satisfy

$$
0\le\omega_p\le2,\qquad 0\le\omega_{pq}\le2(2 - \delta_{pq}),
$$

since an orbital holds two electrons and a pair of distinct doubly occupied orbitals contains four electron pairs. Natural-orbital occupations lie in $[0, 2]$ and sum to $N$.

**Energy.**

$$
E = \sum_{pq}h_{pq}D_{pq} + \tfrac12\sum_{pqrs}g_{pqrs}d_{pqrs} + h_{\text{nuc}} .
$$

## The spin-density matrix

Triplet operators such as the Fermi-contact operator need a different density. For a state with definite $M$, only the $\hat T_{pq}^{1,0}$ component survives ([[spin-tensor-operators]]):

$$
D_{pq}^{\mathrm T} = \tfrac1{\sqrt2}\langle0|\hat T_{pq}^{1,0}|0\rangle = \tfrac12\big(\bar D_{p\alpha,q\alpha} - \bar D_{p\beta,q\beta}\big),\qquad \operatorname{Tr}\mathbf D^{\mathrm T} = \langle0|\hat S_z|0\rangle = M .
$$

It measures the excess of $\alpha$ over $\beta$ density. Spin occupations are $\omega_p^{\mathrm T} = \tfrac12(\bar\omega_{p\alpha} - \bar\omega_{p\beta})$.

## Density functions

The operators $\delta(\mathbf r) = \sum_{pq}\phi_p^*(\mathbf r)\phi_q(\mathbf r)E_{pq}$ and $\delta(\mathbf r_1,\mathbf r_2) = \tfrac12\sum_{pqrs}\phi_p^*(\mathbf r_1)\phi_q(\mathbf r_1)\phi_r^*(\mathbf r_2)\phi_s(\mathbf r_2)e_{pqrs}$ probe one electron at $\mathbf r$ or a pair at $(\mathbf r_1,\mathbf r_2)$. Their expectation values are the electron density and the pair density:

$$
\rho(\mathbf r) = \sum_{pq}D_{pq}\phi_p^*(\mathbf r)\phi_q(\mathbf r),\qquad
\rho(\mathbf r_1,\mathbf r_2) = \tfrac12\sum_{pqrs}d_{pqrs}\phi_p^*(\mathbf r_1)\phi_q(\mathbf r_1)\phi_r^*(\mathbf r_2)\phi_s(\mathbf r_2),
$$

the spin-integrated diagonals of $\gamma_1$ and $\gamma_2$.

!!! example "Full CI water, STO-3G, Szabo's geometry (computed for this note)"
    14 spin orbitals, 10 electrons, $E = -75.01242581$ hartree.

    | Property | Value | Requirement |
    |---|---|---|
    | $\operatorname{Tr}\bar{\mathbf D}$ | 10.000000 | $N$ |
    | Eigenvalues of $\bar{\mathbf D}$ | 0.0130 to 1.0000 | $[0, 1]$ |
    | $\bar{\mathbf T}$: dimension, smallest eigenvalue | 91, $5.0\times10^{-5}$ | $\ge0$ |
    | $\operatorname{Tr}\bar{\mathbf T}$ | 45.000000 | $N(N-1)/2$ |
    | $\max[\omega_{PQ} - \min(\omega_P,\omega_Q)]$ | $\le0$ | $\le0$ |
    | $\max(|\bar D_{PQ}| - \sqrt{\omega_P\omega_Q})$ | $\le0$ | $\le0$ |
    | Orbital $\omega_p$ | 0.0264 to 2.0000 | $[0, 2]$ |
    | $\sum_{pq}\omega_{pq}$ | 90.0000 | $N(N-1)$ |
    | $E$ from $D_{pq}$, $d_{pqrs}$ and integrals | −75.01242581 | full-CI energy |

    - **Symmetries.** $d_{pqrs} = d_{rspq} = d_{qpsr}$ to $10^{-16}$, while $d_{pqrs}$ and $d_{rqps}$ differ by up to 6.0: the spin-orbital antisymmetry does not survive spin integration.
    - **Hartree-Fock determinant.** $\bar{\mathbf T}$ is diagonal with trace 45, and every pair occupation is the product of two occupation numbers.
    - **H₂O⁺ doublet ($M = \tfrac12$), full CI.** $\operatorname{Tr}\mathbf D^{\mathrm T} = 0.500000$; the singly occupied orbital carries spin occupation 0.4971.

## Source

Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, Chichester, 2000), Sec. 1.7, pp. 19-25, Eqs. (1.7.1)-(1.7.45); Sec. 2.7, pp. 61-65, Eqs. (2.7.1)-(2.7.35). The explicit HF factorization of $\bar d$ and the cumulant remark are general knowledge. Calculations with PySCF 2.14.
