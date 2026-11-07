---
id: slater-determinants
title: Hartree products and Slater determinants
summary: Products of spin orbitals solve independent-electron problems but distinguish electrons; antisymmetrizing gives the Slater determinant. Normalization, overlap of determinants, the short-hand ket notation, and how antisymmetry correlates same-spin electrons (Fermi hole) but not opposite-spin ones.
status: in-progress
kind: theory
level: introductory
tags: [basics, slater-determinant, hartree-product, antisymmetry, fermi-hole, exchange]
prerequisites: [spin-orbitals-and-antisymmetry]
related: [matrices-and-determinants, slater-condon-rules, minimal-basis-h2-model, excited-determinants, creation-and-annihilation-operators]
order: 30
date: 2026-11-03
---

## Hartree products

Suppose the Hamiltonian is a sum of one-electron operators,

$$
\hat{\mathcal H} = \sum_{i=1}^{N} h(i),
$$

either because the electron repulsion is ignored, or because $h$ is an effective operator that includes it on average (as in Hartree-Fock). Let the eigenfunctions of $h$ be spin orbitals: $h\,\chi_j = \varepsilon_j\chi_j$. Then the **Hartree product**

$$
\Psi^{\text{HP}}(\mathbf x_1,\dots,\mathbf x_N) = \chi_i(\mathbf x_1)\,\chi_j(\mathbf x_2)\cdots\chi_k(\mathbf x_N)
$$

is an eigenfunction of $\hat{\mathcal H}$ with eigenvalue

$$
E = \varepsilon_i + \varepsilon_j + \cdots + \varepsilon_k .
$$

The proof (Szabo Ex. 2.2): $h(1)$ acts only on $\chi_i(\mathbf x_1)$ and returns $\varepsilon_i$ times the same product, and similarly for every term in the sum.

**It is uncorrelated.** $|\Psi^{\text{HP}}|^2\,\mathrm d\mathbf x_1\cdots\mathrm d\mathbf x_N$ factorizes into $|\chi_i(\mathbf x_1)|^2\mathrm d\mathbf x_1\cdots|\chi_k(\mathbf x_N)|^2\mathrm d\mathbf x_N$. The probability of finding electron 1 somewhere does not depend on where electron 2 is.

**It violates antisymmetry.** It labels electron 1 as being in $\chi_i$, electron 2 in $\chi_j$, and so on, so the electrons are distinguishable.

## Two-electron determinant

Put electrons 1, 2 in $\chi_i$, $\chi_j$, or the other way round, and take the antisymmetric combination:

$$
\Psi(\mathbf x_1,\mathbf x_2) = 2^{-1/2}\big[\chi_i(\mathbf x_1)\chi_j(\mathbf x_2) - \chi_j(\mathbf x_1)\chi_i(\mathbf x_2)\big]
= 2^{-1/2}\begin{vmatrix}\chi_i(\mathbf x_1) & \chi_j(\mathbf x_1)\\ \chi_i(\mathbf x_2) & \chi_j(\mathbf x_2)\end{vmatrix}.
$$

Its properties:

- It satisfies $\Psi(\mathbf x_1,\mathbf x_2) = -\Psi(\mathbf x_2,\mathbf x_1)$.
- It vanishes if $i=j$: no two electrons in one spin orbital.
- **Normalization (Szabo Ex. 2.3).** Expanding $\langle\Psi|\Psi\rangle$ gives $\tfrac12[\langle\chi_i|\chi_i\rangle\langle\chi_j|\chi_j\rangle - 2\,\mathrm{Re}\,\langle\chi_i|\chi_j\rangle\langle\chi_j|\chi_i\rangle + \langle\chi_j|\chi_j\rangle\langle\chi_i|\chi_i\rangle] = \tfrac12[1 - 0 + 1] = 1$ for orthonormal $\chi_i\ne\chi_j$.
- **Still an eigenfunction (Szabo Ex. 2.4).** For $\hat{\mathcal H} = h(1) + h(2)$, each of the two Hartree products has eigenvalue $\varepsilon_i+\varepsilon_j$, so their difference has the same eigenvalue.

## N-electron Slater determinant

$$
\Psi(\mathbf x_1,\dots,\mathbf x_N) = (N!)^{-1/2}
\begin{vmatrix}
\chi_i(\mathbf x_1) & \chi_j(\mathbf x_1) & \cdots & \chi_k(\mathbf x_1)\\
\chi_i(\mathbf x_2) & \chi_j(\mathbf x_2) & \cdots & \chi_k(\mathbf x_2)\\
\vdots & \vdots & & \vdots\\
\chi_i(\mathbf x_N) & \chi_j(\mathbf x_N) & \cdots & \chi_k(\mathbf x_N)
\end{vmatrix}.
$$

**Rows are electrons, columns are spin orbitals.** The properties of [[matrices-and-determinants]] then give the physics:

- Exchanging two electrons swaps two rows, which changes the sign: antisymmetry.
- Two electrons in one spin orbital means two equal columns, which makes the determinant zero: exclusion.
- $(N!)^{-1/2}$ normalizes it: the $N!$ terms are mutually orthogonal products, each with norm 1.

**Short-hand.** Only the diagonal is written, with electrons in the order $1,\dots,N$:

$$
|\chi_i\chi_j\cdots\chi_k\rangle \equiv |ij\cdots k\rangle .
$$

The normalization constant is included. Swapping two **columns** (orbital labels) changes the sign:

$$
|\cdots\chi_m\cdots\chi_n\cdots\rangle = -\,|\cdots\chi_n\cdots\chi_m\cdots\rangle .
$$

Up to sign, a determinant is fixed by **which** spin orbitals are occupied. Determinants built from orthonormal spin orbitals are normalized, and two determinants that differ in at least one occupied spin orbital are orthogonal.

!!! example "Overlap of two determinants (Szabo Ex. 2.5)"
    Let $|K\rangle = |\chi_i\chi_j\rangle$ and $|L\rangle = |\chi_k\chi_l\rangle$ with all orbitals from one orthonormal set. Expanding both,
    $$
    \langle K|L\rangle = \tfrac12\big[2\,\delta_{ik}\delta_{jl} - 2\,\delta_{il}\delta_{jk}\big] = \delta_{ik}\delta_{jl} - \delta_{il}\delta_{jk}.
    $$
    The overlap is $+1$ if $k=i$, $l=j$ (the same determinant), and $-1$ if $k=j$, $l=i$ (columns swapped, $|L\rangle = -|K\rangle$). It is $0$ otherwise.

## Exchange correlation and the Fermi hole

Antisymmetrizing changes the pair probability. Consider $|\chi_1\chi_2\rangle$ with two different spatial orbitals $\psi_1,\psi_2$. Let $P(\mathbf r_1,\mathbf r_2)\,\mathrm d\mathbf r_1\mathrm d\mathbf r_2$ be the probability of electron 1 in $\mathrm d\mathbf r_1$ and electron 2 in $\mathrm d\mathbf r_2$, obtained by integrating $|\Psi|^2$ over both spins.

**Opposite spins**, $\chi_1 = \psi_1\alpha$, $\chi_2 = \psi_2\beta$. The cross terms vanish on spin integration ($\langle\alpha|\beta\rangle = 0$):

$$
P(\mathbf r_1,\mathbf r_2) = \tfrac12\Big[|\psi_1(\mathbf r_1)|^2|\psi_2(\mathbf r_2)|^2 + |\psi_1(\mathbf r_2)|^2|\psi_2(\mathbf r_1)|^2\Big].
$$

This is just the average of the two "who is where" assignments, which is uncorrelated. With $\psi_1 = \psi_2$ it becomes $|\psi_1(\mathbf r_1)|^2|\psi_1(\mathbf r_2)|^2$. In particular $P(\mathbf r,\mathbf r)\ne0$: opposite-spin electrons can be found at the same point.

**Parallel spins**, $\chi_1 = \psi_1\beta$, $\chi_2 = \psi_2\beta$. Now the cross terms survive:

$$
P(\mathbf r_1,\mathbf r_2) = \tfrac12\Big[|\psi_1(\mathbf r_1)|^2|\psi_2(\mathbf r_2)|^2 + |\psi_1(\mathbf r_2)|^2|\psi_2(\mathbf r_1)|^2
- \big(\psi_1^*(\mathbf r_1)\psi_2(\mathbf r_1)\psi_2^*(\mathbf r_2)\psi_1(\mathbf r_2) + \text{c.c.}\big)\Big].
$$

At $\mathbf r_1 = \mathbf r_2 = \mathbf r$ the bracket is $2|\psi_1|^2|\psi_2|^2 - 2|\psi_1|^2|\psi_2|^2 = 0$. Two same-spin electrons are never at the same point, so each is surrounded by a **Fermi hole**.

A single determinant therefore includes **exchange correlation** (same spin) but no correlation of opposite-spin electrons. This is why it is called an "uncorrelated" wave function, and why the correlation energy is defined relative to it.

## Single determinant as an approximation

The simplest antisymmetric trial function for an $N$-electron ground state is one determinant, $|\Psi_0\rangle = |\chi_1\chi_2\cdots\chi_N\rangle$. The [[variational-principle]] picks the best one by minimizing $E_0 = \langle\Psi_0|\hat H|\Psi_0\rangle$ over the spin orbitals. This is the Hartree-Fock approximation, whose orbitals satisfy the eigenvalue equation $f(i)\chi(\mathbf x_i) = \varepsilon\chi(\mathbf x_i)$ with the Fock operator $f$ (derived in Szabo Ch. 3). Diagonalizing $f$ in a basis of $K$ spatial functions gives $2K$ spin orbitals. The $N$ lowest are **occupied** (labels $a,b,c,\dots$) and the remaining $2K-N$ are **virtual** (labels $r,s,t,\dots$). See [[excited-determinants]].

## Source

Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996; reprint of the revised first edition, McGraw-Hill, 1989), Sec. 2.2.2-2.2.4, pp. 47-55, Eqs. (2.28)-(2.53), Ex. 2.2-2.5.
