---
id: dirac-notation
title: Dirac notation for finite vector spaces
summary: Kets, bras, scalar products, completeness, and matrix representations of linear operators in an N-dimensional complex vector space, built up from ordinary 3D vector algebra. Adjoints and Hermitian operators.
status: in-progress
kind: theory
level: introductory
tags: [basics, linear-algebra, dirac-notation, bra-ket, operators]
prerequisites: []
related: [matrices-and-determinants, change-of-basis, orthonormal-functions-and-operators]
order: 20
date: 2026-11-03
---

## From 3D vectors to kets

In three dimensions a vector is a linear combination of orthonormal unit vectors $\hat e_i$:

$$
\vec a = \sum_{i=1}^{3}\hat e_i\,a_i ,
\qquad
\hat e_i\cdot\hat e_j = \delta_{ij}.
$$

Dotting with $\hat e_j$ picks out a component, $a_j = \hat e_j\cdot\vec a$. Then $\vec a = \sum_i \hat e_i(\hat e_i\cdot\vec a)$, so the **unit dyadic** $\mathbf 1 = \sum_i \hat e_i\hat e_i$ leaves every vector unchanged. This is the completeness relation of the basis. Dirac notation is the same structure in $N$ complex dimensions.

## Kets, bras and the scalar product

Let $\{|i\rangle\}_{i=1}^N$ be a complete basis of **kets**. Any ket is

$$
|a\rangle = \sum_{i=1}^N |i\rangle\,a_i ,
\qquad
\mathbf a = (a_1,\dots,a_N)^{\mathsf T},
$$

where the column $\mathbf a$ is the **representation** of $|a\rangle$ in this basis. The **bra** $\langle a|$ is represented by the row $\mathbf a^\dagger = (a_1^*,\dots,a_N^*)$, and the scalar product is the matrix product

$$
\langle a|b\rangle = \mathbf a^\dagger\mathbf b = \sum_i a_i^* b_i ,
\qquad
\langle a|a\rangle = \sum_i |a_i|^2 \ge 0 .
$$

Writing $\langle a| = \sum_i a_i^*\langle i|$ and demanding agreement with this definition forces

$$
\langle i|j\rangle = \delta_{ij},
$$

so the basis must be orthonormal. Two consequences used constantly:

$$
a_j = \langle j|a\rangle,
\qquad
\langle a|b\rangle = \langle b|a\rangle^* .
$$

## Completeness: inserting the identity

Substituting $a_i = \langle i|a\rangle$ into the expansion gives $|a\rangle = \sum_i |i\rangle\langle i|a\rangle$ for every $|a\rangle$, hence

$$
\mathbf 1 = \sum_{i=1}^N |i\rangle\langle i| .
$$

Most manipulations in quantum chemistry are "insert $\mathbf 1$ and regroup". For example $\langle a|b\rangle = \sum_i\langle a|i\rangle\langle i|b\rangle$ reproduces the component formula.

## Operators and their matrices

A linear operator $\hat O$ maps kets to kets, $\hat O|a\rangle = |b\rangle$, and satisfies $\hat O(x|a\rangle + y|b\rangle) = x\hat O|a\rangle + y\hat O|b\rangle$. It is fixed by its action on the basis:

$$
\hat O|i\rangle = \sum_j |j\rangle\,O_{ji},
\qquad
O_{ji} = \langle j|\hat O|i\rangle .
$$

Note the index order: column $i$ of $\mathbf O$ holds the components of $\hat O|i\rangle$. The same result follows by inserting the identity, $\hat O|i\rangle = \sum_j|j\rangle\langle j|\hat O|i\rangle$. In components, $\hat O|a\rangle = |b\rangle$ becomes $b_j = \sum_i O_{ji}a_i$, i.e. $\mathbf b = \mathbf O\mathbf a$.

**Products.** For $\hat C = \hat A\hat B$,

$$
C_{ij} = \langle i|\hat A\,\mathbf 1\,\hat B|j\rangle = \sum_k \langle i|\hat A|k\rangle\langle k|\hat B|j\rangle = \sum_k A_{ik}B_{kj},
$$

so the representation of a product is the product of representations. In general $\hat A\hat B \ne \hat B\hat A$. The commutator and anticommutator are

$$
[\hat A,\hat B] = \hat A\hat B - \hat B\hat A,
\qquad
\{\hat A,\hat B\} = \hat A\hat B + \hat B\hat A .
$$

## Adjoint and Hermitian operators

If $\hat O|a\rangle = |b\rangle$, the **adjoint** $\hat O^\dagger$ is defined by the corresponding bra equation $\langle a|\hat O^\dagger = \langle b|$. Taking scalar products with an arbitrary $|c\rangle$:

$$
\langle a|\hat O^\dagger|c\rangle = \langle b|c\rangle = \langle c|b\rangle^* = \langle c|\hat O|a\rangle^* .
$$

So in any orthonormal basis $(O^\dagger)_{ij} = O_{ji}^*$: the matrix of the adjoint is the conjugate transpose. An operator is **Hermitian** if $\hat O^\dagger = \hat O$, equivalently

$$
\langle a|\hat O|b\rangle = \langle b|\hat O|a\rangle^* \quad\text{for all } a,b .
$$

Its eigenvalues are real and its eigenvectors can be chosen orthonormal (see [[matrix-eigenvalue-problem]]).

!!! example "Commutator and anticommutator of two symmetric matrices (Szabo Ex. 1.2)"
    $$
    \mathbf A = \begin{pmatrix}1&1&0\\1&2&2\\0&2&-1\end{pmatrix},
    \qquad
    \mathbf B = \begin{pmatrix}1&-1&1\\-1&0&0\\1&0&1\end{pmatrix}.
    $$
    Multiplying out,
    $$
    [\mathbf A,\mathbf B] = \begin{pmatrix}0&-2&4\\2&0&3\\-4&-3&0\end{pmatrix},
    \qquad
    \{\mathbf A,\mathbf B\} = \begin{pmatrix}0&0&-2\\0&-2&3\\-2&3&-2\end{pmatrix}.
    $$
    Check: for real symmetric $\mathbf A,\mathbf B$, $(\mathbf{AB})^{\mathsf T} = \mathbf{BA}$, so the commutator must be antisymmetric and the anticommutator symmetric. Both are. Since $[\mathbf A,\mathbf B]\ne 0$, the product $\mathbf{AB}$ is not symmetric (compare Szabo Ex. 1.4d). Numbers checked with NumPy.

## Source

Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996; reprint of the revised first edition, McGraw-Hill, 1989), Sec. 1.1.1 and 1.1.4, pp. 2-12, Eqs. (1.1)-(1.61), Ex. 1.1-1.2.
