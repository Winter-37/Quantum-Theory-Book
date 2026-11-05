---
id: heisenberg-picture-and-time-translation
title: Time evolution operator, Heisenberg picture and energy conservation
summary: For time-independent Ĥ, Û(t) = exp(−itĤ/ħ) generates translations in time. Heisenberg operators Q̂_H(t) = Û†Q̂Û obey iħ dQ̂_H/dt = [Q̂_H, Ĥ], which reproduces the classical equations of motion for the oscillator and the free particle. Time-translation invariance requires ∂Ĥ/∂t = 0 and implies energy conservation. Also covers the propagator K(x, x′, t) (Mehler kernel for the oscillator, free kernel) and the Galilean boost operator, all checked numerically.
status: in-progress
kind: derivation
level: intermediate
tags: [time-evolution-operator, heisenberg-picture, schrodinger-picture, heisenberg-equation-of-motion, propagator, mehler-kernel, energy-conservation, galilean-boost, griffiths]
prerequisites: [stationary-states, harmonic-oscillator-ladder-operators, translation-operator-and-translational-symmetry]
related: [symmetry-conservation-and-degeneracy, free-particle-and-wave-packets, harmonic-oscillator-coherent-states, momentum-operator-and-ehrenfest-theorem, energy-time-uncertainty-principle, baker-campbell-hausdorff, propagators-and-superoperators]
also: [02_Quantum_Mechanics/09_Symmetry_and_Group_Theory]
date: 2026-11-05
---

## The time-evolution operator

**Definition.** $\hat U(t)\Psi(x,0) = \Psi(x,t)$.

**Closed form.** If $\hat H$ does not depend on time, $\partial_t^n\Psi = (-i\hat H/\hbar)^n\Psi$, and the Taylor series in $t$ sums to

$$
\hat U(t) = e^{-it\hat H/\hbar}.
$$

The Hamiltonian is the **generator of translations in time**. $\hat U$ is unitary, and on stationary states it is just the phase $e^{-iE_nt/\hbar}$. So $\Psi(x,t) = \sum_nc_ne^{-iE_nt/\hbar}\psi_n(x)$ is the operator statement of "expand in stationary states and attach the wiggle factors" ([[stationary-states]]).

**When the series fails.** The Taylor argument assumes $\Psi$ is analytic in $t$, which can fail. Griffiths notes a counterexample (Holstein and Swift, Am. J. Phys. 40, 829, 1989; cited from the book, not checked here). The result survives if the exponential is defined spectrally, as for translations ([[translation-operator-and-translational-symmetry]]).

**Time-dependent $\hat H$.** Only the infinitesimal step survives:

$$
\hat U(t_0+\delta,t_0)\approx1-\frac{i}{\hbar}\hat H(t_0)\,\delta .
$$

## The Heisenberg picture

**Definition.** Apply the time translation to operators instead of states:

$$
\hat Q_H(t) = \hat U^\dagger(t)\,\hat Q\,\hat U(t),\qquad \Psi_H = \Psi(x,0).
$$

**Equivalence.** $\langle\Psi(t)|\hat Q|\Psi(t)\rangle = \langle\Psi_H|\hat Q_H(t)|\Psi_H\rangle$, so the two pictures give identical predictions. Griffiths' analogy: moving hands on a fixed dial versus a fixed hand on a counter-rotating dial.

**Equation of motion.** For $\hat Q$ and $\hat H$ without explicit time dependence, differentiating the definition gives (Problem 6.29)

$$
i\hbar\frac{d\hat Q_H}{dt} = [\hat Q_H,\hat H].
$$

**One particle in $V(x)$.**

$$
\frac{d\hat x_H}{dt} = \frac{\hat p_H}{m},\qquad \frac{d\hat p_H}{dt} = -V'(\hat x_H),
$$

which are Hamilton's equations, now as operator identities. Taking expectation values gives Ehrenfest's theorem ([[momentum-operator-and-ehrenfest-theorem]]).

**Infinitesimal step (Example 6.6).**

$$
\hat x_H(\delta)\approx\hat x+\frac{i\delta}{\hbar}[\hat H,\hat x] = \hat x+\frac{\hat p}{m}\delta,
$$

the quantum version of $x(\delta) = x(0)+v\delta$.

## Exactly solvable cases

**Oscillator (Example 6.7, Problem 6.26).** Acting on $\psi_n$ with $\hat x = \sqrt{\hbar/2m\omega}\,(\hat a_++\hat a_-)$ and replacing $e^{\pm i\hat Ht/\hbar}$ by its eigenvalue on each side:

$$
\hat x_H(t) = \sqrt{\frac{\hbar}{2m\omega}}\left(e^{i\omega t}\hat a_++e^{-i\omega t}\hat a_-\right) = \hat x\cos\omega t+\frac{\hat p}{m\omega}\sin\omega t,
$$

$$
\hat p_H(t) = \hat p\cos\omega t-m\omega\,\hat x\sin\omega t .
$$

These are exactly the classical spring solutions.

**Free particle (Problem 6.27).** $[\hat x,\hat H^n] = n(i\hbar/m)\hat p\hat H^{n-1}$ gives $[\hat x,\hat U] = (t/m)\hat p\hat U$, so

$$
\hat x_H(t) = \hat x+\frac{\hat p}{m}t,\qquad \hat p_H(t) = \hat p .
$$

In particular $\langle x^2\rangle_t$ grows like $t^2\langle p^2\rangle/m^2$ at late times, which is the spreading of a free packet ([[free-particle-and-wave-packets]]).

!!! example "Matrix checks (ħ = m = ω = 1, t = 1.37)"
    **Oscillator.** In an 80-state Fock basis, $\hat U^\dagger\hat x\hat U$ and $\hat U^\dagger\hat p\hat U$ match the formulas above to $5\times10^{-14}$ on the leading $60\times60$ block, away from the truncation edge.

    **Free particle.** On a 1024-point FFT grid, $\hat x_H(t)f$ equals $(\hat x+\hat pt)f$ to $3\times10^{-14}$ for a moving Gaussian.

## Time-translation invariance and energy conservation

**Invariance.** Evolution over an interval $\delta$ should not depend on when it starts: $\hat U(t_1+\delta,t_1) = \hat U(t_2+\delta,t_2)$. With the infinitesimal form this requires $\hat H(t_1) = \hat H(t_2)$ for all times, i.e. $\partial\hat H/\partial t = 0$.

**Conservation.** Then

$$
\frac{d\langle\hat H\rangle}{dt} = \frac i\hbar\langle[\hat H,\hat H]\rangle+\left\langle\frac{\partial\hat H}{\partial t}\right\rangle = 0 .
$$

Energy conservation follows from time-translation invariance. This completes the table in [[symmetry-conservation-and-degeneracy]].

## Propagators (Problem 6.30)

**Kernel.** Inserting $\sum_n|\psi_n\rangle\langle\psi_n|$:

$$
\Psi(x,t) = \int K(x,x',t)\,\Psi(x',0)\,dx',\qquad K(x,x',t) = \sum_n\psi_n^*(x')\,e^{-iE_nt/\hbar}\psi_n(x) .
$$

$|K|^2$ is the probability density for going from $x'$ to $x$ in time $t$.

**Oscillator.** Mehler's formula ($|z|<1$)

$$
\frac{1}{\sqrt{1-z^2}}\exp\!\left[-\frac{\xi^2+\eta^2-2\xi\eta z}{1-z^2}\right] = e^{-\xi^2-\eta^2}\sum_{n=0}^\infty\frac{z^n}{2^nn!}H_n(\xi)H_n(\eta),
$$

with $z = e^{-i\omega t}$ (as a limit from $|z|<1$), sums the series to

$$
K(x,x',t) = \sqrt{\frac{m\omega}{2\pi i\hbar\sin\omega t}}\exp\!\left\{\frac{im\omega\left[(x^2+x'^2)\cos\omega t-2xx'\right]}{2\hbar\sin\omega t}\right\}.
$$

**Free particle.** Replacing $\sum_n$ by $\int dp$ over $f_p(x) = e^{ipx/\hbar}/\sqrt{2\pi\hbar}$:

$$
K(x,x',t) = \sqrt{\frac{m}{2\pi i\hbar t}}\exp\!\left[\frac{im(x-x')^2}{2\hbar t}\right].
$$

!!! example "Propagating Gaussians (ħ = m = ω = 1, t = 1.37)"
    **Mehler identity.** At $\xi = 0.4$, $\eta = -0.9$, $z = 0.55$, both sides give $0.1689256576$, with the series summed to 80 terms.

    **Oscillator.** Start from $\Psi(x,0) = (2a/\pi)^{1/4}e^{-a(x-x_0)^2}$ with $a = 1.5$, $x_0 = 1.2$. Integrating against $K$ by quadrature reproduces $e^{-i\hat Ht}\Psi$ from exact diagonalization on a grid to $8\times10^{-14}$. The density is a Gaussian with

    $$
    \langle x\rangle = x_0\cos\omega t,\qquad
    \sigma^2(t) = \frac{1}{4a}\left[\cos^2\omega t+\left(\frac{2a\hbar}{m\omega}\right)^2\sin^2\omega t\right].
    $$

    Numerically: $\langle x\rangle = 0.239340$ and $\sigma^2 = 1.446960$, both matching the formulas to six figures. The width breathes at $2\omega$ unless $a = m\omega/2\hbar$, which is the coherent state of Problem 2.49 ([[harmonic-oscillator-coherent-states]]). The $\sigma^2(t)$ formula is my closed form, confirmed numerically.

    **Free particle.** Starting from $(2a/\pi)^{1/4}e^{-ax^2}$, $K$ gives $(2a/\pi)^{1/4}e^{-ax^2/(1+2i\hbar at/m)}/\sqrt{1+2i\hbar at/m}$, the result of Problem 2.21, to $2\times10^{-16}$.

## Galilean boosts (Problem 6.35)

**Operator.** A boost to a frame moving with velocity $-v$ is carried out at time $t$ by

$$
\hat\Gamma(v,t) = \exp\!\left[-\frac{i}{\hbar}v\,(t\hat p-m\hat x)\right].
$$

**Transformation of $\hat x$ and $\hat p$.** For infinitesimal $v = \delta$, $\hat x' = \hat x+\delta t$ and $\hat p' = \hat p+m\delta$: positions shift by $vt$ and momenta by $mv$, as a boost should.

**Factorization.** The two pieces of the exponent have a c-number commutator, so the BCH formula ([[baker-campbell-hausdorff]]) gives

$$
\hat\Gamma(v,t) = e^{\frac i\hbar(mvx-\frac12mv^2t)}\,\hat T(vt) = \hat T(vt)\,e^{\frac i\hbar(mvx+\frac12mv^2t)} .
$$

**Use.** If $\Psi$ solves the Schrödinger equation with $V(x)$, then $\hat\Gamma\Psi$ solves it with the moving potential $V(x-vt)$. In differentiating, note $\tfrac{d}{dt}e^{\hat A}\neq e^{\hat A}\tfrac{d\hat A}{dt}$ unless $\hat A$ commutes with $\tfrac{d\hat A}{dt}$.

!!! example "Grid check (v = 0.6, t = 0.9, m = 1)"
    **Exact exponential.** $\hat\Gamma$ was computed by matrix exponentiation on the FFT grid.

    | Test | Max deviation |
    |---|---|
    | $\hat\Gamma^\dagger\hat x\hat\Gamma f$ vs $(x+vt)f$ | $4\times10^{-14}$ |
    | $\hat\Gamma^\dagger\hat p\hat\Gamma f$ vs $(\hat p+mv)f$ | $1\times10^{-13}$ |
    | first factorized form | $1.6\times10^{-14}$ |
    | second factorized form | $1.5\times10^{-14}$ |

## Source

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Sec. 6.8 (6.8.1–6.8.2), Eqs. (6.67)–(6.79) (Eq. 6.70 sits in a footnote), Examples 6.6–6.7; Problems 6.26–6.30, 6.35. Page numbers are not given because the PDF used is an e-book rendering without print pagination. All numbers are computed in `griffiths/ch06_symmetry.py` (sections H and I). The Holstein–Swift reference is quoted from Griffiths' footnote and not checked. The closed form for $\sigma^2(t)$ and the late-time spreading remark are additions.
