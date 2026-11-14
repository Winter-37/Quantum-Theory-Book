---
id: coulomb-cusp-and-helium-expansions
title: The Coulomb hole, the cusp conditions and the slow convergence of orbital expansions - partial-wave and principal expansions of the helium atom
summary: Electron correlation shows up as a Coulomb hole around each electron. At coinciding particles the exact wave function has cusps (∂Ψ/∂r = −ZΨ at a nucleus, ∂Ψ/∂r₁₂ = ½Ψ for two electrons) that no finite expansion in products of smooth orbitals can reproduce. For ground-state helium, the partial-wave increments fall as (L+½)⁻⁴ and the truncation error as (L+1)⁻³; the principal expansion converges as N⁻³. HJO's Table 7.2 fits, their −34.7 μE_h truncation estimate, the N⁻³ extrapolations, and my own He cc-pVXZ full-CI series reproduce this, and explain why correlation energies converge so slowly and why explicitly correlated (r₁₂) methods help.
status: in-progress
kind: theory
level: intermediate
tags: [coulomb-cusp, coulomb-hole, electron-correlation, partial-wave-expansion, principal-expansion, helium, basis-set-convergence, explicitly-correlated, hylleraas]
prerequisites: [electron-correlation, full-ci, radial-basis-functions-slater-and-gaussian]
related: [gaussian-basis-sets-and-convergence, h2-minimal-basis-correlation-analysis, exact-wave-function-properties-and-symmetry, standard-models-h2-and-water]
order: 80
date: 2026-11-04
---

## The Coulomb hole

**HF versus exact.** In Hartree-Fock theory each electron moves in the averaged field of the other. For ground-state He with one electron fixed 0.5 bohr from the nucleus, the HF amplitude of the other electron forms undistorted concentric circles. The exact wave function shifts amplitude away from the fixed electron. The difference (exact − HF), plotted by HJO, is the **Coulomb hole**: wide but shallow, minimum −0.068 near the fixed electron (at 0.49 bohr from the nucleus), with a compensating maximum of 0.012 on the far side.

**Hard part.** Products of orbitals reproduce a crude hole easily; reproducing its centre accurately is very hard.

## Cusp conditions

**Origin.** The Hamiltonian is singular where particles coincide. For the local energy $\hat H\Psi/\Psi$ to stay finite, the kinetic energy must diverge with opposite sign, which requires a kink in $\Psi$. For a totally symmetric He state in the coordinates $r_1$, $r_2$, $r_{12}$ (spherical averaging implied):

$$
\frac{\partial\Psi}{\partial r_i}\Big|_{r_i=0} = -Z\,\Psi\big|_{r_i=0}\quad\text{(nuclear cusp)},\qquad
\frac{\partial\Psi}{\partial r_{12}}\Big|_{r_{12}=0} = \tfrac12\,\Psi\big|_{r_{12}=0}\quad\text{(Coulomb cusp)} .
$$

**Consequences.**

- **Nuclear cusp.** It holds automatically for any function behaving as $e^{-Zr}$ near the nucleus, e.g. STOs. Gaussians have zero slope there and can only approximate it. It matters mostly for densities at the nucleus.
- **Coulomb cusp.** Expanding $\Psi$ along the collinear arrangement gives $\Psi\approx\Psi_0(1 + \tfrac12r_{12})$: continuous, but not differentiable at $r_{12} = 0$. Products of smooth one-electron functions are differentiable everywhere, so **no finite orbital expansion can produce the cusp**. This is the root of the slow convergence of correlation energies.

## Approximate helium wave functions

**CI in STOs (HJO Fig. 7.6).** Expanding in products of STOs with one exponent, $\phi_{nlm}\propto r^{n-1}e^{-\zeta r}Y_{lm}$, converges very slowly; an error below 0.1 m$E_h$ is hard to reach. Optimizing the orbitals numerically lowers the error by a factor of 3-4 at each level but does not change the rate.

**Explicit correlation.** Correlating factors such as $(1 + \tfrac12r_{12})$, or Hylleraas functions with terms $r_1^ir_2^jr_{12}^k$ (the $k = 1$ term carries the cusp), converge dramatically faster: a few terms give m$E_h$ accuracy. This motivates the modern R12/F12 methods. Their many-electron integrals are the price; HJO quote R12 limits as benchmarks in Ch. 8.

## Partial-wave expansion

**Setup.** $1/r_{12} = \sum_l r_<^l/r_>^{l+1}P_l(\cos\theta_{12})$. For a $^1S$ state the CI wave function is a sum of partial waves $\Psi_l$, each built from determinants of orbitals with angular momentum $l$. $E_L$ is the CI energy with all $l\le L$ (each partial wave saturated radially).

**Asymptotics (HJO Eqs. 7.4.13 and 7.4.19).**

$$
\varepsilon_L = E_L - E_{L-1} = e_4\big(L+\tfrac12\big)^{-4} + e_5\big(L+\tfrac12\big)^{-5} + \cdots,\qquad
\Delta E_L = \sum_{l>L}\varepsilon_l\approx\tfrac13e_4(L+1)^{-3} + \tfrac14e_5(L+1)^{-4} .
$$

Theory gives $e_4 = -0.074226$ and $e_5 = -0.030989$ for He. The truncation error falls only as $(L+1)^{-3}$.

!!! example "HJO's He partial-wave energies, refitted (computed for this note)"
    From HJO Table 7.1 ($E_0 = -2.8790288$ to $E_8 = -2.9036897$), two-parameter fits of $\varepsilon_L$ for $L\ge l_{\min}$:

    | $l_{\min}$ | 1 | 2 | 3 | 4 | 5 |
    |---|---:|---:|---:|---:|---:|
    | $e_4$ | −0.05781 | −0.07175 | −0.07361 | −0.07433 | −0.07427 |
    | $e_5$ | −0.07646 | −0.04041 | −0.03348 | −0.02994 | −0.03036 |

    - **Fits.** These are identical to HJO Table 7.2 and approach the theoretical values as low $L$ is excluded.
    - **Tail.** Summing the $l_{\min} = 3$ model over $l>8$ gives −34.7 μ$E_h$, hence $E = -2.903724$, the exact $^1S$ energy −2.903724377.
    - **Closed form.** The two-term formula (7.4.18) gives −34.9 μ$E_h$ for $L = 8$ (true −34.7) and −209.7 μ$E_h$ for $L = 4$ (true −205.8).

## Principal expansion

**Setup.** At level $N$ include all orbitals with principal quantum number $\le N$: $1s$; $2s2p$; $3s3p3d$; … (HJO Fig. 7.9). Each level adds a finite number of optimized orbitals, which is what correlation-consistent basis sets imitate ([[gaussian-basis-sets-and-convergence]]).

**Rate.** If each natural orbital $nlm$ contributes about $-An^{-6}$ (independent of $l$; HJO Eq. 7.5.4), then a level with $n = N$ adds $N^2$ orbitals:

$$
\varepsilon_N\approx c_4\big(N-\tfrac12\big)^{-4},\qquad \Delta E_N\approx cN^{-3}.
$$

For the partial-wave expansion the same assumption gives $\varepsilon_L\approx-\tfrac23A(L+\tfrac12)^{-4}$. The two expansions converge at the same rate per level, but the principal expansion needs only finitely many orbitals per level.

!!! example "Principal expansion of He (HJO Table 7.3; analysis computed for this note)"
    - **Errors.** $E_N - E_{\text{exact}}$ = 42 044, 6 050, 1 883, 815, 424, 248, 157, 106 and 74 μ$E_h$ for $N = 1$-9. The fit gives $c_4 = -0.182$.
    - **Two-point $N^{-3}$ extrapolation** $E_\infty = (Y^3E_Y - X^3E_X)/(Y^3 - X^3)$ from levels (3,4), (4,5), (5,6), (6,7), (7,8) and (8,9) gives errors of 36.0, 14.1, 6.6, 2.6, 2.9 and −1.1 μ$E_h$ (the (7,8) error is not smaller than (6,7)'s, so the sequence is not monotonic).

    **My own He full CI in cc-pVXZ** (a Gaussian realization of the principal expansion):

    | Basis | Functions | $E_{\text{HF}}$ | $E_{\text{FCI}}$ | % of exact correlation (−42.044 m$E_h$) |
    |---|---:|---:|---:|---:|
    | cc-pVDZ | 5 | −2.855160 | −2.887595 | 77.1 |
    | cc-pVTZ | 14 | −2.861153 | −2.900232 | 92.9 |
    | cc-pVQZ | 30 | −2.861514 | −2.902411 | 97.3 |
    | cc-pV5Z | 55 | −2.861625 | −2.903152 | 98.8 |

    - **Convergence.** The correlation error (9.6, 3.0, 1.1, 0.5 m$E_h$) falls roughly as $X^{-3}$.
    - **Extrapolation.** $X^{-3}$ extrapolations of the correlation energy from (D,T), (T,Q) and (Q,5) are within 0.2 m$E_h$ of the exact value (0.17, −0.18, −0.14 m$E_h$). The Q5 value slightly **overshoots**, a reminder that $X^{-3}$ is only the leading term.

## Summary (HJO Sec. 7.6, with the numbers)

**HF energy versus correlation energy.**

- **HF.** Converges essentially exponentially with basis size.
- **Correlation.** Converges only as an inverse power: $(L+1)^{-3}$ or $X^{-3}$, set by the Coulomb cusp.

**Remedies.** Either extrapolate in the cardinal number, or build $r_{12}$ dependence into the wave function.

**Static versus dynamical correlation.**

- **Static correlation** (near-degeneracy; [[h2-minimal-basis-correlation-analysis]]) needs few orbitals.
- **Dynamical correlation**, short range and governed by the cusp, needs high angular momenta.

## Source

Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, Chichester, 2000), Ch. 7, pp. 256-286, Eqs. (7.1.1)-(7.5.5), Tables 7.1-7.3, Figs. 7.1-7.10. Table values and equations read from the page images. The fits, extrapolations and cc-pVXZ full-CI calculations (PySCF 2.14) were done for this note.
