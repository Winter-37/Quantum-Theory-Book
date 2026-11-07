---
id: unitary-matrices-exponential-logarithm
title: Exponential parametrization of unitary matrices, special unitary and orthogonal matrices, metric-preserving transformations, and the matrix logarithm
summary: Every unitary matrix is exp(X) for some anti-Hermitian X, every such exponential is unitary, and the elements of X are unconstrained, which makes it the natural parametrization for orbital optimization. Removing the diagonal phases gives special unitary matrices (det = 1); real antisymmetric X gives special orthogonal ones, computable in real arithmetic from the eigenvectors of X². Transformations preserving a metric S are exp(XS), with S-commutator BCH expansions. The matrix logarithm inverts the exponential only near the identity. All relations checked numerically.
status: in-progress
kind: theory
level: intermediate
tags: [matrix-exponential, unitary-matrix, orthogonal-matrix, matrix-logarithm, anti-hermitian, exponential-parametrization, metric]
prerequisites: [functions-of-matrices, matrices-and-determinants, baker-campbell-hausdorff]
related: [orbital-rotations, nonorthogonal-second-quantization, change-of-basis, scf-second-order-and-stability, mcscf-second-order-optimization]
order: 70
date: 2026-11-04
---

## What a good parametrization of unitary matrices needs

Optimizing orbitals means searching over unitary matrices $\mathbf U^\dagger\mathbf U = \mathbf 1$. A parametrization should (i) generate every unitary matrix, (ii) generate only unitary matrices, and (iii) use independent parameters. The elements of $\mathbf U$ fail (iii): they are coupled by $\mathbf U^\dagger\mathbf U = \mathbf 1$. The exponential satisfies all three.

## Matrix exponentials

**Definition and rules.** $\exp\mathbf A = \sum_{n\ge0}\mathbf A^n/n!$ converges for every finite matrix ([[functions-of-matrices]]). It satisfies:

- $\exp(\mathbf A)^\dagger = \exp(\mathbf A^\dagger)$;
- $\mathbf B\exp(\mathbf A)\mathbf B^{-1} = \exp(\mathbf B\mathbf A\mathbf B^{-1})$;
- $\exp(\mathbf A + \mathbf B) = \exp\mathbf A\exp\mathbf B$ **only if** $[\mathbf A,\mathbf B] = 0$;
- $\exp(-\mathbf A)\exp(\mathbf A) = \mathbf 1$;
- $\det\exp\mathbf A = \exp\operatorname{Tr}\mathbf A$;
- $\exp(-\mathbf A)\mathbf B\exp(\mathbf A) = \mathbf B + [\mathbf B,\mathbf A] + \tfrac12[[\mathbf B,\mathbf A],\mathbf A] + \cdots$ ([[baker-campbell-hausdorff]]).

## Unitary matrices as exponentials

**Every unitary matrix is an exponential.** By the spectral theorem $\mathbf U = \mathbf V\boldsymbol\epsilon\mathbf V^\dagger$ with $\mathbf V$ unitary and $\epsilon_k = e^{i\delta_k}$ ($\delta_k$ real). Then $\mathbf U = \exp(i\mathbf V\boldsymbol\delta\mathbf V^\dagger) = \exp\mathbf X$ with $\mathbf X = i\mathbf V\boldsymbol\delta\mathbf V^\dagger$ anti-Hermitian.

**Every such exponential is unitary.** If $\mathbf X^\dagger = -\mathbf X$, then $\exp(\mathbf X)^\dagger\exp(\mathbf X) = \exp(-\mathbf X)\exp(\mathbf X) = \mathbf 1$.

**Independent parameters.** The elements on and below the diagonal of $\mathbf X$ are free. Diagonal elements are imaginary, off-diagonal elements complex: $n^2$ real parameters for $n\times n$.

**Special unitary.** Split $\mathbf X = i{}^{\mathrm D}\mathbf X + {}^{\mathrm R}\mathbf X + i{}^{\mathrm I}\mathbf X$, with real diagonal ${}^{\mathrm D}\mathbf X$, real antisymmetric ${}^{\mathrm R}\mathbf X$ and real symmetric ${}^{\mathrm I}\mathbf X$ with zero diagonal. Without the diagonal part, $\operatorname{Tr}\mathbf X = 0$ and $\det\exp\mathbf X = 1$. Any unitary matrix is a diagonal phase matrix times a special unitary one, $\mathbf U = \exp(i{}^{\mathrm D}\tilde{\mathbf X})\exp({}^{\mathrm R}\tilde{\mathbf X} + i{}^{\mathrm I}\tilde{\mathbf X})$. The phases are usually redundant in electronic-structure work.

**Orthogonal.** A real orthogonal matrix is $\mathbf Q = \mathbf d\exp({}^{\mathrm R}\mathbf X)$ with $\mathbf d$ diagonal with entries $\pm1$. Dropping $\mathbf d$ gives the **special orthogonal** matrices $\mathbf R = \exp({}^{\mathrm R}\mathbf X)$, $n(n-1)/2$ parameters, used for real orbital rotations ([[orbital-rotations]]).

## Evaluating the exponential

- **Series.** Converges quickly when $\lVert\mathbf X\rVert$ is small.
- **Diagonalization.** $\mathbf X = i\mathbf V\boldsymbol\delta\mathbf V^\dagger\Rightarrow\exp\mathbf X = \mathbf V\exp(i\boldsymbol\delta)\mathbf V^\dagger$. For a real antisymmetric matrix this needs complex arithmetic.
- **Real arithmetic for real antisymmetric $\mathbf K$ (HJO Eq. 3.1.31).** $\mathbf K^2$ is real symmetric with nonpositive eigenvalues, $\mathbf K^2 = -\mathbf W\boldsymbol\tau^2\mathbf W^{\mathsf T}$. Splitting the series into even and odd powers,

$$
\exp\mathbf K = \mathbf W\cos(\boldsymbol\tau)\mathbf W^{\mathsf T} + \mathbf W\boldsymbol\tau^{-1}\sin(\boldsymbol\tau)\mathbf W^{\mathsf T}\mathbf K,
$$

  with $\tau^{-1}\sin\tau\to1$ for zero eigenvalues (always present when $n$ is odd). Eigenvalues of $\mathbf K^2$ come in degenerate pairs (one pair per $2\times2$ rotation plane).
- **2×2.** $\exp\begin{pmatrix}0&-t\\t&0\end{pmatrix} = \begin{pmatrix}\cos t&-\sin t\\ \sin t&\cos t\end{pmatrix}$.

## Transformations that preserve a metric

**Parametrization.** For nonorthogonal bases one needs $\mathbf W$ with $\mathbf W^\dagger\mathbf S\mathbf W = \mathbf S$ for a Hermitian positive definite metric $\mathbf S$. Any such $\mathbf W$ is $\mathbf S^{-1/2}\mathbf U\mathbf S^{1/2}$ with $\mathbf U$ unitary. Writing $\mathbf U = \exp(\mathbf S^{1/2}\mathbf X\mathbf S^{1/2})$ with $\mathbf X$ anti-Hermitian gives

$$
\mathbf W = \exp(\mathbf X\mathbf S),\qquad \exp(-\mathbf S\mathbf X)\,\mathbf S\exp(\mathbf X\mathbf S) = \mathbf S .
$$

**Asymmetric BCH.** With S-commutators $[\mathbf A,\mathbf B]_{\mathrm S} = \mathbf A\mathbf S\mathbf B - \mathbf B\mathbf S\mathbf A$,

$$
\exp(-\mathbf X\mathbf S)\,\mathbf A\exp(\mathbf S\mathbf X) = \mathbf A + [\mathbf A,\mathbf X]_{\mathrm S} + \tfrac12[[\mathbf A,\mathbf X]_{\mathrm S},\mathbf X]_{\mathrm S} + \cdots,
$$

an ordinary BCH series with $\mathbf S$ inserted between adjacent factors (HJO Eq. 3.1.47).

## The matrix logarithm

**Definition.** For diagonalizable nonsingular $\mathbf A = \mathbf Z\boldsymbol\alpha\mathbf Z^{-1}$, $\log\mathbf A = \mathbf Z\log(\boldsymbol\alpha)\mathbf Z^{-1}$, with the principal branch $-\pi<\arg z\le\pi$ of the scalar logarithm.

**Inverse only near the identity.** The exponential maps all matrices whose eigenvalues differ by multiples of $2\pi i$ onto the same matrix, so it has no global inverse. $\log$ inverts $\exp$ for $\mathbf X$ whose eigenvalues have imaginary parts in $(-\pi, \pi]$. For anti-Hermitian $\mathbf X$, this means rotation angles $|\delta_k|<\pi$.

**Series and properties.**

$$
\log(\mathbf 1 + \mathbf S) = -\sum_{n\ge1}\frac{(-1)^n}{n}\mathbf S^n\quad(\text{eigenvalues of }\mathbf S\text{ inside the unit circle}),
$$

$$
(\log\mathbf A)^\dagger = \log\mathbf A^\dagger,\qquad \log\mathbf A^n = n\log\mathbf A,\qquad \log\mathbf A\mathbf B = \log\mathbf A + \log\mathbf B\ \text{ if }[\log\mathbf A,\log\mathbf B] = 0,\qquad (\log\mathbf U)^\dagger = -\log\mathbf U\ \text{for unitary }\mathbf U .
$$

The logarithm maps unitary matrices to anti-Hermitian ones. This is how one recovers $\boldsymbol\kappa$ from a given orbital transformation, for example to restart an optimization from known orbitals.

!!! example "Numerical checks, random 5×5 matrices (computed for this note)"
    | Relation | Deviation |
    |---|---:|
    | $\exp(\mathbf X)$ unitary for anti-Hermitian $\mathbf X$ | $3\times10^{-16}$ |
    | $\det\exp\mathbf X = \exp\operatorname{Tr}\mathbf X$ | $4\times10^{-16}$ |
    | $\mathbf V\exp(i\boldsymbol\delta)\mathbf V^\dagger = \exp\mathbf X$ | $8\times10^{-16}$ |
    | $\det\exp(\mathbf X - \operatorname{diag}\mathbf X)$ | $1.000000 + 0.000000i$ |
    | Real-arithmetic formula vs `scipy.linalg.expm` | $5\times10^{-15}$ |
    | $\log(\mathbf 1 + \mathbf S)$ series vs `logm`, spectral radius 0.56 | $9\times10^{-16}$ |
    | $\mathbf W = \exp(\mathbf X\mathbf S)$: $\mathbf W^\dagger\mathbf S\mathbf W - \mathbf S$ | $3\times10^{-14}$ |
    | $\mathbf W = \mathbf S^{-1/2}\exp(\mathbf S^{1/2}\mathbf X\mathbf S^{1/2})\mathbf S^{1/2}$ | $3\times10^{-14}$ |
    | Asymmetric BCH, 25 terms | $5\times10^{-11}$ |

    **Branch problem.**

    - For $\mathbf X$ with largest rotation angle 1.00, $\log\exp\mathbf X$ returns $\mathbf X$ to $10^{-15}$.
    - Scaled to largest angle 9.96, $\log\exp\mathbf X$ differs from $\mathbf X$ by 4.2. It is still anti-Hermitian, and its exponential is still the same $\mathbf U$ to $10^{-15}$: a different, equally valid generator.

## Source

Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, Chichester, 2000), Sec. 3.1, pp. 80-86, Eqs. (3.1.1)-(3.1.50); Sec. 3.4, pp. 93-95, Eqs. (3.4.1)-(3.4.16); Exercises 3.1-3.3. Equations taken from the page images. Numerical checks computed for this note (NumPy, SciPy).
