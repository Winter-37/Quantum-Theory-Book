---
id: two-particle-systems-and-reduced-mass
title: Two-particle systems, entanglement and the reduced mass
summary: The two-particle wave function Ψ(r₁, r₂, t) and its Schrödinger equation. Two exactly separable cases are worked out. Non-interacting particles give product states, and their superpositions can be entangled. Central two-body forces separate into free centre-of-mass motion plus relative motion with the reduced mass μ = m₁m₂/(m₁+m₂). Applications: the reduced-mass correction to hydrogen, the H/D isotope shift, positronium, muonic hydrogen, and the isotope splitting of HCl vibrational lines.
status: in-progress
kind: derivation
level: introductory
tags: [two-body-problem, reduced-mass, center-of-mass, entanglement, isotope-shift, positronium, muonic-hydrogen, griffiths]
prerequisites: [schrodinger-equation-in-three-dimensions, hydrogen-atom]
related: [bosons-fermions-and-exchange-forces, born-oppenheimer-approximation, molecular-hamiltonian, harmonic-oscillator-ladder-operators]
order: 10
date: 2026-11-05
---

## The two-particle wave function

The state of two particles is one function of both sets of coordinates, $\Psi(\mathbf r_1,\mathbf r_2,t)$. It obeys

$$
i\hbar\frac{\partial\Psi}{\partial t} = \left[-\frac{\hbar^2}{2m_1}\nabla_1^2 - \frac{\hbar^2}{2m_2}\nabla_2^2 + V(\mathbf r_1,\mathbf r_2,t)\right]\Psi .
$$

$|\Psi|^2d^3\mathbf r_1\,d^3\mathbf r_2$ is the probability of finding particle 1 in $d^3\mathbf r_1$ *and* particle 2 in $d^3\mathbf r_2$, and $\int|\Psi|^2d^3\mathbf r_1d^3\mathbf r_2 = 1$. For a time-independent $V$, stationary states $\psi(\mathbf r_1,\mathbf r_2)e^{-iEt/\hbar}$ form a complete set. In general the two-particle TISE is hard, but two cases reduce to one-particle problems.

## Case 1: non-interacting particles

**Separation.** If $V = V_1(\mathbf r_1)+V_2(\mathbf r_2)$, the TISE separates with $\psi = \psi_a(\mathbf r_1)\psi_b(\mathbf r_2)$ and $E = E_a+E_b$, giving

$$
\Psi(\mathbf r_1,\mathbf r_2,t) = \Psi_a(\mathbf r_1,t)\,\Psi_b(\mathbf r_2,t).
$$

In this product state, particle 1 is in state $a$ and particle 2 in state $b$.

**Entanglement.** Superpositions of products also solve the equation, for example

$$
\Psi = \tfrac35\Psi_a(\mathbf r_1,t)\Psi_b(\mathbf r_2,t)+\tfrac45\Psi_c(\mathbf r_1,t)\Psi_d(\mathbf r_2,t).
$$

Measuring particle 1's energy gives $E_a$ with probability 9/25, after which particle 2 is certainly in $b$, or $E_c$ with probability 16/25, after which it is in $d$. The state of each particle depends on the other. A state that cannot be written as a single product is **entangled**. For identical particles the symmetrization requirement forces a further kind of correlation ([[bosons-fermions-and-exchange-forces]]).

## Case 2: interaction through the separation only (Griffiths Problem 5.1)

**Coordinates.** Let $V = V(|\mathbf r_1-\mathbf r_2|)$. Change to relative and centre-of-mass coordinates:

$$
\mathbf r = \mathbf r_1-\mathbf r_2,\qquad \mathbf R = \frac{m_1\mathbf r_1+m_2\mathbf r_2}{m_1+m_2},\qquad
\mu = \frac{m_1m_2}{m_1+m_2}.
$$

The chain rule gives $\nabla_1 = (\mu/m_2)\nabla_R+\nabla_r$ and $\nabla_2 = (\mu/m_1)\nabla_R-\nabla_r$.

**Separated equation.** The cross terms cancel, leaving

$$
-\frac{\hbar^2}{2(m_1+m_2)}\nabla_R^2\psi - \frac{\hbar^2}{2\mu}\nabla_r^2\psi + V(r)\psi = E\psi .
$$

With $\psi = \psi_R(\mathbf R)\psi_r(\mathbf r)$:

- the **centre of mass** moves as a free particle of mass $m_1+m_2$;
- the **relative coordinate** obeys a one-body equation with the reduced mass $\mu$ in the potential $V(r)$;
- the energies add: $E = E_R+E_r$.

This is the same reduction as in classical mechanics. For hydrogen, every result of [[hydrogen-atom]] holds with $m_e\to\mu$.

## Worked examples

!!! example "Reduced-mass corrections (Griffiths Problem 5.2)"
    CODATA constants via SciPy.

    **(a) Size of the correction.** Using $m_e$ instead of $\mu$ overestimates the hydrogen binding energy by $(m_e-\mu)/\mu = m_e/m_p = 0.0545\%$.

    **(b) Isotope shift.** Balmer $\alpha$ (vacuum wavelengths) is 656.4696 nm for H and 656.2910 nm for D (deuteron mass), a separation of **0.1786 nm**. Deuterium was discovered from exactly this shift.

    **(c) Positronium** ($e^+e^-$, $\mu = m_e/2$). $E_1 = -6.803$ eV: half the hydrogen binding energy, and twice the Bohr radius.

    **(d) Muonic hydrogen** ($m_\mu = 206.77\,m_e$). $\mu = 185.84\,m_e$, so all energies scale by 185.84. Lyman $\alpha$ moves from 121.6 nm to **0.6538 nm**, in the X-ray range, and the orbit is 186 times smaller. This makes muonic atoms sensitive probes of nuclear size.

!!! example "HCl vibrational isotope splitting (Griffiths Problem 5.3)"
    **Model.** Treat the bond as an oscillator with the same force constant $k$ for both chlorine isotopes, so $\nu\propto\sqrt{k/\mu}$ and

    $$
    \frac{\Delta\nu}{\nu} = 1-\sqrt{\frac{\mu(^1\mathrm H^{35}\mathrm{Cl})}{\mu(^1\mathrm H^{37}\mathrm{Cl})}} .
    $$

    **Result.** With integer masses 1, 35, 37 this gives $7.51\times10^{-4}$, Griffiths's stated answer. With the actual atomic masses (1.007825, 34.968853, 36.965903 u) it gives $7.57\times10^{-4}$. The difference comes from the mass of H relative to 1 u.

    **Why $k$ is the same.** The force constant is a property of the Born–Oppenheimer potential surface, which does not depend on nuclear mass ([[born-oppenheimer-approximation]]).

## Source

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Sec. 5.1 (opening), Eqs. (5.1)-(5.15); Problems 5.1-5.3. Page numbers are not given because the PDF used is an e-book rendering without print pagination. Numbers recomputed with `griffiths/ch05_identical.py` (section A); the exact-mass HCl value and the deuterium/muonic remarks are additions.
