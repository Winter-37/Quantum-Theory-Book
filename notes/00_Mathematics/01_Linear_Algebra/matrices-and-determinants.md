---
id: matrices-and-determinants
title: Matrices and determinants
summary: Matrix multiplication, adjoint, trace, inverse, unitary and Hermitian matrices, and the permutation definition of the determinant with its properties. The determinant criterion for nontrivial solutions of Ac = 0.
status: in-progress
kind: reference
level: introductory
tags: [basics, linear-algebra, determinant, matrices]
prerequisites: []
related: [dirac-notation, slater-determinants, matrix-eigenvalue-problem]
order: 10
date: 2026-11-03
---

## Matrices

An $N\times M$ matrix $\mathbf A$ has elements $A_{ij}$, $i = 1..N$ (rows), $j = 1..M$ (columns), in general complex. If $\mathbf A$ is $N\times M$ and $\mathbf B$ is $M\times P$, then $\mathbf C = \mathbf{AB}$ is $N\times P$ with

$$
C_{ij} = \sum_{k=1}^{M} A_{ik}B_{kj}.
$$

A column matrix $\mathbf a$ has $M$ elements, and $\mathbf{Aa} = \mathbf b$ means $b_i = \sum_j A_{ij}a_j$.

**Adjoint.** $(\mathbf A^\dagger)_{ij} = A_{ji}^*$. For real matrices this is the transpose. The adjoint reverses products, $(\mathbf{AB})^\dagger = \mathbf B^\dagger\mathbf A^\dagger$, since $[(\mathbf{AB})^\dagger]_{ij} = \sum_k A_{jk}^*B_{ki}^* = \sum_k (\mathbf B^\dagger)_{ik}(\mathbf A^\dagger)_{kj}$. For columns, $\mathbf a^\dagger\mathbf b = \sum_i a_i^*b_i$ is the scalar product.

### Square matrices: definitions

| Name | Definition |
|---|---|
| diagonal | $A_{ij} = A_{ii}\delta_{ij}$ |
| trace | $\operatorname{tr}\mathbf A = \sum_i A_{ii}$ |
| unit matrix | $(\mathbf 1)_{ij} = \delta_{ij}$, $\mathbf{1A} = \mathbf{A1} = \mathbf A$ |
| inverse | $\mathbf A^{-1}\mathbf A = \mathbf A\mathbf A^{-1} = \mathbf 1$ |
| unitary | $\mathbf A^{-1} = \mathbf A^\dagger$ (real: orthogonal) |
| Hermitian | $\mathbf A^\dagger = \mathbf A$, i.e. $A_{ij} = A_{ji}^*$ (real: symmetric) |

### Useful identities (Szabo Ex. 1.4)

- $\operatorname{tr}(\mathbf{AB}) = \sum_{ik}A_{ik}B_{ki} = \operatorname{tr}(\mathbf{BA})$.
- $(\mathbf{AB})^{-1} = \mathbf B^{-1}\mathbf A^{-1}$.
- If $\mathbf U$ is unitary and $\mathbf B = \mathbf U^\dagger\mathbf{AU}$, then $\mathbf A = \mathbf{UBU}^\dagger$.
- If $\mathbf A$, $\mathbf B$ and $\mathbf C = \mathbf{AB}$ are all Hermitian, then $\mathbf{AB} = \mathbf C = \mathbf C^\dagger = \mathbf B\mathbf A$, so $\mathbf A$ and $\mathbf B$ commute.
- If $\mathbf A$ is Hermitian and invertible, $\mathbf A^{-1}$ is Hermitian: $(\mathbf A^{-1})^\dagger = (\mathbf A^\dagger)^{-1} = \mathbf A^{-1}$.
- For $2\times2$:
$$
\mathbf A^{-1} = \frac{1}{A_{11}A_{22}-A_{12}A_{21}}\begin{pmatrix}A_{22}&-A_{12}\\-A_{21}&A_{11}\end{pmatrix}.
$$

## Determinants

The determinant of an $N\times N$ matrix is the signed sum over all $N!$ permutations $\mathscr P$ of the column indices:

$$
\det\mathbf A = |\mathbf A| = \sum_{\mathscr P}(-1)^{p}\,A_{1 i_1}A_{2 i_2}\cdots A_{N i_N},
$$

where $(i_1,\dots,i_N)$ is the permuted order and $p$ is the number of transpositions needed to restore it to $1,2,\dots,N$ (only its parity matters). For $N=2$ the two permutations are $(1,2)$ with $p=0$ and $(2,1)$ with $p=1$:

$$
\begin{vmatrix}A_{11}&A_{12}\\A_{21}&A_{22}\end{vmatrix} = A_{11}A_{22}-A_{12}A_{21}.
$$

### Properties

1. A row or column of zeros gives $|\mathbf A| = 0$.
2. A diagonal matrix has $|\mathbf A| = \prod_i A_{ii}$.
3. Swapping two rows (or two columns) changes the sign.
4. $|\mathbf A| = (|\mathbf A^\dagger|)^*$.
5. $|\mathbf{AB}| = |\mathbf A|\,|\mathbf B|$.

From these:

6. Two equal rows (or columns) give $|\mathbf A| = 0$: swapping them changes the sign but not the matrix, so $|\mathbf A| = -|\mathbf A|$. This is the mathematical origin of the Pauli principle for [[slater-determinants]].
7. $|\mathbf A^{-1}| = 1/|\mathbf A|$, from property 5 with $\mathbf{AA}^{-1} = \mathbf 1$.
8. If $\mathbf{AA}^\dagger = \mathbf 1$, then $|\mathbf A|\,|\mathbf A|^* = 1$: a unitary matrix has $|\det| = 1$.
9. If $\mathbf U^\dagger\mathbf{OU} = \boldsymbol\Omega$ with $\mathbf U$ unitary, then $|\boldsymbol\Omega| = |\mathbf O|$.

**Linearity in one column.** If one column is a linear combination, the determinant splits:

$$
\Big|\ \cdots\ \sum_k c_k\mathbf b_k\ \cdots\ \Big| = \sum_k c_k\,\big|\ \cdots\ \mathbf b_k\ \cdots\ \big| ,
$$

with all other columns unchanged; the same holds for rows. This is used whenever a determinant of orbitals is expanded in a basis.

## When does $\mathbf{Ac} = 0$ have a nontrivial solution?

If $|\mathbf A| \ne 0$ then $\mathbf A^{-1}$ exists and $\mathbf c = \mathbf A^{-1}\mathbf 0 = \mathbf 0$. So a solution $\mathbf c \ne 0$ requires

$$
|\mathbf A| = 0 .
$$

Conversely, $|\mathbf A|=0$ means the columns are linearly dependent, which gives a nonzero $\mathbf c$. Applied to $\mathbf A = \mathbf O - \omega\mathbf 1$, this is the secular equation of the [[matrix-eigenvalue-problem]].

## Source

Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996; reprint of the revised first edition, McGraw-Hill, 1989), Sec. 1.1.2-1.1.3, pp. 5-9, Eqs. (1.20)-(1.40), Ex. 1.3-1.7.
