---
id: central-potentials-and-spherical-harmonics
title: Central potentials, spherical harmonics and the radial equation
summary: Separation of the Schrödinger equation for V(r) in spherical coordinates. The angular equation gives Legendre and associated Legendre functions and spherical harmonics Y_ℓ^m (Griffiths phase convention, checked to equal the Condon–Shortley Y of SymPy/SciPy). The radial equation for u = rR has an effective potential with a centrifugal term. Examples: the infinite spherical well (zeros of spherical Bessel functions, level ordering, 2ℓ+1 degeneracy), the finite spherical well's threshold for binding, and reconstructing V from a given ψ.
status: in-progress
kind: derivation
level: intermediate
tags: [central-potential, spherical-coordinates, spherical-harmonics, legendre-polynomials, associated-legendre, radial-equation, effective-potential, spherical-bessel, condon-shortley, griffiths]
prerequisites: [schrodinger-equation-in-three-dimensions, eigenfunctions-of-hermitian-operators]
related: [orbital-angular-momentum, hydrogen-atom, solid-harmonics-angular-basis, radial-basis-functions-slater-and-gaussian]
also: []
date: 2026-11-04
---

## Separation

**Laplacian.** In spherical coordinates $(r,\theta,\phi)$ ($\theta$ polar, $\phi$ azimuthal):

$$
\nabla^2 = \frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2\frac{\partial}{\partial r}\right) + \frac{1}{r^2\sin\theta}\frac{\partial}{\partial\theta}\left(\sin\theta\frac{\partial}{\partial\theta}\right) + \frac{1}{r^2\sin^2\theta}\frac{\partial^2}{\partial\phi^2}.
$$

**Ansatz.** For a central potential $V(r)$, put $\psi = R(r)\,Y(\theta,\phi)$ into the TISE and multiply by $-2mr^2/\hbar^2\psi$. The radial and angular parts separate, with separation constant written as $\ell(\ell+1)$:

$$
\frac{1}{R}\frac{d}{dr}\left(r^2\frac{dR}{dr}\right) - \frac{2mr^2}{\hbar^2}[V-E] = \ell(\ell+1),
$$

$$
\frac{1}{Y}\left[\frac{1}{\sin\theta}\frac{\partial}{\partial\theta}\left(\sin\theta\frac{\partial Y}{\partial\theta}\right)+\frac{1}{\sin^2\theta}\frac{\partial^2Y}{\partial\phi^2}\right] = -\ell(\ell+1).
$$

The angular equation does not contain $V$. Every central potential shares the same angular functions, which is why atomic basis functions all have the same angular parts ([[solid-harmonics-angular-basis]]).

## The angular equation

**Azimuthal part.** A second separation, $Y = \Theta(\theta)\Phi(\phi)$, with constant $m^2$, gives $\Phi = e^{im\phi}$. Single-valuedness, $\Phi(\phi+2\pi) = \Phi(\phi)$, forces

$$
m = 0,\pm1,\pm2,\ldots
$$

**Polar part.** $\sin\theta\,(\sin\theta\,\Theta')' + [\ell(\ell+1)\sin^2\theta - m^2]\Theta = 0$. Its regular solution is the associated Legendre function $\Theta = P_\ell^m(\cos\theta)$, with (Griffiths's definitions, $m\ge0$)

$$
P_\ell(x) = \frac{1}{2^\ell\ell!}\left(\frac{d}{dx}\right)^\ell(x^2-1)^\ell,
\qquad
P_\ell^m(x) = (-1)^m(1-x^2)^{m/2}\left(\frac{d}{dx}\right)^mP_\ell(x).
$$

**Quantization.** The Rodrigues formula requires $\ell$ to be a non-negative integer, and $P_\ell^m = 0$ for $m>\ell$. Hence

$$
\ell = 0,1,2,\ldots,\qquad m = -\ell,\ldots,\ell\quad(2\ell+1\text{ values}).
$$

The second solution of the $\theta$ equation blows up at $\theta = 0$ or $\pi$. For example $\ln\tan(\theta/2)$ for $\ell=m=0$ (Problem 4.5).

**Legendre orthogonality** (Problem 4.8):

$$
\int_{-1}^1P_\ell P_{\ell'}\,dx = \frac{2}{2\ell+1}\delta_{\ell\ell'}.
$$

**Spherical harmonics.** With $d^3\mathbf r = r^2dr\,d\Omega$ and $d\Omega = \sin\theta\,d\theta\,d\phi$, normalize the radial and angular parts separately ($\int|R|^2r^2dr = 1$, $\int|Y|^2d\Omega = 1$):

$$
Y_\ell^m(\theta,\phi) = \sqrt{\frac{2\ell+1}{4\pi}\frac{(\ell-m)!}{(\ell+m)!}}\;e^{im\phi}P_\ell^m(\cos\theta),
\qquad
Y_\ell^{-m} = (-1)^m\left(Y_\ell^m\right)^*,
$$

$$
\int\left(Y_\ell^m\right)^*Y_{\ell'}^{m'}\,d\Omega = \delta_{\ell\ell'}\delta_{mm'} .
$$

Examples:

$$
Y_0^0 = \frac{1}{\sqrt{4\pi}},\quad Y_1^0 = \sqrt{\frac{3}{4\pi}}\cos\theta,\quad Y_1^{\pm1} = \mp\sqrt{\frac{3}{8\pi}}\sin\theta\,e^{\pm i\phi},\quad Y_2^{\pm1} = \mp\sqrt{\frac{15}{8\pi}}\sin\theta\cos\theta\,e^{\pm i\phi}.
$$

**Phase convention.** In Griffiths the $(-1)^m$ sits inside $P_\ell^m$. The resulting $Y_\ell^m$ coincide with the Condon–Shortley spherical harmonics of SymPy (`Ynm`) and SciPy (`sph_harm_y`): the maximum difference is $3\times10^{-16}$ for $\ell\le4$ at test points. Numerical orthonormality of the 16 functions with $\ell\le3$ holds to $2\times10^{-14}$. Other books move the sign into $Y$ or drop it, so check before mixing formulas.

## The radial equation

**Reduction to 1D.** Put $u(r) = rR(r)$:

$$
-\frac{\hbar^2}{2m}\frac{d^2u}{dr^2} + \left[V(r)+\frac{\hbar^2}{2m}\frac{\ell(\ell+1)}{r^2}\right]u = Eu,
\qquad\int_0^\infty|u|^2dr = 1,\qquad u(0)=0 .
$$

This is a 1D problem on the half-line, with an **effective potential** that includes the repulsive centrifugal term. The energy depends on $\ell$ but not on $m$. Every central potential therefore has at least $(2\ell+1)$-fold degeneracy. More than that is "accidental" (hydrogen, 3D oscillator) and signals a hidden symmetry (Griffiths Ch. 6).

**Behaviour at the origin.** As $r\to0$ the centrifugal term dominates (if $V$ is less singular than $1/r^2$), so $u\sim r^{\ell+1}$ and $R\sim r^\ell$.

## Infinite spherical well (Griffiths Example 4.1, Problem 4.10)

**Radial solutions.** With $V = 0$ for $r<a$ and $k = \sqrt{2mE}/\hbar$, the regular solution is $R = j_\ell(kr)$, a spherical Bessel function:

$$
j_\ell(x) = (-x)^\ell\left(\frac{1}{x}\frac{d}{dx}\right)^\ell\frac{\sin x}{x},\qquad
j_0 = \frac{\sin x}{x},\quad j_1 = \frac{\sin x}{x^2}-\frac{\cos x}{x}.
$$

The Neumann functions $n_\ell$ blow up at the origin and are discarded.

**Quantization.** $j_\ell(ka) = 0$ gives $k = \beta_{N\ell}/a$, where $\beta_{N\ell}$ is the $N$th zero of $j_\ell$:

$$
E_{N\ell} = \frac{\hbar^2}{2ma^2}\beta_{N\ell}^2,\qquad\text{degeneracy }2\ell+1 .
$$

For $\ell=0$, $\beta = N\pi$, exactly the 1D well.

!!! example "Level ordering (energies in $\hbar^2/2ma^2$)"
    | $E$ | 9.8696 | 20.1907 | 33.2175 | 39.4784 | 48.8312 | 59.6795 | 66.9543 | 82.7192 | 88.8264 |
    |---|---|---|---|---|---|---|---|---|---|
    | $(N,\ell)$ | (1,0) | (1,1) | (1,2) | (2,0) | (1,3) | (2,1) | (1,4) | (2,2) | (3,0) |
    | Degeneracy | 1 | 3 | 5 | 1 | 7 | 3 | 9 | 5 | 1 |

    The levels interleave in $\ell$, unlike hydrogen, where all $\ell<n$ share one energy. This ordering ($1s, 1p, 1d, 2s, 1f, 2p, \ldots$) is the starting point of the nuclear shell model.

    **Large $N$** (Problem 4.10). For $\ell=1$, $\beta_{N1}\to(N+\tfrac12)\pi$. The values $\beta^2$ are 20.19, 296.55 and 4145.70 for $N = 1, 5, 20$, against $(N+\tfrac12)^2\pi^2$ = 22.21, 298.56 and 4147.70. The difference tends to 2.

## Finite spherical well (Problem 4.11)

**Mapping to 1D.** For $\ell = 0$, $u$ obeys the 1D equation on $r>0$ with $u(0) = 0$. These are exactly the *odd* states of a 1D finite well of half-width $a$ ([[finite-square-well]]).

**Threshold.** The first odd state appears at $z_0 = \pi/2$, so a 3D well binds only if

$$
V_0a^2 > \frac{\pi^2\hbar^2}{8m}.
$$

Unlike 1D, a weak enough 3D well has *no* bound state.

**Numbers** ($\hbar=m=a=1$, threshold 1.2337): no bound state at $V_0 = 1.2$; $E = -0.00212$ at $V_0 = 1.3$; $E = -6.7791$ at $V_0 = 10$.

## Reading V from ψ (Problem 4.3)

With $\hbar = m = 1$, require $V\to0$ at infinity (first case) or $V(0) = 0$ (second case).

| $\psi$ | $V(r)$ | $E$ |
|---|---|---|
| $Ae^{-r/a}$ | $-\hbar^2/(mar)$ (Coulomb-like) | $-\hbar^2/2ma^2$ |
| $Ae^{-r^2/a^2}$ | $2\hbar^2r^2/(ma^4)$ (oscillator) | $3\hbar^2/ma^2$ |

The second is the 3D oscillator ground state, $E = \tfrac32\hbar\omega$ with $\omega = 2\hbar/ma^2$.

## Source

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Secs. 4.1.1-4.1.3, Eqs. (4.13)-(4.51), Tables 4.1-4.4, Example 4.1, Figs. 4.2-4.3 (described); Problems 4.3-4.11. Page numbers are not given because the PDF used is an e-book rendering without print pagination. The phase-convention comparison, the level table, the threshold numbers and the shell-model remark are additions computed in `griffiths/ch04_3d.py` (section B).
