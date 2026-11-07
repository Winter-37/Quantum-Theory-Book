---
id: gaussian-basis-functions
title: Slater and Gaussian functions, contraction, and STO-nG fits
summary: Slater-type orbitals have the right cusp and tail but awkward multicentre integrals; Gaussians have neither but satisfy the Gaussian product theorem. Contracted Gaussians fitted to Slater functions (STO-1G/2G/3G) by maximizing overlap, exponent scaling, and the integral formulas Szabo uses. Fits recomputed numerically.
status: in-progress
kind: theory
level: intermediate
tags: [basis-sets, gaussian, slater, sto-ng, contraction, gaussian-product-theorem, integrals]
prerequisites: [rhf]
related: [pople-basis-sets, scf-procedure, variational-principle, radial-basis-functions-slater-and-gaussian, gaussian-basis-sets-and-convergence, gaussian-overlap-distributions-and-one-electron-integrals]
order: 10
date: 2026-11-03
---

## Slater versus Gaussian 1s functions

Normalized 1s functions centred at $\mathbf R_A$:

$$
\phi^{\text{SF}}_{1s}(\zeta,\mathbf r-\mathbf R_A) = (\zeta^3/\pi)^{1/2}\,e^{-\zeta|\mathbf r-\mathbf R_A|},
\qquad
\phi^{\text{GF}}_{1s}(\alpha,\mathbf r-\mathbf R_A) = (2\alpha/\pi)^{3/4}\,e^{-\alpha|\mathbf r-\mathbf R_A|^2}.
$$

| | Slater (STO) | Gaussian (GTO) |
|---|---|---|
| nuclear cusp | correct, $\partial\phi/\partial r\ne0$ at $r=0$ | none, zero slope at $r=0$ |
| long range | $e^{-\zeta r}$, like exact bound states | $e^{-\alpha r^2}$, falls off too fast |
| 3- and 4-centre integrals | no closed form, expensive | closed form, fast |

Higher angular momentum is obtained with Cartesian prefactors $x^ky^lz^m$ ($k+l+m = 0, 1, 2$ for s, p, d) or with spherical harmonics. Six Cartesian $d$ functions contain one extra s-like combination $x^2+y^2+z^2$ relative to the five spherical ones.

## Gaussian product theorem

The product of two 1s Gaussians on different centres is a single 1s Gaussian on a centre between them (Szabo Ex. 3.19):

$$
\phi^{\text{GF}}_{1s}(\alpha,\mathbf r-\mathbf R_A)\,\phi^{\text{GF}}_{1s}(\beta,\mathbf r-\mathbf R_B) = K_{AB}\,\phi^{\text{GF}}_{1s}(p,\mathbf r-\mathbf R_P),
$$

$$
p = \alpha+\beta,
\qquad
\mathbf R_P = \frac{\alpha\mathbf R_A + \beta\mathbf R_B}{\alpha+\beta},
\qquad
K_{AB} = \Big(\frac{2\alpha\beta}{(\alpha+\beta)\pi}\Big)^{3/4}\exp\Big(-\frac{\alpha\beta}{\alpha+\beta}|\mathbf R_A - \mathbf R_B|^2\Big).
$$

Every charge distribution $\phi_\mu\phi_\nu$ therefore collapses to one centre, and a four-centre integral $(\mu\nu|\lambda\sigma)$ reduces to a two-centre one. That is why molecular codes use Gaussians despite their poor shape. The identity was checked numerically at an arbitrary point to $10^{-15}$ relative error.

## Contracted Gaussians

Fix the poor shape by using fixed linear combinations of **primitive** Gaussians:

$$
\phi^{\text{CGF}}_\mu(\mathbf r - \mathbf R_A) = \sum_{p=1}^{L}d_{p\mu}\,g_p(\alpha_{p\mu},\mathbf r - \mathbf R_A).
$$

$L$ is the **contraction length**. The exponents $\alpha_{p\mu}$ and coefficients $d_{p\mu}$ are fixed in advance; only the coefficients of the contracted functions in the MOs are varied in the SCF. This keeps $K$ (and the $K^4$ integral count) small, while each function has many primitives.

## STO-LG: least-squares fits to a Slater function

Choose the $L$ exponents and coefficients that maximize the overlap of the normalized contraction with a Slater 1s function of $\zeta = 1$:

$$
S = \int\mathrm d\mathbf r\ \phi^{\text{SF}}_{1s}(\zeta=1,\mathbf r)\,\phi^{\text{CGF}}_{1s}(\mathbf r).
$$

Maximizing $S$ for a normalized contraction is equivalent to minimizing the least-squares error $\int|\phi^{\text{SF}} - \phi^{\text{CGF}}|^2$. Results, with coefficients for normalized primitives:

| | exponents $\alpha$ | coefficients $d$ | overlap $S$ |
|---|---|---|---:|
| STO-1G | 0.270950 | 1 | 0.978404 |
| STO-2G | 0.151623, 0.851819 | 0.678914, 0.430129 | 0.998420 |
| STO-3G | 0.109818, 0.405771, 2.22766 | 0.444635, 0.535328, 0.154329 | 0.999835 |

These were recomputed here by numerical optimization (Nelder-Mead on log-exponents, numerical radial quadrature). They reproduce Szabo Eqs. (3.219)-(3.221) to all printed digits. The OCR'd text shows 0.534328 for the middle STO-3G coefficient; the optimum is 0.535328, so that is a scan error.

**The cusp is still missing (Szabo Ex. 3.20).** At the nucleus,

| | STO-1G | STO-2G | STO-3G | Slater |
|---|---:|---:|---:|---:|
| $\phi(0)$ | 0.2677 | 0.3894 | 0.4550 | $\pi^{-1/2} = 0.5642$ |

The overlap converges much faster than the value at the nucleus. Energies (dominated by the valence region) are fine, while properties at the nucleus (Fermi contact, electron density at the nucleus) are not.

## Scaling to other exponents

A Slater exponent only rescales $r$. If $\zeta = 1$ is fitted by Gaussians with exponents $\alpha_p$, then $\zeta$ is fitted by

$$
\alpha_p(\zeta) = \alpha_p(\zeta = 1)\times\zeta^2,
$$

with the same $d_p$. **Example (Szabo Ex. 3.21).** For STO-1G H$_2$ with $\zeta = 1.24$, $\alpha = 0.270950\times1.24^2 = 0.41662$. The overlap at $R = 1.4$ bohr is

$$
S_{12} = e^{-\alpha R^2/2} = 0.6648
$$

(for equal exponents the prefactor of the Gaussian overlap formula is 1). The STO-3G value is 0.6593.

## Integral formulas (1s Gaussians, unnormalized $e^{-\alpha r_A^2}$, $e^{-\beta r_B^2}$)

With $p = \alpha+\beta$, $\mu = \alpha\beta/p$, $R = |\mathbf R_A - \mathbf R_B|$:

$$
S = \Big(\frac{\pi}{p}\Big)^{3/2}e^{-\mu R^2},
\qquad
T = \mu\,(3 - 2\mu R^2)\Big(\frac{\pi}{p}\Big)^{3/2}e^{-\mu R^2},
$$

$$
V^{C} = -\frac{2\pi Z_C}{p}\,e^{-\mu R^2}\,F_0\big(p|\mathbf R_P - \mathbf R_C|^2\big),
\qquad
F_0(t) = \tfrac12\sqrt{\pi/t}\,\operatorname{erf}(\sqrt t),
$$

and two-electron integrals of the same type with $F_0$. These are Szabo's Appendix A formulas, which are standard (e.g. Helgaker-Jørgensen-Olsen Ch. 9). Codes such as PySCF/libcint generalize them to any angular momentum with recursion relations.

## Source

Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996; reprint of the revised first edition, McGraw-Hill, 1989), Sec. 3.5.1, pp. 153-159, Eqs. (3.203)-(3.224), Table 3.1, Ex. 3.19-3.21; Sec. 3.6.1, pp. 180-184; Appendix A. Fits recomputed for this note.
