---
id: translation-operator-and-translational-symmetry
title: The translation operator, Bloch's theorem and momentum conservation
summary: T̂(a)ψ(x) = ψ(x−a) equals exp(−iap̂/ħ), so momentum generates translations. T̂ is unitary; operators transform as Q̂' = T̂†Q̂T̂, giving x̂' = x̂ + a and p̂' = p̂. A Hamiltonian commuting with T̂(a) for one lattice spacing yields Bloch's theorem ψ = e^{iqx}u(x); commuting for every a yields [Ĥ, p̂] = 0 and momentum conservation. Checked by FFT, and Griffiths Problem 6.6 (bands of a square-well lattice from the u_nq equation) is solved and compared with the exact transfer-matrix condition.
status: in-progress
kind: derivation
level: intermediate
tags: [translation-operator, generator, unitary-transformation, active-passive, bloch-theorem, crystal-momentum, brillouin-zone, momentum-conservation, griffiths]
prerequisites: [position-momentum-and-energy-representations, hilbert-space-and-hermitian-operators]
related: [band-structure-and-the-dirac-comb, parity-and-parity-selection-rules, rotation-operator-and-rotational-symmetry, symmetry-conservation-and-degeneracy, one-dimensional-scattering-and-transfer-matrix, functions-of-matrices]
also: []
date: 2026-11-05
---

## Definition and generator

**Definition.** The translation operator shifts a function to the right by $a$:

$$
\hat T(a)\psi(x) = \psi(x-a).
$$

The new function takes at $x$ the value the old one had at $x-a$; the sign is that of an active shift to the right.

**Generator.** Expanding $\psi(x-a)$ in a Taylor series and writing $d/dx = (i/\hbar)\hat p$:

$$
\psi(x-a) = \sum_{n=0}^\infty\frac{(-a)^n}{n!}\frac{d^n\psi}{dx^n} = \sum_{n=0}^\infty\frac1{n!}\left(-\frac{ia}{\hbar}\hat p\right)^n\psi
\quad\Longrightarrow\quad
\hat T(a) = e^{-ia\hat p/\hbar}.
$$

Momentum is the **generator of translations**.

**Beyond Taylor series.** The result holds for any $\psi$ if the exponential is defined spectrally, $\hat T(a) = \int e^{-iap/\hbar}|p\rangle\langle p|\,dp$: multiply the momentum-space wave function by $e^{-iap/\hbar}$ and transform back (Problem 6.31). This is exactly an FFT shift, and it works for $\psi = \sqrt\lambda\,e^{-\lambda|x|}$ even though $\psi'$ is undefined at $0$ (see the example below).

**Unitarity.** Since $\hat p$ is Hermitian, $\hat T(a)^\dagger = e^{+ia\hat p/\hbar} = \hat T(-a) = \hat T(a)^{-1}$ (Problem 6.2: $e^{i\hat Q}$ is unitary for Hermitian $\hat Q$).

## How operators transform

**Definition.** The transformed operator $\hat Q'$ is fixed by requiring the same expectation value in the untranslated state as $\hat Q$ has in the translated one, $\langle\psi'|\hat Q|\psi'\rangle = \langle\psi|\hat Q'|\psi\rangle$ for all $\psi$. With $\psi' = \hat T\psi$,

$$
\hat Q' = \hat T^\dagger\hat Q\hat T .
$$

**Position and momentum.** On a test function, $\hat T(-a)\,x\,\hat T(a)f(x) = \hat T(-a)[x f(x-a)] = (x+a)f(x)$, so

$$
\hat x' = \hat x + a,\qquad \hat p' = \hat p,
$$

the second because $\hat p$ commutes with any function of $\hat p$. Since $\hat T^\dagger(\cdot)\hat T$ preserves products, every operator that is a power series in $\hat x$ and $\hat p$ transforms as $\hat Q'(\hat x,\hat p) = \hat Q(\hat x+a,\hat p)$ (Problem 6.4).

**Active and passive.** Shifting the wave function right by $a$ (active) or the coordinate origin left by $a$ (passive) give the same expectation values. In the passive picture, a point at distance $b$ from the old origin sits at $a+b$ from the new one, which is what $\hat x' = \hat x + a$ expresses.

## Translational symmetry

**Invariance.** A system is translationally invariant if $\hat T^\dagger\hat H\hat T = \hat H$, equivalently $[\hat H,\hat T] = 0$. For $\hat H = \hat p^2/2m + V(x)$ this is $V(x+a) = V(x)$. Two cases:

- **continuous**: true for all $a$ (only a constant potential, for one particle);
- **discrete**: true for $a$ a multiple of a lattice spacing (a crystal).

### Discrete symmetry: Bloch's theorem

**Common eigenstates.** Commuting operators share an eigenbasis, so stationary states can be chosen with $\hat T(a)\psi = \lambda\psi$. A unitary operator has $|\lambda| = 1$; Griffiths writes $\lambda = e^{-iqa}$ with $\hbar q$ the **crystal momentum**:

$$
\psi(x-a) = e^{-iqa}\psi(x)
\quad\Longleftrightarrow\quad
\psi(x) = e^{iqx}u(x),\quad u(x+a) = u(x).
$$

The equivalence: define $u = e^{-iqx}\psi$; then $u(x-a) = e^{-iqx}e^{iqa}\psi(x-a) = u(x)$ (Problem 6.5).

**Meaning.** Stationary states in a periodic potential are travelling waves modulated by a periodic function, with nonzero velocity. An electron can cross a perfect crystal without scattering; resistance comes from imperfections and thermal motion. The states themselves need not be invariant, only chosen as eigenstates of $\hat T$.

**Brillouin zone.** $q$ and $q+2\pi/a$ give the same $\lambda$, so $qa\in(-\pi,\pi]$ suffices: the first Brillouin zone. The Dirac-comb bands and the transfer-matrix condition $\cos qa = \tfrac12\mathrm{Tr}\,\mathsf T$ are worked out in [[band-structure-and-the-dirac-comb]].

**Equation for $u$.** Substituting $\psi = e^{iqx}u_{nq}$ into the Schrödinger equation:

$$
-\frac{\hbar^2}{2m}u_{nq}'' - \frac{i\hbar^2q}{m}u_{nq}' + V(x)u_{nq} = \left(E_{nq}-\frac{\hbar^2q^2}{2m}\right)u_{nq},
$$

an eigenvalue problem on one cell with **periodic** boundary conditions.

### Continuous symmetry: momentum conservation

For an infinitesimal shift, $\hat T(\delta)\approx1-i\delta\hat p/\hbar$, so $[\hat H,\hat T(\delta)] = 0$ requires $[\hat H,\hat p] = 0$. By the generalized Ehrenfest theorem,

$$
\frac{d\langle\hat p\rangle}{dt} = \frac i\hbar\langle[\hat H,\hat p]\rangle = 0 .
$$

Momentum conservation is a consequence of translational symmetry. The nontrivial case is interacting particles: for $V(|x_1-x_2|)$ the joint translation is $e^{-ia(\hat p_1+\hat p_2)/\hbar}$, it commutes with $\hat H$, and the total momentum is conserved (Problem 6.7). The probability distribution of $p$, not only its mean, is constant ([[symmetry-conservation-and-degeneracy]]).

## Worked examples

!!! example "FFT checks (ħ = 1, 4096-point grid on [−40, 40))"
    $\hat T(a)$ is applied as $e^{-ika}$ in Fourier space, with $a = 2.7$.

    | Test | Max deviation |
    |---|---|
    | Gaussian packet $e^{-(x-1)^2}\cos3x$: $\hat T\psi$ vs $\psi(x-a)$ | $3\times10^{-16}$ |
    | $\hat T^\dagger\hat x\hat T f$ vs $(x+a)f$ | $4\times10^{-15}$ |
    | $\hat T^\dagger\hat p\hat T f$ vs $\hat p f$ | $3\times10^{-14}$ |
    | Cusp $\sqrt\lambda e^{-\lambda|x|}$, $\lambda = 1.3$ (Problem 6.31) | $4.7\times10^{-3}$ max, $1.1\times10^{-4}$ rms |

    The cusp error is Gibbs ringing confined to the kink and shrinks as the grid is refined. The spectral definition shifts the function correctly even where its Taylor series does not exist.

!!! example "Bands of a square-well lattice (Problem 6.6)"
    **Set-up.** Units $\hbar = m = a = 1$. In each cell $V = -V_0$ for $\tfrac14<x<\tfrac34$ and $0$ otherwise, with $V_0 = 20\hbar^2/2ma^2 = 10$.

    **Method 1 (as Griffiths asks).** Discretize the $u_{nq}$ equation on a periodic grid of $M$ points. The first derivative is the central difference $(u_{j+1}-u_{j-1})/2\Delta x$; then $-i q\,D_1$ is Hermitian and the matrix can be diagonalized with a Hermitian solver.

    **Method 2 (exact check).** Multiply the $2\times2$ transfer matrices of the three pieces of the cell and solve $\cos qa = \tfrac12\mathrm{Tr}\,\mathsf T(E)$ by root finding ([[one-dimensional-scattering-and-transfer-matrix]]).

    | $qa$ | $E_1$ ($M=1600$) | $E_1$ exact | $E_2$ ($M=1600$) | $E_2$ exact |
    |---|---|---|---|---|
    | $0$ | −5.99465 | −5.99465 | 14.42401 | 14.42404 |
    | $\pm\pi/2$ | −5.03022 | −5.03022 | 6.77601 | 6.77601 |
    | $\pm\pi$ | −3.49096 | −3.49097 | 2.80914 | 2.80912 |

    Energies are in units of $\hbar^2/ma^2$; with $M = 400$ the agreement is still about $10^{-3}$.

    **Reading the table.**

    - Band 1 is a narrow bound band: it runs from $-5.995$ at $q=0$ to $-3.491$ at the zone edge. It is the single-well bound state broadened by tunnelling.
    - A gap of about $6.3$ separates it from band 2. Band 2 starts at the zone edge ($2.809$) and rises to $14.424$ at $q = 0$.
    - $E(q) = E(-q)$, as time reversal requires for a real potential ([[symmetry-conservation-and-degeneracy]]).

    **Sign in the problem statement.** Griffiths' note to Problem 6.6 labels states as $\psi_{nq} = e^{-iqx}u_{nq}$. That clashes with Eq. (6.12) and with the $u$ equation of part (a), which follows from $e^{+iqx}u$. With $e^{-iqx}$ the first-derivative term changes sign, which is the same as $q\to-q$. The energies are unaffected.

## Source

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Secs. 6.1–6.2, Eqs. (6.1)–(6.14), Example 6.1, Figs. 6.2, 6.5, 6.6 (described); Problems 6.2–6.7, 6.31. Page numbers are not given because the PDF used is an e-book rendering without print pagination. All numbers are computed in `griffiths/ch06_symmetry.py` (sections A and B). The transfer-matrix cross-check of Problem 6.6 is an addition.
