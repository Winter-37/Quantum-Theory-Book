---
id: matrix-eigenvalue-problem
title: The Hermitian matrix eigenvalue problem
summary: Hermitian operators have real eigenvalues and orthonormal eigenvectors. Diagonalizing a Hermitian matrix is finding the unitary U with U†OU diagonal, whose columns are the eigenvectors. Secular determinant and the closed-form 2x2 Jacobi rotation, with worked examples.
status: in-progress
kind: derivation
level: introductory
tags: [basics, linear-algebra, eigenvalues, diagonalization, jacobi, secular-equation]
prerequisites: [dirac-notation, change-of-basis]
related: [matrices-and-determinants, functions-of-matrices, linear-variation-method]
order: 40
date: 2026-11-03
---

## Statement

A ket $|\alpha\rangle$ is an eigenvector of $\hat O$ with eigenvalue $\omega_\alpha$ if

$$
\hat O|\alpha\rangle = \omega_\alpha|\alpha\rangle,
\qquad \langle\alpha|\alpha\rangle = 1 .
$$

Throughout, $\hat O$ is **Hermitian**, $\langle a|\hat O|b\rangle = \langle b|\hat O|a\rangle^*$.

## Properties of Hermitian operators

**1. Eigenvalues are real.** Set $a=b=\alpha$ in the Hermiticity condition: $\langle\alpha|\hat O|\alpha\rangle = \langle\alpha|\hat O|\alpha\rangle^*$. The left side is $\omega_\alpha$, the right side $\omega_\alpha^*$, so $\omega_\alpha = \omega_\alpha^*$.

**2. Eigenvectors with different eigenvalues are orthogonal.** The adjoint of $\hat O|\beta\rangle = \omega_\beta|\beta\rangle$ is $\langle\beta|\hat O = \omega_\beta\langle\beta|$ (using $\hat O^\dagger=\hat O$, $\omega_\beta$ real). Close the first equation (for $\alpha$) with $\langle\beta|$ and the second with $|\alpha\rangle$, and subtract:

$$
(\omega_\alpha - \omega_\beta)\langle\beta|\alpha\rangle = 0 .
$$

So $\langle\beta|\alpha\rangle = 0$ whenever $\omega_\alpha\ne\omega_\beta$.

**3. Degenerate eigenvectors can be made orthogonal.** If $\hat O|1\rangle = \omega|1\rangle$ and $\hat O|2\rangle = \omega|2\rangle$, any combination $x|1\rangle + y|2\rangle$ has the same eigenvalue. Let both be normalized with real overlap $S = \langle1|2\rangle \ne 0$ ($0<|S|<1$). **Schmidt orthogonalization:** keep $|\mathrm I\rangle = |1\rangle$ and take $|\mathrm{II}'\rangle = |1\rangle + c|2\rangle$ with $c = -1/S$ so that $\langle\mathrm I|\mathrm{II}'\rangle = 1 + cS = 0$. Normalizing,

$$
|\mathrm{II}\rangle = (S^{-2}-1)^{-1/2}\left(|1\rangle - S^{-1}|2\rangle\right).
$$

Check: $\langle\mathrm{II}'|\mathrm{II}'\rangle = 1 + 2cS + c^2 = 1 - 2 + S^{-2} = S^{-2}-1$. The book takes $S$ real. For complex $S$ the general Gram-Schmidt step is $|\mathrm{II}\rangle \propto |2\rangle - |1\rangle\langle1|2\rangle$, normalized by $(1-|S|^2)^{-1/2}$; for real $S$ it is the same vector as above up to sign.

Hence the eigenvectors of a Hermitian operator form an orthonormal set, $\langle\alpha|\beta\rangle = \delta_{\alpha\beta}$, and in that basis the operator is diagonal, $\langle\beta|\hat O|\alpha\rangle = \omega_\alpha\delta_{\alpha\beta}$.

## Diagonalization as a unitary transformation

Given $O_{ij} = \langle i|\hat O|j\rangle$ in an orthonormal basis, we want the orthonormal basis $\{|\alpha\rangle\}$ in which $\hat O$ is diagonal. By [[change-of-basis]] the two matrices are related by $\boldsymbol\Omega = \mathbf U^\dagger\mathbf{OU}$, so the task is to find unitary $\mathbf U$ with

$$
\mathbf U^\dagger\mathbf O\mathbf U = \boldsymbol\omega = \operatorname{diag}(\omega_1,\dots,\omega_N).
$$

An $N\times N$ Hermitian matrix therefore has $N$ eigenvalues (counted with degeneracy).

**Column picture.** Write the problem as $\mathbf O\mathbf c^\alpha = \omega_\alpha\mathbf c^\alpha$, with normalized, mutually orthogonal $\mathbf c^\alpha$: $\sum_i (c_i^\alpha)^*c_i^\beta = \delta_{\alpha\beta}$. Put the eigenvectors in the columns of $\mathbf U$, $U_{i\alpha} = c_i^\alpha$. Then the $N$ eigenvalue equations are one matrix equation, and orthonormality is unitarity:

$$
\mathbf{OU} = \mathbf U\boldsymbol\omega,
\qquad
\mathbf U^\dagger\mathbf U = \mathbf 1
\;\Longrightarrow\;
\mathbf U^\dagger\mathbf{OU} = \boldsymbol\omega .
$$

Column $\alpha$ of $\mathbf{OU} = \mathbf U\boldsymbol\omega$ reads $\sum_j O_{ij}U_{j\alpha} = U_{i\alpha}\omega_\alpha$, which is exactly $\mathbf O\mathbf c^\alpha = \omega_\alpha\mathbf c^\alpha$ (Szabo Ex. 1.9).

## The secular determinant

$(\mathbf O - \omega\mathbf 1)\mathbf c = 0$ has a nonzero solution only if (see [[matrices-and-determinants]])

$$
|\mathbf O - \omega\mathbf 1| = 0 ,
$$

a polynomial of degree $N$ in $\omega$ whose roots are the eigenvalues. Each eigenvector then follows from the linear equations, up to a factor fixed by normalization. This route is useful by hand for $N=2$ or $3$; numerical codes never use it (see "Computational note").

## The 2x2 real symmetric case

Let $O_{12} = O_{21}$ (real).

### Via the secular equation

$$
\begin{vmatrix}O_{11}-\omega & O_{12}\\ O_{12} & O_{22}-\omega\end{vmatrix}
= \omega^2 - (O_{11}+O_{22})\,\omega + O_{11}O_{22} - O_{12}^2 = 0,
$$

$$
\omega_{\mp} = \tfrac12\left[O_{11}+O_{22} \mp \sqrt{(O_{22}-O_{11})^2 + 4O_{12}^2}\right].
$$

Special case $O_{11}=O_{22}=a$, $O_{12}=b$: $\omega = a\mp b$ (with $b>0$ the lower is $a-b$), with eigenvectors

$$
\omega = a-b:\ \ \mathbf c = 2^{-1/2}(1,-1)^{\mathsf T},
\qquad
\omega = a+b:\ \ \mathbf c = 2^{-1/2}(1,1)^{\mathsf T}.
$$

(The eigenvector equation for $a+b$ gives $ac_1 + bc_2 = (a+b)c_1$, so $c_1 = c_2$.)

**Without determinants (Szabo Ex. 1.10).** Set $\mathbf c = (1, c)^{\mathsf T}$. The two equations are $O_{11} + O_{12}c = \omega$ and $O_{21} + O_{22}c = \omega c$. Eliminating $c = (\omega - O_{11})/O_{12}$ from the second gives back the same quadratic. This trick is used later in the book to get the lowest root of a matrix by iteration without forming a determinant.

### Via a rotation (Jacobi)

A real $2\times2$ orthogonal matrix has one free parameter. Take

$$
\mathbf U = \begin{pmatrix}\cos\theta & \sin\theta\\ \sin\theta & -\cos\theta\end{pmatrix},
\qquad \mathbf U^{\mathsf T}\mathbf U = \mathbf 1 \text{ for all } \theta .
$$

Then

$$
\mathbf U^{\mathsf T}\mathbf{OU} =
\begin{pmatrix}
O_{11}\cos^2\theta + O_{22}\sin^2\theta + O_{12}\sin2\theta &
\tfrac12(O_{11}-O_{22})\sin2\theta - O_{12}\cos2\theta\\
\tfrac12(O_{11}-O_{22})\sin2\theta - O_{12}\cos2\theta &
O_{11}\sin^2\theta + O_{22}\cos^2\theta - O_{12}\sin2\theta
\end{pmatrix}.
$$

The off-diagonal element vanishes for

$$
\theta_0 = \tfrac12\tan^{-1}\frac{2O_{12}}{O_{11}-O_{22}},
$$

and the eigenpairs are

$$
\omega_1 = O_{11}\cos^2\theta_0 + O_{22}\sin^2\theta_0 + O_{12}\sin2\theta_0,
\quad
\mathbf c^1 = \begin{pmatrix}\cos\theta_0\\ \sin\theta_0\end{pmatrix},
$$

$$
\omega_2 = O_{11}\sin^2\theta_0 + O_{22}\cos^2\theta_0 - O_{12}\sin2\theta_0,
\quad
\mathbf c^2 = \begin{pmatrix}\sin\theta_0\\ -\cos\theta_0\end{pmatrix}.
$$

!!! warning "Which root is the lower one"
    With $\theta_0$ taken from the principal branch $|\theta_0|\le\pi/4$, $\omega_1$ is the eigenvalue "connected" to $O_{11}$: it is the **larger** root when $O_{11}>O_{22}$ and the smaller one when $O_{11}<O_{22}$. Label the roots by value afterwards, not by subscript. If $O_{11} = O_{22}$ use $\theta_0 = \pm\pi/4$ (sign of $O_{12}$).

The **Jacobi method** for $N\times N$ matrices repeats such $2\times2$ rotations on the largest off-diagonal element until the matrix is diagonal to working precision.

!!! example "Two 2x2 matrices (Szabo Ex. 1.11)"
    **$\mathbf A = \begin{pmatrix}3&1\\1&3\end{pmatrix}$.** Equal diagonal, so $\omega = 3\mp1$:
    $$
    \omega = 2:\ 2^{-1/2}(1,-1)^{\mathsf T}, \qquad \omega = 4:\ 2^{-1/2}(1,1)^{\mathsf T}.
    $$
    In the rotation route $O_{11}-O_{22} = 0$, so $\theta_0 = \pi/4$ and $\omega_1 = \tfrac32 + \tfrac32 + 1 = 4$, $\omega_2 = 2$.

    **$\mathbf B = \begin{pmatrix}3&1\\1&2\end{pmatrix}$.** Secular route:
    $$
    \omega^2 - 5\omega + 5 = 0
    \;\Rightarrow\;
    \omega = \frac{5\mp\sqrt5}{2} = 1.381966,\ 3.618034 .
    $$
    Rotation route: $\tan2\theta_0 = 2/(3-2) = 2$, so $\theta_0 = \tfrac12\tan^{-1}2 = 0.553574$ rad $= 31.7175^\circ$. Since $O_{11}>O_{22}$, $\omega_1 = 3.618034$ with $\mathbf c^1 = (0.850651, 0.525731)^{\mathsf T}$, and $\omega_2 = 1.381966$ with $\mathbf c^2 = (0.525731, -0.850651)^{\mathsf T}$. Check: $\omega_1+\omega_2 = 5 = \operatorname{tr}\mathbf B$ and $\omega_1\omega_2 = 5 = |\mathbf B|$. All values checked with `numpy.linalg.eigh`.

## Computational note

Expanding the characteristic polynomial is numerically unstable and costs far more than needed. Library routines (LAPACK `dsyevd`/`zheevd`, called by `numpy.linalg.eigh` and `scipy.linalg.eigh`) reduce the matrix to tridiagonal form by orthogonal transformations and then diagonalize it, at $O(N^3)$ cost. For very large sparse matrices (CI), one uses iterative methods such as Davidson that only need matrix-vector products.

```python
import numpy as np
B = np.array([[3., 1.], [1., 2.]])
w, U = np.linalg.eigh(B)          # ascending eigenvalues, eigenvectors in columns
print(w)                          # [1.38196601 3.61803399]
print(np.allclose(U.T @ B @ U, np.diag(w)))   # True
```

## Source

Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996; reprint of the revised first edition, McGraw-Hill, 1989), Sec. 1.1.6, pp. 15-21, Eqs. (1.72)-(1.107), Ex. 1.9-1.11.
