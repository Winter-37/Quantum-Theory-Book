---
id: second-quantization-in-a-finite-basis
title: Second-quantized operators are projections - operator products and the canonical commutator in a finite basis
summary: In a finite spin-orbital basis a second-quantized operator is the projection of the exact operator onto the basis. The representation of a product of two operators then differs from the product of the representations by a one-electron term Σ(O_PQ − Σ_R A_PR B_RQ) a†_P a_Q that vanishes only for a complete basis, and the commutator [x̂, p̂_x] is a general one-electron operator rather than iN. Water calculations show ⟨[x̂, p̂_x]⟩/iN rising from 0.29 (STO-3G) to 0.96 (aug-cc-pVQZ). First- and second-quantization operators compared.
status: in-progress
kind: theory
level: intermediate
tags: [second-quantization, projection, finite-basis, canonical-commutator, operator-products, basis-set-incompleteness]
prerequisites: [second-quantized-operators, creation-and-annihilation-operators]
related: [nonorthogonal-second-quantization, polarization-propagator-rpa, gaussian-basis-functions, hf-closed-shell-basis-set-trends]
also: [04_Electronic_Structure_Theory/02_Basis_Sets_and_Orbital_Theory]
date: 2026-11-04
---

## Operator products

**Setup.** Let $A^c = \sum_iA^c(\mathbf x_i)$ and $B^c = \sum_iB^c(\mathbf x_i)$ be one-electron operators in first quantization (superscript $c$ for "coordinate"), with second-quantized representations $\hat A = \sum_{PQ}A_{PQ}a_P^\dagger a_Q$ and $\hat B = \sum_{PQ}B_{PQ}a_P^\dagger a_Q$ in an orthonormal spin-orbital basis. Sums and linear combinations are represented faithfully: $aA^c + bB^c\to a\hat A + b\hat B$.

**The product is not.** $A^cB^c$ has a one-electron part $O^c = \sum_iA^c(\mathbf x_i)B^c(\mathbf x_i)$ and a two-electron part $T^c = \tfrac12\sum_{i\ne j}[A^c(\mathbf x_i)B^c(\mathbf x_j) + A^c(\mathbf x_j)B^c(\mathbf x_i)]$. Representing each part and anticommuting to collect terms gives (HJO Eq. 1.5.15)

$$
\widehat{A^cB^c} = \hat A\hat B + \sum_{PQ}\Big(O_{PQ} - \sum_RA_{PR}B_{RQ}\Big)a_P^\dagger a_Q,
\qquad O_{PQ} = \int\phi_P^*(\mathbf x)A^c(\mathbf x)B^c(\mathbf x)\phi_Q(\mathbf x)\,\mathrm d\mathbf x .
$$

**Complete basis.** With $\delta(\mathbf x - \mathbf x') = \sum_{P=1}^\infty\phi_P(\mathbf x)\phi_P^*(\mathbf x')$, $O_{PQ} = \sum_RA_{PR}B_{RQ}$ and the correction vanishes. In a finite basis it does not: the representation of a product depends on **when** the projection is made, before or after multiplying.

## The canonical commutator

**Exact.** $[r_\alpha^c, p_\beta^c] = i\delta_{\alpha\beta}^c$ with $\delta_{\alpha\beta}^c = \sum_{i=1}^N\delta_{\alpha\beta}$, i.e. $i\delta_{\alpha\beta}N$ on an $N$-electron state.

**Projected.** With $[a_P^\dagger a_Q, a_R^\dagger a_S] = \delta_{QR}a_P^\dagger a_S - \delta_{PS}a_R^\dagger a_Q$ ([[second-quantized-operators]]),

$$
[\hat r_\alpha, \hat p_\beta] = \sum_{PQ}a_P^\dagger a_Q\sum_R\big([r_\alpha]_{PR}[p_\beta]_{RQ} - [p_\beta]_{PR}[r_\alpha]_{RQ}\big),
$$

a general one-electron operator. Only in a complete basis does it reduce to $i\delta_{\alpha\beta}\hat N$. Likewise the projected position operator does not commute with the projected electron repulsion.

**Consequences.** Any derivation that uses an exact commutator inherits a basis-set error:

- the equivalence of length and velocity oscillator strengths ([[polarization-propagator-rpa]]);
- the Thomas-Reiche-Kuhn sum rule;
- hypervirial and gauge-origin relations.

!!! example "Water, RHF, Szabo's geometry (computed for this note)"
    For each basis: $\langle0|[\hat x, \hat p_x]|0\rangle/iN$ (exactly 1 in a complete basis), and the resolution-of-identity defect $\langle i|x^2|i\rangle - \sum_p\langle i|x|p\rangle^2$ averaged over the occupied MOs (exactly 0 in a complete basis). $x$ lies in the molecular plane perpendicular to the $C_2$ axis, $z$ along it.

    | Basis | Functions | $\langle[\hat x,\hat p_x]\rangle/iN$ | RI defect, $x^2$ | $\langle[\hat z,\hat p_z]\rangle/iN$ | RI defect, $z^2$ |
    |---|---:|---:|---:|---:|---:|
    | STO-3G | 7 | 0.2945 | 0.1829 | 0.1772 | 0.2227 |
    | 6-31G | 13 | 0.4104 | 0.1668 | 0.3015 | 0.2207 |
    | cc-pVDZ | 24 | 0.7764 | 0.0509 | 0.7540 | 0.0653 |
    | aug-cc-pVTZ | 92 | 0.9087 | 0.0014 | 0.9044 | 0.0021 |
    | aug-cc-pVQZ | 172 | 0.9629 | 0.0003 | 0.9605 | 0.0005 |

    - **Different rates.** The product defect for $x^2$ is already small in aug-cc-pVTZ. The commutator converges much more slowly: it involves derivatives, which probe the core region where the basis is least complete.
    - **Why the numbers are below 1.** $[x][p_x] - [p_x][x]$ restricted to a finite space has zero trace over the **full** basis (a commutator of finite matrices is traceless). The value $iN$ can therefore only be approached on the occupied subspace, never reached exactly.

## First and second quantization compared

| | First quantization | Second quantization |
|---|---|---|
| One-electron operator | $\sum_if^c(\mathbf x_i)$ | $\sum_{PQ}f_{PQ}a_P^\dagger a_Q$ |
| Two-electron operator | $\tfrac12\sum_{i\ne j}g^c(\mathbf x_i,\mathbf x_j)$ | $\tfrac12\sum_{PQRS}g_{PQRS}a_P^\dagger a_R^\dagger a_Sa_Q$ |
| Dependence on the spin-orbital basis | operators independent; determinants depend on it | operators depend on it; ON vectors are abstract |
| Dependence on $N$ | operators depend on $N$ | operators independent of $N$ |
| Exactness | exact operators | projected operators |

(HJO's two-electron integrals are in the charge-distribution order, $g_{PQRS} = \int\int\phi_P^*(\mathbf x_1)\phi_R^*(\mathbf x_2)g\,\phi_Q(\mathbf x_1)\phi_S(\mathbf x_2)$, i.e. $(PQ|RS)$; see [[second-quantized-operators]] for the translation to $\langle ij|kl\rangle$.)

**Practical meaning.** A second-quantized operator acting on an ON vector gives another vector in the same Fock space. A first-quantized operator acting on a determinant generally leaves the space spanned by determinants of the finite basis. The difference is usually hidden in first quantization because one works with matrix elements directly. The incompleteness problems are not caused by second quantization; they appear whenever a finite basis is used, but second quantization exposes them at the operator level.

**Unified description.** Every ON vector is a string of creators on the vacuum, so any matrix element is a vacuum expectation value of an operator string, and antisymmetry follows from the algebra without bookkeeping of phases ([[creation-and-annihilation-operators]]).

## Source

Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, Chichester, 2000), Secs. 1.5-1.6, pp. 14-19, Eqs. (1.5.1)-(1.6.2), Box 1.2. The traceless-commutator remark and the list of consequences are general knowledge. Water calculations with PySCF 2.14.
