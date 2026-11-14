---
id: harmonic-oscillator-coherent-states
title: Coherent states of the harmonic oscillator
summary: Eigenstates of the lowering operator, a₋|α⟩ = α|α⟩. Covers moments (minimum uncertainty for every α), the expansion c_n = e^{−|α|²/2}αⁿ/√n! (Poisson weights), time evolution α → αe^{−iωt} (the state stays coherent and ⟨x⟩ follows the classical trajectory), why ⟨x⟩ oscillates at ω for any state, and the largest ⟨p⟩ for a ground/first-excited superposition. Checked with truncated ladder matrices.
status: in-progress
kind: derivation
level: intermediate
tags: [coherent-states, harmonic-oscillator, lowering-operator, minimum-uncertainty, poisson-distribution, quasi-classical, griffiths]
prerequisites: [harmonic-oscillator-ladder-operators, generalized-uncertainty-principle, energy-time-uncertainty-principle]
related: [harmonic-oscillator-analytic-solution, free-particle-and-wave-packets, position-momentum-and-energy-representations]
order: 70
date: 2026-11-04
---

## Motivation

Among the oscillator eigenstates only $\psi_0$ reaches $\sigma_x\sigma_p = \hbar/2$; the others give $(n+\tfrac12)\hbar$ ([[harmonic-oscillator-ladder-operators]]). Certain superpositions, called **coherent states**, also saturate the bound, keep doing so for all time, and move like a classical particle. They are the eigenstates of the lowering operator:

$$
\hat a_-|\alpha\rangle = \alpha|\alpha\rangle,\qquad \alpha\in\mathbb C .
$$

The raising operator has no normalizable eigenstates (Griffiths footnote 42).

## Moments

Use $x = \sqrt{\hbar/2m\omega}\,(\hat a_++\hat a_-)$ and $\hat p = i\sqrt{\hbar m\omega/2}\,(\hat a_+-\hat a_-)$, together with $\langle\alpha|\hat a_+ = \alpha^*\langle\alpha|$ (because $\hat a_+ = \hat a_-^\dagger$) and $\hat a_-\hat a_+ = \hat a_+\hat a_- + 1$.

**First moments.**

$$
\langle x\rangle = \sqrt{\frac{2\hbar}{m\omega}}\,\mathrm{Re}\,\alpha,\qquad
\langle p\rangle = \sqrt{2\hbar m\omega}\,\mathrm{Im}\,\alpha .
$$

**Second moments.**

$$
\langle x^2\rangle = \frac{\hbar}{2m\omega}\left[(\alpha+\alpha^*)^2+1\right],\qquad
\langle p^2\rangle = \frac{\hbar m\omega}{2}\left[1-(\alpha-\alpha^*)^2\right].
$$

**Spreads.**

$$
\sigma_x = \sqrt{\frac{\hbar}{2m\omega}},\qquad \sigma_p = \sqrt{\frac{\hbar m\omega}{2}},\qquad \sigma_x\sigma_p = \frac{\hbar}{2}\quad\text{for every }\alpha .
$$

The spreads equal those of the ground state. A coherent state is the ground-state Gaussian displaced in phase space to $(\langle x\rangle,\langle p\rangle)$, consistent with the minimum-uncertainty result of [[generalized-uncertainty-principle]].

## Energy-basis expansion

Write $|\alpha\rangle = \sum_nc_n|n\rangle$. Then

$$
\hat a_-|\alpha\rangle = \sum_nc_n\sqrt n\,|n-1\rangle = \alpha\sum_nc_n|n\rangle
\ \Rightarrow\ c_{n+1} = \frac{\alpha}{\sqrt{n+1}}c_n
\ \Rightarrow\ c_n = \frac{\alpha^n}{\sqrt{n!}}c_0,
$$

and normalization gives $|c_0|^2e^{|\alpha|^2} = 1$, so $c_0 = e^{-|\alpha|^2/2}$.

**Poisson statistics.** The energy-level probabilities are

$$
P(n) = e^{-|\alpha|^2}\frac{|\alpha|^{2n}}{n!},
$$

a Poisson distribution with $\langle n\rangle = \mathrm{var}(n) = |\alpha|^2$. This is the photon-number statistics of an ideal laser mode, since a field mode is an oscillator. Griffiths does not make this remark; it is standard.

## Time evolution: coherent states stay coherent

Attach $e^{-iE_nt/\hbar} = e^{-i\omega t/2}e^{-in\omega t}$ to each term:

$$
c_n(t) = e^{-i\omega t/2}\,e^{-|\alpha|^2/2}\,\frac{(\alpha e^{-i\omega t})^n}{\sqrt{n!}} .
$$

This is a coherent state (up to a global phase) with

$$
\alpha(t) = \alpha\,e^{-i\omega t}.
$$

**Classical motion.** Writing $\alpha = C\sqrt{m\omega/2\hbar}\,e^{i\phi}$:

$$
\langle x\rangle(t) = C\cos(\omega t-\phi),\qquad \sigma_x = \sqrt{\hbar/2m\omega}\ \text{(constant)}.
$$

The packet oscillates rigidly along the classical trajectory with amplitude $C$, without spreading. This is the quasi-classical behaviour, and a contrast with the free Gaussian, which always spreads ([[free-particle-and-wave-packets]]).

**Ground state.** $|0\rangle$ is itself coherent, with $\alpha = 0$.

## Any oscillator state: ⟨x⟩ oscillates at ω (Griffiths Problem 3.40)

For a general $\Psi = \sum c_n\psi_ne^{-iE_nt/\hbar}$, $x$ connects only $n$ and $n\pm1$, through $\langle n|x|n'\rangle = \sqrt{\hbar/2m\omega}\,(\sqrt{n'}\,\delta_{n,n'-1}+\sqrt n\,\delta_{n',n-1})$. Hence

$$
\langle x\rangle = C\cos(\omega t-\phi),\qquad Ce^{-i\phi} = \sqrt{\frac{2\hbar}{m\omega}}\sum_n\sqrt{n+1}\,c_{n+1}^*c_n .
$$

Only adjacent-level interference contributes, and adjacent levels differ by exactly $\hbar\omega$. This agrees with the generalized Ehrenfest theorem for a quadratic potential ([[energy-time-uncertainty-principle]]).

## Worked examples

!!! example "Numerical check ($\hbar=m=\omega=1$, 80 levels, $\alpha = 1.2\,e^{0.6i}$)"
    | Quantity | Result | Exact |
    |---|---|---|
    | $\sum|c_n|^2$ | 1.000000000000 | 1 |
    | $|\hat a_-c - \alpha c|$ (first 60 levels) | $1\times10^{-16}$ | 0 |
    | $\langle x\rangle$ | 1.400641 | $\sqrt2\,\mathrm{Re}\,\alpha$ = 1.400641 |
    | $\langle p\rangle$ | 0.958230 | $\sqrt2\,\mathrm{Im}\,\alpha$ = 0.958230 |
    | $\sigma_x = \sigma_p$ | 0.707107 | $1/\sqrt2$ |
    | $\sigma_x\sigma_p$ | 0.500000 | 1/2 |
    | $\langle n\rangle$, var $n$ | 1.440000, 1.440000 | $|\alpha|^2$ = 1.44 |

    After evolving each $c_n$ by $e^{-i(n+1/2)t}$, the state remains an eigenvector of $\hat a_-$ with eigenvalue $\alpha e^{-it}$ (residual $2\times10^{-16}$). $\langle x\rangle$ equals $\sqrt2|\alpha|\cos(t-\arg\alpha)$: 1.563092 at $t=1$ and $-0.548641$ at $t=2.5$.

!!! example "Largest ⟨p⟩ from E = ½ħω or 3/2ħω with equal probability (Griffiths Problem 3.41)"
    **Momentum of the superposition.** For $\Psi = (\psi_0 + e^{i\theta}\psi_1)/\sqrt2$,

    $$
    \langle p\rangle = \sqrt{2\hbar m\omega}\;\mathrm{Im}(c_0^*c_1) = \sqrt{\frac{\hbar m\omega}{2}}\sin\theta .
    $$

    **Maximum.** $\theta = \pi/2$ gives $\langle p\rangle_{\max} = \sqrt{\hbar m\omega/2}$. A scan over $\theta$ in 3601 steps confirms the maximum 0.707107.

    **Time evolution.** Starting from $\Psi(x,0) = (\psi_0+i\psi_1)/\sqrt2$:

    $$
    \Psi(x,t) = \frac{1}{\sqrt2}\left[\psi_0\,e^{-i\omega t/2} + i\,\psi_1\,e^{-3i\omega t/2}\right].
    $$

## Source

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Further Problems on Ch. 3: Problems 3.39 (Eq. 3.114), 3.40, 3.41, 3.42; footnote 42. Page numbers are not given because the PDF used is an e-book rendering without print pagination. All results are worked solutions to these problems (Griffiths gives only $c_0 = e^{-|\alpha|^2/2}$ and $\alpha(t) = \alpha e^{-i\omega t}$ as stated answers). The Poisson/laser remark is an addition. Numbers from `griffiths/ch03_formalism.py` (section F).
