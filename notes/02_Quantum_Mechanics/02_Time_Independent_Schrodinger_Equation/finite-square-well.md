---
id: finite-square-well
title: The finite square well
summary: Bound states of a well of depth V0 and width 2a, from the transcendental equations tan z = √((z0/z)² − 1) (even) and −cot z = √(...) (odd). Covers the number of bound states, the deep-well and shallow-well limits (always at least one bound state), the delta-function limit, a half-well example where the particle is more likely outside than inside, scattering with the transmission formula and its resonances. Checked against finite-difference diagonalization and a transfer-matrix solver.
status: in-progress
kind: derivation
level: introductory
tags: [finite-square-well, bound-states, transcendental-equation, resonance, ramsauer-townsend, transmission, griffiths]
prerequisites: [stationary-states, infinite-square-well, delta-function-potential]
related: [one-dimensional-scattering-and-transfer-matrix, free-particle-and-wave-packets]
order: 70
date: 2026-11-04
---

## Setup

$$
V(x) = \begin{cases}-V_0, & |x|\le a\\ 0, & |x|>a\end{cases}\qquad (V_0>0).
$$

The well supports bound states ($-V_0<E<0$) and scattering states ($E>0$).

## Bound states

**Wave numbers.**

$$
\kappa = \frac{\sqrt{-2mE}}{\hbar}\ (\text{outside}),\qquad
l = \frac{\sqrt{2m(E+V_0)}}{\hbar}\ (\text{inside}).
$$

**Form of the solution.** Outside, normalizability leaves $e^{\mp\kappa x}$ on the right and left. $V$ is even, so solutions can be taken even ($\cos lx$ inside) or odd ($\sin lx$ inside), as shown in [[stationary-states]]. Only $x=a$ then needs matching.

**Even states.** Matching $Fe^{-\kappa a} = D\cos la$ and $-\kappa Fe^{-\kappa a} = -lD\sin la$, and dividing, gives $\kappa = l\tan la$.

**Odd states.** The same steps give $\kappa = -l\cot la$.

**Dimensionless form.** Introduce

$$
z = la,\qquad z_0 = \frac{a}{\hbar}\sqrt{2mV_0},\qquad \kappa a = \sqrt{z_0^2-z^2}.
$$

The quantization conditions become

$$
\text{even:}\ \tan z = \sqrt{\left(\frac{z_0}{z}\right)^2-1},\qquad
\text{odd:}\ -\cot z = \sqrt{\left(\frac{z_0}{z}\right)^2-1},\qquad
E = \frac{\hbar^2z^2}{2ma^2} - V_0 .
$$

$z_0$ alone, a combination of width and depth, fixes the spectrum in units of $V_0$.

**Number of bound states.** Even roots lie in $(j\pi, j\pi+\pi/2)$ and odd roots in $(j\pi+\pi/2, (j+1)\pi)$, and both require $z<z_0$. The count is therefore

$$
N = \left\lceil \frac{2z_0}{\pi}\right\rceil .
$$

There is always at least one (even) bound state, however shallow or narrow the well. The first odd state appears when $z_0>\pi/2$ (Griffiths Problem 2.29).

**Limits.**

- **Wide, deep well** ($z_0\to\infty$). The roots approach $z = n\pi/2$, so $E_n + V_0 \to n^2\pi^2\hbar^2/2m(2a)^2$, the [[infinite-square-well]] of width $2a$. Even states give odd $n$ and odd states give even $n$.
- **Delta limit** (Problem 2.31). Let $a\to0$ and $V_0\to\infty$ with $2aV_0 = \alpha$ fixed. Then $z_0\to0$, a single even state survives, and $E\to-m\alpha^2/2\hbar^2$, the [[delta-function-potential]] result:

| $a$ | $V_0$ | $E$ |
|---|---|---|
| 0.1 | 5 | $-0.442107$ |
| 0.01 | 50 | $-0.493434$ |
| 0.001 | 500 | $-0.499334$ |
| limit | | $-0.5$ |

Units: $\hbar=m=\alpha=1$.

## Worked examples

!!! example "$z_0 = 8$: six bound states ($\hbar=m=a=1$, $V_0 = 32$)"
    Root finding, checked against finite-difference diagonalization on $[-8,8]$ with 6000 points:

    | Parity | $z$ | $E+V_0$ | $E$ (roots) | $E$ (finite difference) |
    |---|---|---|---|---|
    | even | 1.395466 | 0.973663 | $-31.026337$ | $-31.0266$ |
    | odd | 2.785902 | 3.880625 | $-28.119375$ | $-28.1206$ |
    | even | 4.164831 | 8.672908 | $-23.327092$ | $-23.3298$ |
    | odd | 5.521446 | 15.243185 | $-16.756815$ | $-16.7615$ |
    | even | 6.830674 | 23.329056 | $-8.670944$ | $-8.6779$ |
    | odd | 7.957321 | 31.659483 | $-0.340517$ | $-0.3459$ |

    $\lceil 16/\pi\rceil = 6$. The finite-difference values drift by up to about $5\times10^{-3}$ for the top state. The step in $V$ makes the three-point scheme converge more slowly than for smooth potentials.

!!! example "More likely outside than inside (Griffiths Problem 2.48)"
    **Potential.** $V=\infty$ for $x<0$, $V = -32\hbar^2/ma^2$ for $0\le x\le a$, and $V=0$ for $x>a$.

    **Reduction to the symmetric well.** The wall forces $\psi(0)=0$, so the states are exactly the *odd* states of the symmetric well with $z_0 = a\sqrt{2m\cdot32\hbar^2/ma^2}/\hbar = 8$. That gives three bound states.

    **Topmost state.** $z = 7.957321$ and $\kappa a = \sqrt{64-z^2} = 0.8253$, so the exponential tail is long. Integrating $\sin^2(zx/a)$ inside and the matched tail $\sin^2z\,e^{-2\kappa(x-a)}$ outside:

    $$
    P(x>a) = 0.542041 .
    $$

    This agrees with the book's 0.542. The particle is bound, yet more likely to be found outside the well than inside.

## Scattering states

**Setup.** For $E>0$, with $k = \sqrt{2mE}/\hbar$ outside and $l$ as before inside, take $Ae^{ikx}+Be^{-ikx}$ on the left and $Fe^{ikx}$ on the right. Four matching conditions fix $B$, $C$, $D$ and $F$ in terms of $A$, giving

$$
T^{-1} = 1 + \frac{V_0^2}{4E(E+V_0)}\sin^2\!\left(\frac{2a}{\hbar}\sqrt{2m(E+V_0)}\right).
$$

**Resonances.** $T=1$ exactly when the sine vanishes, $2la = n\pi$, that is when

$$
E_n + V_0 = \frac{n^2\pi^2\hbar^2}{2m(2a)^2}.
$$

These are the infinite-well levels of width $2a$: the well becomes transparent when a whole number of half-wavelengths fits inside. The effect is seen experimentally as the Ramsauer–Townsend minimum in electron scattering from noble-gas atoms.

!!! example "Transmission checks ($\hbar=m=a=1$, $V_0=10$)"
    | $E$ | Closed form $T$ | Transfer-matrix $T$ | $R+T$ |
    |---|---|---|---|
    | 0.5 | 0.761132 | 0.761132 | 1.00000000 |
    | 2.0 | 0.878382 | 0.878382 | 1.00000000 |
    | 7.0 | 0.885096 | 0.885096 | 1.00000000 |

    Resonances at $E = n^2\pi^2/8 - 10$ for $n = 3, 4, 5$, that is $E = 1.103305$, $9.739209$ and $20.842514$, give $T = 1.0000000000$.

## Source

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Sec. 2.6, Eqs. (2.148)-(2.174), Figs. 2.16-2.18 (described); Problems 2.29, 2.31, 2.32, 2.48. Page numbers are not given because the PDF used is an e-book rendering without print pagination. The bound-state count formula, the mention of the Ramsauer–Townsend effect and all numerical tables are additions or computed answers, not quotations. Recomputed with `griffiths/ch02_tise.py` (section G).
