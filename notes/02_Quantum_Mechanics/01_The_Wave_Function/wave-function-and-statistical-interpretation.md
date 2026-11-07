---
id: wave-function-and-statistical-interpretation
title: The wave function and Born's statistical interpretation
summary: The one-dimensional time-dependent Schrödinger equation, Born's rule for |Ψ|², the realist, orthodox and agnostic readings of a measurement, collapse, and the probability toolkit (densities, expectation values, variance) used in the rest of quantum mechanics. Includes two worked distributions with checked numbers.
status: in-progress
kind: theory
level: introductory
tags: [wave-function, born-rule, schrodinger-equation, probability, expectation-value, variance, measurement, griffiths]
prerequisites: []
related: [normalization-and-probability-current, momentum-operator-and-ehrenfest-theorem, de-broglie-and-heisenberg-uncertainty, generalized-statistical-interpretation, one-particle-rdm]
order: 10
date: 2026-11-04
---

## Overview

Classical mechanics describes one particle by a trajectory $x(t)$, obtained from Newton's law and initial data. Quantum mechanics replaces the trajectory by a complex function $\Psi(x,t)$, the **wave function**, which obeys a first-order-in-time wave equation. $\Psi$ does not say where the particle *is*; it gives a probability distribution for where a position measurement will find it. This note fixes the equation of motion, the probabilistic reading of $\Psi$, and the elementary statistics that the reading requires.

## The Schrödinger equation in one dimension

For a particle of mass $m$ on the $x$ axis in a real potential $V(x,t)$, the wave function obeys

$$
i\hbar\,\frac{\partial \Psi}{\partial t} = -\frac{\hbar^2}{2m}\,\frac{\partial^2 \Psi}{\partial x^2} + V\Psi .
$$

Here $\hbar = h/2\pi$, the reduced Planck constant. Griffiths quotes $\hbar = 1.054573\times10^{-34}$ J s; the SI value, exact since the 2019 redefinition fixed $h$, is $\hbar = 1.054571817\ldots\times10^{-34}$ J s (relative difference about $10^{-6}$, irrelevant for anything in these notes).

Three structural facts follow from the form of the equation:

1. **First order in $t$.** Specifying $\Psi(x,0)$ for all $x$ fixes $\Psi(x,t)$ for all later $t$. The quantum initial data is a whole function, not the pair $(x_0, v_0)$.
2. **Linear.** If $\Psi_1$ and $\Psi_2$ are solutions, so is $c_1\Psi_1 + c_2\Psi_2$ for any complex constants. Superposition is built in.
3. **Complex.** Because of the explicit $i$, a solution cannot stay real as it evolves: even when the spatial part is real, as for the stationary states of [[stationary-states]], the time factor $e^{-iEt/\hbar}$ is complex. Only $|\Psi|^2$, not $\Psi$ itself, carries a direct probabilistic meaning.

The Schrödinger equation is a postulate: it is not derived here from anything more basic.

## Born's statistical interpretation

**Born rule.** $|\Psi(x,t)|^2 = \Psi^*\Psi$ is the probability *density* for finding the particle at $x$ at time $t$:

$$
\int_a^b |\Psi(x,t)|^2\,dx = \text{probability that a position measurement at time } t \text{ gives a result in } [a,b].
$$

$|\Psi|^2$ has units of 1/length in one dimension, so $\Psi$ has units of length$^{-1/2}$.

**What a single measurement does.** Suppose a measurement finds the particle near a point $C$. Where was it just before? Griffiths sorts the possible answers into three positions:

| Position | Answer | Consequence |
|---|---|---|
| Realist | It was at $C$; we just did not know. | $\Psi$ is an incomplete description; extra "hidden variables" would be needed. |
| Orthodox (Copenhagen) | It was not anywhere definite; the measurement produced the value. | Measurement is a special kind of process, unlike ordinary Schrödinger evolution. |
| Agnostic | The question is not testable, so do not ask it. | Avoids the problem rather than solving it. |

Bell (1964) showed that the realist and orthodox answers make *different* experimental predictions (for entangled pairs), which removed the agnostic option. Experiments favour the orthodox answer over local hidden variables. Griffiths notes (his footnote 8) that this is slightly too strong: nonlocal hidden-variable theories (Bohm) and the many-worlds formulation do not fit the three boxes. The full argument is in Griffiths Ch. 12.

**Repeated measurement and collapse.** A second position measurement made immediately after the first returns the same value. In the orthodox picture this is explained by **collapse**: the measurement replaces $\Psi$ by a function sharply peaked at $C$, which then spreads again under the Schrödinger equation. There are thus two distinct kinds of evolution: smooth, deterministic, linear evolution under the Schrödinger equation between measurements, and abrupt, random collapse at a measurement. The theory itself does not say what physically counts as a measurement; Griffiths defers this to the Afterword.

**Interference.** A single electron sent through a double slit makes one dot on the screen, at a random place. Only the accumulated pattern of many independent electrons, each described by the same $\Psi$, reproduces the two-slit interference fringes. This is the Born rule seen directly: $|\Psi|^2$ is the histogram that emerges, dot by dot. Detecting which slit each electron used changes $\Psi$ (by collapse) and removes the fringes.

## Probability toolkit

### Discrete variables

Let a variable take values $j$ with counts $N(j)$, total $N=\sum_j N(j)$. Then:

$$
P(j) = \frac{N(j)}{N}, \qquad \sum_j P(j) = 1, \qquad \langle f(j)\rangle = \sum_j f(j)\,P(j).
$$

- **Most probable value:** the $j$ that maximizes $P(j)$.
- **Median:** the value with equal probability above and below.
- **Mean** (in quantum mechanics, the **expectation value**): $\langle j\rangle = \sum_j jP(j)$. It is an average over many trials, not the most likely single outcome, and need not even be an allowed value of $j$.

**Spread.** With $\Delta j = j - \langle j\rangle$, the mean deviation vanishes identically, $\langle\Delta j\rangle = \langle j\rangle - \langle j\rangle = 0$. The **variance** uses the square instead:

$$
\sigma^2 \equiv \langle(\Delta j)^2\rangle
= \langle j^2\rangle - 2\langle j\rangle\langle j\rangle + \langle j\rangle^2
= \langle j^2\rangle - \langle j\rangle^2 .
$$

The middle step uses that $\langle j\rangle$ is a constant that can be taken outside the sum. Since $\sigma^2\ge 0$,

$$
\langle j^2\rangle \ge \langle j\rangle^2 ,
$$

with equality only when every outcome is the same (no spread). The **standard deviation** is $\sigma$.

### Continuous variables

For a continuous variable the probability of any exact value is zero. The **probability density** $\rho(x)$ is defined by: the probability of finding a value in $[x, x+dx]$ is $\rho(x)\,dx$. Then

$$
P_{ab} = \int_a^b \rho(x)\,dx, \qquad
\int_{-\infty}^{\infty}\rho(x)\,dx = 1, \qquad
\langle f(x)\rangle = \int_{-\infty}^{\infty} f(x)\,\rho(x)\,dx,
$$

$$
\sigma^2 = \langle(\Delta x)^2\rangle = \langle x^2\rangle - \langle x\rangle^2 .
$$

A density may diverge at a point (see the falling rock below) as long as it stays integrable. For a particle, $\rho(x) = |\Psi(x,t)|^2$.

## Worked examples

!!! example "Discrete: the age distribution (Griffiths Sec. 1.3.1)"
    Fourteen people: one aged 14, one aged 15, three aged 16, two aged 22, two aged 24, five aged 25.

    | Quantity | Value |
    |---|---|
    | $N$ | 14 |
    | Most probable $j$ | 25 |
    | Median | 23 (7 people are younger and 7 older; the 7th and 8th ages are 22 and 24) |
    | $\langle j\rangle$ | $294/14 = 21$ |
    | $\langle j^2\rangle$ | $6434/14 = 459.5714$ |
    | $\sigma^2$ from $\langle(\Delta j)^2\rangle$ | 18.5714 |
    | $\sigma^2$ from $\langle j^2\rangle - \langle j\rangle^2$ | $459.5714 - 441 = 18.5714$ |
    | $\sigma$ | 4.3095 |

    Nobody in the room is 21 or 23: the mean and median need not be outcomes.

!!! example "Continuous: a falling rock photographed at random times (Griffiths Example 1.2, Problem 1.2)"
    A rock falls from rest through height $h$. Photographs are taken at uniformly random times during the fall, and the distance fallen, $x$, is read off each one.

    **Density.** $x = \tfrac12 g t^2$, $v = gt$, total time $T=\sqrt{2h/g}$. The fraction of photographs taken in $[t, t+dt]$ is $dt/T$, and

    $$
    \frac{dt}{T} = \frac{dx}{gt}\sqrt{\frac{g}{2h}} = \frac{dx}{2\sqrt{hx}}
    \quad\Longrightarrow\quad
    \rho(x) = \frac{1}{2\sqrt{hx}}, \quad 0\le x\le h .
    $$

    $\rho$ diverges at $x=0$ (the rock lingers near the top), yet $\int_0^h\rho\,dx = 1$.

    **Moments.**

    $$
    \langle x\rangle = \frac{h}{3},\qquad \langle x^2\rangle = \frac{h^2}{5},\qquad
    \sigma = \sqrt{\frac{h^2}{5}-\frac{h^2}{9}} = \frac{2h}{3\sqrt5} = 0.29814\,h .
    $$

    The mean, $h/3$, is less than $h/2$, as expected.

    **Probability of landing outside $\langle x\rangle\pm\sigma$.** The cumulative distribution is $F(x)=\sqrt{x/h}$. With $x_\pm = h/3 \pm \sigma = (0.63148,\ 0.03519)\,h$,

    $$
    P_{\text{out}} = 1 - \left(\sqrt{0.63148} - \sqrt{0.03519}\right) = 0.39294 .
    $$

    So about 39% of the photographs fall more than one standard deviation from the mean. A Gaussian would give 31.7%; the difference reflects the skewed, divergent density.

## Remarks

- The expectation value $\langle x\rangle$ of a quantum state is an **ensemble** average: the average of single position measurements on many identically prepared systems. It is not the average of repeated measurements on one system, because the first measurement collapses $\Psi$ and later ones just repeat its result.
- In three dimensions $|\Psi(\mathbf r)|^2$ has units of 1/volume. For $N$ electrons, integrating the $N$-particle $|\Psi|^2$ over all coordinates but one gives the electron density used in quantum chemistry ([[one-particle-rdm]]).

## Source

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Secs. 1.1-1.3, Eqs. (1.1)-(1.19), Example 1.1, Example 1.2, Problems 1.1-1.2, footnotes 3 and 8. Page numbers are not given because the PDF used is an e-book rendering without print pagination. Equations were read from the page images. All numbers recomputed for this note with `griffiths/ch01_wave_function.py` (sections A, B, H; SymPy and SciPy `constants`, CODATA 2018).
