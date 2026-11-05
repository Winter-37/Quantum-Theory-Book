---
id: free-particle-and-wave-packets
title: The free particle, wave packets and group velocity
summary: Free-particle plane waves are not normalizable, so physical states are wave packets built by Fourier superposition (Plancherel's theorem). The note covers the paradox of the phase velocity being half the classical speed and its resolution by the group velocity dω/dk, the spreading of a square packet and of a gaussian packet (exact σx(t), uncertainty product growing in time), and FFT propagation checked against the closed form.
status: in-progress
kind: derivation
level: introductory
tags: [free-particle, plane-waves, wave-packet, fourier-transform, plancherel, group-velocity, phase-velocity, dispersion, gaussian-wave-packet, griffiths]
prerequisites: [stationary-states, de-broglie-and-heisenberg-uncertainty]
related: [normalization-and-probability-current, delta-function-potential, one-dimensional-scattering-and-transfer-matrix, generalized-statistical-interpretation]
also: []
date: 2026-11-04
---

## Separable solutions

With $V=0$ the TISE is $\psi'' = -k^2\psi$, $k = \sqrt{2mE}/\hbar$. There are no boundary conditions, so every $E>0$ is allowed. In exponential form, letting $k$ run over both signs:

$$
\Psi_k(x,t) = A\,e^{i\left(kx - \frac{\hbar k^2}{2m}t\right)},\qquad
k = \pm\frac{\sqrt{2mE}}{\hbar}\ \begin{cases}k>0: & \text{moving right}\\ k<0: & \text{moving left.}\end{cases}
$$

Each is a travelling wave with $p = \hbar k$ and wavelength $2\pi/|k|$.

**Two problems.**

1. **Speed.** The wave crests move at $v_{\rm phase} = \hbar|k|/2m = \sqrt{E/2m}$, half the classical speed $v_{\rm classical} = \sqrt{2E/m}$.
2. **Normalization.** $\int|\Psi_k|^2dx = |A|^2\cdot\infty$. A free particle cannot be in a state of definite energy.

## Wave packets

The general solution is still a superposition of separable solutions, now an integral over the continuous label $k$:

$$
\Psi(x,t) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\phi(k)\,e^{i\left(kx - \frac{\hbar k^2}{2m}t\right)}dk .
$$

This can be normalized for suitable $\phi(k)$. Matching $\Psi(x,0)$ is a Fourier problem, solved by **Plancherel's theorem**:

$$
f(x) = \frac{1}{\sqrt{2\pi}}\int F(k)\,e^{ikx}dk
\quad\Longleftrightarrow\quad
F(k) = \frac{1}{\sqrt{2\pi}}\int f(x)\,e^{-ikx}dx,
$$

so that

$$
\phi(k) = \frac{1}{\sqrt{2\pi}}\int\Psi(x,0)\,e^{-ikx}dx .
$$

With the symmetric $1/\sqrt{2\pi}$ convention, $\int|\phi|^2dk = \int|\Psi|^2dx$. Griffiths Problem 2.19 obtains the theorem as the $a\to\infty$ limit of Fourier series on $[-a,a]$. The physical meaning of $\phi$, as the momentum-space wave function, comes in [[generalized-statistical-interpretation]].

## Group velocity resolves the speed paradox

**General dispersion relation.** Write $\Psi = (2\pi)^{-1/2}\int\phi(k)e^{i(kx-\omega(k)t)}dk$ with $\phi$ sharply peaked at $k_0$. Expand $\omega(k)\approx\omega_0+\omega_0'(k-k_0)$ and set $s=k-k_0$:

$$
\Psi(x,t) \approx \frac{1}{\sqrt{2\pi}}\,e^{i(k_0x-\omega_0t)}\int\phi(k_0+s)\,e^{is(x-\omega_0't)}ds .
$$

The prefactor is the ripple, moving at $v_{\rm phase} = \omega/k$. The integral is the envelope, a function of $x-\omega_0't$, moving at

$$
v_{\rm group} = \frac{d\omega}{dk}\Big|_{k_0}.
$$

**Free particle.** $\omega = \hbar k^2/2m$ gives $v_{\rm group} = \hbar k/m = 2v_{\rm phase} = v_{\rm classical}$. The particle is the envelope, and the envelope moves at the classical speed.

## Spreading: two exact cases

!!! example "Square initial packet (Griffiths Example 2.6)"
    **State.** $\Psi(x,0) = 1/\sqrt{2a}$ for $|x|<a$, zero otherwise.

    **Momentum amplitude.**

    $$
    \phi(k) = \frac{1}{\sqrt{\pi a}}\,\frac{\sin ka}{k}.
    $$

    $\phi$ has width $\sim\pi/a$: a narrow box gives a broad $\phi$ and vice versa, which is the uncertainty principle in action. The integral for $\Psi(x,t)$ has no elementary closed form.

    **Numerical evaluation** at $t = ma^2/\hbar$, direct $k$ quadrature on $|k|<400/a$, with captured norm 0.9992:

    | $x/a$ | 0 | 1 | 2 | 4 |
    |---|---|---|---|---|
    | $a\,|\Psi|^2$ | 0.3113 | 0.2211 | 0.0665 | 0.0137 |

    The flat top of height 0.5 has become a rounded peak of about 0.31 with spreading tails, consistent with Griffiths Fig. 2.8.

!!! example "Gaussian packet (Griffiths Problem 2.21)"
    **State.** $\Psi(x,0) = (2a/\pi)^{1/4}e^{-ax^2}$.

    **Time evolution.** Completing the square in the $k$ integral gives

    $$
    \Psi(x,t) = \left(\frac{2a}{\pi}\right)^{1/4}\frac{e^{-ax^2/\gamma^2}}{\gamma},\qquad \gamma = \sqrt{1+\frac{2i\hbar at}{m}}.
    $$

    **Density.** With $w^2 \equiv a/[1+(2\hbar at/m)^2]$, $|\Psi|^2 = \sqrt{2/\pi}\,w\,e^{-2w^2x^2}$.

    **Spreads.**

    $$
    \sigma_x = \frac{1}{2w},\qquad \sigma_p = \hbar\sqrt a\ \text{(constant)},\qquad
    \sigma_x\sigma_p = \frac{\hbar}{2}\sqrt{1+\left(\frac{2\hbar at}{m}\right)^2}.
    $$

    The product is minimal, $\hbar/2$, at $t=0$ and grows thereafter. The momentum distribution never changes, since $|\phi(k)|$ is time independent for a free particle; the packet spreads because its faster and slower components separate.

    **FFT check** ($a=1/2$, $\hbar=m=1$; $2^{14}$ points on a 400-wide box):

    | $t$ | $\max|\Psi_{\rm FFT}-\Psi_{\rm exact}|$ | $\sigma_x$ | $\sigma_x\sigma_p/\hbar$ |
    |---|---|---|---|
    | 0 | $3\times10^{-16}$ | 0.707107 | 0.500000 |
    | 1 | $4\times10^{-16}$ | 1.000000 | 0.707107 |
    | 5 | $2\times10^{-16}$ | 3.605551 | 2.549510 |

    **Moving packet.** Multiplying by $e^{ik_0x}$ with $k_0=3$ gives, at $t=4$, $\langle x\rangle = 12.000000 = (\hbar k_0/m)t$: the packet moves at the group velocity, not the phase velocity, which would give 6.

!!! example "Exponential packet (Griffiths Problem 2.20)"
    **State.** $\Psi(x,0) = \sqrt a\,e^{-a|x|}$.

    **Momentum amplitude.**

    $$
    \phi(k) = \sqrt{\frac{2}{\pi}}\,\frac{a^{3/2}}{a^2+k^2},
    $$

    a Lorentzian, with $\int|\phi|^2dk = 1.0000000000$ (Plancherel).

    **Limits.** Large $a$ gives a sharp spike in $x$ and a flat $\phi$; small $a$ gives a broad spread in $x$ and a narrow $\phi$.

## Probability current

For $\Psi_k$, $J = (\hbar k/m)|A|^2$, positive for $k>0$: probability flows in the direction of motion ([[normalization-and-probability-current]]). Plane waves are not normalizable, but used as idealized beams they are the language of [[one-dimensional-scattering-and-transfer-matrix]].

## Source

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Sec. 2.4, Eqs. (2.91)-(2.111), Example 2.6, Figs. 2.8-2.10 (described, not reproduced); Problems 2.17-2.21. Page numbers are not given because the PDF used is an e-book rendering without print pagination. The closed forms for $|\Psi|^2$, $\sigma_x$ and $\sigma_x\sigma_p$ are worked answers to Problem 2.21 (Griffiths gives $\gamma$ and the partial answer $\langle p^2\rangle = a\hbar^2$), verified numerically. Numbers recomputed with `griffiths/ch02_tise.py` (section E).
