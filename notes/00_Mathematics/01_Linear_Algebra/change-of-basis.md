---
id: change-of-basis
title: Change of basis and unitary transformations
summary: Two orthonormal bases are related by a unitary matrix whose elements are their overlaps; operator matrices transform as Ω = U†OU. Trace and determinant are invariant.
status: in-progress
kind: derivation
level: introductory
tags: [basics, linear-algebra, unitary, basis-transformation]
prerequisites: [dirac-notation]
related: [matrix-eigenvalue-problem, orbital-rotations]
order: 30
date: 2026-11-03
---

## Setting

Take two complete orthonormal bases of the same $N$-dimensional space. Latin labels denote the first, Greek labels the second:

$$
\langle i|j\rangle = \delta_{ij},\quad \sum_i |i\rangle\langle i| = \mathbf 1,
\qquad
\langle\alpha|\beta\rangle = \delta_{\alpha\beta},\quad \sum_\alpha |\alpha\rangle\langle\alpha| = \mathbf 1 .
$$

## The transformation matrix is unitary

Expand each new vector in the old basis by inserting the identity:

$$
|\alpha\rangle = \sum_i |i\rangle\langle i|\alpha\rangle = \sum_i |i\rangle\,U_{i\alpha},
\qquad
U_{i\alpha} \equiv \langle i|\alpha\rangle .
$$

The inverse direction uses $\langle\alpha|i\rangle = \langle i|\alpha\rangle^* = U_{i\alpha}^* = (\mathbf U^\dagger)_{\alpha i}$:

$$
|i\rangle = \sum_\alpha |\alpha\rangle\,(\mathbf U^\dagger)_{\alpha i}.
$$

Beware the index order: $\langle\alpha|i\rangle$ is **not** $U_{\alpha i}$.

Orthonormality of the old basis gives

$$
\delta_{ij} = \langle i|j\rangle = \sum_\alpha \langle i|\alpha\rangle\langle\alpha|j\rangle = \sum_\alpha U_{i\alpha}(\mathbf U^\dagger)_{\alpha j} = (\mathbf{UU}^\dagger)_{ij},
$$

and the same argument starting from $\langle\alpha|\beta\rangle = \delta_{\alpha\beta}$ gives $\mathbf U^\dagger\mathbf U = \mathbf 1$. So **two orthonormal bases are related by a unitary matrix**, whose elements are the overlaps between them. For real bases $\mathbf U$ is orthogonal.

## How operator matrices transform

Let $O_{ij} = \langle i|\hat O|j\rangle$ and $\Omega_{\alpha\beta} = \langle\alpha|\hat O|\beta\rangle$. Inserting the identity twice:

$$
\Omega_{\alpha\beta} = \sum_{ij}\langle\alpha|i\rangle\langle i|\hat O|j\rangle\langle j|\beta\rangle = \sum_{ij}(\mathbf U^\dagger)_{\alpha i}\,O_{ij}\,U_{j\beta},
$$

$$
\boldsymbol\Omega = \mathbf U^\dagger\mathbf O\mathbf U,
\qquad
\mathbf O = \mathbf U\boldsymbol\Omega\mathbf U^\dagger .
$$

The point of this result: for a Hermitian $\hat O$ one can always choose the new basis so that $\boldsymbol\Omega$ is diagonal. Finding that $\mathbf U$ is the [[matrix-eigenvalue-problem]].

## Invariants

The trace is invariant, using cyclicity:

$$
\operatorname{tr}\boldsymbol\Omega = \operatorname{tr}(\mathbf U^\dagger\mathbf{OU}) = \operatorname{tr}(\mathbf{UU}^\dagger\mathbf O) = \operatorname{tr}\mathbf O .
$$

The determinant is invariant, using $|\mathbf{AB}| = |\mathbf A||\mathbf B|$ and $|\mathbf U^\dagger||\mathbf U| = |\mathbf U^\dagger\mathbf U| = 1$:

$$
|\boldsymbol\Omega| = |\mathbf U^\dagger|\,|\mathbf O|\,|\mathbf U| = |\mathbf O| .
$$

!!! note "Where this shows up"
    Rotating molecular orbitals among themselves is exactly this transformation. Because a determinant is invariant (up to a phase) under a unitary mixing of its occupied orbitals, the Hartree-Fock energy and density do not depend on which orthonormal set spans the occupied space. This is the freedom used to reach the canonical Hartree-Fock equations.

## Source

Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996; reprint of the revised first edition, McGraw-Hill, 1989), Sec. 1.1.5, pp. 13-14, Eqs. (1.62)-(1.71), Ex. 1.8.
