---
id: solid-harmonics-angular-basis
title: The angular part of atomic basis functions - central-field separation, spherical and real solid harmonics, Cartesian expressions and recurrences
summary: In a central field the one-electron functions factor into a radial part and a spherical harmonic, so the angular part of every atomic basis function is universal. Scaling by r^l gives solid harmonics, polynomials in x, y, z. HJO's real solid harmonics S_lm (Condon-Shortley phases) have an explicit Cartesian formula and diagonal plus vertical recurrences. Both were implemented and checked against the spherical-harmonic definition through l = 6, together with the low-order forms and the counting of 2l+1 spherical versus (l+1)(l+2)/2 Cartesian components.
status: in-progress
kind: derivation
level: intermediate
tags: [spherical-harmonics, solid-harmonics, angular-momentum, basis-functions, cartesian-gaussians, recurrence-relations]
prerequisites: [gaussian-basis-functions]
related: [radial-basis-functions-slater-and-gaussian, gaussian-overlap-distributions-and-one-electron-integrals, multipole-methods-and-integral-screening]
also: [02_Quantum_Mechanics/04_Angular_Momentum_and_Spin, 00_Mathematics/Linear_Algebra]
date: 2026-11-04
---

## Why the angular part is universal

**Separation.** For a central field $V(r)$, the Hamiltonian $-\tfrac12\nabla^2 + V(r)$ commutes with $\hat L^2$ and $\hat L_z$. The Laplacian in polar coordinates separates into a radial operator and $-\hat L^2/r^2$, so the solutions are $\psi_{nlm} = R_{nl}(r)Y_{lm}(\theta,\varphi)$, where $R_{nl}$ satisfies the radial equation

$$
\Big[-\frac12\frac{\mathrm d^2}{\mathrm dr^2} + \frac{l(l+1)}{2r^2} + V(r)\Big]\big(rR_{nl}\big) = E\,\big(rR_{nl}\big).
$$

**Consequences.**

- **Same angular functions everywhere.** The angular functions are the spherical harmonics for **any** $V(r)$.
- **Radial functions depend on $l$** (through the centrifugal term). Radial functions with different $l$ are not mutually orthogonal: they come from different effective Hamiltonians.
- **Completeness.** Complete radial sets in $L^2(\mathbb R^+, r^2)$ times the complete set $Y_{lm}$ on the sphere give a complete set in $L^2(\mathbb R^3)$. All basis functions in HJO are of this product form; they differ only in the radial part ([[radial-basis-functions-slater-and-gaussian]]).

## Solid harmonics

**Definition.** Multiplying by $r^l$ turns a spherical harmonic into a homogeneous polynomial of degree $l$ in $x$, $y$, $z$: the solid harmonic $\mathcal Y_{lm}(\mathbf r) = r^lY_{lm}$. It still satisfies the angular-momentum eigenvalue equations, since $\hat L^2$ and $\hat L_z$ commute with $r$. Properties: $\mathcal Y_{lm}(-\mathbf r) = (-1)^l\mathcal Y_{lm}(\mathbf r)$ and $\mathcal Y_{lm}^* = (-1)^m\mathcal Y_{l,-m}$.

**Real solid harmonics (HJO Eqs. 6.4.19-6.4.21).** Molecules lack spherical symmetry, so nothing is gained from complex functions. HJO define

$$
S_{l0} = \sqrt{\frac{4\pi}{2l+1}}\,\mathcal Y_{l0},\qquad
S_{lm} = (-1)^m\sqrt{\frac{8\pi}{2l+1}}\,\mathrm{Re}\,\mathcal Y_{lm},\qquad
S_{l,-m} = (-1)^m\sqrt{\frac{8\pi}{2l+1}}\,\mathrm{Im}\,\mathcal Y_{lm}\qquad(m>0),
$$

a unitary transform of Racah-normalized complex harmonics. Low orders:

| $l$ | Real solid harmonics |
|---|---|
| 0 | $1$ |
| 1 | $x$, $y$, $z$ |
| 2 | $\tfrac12(3z^2 - r^2)$, $\sqrt3\,xz$, $\sqrt3\,yz$, $\tfrac{\sqrt3}2(x^2 - y^2)$, $\sqrt3\,xy$ |
| 3 | e.g. $S_{3,-2} = \sqrt{15}\,xyz$ |

**Explicit Cartesian form (HJO Eqs. 6.4.47-6.4.50).**

$$
S_{lm} = N_{lm}^{\mathrm S}\sum_{t=0}^{\lfloor(l-|m|)/2\rfloor}\sum_{u=0}^t\sum_{v=v_m}^{\lfloor|m|/2-v_m\rfloor+v_m}C_{tuv}^{lm}\,x^{2t+|m|-2(u+v)}y^{2(u+v)}z^{l-2t-|m|},
$$

$$
C_{tuv}^{lm} = (-1)^{t+v-v_m}\Big(\frac14\Big)^t\binom lt\binom{l-t}{|m|+t}\binom tu\binom{|m|}{2v},\qquad
N_{lm}^{\mathrm S} = \frac1{2^{|m|}l!}\sqrt{\frac{2(l+|m|)!(l-|m|)!}{2^{\delta_{m0}}}},
$$

with $v_m = 0$ for $m\ge0$ and $\tfrac12$ for $m<0$. It comes from expanding $(x^2+y^2)^t$ and the real and imaginary parts of $(x + iy)^{|m|}$ binomially.

**Recurrences (HJO Sec. 6.4.5, scale factors $n_{lm} = 1$).**

- **Diagonal ($l$ and $|m|$ together):**

$$
S_{l+1,l+1} = \sqrt{\frac{2^{\delta_{l0}}(2l+1)}{2l+2}}\big[xS_{ll} - (1-\delta_{l0})yS_{l,-l}\big],\qquad
S_{l+1,-l-1} = \sqrt{\frac{2^{\delta_{l0}}(2l+1)}{2l+2}}\big[yS_{ll} + (1-\delta_{l0})xS_{l,-l}\big].
$$

- **Vertical ($m$ fixed):**

$$
S_{lm} = \frac{(2l-1)\,zS_{l-1,m} - \sqrt{(l+|m|-1)(l-|m|-1)}\,r^2S_{l-2,m}}{\sqrt{(l+|m|)(l-|m|)}} .
$$

  Recursion is the efficient way to generate all harmonics up to some $l$. HJO reuse it, with scaled harmonics, for multipole expansions ([[multipole-methods-and-integral-screening]]).

!!! example "Checks (computed for this note)"
    At 2000 random points, for all $l\le6$ and every $m$:

    - the explicit formula and the recurrences reproduce the defining expressions in terms of `scipy`'s Condon-Shortley spherical harmonics to $5\times10^{-12}$ (relative to values of order $r^6$);
    - the low-order forms in the table hold to $10^{-14}$.

## Spherical versus Cartesian components

A shell of angular momentum $l$ has $2l + 1$ spherical (solid-harmonic) functions but $(l+1)(l+2)/2$ Cartesian monomials $x^iy^jz^k$ with $i + j + k = l$:

| $l$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Spherical | 1 | 3 | 5 | 7 | 9 | 11 | 13 |
| Cartesian | 1 | 3 | 6 | 10 | 15 | 21 | 28 |

**Contaminants.** The extra Cartesian combinations are lower-$l$ functions times $r^2$: a $d$ shell's six Cartesians contain an $s$-type $x^2 + y^2 + z^2$, an $f$ shell's ten contain three $p$-type functions. HJO recommend spherical-harmonic GTOs, which are more compact. Integrals are nevertheless computed over Cartesians (separable, Gaussian product rule) and transformed afterwards ([[gaussian-overlap-distributions-and-one-electron-integrals]]); PySCF's `cart2sph` matrices map 6→5, 10→7, 15→9.

## Source

Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, Chichester, 2000), Secs. 6.3-6.4, pp. 204-218, Eqs. (6.3.1)-(6.4.70), Table 6.3. Equations read from the page images. Checks computed with NumPy and SciPy (`sph_harm_y`).
