---
id: hydrogen-atom
title: The hydrogen atom
summary: Full solution of the hydrogen radial equation by power series. Covers asymptotics, the recursion, termination giving the Bohr formula E_n = −13.6 eV/n², the Bohr radius, radial functions via associated Laguerre polynomials (3rd-edition normalization, checked against the book's table for n ≤ 4), the n² degeneracy, nodes, the moments ⟨r⟩, ⟨r²⟩, ⟨1/r⟩, the spectrum (Rydberg formula, Lyman/Balmer/Paschen, reduced-mass correction) and hydrogenic ions. Verified symbolically and by finite differences.
status: in-progress
kind: derivation
level: intermediate
tags: [hydrogen-atom, coulomb-potential, bohr-formula, bohr-radius, laguerre-polynomials, radial-wave-functions, degeneracy, rydberg, spectrum, hydrogenic-ions, griffiths]
prerequisites: [central-potentials-and-spherical-harmonics, harmonic-oscillator-analytic-solution]
related: [orbital-angular-momentum, atomic-units, radial-basis-functions-slater-and-gaussian, hellmann-feynman-and-virial-theorems, coulomb-cusp-and-helium-expansions]
also: [03_Quantum_Chemistry/01_Atomic_Structure]
date: 2026-11-04
---

## Setup

**Model.** A proton is fixed at the origin and an electron (mass $m_e$, charge $-e$) moves in the Coulomb potential. The radial equation for $u = rR$ is

$$
-\frac{\hbar^2}{2m_e}\frac{d^2u}{dr^2} + \left[-\frac{e^2}{4\pi\epsilon_0}\frac1r + \frac{\hbar^2}{2m_e}\frac{\ell(\ell+1)}{r^2}\right]u = Eu .
$$

**Bound and scattering states.** For $E<0$ the states are bound. $E>0$ gives electron–proton scattering, which is not treated here.

**Reduced mass.** The proton's finite mass is accounted for by replacing $m_e$ with the reduced mass $\mu = m_em_p/(m_e+m_p)$ (see the spectrum table below).

## Solution by power series

**Dimensionless form.** Set

$$
\kappa = \frac{\sqrt{-2m_eE}}{\hbar},\qquad \rho = \kappa r,\qquad \rho_0 = \frac{m_ee^2}{2\pi\epsilon_0\hbar^2\kappa}.
$$

Then

$$
\frac{d^2u}{d\rho^2} = \left[1-\frac{\rho_0}{\rho}+\frac{\ell(\ell+1)}{\rho^2}\right]u .
$$

**Asymptotics.** As $\rho\to\infty$, $u\sim e^{-\rho}$; the $e^{+\rho}$ branch is discarded. As $\rho\to0$, $u\sim\rho^{\ell+1}$; the $\rho^{-\ell}$ branch is discarded. Peel off both behaviours:

$$
u = \rho^{\ell+1}e^{-\rho}v(\rho)
\quad\Longrightarrow\quad
\rho v'' + 2(\ell+1-\rho)v' + [\rho_0-2(\ell+1)]v = 0 .
$$

**Recursion.** With $v = \sum_jc_j\rho^j$:

$$
c_{j+1} = \frac{2(j+\ell+1)-\rho_0}{(j+1)(j+2\ell+2)}\,c_j .
$$

**Termination.** For large $j$, $c_{j+1}\approx 2c_j/(j+1)$, so $v\approx c_0e^{2\rho}$ and $u\sim\rho^{\ell+1}e^{+\rho}$, which is not normalizable. The series must stop. If $c_{N-1}\neq0$ and $c_N = 0$, then $2(N+\ell) = \rho_0$. Define the **principal quantum number** $n = N+\ell$:

$$
\rho_0 = 2n
\quad\Longrightarrow\quad
E_n = -\left[\frac{m_e}{2\hbar^2}\left(\frac{e^2}{4\pi\epsilon_0}\right)^2\right]\frac{1}{n^2} = \frac{E_1}{n^2},\qquad n = 1,2,3,\ldots
$$

This is the **Bohr formula**. Moreover

$$
\kappa = \frac{1}{an},\qquad a = \frac{4\pi\epsilon_0\hbar^2}{m_ee^2},\qquad \rho = \frac{r}{an}.
$$

**Values** (CODATA via SciPy, infinite proton mass): $E_1 = -13.605693$ eV and $a = 0.529177$ Å. In [[atomic-units]] these are $E_n = -1/2n^2$ hartree and $a = 1$ bohr.

## Wave functions

**Normalized eigenfunctions.**

$$
\psi_{n\ell m} = \sqrt{\left(\frac{2}{na}\right)^3\frac{(n-\ell-1)!}{2n\,(n+\ell)!}}\;e^{-r/na}\left(\frac{2r}{na}\right)^\ell\left[L_{n-\ell-1}^{2\ell+1}\!\left(\frac{2r}{na}\right)\right]Y_\ell^m(\theta,\phi).
$$

**Laguerre convention.** The 3rd edition uses

$$
L_q(x) = \frac{e^x}{q!}\frac{d^q}{dx^q}\left(e^{-x}x^q\right),\qquad L_q^p(x) = (-1)^p\frac{d^p}{dx^p}L_{p+q}(x),
$$

the modern convention, the same as SciPy's `genlaguerre`. Older texts, including the 2nd edition of Griffiths, use unnormalized Laguerre polynomials and a correspondingly different prefactor, so do not mix formulas between editions.

**Check.** The radial part of the formula above was evaluated symbolically and agrees *exactly* with Griffiths Table 4.7 for every $(n,\ell)$ with $n\le4$. For example:

$$
R_{10} = \frac{2}{a^{3/2}}e^{-r/a},\qquad
R_{20} = \frac{1}{\sqrt2\,a^{3/2}}\left(1-\frac{r}{2a}\right)e^{-r/2a},\qquad
R_{21} = \frac{1}{2\sqrt6\,a^{3/2}}\frac{r}{a}e^{-r/2a}.
$$

**Ground state.**

$$
\psi_{100} = \frac{1}{\sqrt{\pi a^3}}\,e^{-r/a}.
$$

Its radial density $r^2|R_{10}|^2\propto r^2e^{-2r/a}$ peaks at $r=a$ (Problem 4.16). This is the most probable radius, distinct from $\langle r\rangle = 3a/2$.

**Degeneracy.** For given $n$, $\ell = 0,\ldots,n-1$ and $m = -\ell,\ldots,\ell$, so

$$
d(n) = \sum_{\ell=0}^{n-1}(2\ell+1) = n^2,
$$

or $2n^2$ with spin. Energy is independent of $\ell$. This extra degeneracy, beyond $2\ell+1$, comes from a hidden symmetry: the conserved Laplace–Runge–Lenz vector (Griffiths Ch. 6).

**Nodes.**

- Radial nodes: $n-\ell-1$.
- Conical nodes in $\theta$: $\ell-m$.
- Planes of $\mathrm{Re}\,\psi$ or $\mathrm{Im}\,\psi$ in $\phi$: $m$.

**Orthonormality.** $\int\psi_{n\ell m}^*\psi_{n'\ell'm'}\,d^3\mathbf r = \delta_{nn'}\delta_{\ell\ell'}\delta_{mm'}$. Spherical-harmonic orthogonality handles $\ell$ and $m$; distinct $\hat H$ eigenvalues handle $n$. Checked, for example: $\int R_{10}R_{20}r^2dr = 0$ and $\int R_{21}R_{31}r^2dr = 0$.

## Moments

**General formulas** (exact, in units of $a$):

$$
\langle r\rangle = \frac{a}{2}\left[3n^2-\ell(\ell+1)\right],\qquad
\langle r^2\rangle = \frac{a^2n^2}{2}\left[5n^2+1-3\ell(\ell+1)\right],\qquad
\left\langle\frac1r\right\rangle = \frac{1}{n^2a}.
$$

Verified symbolically for all ten $(n,\ell)$ with $n\le4$:

| $(n,\ell)$ | 10 | 20 | 21 | 30 | 31 | 32 | 40 | 43 |
|---|---|---|---|---|---|---|---|---|
| $\langle r\rangle/a$ | 3/2 | 6 | 5 | 27/2 | 25/2 | 21/2 | 24 | 18 |
| $\langle r^2\rangle/a^2$ | 3 | 42 | 30 | 207 | 180 | 126 | 648 | 360 |

**Virial check.** $\langle1/r\rangle = 1/n^2a$ gives $\langle V\rangle = 2E_n$ and $\langle T\rangle = -E_n$, consistent with the virial theorem for $1/r$ ([[hellmann-feynman-and-virial-theorems]]).

!!! example "Problems 4.15, 4.17, 4.18, 4.54"
    **Problem 4.15.** In the ground state, $\langle x\rangle = 0$ and $\langle x^2\rangle = \langle r^2\rangle/3 = a^2$. In $\psi_{211}$, which is not spherically symmetric, $\langle x^2\rangle = 12a^2$.

    **Problem 4.17.** $\langle zHz\rangle_{100} = 0$. Quick route: $\langle[z,[H,z]]\rangle = \hbar^2/m$ and $\langle Hz^2+z^2H\rangle = 2E_1\langle z^2\rangle$, so

    $$
    2\langle zHz\rangle = \frac{\hbar^2}{m} + 2E_1a^2 = 0 .
    $$

    Direct integration confirms it.

    **Problem 4.18.** For $(\psi_{211}+\psi_{21-1})/\sqrt2$, $\langle V\rangle = 2E_2 = -6.80$ eV, independent of $t$ because both components have the same energy.

    **Problem 4.54.** The probability of finding the ground-state electron inside a nucleus of radius $b = 1$ fm is

    $$
    P = 1-\left(1+\frac{2b}{a}+\frac{2b^2}{a^2}\right)e^{-2b/a} = 9.10\times10^{-15},
    $$

    while the leading term $\tfrac43(b/a)^3$ gives $9.00\times10^{-15}$. The density $|\psi(0)|^2 = 1/\pi a^3$ is what enters hyperfine contact interactions.

!!! example "Finite-difference check of the spectrum (atomic units)"
    The radial equation on a uniform grid ($r\le80$ bohr, 16000 points) gives:

    | $\ell$ | Lowest three energies (hartree) |
    |---|---|
    | 0 | $-0.50000$, $-0.12500$, $-0.05556$ |
    | 1 | $-0.12500$, $-0.05556$, $-0.03125$ |
    | 2 | $-0.05556$, $-0.03125$, $-0.02000$ |

    These are $-1/2n^2$ with $n\ge\ell+1$. The $\ell$-degeneracy appears numerically.

## Spectrum

**Transition energies.** A transition $n_i\to n_f$ emits a photon of energy $E_i - E_f$. With $E = h\nu$ and $\lambda = c/\nu$:

$$
\frac{1}{\lambda} = \mathcal R\left(\frac{1}{n_f^2}-\frac{1}{n_i^2}\right),\qquad
\mathcal R = \frac{m_e}{4\pi c\hbar^3}\left(\frac{e^2}{4\pi\epsilon_0}\right)^2 = 1.097373\times10^7\ \text{m}^{-1}.
$$

**Series.** $n_f = 1$ is the Lyman series (ultraviolet), $n_f = 2$ the Balmer series (visible), and $n_f = 3$ the Paschen series (infrared).

| Line | $\lambda$ with $\mathcal R_\infty$ | $\lambda$ with reduced mass |
|---|---|---|
| Lyman $\alpha$ ($2\to1$) | 121.502 nm | 121.568 nm |
| H$\alpha$ ($3\to2$) | 656.112 nm | 656.470 nm |
| H$\beta$ ($4\to2$) | 486.009 nm | 486.274 nm |
| Paschen $\alpha$ ($4\to3$) | 1874.607 nm | 1875.627 nm |

Wavelengths are vacuum values. The reduced-mass shift ($\mu/m_e = 0.99946$) is about 0.05%, far larger than the spectrometer resolution, so it matters in practice.

**Hydrogenic ions** (Problem 4.19). Replace $e^2\to Ze^2$: $E_n(Z) = Z^2E_n$, $a(Z) = a/Z$, $\mathcal R(Z) = Z^2\mathcal R$.

| Ion | $E_1$ | $a/Z$ | Lyman $\alpha$ | Series limit |
|---|---|---|---|---|
| He⁺ ($Z=2$) | $-54.42$ eV | 0.2646 Å | 30.38 nm | 22.78 nm |
| Li²⁺ ($Z=3$) | $-122.45$ eV | 0.1764 Å | 13.50 nm | 10.13 nm |

Both fall in the extreme ultraviolet.

## What the exact solution does not include

Fine structure (relativity and spin–orbit coupling), the Lamb shift and hyperfine splitting are all perturbations on top of the Bohr levels (Griffiths Ch. 7). The Coulomb cusp, $\partial\ln\psi/\partial r = -1/a$ at $r=0$, is exact here; for many-electron atoms see [[coulomb-cusp-and-helium-expansions]].

## Source

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Sec. 4.2, Eqs. (4.52)-(4.94), Tables 4.5-4.7, Figs. 4.6-4.10 (described); Problems 4.12-4.19, 4.54. Page numbers are not given because the PDF used is an e-book rendering without print pagination. The general moment formulas are standard results, here verified symbolically for $n\le4$, not quoted from Griffiths. Reduced-mass wavelengths, hydrogenic tables and finite-difference spectra are computed in `griffiths/ch04_3d.py` (section C) with SciPy CODATA constants.
