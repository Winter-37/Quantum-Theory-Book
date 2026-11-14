---
id: excited-determinants
title: Excited determinants and the full CI expansion
summary: Occupied/virtual labelling, singly and doubly excited determinants, counting the determinant space, and why the exact wave function in a finite one-electron basis is a linear combination of all N-electron determinants (full CI).
status: in-progress
kind: theory
level: introductory
tags: [ci, full-ci, excitations, determinant-space, correlation-energy]
prerequisites: [slater-determinants, linear-variation-method]
related: [slater-condon-rules, minimal-basis-h2-model, creation-and-annihilation-operators]
order: 40
date: 2026-11-03
---

## Labels

A finite basis gives $2K$ orthonormal spin orbitals, such as those from a Hartree-Fock calculation. The reference determinant occupies $N$ of them:

$$
|\Psi_0\rangle = |\chi_1\chi_2\cdots\chi_a\chi_b\cdots\chi_N\rangle .
$$

**Convention (Szabo).**

| Labels | Meaning |
|---|---|
| $a, b, c, \dots$ | spin orbitals occupied in $|\Psi_0\rangle$ |
| $r, s, t, \dots$ | virtual (unoccupied) spin orbitals |
| $i, j, k, \dots$ | any spin orbital |

## Excited determinants

$|\Psi_0\rangle$ is one of $\binom{2K}{N}$ determinants that can be formed. The others are classified by how many occupied spin orbitals they replace.

- **Singly excited:** $\chi_a\to\chi_r$, with $\chi_r$ placed in the column where $\chi_a$ was,
$$
|\Psi_a^r\rangle = |\chi_1\chi_2\cdots\chi_r\chi_b\cdots\chi_N\rangle .
$$
- **Doubly excited:** $\chi_a\to\chi_r$ and $\chi_b\to\chi_s$,
$$
|\Psi_{ab}^{rs}\rangle = |\chi_1\chi_2\cdots\chi_r\chi_s\cdots\chi_N\rangle ,
$$
and similarly for triples, quadruples, and so on up to $N$-fold.

Keeping the replaced orbital in the **same column** fixes the sign of each excited determinant. Any other ordering differs by a sign from column swaps, which matters when matrix elements are combined.

Excited determinants are not exact excited states. They are a basis for expanding exact states, and are labelled by their relation to $|\Psi_0\rangle$.

## Counting

With $N$ occupied and $2K-N$ virtual spin orbitals, an $n$-fold excitation chooses $n$ occupied and $n$ virtual orbitals:

$$
\#\{n\text{-fold}\} = \binom{N}{n}\binom{2K-N}{n},
\qquad
\sum_{n=0}^{N}\binom{N}{n}\binom{2K-N}{n} = \binom{2K}{N}
$$

(Vandermonde's identity).

!!! example "Minimal-basis benzene (Szabo Ex. 2.7)"
    The basis has 6 C × 5 functions + 6 H × 1 function = 36 spatial functions, so $2K = 72$ spin orbitals, and $N = 42$ electrons ($30$ virtual spin orbitals).

    | Space | Count |
    |---|---:|
    | all determinants $\binom{72}{42}$ | $1.643\times10^{20}$ |
    | singles $42\times30$ | 1 260 |
    | doubles $\binom{42}{2}\binom{30}{2} = 861\times435$ | 374 535 |

    These count all determinants regardless of $M_S$ or spatial symmetry. Restricting to $M_S = 0$ and the right irreducible representation reduces the numbers, but full CI is still out of reach. Computed exactly with Python `math.comb`.

## Form of the exact wave function

**One electron.** If $\{\chi_i(\mathbf x)\}$ is complete, any one-variable function is $\Phi(\mathbf x_1) = \sum_i a_i\chi_i(\mathbf x_1)$.

**Two electrons.** For fixed $\mathbf x_2$, expand in $\mathbf x_1$, then expand each coefficient in $\mathbf x_2$:

$$
\Phi(\mathbf x_1,\mathbf x_2) = \sum_{ij} b_{ij}\,\chi_i(\mathbf x_1)\chi_j(\mathbf x_2).
$$

Antisymmetry $\Phi(\mathbf x_1,\mathbf x_2) = -\Phi(\mathbf x_2,\mathbf x_1)$ requires $b_{ij} = -b_{ji}$, so $b_{ii} = 0$ and the pairs combine into determinants:

$$
\Phi(\mathbf x_1,\mathbf x_2) = \sum_{j>i} b_{ij}\big[\chi_i(\mathbf x_1)\chi_j(\mathbf x_2) - \chi_j(\mathbf x_1)\chi_i(\mathbf x_2)\big] = \sum_{j>i}2^{1/2}b_{ij}\,|\chi_i\chi_j\rangle .
$$

**N electrons.** By the same argument any antisymmetric function is a linear combination of all $N$-electron determinants built from the complete set. Writing it relative to $|\Psi_0\rangle$,

$$
|\Phi\rangle = c_0|\Psi_0\rangle + \sum_{ar}c_a^r|\Psi_a^r\rangle + \sum_{a<b,\ r<s}c_{ab}^{rs}|\Psi_{ab}^{rs}\rangle + \sum_{a<b<c,\ r<s<t}c_{abc}^{rst}|\Psi_{abc}^{rst}\rangle + \cdots
$$

The restricted sums count each determinant once.

**In a finite basis.** The $\binom{2K}{N}$ determinants are an orthonormal basis for the $N$-electron space spanned by the $2K$ spin orbitals. Diagonalizing $\hat H$ in it is **full CI**. By the [[linear-variation-method]]:

- The lowest eigenvalue $\mathcal E_0$ is the exact ground-state energy within that one-electron basis.
- The higher eigenvalues bound the excited states from above.

The **(basis-set) correlation energy** is defined as

$$
E_{\text{corr}} = \mathcal E_0 - E_0 ,
$$

the difference between the full CI and Hartree-Fock energies in the same basis. As $K\to\infty$ (complete basis) full CI approaches the exact nonrelativistic Born-Oppenheimer energy.

The smallest worked case is the 2x2 full CI of [[minimal-basis-h2-model]]. Matrix elements between determinants are given by the [[slater-condon-rules]].

## Source

Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996; reprint of the revised first edition, McGraw-Hill, 1989), Sec. 2.2.6-2.2.7, pp. 58-64, Eqs. (2.54)-(2.78), Ex. 2.7.
