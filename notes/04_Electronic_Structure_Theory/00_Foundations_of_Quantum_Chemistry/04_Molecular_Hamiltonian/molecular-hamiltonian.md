---
id: molecular-hamiltonian
title: The molecular and electronic Hamiltonians
summary: The nonrelativistic Coulomb Hamiltonian for N electrons and M nuclei in atomic units, its five terms, and the clamped-nucleus electronic Hamiltonian written as one-electron plus two-electron operators.
status: in-progress
kind: theory
level: introductory
tags: [basics, hamiltonian, atomic-units, electronic-structure]
prerequisites: [atomic-units]
related: [born-oppenheimer-approximation, slater-condon-rules, second-quantized-operators]
also: []
date: 2026-11-03
---

## The full Hamiltonian

Quantum chemistry mostly seeks approximate solutions of the nonrelativistic, time-independent Schrödinger equation $\hat H|\Phi\rangle = \mathcal E|\Phi\rangle$ for $N$ electrons at $\mathbf r_i$ and $M$ nuclei at $\mathbf R_A$.

**Notation.** $i,j$ label electrons, $A,B$ nuclei.

- $r_{iA} = |\mathbf r_i - \mathbf R_A|$ is an electron-nucleus distance.
- $r_{ij} = |\mathbf r_i - \mathbf r_j|$ is an electron-electron distance.
- $R_{AB} = |\mathbf R_A - \mathbf R_B|$ is a nucleus-nucleus distance.
- $Z_A$ is the atomic number of nucleus $A$, and $M_A$ is its mass in units of the electron mass.

In [[atomic-units]],

$$
\hat H =
-\sum_{i=1}^{N}\tfrac12\nabla_i^2
-\sum_{A=1}^{M}\frac{1}{2M_A}\nabla_A^2
-\sum_{i=1}^{N}\sum_{A=1}^{M}\frac{Z_A}{r_{iA}}
+\sum_{i=1}^{N}\sum_{j>i}^{N}\frac{1}{r_{ij}}
+\sum_{A=1}^{M}\sum_{B>A}^{M}\frac{Z_AZ_B}{R_{AB}} .
$$

The terms, in order, are:

1. Kinetic energy of the electrons.
2. Kinetic energy of the nuclei.
3. Electron-nucleus Coulomb attraction.
4. Electron-electron repulsion.
5. Nucleus-nucleus repulsion.

The restricted sums $j>i$ and $B>A$ count each pair once.

The Hamiltonian contains no spin coordinates and no relativistic terms (spin-orbit, scalar-relativistic, finite nuclear size). These matter for heavy elements and for fine structure, and are added separately when needed.

## The electronic Hamiltonian

With the nuclei clamped at fixed positions (the [[born-oppenheimer-approximation]]), term 2 is dropped and term 5 becomes a constant. What remains is

$$
\hat H_{\text{elec}} =
-\sum_{i=1}^{N}\tfrac12\nabla_i^2
-\sum_{i=1}^{N}\sum_{A=1}^{M}\frac{Z_A}{r_{iA}}
+\sum_{i=1}^{N}\sum_{j>i}^{N}\frac{1}{r_{ij}} .
$$

The constant term only shifts eigenvalues, so the total energy at fixed nuclei is

$$
\mathcal E_{\text{tot}} = \mathcal E_{\text{elec}} + \sum_{A}\sum_{B>A}\frac{Z_AZ_B}{R_{AB}} .
$$

!!! warning "Electronic vs total energy"
    Programs usually print the total energy (PySCF `e_tot`). Szabo often quotes the electronic energy. For H$_2$ at $R = 1.4$ bohr the difference is $1/1.4 = 0.714286$ hartree. Always check which one is being compared.

## One- and two-electron structure

Group the electronic Hamiltonian by how many electrons each term involves:

$$
\hat H_{\text{elec}} = \sum_{i=1}^{N} h(i) + \sum_{i=1}^{N}\sum_{j>i}^{N} \frac{1}{r_{ij}},
\qquad
h(i) = -\tfrac12\nabla_i^2 - \sum_A\frac{Z_A}{r_{iA}} .
$$

Here $h(i)$ is the **core Hamiltonian** of electron $i$: its kinetic energy plus its attraction to all the bare nuclei. Each part has a known structure:

- **One-electron part.** Every other operator of this type, such as the dipole operator $-\sum_i\mathbf r_i$, has the same structure, $\hat{\mathcal O}_1 = \sum_i h(i)$.
- **Two-electron part.** This is the only part that couples electrons, $\hat{\mathcal O}_2 = \sum_{i<j} v(i,j)$.

This split decides the rules for matrix elements between determinants ([[slater-condon-rules]]) and the form of the operator in [[second-quantized-operators]].

If the electron-electron repulsion is dropped, the Hamiltonian is a sum of independent one-electron operators. Its eigenfunctions are then products of orbitals, which is the starting point for [[slater-determinants]].

## Source

Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996; reprint of the revised first edition, McGraw-Hill, 1989), Sec. 2.1, pp. 40-41 and 43-44, Eqs. (2.1), (2.2), (2.10), (2.14).
