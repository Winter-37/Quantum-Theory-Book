---
id: gaussian-overlap-distributions-and-one-electron-integrals
title: Gaussian overlap distributions and one-electron integrals - the product rule, Obara-Saika and McMurchie-Davidson recurrences, Hermite Gaussians and Gauss-Hermite quadrature
summary: Contracted spherical-harmonic GTOs are evaluated through primitive Cartesian Gaussians, which factorize in x, y and z. The Gaussian product rule turns a pair of Gaussians into a single Gaussian at the weighted centre P. Three routes to overlap, multipole, kinetic and nuclear-attraction integrals follow from it: Obara-Saika recurrences, McMurchie-Davidson expansion in Hermite Gaussians, and Gauss-Hermite quadrature. My own implementation of all three agrees with PySCF/libcint to 10⁻¹⁵-10⁻¹³.
status: in-progress
kind: algorithm
level: advanced
tags: [molecular-integrals, gaussian-product-rule, obara-saika, mcmurchie-davidson, hermite-gaussians, overlap-integrals, kinetic-energy-integrals, multipole-integrals, gauss-hermite-quadrature, cartesian-gaussians]
prerequisites: [gaussian-basis-functions, solid-harmonics-angular-basis]
related: [electron-repulsion-integrals-md-os-rys, multipole-methods-and-integral-screening, integral-notation, radial-basis-functions-slater-and-gaussian]
order: 70
date: 2026-11-04
---

## From contracted spherical GTOs to Cartesian primitives

**What the program works with (HJO Sec. 9.1).** A contracted spherical-harmonic GTO is

$$
\chi_{lm}(\mathbf r) = \sum_kd_k\,N_k\,S_{lm}(\mathbf r_A)\,e^{-\alpha_kr_A^2},
$$

with $S_{lm}$ the real solid harmonics of [[solid-harmonics-angular-basis]]. $S_{lm}$ is a fixed linear combination of the Cartesian monomials $x_A^iy_A^jz_A^k$ ($i + j + k = l$).

**The standard order of operations.**

1. Compute integrals over **primitive Cartesian** Gaussians $G_{ijk}(\alpha,\mathbf A) = x_A^iy_A^jz_A^ke^{-\alpha r_A^2}$.
2. Contract them.
3. Transform to spherical harmonics.

Each step costs fewer operations the later it is done in a recursion. Exponent-independent steps, such as the horizontal recurrences of [[electron-repulsion-integrals-md-os-rys]], can be moved after contraction.

**Separability.** $G_{ijk} = G_i(x)G_j(y)G_k(z)$ with $G_i(x) = x_A^ie^{-\alpha x_A^2}$. Every one-electron integral of a separable operator is a product of three one-dimensional integrals. Derivatives obey two-term relations:

$$
\frac{\partial G_i}{\partial A_x} = 2\alpha G_{i+1} - iG_{i-1} = -\frac{\partial G_i}{\partial x},\qquad x_AG_i = G_{i+1}.
$$

## The Gaussian product rule

**Rule.** Two Gaussians on different centres multiply to one Gaussian on the line between them:

$$
e^{-ax_A^2}e^{-bx_B^2} = K^{ab}_x\,e^{-px_P^2},\qquad
p = a + b,\quad \mu = \frac{ab}{a+b},\quad P_x = \frac{aA_x + bB_x}{p},\quad K^{ab}_x = e^{-\mu X_{AB}^2} .
$$

**Overlap distribution.** $\Omega_{ij}(x) = G_i(x,a,A_x)G_j(x,b,B_x)$ is a polynomial of degree $i + j$ times this single Gaussian.

**Consequences.**

- **Size.** Its extent is set by $p$, its magnitude by $K^{ab}$, which decays as the square of the separation. This is the root of the linear scaling of overlap-type integrals ([[multipole-methods-and-integral-screening]]).
- **Check.** I verified the rule numerically to $3\times10^{-17}$.

## Obara-Saika recurrences

**Overlap (HJO Eqs. 9.3.8-9.3.9).** Write $S_{ij} = \langle G_i|G_j\rangle$ in one dimension:

$$
S_{i+1,j} = X_{PA}S_{ij} + \frac1{2p}\big(iS_{i-1,j} + jS_{i,j-1}\big),\qquad
S_{i,j+1} = X_{PB}S_{ij} + \frac1{2p}\big(iS_{i-1,j} + jS_{i,j-1}\big),\qquad
S_{00} = \sqrt{\frac\pi p}\,e^{-\mu X_{AB}^2}.
$$

The 3D overlap is $S_{ij}S_{kl}S_{mn}$.

**Derivation idea.** Shifting both centres by the same amount leaves $S_{ij}$ unchanged, so $(\partial_{A_x}+\partial_{B_x})S_{ij} = 0$. With $\partial_AG_i = 2aG_{i+1} - iG_{i-1}$ this gives $2aS_{i+1,j} - iS_{i-1,j} + 2bS_{i,j+1} - jS_{i,j-1} = 0$ (HJO 9.3.6), and eliminating $S_{i,j+1}$ with $S_{i,j+1} = S_{i+1,j} + X_{AB}S_{ij}$ yields the first recurrence.

**Multipole moments.** Integrals over $x_C^e$ follow by adding a third index (HJO Sec. 9.3.2, Eqs. 9.3.11-9.3.17). One convenient form, which I checked numerically to $10^{-16}$, raises the multipole order: $M^{e+1}_{ij} = X_{PC}M^e_{ij} + (iM^e_{i-1,j} + jM^e_{i,j-1} + eM^{e-1}_{ij})/(2p)$.

**Kinetic energy.** Either use $\partial_x^2G_j = j(j-1)G_{j-2} - 2b(2j+1)G_j + 4b^2G_{j+2}$ (as my code does), or HJO's Obara-Saika recurrence (Eqs. 9.3.40-9.3.42; I checked the first numerically to $6\times10^{-17}$):

$$
T_{i+1,j} = X_{PA}T_{ij} + \frac1{2p}\big(iT_{i-1,j} + jT_{i,j-1}\big) + \frac bp\big(2aS_{i+1,j} - iS_{i-1,j}\big),\qquad
T_{00} = \Big[a - 2a^2\Big(X_{PA}^2 + \frac1{2p}\Big)\Big]S_{00}.
$$

Then

$$
T = T_{ij}S_{kl}S_{mn} + S_{ij}T_{kl}S_{mn} + S_{ij}S_{kl}T_{mn}.
$$

## Hermite Gaussians and the McMurchie-Davidson scheme

**Hermite Gaussians (HJO Sec. 9.4).** $\Lambda_t(x) = (\partial/\partial P_x)^te^{-px_P^2}$, a Hermite polynomial times the Gaussian. Their key property is that only $t = 0$ survives integration:

$$
\int\Lambda_t\,\mathrm dx = \delta_{t0}\sqrt{\pi/p}.
$$

**Expansion of overlap distributions (HJO Eqs. 9.5.1 and 9.5.6-9.5.8).**

$$
\Omega_{ij}(x) = \sum_{t=0}^{i+j}E^{ij}_t\Lambda_t(x),\qquad
E^{i+1,j}_t = \frac1{2p}E^{ij}_{t-1} + X_{PA}E^{ij}_t + (t+1)E^{ij}_{t+1},\qquad E^{00}_0 = K^{ab}_x,
$$

with the analogous relation for $j + 1$ (using $X_{PB}$) and $E^{ij}_t = 0$ outside $0\le t\le i + j$.

**Integrals from the coefficients.**

- **Overlap.** $S_{ij} = E^{ij}_0\sqrt{\pi/p}$.
- **Multipoles.** These are short sums, e.g. $\langle x_C\rangle = (E^{ij}_1 + X_{PC}E^{ij}_0)\sqrt{\pi/p}$.
- **Nuclear attraction.** $V = \frac{2\pi}{p}\sum_{tuv}E^{ij}_tE^{kl}_uE^{mn}_vR_{tuv}(p,\mathbf R_{PC})$, with the Hermite Coulomb integrals $R_{tuv}$ built from the Boys function ([[electron-repulsion-integrals-md-os-rys]]).

The Hermite expansion is done once per pair. Every operator then needs only the integrals over $\Lambda_t$.

## Gauss-Hermite quadrature

**Exact quadrature (HJO Sec. 9.6).** $\Omega_{ij}$ is a polynomial of degree $i + j$ times $e^{-px_P^2}$. $n$-point Gauss-Hermite quadrature, exact for polynomials of degree $2n - 1$, therefore integrates it exactly as soon as $n > (i+j)/2$:

$$
S_{ij} = \frac{K^{ab}_x}{\sqrt p}\sum_{k=1}^nw_k\,(x_k - A_x)^i(x_k - B_x)^j,\qquad x_k = P_x + t_k/\sqrt p .
$$

**Same machinery for ERIs.** The Rys scheme for two-electron integrals applies this idea with a different weight function ([[electron-repulsion-integrals-md-os-rys]]).

## Checks

!!! example "Own one-electron integral code versus PySCF/libcint (computed for this note)"
    **Test set.** 13 Cartesian functions: one primitive each, an $s$ on H, a $p$ on He, a $d$ on Li and a $p$ on Be, at non-symmetric positions. PySCF normalizes each Cartesian component differently, so I rescaled each function by $\sqrt{S^{\text{ref}}_{\mu\mu}/S^{\text{raw}}_{\mu\mu}}$ before comparing.

    | Integral | Method | Max deviation |
    |---|---|---:|
    | Overlap | Obara-Saika | $8.9\times10^{-16}$ |
    | Kinetic | Obara-Saika + second derivatives | $1.8\times10^{-15}$ |
    | Nuclear attraction | McMurchie-Davidson | $2.3\times10^{-13}$ |

    **One-dimensional checks** ($a = 0.9$, $b = 0.4$, $A = 0.3$, $B = -0.7$, $i = 3$, $j = 2$; reference is numerical quadrature):

    - **Overlap.** OS gives $S_{32} = 0.18944921454$. MD ($E_0\sqrt{\pi/p}$) agrees to $2\times10^{-16}$.
    - **Moments.** The first and second moments about $C = 0.25$ from the $E^{ij}_t$ agree to $10^{-15}$. For the second moment I used $\big[(X_{PC}^2 + \tfrac1{2p})E_0 + 2X_{PC}E_1 + 2E_2\big]\sqrt{\pi/p}$, which I derived from the moments of $\Lambda_t$.
    - **Gauss-Hermite.** With $n = 2$ the error is 0.16; with $n = 3$ ($> 5/2$) it is exact ($6\times10^{-17}$).

    Code: `ints.py` (functions `os_overlap_1d`, `kinetic`, `E_coef`, `nuclear_md`), kept in `hjo/c69/` of my working files.

```python
def E_coef(i, j, a, b, A, B):        # McMurchie-Davidson Hermite coefficients E^{ij}_t, HJO (9.5.6)-(9.5.8)
    p = a + b; mu = a*b/p; P = (a*A + b*B)/p; XPA, XPB = P - A, P - B
    E = np.zeros((i + 1, j + 1, i + j + 2)); E[0, 0, 0] = exp(-mu*(A - B)**2)
    for ii in range(i + 1):
        for jj in range(j + 1):
            if ii == 0 and jj == 0: continue
            for t in range(ii + jj + 1):
                if ii > 0: v = XPA*E[ii-1, jj, t] + (t+1)*E[ii-1, jj, t+1] + (E[ii-1, jj, t-1]/(2*p) if t else 0)
                else:      v = XPB*E[ii, jj-1, t] + (t+1)*E[ii, jj-1, t+1] + (E[ii, jj-1, t-1]/(2*p) if t else 0)
                E[ii, jj, t] = v
    return E[i, j]
```

## Source

Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, Chichester, 2000), Secs. 9.1-9.6, pp. 336-361, Eqs. (9.1.1)-(9.6.40). Equations read from the text extraction and page images. Implementation and checks (NumPy, SciPy, PySCF 2.14) done for this note.
