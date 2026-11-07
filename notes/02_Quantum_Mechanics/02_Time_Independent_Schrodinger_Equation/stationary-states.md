---
id: stationary-states
title: Stationary states and separation of variables
summary: Separating the time-dependent Schrödinger equation for a time-independent potential gives the time-independent equation Hψ = Eψ and the phase e^{−iEt/ħ}. Stationary states have time-independent densities and sharp energy; the general solution is a superposition whose coefficients give energy probabilities |c_n|². Includes the general theorems (E real, ψ real, parity, E > V_min) and a two-state beat worked numerically.
status: in-progress
kind: derivation
level: introductory
tags: [stationary-states, separation-of-variables, time-independent-schrodinger-equation, hamiltonian, superposition, energy-measurement, griffiths]
prerequisites: [wave-function-and-statistical-interpretation, normalization-and-probability-current, momentum-operator-and-ehrenfest-theorem]
related: [infinite-square-well, harmonic-oscillator-ladder-operators, free-particle-and-wave-packets, generalized-statistical-interpretation, matrix-eigenvalue-problem]
order: 10
date: 2026-11-04
---

## Separation of variables

Assume the potential depends on $x$ only. Look for product solutions

$$
\Psi(x,t) = \psi(x)\,\varphi(t).
$$

Substitute into $i\hbar\,\partial_t\Psi = -(\hbar^2/2m)\,\partial_x^2\Psi + V\Psi$ and divide by $\psi\varphi$:

$$
i\hbar\,\frac{1}{\varphi}\frac{d\varphi}{dt} = -\frac{\hbar^2}{2m}\frac{1}{\psi}\frac{d^2\psi}{dx^2} + V(x).
$$

The left side depends only on $t$ and the right side only on $x$. Both must therefore equal the same constant, called $E$. This gives two ordinary differential equations.

**Time part.**

$$
\frac{d\varphi}{dt} = -\frac{iE}{\hbar}\varphi \quad\Longrightarrow\quad \varphi(t) = e^{-iEt/\hbar}.
$$

The integration constant is absorbed into $\psi$.

**Space part: the time-independent Schrödinger equation (TISE).**

$$
-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + V\psi = E\psi
\qquad\Longleftrightarrow\qquad
\hat H\psi = E\psi,\quad
\hat H = -\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2} + V(x).
$$

$\hat H$ is the classical Hamiltonian $p^2/2m + V$ with $p\to-i\hbar\,\partial_x$. The TISE is an eigenvalue equation; numerically it becomes a matrix eigenvalue problem ([[matrix-eigenvalue-problem]], and the finite-difference example in [[infinite-square-well]]).

## Why separable solutions matter

**1. They are stationary.** For $\Psi = \psi e^{-iEt/\hbar}$, the density $|\Psi|^2 = |\psi|^2$ does not depend on time. For any observable,

$$
\langle Q\rangle = \int\psi^*\,Q\!\left(x,-i\hbar\tfrac{d}{dx}\right)\psi\,dx,
$$

so every expectation value is constant. In particular $\langle x\rangle$ is constant, hence $\langle p\rangle = 0$: nothing moves in a stationary state.

**2. They have sharp energy.** Since $\hat H\psi = E\psi$, also $\hat H^2\psi = E^2\psi$. Therefore $\langle H\rangle = E$, $\langle H^2\rangle = E^2$ and

$$
\sigma_H^2 = \langle H^2\rangle - \langle H\rangle^2 = 0 .
$$

Every energy measurement on this state returns $E$.

**3. They span the solutions.** The TISE typically has a discrete set of solutions $\psi_n$ with **allowed energies** $E_n$. By linearity, the general solution of the time-dependent equation is

$$
\Psi(x,t) = \sum_n c_n\,\psi_n(x)\,e^{-iE_nt/\hbar},
\qquad
\Psi(x,0) = \sum_n c_n\psi_n(x).
$$

**Recipe.** Solve the TISE, expand the initial state in the $\psi_n$ to obtain the $c_n$, and attach the phase $e^{-iE_nt/\hbar}$ to each term. The superposition itself is *not* stationary when two or more $E_n$ with $c_n\neq0$ differ.

## Meaning of the coefficients

Griffiths states here, and justifies in Ch. 3 ([[generalized-statistical-interpretation]]):

$$
|c_n|^2 = \text{probability that an energy measurement gives } E_n,
\qquad
\sum_n|c_n|^2 = 1,
\qquad
\langle H\rangle = \sum_n|c_n|^2E_n .
$$

**Proof of the sum rules,** given orthonormal $\psi_n$ ($\int\psi_m^*\psi_n\,dx = \delta_{mn}$, proved for specific potentials in later notes):

$$
1 = \int|\Psi|^2dx = \sum_{m,n}c_m^*c_n\int\psi_m^*\psi_n\,dx = \sum_n|c_n|^2,
$$

and in the same way $\int\Psi^*\hat H\Psi\,dx = \sum_n|c_n|^2E_n$.

**Energy conservation.** The $c_n$ do not depend on $t$, so the energy probabilities, and hence $\langle H\rangle$, are constant in time.

## General theorems (Griffiths Problems 2.1-2.2)

These hold for normalizable solutions of the TISE with real $V$.

1. **$E$ is real.** Write $E = E_0 + i\Gamma$. Then $|\Psi|^2 = |\psi|^2e^{2\Gamma t/\hbar}$, and the total probability stays at 1 for all $t$ (see [[normalization-and-probability-current]]) only if $\Gamma = 0$.
2. **$\psi$ can be taken real.** If $\psi$ solves the TISE at energy $E$, so does $\psi^*$ (since $V$ and $E$ are real). Hence so do the real combinations $\psi+\psi^*$ and $i(\psi-\psi^*)$. A complex solution is therefore a combination of real solutions at the same energy. This does not make $\Psi(x,t)$ real.
3. **Even potentials allow parity eigenstates.** If $V(-x)=V(x)$, then $\psi(-x)$ is also a solution at energy $E$, and so are $\psi(x)\pm\psi(-x)$. Solutions can be chosen even or odd.
4. **$E > V_{\min}$.** Write the TISE as $\psi'' = (2m/\hbar^2)(V-E)\psi$. If $E<V_{\min}$, then $\psi$ and $\psi''$ always have the same sign. $\psi$ then curves away from the axis everywhere and cannot go to zero at both ends, so it cannot be normalized. Classically, the kinetic energy cannot be negative.

## Worked example

!!! example "Two-state beat in the infinite square well (Griffiths Example 2.1 and Problem 2.5)"
    **State.** Take $\Psi(x,0) = \tfrac{1}{\sqrt2}\left[\psi_1+\psi_2\right]$ in the well of width $a$ ([[infinite-square-well]]). The $\psi_n$ are real and orthonormal, so $A = 1/\sqrt2$. With $\omega \equiv (E_2-E_1)/\hbar = 3\pi^2\hbar/2ma^2$:

    $$
    |\Psi(x,t)|^2 = \tfrac12\left[\psi_1^2+\psi_2^2+2\psi_1\psi_2\cos\omega t\right].
    $$

    The density sloshes back and forth at the Bohr frequency $\omega$. The interference term is the only source of time dependence.

    **Position.** $\langle x\rangle(t) = \tfrac a2 + \langle\psi_1|x|\psi_2\rangle\cos\omega t$, with

    $$
    \langle\psi_1|x|\psi_2\rangle = \frac{2}{a}\int_0^a x\sin\frac{\pi x}{a}\sin\frac{2\pi x}{a}\,dx = -\frac{16a}{9\pi^2} = -0.180127\,a .
    $$

    The amplitude $0.180a$ is less than $a/2$, as it must be.

    **Momentum.** $\langle p\rangle = m\,d\langle x\rangle/dt = (8\hbar/3a)\sin\omega t$.

    **Energy.** A measurement gives $E_1$ or $E_2$, each with probability $1/2$, and $\langle H\rangle = (E_1+E_2)/2 = 5\pi^2\hbar^2/4ma^2$.

    Checked by quadrature in `ch02_tise.py` (section A).

## Source

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Sec. 2.1, Eqs. (2.1)-(2.21), Example 2.1, Problems 2.1, 2.2, 2.5. Page numbers are not given because the PDF used is an e-book rendering without print pagination. Equations were read from the page images. Numbers recomputed with `griffiths/ch02_tise.py` (section A).
