---
id: schrodinger-equation-in-three-dimensions
title: The Schrödinger equation in three dimensions; Cartesian separation
summary: The 3D Schrödinger equation with p → −iħ∇, the canonical commutators [r_i, p_j] = iħδ_ij, 3D Ehrenfest and Heisenberg relations, and separation in Cartesian coordinates. Worked cases are the cubical box (degeneracies, including the accidental four-fold E₁₄ = 27) and the isotropic 3D oscillator, with energies (n + 3/2)ħω and degeneracy (n+1)(n+2)/2. Also the 3D probability current and the virial theorem in 3D.
status: in-progress
kind: derivation
level: introductory
tags: [three-dimensions, laplacian, separation-of-variables, particle-in-a-box, degeneracy, 3d-harmonic-oscillator, canonical-commutation, griffiths]
prerequisites: [stationary-states, infinite-square-well, harmonic-oscillator-ladder-operators]
related: [central-potentials-and-spherical-harmonics, hydrogen-atom, energy-time-uncertainty-principle, normalization-and-probability-current]
also: []
date: 2026-11-04
---

## Equation and postulates in 3D

The classical energy $\frac{1}{2m}(p_x^2+p_y^2+p_z^2)+V$ becomes an operator by the substitution $\mathbf p\to-i\hbar\nabla$:

$$
i\hbar\frac{\partial\Psi}{\partial t} = -\frac{\hbar^2}{2m}\nabla^2\Psi + V\Psi,
\qquad
\nabla^2 = \frac{\partial^2}{\partial x^2}+\frac{\partial^2}{\partial y^2}+\frac{\partial^2}{\partial z^2}.
$$

**Interpretation and normalization.** $|\Psi(\mathbf r,t)|^2d^3\mathbf r$ is the probability of finding the particle in $d^3\mathbf r$, and $\int|\Psi|^2d^3\mathbf r = 1$.

**Stationary states.** For time-independent $V$, the states $\psi_n(\mathbf r)e^{-iE_nt/\hbar}$ satisfy $-\frac{\hbar^2}{2m}\nabla^2\psi+V\psi = E\psi$, and the general solution is $\sum c_n\psi_ne^{-iE_nt/\hbar}$. An integral replaces the sum for continuum states.

**Canonical commutators** (Problem 4.1):

$$
[r_i,p_j] = -[p_i,r_j] = i\hbar\,\delta_{ij},\qquad [r_i,r_j] = [p_i,p_j] = 0 .
$$

**Consequences.**

- Ehrenfest: $\frac{d}{dt}\langle\mathbf r\rangle = \langle\mathbf p\rangle/m$ and $\frac{d}{dt}\langle\mathbf p\rangle = \langle-\nabla V\rangle$.
- Heisenberg holds componentwise: $\sigma_x\sigma_{p_x}\ge\hbar/2$ and likewise for $y$ and $z$.
- There is no restriction on $\sigma_x\sigma_{p_y}$, since $x$ and $p_y$ commute.

**Probability current** (Problem 4.49):

$$
\mathbf J = \frac{i\hbar}{2m}\left(\Psi\nabla\Psi^*-\Psi^*\nabla\Psi\right),
\qquad
\frac{\partial|\Psi|^2}{\partial t} + \nabla\cdot\mathbf J = 0 .
$$

By the divergence theorem, probability leaves a volume only through its surface, generalizing [[normalization-and-probability-current]].

**Virial theorem** (Problem 4.48). For a stationary state, $2\langle T\rangle = \langle\mathbf r\cdot\nabla V\rangle$.

- Hydrogen: $\langle T\rangle = -E_n$.
- 3D oscillator: $\langle T\rangle = \langle V\rangle = E_n/2$.

The 1D derivation is in [[energy-time-uncertainty-principle]].

## Cartesian separation

**Ansatz.** If $V = V_x(x)+V_y(y)+V_z(z)$, write $\psi = X(x)Y(y)Z(z)$. Then each factor obeys a 1D Schrödinger equation, and

$$
E = E_x+E_y+E_z .
$$

**Degeneracy.** Distinct $(E_x,E_y,E_z)$ triples with the same sum give **degenerate** levels. In one dimension, bound states are never degenerate (Griffiths Problem 2.44). In three dimensions degeneracy is the rule.

## Worked examples

!!! example "Cubical box of side $a$ (Griffiths Problem 4.2)"
    **Solution.**

    $$
    \psi = \left(\frac2a\right)^{3/2}\sin\frac{n_x\pi x}{a}\sin\frac{n_y\pi y}{a}\sin\frac{n_z\pi z}{a},
    \qquad
    E = \frac{\pi^2\hbar^2}{2ma^2}\left(n_x^2+n_y^2+n_z^2\right).
    $$

    **Lowest levels**, enumerated, in units of $\pi^2\hbar^2/2ma^2$:

    | Level | 1 | 2 | 3 | 4 | 5 | 6 | ... | 14 |
    |---|---|---|---|---|---|---|---|---|
    | $n_x^2+n_y^2+n_z^2$ | 3 | 6 | 9 | 11 | 12 | 14 | ... | 27 |
    | Degeneracy | 1 | 3 | 3 | 3 | 1 | 6 | ... | 4 |

    **Pattern.**

    - Permutations of three distinct integers give 6.
    - Two equal integers give 3.
    - Three equal integers give 1.

    **The accidental case $E_{14}$.** It is four-fold because $27 = 1^2+1^2+5^2 = 3^2+3^2+3^2$. Three states come from permutations of $(1,1,5)$ and one is $(3,3,3)$. The symmetry of the cube explains the 3. The extra state is a number-theoretic coincidence.

!!! example "Isotropic 3D oscillator (Griffiths Problems 4.46-4.47)"
    **Separation.** $V = \tfrac12m\omega^2r^2 = \tfrac12m\omega^2(x^2+y^2+z^2)$ separates into three 1D oscillators:

    $$
    E_n = \left(n+\tfrac32\right)\hbar\omega,\qquad n = n_x+n_y+n_z,\qquad d(n) = \frac{(n+1)(n+2)}{2}.
    $$

    **Degeneracy.** Counting the triples gives $1, 3, 6, 10, 15, 21$ for $n = 0,\ldots,5$, in agreement with the formula.

    **Spherical coordinates.** Solving the radial equation by power series (Problem 4.47) shows that level $n$ contains $\ell = n, n-2, \ldots$ down to 0 or 1. For example, $n=2$ contains $\ell=2$ (5 states) and $\ell=0$ (1 state), totalling 6. Like hydrogen, the oscillator has more degeneracy than rotational symmetry alone requires: a hidden SU(3) symmetry, mentioned here, not proved.

    **Link to quantum chemistry.** The Cartesian functions $x^iy^jz^ke^{-\alpha r^2}$ with $i+j+k = n$ number $(n+1)(n+2)/2$, the same count. This is why Cartesian Gaussian shells have 6 $d$ and 10 $f$ components, against 5 and 7 spherical ones ([[solid-harmonics-angular-basis]]).

## Source

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Sec. 4.1 (opening), Eqs. (4.1)-(4.12); Problems 4.1, 4.2, 4.46-4.49 (Eqs. 4.215-4.222). Page numbers are not given because the PDF used is an e-book rendering without print pagination. The degeneracy tables are enumerated in `griffiths/ch04_3d.py` (section A). The SU(3) remark and the basis-function link are additions.
