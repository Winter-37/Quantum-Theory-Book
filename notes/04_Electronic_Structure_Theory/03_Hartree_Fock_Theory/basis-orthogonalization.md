---
id: basis-orthogonalization
title: Orthogonalizing a non-orthogonal basis
summary: The overlap matrix is positive definite; symmetric (Löwdin) orthogonalization X = S^(-1/2) and canonical orthogonalization X = U s^(-1/2) turn FC = SCε into an ordinary eigenvalue problem F'C' = C'ε, and canonical orthogonalization handles near-linear dependence by dropping small eigenvalues of S.
status: in-progress
kind: derivation
level: intermediate
tags: [overlap-matrix, lowdin, symmetric-orthogonalization, canonical-orthogonalization, linear-dependence]
prerequisites: [rhf, functions-of-matrices]
related: [nonorthogonal-second-quantization, scf-procedure, population-analysis, change-of-basis]
order: 60
date: 2026-11-03
---

## Why orthogonalize

The Roothaan equations $\mathbf{FC} = \mathbf{SC}\boldsymbol\varepsilon$ ([[rhf]]) are a generalized eigenvalue problem because atom-centred basis functions overlap. Look for a transformation

$$
\phi'_\mu = \sum_\nu\phi_\nu X_{\nu\mu}
\qquad\text{with}\qquad
\mathbf X^\dagger\mathbf S\mathbf X = \mathbf 1 .
$$

In the new, orthonormal basis $\{\phi'_\mu\}$ the problem is an ordinary Hermitian eigenvalue problem.

## Transformed Roothaan equations

Substitute $\mathbf C = \mathbf X\mathbf C'$ into $\mathbf{FC} = \mathbf{SC}\boldsymbol\varepsilon$ and multiply by $\mathbf X^\dagger$:

$$
\underbrace{\mathbf X^\dagger\mathbf F\mathbf X}_{\mathbf F'}\mathbf C' = \underbrace{\mathbf X^\dagger\mathbf S\mathbf X}_{\mathbf 1}\mathbf C'\boldsymbol\varepsilon
\quad\Longrightarrow\quad
\mathbf F'\mathbf C' = \mathbf C'\boldsymbol\varepsilon .
$$

Diagonalize $\mathbf F'$ ([[matrix-eigenvalue-problem]]) and back-transform, $\mathbf C = \mathbf X\mathbf C'$. Szabo Ex. 3.16 checks that this reproduces the original equations.

## The overlap matrix is positive definite

Diagonalize $\mathbf S$: $\mathbf U^\dagger\mathbf{SU} = \mathbf s$. For eigenvector $\mathbf c^i$ (column $i$ of $\mathbf U$), Szabo Ex. 3.15 gives

$$
s_i = \sum_{\mu\nu}c_\mu^{i*}S_{\mu\nu}c_\nu^i = \int\mathrm d\mathbf r\ \Big|\sum_\mu c_\mu^i\phi_\mu(\mathbf r)\Big|^2 > 0 .
$$

It can only be zero if the basis functions are linearly dependent. So $\mathbf s^{-1/2}$ exists.

## Symmetric (Löwdin) orthogonalization

$$
\mathbf X = \mathbf S^{-1/2} = \mathbf U\mathbf s^{-1/2}\mathbf U^\dagger
\qquad
\big(\mathbf X^\dagger\mathbf{SX} = \mathbf S^{-1/2}\mathbf S\mathbf S^{-1/2} = \mathbf 1\big),
$$

computed as a function of a Hermitian matrix ([[functions-of-matrices]]).

**Properties.**

- Among all orthonormalizing transformations it keeps the new functions closest to the old ones in a least-squares sense. Each $\phi'_\mu$ still "belongs" to the atom of $\phi_\mu$. This is the basis of Löwdin population analysis ([[population-analysis]]).
- It keeps all $K$ functions.

## Canonical orthogonalization

$$
\mathbf X = \mathbf U\mathbf s^{-1/2},
\qquad
X_{\mu i} = U_{\mu i}/\sqrt{s_i}
\qquad
\big(\mathbf X^\dagger\mathbf{SX} = \mathbf s^{-1/2}\mathbf U^\dagger\mathbf{SU}\mathbf s^{-1/2} = \mathbf 1\big).
$$

Each new function is an eigenvector of $\mathbf S$ scaled by $1/\sqrt{s_i}$.

**Linear dependence.** In large or diffuse basis sets some $s_i$ become very small. The columns with $s_i\to0$ then have huge coefficients, and rounding errors explode. Canonical orthogonalization removes them by keeping only the columns with $s_i$ above a threshold (typically $10^{-6}$ to $10^{-8}$). This gives a rectangular $K\times m$ matrix $\mathbf X$ with $m<K$; the near-dependent combinations are dropped from the variational space. Symmetric orthogonalization cannot do this without losing its symmetric form.

!!! example "Two-function basis (minimal H₂, STO-3G, R = 1.4 bohr)"
    **Diagonalize S.** $\mathbf S = \begin{pmatrix}1&S\\S&1\end{pmatrix}$ with $S = 0.6593$. The eigenvalues are $1\pm S = 1.6593$ and $0.3407$, with eigenvectors $2^{-1/2}(1,\pm1)$.

    **Canonical orthogonalization.**
    $$
    \mathbf X_{\text{can}} = \begin{pmatrix}[2(1+S)]^{-1/2} & [2(1-S)]^{-1/2}\\ [2(1+S)]^{-1/2} & -[2(1-S)]^{-1/2}\end{pmatrix}.
    $$
    Its columns are already the symmetry-adapted MOs of [[minimal-basis-h2-model]].

    **Symmetric orthogonalization.**
    $$
    \mathbf X_{\text{sym}} = \tfrac12\begin{pmatrix}(1+S)^{-1/2}+(1-S)^{-1/2} & (1+S)^{-1/2}-(1-S)^{-1/2}\\ (1+S)^{-1/2}-(1-S)^{-1/2} & (1+S)^{-1/2}+(1-S)^{-1/2}\end{pmatrix}.
    $$
    Each orthonormal function remains centred mainly on its own atom.

    Szabo's numbers for HeH$^+$ ($S = 0.4508$) follow from the same formulas with $s_{1,2} = 1\pm S = 1.4508,\ 0.5492$.

## Source

Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996; reprint of the revised first edition, McGraw-Hill, 1989), Sec. 3.4.5, pp. 142-145, Eqs. (3.158)-(3.180), Ex. 3.15-3.16; Sec. 3.5.3, p. 170, Ex. 3.28.
