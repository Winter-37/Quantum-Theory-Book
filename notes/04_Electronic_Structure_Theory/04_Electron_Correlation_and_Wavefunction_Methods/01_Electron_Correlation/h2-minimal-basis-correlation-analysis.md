---
id: h2-minimal-basis-correlation-analysis
title: H₂ in a minimal basis of hydrogenic 1s orbitals - bonding, two-configuration, covalent, ionic and open-shell states, energy decomposition, and static versus dynamical correlation
summary: HJO's model system, H₂ with one hydrogenic 1s function (exponent 1) per atom, analysed through densities and an energy breakdown into kinetic, nuclear-attraction and electron-repulsion parts. The bond lowers the kinetic energy. Mixing in σ_u² (τ = −0.1109) correlates the electrons and lowers the repulsion by 5%. The covalent (Heitler-London) and ionic structures correspond to τ = ∓0.1400. At dissociation σ_g² is half covalent, half ionic (E = −11/16), and the degenerate two-configuration state recovers −1 E_h: static correlation. All integrals and Tables 5.1-5.3 reproduced with a 16-Gaussian fit to the Slater 1s function.
status: in-progress
kind: derivation
level: introductory
tags: [h2, minimal-basis, static-correlation, dynamical-correlation, covalent-ionic, heitler-london, two-configuration, energy-decomposition]
prerequisites: [minimal-basis-h2-model, density-matrices-second-quantization, electron-correlation]
related: [h2-dissociation-rhf-uhf, mcscf-and-gvb, natural-orbitals, full-ci, standard-models-h2-and-water]
also: [04_Electronic_Structure_Theory/04_Electron_Correlation_and_Wavefunction_Methods/01_Electron_Correlation/Static_Correlation, 04_Electronic_Structure_Theory/04_Electron_Correlation_and_Wavefunction_Methods/01_Electron_Correlation/Dynamic_Correlation]
date: 2026-11-04
---

## The model

**Basis and orbitals.** One normalized hydrogenic $1s$ function with exponent 1 on each nucleus, overlap $S$ ($S = 0.7529$ at $R = 1.4$ bohr). By symmetry the MOs are fixed:

$$
\phi_1 = 1\sigma_g = \frac{1s_A + 1s_B}{\sqrt{2(1+S)}},\qquad \phi_2 = 1\sigma_u = \frac{1s_A - 1s_B}{\sqrt{2(1-S)}} .
$$

Szabo's version of this model uses STO-3G with exponent 1.24 ([[minimal-basis-h2-model]]); HJO keep exponent 1, which is exact for the separated atoms.

**States.** The $^1\Sigma_g^+$ space is spanned by $|1\sigma_g^2\rangle$ and $|1\sigma_u^2\rangle$, combined as

$$
|{}^1\Sigma_g^+(\tau)\rangle = \cos\tau\,|1\sigma_g^2\rangle + \sin\tau\,|1\sigma_u^2\rangle .
$$

The open shell $1\sigma_g1\sigma_u$ gives $^3\Sigma_u^+$ and $^1\Sigma_u^+$.

**Densities.** For the two-configuration state, $D_{11} = 2\cos^2\tau$ and $D_{22} = 2\sin^2\tau$ (the natural occupations), $d_{1111} = 2\cos^2\tau$, $d_{2222} = 2\sin^2\tau$, and the off-diagonal pair density is $d_{2121} = \sin2\tau$ ([[density-matrices-second-quantization]]). The energy is

$$
E(\tau) = 2\cos^2\tau\,h_{11} + 2\sin^2\tau\,h_{22} + \cos^2\tau\,g_{1111} + \sin^2\tau\,g_{2222} + \sin2\tau\,g_{2121} + \frac1R .
$$

The first four terms are "classical"; the $\sin2\tau\,g_{2121}$ term is the exchange-correlation part of the repulsion.

**Integrals at $R = 1.4$ bohr** (computed here; HJO Table 5.1 values agree to $10^{-4}$):

| Integral | Value | Integral | Value |
|---|---:|---|---:|
| $h_{11}$ (kinetic + attraction) | −1.1856 = 0.4081 − 1.5937 | $g_{1111}$ | 0.5660 |
| $h_{22}$ | −0.5737 = 1.1522 − 1.7258 | $g_{2222}$ | 0.5863 |
| | | $g_{2211}$ ($J_{12}$) | 0.5564 |
| | | $g_{2121}$ ($K_{12}$) | 0.1402 (HJO 0.1403) |

At infinite separation: $h_{11} = h_{22} = -\tfrac12$ and all four two-electron integrals equal $\tfrac5{16}$.

## Energies and their decomposition

!!! example "HJO Table 5.2, $R = 1.4$ bohr (computed for this note; total energies include $1/R = 0.7143$)"
    | State | $\tau$ | Kinetic | Attraction | Repulsion (classical + xc) | Total |
    |---|---:|---:|---:|---|---:|
    | $1\sigma_g^2$ | 0 | 0.8162 | −3.1874 | 0.5660 + 0 = 0.5660 | −1.0909 |
    | $1\sigma_u^2$ | $\pi/2$ | 2.3043 | −3.4517 | 0.5863 + 0 = 0.5863 | 0.1532 |
    | Ground two-configuration | −0.1109 | 0.8344 | −3.1907 | 0.5663 − 0.0308 = 0.5354 | −1.1065 |
    | Excited two-configuration | $-0.1109 + \pi/2$ | 2.2861 | −3.4484 | 0.5860 + 0.0308 = 0.6169 | 0.1688 |
    | Covalent (Heitler-London) | −0.1400 | 0.8452 | −3.1926 | 0.5664 − 0.0388 = 0.5277 | −1.1055 |
    | Ionic | +0.1400 | 0.8452 | −3.1926 | 0.5664 + 0.0388 = 0.6052 | −1.0279 |
    | $^3\Sigma_u^+$ | | 1.5603 | −3.3196 | 0.5564 − 0.1402 = 0.4162 | −0.6289 |
    | $^1\Sigma_u^+$ | | 1.5603 | −3.3196 | 0.5564 + 0.1402 = 0.6966 | −0.3484 |

**What the table says.**

- **The bond is kinetic.** $1\sigma_g^2$ and $1\sigma_u^2$ have similar potential energies (the bonding one is even higher), but the kinetic energy of $1\sigma_g^2$ is 1.49 hartree lower. Two separated atoms have $E = -1$; the bonding configuration lies 0.0909 below.
- **Correlation lowers repulsion.** Optimizing $\tau$ (ground state $\tau_0 = -0.1109$, natural occupations 1.976 and 0.024) lowers the repulsion from 0.5660 to 0.5354, by 5%. The kinetic energy rises slightly. The gain of 0.0156 hartree is the correlation energy of this model. The $1\sigma_u^2$ admixture reduces the probability of both electrons being on the same atom: **left-right correlation**.
- **Covalent and ionic.** In MO form, the Heitler-London function $1s_A1s_B + 1s_B1s_A$ is $(1+S)|1\sigma_g^2\rangle - (1-S)|1\sigma_u^2\rangle$ (normalized), i.e. $\tau_{\text{cov}} = \arctan[-(1-S)/(1+S)] = -0.1400$; the ionic function $1s_A1s_A + 1s_B1s_B$ has $\tau_{\text{ion}} = +0.1400$. The covalent state (−1.1055) is close to the optimal ground state (−1.1065); the optimal state contains a small ionic admixture.
- **Open shells.** The triplet is lower than the open-shell singlet by $2K_{12} = 0.280$ hartree, the exchange integral at work.

## Dissociation

**Integrals at $R\to\infty$.** All two-electron integrals are $\tfrac5{16}$, half the on-site repulsion $(1s1s|1s1s) = \tfrac58$, because each delocalized orbital places only half an electron on each atom, and $E(\tau) = -1 + \tfrac5{16} + \tfrac5{16}\sin2\tau$.

| State (HJO Table 5.3) | $\tau$ | Repulsion | Energy |
|---|---:|---|---:|
| $1\sigma_g^2$ or $1\sigma_u^2$ | 0 or $\pi/2$ | $\tfrac5{16} + 0$ | $-\tfrac{11}{16}$ |
| Optimal ground = covalent | $-\pi/4$ | $\tfrac5{16} - \tfrac5{16} = 0$ | −1 |
| Optimal excited = ionic | $+\pi/4$ | $\tfrac5{16} + \tfrac5{16}$ | $-\tfrac38$ |
| $^3\Sigma_u^+$ | | 0 | −1 |
| $^1\Sigma_u^+$ | | $\tfrac58$ | $-\tfrac38$ |

**Reading it.**

- **$1\sigma_g^2$ is half covalent and half ionic.** Its energy $-\tfrac{11}{16} = \tfrac12(-1) + \tfrac12(-\tfrac38)$ is the average of the neutral atoms ($-1$) and of $\text{H}^- + \text{H}^+$ ($-\tfrac38$ in this basis). This is the RHF dissociation error ([[h2-dissociation-rhf-uhf]]).
- **Equal weights.** At infinite separation $1\sigma_g$ and $1\sigma_u$ are degenerate, and the correct state is the equal-weight combination $\tau = -\pi/4$, which removes the ionic part exactly.

## Static and dynamical correlation

- **Static (nondynamical) correlation:** the $1\sigma_u^2$ admixture at large $R$. It is required by the near-degeneracy of $1\sigma_g^2$ and $1\sigma_u^2$, not by electron-electron cusp behaviour. Its weight approaches 50%.
- **Dynamical correlation:** the small $1\sigma_u^2$ weight at equilibrium, part of the short-range avoidance of the electrons. A larger basis adds angular ($\pi_u$) and radial ($2\sigma_g$) correlating orbitals ([[standard-models-h2-and-water]]).
- **Not separable in general.** The same configuration can carry both kinds depending on geometry. Large basis sets are needed for dynamical correlation; a few well-chosen configurations (MCSCF) handle static correlation ([[mcscf-and-gvb]]).

## Source

Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, Chichester, 2000), Sec. 5.2, pp. 146-162, Eqs. (5.2.1)-(5.2.70), Tables 5.1-5.3. All integrals and energies recomputed for this note with PySCF 2.14, using a least-squares 16-term even-tempered Gaussian expansion of the $\zeta = 1$ Slater function (overlap with the exact function 0.999998; H-atom energy −0.499997).
