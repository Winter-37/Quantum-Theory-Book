---
id: harmonic-oscillator-analytic-solution
title: The harmonic oscillator by power series; Hermite polynomials
summary: Direct solution of the oscillator equation. Dimensionless form, peeling off the gaussian asymptote, the two-term recursion and why normalizability forces it to terminate (K = 2n + 1), Hermite polynomials and their identities (Rodrigues formula, recursion, derivative, generating function), the normalized eigenfunctions, classically forbidden probabilities, and the shooting method as a numerical cross-check.
status: in-progress
kind: derivation
level: introductory
tags: [harmonic-oscillator, power-series, frobenius, hermite-polynomials, shooting-method, tunnelling-into-forbidden-region, griffiths]
prerequisites: [stationary-states, harmonic-oscillator-ladder-operators]
related: [radial-basis-functions-slater-and-gaussian, gaussian-basis-functions, infinite-square-well]
order: 40
date: 2026-11-04
---

## Dimensionless equation

Starting from $-\tfrac{\hbar^2}{2m}\psi'' + \tfrac12m\omega^2x^2\psi = E\psi$, measure length and energy in natural oscillator units:

$$
\xi = \sqrt{\frac{m\omega}{\hbar}}\,x,\qquad K = \frac{2E}{\hbar\omega}
\qquad\Longrightarrow\qquad
\frac{d^2\psi}{d\xi^2} = (\xi^2-K)\,\psi .
$$

## Asymptotics and the substitution

**Large $|\xi|$.** There $\xi^2$ dominates $K$, so $\psi''\approx\xi^2\psi$, with approximate solutions $Ae^{-\xi^2/2}+Be^{+\xi^2/2}$. The growing one is not normalizable.

**Substitution.** Peel off the decaying factor, $\psi(\xi) = h(\xi)\,e^{-\xi^2/2}$. This step is exact; only its motivation used the approximation. Then

$$
h'' - 2\xi h' + (K-1)h = 0 .
$$

## Power series and the recursion

Insert $h = \sum_j a_j\xi^j$ and collect powers of $\xi$. Each coefficient must vanish:

$$
a_{j+2} = \frac{2j+1-K}{(j+1)(j+2)}\,a_j .
$$

The recursion steps by two, so $a_0$ generates an even series $h_{\rm even}$ and $a_1$ an odd series $h_{\rm odd}$. These are the two independent solutions of a second-order ODE.

**Why the series must terminate.** For large $j$ the ratio tends to $a_{j+2}/a_j\approx 2/j$, giving $a_j\approx C/(j/2)!$. Then

$$
h(\xi) \approx C\sum_j\frac{\xi^{2j}}{j!} = Ce^{\xi^2}
\quad\Longrightarrow\quad
\psi \sim e^{+\xi^2/2},
$$

which is the non-normalizable branch again. A normalizable solution therefore requires the series to stop at some highest power $n$, with $a_{n+2}=0$:

$$
K = 2n+1 \quad\Longrightarrow\quad E_n = \left(n+\tfrac12\right)\hbar\omega,\qquad n = 0,1,2,\ldots
$$

In addition, the other-parity series must be switched off ($a_1=0$ for even $n$, $a_0=0$ for odd $n$). This reproduces the algebraic result of [[harmonic-oscillator-ladder-operators]].

**Physical picture.** For any $E$ the ODE has solutions. For almost every $E$, however, they blow up at large $|\xi|$, and the sign of the divergence flips as $E$ crosses an eigenvalue. Shooting from $\xi=0$ with even initial data ($\psi(0)=1$, $\psi'(0)=0$):

| $E/\hbar\omega$ | $\psi(\xi=4)$ |
|---|---|
| 0.49 | $+6.95$ |
| 0.51 | $-6.72$ |

Only exactly at $E=\tfrac12\hbar\omega$ does the tail turn over to zero.

## Hermite polynomials

At $K=2n+1$ the recursion becomes $a_{j+2} = -2(n-j)\,a_j/[(j+1)(j+2)]$, and the terminating polynomial, scaled so that the leading coefficient is $2^n$, is the Hermite polynomial $H_n(\xi)$:

| $n$ | $H_n(\xi)$ |
|---|---|
| 0 | $1$ |
| 1 | $2\xi$ |
| 2 | $4\xi^2-2$ |
| 3 | $8\xi^3-12\xi$ |
| 4 | $16\xi^4-48\xi^2+12$ |
| 5 | $32\xi^5-160\xi^3+120\xi$ |
| 6 | $64\xi^6-480\xi^4+720\xi^2-120$ |

The normalized eigenfunctions are

$$
\psi_n(x) = \left(\frac{m\omega}{\pi\hbar}\right)^{1/4}\frac{1}{\sqrt{2^nn!}}\,H_n(\xi)\,e^{-\xi^2/2}.
$$

**Identities** (Griffiths Problem 2.16; all checked symbolically for $n\le6$):

$$
\begin{aligned}
&\text{Rodrigues:} && H_n(\xi) = (-1)^ne^{\xi^2}\frac{d^n}{d\xi^n}e^{-\xi^2},\\
&\text{recursion:} && H_{n+1} = 2\xi H_n - 2nH_{n-1},\\
&\text{derivative:} && H_n' = 2nH_{n-1},\\
&\text{generating function:} && e^{-z^2+2z\xi} = \sum_{n=0}^\infty\frac{z^n}{n!}H_n(\xi).
\end{aligned}
$$

**Properties of $\psi_n$.**

- $\psi_n$ has parity $(-1)^n$ and exactly $n$ nodes.
- Odd states vanish at the centre.
- Every state has nonzero probability beyond the classical turning points.
- At large $n$, the coarse-grained $|\psi_n|^2$ approaches the classical density $1/(\pi\sqrt{A^2-x^2})$, where $A$ is the classical amplitude.

## Probability in the classically forbidden region

**Turning points.** Classically, energy $E_n$ confines the particle to $|\xi|\le\sqrt{2n+1}$.

**Ground state** (Griffiths Problem 2.14):

$$
P_{\text{out}} = \frac{1}{\sqrt\pi}\int_{|\xi|>1}e^{-\xi^2}d\xi = \operatorname{erfc}(1) = 0.157299 .
$$

**Excited states** (computed here, beyond Griffiths):

| $n$ | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| $P_{\text{out}}$ | 0.1573 | 0.1116 | 0.0951 | 0.0855 |

The forbidden-region probability shrinks slowly with $n$, consistent with the approach to classical behaviour.

## Worked example

!!! example "Three independent routes to the same spectrum ($\hbar=m=\omega=1$)"
    1. **Recursion.** Running the recursion with $K=2n+1$ and scaling to leading coefficient $2^n$ reproduces the integer coefficients of $H_0,\ldots,H_6$ exactly.
    2. **Shooting** ("wag the dog", Griffiths Problems 2.55-2.56). Integrate $\psi''=(\xi^2-K)\psi$ from $\xi=0$ to $6$, with $(\psi,\psi') = (1,0)$ for even states or $(0,1)$ for odd states. Bisecting on $K$ for a zero tail gives $K = 1.0000000,\ 3.0000000,\ 5.0000000,\ 7.0000000$.
    3. **Finite differences.** On $[-10,10]$ with $\Delta x = 0.005$, the lowest six eigenvalues are $0.499999,\ 1.499996,\ 2.49999,\ 3.49998,\ 4.499968,\ 5.499952$. The error grows with $n$ as $O(n^2\Delta x^2)$.

## Note for quantum chemists

$e^{-\alpha x^2}$ times a polynomial is exactly the Cartesian Gaussian form used for basis functions ([[gaussian-basis-functions]]). The oscillator eigenfunctions are the case where such functions are exact eigenstates. Hermite polynomials also appear in the Hermite Gaussians of the McMurchie–Davidson integral scheme ([[electron-repulsion-integrals-md-os-rys]]).

## Source

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Sec. 2.3.2, Eqs. (2.71)-(2.90), Table 2.1, Figs. 2.6-2.7 (described, not reproduced); Problems 2.14-2.16, 2.55, 2.56; footnotes 32, 35, 36. Page numbers are not given because the PDF used is an e-book rendering without print pagination. The excited-state forbidden-region probabilities and the remark on Gaussian basis functions are additions. Numbers recomputed with `griffiths/ch02_tise.py` (section D).
