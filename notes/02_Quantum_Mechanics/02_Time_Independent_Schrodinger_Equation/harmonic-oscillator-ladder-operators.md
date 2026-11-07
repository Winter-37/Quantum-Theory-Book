---
id: harmonic-oscillator-ladder-operators
title: The harmonic oscillator by ladder operators
summary: Algebraic solution of the 1D harmonic oscillator. Defines a± and [x,p] = iħ, factorizes H = ħω(a₊a₋ + ½), proves that a± raise and lower the energy by ħω, gets the ground state from a₋ψ₀ = 0, the spectrum (n + ½)ħω, the normalization √(n+1), √n, Hermitian conjugacy and orthonormality, and uses x, p in terms of a± to compute moments (virial split, σxσp = (n + ½)ħ). Checked with truncated ladder matrices and symbolic algebra.
status: in-progress
kind: derivation
level: introductory
tags: [harmonic-oscillator, ladder-operators, raising-lowering, commutator, canonical-commutation-relation, number-operator, griffiths]
prerequisites: [stationary-states, momentum-operator-and-ehrenfest-theorem]
related: [harmonic-oscillator-analytic-solution, de-broglie-and-heisenberg-uncertainty, creation-and-annihilation-operators, hellmann-feynman-and-virial-theorems, baker-campbell-hausdorff]
order: 30
date: 2026-11-04
---

## Why the oscillator

Expanding any smooth potential about a minimum $x_0$, with $V'(x_0)=0$ and the additive constant dropped:

$$
V(x) \approx \tfrac12V''(x_0)(x-x_0)^2 .
$$

Small oscillations about any equilibrium are therefore harmonic, with spring constant $k = V''(x_0)$ and $\omega = \sqrt{k/m}$. Molecular vibrations are the obvious chemical example. The problem is

$$
-\frac{\hbar^2}{2m}\psi'' + \frac12m\omega^2x^2\psi = E\psi
\quad\Longleftrightarrow\quad
\hat H = \frac{1}{2m}\left[\hat p^2 + (m\omega x)^2\right].
$$

This note solves it algebraically; [[harmonic-oscillator-analytic-solution]] solves the same equation by power series.

## The commutator $[x,\hat p]$

The commutator of two operators is defined as $[\hat A,\hat B] \equiv \hat A\hat B - \hat B\hat A$. Acting on a test function $f$:

$$
[x,\hat p]f = x(-i\hbar f') - (-i\hbar)(xf)' = i\hbar f
\quad\Longrightarrow\quad
[x,\hat p] = i\hbar .
$$

This is the **canonical commutation relation**.

## Ladder operators and factorization

If $\hat p$ and $x$ were numbers, $u^2+v^2 = (iu+v)(-iu+v)$ would factor the Hamiltonian. Because they do not commute, the factorization leaves a remainder. Define

$$
\hat a_\pm = \frac{1}{\sqrt{2\hbar m\omega}}\left(\mp i\hat p + m\omega x\right).
$$

Multiplying out, the cross terms combine into a commutator:

$$
\hat a_\mp\hat a_\pm = \frac{1}{2\hbar m\omega}\left[\hat p^2 + (m\omega x)^2\right] \mp \frac{i}{2\hbar}[x,\hat p]
= \frac{\hat H}{\hbar\omega} \pm \frac12 .
$$

Hence

$$
\hat H = \hbar\omega\left(\hat a_+\hat a_- + \tfrac12\right) = \hbar\omega\left(\hat a_-\hat a_+ - \tfrac12\right),
\qquad
[\hat a_-,\hat a_+] = 1 .
$$

## Climbing the ladder

**Claim.** If $\hat H\psi = E\psi$, then $\hat a_\pm\psi$ is a solution with energy $E\pm\hbar\omega$.

**Proof** (upper sign). Using $\hat a_-\hat a_+ = \hat a_+\hat a_- + 1$:

$$
\hat H(\hat a_+\psi) = \hbar\omega\left(\hat a_+\hat a_-\hat a_+ + \tfrac12\hat a_+\right)\psi
= \hat a_+\,\hbar\omega\left(\hat a_+\hat a_- + 1 + \tfrac12\right)\psi
= \hat a_+(\hat H + \hbar\omega)\psi = (E+\hbar\omega)(\hat a_+\psi).
$$

The lower sign follows the same way.

**Bottom rung.** Repeated lowering would eventually give $E<0 = V_{\min}$, which is impossible ([[stationary-states]]). The ladder must therefore stop at a state that the lowering operator annihilates, $\hat a_-\psi_0 = 0$:

$$
\left(\hbar\frac{d}{dx} + m\omega x\right)\psi_0 = 0
\quad\Longrightarrow\quad
\psi_0(x) = \left(\frac{m\omega}{\pi\hbar}\right)^{1/4}e^{-m\omega x^2/2\hbar}.
$$

**Spectrum.** $\hat H\psi_0 = \hbar\omega(\hat a_+\hat a_- + \tfrac12)\psi_0 = \tfrac12\hbar\omega\,\psi_0$. Climbing from there:

$$
E_n = \left(n+\tfrac12\right)\hbar\omega,\qquad n = 0,1,2,\ldots
$$

The spectrum is evenly spaced, and the zero-point energy is $\tfrac12\hbar\omega$.

**No other states** (Griffiths footnote 28). Any other solution would generate its own ladder. That ladder's bottom rung would also satisfy $\hat a_-\psi = 0$, whose only normalizable solution is $\psi_0$, so the second ladder is the same as the first.

## Normalization, conjugacy, orthonormality

**Hermitian conjugates.** For square-integrable $f,g$, integration by parts gives

$$
\int f^*(\hat a_\pm g)\,dx = \int(\hat a_\mp f)^*g\,dx .
$$

So $\hat a_\mp$ is the Hermitian conjugate of $\hat a_\pm$.

**Number operator.** From $\hat H = \hbar\omega(\hat a_+\hat a_- + \tfrac12)$, $\hat a_+\hat a_-\psi_n = n\psi_n$, and likewise $\hat a_-\hat a_+\psi_n = (n+1)\psi_n$.

**Normalization factors.** Write $\hat a_+\psi_n = c_n\psi_{n+1}$. Then

$$
|c_n|^2 = \int|\hat a_+\psi_n|^2dx = \int\psi_n^*\hat a_-\hat a_+\psi_n\,dx = n+1 .
$$

The lowering case is similar, and choosing the phases real:

$$
\hat a_+\psi_n = \sqrt{n+1}\,\psi_{n+1},\qquad
\hat a_-\psi_n = \sqrt n\,\psi_{n-1},\qquad
\psi_n = \frac{1}{\sqrt{n!}}(\hat a_+)^n\psi_0 .
$$

**Orthonormality.** Compute $\int\psi_m^*(\hat a_+\hat a_-)\psi_n\,dx$ in two ways. Acting to the right gives $n\int\psi_m^*\psi_n\,dx$; moving the operators to the left with the conjugacy relation gives $m\int\psi_m^*\psi_n\,dx$. Hence $(n-m)\int\psi_m^*\psi_n\,dx = 0$, so $\int\psi_m^*\psi_n\,dx = \delta_{mn}$.

The same algebra, with $\hat a_+\to a^\dagger$, reappears for fermions in [[creation-and-annihilation-operators]], with anticommutators in place of commutators.

## Moments without integrals

Inverting the definitions:

$$
x = \sqrt{\frac{\hbar}{2m\omega}}\,(\hat a_++\hat a_-),
\qquad
\hat p = i\sqrt{\frac{\hbar m\omega}{2}}\,(\hat a_+-\hat a_-).
$$

**Example: $x^2$.** $x^2 \propto \hat a_+^2 + \hat a_+\hat a_- + \hat a_-\hat a_+ + \hat a_-^2$. In $\langle\psi_n|x^2|\psi_n\rangle$ the terms $\hat a_\pm^2$ shift $n$ by $\pm2$ and drop out by orthogonality, leaving

$$
\langle x^2\rangle_n = \frac{\hbar}{2m\omega}(2n+1).
$$

Similarly, $\langle p^2\rangle_n = \tfrac12\hbar m\omega(2n+1)$ and $\langle x\rangle_n = \langle p\rangle_n = 0$.

**Consequences.**

- **Virial split.** $\langle V\rangle_n = \langle T\rangle_n = \tfrac12E_n$. Half the energy is potential and half kinetic, as the virial theorem requires for a quadratic potential ([[hellmann-feynman-and-virial-theorems]]).
- **Uncertainty.** $\sigma_x\sigma_p = (n+\tfrac12)\hbar$, saturating $\hbar/2$ only in the ground state.

## Worked examples

!!! example "Truncated ladder matrices ($\hbar=m=\omega=1$, 40 levels)"
    Build $\mathsf a_+$ with $(\mathsf a_+)_{n+1,n} = \sqrt{n+1}$, set $\mathsf a_- = \mathsf a_+^{\rm T}$, then $\mathsf x = (\mathsf a_++\mathsf a_-)/\sqrt2$, $\mathsf p = i(\mathsf a_+-\mathsf a_-)/\sqrt2$ and $\mathsf H = \tfrac12(\mathsf p^2+\mathsf x^2)$.

    | Check | Result |
    |---|---|
    | $[\mathsf a_-,\mathsf a_+]$ on the first 39 levels | the identity to $10^{-14}$ |
    | $[\mathsf a_-,\mathsf a_+]$ at the last level | $-39$ (truncation artefact: no finite matrices satisfy $[\mathsf x,\mathsf p] = i$, since the trace of a commutator is zero) |
    | $\mathsf H$ (first 30 levels) | diagonal: $0.5, 1.5, 2.5, \ldots$ |
    | $\langle x^2\rangle_n$, $\langle p^2\rangle_n$ for $n=0,\ldots,4$ | $n+\tfrac12$ |
    | $\langle V\rangle_n = \langle T\rangle_n$ | $(n+\tfrac12)/2$ |

    Symbolically (SymPy), $(\hat a_+)^n\psi_0/\sqrt{n!}$ equals the Hermite form of [[harmonic-oscillator-analytic-solution]] for $n = 0,\ldots,6$.

!!! example "Superposition $\Psi(x,0) = A[3\psi_0+4\psi_1]$ (Griffiths Problem 2.13)"
    **Normalization and energies.** $A = 1/5$. The energy is $\tfrac12\hbar\omega$ with probability $9/25$ and $\tfrac32\hbar\omega$ with probability $16/25$, so $\langle H\rangle = 1.14\,\hbar\omega$.

    **Position.** Only the cross term survives:

    $$
    \langle x\rangle(t) = 2\cdot\tfrac35\cdot\tfrac45\sqrt{\frac{\hbar}{2m\omega}}\cos\omega t = \frac{24}{25}\sqrt{\frac{\hbar}{2m\omega}}\cos\omega t .
    $$

    In units with $\hbar=m=\omega=1$ the amplitude is $0.678823$.

    **Momentum.** $\langle p\rangle = m\,d\langle x\rangle/dt$. Ehrenfest's theorem holds exactly here, because $V$ is quadratic ([[momentum-operator-and-ehrenfest-theorem]]).

    **Frequency.** $|\Psi|^2$ oscillates at exactly the classical frequency $\omega$, because adjacent levels differ by $\hbar\omega$. Mixing $\psi_0$ with $\psi_2$ would give $2\omega$.

## Source

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Secs. 2.3-2.3.1, Eqs. (2.42)-(2.70), Examples 2.4, 2.5; Problems 2.10-2.13. Page numbers are not given because the PDF used is an e-book rendering without print pagination. The trace argument for why finite matrices cannot satisfy $[x,p]=i\hbar$ is mine. Numbers recomputed with `griffiths/ch02_tise.py` (section C).
