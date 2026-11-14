---
id: energy-time-uncertainty-principle
title: Time dependence of expectation values and the energy–time uncertainty principle
summary: The generalized Ehrenfest theorem d⟨Q⟩/dt = (i/ħ)⟨[H,Q]⟩ + ⟨∂Q/∂t⟩ (conserved quantities commute with H). The energy–time relation ΔE Δt ≥ ħ/2 follows with Δt = σ_Q/|d⟨Q⟩/dt|, the time for ⟨Q⟩ to change by one standard deviation (Mandelstam–Tamm). Examples: two-state beat, passing wave packet, Δ-resonance width, time to reach an orthogonal state, and the virial theorem. Also why "borrowing energy" is a misreading.
status: in-progress
kind: derivation
level: intermediate
tags: [energy-time-uncertainty, ehrenfest-theorem, conservation-laws, mandelstam-tamm, virial-theorem, lifetime, linewidth, griffiths]
prerequisites: [generalized-uncertainty-principle, stationary-states]
related: [momentum-operator-and-ehrenfest-theorem, hellmann-feynman-and-virial-theorems, harmonic-oscillator-coherent-states]
order: 60
date: 2026-11-04
---

## Why it is different from position–momentum

$\Delta x\,\Delta p\ge\hbar/2$ relates spreads of two dynamical variables measured on an ensemble. In non-relativistic quantum mechanics, time is *not* a dynamical variable: it is the parameter on which everything else depends, and there is no time operator to measure. Relativity puts $(ct,x)$ and $(E/c,p)$ in four-vectors, which suggests an analogous energy–time relation. In this theory, however, the relation needs its own derivation, and its $\Delta t$ has a different meaning.

## Generalized Ehrenfest theorem

Differentiate $\langle Q\rangle = \langle\Psi|\hat Q\Psi\rangle$, use $i\hbar\,\partial_t\Psi = \hat H\Psi$, and move $\hat H$ across the inner product by hermiticity:

$$
\boxed{\ \frac{d}{dt}\langle Q\rangle = \frac{i}{\hbar}\left\langle[\hat H,\hat Q]\right\rangle + \left\langle\frac{\partial\hat Q}{\partial t}\right\rangle\ }
$$

**Conservation.** If $\hat Q$ has no explicit time dependence and commutes with $\hat H$, then $\langle Q\rangle$ is constant, for every state. This is the quantum meaning of a conserved quantity.

**Special cases** (Griffiths Problems 3.18-3.19).

| $Q$ | Result | Meaning |
|---|---|---|
| $1$ | $d\langle1\rangle/dt = 0$ | conservation of probability ([[normalization-and-probability-current]]) |
| $H$ | $d\langle H\rangle/dt = 0$ | energy conservation, for time-independent $V$ |
| $x$ | $d\langle x\rangle/dt = \langle p\rangle/m$ | |
| $p$ | $d\langle p\rangle/dt = -\langle V'\rangle$ | Ehrenfest ([[momentum-operator-and-ehrenfest-theorem]]) |

Consequences: for $V=0$, $\langle x\rangle$ moves at constant velocity for *any* packet. For $V = \tfrac12m\omega^2x^2$, $\langle x\rangle$ oscillates at exactly $\omega$ for any state.

## Derivation of $\Delta E\,\Delta t\ge\hbar/2$

Take $A = H$ and $B = Q$, with $Q$ not explicitly time dependent, in the generalized uncertainty principle ([[generalized-uncertainty-principle]]):

$$
\sigma_H^2\sigma_Q^2 \ge \left(\frac{1}{2i}\langle[\hat H,\hat Q]\rangle\right)^2 = \left(\frac{\hbar}{2}\right)^2\left(\frac{d\langle Q\rangle}{dt}\right)^2 .
$$

Define

$$
\Delta E\equiv\sigma_H,\qquad \Delta t\equiv\frac{\sigma_Q}{|d\langle Q\rangle/dt|}
\quad\Longrightarrow\quad \Delta E\,\Delta t\ge\frac{\hbar}{2}.
$$

**What $\Delta t$ is.** It is the time for $\langle Q\rangle$ to move by one standard deviation $\sigma_Q$. It depends on which observable is watched; this is the Mandelstam–Tamm formulation (Griffiths footnote 25). If $\Delta E$ is small, *every* observable changes slowly. A stationary state, with $\Delta E=0$, never changes at all.

**What it is not.** Griffiths stresses that it is not licence to "borrow" energy $\Delta E$ for a time $\hbar/2\Delta E$. Nothing in the derivation violates energy conservation; the relation concerns spreads and rates.

## Examples

!!! example "Two-state beat (Griffiths Example 3.5 and Problem 3.20)"
    **State.** $\Psi = (\psi_1e^{-iE_1t/\hbar}+\psi_2e^{-iE_2t/\hbar})/\sqrt2$ in the infinite well ($a=1$, $\hbar=m=1$).

    **Rough estimate.** Take $\Delta E\approx E_2-E_1$ and $\Delta t\approx$ the beat period $2\pi\hbar/(E_2-E_1)$. This gives $\Delta E\,\Delta t\approx 2\pi\hbar$.

    **Exact check with $Q=x$.**

    - $\sigma_H = (E_2-E_1)/2 = 7.4022$.
    - $\langle x\rangle(t) = \tfrac12 - \tfrac{16}{9\pi^2}\cos\omega t$.
    - $\langle x^2\rangle(t) = \tfrac13 - \tfrac{5}{16\pi^2} - \tfrac{16}{9\pi^2}\cos\omega t$, using $\langle1|x^2|2\rangle = \langle1|x|2\rangle$, which follows from parity about $a/2$.

    Over a full period,

    $$
    \min_t\left[\sigma_H\sigma_x - \tfrac{\hbar}{2}\left|\tfrac{d\langle x\rangle}{dt}\right|\right] = 0.349 > 0 .
    $$

!!! example "Time to become orthogonal (Griffiths Problem 3.38)"
    For the same state, $\langle\Psi(0)|\Psi(t)\rangle = \tfrac12(e^{-iE_1t/\hbar}+e^{-iE_2t/\hbar})$, which first vanishes at

    $$
    \tau = \frac{\pi\hbar}{E_2-E_1}.
    $$

    With $\Delta t = \tau/\pi$ (Vaidman's version, Griffiths footnote 41) and $\Delta E = \sigma_H = (E_2-E_1)/2$:

    $$
    \Delta E\,\Delta t = \frac{\hbar}{2}\quad\text{exactly}.
    $$

    An equal two-state superposition reaches an orthogonal state as fast as the bound allows.

!!! example "Passing wave packet and resonance width (Griffiths Examples 3.6-3.7)"
    **Wave packet.** A packet of width $\Delta x$ passes a point in $\Delta t = m\Delta x/p$. With $\Delta E = p\Delta p/m$, this gives $\Delta E\,\Delta t = \Delta x\,\Delta p\ge\hbar/2$.

    **$\Delta(1232)$ resonance.** Its mass histogram has width about 120 MeV/$c^2$, and its lifetime is about $10^{-23}$ s:

    $$
    \Delta E\,\Delta t = 60\ \text{MeV}\times10^{-23}\ \text{s} = 6\times10^{-22}\ \text{MeV s},\qquad
    \hbar/2 = 3.29\times10^{-22}\ \text{MeV s}.
    $$

    The mass spread is about as small as the principle allows. Griffiths admits (footnote 26) that the lifetime is in practice *inferred* from the width this way, so the example is circular as a test.

## Virial theorem (Griffiths Problem 3.37)

**Derivation.** Apply the generalized Ehrenfest theorem to $Q = xp$. With $[\hat H,x\hat p] = -i\hbar\left(\hat p^2/m - xV'\right)$:

$$
\frac{d}{dt}\langle xp\rangle = 2\langle T\rangle - \left\langle x\frac{dV}{dx}\right\rangle .
$$

**Stationary states.** There every expectation value is constant, so

$$
2\langle T\rangle = \langle xV'\rangle .
$$

**Power laws.** For $V\propto x^s$, $\langle xV'\rangle = s\langle V\rangle$, so $\langle T\rangle = \tfrac s2\langle V\rangle$. The oscillator ($s=2$) gives $\langle T\rangle = \langle V\rangle$ ([[harmonic-oscillator-ladder-operators]]). A quartic ($s=4$) gives $\langle T\rangle = 2\langle V\rangle$. The Coulomb case ($s=-1$, $2\langle T\rangle = -\langle V\rangle$) is in [[hellmann-feynman-and-virial-theorems]].

!!! example "Finite-difference check ($\hbar=m=1$, 4000 points on $[-8,8]$)"
    | Potential | $n$ | $2\langle T\rangle$ | $\langle xV'\rangle$ | $\langle T\rangle/\langle V\rangle$ |
    |---|---|---|---|---|
    | $x^2/2$ | 0 | 0.50000 | 0.50000 | 1.00000 |
    | $x^2/2$ | 2 | 2.49996 | 2.49999 | 0.99999 |
    | $x^4$ | 0 | 0.89064 | 0.89064 | 1.99999 |
    | $x^4$ | 2 | 6.26215 | 6.26230 | 1.99995 |

## Source

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Sec. 3.5.3, Eqs. (3.71)-(3.76), Examples 3.5-3.7; Problems 3.18-3.22, 3.37 (Eqs. 3.112-3.113), 3.38; footnotes 23-26, 41. Page numbers are not given because the PDF used is an e-book rendering without print pagination. The commutator $[\hat H,x\hat p]$, the power-law corollary and all numerical tables are worked here, not quoted. Numbers from `griffiths/ch03_formalism.py` (section D).
