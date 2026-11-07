---
id: generalized-statistical-interpretation
title: The generalized statistical interpretation; momentum-space wave functions
summary: The measurement postulate in general form. A measurement of Q returns an eigenvalue q_n with probability |⟨f_n|Ψ⟩|² (or |c(z)|²dz for a continuous spectrum), then collapses the state. Recovers the Born rule for position, defines the momentum-space wave function Φ(p,t) as the Fourier transform of Ψ, gives operators in momentum space (x → iħ∂/∂p), and works through the delta-well momentum distribution, a Lorentzian, and sequential measurements of incompatible observables.
status: in-progress
kind: theory
level: intermediate
tags: [measurement, born-rule, collapse, expansion-coefficients, momentum-space, fourier-transform, sequential-measurement, griffiths]
prerequisites: [eigenfunctions-of-hermitian-operators, wave-function-and-statistical-interpretation]
related: [generalized-uncertainty-principle, position-momentum-and-energy-representations, stationary-states, free-particle-and-wave-packets]
order: 30
date: 2026-11-04
---

## The postulate

A measurement of an observable $Q(x,p)$ on a particle in state $\Psi(x,t)$ always yields **one of the eigenvalues** of $\hat Q = Q(x,-i\hbar\,d/dx)$.

**Discrete spectrum.** With orthonormal eigenfunctions $f_n$ and eigenvalues $q_n$:

$$
P(q_n) = |c_n|^2,\qquad c_n = \langle f_n|\Psi\rangle .
$$

**Continuous spectrum.** With Dirac-orthonormal eigenfunctions $f_z$ and real eigenvalues $q(z)$:

$$
P(\text{result in } dz) = |c(z)|^2dz,\qquad c(z) = \langle f_z|\Psi\rangle .
$$

**After the measurement** the wave function collapses to the corresponding eigenstate. For a continuous spectrum it collapses to a narrow range set by the resolution of the apparatus.

**Wording.** Griffiths warns (footnote 18) against saying "$|c_n|^2$ is the probability that the particle is in $f_n$". The particle is in the state $\Psi$. $|c_n|^2$ is the probability that a measurement *returns* $q_n$, after which the particle *will be* in $f_n$.

## Consistency checks

**Expansion.** Completeness gives $\Psi = \sum_nc_n(t)f_n$, with $c_n(t) = \langle f_n|\Psi\rangle$ by Fourier's trick. The time dependence sits in the coefficients. For $\hat Q = \hat H$ with time-independent $V$ it is just the phase $e^{-iE_nt/\hbar}$ ([[stationary-states]]).

**Normalization.**

$$
1 = \langle\Psi|\Psi\rangle = \sum_{n,n'}c_{n'}^*c_n\langle f_{n'}|f_n\rangle = \sum_n|c_n|^2 .
$$

**Expectation value.**

$$
\langle Q\rangle = \langle\Psi|\hat Q\Psi\rangle = \sum_{n,n'}c_{n'}^*c_nq_n\delta_{n'n} = \sum_nq_n|c_n|^2,
$$

which is the probability-weighted average of the outcomes, as it should be.

**Position recovers Born.** With $g_y = \delta(x-y)$, $c(y) = \langle g_y|\Psi\rangle = \Psi(y,t)$. So $P(dy) = |\Psi(y,t)|^2dy$, the original rule.

## Momentum space

With $f_p = e^{ipx/\hbar}/\sqrt{2\pi\hbar}$, the coefficient function is the **momentum-space wave function**:

$$
\Phi(p,t) = \langle f_p|\Psi\rangle = \frac{1}{\sqrt{2\pi\hbar}}\int e^{-ipx/\hbar}\,\Psi(x,t)\,dx,
$$

$$
\Psi(x,t) = \frac{1}{\sqrt{2\pi\hbar}}\int e^{ipx/\hbar}\,\Phi(p,t)\,dp .
$$

$|\Phi(p,t)|^2dp$ is the probability that a momentum measurement gives a result in $dp$. Plancherel's theorem guarantees $\int|\Phi|^2dp = \int|\Psi|^2dx$.

**Operators in momentum space.** Since $x\,e^{-ipx/\hbar} = i\hbar\,\partial_p e^{-ipx/\hbar}$:

$$
\langle Q(x,p,t)\rangle =
\begin{cases}
\displaystyle\int\Psi^*\,\hat Q\!\left(x,-i\hbar\tfrac{\partial}{\partial x},t\right)\Psi\,dx & \text{(position space)}\\[2ex]
\displaystyle\int\Phi^*\,\hat Q\!\left(i\hbar\tfrac{\partial}{\partial p},p,t\right)\Phi\,dp & \text{(momentum space).}
\end{cases}
$$

In particular $\langle x\rangle = \int\Phi^*(i\hbar\,\partial_p)\Phi\,dp$ (Problem 3.13).

**Numerical check.** For a Gaussian with $\langle x\rangle = 1.3$ and $\langle p\rangle = 0.7$, FFT to $\Phi$ followed by $i\hbar\,\partial_p$ gives $\langle x\rangle = 1.29987$, matching the position-space value 1.30000 to the accuracy of the finite-difference derivative.

**Free particle** (Problem 3.12). $\Phi(p,t) = \phi(p/\hbar)\,e^{-ip^2t/2m\hbar}/\sqrt\hbar$, so $|\Phi(p,t)|^2$ is time independent: momentum is conserved. This is why the Gaussian packet in [[free-particle-and-wave-packets]] spreads in $x$ with constant $\sigma_p$.

## Worked examples

!!! example "Momentum distribution of the delta-well bound state (Griffiths Example 3.4)"
    **State.** $\psi = (\sqrt{m\alpha}/\hbar)\,e^{-m\alpha|x|/\hbar^2}$. With $p_0 \equiv m\alpha/\hbar$:

    $$
    \Phi(p,t) = \sqrt{\frac{2}{\pi}}\,\frac{p_0^{3/2}}{p^2+p_0^2}\,e^{-iEt/\hbar}.
    $$

    This is a Lorentzian, the Fourier transform of a two-sided exponential.

    **Probability of a large momentum.**

    $$
    P(p>p_0) = \frac{2}{\pi}p_0^3\int_{p_0}^\infty\frac{dp}{(p^2+p_0^2)^2} = \frac14 - \frac{1}{2\pi} = 0.090845 .
    $$

    **FFT check** ($p_0=1$, $2^{16}$ points on a 400-wide box). $\int|\Phi|^2 = 1.000012$, and $|\Phi_{\rm FFT}|$ agrees with the Lorentzian to $4.4\times10^{-6}$. Summing the grid density for $p>1$ gives 0.0913; the difference from 0.0908 is the grid's $\Delta p = 0.016$ resolution at the edge of the interval.

!!! example "Lorentzian in position (Griffiths Problem 3.36)"
    **State.** $\Psi(x,0) = A/(x^2+a^2)$.

    **Position.** $A = \sqrt{2a^3/\pi}$, $\langle x\rangle = 0$, $\langle x^2\rangle = a^2$, so $\sigma_x = a$.

    **Momentum.**

    $$
    \Phi(p,0) = \sqrt{\frac{a}{\hbar}}\,e^{-a|p|/\hbar},
    $$

    which is normalized. $\langle p\rangle = 0$ and $\langle p^2\rangle = \hbar^2/2a^2$, so

    $$
    \sigma_x\sigma_p = \frac{\hbar}{\sqrt2}.
    $$

    This mirrors the cusp state $e^{-\lambda|x|}$, with the roles of $x$ and $p$ swapped ([[de-broglie-and-heisenberg-uncertainty]]).

    The FFT reproduces $e^{-|p|}$ to $3\times10^{-3}$; the error is truncation of the slow $1/x^2$ tail on the finite box.

!!! example "Oscillator ground state in momentum space (Griffiths Problem 3.11)"
    $\Phi_0(p) = (\pi m\omega\hbar)^{-1/4}\,e^{-p^2/2m\omega\hbar}$: a Gaussian again, with the roles of $x$ and $p$ swapped up to scale. The classical momentum range at $E_0$ is $|p|\le\sqrt{m\hbar\omega}$, so

    $$
    P(\text{outside}) = \operatorname{erfc}(1) = 0.1573,
    $$

    the same as the position result in [[harmonic-oscillator-analytic-solution]].

!!! example "Sequential measurements of incompatible observables (Griffiths Problem 3.33)"
    **Setup.** $\hat A$ has eigenstates $\psi_{1,2}$ (eigenvalues $a_{1,2}$), and $\hat B$ has eigenstates $\phi_{1,2}$, with

    $$
    \psi_1 = (3\phi_1+4\phi_2)/5,\qquad \psi_2 = (4\phi_1-3\phi_2)/5 .
    $$

    **Sequence.**

    1. Measure $A$ and get $a_1$: the state is $\psi_1$.
    2. Measure $B$: $b_1$ with probability $9/25$ (state $\phi_1$), or $b_2$ with probability $16/25$ (state $\phi_2$).
    3. Measure $A$ again. Inverting, $\phi_1 = (3\psi_1+4\psi_2)/5$ and $\phi_2 = (4\psi_1-3\psi_2)/5$, so

    $$
    P(a_1) = \frac{9}{25}\cdot\frac{9}{25} + \frac{16}{25}\cdot\frac{16}{25} = \frac{337}{625} = 0.5392 .
    $$

    The intervening $B$ measurement destroyed the certainty about $A$. Had the outcome of $B$ been reported, the answer would be $9/25$ or $16/25$.

## Source

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Sec. 3.4, Eqs. (3.43)-(3.58), Example 3.4; Problems 3.11-3.13, 3.33, 3.36; footnotes 15-18. Page numbers are not given because the PDF used is an e-book rendering without print pagination. Problem answers are worked here, not quoted; Example 3.4's 0.0908 is the book's and is reproduced exactly. Numbers from `griffiths/ch03_formalism.py` (section B).
