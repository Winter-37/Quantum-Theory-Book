---
id: delta-function-potential
title: Bound and scattering states; the delta-function well
summary: The bound/scattering classification by the potential at infinity, the Dirac delta and why it makes ψ′ jump, the single bound state E = −mα²/2ħ² of the delta well, reflection and transmission for scattering (identical for well and barrier), the uncertainty product of the bound state, and the double-delta well (even/odd bound states, existence condition for the odd one, transmission).
status: in-progress
kind: derivation
level: introductory
tags: [delta-function, bound-states, scattering-states, boundary-conditions, reflection, transmission, tunnelling, double-well, griffiths]
prerequisites: [stationary-states, free-particle-and-wave-packets]
related: [finite-square-well, one-dimensional-scattering-and-transfer-matrix, de-broglie-and-heisenberg-uncertainty, normalization-and-probability-current]
order: 60
date: 2026-11-04
---

## Bound versus scattering states

Classically, a particle trapped between turning points is **bound**, and one that comes in from infinity and returns there is **scattered**. Quantum tunnelling lets a particle leak through any finite barrier, so only the potential at infinity decides:

$$
E < V(-\infty)\ \text{and}\ E < V(+\infty):\ \text{bound};\qquad
E > V(-\infty)\ \text{or}\ E > V(+\infty):\ \text{scattering}.
$$

When $V\to0$ at both ends this reduces to $E<0$ (bound) versus $E>0$ (scattering). Bound states are normalizable and discretely labelled (a sum over $n$). Scattering states are not normalizable and are continuously labelled (an integral over $k$).

## The delta function and the derivative jump

**Definition.** $\delta(x)$ is zero for $x\neq0$ with $\int\delta\,dx = 1$. It is a distribution, defined by what it does under an integral:

$$
\int f(x)\,\delta(x-a)\,dx = f(a).
$$

**Integrating the TISE across a point.** Integrate from $-\epsilon$ to $\epsilon$ and let $\epsilon\to0$:

$$
\Delta\!\left(\frac{d\psi}{dx}\right) \equiv \psi'(0^+)-\psi'(0^-) = \frac{2m}{\hbar^2}\lim_{\epsilon\to0}\int_{-\epsilon}^{\epsilon}V(x)\psi(x)\,dx .
$$

For finite $V$ the right side vanishes, so $\psi'$ is continuous. This is the general justification for the two standard boundary conditions:

1. $\psi$ is always continuous;
2. $\psi'$ is continuous except where $V$ is infinite.

For $V = -\alpha\delta(x)$ with $\alpha>0$,

$$
\Delta\psi' = -\frac{2m\alpha}{\hbar^2}\,\psi(0).
$$

## The single bound state

**Form of the solution.** For $E<0$ set $\kappa = \sqrt{-2mE}/\hbar$. Normalizability selects $Be^{\kappa x}$ for $x<0$ and $Fe^{-\kappa x}$ for $x>0$, and continuity of $\psi$ gives $F=B$.

**Derivative jump.** $\psi'$ jumps from $+B\kappa$ to $-B\kappa$, so $-2B\kappa = -2m\alpha B/\hbar^2$:

$$
\kappa = \frac{m\alpha}{\hbar^2},\qquad
E = -\frac{m\alpha^2}{2\hbar^2},\qquad
\psi(x) = \frac{\sqrt{m\alpha}}{\hbar}\,e^{-m\alpha|x|/\hbar^2}.
$$

There is exactly one bound state, whatever the strength $\alpha$.

**Uncertainty** (Griffiths Problem 2.24). $\langle x^2\rangle = \hbar^4/2m^2\alpha^2$ and $\langle p^2\rangle = (m\alpha/\hbar)^2$, so

$$
\sigma_x\sigma_p = \frac{\hbar}{\sqrt2}.
$$

The kink must be handled with care: $\psi''$ contains a $\delta$ at the origin. This is the same cusp state, with the same pitfall, as in [[de-broglie-and-heisenberg-uncertainty]].

## Scattering from the delta well

**Setup.** For $E>0$ set $k = \sqrt{2mE}/\hbar$, with $\psi = Ae^{ikx}+Be^{-ikx}$ on the left and $Fe^{ikx}+Ge^{-ikx}$ on the right. Here $A$ is the incident amplitude, $B$ reflected, $F$ transmitted, and $G=0$ for a beam from the left.

**Boundary conditions.** Continuity gives $A+B = F$. The jump condition, with $\beta\equiv m\alpha/\hbar^2k$, gives $F - A + B = 2i\beta(A+B)$. Solving:

$$
B = \frac{i\beta}{1-i\beta}A,\qquad F = \frac{1}{1-i\beta}A .
$$

**Coefficients.**

$$
R = \frac{|B|^2}{|A|^2} = \frac{\beta^2}{1+\beta^2} = \frac{1}{1+2\hbar^2E/m\alpha^2},
\qquad
T = \frac{|F|^2}{|A|^2} = \frac{1}{1+\beta^2} = \frac{1}{1+m\alpha^2/2\hbar^2E},
$$

and $R+T=1$. Since $R$ and $T$ depend on $\alpha^2$ only, a delta **barrier** ($\alpha<0$) transmits exactly as much as the well. A particle tunnels through an infinitely high spike with probability $T$, which approaches 1 at high energy.

**Interpretation.** The scattering states are not normalizable. $R$ and $T$ are the reflection and transmission probabilities for a wave packet whose energies are sharply peaked near $E$. Building the packet explicitly is a numerical job; Griffiths footnote 48 points to software for it.

## Double delta well (Griffiths Problems 2.27-2.28)

**Potential.** $V = -\alpha[\delta(x+a)+\delta(x-a)]$. Write $g = m\alpha/\hbar^2$.

**Bound states** have $\psi\propto\cosh\kappa x$ (even) or $\sinh\kappa x$ (odd) between the spikes and $e^{-\kappa|x|}$ outside. The jump condition at $x=a$ gives

$$
\text{even:}\quad \kappa\left(1+\tanh\kappa a\right) = 2g,\qquad
\text{odd:}\quad \kappa\left(1+\coth\kappa a\right) = 2g .
$$

$\kappa(1+\coth\kappa a)\ge 1/a$, with equality only as $\kappa\to0$, so an odd bound state exists only if $\alpha > \hbar^2/2ma$. The even state always exists.

**Limits.**

- As $a\to\infty$ (with $\alpha$ fixed), both energies tend to the single-well value $-m\alpha^2/2\hbar^2$, a two-fold degeneracy.
- As $a\to0$, the two wells merge into a single delta of strength $2\alpha$, with energy $-2m\alpha^2/\hbar^2$, and the odd state is lost.

The even (bonding) state lies below the single-well energy and the odd (antibonding) state above it. This is the one-dimensional cartoon of the H₂⁺ bonding and antibonding pair.

!!! example "Numbers (energies in units of $\hbar^2/ma^2$)"
    | $\alpha$ | Even $E$ | Odd $E$ | Single-well $E$ |
    |---|---|---|---|
    | $\hbar^2/ma$ | $-0.614783$ | $-0.317455$ | $-0.5$ |
    | $\hbar^2/4ma$ | $-0.068235$ | none ($\alpha < \hbar^2/2ma$) | $-0.03125$ |

    **Transmission.** In the transfer-matrix language of [[one-dimensional-scattering-and-transfer-matrix]], $\mathsf M = \mathsf M_2\mathsf M_1$ and $T = 1/|M_{22}|^2$. With $\beta = g/k$:

    $$
    T^{-1} = \left|(1-i\beta)^2 + \beta^2e^{4ika}\right|^2 = 1 + 4\beta^2\left(\cos2ka - \beta\sin2ka\right)^2 .
    $$

    Check with $\alpha = \hbar^2/ma$ and $\hbar=m=a=1$ (so $g=1$):

    | $E$ | Matrix product | Closed form | Brute-force thin wells |
    |---|---|---|---|
    | 0.3 | 0.085199 | 0.085199 | 0.085199 |
    | 1.0 | 0.267804 | 0.267804 | 0.267805 |
    | 3.0 | 0.813368 | 0.813368 | 0.813369 |

    **Single-delta check.** A rectangle of depth $10^5$ and width $10^{-5}$ reproduces $T = 1/(1+\beta^2)$ to $2\times10^{-6}$ at $E = 0.1, 0.5, 2.0$, with $R+T=1$ to $10^{-8}$.

## Source

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Sec. 2.5, Eqs. (2.112)-(2.147), Figs. 2.11-2.15 (described); Problems 2.22-2.28, 2.54(d); footnotes 44-48. Page numbers are not given because the PDF used is an e-book rendering without print pagination. The double-delta conditions, the odd-state threshold, the closed-form $T$ and all numbers are derived here, not quoted. Recomputed with `griffiths/ch02_tise.py` (section F).
