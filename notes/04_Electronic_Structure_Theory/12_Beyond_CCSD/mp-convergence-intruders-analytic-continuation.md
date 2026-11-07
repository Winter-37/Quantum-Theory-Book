---
id: mp-convergence-intruders-analytic-continuation
title: Convergence of perturbation series (HJO 14.5) - the two-state model, points of degeneracy and intruders in the complex plane, gap shifts, front-door and back-door intruders, divergence of the MP series for HF, and analytic continuation
summary: A perturbation series in z for H₀ + zU converges at z = 1 only if no point of degeneracy (where the reference state meets another eigenvalue in the complex z plane) lies inside the unit circle. In the two-state model these points are ζ± = (β − α + γ)(γ ± 2i|δ|)/(4δ² + γ²). Back-door intruders (Re ζ < 0: high, diffuse, multiply excited states with weak repulsion) produce alternating divergence. Front-door intruders (Re ζ > 0: low states, strong coupling) produce slow oscillations. Recomputed: HJO's degeneracy points from their two-state matrices (−0.74272 ± 0.00007i; 0.801 ± 0.579i), the gap-shift results γ_c = 5/8 and γ_m = 9/4, the closed-form coefficients, and analytic continuation of the back-door model (diverging at z = 0, converging to 10⁻¹⁴ when re-expanded at z′ = 0.4). HJO's HF-molecule full-CI scans are quoted.
status: in-progress
kind: theory
level: advanced
tags: [perturbation-theory, convergence, intruder-states, points-of-degeneracy, moller-plesset, analytic-continuation, gap-shift, divergence]
prerequisites: [rspt-wigner-rule-and-hylleraas-functional, moller-plesset-and-coupled-cluster-perturbation-theory]
related: [standard-models-h2-and-water, caspt2-and-caspt-series, mp3]
order: 20
date: 2026-11-04
---

## The two-state model

**Setup (HJO Sec. 14.5.1).** Take $\mathbf H = \begin{pmatrix}\alpha & \delta\\ \delta & \beta\end{pmatrix}$ with $\beta > \alpha$, split Epstein-Nesbet style into its diagonal and off-diagonal parts. Then

$$
E = \frac{\alpha + \beta}{2} - \frac{\beta - \alpha}{2}\sqrt{1 + \frac{4\delta^2}{(\beta - \alpha)^2}} .
$$

- **Only even orders survive:** $E^{(2n)} = (-1)^n\frac{(2n-3)!!\,2^{n-1}}{n!}\frac{\delta^{2n}}{(\beta - \alpha)^{2n-1}}$.
- **Convergence condition:** $|\delta| < (\beta - \alpha)/2$.

**General criterion (HJO Sec. 14.5.2, after Kato).** $E_k(z)$ for $\hat H_0 + z\hat U$ is analytic except at *points of degeneracy* $\zeta$, where state $k$ meets another state.

- **Pairs.** For real symmetric matrices these come in conjugate pairs.
- **Radius of convergence.** The series in $z$ converges out to the nearest such point.
- **Intruders.** A degeneracy inside the unit circle is called an intruder. It is *front-door* if $\mathrm{Re}\,\zeta > 0$ and *back-door* if $\mathrm{Re}\,\zeta < 0$.
- **What matters.** Convergence depends on avoiding degeneracies of $\hat H_0 + z\hat U$ for $|z|\le1$, not on $\hat H_0$ being "close" to $\hat H$.

**Gap shifts (HJO Sec. 14.5.3).** Move $\gamma$ from $\hat U$ into the excited zero-order energy: $\mathbf H_0 = \mathrm{diag}(\alpha, \beta + \gamma)$ and $\mathbf U = \begin{pmatrix}0 & \delta\\ \delta & -\gamma\end{pmatrix}$. Then

$$
\zeta_\pm = \frac{\beta - \alpha + \gamma}{4\delta^2 + \gamma^2}\,(\gamma\pm2i|\delta|),\qquad
\text{convergent for}\ \gamma > \gamma_c = \frac{4\delta^2 - (\beta - \alpha)^2}{2(\beta - \alpha)} .
$$

- **Real axis.** On the real axis the two states show an avoided crossing at $z_{\min} = \mathrm{Re}\,\zeta$, with gap $2|(\beta - \alpha + \gamma)\delta|/\sqrt{4\delta^2 + \gamma^2}$.
- **Back-door intruders** require $-(\beta - \alpha) < \gamma < 0$. For small $\delta$ their corrections alternate, $E^{(n)}\approx\gamma^{n-2}\delta^2/(\beta - \alpha + \gamma)^{n-1}$.

!!! example "Gap-shifted model with α = 1, β = 2, δ = ¾ (HJO Fig. 14.3; computed for this note)"
    **Thresholds.** $\gamma_c = 0.625$. The shift that pushes the degeneracies farthest out is $\gamma_m = 2.250$, with $|\zeta| = 1.202$.

    **Errors** $|E_{\text{PT}}(n) - E|$ from my RSPT recursion, which agrees with HJO's closed form (14.5.35) to $10^{-16}$:

    | $\gamma$ | $n = 10$ | $n = 50$ | $n = 100$ | $n = 200$ |
    |---|---:|---:|---:|---:|
    | 0 (unshifted) | 0.49 | $5\times10^5$ | $1\times10^{14}$ | $2\times10^{31}$ |
    | 0.675 ($\gamma_c$ + 0.05) | $6\times10^{-3}$ | $7\times10^{-4}$ | $6\times10^{-5}$ | $5\times10^{-6}$ |
    | 2.25 ($\gamma_m$) | $3\times10^{-4}$ | $4\times10^{-7}$ | $6\times10^{-12}$ | $4\times10^{-16}$ |
    | 10 | $9\times10^{-2}$ | $4\times10^{-4}$ | $1\times10^{-6}$ | $2\times10^{-10}$ |

## Intruders in the Møller-Plesset series

**Diagnosing intruders (HJO Secs. 14.5.4-14.5.5).** Scan $E_k(z)$ on the real axis and look for avoided crossings. HJO did this with full CI for HF (91.694 pm) in three cases:

- **cc-pVDZ at equilibrium.** No crossing; the series converges.
- **Partly augmented aug-cc-pVDZ at equilibrium.** A sharp back-door crossing at $z = -0.743$. The MP series oscillates about FCI up to order 14 and then diverges.
- **cc-pVDZ at $2.5R_e$.** A back-door crossing at $-0.598$, plus a weak front-door one near $0.8$. Corrections 10-30 undulate; after that, alternating divergence takes over.

**HJO's two-state projections and their degeneracy points (recomputed from their matrices, Eqs. 14.5.40-14.5.43):**

| Case | $\mathbf H_0$ | $\mathbf U$ | $\zeta$ (mine) | HJO |
|---|---|---|---|---|
| aug, $R_e$ (back door) | diag(−54.65980, −49.41060) | [[−44.91005, −0.00034], [−0.00034, −37.84247]] | −0.74272 ± 0.00007i | −0.743 ± 0.00007i |
| cc-pVDZ, $2.5R_e$ (front door) | diag(−56.28832, −55.87498) | [[−43.65655, 0.12252], [0.12252, −43.99542]] | 0.801 ± 0.579i | 0.801 ± 0.579i |

With HJO's rounded parameters for the front-door model ($\beta - \alpha = 0.07$, $\delta = 0.12$, $\gamma = 0.34$), formula (14.5.22) gives $0.805\pm0.568i$, with $|\zeta| = 0.985$, just inside the unit circle.

**Why back-door intruders are common in MP theory.**

- **The ground state.** $E^{(1)} = \langle\hat\Phi\rangle$ is minus the electron repulsion, so $E(z)$ falls steeply as $z$ decreases.
- **Diffuse, multiply excited states.** Their electrons are far apart and repel weakly, so their $E(z)$ has a gentler slope. The curves can therefore cross at some $-1 < z < 0$.
- **Basis dependence.** Diffuse basis functions make these states available. That is why the series diverges for equilibrium HF in aug-cc-pVDZ but not in cc-pVDZ.

## Analytic continuation

**Method (HJO Sec. 14.5.6).** If the only intruder is a back-door one at $|\zeta_B| < 1$, re-expand around a point $0 < z' < |\zeta_B|$:

$$
E'^{(n)} = \sum_{m\ge n}\binom{m}{n}E^{(m)}z'^{\,m-n} .
$$

The new series converges inside a disc about $z'$ that reaches the nearest degeneracy. If $z = 1$ lies inside, the physical energy follows; otherwise continue in steps. For HF/aug at $R_e$, HJO's re-expansion at $z' = 0.4$ converges to FCI (−100.24664 $E_h$) by order 6, while the series about 0 alternates (their Table 14.4; quoted).

!!! example "Analytic continuation of HJO's back-door two-state model (computed for this note; error in $E_h$)"
    | Order | Expansion at $z = 0$ | Re-expansion at $z' = 0.4$ |
    |---:|---:|---:|
    | 1 | $9.4\times10^{-9}$ | $1.4\times10^{-9}$ |
    | 4 | $-2.3\times10^{-8}$ | $-2.1\times10^{-10}$ |
    | 8 | $-7.5\times10^{-8}$ | $-1.6\times10^{-11}$ |
    | 12 | $-2.5\times10^{-7}$ | $-1.2\times10^{-12}$ |
    | 20 | $-2.7\times10^{-6}$ | $1\times10^{-14}$ |
    | 40 | $-1.0\times10^{-3}$ | $3\times10^{-14}$ |

    - **Divergence at $z = 0$.** The error ratio is $-1.346 = 1/(-0.743)$ per order, exactly the reciprocal of the degeneracy point.
    - **Convergence at $z'$.** The re-expanded series converges, because $|1 - 0.4| < |-0.743 - 0.4|$.
    - **Scale.** The coupling is tiny, so the errors are small in absolute terms, but the qualitative behaviour is the same as in HJO's table.

**Outlook (HJO).** The MP series is unpredictable: it alternates or oscillates with long periods and can diverge for simple molecules. Low orders are nonetheless useful (HJO Ch. 15). For water/cc-pVDZ see [[standard-models-h2-and-water]]: smooth convergence at $R_{\text{ref}}$, oscillation and overshoot at $2R_{\text{ref}}$.

## Source

Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, Chichester, 2000), Sec. 14.5, pp. 769-783, Eqs. (14.5.1)-(14.5.46), Figs. 14.1-14.7, Table 14.4. Recomputed for this note with NumPy (`hjo/c14/rspt.py`, `hjo/c14/ancont.py`). HJO's HF full-CI scans and Table 14.4 are quoted.
