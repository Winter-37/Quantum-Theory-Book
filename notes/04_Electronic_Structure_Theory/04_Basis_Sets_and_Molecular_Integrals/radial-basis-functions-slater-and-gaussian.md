---
id: radial-basis-functions-slater-and-gaussian
title: Radial atomic basis functions - completeness, hydrogenic, Laguerre, Slater, harmonic-oscillator and Gaussian functions, tested on the carbon orbitals
summary: HJO's requirements on one-electron basis functions (systematic completeness, fast convergence, easy integrals) and why one-centre and universal harmonic-oscillator bases fail in practice. The radial functions are built from Laguerre polynomials. Hydrogenic functions need the continuum and become too diffuse; fixed-exponent Laguerre functions (equivalent to STOs) and harmonic-oscillator functions (equivalent to GTOs) are complete but converge slowly; nodeless STOs and GTOs with variable exponents converge fast. HJO's least-squares expansions of the carbon ³P Hartree-Fock orbitals were repeated, using Clementi-Roetti STO orbitals as the target.
status: in-progress
kind: theory
level: intermediate
tags: [basis-functions, slater-type-orbitals, gaussian-type-orbitals, laguerre-functions, harmonic-oscillator, completeness, cusp, carbon]
prerequisites: [solid-harmonics-angular-basis, gaussian-basis-functions]
related: [gaussian-basis-sets-and-convergence, coulomb-cusp-and-helium-expansions, pople-basis-sets, basis-orthogonalization]
order: 40
date: 2026-11-04
---

## Requirements and completeness

**HJO's three requirements.** A basis should

1. extend systematically towards completeness;
2. converge quickly for real atomic and molecular orbitals;
3. allow easy (and numerically stable) integral evaluation.

No family has all three. Gaussians win by combining acceptable convergence with fast integrals.

**Completeness in the norm.** A set is complete if every square-integrable $f$ can be approximated with $\lVert f - \sum_nc_nh_n\rVert<\epsilon$.

- **Norm, not pointwise.** Complete sets exist whose members all vanish at the origin.
- **Energies need more.** Convergence of FCI energies requires completeness in Sobolev norms involving the kinetic energy.
- **Many electrons.** A complete one-electron set generates a complete set of determinants for $N$ electrons.

**One centre or many.**

- **Universal harmonic-oscillator basis.** A superposition of atom-centred harmonic potentials is again harmonic. HJO show that this gives a complete orthonormal "universal" basis for any molecule, but it converges hopelessly slowly.
- **Atom-centred ("atoms-in-molecules") bases.** These are compact and of similar quality for all sizes and geometries. Their costs:
    - no orthogonality between centres;
    - basis-set dependence of geometric derivatives (Pulay terms, [[analytic-gradients-and-force-constants]]);
    - linear dependence when extended;
    - basis-set superposition error ([[basis-set-superposition-error]]).

## Exponential radial functions

**Laguerre polynomials.** $L_n^\alpha(x)$ has $n$ roots, whose positions shift upwards with $\alpha$. The polynomials are orthogonal with weight $x^\alpha e^{-x}$ on $\mathbb R^+$. Conventions vary: HJO's lower index is the degree.

| Family | Radial form (unnormalized) | Status |
|---|---|---|
| Hydrogenic | $(2Zr/n)^lL_{n-l-1}^{2l+1}(2Zr/n)\,e^{-Zr/n}$ | incomplete without continuum; $\langle r\rangle\propto n^2$, too diffuse |
| Laguerre | $(2\zeta r)^lL_{n-l-1}^{2l+2}(2\zeta r)\,e^{-\zeta r}$ | complete, orthonormal for fixed $\zeta$; $\langle r\rangle = (n+\tfrac12)/\zeta$ |
| Slater (STO) | $r^{n-1}e^{-\zeta r}$ (times a solid harmonic) | complete for fixed $\zeta$; same span as Laguerre up to each $n$; nuclear cusp for $1s$ |
| Variable-exponent STOs | $r^le^{-\zeta_{nl}r}$ | complete if the $\zeta_{nl}$ have a finite accumulation point (a sufficient condition, from HJO ref. 17) |

**Minimal STO bases and Slater's rules.** One STO per occupied orbital, with exponents matched to $\langle r\rangle$ of the HF orbitals. Slater's rules give 5.70 for carbon $1s$ and 1.625 for $2s$ and $2p$. Double-zeta sets use two STOs per occupied orbital. Accurate atomic STO expansions exist, e.g. Clementi-Roetti for carbon (HJO Table 6.5): 2 $1s$, 4 $2s$ and 4 $2p$ STOs. Their weakness is the multicentre two-electron integrals, which is why molecular work moved to Gaussians.

## Gaussian radial functions

| Family | Radial form | Remarks |
|---|---|---|
| Harmonic oscillator (HO) | $r^lL_{n-l-1}^{l+1/2}(2\alpha r^2)\,e^{-\alpha r^2}$ | complete, orthonormal; levels $\bar n = 2(n-1)-l$, degeneracy $(\bar n+1)(\bar n+2)/2$; no cusp, Gaussian decay |
| Spherical-harmonic GTOs | $S_{lm}(\mathbf r)\,r^{2(n-l-1)}e^{-\alpha r^2}$ | complete for fixed $\alpha$; in practice only $n = l + 1$, with variable exponents |
| Cartesian GTOs | $x^iy^jz^k\,e^{-\alpha r^2}$ | separable, Gaussian product rule; $(l+1)(l+2)/2$ per shell ([[solid-harmonics-angular-basis]]) |

**Extent.** STO size grows linearly with $n$ and $\zeta^{-1}$, GTO size only as $\sqrt n$ and $\alpha^{-1/2}$. Gaussians therefore need many more functions, or much smaller exponents, to describe the outer region.

**Completeness with variable exponents.** Sufficient conditions are an accumulation point $0<\alpha_l<\infty$, or exponents decreasing to zero whose sum diverges (e.g. $1/n$). Such sets converge slowly and are numerically awkward; practical sets are discussed in [[gaussian-basis-sets-and-convergence]].

**Why Gaussians anyway.** Separability in $x$, $y$, $z$ and the Gaussian product rule make all molecular integrals cheap ([[gaussian-overlap-distributions-and-one-electron-integrals]], [[electron-repulsion-integrals-md-os-rys]]).

## The carbon test

**Method.** HJO expand the numerical HF $1s$, $2s$ and $2p$ orbitals of C($^3P$) by least squares in each family. The error is $\lVert f - g\rVert$ for the normalized orbital $f$, which equals $\sqrt{1 - \mathbf T^{\mathsf T}\mathbf S^{-1}\mathbf T}$.

!!! example "Least-squares expansions of the carbon orbitals (computed for this note; HJO's counts in parentheses)"
    Target orbitals: the Clementi-Roetti STO expansions of HJO Table 6.5 (norms 0.999998, 0.999992, 1.000000; $\langle r\rangle$ = 0.269, 1.589, 1.715 bohr). HJO used numerical HF orbitals. The table gives the number of functions needed to reach an error below 0.1 and below 0.01.

    | Basis (fixed exponent) | Orbital | < 0.1 | < 0.01 |
    |---|---|---:|---:|
    | Laguerre, $\zeta = 1$ | $1s$ | 12 (12) | 21 (21) |
    | Laguerre, $\zeta = 1$ | $2s$ | 6 (6) | 13 (16) |
    | Laguerre, $\zeta = 1$ | $2p$ | 4 (4) | 9 (13) |
    | Laguerre, $\zeta = 5.6$ | $1s$ | 1 | 3 (3) |
    | Laguerre, $\zeta = 2.0$ | $2s$ | 4 | 6 (6) |
    | Laguerre, $\zeta = 1.6$ | $2p$ | 3 | 5 (5) |
    | HO, $\alpha = 1$ | $1s$ | 30 (30) | > 40 |
    | HO, $\alpha = 1$ | $2s$ | 10 (10) | > 40 |
    | HO, $\alpha = 1$ | $2p$ | 10 (10) | 29 |
    | HO, $\alpha = 11$ | $1s$ | 4 (3) | 21 (21) |

    - **Agreement.** Most counts agree exactly; the two 0.01 counts for $\zeta = 1$ and the HO $\alpha = 11$ count differ slightly, which I attribute to the STO target versus HJO's numerical orbitals.
    - **Single 2s Laguerre function.** The best has $\zeta = 2.52$ with overlap 0.824 (HJO: 2.52, 0.82). Its maximum is in the right place, but it misses the inner node region.
    - **Lessons.** No single exponent serves core and valence. Gaussian (HO) expansions are bumpier and slower than exponential ones, even with the best exponent.

## Source

Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, Chichester, 2000), Secs. 6.1-6.3 and 6.5-6.6, pp. 201-207 and 218-240, Box 6.1, Tables 6.4-6.7, Figs. 6.2-6.11. The carbon expansions were recomputed for this note on a radial grid, using the Clementi-Roetti coefficients printed in HJO Table 6.5.
