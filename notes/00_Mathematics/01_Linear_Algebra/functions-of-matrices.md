---
id: functions-of-matrices
title: Functions of Hermitian matrices
summary: Define f(A) by its power series; for Hermitian A, diagonalize, apply f to the eigenvalues, and transform back, f(A) = U f(a) U†. Square roots, inverses, determinant and trace from eigenvalues, and the resolvent (Green's function).
status: in-progress
kind: derivation
level: introductory
tags: [basics, linear-algebra, matrix-functions, resolvent, symmetric-orthogonalization]
prerequisites: [matrix-eigenvalue-problem]
related: [unitary-matrices-exponential-logarithm, change-of-basis, baker-campbell-hausdorff]
order: 50
date: 2026-11-03
---

## Definition

For a Hermitian matrix $\mathbf A$, a function $f(\mathbf A)$ is defined through the Taylor series of $f$:

$$
f(\mathbf A) = \sum_{n=0}^{\infty} c_n\mathbf A^n,
\qquad\text{e.g.}\quad
e^{\mathbf A} = \mathbf 1 + \mathbf A + \tfrac{1}{2!}\mathbf A^2 + \cdots
$$

The square root is the matrix $\mathbf A^{1/2}$ with $\mathbf A^{1/2}\mathbf A^{1/2} = \mathbf A$.

## Evaluation by diagonalization

For a diagonal matrix $\mathbf a = \operatorname{diag}(a_1,\dots,a_N)$, powers act element by element, so $f(\mathbf a) = \operatorname{diag}(f(a_1),\dots,f(a_N))$.

For a general Hermitian $\mathbf A$, diagonalize: $\mathbf U^\dagger\mathbf{AU} = \mathbf a$, i.e. $\mathbf A = \mathbf{UaU}^\dagger$ (see [[matrix-eigenvalue-problem]]). Because $\mathbf U^\dagger\mathbf U = \mathbf 1$, the inner factors cancel in powers:

$$
\mathbf A^n = \mathbf{UaU}^\dagger\,\mathbf{UaU}^\dagger\cdots = \mathbf U\mathbf a^n\mathbf U^\dagger ,
$$

so

$$
f(\mathbf A) = \mathbf U\Big(\sum_n c_n\mathbf a^n\Big)\mathbf U^\dagger = \mathbf U\,f(\mathbf a)\,\mathbf U^\dagger .
$$

The recipe: diagonalize, apply $f$ to each eigenvalue, transform back. Check for the square root: $\mathbf U\mathbf a^{1/2}\mathbf U^\dagger\,\mathbf U\mathbf a^{1/2}\mathbf U^\dagger = \mathbf{UaU}^\dagger = \mathbf A$.

If some $f(a_i)$ is infinite, $f(\mathbf A)$ does not exist. Example: $\mathbf A^{-1}$ fails when an eigenvalue is zero.

## Consequences (Szabo Ex. 1.12)

With $\mathbf A\mathbf c^\alpha = a_\alpha\mathbf c^\alpha$:

$$
\det(\mathbf A^n) = \prod_{\alpha} a_\alpha^n,
\qquad
\operatorname{tr}(\mathbf A^n) = \sum_\alpha a_\alpha^n .
$$

Both follow from the invariance of the determinant and trace under unitary transformations ([[change-of-basis]]) applied to $\mathbf A^n = \mathbf U\mathbf a^n\mathbf U^\dagger$. In particular $\det\mathbf A = 0$ exactly when an eigenvalue vanishes, which is when $\mathbf A^{-1}$ does not exist.

**Resolvent.** For $\mathbf G(\omega) = (\omega\mathbf 1 - \mathbf A)^{-1}$,

$$
G_{ij}(\omega) = \sum_\alpha\frac{U_{i\alpha}U_{j\alpha}^*}{\omega - a_\alpha}
= \sum_\alpha\frac{c_i^\alpha\,c_j^{\alpha*}}{\omega - a_\alpha}
= \sum_\alpha\frac{\langle i|\alpha\rangle\langle\alpha|j\rangle}{\omega - a_\alpha}.
$$

This gives the solution of $(\omega\mathbf 1 - \mathbf A)\mathbf x = \mathbf c$ for all $\omega$ after one diagonalization, $x_i = \sum_{j\alpha}U_{i\alpha}U_{j\alpha}^*c_j/(\omega - a_\alpha)$, instead of one matrix inversion per $\omega$. The poles of $\mathbf G$ sit at the eigenvalues; the same structure reappears in the one-particle Green's function.

!!! example "A symmetric 2x2 matrix with equal diagonal (Szabo Ex. 1.13)"
    $\mathbf A = \begin{pmatrix}a&b\\b&a\end{pmatrix}$ has eigenvalues $a\pm b$ with eigenvectors $2^{-1/2}(1,\pm1)^{\mathsf T}$. With $\mathbf U = 2^{-1/2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}$ (columns for $a+b$ and $a-b$),
    $$
    f(\mathbf A) = \tfrac12\begin{pmatrix}
    f(a+b)+f(a-b) & f(a+b)-f(a-b)\\
    f(a+b)-f(a-b) & f(a+b)+f(a-b)
    \end{pmatrix}.
    $$
    Numerical check with $a=3$, $b=1$ (eigenvalues 4 and 2):

    | $f$ | diagonal $\tfrac12[f(4)+f(2)]$ | off-diagonal $\tfrac12[f(4)-f(2)]$ |
    |---|---:|---:|
    | $\sqrt{x}$ | 1.707107 | 0.292893 |
    | $e^{x}$ | 30.993603 | 23.604547 |

    Both rows agree with `scipy.linalg.sqrtm` and `scipy.linalg.expm`.

!!! note "Where this is used"
    The most common use in electronic structure is $\mathbf S^{-1/2}$, the inverse square root of the basis-function overlap matrix, which gives symmetric (Löwdin) orthogonalization of the basis before solving the Roothaan equations. Matrix exponentials $e^{-\boldsymbol\kappa}$ of antisymmetric $\boldsymbol\kappa$ parametrize orbital rotations.

## Source

Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996; reprint of the revised first edition, McGraw-Hill, 1989), Sec. 1.1.7, pp. 21-24, Eqs. (1.108)-(1.115), Ex. 1.12-1.13.
