---
id: orthonormal-functions-and-operators
title: Complete orthonormal functions, the delta function, and operators
summary: Functions expanded in a complete orthonormal set behave like vectors with infinitely many components. Completeness gives the Dirac delta function; local and nonlocal operators; Hermitian operators on functions; and the reduction of an operator eigenvalue equation to a matrix eigenvalue problem.
status: in-progress
kind: theory
level: introductory
tags: [basics, function-space, dirac-delta, hermitian, completeness, basis-expansion]
prerequisites: [dirac-notation]
related: [matrix-eigenvalue-problem, linear-variation-method, variational-principle]
order: 80
date: 2026-11-03
---

## Functions as vectors

Let $\{\psi_i(x)\}_{i=1}^{\infty}$ be orthonormal on an interval (limits dropped below),

$$
\int \mathrm dx\ \psi_i^*(x)\,\psi_j(x) = \delta_{ij},
$$

and **complete**: any well-behaved $a(x)$ can be written

$$
a(x) = \sum_i \psi_i(x)\,a_i .
$$

Multiplying by $\psi_j^*(x)$ and integrating, orthonormality picks out the coefficient,

$$
a_j = \int\mathrm dx\ \psi_j^*(x)\,a(x).
$$

So a function is fixed by its components $\{a_i\}$, exactly as a vector is fixed by its components in a basis. Fourier series are the familiar example.

## The Dirac delta function

Insert the coefficient formula back into the expansion:

$$
a(x) = \int\mathrm dx'\ \Big[\sum_i \psi_i(x)\,\psi_i^*(x')\Big]\,a(x').
$$

The bracket reproduces any function under the integral, which defines the **Dirac delta function**:

$$
\sum_i \psi_i(x)\,\psi_i^*(x') = \delta(x - x'),
\qquad
a(x) = \int\mathrm dx'\ \delta(x-x')\,a(x').
$$

This is the continuous analogue of $a_i = \sum_j\delta_{ij}a_j$, and $\delta(x-x') = \delta(x'-x)$ like $\delta_{ij} = \delta_{ji}$. Setting $x=0$ and then $a\equiv1$:

$$
a(0) = \int\mathrm dx\ a(x)\,\delta(x),
\qquad
\int\mathrm dx\ \delta(x) = 1,
$$

for any interval containing $x=0$. A concrete representation is a box of unit area that shrinks to zero width:

$$
\delta(x) = \lim_{\varepsilon\to0}\delta_\varepsilon(x),
\qquad
\delta_\varepsilon(x) = \begin{cases}1/(2\varepsilon) & -\varepsilon<x<\varepsilon\\ 0 & \text{otherwise.}\end{cases}
$$

Check (Szabo Ex. 1.14): $\int a(x)\delta_\varepsilon(x)\,\mathrm dx = \frac{1}{2\varepsilon}\int_{-\varepsilon}^{\varepsilon}a(x)\,\mathrm dx$, the average of $a$ over $[-\varepsilon,\varepsilon]$. For continuous $a$ this tends to $a(0)$ as $\varepsilon\to0$ (mean value theorem).

## Bra-ket notation for functions

Define

$$
\psi_i(x) \leftrightarrow |i\rangle,\quad
a(x)\leftrightarrow|a\rangle,\quad
a^*(x)\leftrightarrow\langle a|,
\qquad
\langle a|b\rangle \equiv \int\mathrm dx\ a^*(x)\,b(x).
$$

Then orthonormality, components and expansion read $\langle i|j\rangle = \delta_{ij}$, $a_i = \langle i|a\rangle$, $|a\rangle = \sum_i|i\rangle\langle i|a\rangle$, identical to the finite-dimensional formulas in [[dirac-notation]]. Every finite-dimensional result whose proof only used these rules carries over.

## Operators on functions

An operator maps a function to a function, $\hat O a(x) = b(x)$, or $\hat O|a\rangle = |b\rangle$.

- **Nonlocal (integral) operator:** $b(x) = \int\mathrm dx'\ O(x,x')\,a(x')$. Finding $b$ at one point needs $a$ everywhere. The kernel $O(x,x')$ is a "continuous matrix", the analogue of $b_i = \sum_j O_{ij}a_j$. The Hartree-Fock exchange operator is of this type.
- **Local operator:** $b(x_0)$ depends only on $a$ in an infinitesimal neighbourhood of $x_0$. Multiplication by a potential $V(x)$ and $\mathrm d/\mathrm dx$ are local.

**Matrix elements and eigenfunctions.** Write

$$
\langle a|\hat O|b\rangle \equiv \int\mathrm dx\ a^*(x)\,\hat O\,b(x).
$$

If $\hat O\phi_\alpha = \omega_\alpha\phi_\alpha$ with $\langle\alpha|\alpha\rangle = 1$, then $\omega_\alpha = \langle\alpha|\hat O|\alpha\rangle$. "Multiplying by $\langle a|$" now means multiplying by $a^*(x)$ and integrating.

**Hermitian operators** satisfy

$$
\int\mathrm dx\ a^*(x)\,\hat O\,b(x) = \Big[\int\mathrm dx\ b^*(x)\,\hat O\,a(x)\Big]^* ,
\qquad
\langle a|\hat O|b\rangle = \langle b|\hat O|a\rangle^* .
$$

This is the same condition as for matrices, so the proofs in [[matrix-eigenvalue-problem]] apply unchanged: eigenvalues are real and eigenfunctions can be chosen orthonormal.

!!! warning "Hermiticity depends on the function space"
    For differential operators the condition holds only after integration by parts with boundary terms that vanish. For example $-\mathrm i\,\mathrm d/\mathrm dx$ is Hermitian on functions that vanish at the ends of the interval (or are periodic), not on arbitrary functions. This is why trial functions in the [[variational-principle]] must obey the same boundary conditions as the exact solutions.

## Operator eigenvalue problem becomes a matrix problem

**Matrix representation (Szabo Ex. 1.15).** Since $\hat O\psi_i$ is again a function, expand it:

$$
\hat O\psi_i(x) = \sum_j \psi_j(x)\,O_{ji},
\qquad
O_{ji} = \int\mathrm dx\ \psi_j^*(x)\,\hat O\,\psi_i(x) = \langle j|\hat O|i\rangle .
$$

In bra-ket form this is $\hat O|i\rangle = \sum_j|j\rangle\langle j|\hat O|i\rangle$, the identity inserted.

**Eigenvalue problem (Szabo Ex. 1.16).** Expand the unknown eigenfunction, $\phi(x) = \sum_i c_i\psi_i(x)$, insert into $\hat O\phi = \omega\phi$, multiply by $\psi_j^*$ and integrate:

$$
\sum_i O_{ji}\,c_i = \omega\,c_j
\quad\Longleftrightarrow\quad
\mathbf O\mathbf c = \omega\,\mathbf c .
$$

$\mathbf O$ is infinite. Truncating to the first $N$ basis functions gives an $N\times N$ problem whose eigenvalues approximate the true ones; the lowest is an upper bound to the exact lowest eigenvalue ([[linear-variation-method]]). This truncation is what every finite-basis electronic-structure calculation does.

## The full picture: position kets (Szabo Ex. 1.17)

Introduce a continuous orthonormal basis $|x\rangle$ with

$$
\int\mathrm dx\ |x\rangle\langle x| = \mathbf 1,
\qquad
\langle x|x'\rangle = \delta(x-x').
$$

Then a function is the component of an abstract ket along $|x\rangle$: $b(x) = \langle x|b\rangle$, $a^*(x) = \langle a|x\rangle$, and $\psi_i(x) = \langle x|i\rangle$. Each earlier formula is an identity insertion:

- $\langle a|b\rangle = \int\mathrm dx\,\langle a|x\rangle\langle x|b\rangle$ gives the integral scalar product.
- $\langle i|j\rangle = \int\mathrm dx\,\langle i|x\rangle\langle x|j\rangle = \int\psi_i^*\psi_j$ gives orthonormality.
- $\langle x|x'\rangle = \sum_i\langle x|i\rangle\langle i|x'\rangle = \sum_i\psi_i(x)\psi_i^*(x')$ gives completeness as a delta function.
- $\langle x'|\hat O|a\rangle = \int\mathrm dx\,\langle x'|\hat O|x\rangle\langle x|a\rangle$ with $O(x',x) = \langle x'|\hat O|x\rangle$ gives the integral-operator form.
- Inserting $\sum_i|i\rangle\langle i|$ on both sides: $O(x,x') = \sum_{ij}\psi_i(x)\,O_{ij}\,\psi_j^*(x')$.

## Source

Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996; reprint of the revised first edition, McGraw-Hill, 1989), Sec. 1.2, pp. 24-30, Eqs. (1.116)-(1.140), Ex. 1.14-1.17.
