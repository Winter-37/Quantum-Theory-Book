---
id: infinite-square-well
title: The infinite square well
summary: Particle in a box of width a. Energies n²π²ħ²/2ma², sine eigenfunctions and their properties (parity, node counting, orthonormality, completeness), Fourier's trick for expansion coefficients, uncertainty products, two expansion examples (parabola and triangle, the latter showing the δ-function term in ⟨H⟩ for a kinked state), and the finite-difference matrix method with its convergence.
status: in-progress
kind: derivation
level: introductory
tags: [infinite-square-well, particle-in-a-box, orthonormality, completeness, fourier-series, finite-difference, griffiths]
prerequisites: [stationary-states]
related: [finite-square-well, harmonic-oscillator-ladder-operators, de-broglie-and-heisenberg-uncertainty, orthonormal-functions-and-operators, matrix-eigenvalue-problem]
also: []
date: 2026-11-04
---

## Solution

**Potential.** $V=0$ for $0\le x\le a$ and $V=\infty$ elsewhere.

**Outside the well** $\psi=0$.

**Inside the well** the TISE is

$$
\psi'' = -k^2\psi,\qquad k = \frac{\sqrt{2mE}}{\hbar},
$$

with general solution $\psi = A\sin kx + B\cos kx$. Using $E>0$ here is justified by the general result $E > V_{\min}$ in [[stationary-states]].

**Boundary conditions.** $\psi$ must be continuous at both walls. $\psi'$ need not be, because $V$ is infinite there (see [[delta-function-potential]] for why).

- $\psi(0)=0$ gives $B=0$.
- $\psi(a)=0$ with $A\neq0$ gives $\sin ka=0$, so $k_n = n\pi/a$ with $n = 1,2,3,\ldots$.

Here $n=0$ gives $\psi\equiv0$, and negative $n$ repeat the positive ones up to sign. Normalizing:

$$
E_n = \frac{\hbar^2k_n^2}{2m} = \frac{n^2\pi^2\hbar^2}{2ma^2},
\qquad
\psi_n(x) = \sqrt{\frac{2}{a}}\,\sin\frac{n\pi x}{a}\quad(0\le x\le a).
$$

The boundary condition at $x=a$ fixes $k$, and hence the energy, not the amplitude: quantization comes from requiring the solution to fit the box.

## Properties of the $\psi_n$

1. **Parity about the centre.** $\psi_1,\psi_3,\ldots$ are even about $x=a/2$; $\psi_2,\psi_4,\ldots$ are odd. This holds because $V$ is symmetric about the centre.
2. **Nodes.** $\psi_n$ has $n-1$ interior nodes. This is true for any one-dimensional potential (Griffiths Problem 2.45).
3. **Orthonormality.**

    $$
    \int_0^a\psi_m^*\psi_n\,dx = \delta_{mn}.
    $$

    For $m\neq n$, write $\sin\sin = \tfrac12[\cos(m-n)\theta - \cos(m+n)\theta]$. Both cosines integrate to sines of integer multiples of $\pi$, which vanish. The step fails for $m=n$, where normalization gives 1 instead.

4. **Completeness.** Any reasonable $f$ on $[0,a]$ can be expanded as $f = \sum_nc_n\psi_n$. This is the Fourier sine series, and Dirichlet's theorem guarantees convergence.

**Fourier's trick.** Multiply the expansion by $\psi_m^*$ and integrate. Orthonormality leaves one term:

$$
c_n = \int\psi_n^*(x)\,f(x)\,dx .
$$

The general solution is therefore $\Psi(x,t) = \sum_n c_n\sqrt{2/a}\,\sin(n\pi x/a)\,e^{-in^2\pi^2\hbar t/2ma^2}$.

## Uncertainty in the $n$th state (Griffiths Problem 2.4)

**Position.** $\langle x\rangle = a/2$ and

$$
\langle x^2\rangle = a^2\left(\frac13 - \frac{1}{2n^2\pi^2}\right).
$$

**Momentum.** $\langle p\rangle = 0$ and $\langle p^2\rangle = (n\pi\hbar/a)^2 = 2mE_n$.

**Product.**

$$
\sigma_x\sigma_p = \frac{\hbar}{2}\sqrt{\frac{n^2\pi^2}{3}-2}.
$$

| $n$ | 1 | 2 | 3 | 10 |
|---|---|---|---|---|
| $\sigma_x\sigma_p/\hbar$ | 0.5679 | 1.6703 | 2.6272 | 9.0414 |

The ground state comes closest to the bound $\hbar/2$.

## Worked examples

!!! example "Parabolic initial state (Griffiths Example 2.2)"
    $\Psi(x,0) = Ax(a-x)$ with $A = \sqrt{30/a^5}$.

    **Coefficients.** Fourier's trick gives

    $$
    c_n = \frac{4\sqrt{15}}{(n\pi)^3}\left[1-(-1)^n\right]
    = \begin{cases}8\sqrt{15}/(n\pi)^3, & n\text{ odd}\\ 0, & n\text{ even.}\end{cases}
    $$

    Even $n$ vanish by symmetry about $a/2$.

    | Check | Value |
    |---|---|
    | $\lvert c_1\rvert^2$ | $0.998555$ |
    | $\sum\lvert c_n\rvert^2 = (960/\pi^6)\sum_{\rm odd}n^{-6}$ | $1.000000000000$ (using $\sum_{\rm odd}n^{-6} = \pi^6/960$) |
    | $\langle H\rangle = (480\hbar^2/\pi^4ma^2)\sum_{\rm odd}n^{-4}$ | $5\,\hbar^2/ma^2$, versus $E_1 = 4.9348\,\hbar^2/ma^2$ |

    The state is 99.86% ground state, and the small excited admixture raises $\langle H\rangle$ slightly above $E_1$.

!!! example "Triangular initial state and the hidden $\delta$ (Griffiths Problems 2.7 and 2.39)"
    $\Psi(x,0) = Ax$ for $x\le a/2$ and $A(a-x)$ for $x\ge a/2$, with $A = \sqrt{12/a^3}$.

    **Coefficients.**

    $$
    c_n = \frac{4\sqrt6}{(n\pi)^2}\sin\frac{n\pi}{2},\qquad |c_1|^2 = \frac{96}{\pi^4} = 0.985534 .
    $$

    **Energy from the expansion.**

    $$
    \langle H\rangle = \sum_n|c_n|^2E_n = \frac{48\hbar^2}{\pi^2ma^2}\sum_{\rm odd}\frac1{n^2} = \frac{6\hbar^2}{ma^2}.
    $$

    Summing to $n=2\times10^6$ gives 5.999999. The tail falls only as $n^{-2}$, because the state has a kink.

    **Energy directly.** $-\tfrac{\hbar^2}{2m}\int\Psi^*\Psi''dx$ is zero on each linear piece. The whole answer comes from the $\delta$ in $\Psi''$ at the kink, where $\Psi'$ jumps by $-2A$:

    $$
    \langle H\rangle = -\frac{\hbar^2}{2m}\,\Psi(a/2)\,(-2A) = \frac{\hbar^2}{2m}\cdot\frac{Aa}{2}\cdot 2A = \frac{6\hbar^2}{ma^2}.
    $$

    The safe form $\frac{\hbar^2}{2m}\int|\Psi'|^2dx = \frac{\hbar^2}{2m}A^2a$ gives the same value.

!!! example "Finite-difference matrix (Griffiths Problem 2.61)"
    Slice $[0,a]$ into $N+1$ intervals, $\Delta x = a/(N+1)$, with $\psi_0 = \psi_{N+1} = 0$. The three-point second derivative turns the TISE into $\mathsf H\boldsymbol\psi = E\boldsymbol\psi$, where $\mathsf H$ is tridiagonal with diagonal $2\lambda + V_j$ and off-diagonal $-\lambda$, and $\lambda = \hbar^2/2m\Delta x^2$.

    The eigenvalues of this matrix are known in closed form, $E^{\rm FD}_n = (4\lambda)\sin^2[n\pi/2(N+1)]$, so the ratio to the exact $E_n$ is $(\sin\theta/\theta)^2$ with $\theta = n\pi/2(N+1)$:

    | $N$ | $E_1^{\rm FD}/E_1$ | $E_2^{\rm FD}/E_2$ | $E_5^{\rm FD}/E_5$ |
    |---|---|---|---|
    | 1 | 0.8106 | (no second state) | (no fifth state) |
    | 3 | 0.9496 | 0.8106 | (no fifth state) |
    | 10 | 0.9932 | 0.9731 | 0.8412 |
    | 100 | 0.99992 | 0.99968 | 0.99799 |

    The scheme always undershoots, and the error is $O(\Delta x^2)$ with a coefficient growing as $n^2$: high states need finer grids. The same tridiagonal matrix with $V_j\neq0$ is the workhorse used throughout these notes to check analytic spectra.

## Source

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Sec. 2.2, Eqs. (2.22)-(2.41), Example 2.2; Problems 2.4, 2.7, 2.39, 2.45, 2.61 (Eqs. 2.195-2.201). Page numbers are not given because the PDF used is an e-book rendering without print pagination. The closed form for $E^{\rm FD}_n$ is a standard result for the tridiagonal Toeplitz matrix, stated here and confirmed numerically, not taken from Griffiths. Numbers recomputed with `griffiths/ch02_tise.py` (section B).
