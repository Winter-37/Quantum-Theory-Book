---
id: fock-operator
title: Coulomb, exchange, and Fock operators
summary: The spin-orbital Fock operator f = h + Σ_b (J_b − K_b), the local Coulomb and nonlocal exchange operators, their matrix elements, Hermiticity of f, cancellation of self-interaction, and orbital energies.
status: in-progress
kind: theory
level: intermediate
tags: [hartree-fock, fock-operator, coulomb-operator, exchange-operator, mean-field]
prerequisites: [slater-condon-rules, integral-notation]
related: [hartree-fock-equations, rhf, uhf, koopmans-theorem]
also: []
date: 2026-11-03
---

## The Hartree-Fock eigenvalue equation

The Hartree-Fock spin orbitals solve a one-electron eigenvalue equation (derived in [[hartree-fock-equations]]):

$$
f(1)\,\chi_a(1) = \varepsilon_a\,\chi_a(1),
\qquad
f(1) = h(1) + v^{\text{HF}}(1).
$$

Here $h(1) = -\tfrac12\nabla_1^2 - \sum_A Z_A/r_{1A}$ is the core Hamiltonian, and the **Hartree-Fock potential** $v^{\text{HF}}$ is the average field that electron 1 feels from the other electrons. Because $v^{\text{HF}}$ depends on the occupied spin orbitals $\{\chi_b\}$, the equation is nonlinear and is solved iteratively: the self-consistent field.

Labels follow [[excited-determinants]]: $a, b, c$ occupied, $r, s, t$ virtual, $i, j, k$ any. Electron "1" stands for coordinate $\mathbf x_1$.

## Coulomb operator

$$
\mathcal J_b(1)\,\chi_a(1) = \Big[\int\mathrm d\mathbf x_2\ |\chi_b(2)|^2\,r_{12}^{-1}\Big]\chi_a(1).
$$

This is the electrostatic potential of the charge cloud $|\chi_b|^2$, evaluated at $\mathbf x_1$. It is **local**: the result at $\mathbf x_1$ needs only $\chi_a(\mathbf x_1)$. Its expectation value is the Coulomb integral,

$$
\langle\chi_a|\mathcal J_b|\chi_a\rangle = [aa|bb] = \langle ab|ab\rangle .
$$

## Exchange operator

$\mathcal K_b$ is defined by its action:

$$
\mathcal K_b(1)\,\chi_a(1) = \Big[\int\mathrm d\mathbf x_2\ \chi_b^*(2)\,r_{12}^{-1}\,\chi_a(2)\Big]\chi_b(1).
$$

It swaps the labels of the two electrons: $\chi_a$ ends up under the integral and $\chi_b$ outside. Finding $\mathcal K_b\chi_a$ at $\mathbf x_1$ needs $\chi_a$ everywhere, so it is **nonlocal**, an integral operator with kernel $\chi_b(1)\chi_b^*(2)/r_{12}$ ([[orthonormal-functions-and-operators]]). It has no classical analogue; it comes from antisymmetry. Its expectation value is the exchange integral,

$$
\langle\chi_a|\mathcal K_b|\chi_a\rangle = [ab|ba] = \langle ab|ba\rangle .
$$

## The Fock operator

$$
f(1) = h(1) + \sum_{b}^{N}\big[\mathcal J_b(1) - \mathcal K_b(1)\big].
$$

The sum is over all $N$ **occupied** spin orbitals, including $b = a$ when acting on $\chi_a$. This is harmless because

$$
\big[\mathcal J_a(1) - \mathcal K_a(1)\big]\chi_a(1) = 0 .
$$

The spurious repulsion of an electron with itself cancels exactly. Hartree theory, which lacks $\mathcal K$, and approximate density functionals do not have this cancellation (self-interaction error).

**Matrix elements (Szabo Ex. 3.1).**

$$
\langle\chi_i|f|\chi_j\rangle = \langle i|h|j\rangle + \sum_b^N\big([ij|bb] - [ib|bj]\big) = \langle i|h|j\rangle + \sum_b^N\langle ib||jb\rangle .
$$

**Hermiticity (Szabo Ex. 3.4).** $\langle i|h|j\rangle^* = \langle j|h|i\rangle$ and $\langle ib||jb\rangle^* = \langle jb||ib\rangle$, so $f_{ij}^* = f_{ji}$. The Fock operator is Hermitian, its eigenvalues are real, and its eigenfunctions can be chosen orthonormal.

## Orbital energies

Taking diagonal elements, with $\langle ib||ib\rangle = \langle ib|ib\rangle - \langle ib|bi\rangle$:

$$
\varepsilon_a = \langle a|h|a\rangle + \sum_{b}^{N}\langle ab||ab\rangle,
\qquad
\varepsilon_r = \langle r|h|r\rangle + \sum_{b}^{N}\langle rb||rb\rangle .
$$

**Occupied.** $\varepsilon_a$ is the core energy of $\chi_a$ plus Coulomb and exchange with the other $N-1$ electrons ($b=a$ cancels).

**Virtual.** $\varepsilon_r$ includes interaction with all $N$ occupied electrons, as if $\chi_r$ held an $(N+1)$th electron. This asymmetry is why virtual orbitals are poor descriptions of excited states and why Koopmans electron affinities are unreliable ([[koopmans-theorem]]).

**Sum of orbital energies is not the energy.** Summing $\varepsilon_a$ counts each pair interaction twice:

$$
\sum_a^N\varepsilon_a = \sum_a\langle a|h|a\rangle + \sum_{ab}\langle ab||ab\rangle,
\qquad
E_0 = \sum_a\langle a|h|a\rangle + \tfrac12\sum_{ab}\langle ab||ab\rangle = \sum_a\varepsilon_a - \tfrac12\sum_{ab}\langle ab||ab\rangle .
$$

## Fock operator as a nonlocal one-electron potential

The exact problem has $r_{12}^{-1}$ coupling all electrons. Hartree-Fock replaces it by $v^{\text{HF}}$:

- The **Coulomb part** is a local average potential.
- The **exchange part** is a nonlocal correction that keeps same-spin electrons apart (the Fermi hole, [[slater-determinants]]).

What is missing, instantaneous correlation of electron positions beyond exchange, is the correlation energy.

## Source

Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996; reprint of the revised first edition, McGraw-Hill, 1989), Sec. 3.1, pp. 111-115, Eqs. (3.1)-(3.23), Ex. 3.1, 3.4; orbital energies from Sec. 3.3.1, pp. 123-126.
