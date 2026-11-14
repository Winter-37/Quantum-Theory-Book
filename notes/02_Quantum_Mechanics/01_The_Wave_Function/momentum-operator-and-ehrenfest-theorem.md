---
id: momentum-operator-and-ehrenfest-theorem
title: Expectation values, the momentum operator and Ehrenfest's theorem
summary: Expectation values as ensemble averages, the derivation of d⟨x⟩/dt that motivates p → −iħ∂/∂x, the operator rule for ⟨Q(x,p)⟩, Ehrenfest's theorem d⟨p⟩/dt = ⟨−∂V/∂x⟩ and why it is not Newton's law for ⟨x⟩ in an anharmonic potential, and the effect of a constant potential shift. Checked numerically on a quartic well.
status: in-progress
kind: derivation
level: introductory
tags: [expectation-value, momentum-operator, ehrenfest-theorem, operators, classical-limit, gauge-phase, griffiths]
prerequisites: [wave-function-and-statistical-interpretation, normalization-and-probability-current]
related: [de-broglie-and-heisenberg-uncertainty, generalized-statistical-interpretation, hilbert-space-and-hermitian-operators, hellmann-feynman-and-virial-theorems]
order: 30
date: 2026-11-04
---

## Expectation value of position

For a particle in state $\Psi$,

$$
\langle x\rangle = \int_{-\infty}^{\infty} x\,|\Psi(x,t)|^2\,dx .
$$

This is the mean of single position measurements on an ensemble of identically prepared systems, each measured once. It is not what one gets by measuring one particle repeatedly, since after the first measurement $\Psi$ has collapsed.

All integrals below run over $(-\infty,\infty)$, and $\Psi$ and its derivatives are assumed to vanish at $\pm\infty$, so boundary terms from integration by parts drop.

## How fast does $\langle x\rangle$ move?

Differentiate under the integral (the variable $x$ does not depend on $t$) and use $\partial_t|\Psi|^2$ from [[normalization-and-probability-current]]:

$$
\frac{d\langle x\rangle}{dt} = \int x\,\frac{\partial|\Psi|^2}{\partial t}\,dx
= \frac{i\hbar}{2m}\int x\,\frac{\partial}{\partial x}\left(\Psi^*\frac{\partial\Psi}{\partial x} - \frac{\partial\Psi^*}{\partial x}\Psi\right)dx .
$$

**First integration by parts.** Move the derivative off the bracket onto $x$, using $\partial x/\partial x=1$:

$$
\frac{d\langle x\rangle}{dt} = -\frac{i\hbar}{2m}\int\left(\Psi^*\frac{\partial\Psi}{\partial x} - \frac{\partial\Psi^*}{\partial x}\Psi\right)dx .
$$

**Second integration by parts,** on the second term only: $\int\Psi^{*\prime}\Psi\,dx = -\int\Psi^*\Psi'\,dx$. The two terms become equal, so

$$
\frac{d\langle x\rangle}{dt} = -\frac{i\hbar}{m}\int\Psi^*\frac{\partial\Psi}{\partial x}\,dx .
$$

Note that the time derivative cannot instead be moved onto $x$ in the first expression (Problem 1.6). That would give zero, but the step is illegitimate: $\partial/\partial t$ acts on $|\Psi|^2$, which depends on $t$, and $x$ is an integration variable, not a function of time.

## Momentum as an operator

The velocity of a particle that has no definite position is not defined, but the rate of change of $\langle x\rangle$ is. Griffiths postulates $\langle v\rangle \equiv d\langle x\rangle/dt$, which gives

$$
\langle p\rangle = m\frac{d\langle x\rangle}{dt} = \int\Psi^*\left(-i\hbar\frac{\partial}{\partial x}\right)\Psi\,dx .
$$

**$\langle p\rangle$ is real.** Integrating by parts, $\int\Psi^*\Psi'dx = -\int\Psi^{*\prime}\Psi\,dx = -\left(\int\Psi^*\Psi'dx\right)^*$. So $\int\Psi^*\Psi'dx$ is purely imaginary, and multiplying by $-i\hbar$ gives a real number. This is the first instance of Hermiticity ([[hilbert-space-and-hermitian-operators]]).

**The operator rule.** $\langle x\rangle$ and $\langle p\rangle$ have the same "sandwich" form $\int\Psi^*[\hat Q]\Psi\,dx$, with

$$
\hat x = x\ (\text{multiply}),\qquad \hat p = -i\hbar\frac{\partial}{\partial x}.
$$

Any classical dynamical variable $Q(x,p)$ is then promoted by replacing $p\to-i\hbar\,\partial/\partial x$:

$$
\langle Q(x,p)\rangle = \int\Psi^*\,Q\!\left(x,-i\hbar\frac{\partial}{\partial x}\right)\Psi\,dx .
$$

For example, with $T=p^2/2m$,

$$
\langle T\rangle = -\frac{\hbar^2}{2m}\int\Psi^*\frac{\partial^2\Psi}{\partial x^2}\,dx = \frac{\hbar^2}{2m}\int\left|\frac{\partial\Psi}{\partial x}\right|^2dx .
$$

The second form (after one integration by parts) is manifestly non-negative. It is also the safe form when $\Psi$ has a kink, as in [[de-broglie-and-heisenberg-uncertainty]].

Griffiths treats this rule as a working axiom and justifies it in Ch. 3 ([[generalized-statistical-interpretation]]).

A remark that is not in Griffiths Ch. 1: the substitution is ambiguous for products such as $xp$, because $\hat x\hat p\neq\hat p\hat x$. The usual fix is the Hermitian combination $\tfrac12(\hat x\hat p+\hat p\hat x)$. The ambiguity does not arise for $T+V(x)$.

## Ehrenfest's theorem

Differentiate $\langle p\rangle$ in time and substitute the Schrödinger equation:

$$
\frac{d\langle p\rangle}{dt} = -i\hbar\int\left(\frac{\partial\Psi^*}{\partial t}\frac{\partial\Psi}{\partial x} + \Psi^*\frac{\partial^2\Psi}{\partial x\,\partial t}\right)dx .
$$

**Kinetic terms.** After two integrations by parts the terms containing $\partial^2\Psi/\partial x^2$ cancel in pairs.

**Potential terms.** They leave $\int\left(V\Psi^*\Psi' - \Psi^*(V\Psi)'\right)dx = -\int\Psi^*V'\Psi\,dx$. With the prefactor $-i\hbar\cdot(\pm i/\hbar)$ this gives

$$
\frac{d\langle p\rangle}{dt} = \left\langle -\frac{\partial V}{\partial x}\right\rangle .
$$

Together with $\langle p\rangle = m\,d\langle x\rangle/dt$, this is **Ehrenfest's theorem**: expectation values satisfy equations of the same form as Hamilton's equations.

**Caveat: it is not Newton's law for $\langle x\rangle$.** The force on the right is $\langle F(x)\rangle$, the average of the force over the distribution. Newton's law for $\langle x\rangle$ would need $F(\langle x\rangle)$, the force evaluated at the mean position. The two agree for every state only when $F$ is linear in $x$, that is, when $V$ is at most quadratic (free particle, uniform field, harmonic oscillator). Expanding $F$ about $\langle x\rangle$ gives

$$
\langle F\rangle = F(\langle x\rangle) + \tfrac12F''(\langle x\rangle)\,\sigma_x^2 + \cdots .
$$

The centroid of a wave packet therefore follows the classical trajectory only while $\sigma_x$ is small on the scale over which $F$ curves.

## Constant potential shift

Replace $V(x)$ by $V(x)+V_0$, with $V_0$ independent of both $x$ and $t$ (Griffiths Problem 1.8). If $\Psi$ solves the original equation, then

$$
\tilde\Psi = \Psi\,e^{-iV_0t/\hbar}
$$

solves the shifted one: the time derivative of the phase supplies exactly the extra $V_0\tilde\Psi$. The added phase is global (the same at every $x$), so it cancels in every $\int\tilde\Psi^*\hat Q\tilde\Psi\,dx$. No expectation value changes, just as in classical mechanics, where only differences of potential matter.

## Worked example

!!! example "Ehrenfest in a quartic well (numerical, $\hbar=m=1$)"
    **Setup.** $V=\tfrac12x^2+0.1x^4$. A Gaussian with width $0.7$, released from rest at $x_0=1.5$, is propagated to $t=3$ with Crank–Nicolson ($\Delta t=10^{-3}$, 2400 grid points on $[-12,12]$). Time derivatives are taken by central differences of the stored expectation values.

    | Check | Result |
    |---|---|
    | $\max|d\langle x\rangle/dt - \langle p\rangle|$ | $1.8\times10^{-5}$ (with $\max|\langle p\rangle| = 2.00$) |
    | $\max|d\langle p\rangle/dt - \langle -V'\rangle|$ | $5.5\times10^{-4}$ (with $\max|\langle -V'\rangle| = 3.73$) |
    | $\max|\langle -V'\rangle - (-V'(\langle x\rangle))|$ | **0.997** |
    | $(\langle x\rangle,\langle p\rangle)$ at $t=3$ | $(-0.468,\ 1.630)$ |

    Ehrenfest's theorem holds to grid accuracy. The force at the mean position, however, differs from the mean force by up to about 27% of the peak force: the quartic term makes $F''\neq0$, so $\langle x\rangle$ does not follow the classical trajectory of a point particle started at $x_0=1.5$.

## Source

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Sec. 1.5, Eqs. (1.28)-(1.38), footnotes 16-19; Problems 1.6, 1.7, 1.8. Page numbers are not given because the PDF used is an e-book rendering without print pagination. The remarks on operator ordering and on the expansion of $\langle F\rangle$ are mine, not Griffiths's. Numerical example recomputed with `griffiths/ch01_wave_function.py` (section F).
