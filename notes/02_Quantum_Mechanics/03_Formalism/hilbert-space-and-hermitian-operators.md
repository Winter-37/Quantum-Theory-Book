---
id: hilbert-space-and-hermitian-operators
title: Hilbert space, observables and Hermitian operators
summary: Wave functions live in L², the space of square-integrable functions with inner product ⟨f|g⟩ = ∫f*g. Observables are represented by Hermitian operators, because expectation values must be real. Covers the Hermitian conjugate, the momentum operator's hermiticity and why d/dx alone fails, determinate states as eigenstates (σ_Q = 0), the ring operator i d/dφ with integer spectrum, and the domain/self-adjointness caveat.
status: in-progress
kind: theory
level: intermediate
tags: [hilbert-space, inner-product, schwarz-inequality, hermitian-operator, adjoint, observable, determinate-state, self-adjoint, griffiths]
prerequisites: [momentum-operator-and-ehrenfest-theorem, stationary-states]
related: [eigenfunctions-of-hermitian-operators, generalized-statistical-interpretation, dirac-notation, orthonormal-functions-and-operators]
order: 10
date: 2026-11-04
---

## Hilbert space

**Finite-dimensional picture.** In $N$ dimensions a vector is a column of components $a_n$ in an orthonormal basis, the inner product is $\langle\alpha|\beta\rangle = \sum_na_n^*b_n$, and linear maps are matrices ([[dirac-notation]]). Quantum states are mostly *functions*, which need infinitely many components. Infinite sums and integrals may diverge, so finite-dimensional arguments need care.

**The space.** Normalizability selects the **square-integrable** functions on an interval $(a,b)$:

$$
L^2(a,b) = \left\{f:\ \int_a^b|f(x)|^2dx < \infty\right\}.
$$

This set is a vector space, physicists' **Hilbert space**, and wave functions live in it.

**Inner product.**

$$
\langle f|g\rangle = \int_a^b f(x)^*g(x)\,dx .
$$

**Schwarz inequality.**

$$
\left|\int f^*g\,dx\right| \le \sqrt{\int|f|^2dx\int|g|^2dx}.
$$

This guarantees that the inner product of two members exists, and is the inequality behind the uncertainty principle ([[generalized-uncertainty-principle]]).

**Properties of the inner product.**

- $\langle g|f\rangle = \langle f|g\rangle^*$.
- $\langle f|f\rangle\ge0$, with zero only for $f=0$, or more precisely for $f$ zero almost everywhere.
- Orthonormality: $\langle f_m|f_n\rangle = \delta_{mn}$.
- A set $\{f_n\}$ is **complete** if every $f$ can be written $f = \sum_nc_nf_n$. For an orthonormal set, Fourier's trick then gives $c_n = \langle f_n|f\rangle$.

Two different "completenesses" are in play. A *space* is complete if Cauchy sequences converge inside it (Griffiths footnote 3). A *set of functions* is complete if it spans the space.

**Membership is not automatic.** For example (Griffiths Problem 3.2), $x^\nu\in L^2(0,1)$ iff $\nu>-\tfrac12$. With $\nu=\tfrac12$, both $f=\sqrt x$ and $xf$ belong ($\int|f|^2=\tfrac12$, $\int|xf|^2=\tfrac14$), but $f' = \tfrac12x^{-1/2}$ does not, since $\int|f'|^2$ diverges. Operators can map a vector out of the space, which is why their domains matter (see the last section).

## Observables are Hermitian operators

**Reality condition.** Measurements return real numbers, so expectation values must be real for every state:

$$
\langle Q\rangle = \langle\Psi|\hat Q\Psi\rangle = \langle Q\rangle^* = \langle\hat Q\Psi|\Psi\rangle .
$$

**Definition.** An operator satisfying $\langle f|\hat Qf\rangle = \langle\hat Qf|f\rangle$ for all $f$ is **Hermitian**. The apparently stronger condition

$$
\langle f|\hat Qg\rangle = \langle\hat Qf|g\rangle\quad\text{for all } f,g
$$

is equivalent (Griffiths Problem 3.3: apply the diagonal condition with $h=f+g$ and $h=f+ig$).

**Hermitian conjugate.** $\hat Q^\dagger$ is defined by $\langle f|\hat Qg\rangle = \langle\hat Q^\dagger f|g\rangle$, so a Hermitian operator satisfies $\hat Q=\hat Q^\dagger$. Useful rules (Griffiths Problem 3.5):

$$
(\hat Q\hat R)^\dagger = \hat R^\dagger\hat Q^\dagger,\qquad
(\hat Q+\hat R)^\dagger = \hat Q^\dagger+\hat R^\dagger,\qquad
(c\hat Q)^\dagger = c^*\hat Q^\dagger,\qquad
x^\dagger = x,\quad (d/dx)^\dagger = -d/dx .
$$

**Momentum is Hermitian.** Integrate by parts:

$$
\langle f|\hat pg\rangle = \int f^*(-i\hbar g')\,dx = -i\hbar f^*g\Big|_{-\infty}^{\infty} + \int(-i\hbar f')^*g\,dx = \langle\hat pf|g\rangle .
$$

The boundary term vanishes for $L^2$ functions on the whole line. The factor $i$ is essential. The derivative $d/dx$ alone is **anti-Hermitian**, $(d/dx)^\dagger = -d/dx$, and its expectation values are imaginary.

**Discrete version.** The central-difference matrix $\mathsf D$ on a periodic grid is antisymmetric, $\mathsf D^{\rm T} = -\mathsf D$, so $-i\mathsf D$ is a Hermitian matrix. This is why discretized momentum operators keep a real spectrum.

**Algebra of Hermitian operators** (Griffiths Problem 3.4).

- Sums of Hermitian operators are Hermitian.
- $\alpha\hat Q$ is Hermitian iff $\alpha$ is real.
- A product $\hat Q\hat R$ is Hermitian iff $[\hat Q,\hat R]=0$.
- $x$ and $\hat H = -\tfrac{\hbar^2}{2m}\tfrac{d^2}{dx^2}+V$ are Hermitian.
- The commutator of two Hermitian operators is anti-Hermitian, so $-i[\hat A,\hat B]$ is Hermitian (Problem 3.32).

## Determinate states

**Question.** Can a state give the *same* result $q$ in every measurement of $Q$? Then $\sigma_Q=0$, and using hermiticity of $\hat Q-q$:

$$
\sigma_Q^2 = \langle\Psi|(\hat Q-q)^2\Psi\rangle = \langle(\hat Q-q)\Psi|(\hat Q-q)\Psi\rangle = 0
\quad\Longrightarrow\quad \hat Q\Psi = q\Psi .
$$

**Answer.** Determinate states of $Q$ are eigenfunctions of $\hat Q$, and the measured value is the eigenvalue. Stationary states are the determinate states of energy: the TISE is the eigenvalue equation of $\hat H$.

**Vocabulary.**

- The **spectrum** is the set of eigenvalues.
- An eigenvalue is **degenerate** if two or more independent eigenfunctions share it.
- $\Psi=0$ is excluded as an eigenfunction, because otherwise every number would be an eigenvalue.

## Worked example

!!! example "Operators on a ring (Griffiths Example 3.1 and Problem 3.6)"
    Functions of the azimuthal angle $\phi$ obey $f(\phi+2\pi) = f(\phi)$, as for a bead on a ring.

    **$\hat Q = i\,d/d\phi$ is Hermitian.** Integrating by parts, the boundary term $if^*g\big|_0^{2\pi}$ vanishes by periodicity.

    **Its eigenfunctions** are $e^{-iq\phi}$, and periodicity forces $e^{-2\pi iq}=1$, so

    $$
    q = 0,\pm1,\pm2,\ldots
    $$

    The spectrum is the integers, and it is nondegenerate.

    **$d^2/d\phi^2$ is also Hermitian**, now with two integrations by parts. Its eigenvalues are $-n^2$ ($n=0,1,2,\ldots$). $n=0$ is single, and every $n\ge1$ is doubly degenerate ($e^{\pm in\phi}$).

    **Numerical check.** A 64-point spectral differentiation matrix on $[0,2\pi)$ is Hermitian, with eigenvalues

    - for $i\,d/d\phi$: $\ldots,-2,-1,0,1,2,3,4,\ldots$ to $10^{-10}$;
    - for $d^2/d\phi^2$: $0,-1,-1,-4,-4,-9,-9,\ldots$

## Domains and self-adjointness

"Hermitian" as defined above concerns only how an operator *acts*. An operator is also defined by its **domain**, the functions it may act on; it must not map them out of $L^2$. Representing an observable requires $\hat Q$ and $\hat Q^\dagger$ to have the same action *and* the same domain. Such an operator is **self-adjoint**.

**Example: momentum on a finite interval** (Griffiths Problem 3.48).

- With domain $f(0)=f(a)=0$, $\hat p$ is Hermitian, but $\hat p^\dagger$ accepts any $g$, so $\hat p$ is not self-adjoint.
- Enlarging the domain to $f(a) = \lambda f(0)$ makes $\hat p$ self-adjoint for every $|\lambda|=1$.

There is therefore a whole family of inequivalent momentum operators on an interval. Griffiths avoids the issue elsewhere by working on the infinite line: the infinite well's states are best thought of as functions on $(-\infty,\infty)$ that vanish outside $(0,a)$ (his footnote 9). Physicists usually say "Hermitian" when they mean self-adjoint (footnote 46).

## Source

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Secs. 3.1-3.2, Eqs. (3.1)-(3.29), Example 3.1; Problems 3.1-3.6, 3.32, 3.48; footnotes 2-9, 45-48. Page numbers are not given because the PDF used is an e-book rendering without print pagination. Equations were read from the page images. Numerical checks in `griffiths/ch03_formalism.py` (section A).
