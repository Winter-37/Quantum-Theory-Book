---
id: normalization-and-probability-current
title: Normalization, conservation of probability and the probability current
summary: Why a wave function normalized once stays normalized under the Schrödinger equation with a real potential, the continuity equation and probability current J, conservation of overlaps between two solutions, and how an imaginary potential −iΓ produces exponential decay with lifetime ħ/2Γ. Checked analytically and by Crank–Nicolson propagation.
status: in-progress
kind: derivation
level: introductory
tags: [normalization, square-integrable, continuity-equation, probability-current, unitarity, complex-potential, crank-nicolson, griffiths]
prerequisites: [wave-function-and-statistical-interpretation]
related: [momentum-operator-and-ehrenfest-theorem, stationary-states, hilbert-space-and-hermitian-operators, unitary-matrices-exponential-logarithm]
also: []
date: 2026-11-04
---

## Normalization

The Born rule needs the total probability to be one:

$$
\int_{-\infty}^{\infty} |\Psi(x,t)|^2\,dx = 1 .
$$

The Schrödinger equation is linear and homogeneous, so if $\Psi$ solves it so does $A\Psi$ for any complex constant $A$. Normalizing a solution means choosing $|A|$ so that the integral is 1. The phase of $A$ is left free and has no physical effect.

Two kinds of solutions cannot be normalized:

- $\Psi\equiv0$, which describes no particle at all;
- solutions with $\int|\Psi|^2dx = \infty$.

Physical states are therefore the **square-integrable** solutions ($\Psi\in L^2$). For the integral to converge, $|\Psi|$ must fall off faster than $|x|^{-1/2}$ as $|x|\to\infty$. Plane waves $e^{ikx}$ are not in $L^2$; they are used as idealized limits (see [[free-particle-and-wave-packets]]).

## Normalization is preserved in time

Normalization is imposed at one instant, say $t=0$. It would be inconsistent to impose it again later, since $A$ would then depend on $t$ and $A(t)\Psi$ would no longer solve the Schrödinger equation. The equation must therefore preserve the norm by itself. It does, provided $V$ is real.

**Step 1.** The integral depends only on $t$, so

$$
\frac{d}{dt}\int|\Psi|^2dx = \int\frac{\partial}{\partial t}|\Psi|^2dx,
\qquad
\frac{\partial}{\partial t}|\Psi|^2 = \Psi^*\frac{\partial\Psi}{\partial t} + \frac{\partial\Psi^*}{\partial t}\Psi .
$$

**Step 2.** The Schrödinger equation and its complex conjugate give, using $V^*=V$,

$$
\frac{\partial\Psi}{\partial t} = \frac{i\hbar}{2m}\frac{\partial^2\Psi}{\partial x^2} - \frac{i}{\hbar}V\Psi,
\qquad
\frac{\partial\Psi^*}{\partial t} = -\frac{i\hbar}{2m}\frac{\partial^2\Psi^*}{\partial x^2} + \frac{i}{\hbar}V\Psi^* .
$$

**Step 3.** Substituting, the potential terms cancel and what remains is a total $x$ derivative:

$$
\frac{\partial}{\partial t}|\Psi|^2
= \frac{i\hbar}{2m}\left(\Psi^*\frac{\partial^2\Psi}{\partial x^2} - \frac{\partial^2\Psi^*}{\partial x^2}\Psi\right)
= \frac{\partial}{\partial x}\left[\frac{i\hbar}{2m}\left(\Psi^*\frac{\partial\Psi}{\partial x} - \frac{\partial\Psi^*}{\partial x}\Psi\right)\right].
$$

The second equality holds because differentiating the bracket produces the two cross terms $\pm\Psi^{*\prime}\Psi'$, which cancel.

**Step 4.** Integrate over all $x$:

$$
\frac{d}{dt}\int_{-\infty}^{\infty}|\Psi|^2dx
= \frac{i\hbar}{2m}\left[\Psi^*\frac{\partial\Psi}{\partial x} - \frac{\partial\Psi^*}{\partial x}\Psi\right]_{-\infty}^{+\infty} = 0 .
$$

The boundary term vanishes because a normalizable $\Psi$ goes to zero at $\pm\infty$. Strictly, the step also needs $\partial\Psi/\partial x$ to stay bounded there. Griffiths assumes (his footnote 15) that $\Psi$ and all its derivatives vanish at infinity: mathematical counterexamples exist but do not arise in physics.

**Where $V^*=V$ was used.** In Step 3 the potential terms are $-(i/\hbar)(V - V^*)|\Psi|^2$, which is zero only for a real potential. The imaginary-potential section below shows what happens otherwise.

## The continuity equation

Define the **probability current**

$$
J(x,t) = \frac{i\hbar}{2m}\left(\Psi\frac{\partial\Psi^*}{\partial x} - \Psi^*\frac{\partial\Psi}{\partial x}\right)
= \frac{\hbar}{m}\,\mathrm{Im}\left(\Psi^*\frac{\partial\Psi}{\partial x}\right).
$$

Step 3 above is then the local conservation law

$$
\frac{\partial\rho}{\partial t} + \frac{\partial J}{\partial x} = 0,\qquad \rho = |\Psi|^2 .
$$

For the probability of finding the particle in $[a,b]$, $P_{ab}(t)=\int_a^b|\Psi|^2dx$, integrating gives

$$
\frac{dP_{ab}}{dt} = J(a,t) - J(b,t) .
$$

$J$ is the rate at which probability flows past a point, positive in the $+x$ direction. In one dimension it has units of 1/time.

**Two cases.**

- **Plane wave.** For $\Psi = Ae^{i(kx-\omega t)}$, $J = (\hbar k/m)|A|^2$: the density times the classical velocity $p/m$.
- **Real spatial part.** If $\Psi = f(x)e^{i\theta(t)}$ with $f$ real, then $\Psi^*\Psi' = ff'$ is real and $J=0$. This includes the Gaussian of Griffiths Problem 1.9 (Problem 1.14b) and every bound stationary state.

## Overlaps are conserved too

For two normalizable solutions $\Psi_1$ and $\Psi_2$ of the same Schrödinger equation (same real $V$), the same manipulation with $\Psi_1^*\Psi_2$ in place of $|\Psi|^2$ gives

$$
\frac{d}{dt}\int_{-\infty}^{\infty}\Psi_1^*\Psi_2\,dx
= \frac{i\hbar}{2m}\left[\Psi_1^*\frac{\partial\Psi_2}{\partial x} - \frac{\partial\Psi_1^*}{\partial x}\Psi_2\right]_{-\infty}^{+\infty} = 0 .
$$

All inner products are constant in time, not just norms. In the language of [[hilbert-space-and-hermitian-operators]], time evolution with a real (Hermitian) Hamiltonian is **unitary**.

## Imaginary potential: a model of decay

To describe an unstable particle with lifetime $\tau$, the total probability should decay. Griffiths Problem 1.17 does this crudely with a complex potential

$$
V = V_0 - i\Gamma, \qquad V_0 \text{ real},\ \Gamma>0 .
$$

Redoing Step 3 keeps the potential terms:

$$
\frac{\partial\rho}{\partial t} + \frac{\partial J}{\partial x} = \frac{i}{\hbar}(V^*-V)\rho = \frac{i}{\hbar}(2i\Gamma)\rho = -\frac{2\Gamma}{\hbar}\rho .
$$

Integrating over $x$ (the current term drops out as before):

$$
\frac{dP}{dt} = -\frac{2\Gamma}{\hbar}P
\quad\Longrightarrow\quad
P(t) = P(0)\,e^{-2\Gamma t/\hbar},
\qquad \tau = \frac{\hbar}{2\Gamma}.
$$

The non-Hermitian $-i\Gamma$ acts as a sink, removing probability uniformly from wherever $\rho$ is. The same device (a complex absorbing potential) is used in practice to model decay and to absorb outgoing waves at grid edges.

## Worked examples

!!! example "Normalizing $\Psi = Ae^{-\lambda|x|}e^{-i\omega t}$ (Griffiths Problem 1.5)"
    **Normalization.**

    $$
    1 = |A|^2\int_{-\infty}^{\infty}e^{-2\lambda|x|}dx = \frac{|A|^2}{\lambda}
    \quad\Longrightarrow\quad A=\sqrt\lambda .
    $$

    **Moments.** $\langle x\rangle=0$ by symmetry, and

    $$
    \langle x^2\rangle = 2\lambda\int_0^\infty x^2e^{-2\lambda x}dx = \frac{1}{2\lambda^2},
    \qquad \sigma_x = \frac{1}{\sqrt2\,\lambda}.
    $$

    **Probability outside $\pm\sigma_x$.**

    $$
    P_{\text{out}} = 2\lambda\int_{\sigma_x}^{\infty}e^{-2\lambda x}dx = e^{-2\lambda\sigma_x} = e^{-\sqrt2} = 0.24312 .
    $$

    **Current.** The spatial part is real, so $J=0$ everywhere.

!!! example "Numerical check: Crank–Nicolson propagation ($\hbar=m=1$)"
    **Setup.**

    - Grid: $x\in[-12,12]$, 2400 points, second-order finite-difference Laplacian.
    - Potential: $V=\tfrac12x^2+0.1x^4$.
    - Initial state: Gaussian with width $\sigma=0.7$, centred at $x_0=1.5$, $\langle p\rangle=0$.
    - Propagator: $\left(1+\tfrac{i}{2}H\Delta t\right)\Psi^{n+1}=\left(1-\tfrac{i}{2}H\Delta t\right)\Psi^n$ with $\Delta t=10^{-3}$.

    The Crank–Nicolson propagator is a Cayley transform of a Hermitian matrix, so it is exactly unitary: the discrete analogue of the proof above.

    | Check | Result |
    |---|---|
    | $\max|N(t)-1|$ over $0\le t\le3$ | $2.6\times10^{-14}$ |
    | Continuity residual $\max|\partial_t\rho+\partial_xJ|$ at $t=1.5$ (central differences) | $2.4\times10^{-4}$, against $\max|\partial_t\rho| = 0.70$ |
    | Imaginary potential, $\Gamma=0.2$: $P(t=2)$ numeric | 0.449330 |
    | $e^{-2\Gamma t}$ at $t=2$ | 0.449329 |

    The continuity residual is finite-difference error, not a violation.

## Source

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Sec. 1.4, Eqs. (1.20)-(1.27), footnotes 14-15; Problems 1.5, 1.14, 1.15, 1.17. Page numbers are not given because the PDF used is an e-book rendering without print pagination. The current $J$, the overlap result and the decay law are the answers to those problems, derived here, not quoted. Numbers recomputed with `griffiths/ch01_wave_function.py` (sections C, F, G).
