---
id: de-broglie-and-heisenberg-uncertainty
title: De Broglie relation and the Heisenberg uncertainty principle
summary: The position–wavelength trade-off for any wave, de Broglie's p = h/λ, Heisenberg's σxσp ≥ ħ/2 stated as a property of ensembles, three test states (Gaussian, parabola, e^{−λ|x|}) with exact uncertainty products, the δ-function pitfall in ⟨p²⟩ for a kinked wave function, and the thermal de Broglie criterion for when quantum mechanics is needed.
status: in-progress
kind: theory
level: introductory
tags: [uncertainty-principle, de-broglie, standard-deviation, gaussian-wave-packet, thermal-wavelength, griffiths]
prerequisites: [wave-function-and-statistical-interpretation, momentum-operator-and-ehrenfest-theorem]
related: [generalized-uncertainty-principle, free-particle-and-wave-packets, harmonic-oscillator-ladder-operators, normalization-and-probability-current]
also: []
date: 2026-11-04
---

## The trade-off for any wave

A long sinusoidal wave has a well-defined wavelength but no well-defined position. A short pulse has a well-defined position but no single wavelength. Fourier analysis makes this precise: a function concentrated in a small $\Delta x$ needs a superposition of wavenumbers spread over $\Delta k \gtrsim 1/\Delta x$.

For a matter wave, wavelength is tied to momentum by the **de Broglie relation**:

$$
p = \frac{h}{\lambda} = \frac{2\pi\hbar}{\lambda} = \hbar k .
$$

A spread in wavelength is therefore a spread in momentum, and position and momentum cannot both be sharp. Quantitatively, this is **Heisenberg's uncertainty principle**:

$$
\sigma_x\,\sigma_p \ge \frac{\hbar}{2} .
$$

Here $\sigma_x$ and $\sigma_p$ are the standard deviations of position and momentum in the state $\Psi$. The proof, for any pair of observables, is in [[generalized-uncertainty-principle]] (Griffiths Ch. 3). Griffiths takes de Broglie's relation as motivation here and derives it later from $\hat p = -i\hbar\,\partial_x$ (his footnote 21).

## What the inequality means

$\sigma_x$ and $\sigma_p$ are spreads of outcomes over an **ensemble** of identically prepared systems: measure $x$ on half of them and $p$ on the other half. The principle is not about one measurement disturbing another; it is a property of the state.

- A state with very small $\sigma_x$ (a spike) has a large $\sigma_p$, and the reverse holds for a long sinusoid.
- The inequality bounds the product only from below. Many states (a wiggly, irregular $\Psi$) have both spreads large.

For a given state,

$$
\sigma_x^2 = \langle x^2\rangle - \langle x\rangle^2,
\qquad
\sigma_p^2 = \langle p^2\rangle - \langle p\rangle^2,
\qquad
\langle p^2\rangle = \hbar^2\int\left|\frac{\partial\Psi}{\partial x}\right|^2dx .
$$

The last form of $\langle p^2\rangle$ follows from $-\hbar^2\int\Psi^*\Psi''dx$ after one integration by parts. It is the safe form whenever $\Psi'$ has a jump (see the third example below).

## Three test states

| State | $\sigma_x$ | $\sigma_p$ | $\sigma_x\sigma_p/\hbar$ |
|---|---|---|---|
| Gaussian $\propto e^{-amx^2/\hbar}$ | $\sqrt{\hbar/4am}$ | $\sqrt{am\hbar}$ | $1/2 = 0.5$ (the minimum) |
| Parabola $A(a^2-x^2)$ on $[-a,a]$ | $a/\sqrt7$ | $\sqrt{5/2}\,\hbar/a$ | $\sqrt{5/14} = 0.5976$ |
| Cusp $\sqrt\lambda\,e^{-\lambda|x|}$ | $1/(\sqrt2\lambda)$ | $\hbar\lambda$ | $1/\sqrt2 = 0.7071$ |

The Gaussian saturates the bound; Griffiths Sec. 3.5.2 shows that only Gaussians (allowing a shift in position and a linear phase) do. Sharper features (corners, kinks) cost momentum spread.

## Worked examples

!!! example "Gaussian state (Griffiths Problem 1.9)"
    $\Psi(x,t) = A\,e^{-a\left(mx^2/\hbar + it\right)}$ with $a>0$.

    **Normalization.** $|\Psi|^2 = A^2e^{-2amx^2/\hbar}$, so $A = (2am/\pi\hbar)^{1/4}$.

    **Potential.** Substitute into $i\hbar\,\partial_t\Psi = -(\hbar^2/2m)\Psi'' + V\Psi$:

    - left side: $i\hbar\,\partial_t\Psi = \hbar a\Psi$;
    - kinetic term: $-(\hbar^2/2m)\Psi'' = \left(\hbar a - 2ma^2x^2\right)\Psi$.

    Hence

    $$
    V(x) = 2ma^2x^2 = \tfrac12m\omega^2x^2 \quad\text{with}\quad \omega = 2a .
    $$

    This is the harmonic-oscillator ground state, and $\langle H\rangle = \hbar a = \tfrac12\hbar\omega$ ([[harmonic-oscillator-ladder-operators]]).

    **Moments.**

    $$
    \langle x\rangle = 0,\quad \langle x^2\rangle = \frac{\hbar}{4am},\quad
    \langle p\rangle = 0,\quad \langle p^2\rangle = am\hbar,
    \qquad \sigma_x\sigma_p = \frac{\hbar}{2}.
    $$

!!! example "Parabolic state (Griffiths Problem 1.16)"
    $\Psi = A(a^2-x^2)$ for $|x|\le a$ and zero outside.

    **Normalization.** $\int_{-a}^{a}(a^2-x^2)^2dx = 16a^5/15$, so $A = \sqrt{15}/(4a^{5/2})$.

    **Moments.**

    $$
    \langle x\rangle = 0,\qquad \langle x^2\rangle = \frac{a^2}{7},\qquad \langle p\rangle = 0,
    $$

    $$
    \langle p^2\rangle = -\hbar^2A^2\int_{-a}^{a}(a^2-x^2)(-2)\,dx = \frac{5\hbar^2}{2a^2}.
    $$

    The same value comes from $\hbar^2\int|\Psi'|^2dx$. $\Psi'$ jumps at $x=\pm a$, but $\Psi(\pm a)=0$ kills the $\delta$ terms in $\Psi''$.

    **Product.**

    $$
    \sigma_x\sigma_p = \sqrt{\frac{a^2}{7}\cdot\frac{5\hbar^2}{2a^2}} = \sqrt{\frac{5}{14}}\,\hbar = 0.59761\,\hbar > \frac{\hbar}{2}.
    $$

!!! example "Cusp state $\sqrt\lambda\,e^{-\lambda|x|}$ and the $\delta$-function pitfall (Griffiths Problem 1.5)"
    Here $\Psi(0)\neq0$ and $\Psi'$ jumps from $+\lambda^{3/2}$ to $-\lambda^{3/2}$ at $x=0$. Hence

    $$
    \Psi'' = \lambda^2\Psi - 2\lambda\,\Psi(0)\,\delta(x) .
    $$

    | Method | $\langle p^2\rangle$ |
    |---|---|
    | $-\hbar^2\int\Psi\Psi''$ with the $\delta$ term **dropped** | $-\hbar^2\lambda^2$ (negative, which is impossible) |
    | Contribution of the $\delta$ term, $+2\hbar^2\lambda\Psi(0)^2$ | $+2\hbar^2\lambda^2$ |
    | Total, equal to $\hbar^2\int|\Psi'|^2dx$ | $+\hbar^2\lambda^2$ |

    With $\sigma_x = 1/(\sqrt2\lambda)$ this gives $\sigma_x\sigma_p = \hbar/\sqrt2$. Use the $|\Psi'|^2$ form for any kinked function.

## How large is a de Broglie wavelength?

For an electron of kinetic energy $T$, $\lambda = h/\sqrt{2m_eT}$:

| Particle and condition | $\lambda$ |
|---|---|
| Electron, $T = 1$ eV | 1.2264 nm |
| Electron, $T = 100$ eV | 0.12264 nm (comparable to bond lengths, hence low-energy electron diffraction) |
| Electron, thermal at 300 K | 6.228 nm |
| ⁴He atom, thermal at 300 K | 0.07291 nm |

**Thermal criterion.** Griffiths's rough test (Problem 1.18) is that quantum mechanics is needed when the thermal wavelength

$$
\lambda = \frac{h}{\sqrt{3mk_BT}},
$$

which follows from $p^2/2m = \tfrac32k_BT$, exceeds the characteristic spacing $d$. Then $T < h^2/(3mk_Bd^2)$. Recomputed values:

| System | Quantum below |
|---|---|
| Unbound electrons in a solid, $d=0.3$ nm | $1.29\times10^{5}$ K, so always quantum |
| Silicon nuclei, $d=0.3$ nm | 2.5 K, so normally classical |
| ⁴He gas at 1 atm, using $T<(1/k_B)(h^2/3m)^{3/5}P^{2/5}$ | 2.94 K |
| Atomic H in space, 3 K, $d\approx1$ cm | $\lambda = 1.45$ nm $\ll d$, so classical |

The order of magnitude, not the prefactor, is the content of this criterion.

## Source

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Sec. 1.6, Eqs. (1.39)-(1.40), (1.45), footnote 21; Problems 1.5, 1.9, 1.16, 1.18. Page numbers are not given because the PDF used is an e-book rendering without print pagination. The problem answers are derived here, not quoted. The statement that only the Gaussian saturates the bound refers ahead to Sec. 3.5.2. All entries in the tables recomputed with `griffiths/ch01_wave_function.py` (sections C, D, E, H, I; SymPy, SciPy `constants`, CODATA 2018).
