---
id: one-particle-rdm
title: The one-particle reduced density matrix
summary: Definition of the first-order reduced density matrix γ(x1, x1') by integrating out N−1 electrons, its discrete representation in a spin-orbital basis, Hermiticity and trace N, one-electron expectation values as tr(hγ), the second-quantized form, and the idempotent single-determinant case.
status: in-progress
kind: theory
level: intermediate
tags: [rdm, density-matrix, one-matrix, expectation-values, second-quantization]
prerequisites: [slater-determinants, creation-and-annihilation-operators]
related: [density-matrices-second-quantization, natural-orbitals, rhf, population-analysis]
also: []
date: 2026-11-03
---

## Density function and density matrix

For a normalized $N$-electron wave function $\Phi(\mathbf x_1,\dots,\mathbf x_N)$, $|\Phi|^2\,\mathrm d\mathbf x_1\cdots\mathrm d\mathbf x_N$ is the joint probability of all electron positions. Integrating out all but one electron gives the **one-electron density**:

$$
\rho(\mathbf x_1) = N\int\mathrm d\mathbf x_2\cdots\mathrm d\mathbf x_N\ \Phi(\mathbf x_1,\mathbf x_2,\dots,\mathbf x_N)\,\Phi^*(\mathbf x_1,\mathbf x_2,\dots,\mathbf x_N),
\qquad
\int\mathrm d\mathbf x_1\,\rho(\mathbf x_1) = N .
$$

The factor $N$ accounts for the indistinguishable electrons, any of which could be "electron 1".

Letting the primed and unprimed first arguments differ gives the **first-order reduced density matrix** (the one-matrix, 1-RDM):

$$
\gamma(\mathbf x_1,\mathbf x_1') = N\int\mathrm d\mathbf x_2\cdots\mathrm d\mathbf x_N\ \Phi(\mathbf x_1,\mathbf x_2,\dots,\mathbf x_N)\,\Phi^*(\mathbf x_1',\mathbf x_2,\dots,\mathbf x_N),
\qquad
\gamma(\mathbf x_1,\mathbf x_1) = \rho(\mathbf x_1).
$$

It is a kernel with two continuous indices: a "continuous matrix" ([[orthonormal-functions-and-operators]]).

## Discrete representation

Expand in an orthonormal spin-orbital basis $\{\chi_i\}$:

$$
\gamma(\mathbf x_1,\mathbf x_1') = \sum_{ij}\chi_i(\mathbf x_1)\,\gamma_{ij}\,\chi_j^*(\mathbf x_1'),
\qquad
\gamma_{ij} = \int\mathrm d\mathbf x_1\mathrm d\mathbf x_1'\ \chi_i^*(\mathbf x_1)\,\gamma(\mathbf x_1,\mathbf x_1')\,\chi_j(\mathbf x_1').
$$

**Properties (Szabo Ex. 4.4, 4.5).**

- $\gamma_{ij}^* = \gamma_{ji}$: the matrix $\boldsymbol\gamma$ is Hermitian. This follows from $\gamma(\mathbf x_1,\mathbf x_1')^* = \gamma(\mathbf x_1',\mathbf x_1)$.
- $\operatorname{tr}\boldsymbol\gamma = \sum_i\gamma_{ii} = \int\rho = N$.

**Second quantization (Szabo Ex. 4.7).** With $\hat\psi(\mathbf x) = \sum_i\chi_i(\mathbf x)a_i$,

$$
\gamma(\mathbf x_1,\mathbf x_1') = \langle\Phi|\hat\psi^\dagger(\mathbf x_1')\,\hat\psi(\mathbf x_1)|\Phi\rangle
\quad\Longrightarrow\quad
\gamma_{ij} = \langle\Phi|a_j^\dagger a_i|\Phi\rangle .
$$

The diagonal element $\gamma_{ii} = \langle\hat n_i\rangle$ is the mean occupation of $\chi_i$, between 0 and 1 by the Pauli principle. For real wave functions $\boldsymbol\gamma$ is real symmetric and the order of $i, j$ does not matter. For complex ones, check which index convention a program uses.

## One-electron expectation values

For $\hat{\mathcal O}_1 = \sum_i h(\mathbf x_i)$ (Szabo Ex. 4.6):

$$
\langle\Phi|\hat{\mathcal O}_1|\Phi\rangle = \int\mathrm d\mathbf x_1\ \big[h(\mathbf x_1)\,\gamma(\mathbf x_1,\mathbf x_1')\big]_{\mathbf x_1'=\mathbf x_1} = \sum_{ij}h_{ji}\gamma_{ij} = \operatorname{tr}(\mathbf h\boldsymbol\gamma),
$$

with $h_{ji} = \langle j|h|i\rangle$. The prime is removed only **after** $h$ acts, which matters for differential operators such as the kinetic energy.

All one-electron properties of any state are fixed by its 1-RDM: dipole moments, kinetic and nuclear-attraction energies, populations. The two-electron energy needs the second-order matrix, which is not treated in Szabo.

## Single-determinant (Hartree-Fock) case

For $|\Psi_0\rangle = |\chi_1\cdots\chi_N\rangle$,

$$
\gamma^{\text{HF}}(\mathbf x_1,\mathbf x_1') = \sum_{a}^{N}\chi_a(\mathbf x_1)\chi_a^*(\mathbf x_1'),
\qquad
\gamma^{\text{HF}}_{ij} = \begin{cases}\delta_{ij} & j\text{ occupied}\\ 0 & \text{otherwise.}\end{cases}
$$

**Idempotency.** In the Hartree-Fock spin-orbital basis $\boldsymbol\gamma$ is diagonal with occupation numbers 1 and 0, so

$$
(\boldsymbol\gamma^{\text{HF}})^2 = \boldsymbol\gamma^{\text{HF}}.
$$

$\boldsymbol\gamma^{\text{HF}}$ is the projector onto the occupied space. In an atomic-orbital basis this becomes $\mathbf{PSP} = 2\mathbf P$ for the closed-shell spatial density matrix ([[rhf]]).

**Correlated wave functions.** For a correlated $\Phi$, $\boldsymbol\gamma$ is not idempotent: $\boldsymbol\gamma^2\ne\boldsymbol\gamma$, and its eigenvalues lie strictly between 0 and 1. The eigenvectors and eigenvalues are the [[natural-orbitals]] and their occupation numbers.

**Spatial (spin-summed) 1-RDM.** For spin-free problems one sums over spin:

$$
D_{pq} = \gamma_{p\alpha,q\alpha} + \gamma_{p\beta,q\beta},
\qquad
\operatorname{tr}\mathbf D = N,
$$

with eigenvalues between 0 and 2 (equal to 2 or 0 for a closed-shell determinant).

## Source

Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996; reprint of the revised first edition, McGraw-Hill, 1989), Sec. 4.4, pp. 252-254, Eqs. (4.33)-(4.40), Ex. 4.4-4.7. The field-operator form and the spin-summed matrix are standard notation added here.
