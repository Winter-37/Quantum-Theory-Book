---
id: spin-orbitals-and-antisymmetry
title: Spin orbitals and the antisymmetry principle
summary: Electron spin enters a nonrelativistic theory through two orthonormal spin functions α and β. Spatial orbitals times spin functions give spin orbitals, and many-electron wave functions must change sign when the space-spin coordinates of any two electrons are exchanged.
status: in-progress
kind: theory
level: introductory
tags: [basics, spin, pauli, antisymmetry, spin-orbitals]
prerequisites: [molecular-hamiltonian]
related: [slater-determinants, spin-operators, spin-adapted-configurations]
also: []
date: 2026-11-03
---

## Spin functions

The electronic Hamiltonian contains no spin. Spin is added by giving each electron a spin coordinate $\omega$ and two spin functions, $\alpha(\omega)$ (up) and $\beta(\omega)$ (down). Operationally all we need is that they are orthonormal and complete for one electron's spin:

$$
\int\mathrm d\omega\ \alpha^*(\omega)\alpha(\omega) = \int\mathrm d\omega\ \beta^*(\omega)\beta(\omega) = 1,
\qquad
\int\mathrm d\omega\ \alpha^*(\omega)\beta(\omega) = 0,
$$

or $\langle\alpha|\alpha\rangle = \langle\beta|\beta\rangle = 1$ and $\langle\alpha|\beta\rangle = 0$. The "integral" over $\omega$ is formal: it is a sum over the two spin states. One electron is then described by four coordinates,

$$
\mathbf x = \{\mathbf r,\omega\},
\qquad
\int\mathrm d\mathbf x \equiv \int\mathrm d\mathbf r\int\mathrm d\omega .
$$

## Spatial and spin orbitals

A **spatial orbital** $\psi_i(\mathbf r)$ is a one-electron wave function: $|\psi_i(\mathbf r)|^2\mathrm d\mathbf r$ is the probability of finding the electron in $\mathrm d\mathbf r$. The orbitals are taken orthonormal,

$$
\int\mathrm d\mathbf r\ \psi_i^*(\mathbf r)\psi_j(\mathbf r) = \delta_{ij}.
$$

In practice only a finite set $\{\psi_i\}_{i=1}^K$ is available, so results are "exact" only within the space it spans.

A **spin orbital** $\chi(\mathbf x)$ describes both the spatial distribution and the spin. From each spatial orbital one can form two,

$$
\chi(\mathbf x) = \psi(\mathbf r)\alpha(\omega)\quad\text{or}\quad\psi(\mathbf r)\beta(\omega).
$$

From $K$ spatial orbitals we get $2K$ spin orbitals:

$$
\chi_{2i-1}(\mathbf x) = \psi_i(\mathbf r)\alpha(\omega),
\qquad
\chi_{2i}(\mathbf x) = \psi_i(\mathbf r)\beta(\omega),
\qquad i = 1,\dots,K .
$$

These are orthonormal if the spatial orbitals are: the spin integral gives $\delta$ between spins, the spatial integral gives $\delta$ between orbitals,

$$
\langle\chi_i|\chi_j\rangle = \int\mathrm d\mathbf x\ \chi_i^*(\mathbf x)\chi_j(\mathbf x) = \delta_{ij}.
$$

!!! example "Different spatial orbitals for different spins (Szabo Ex. 2.1)"
    Take two orthonormal spatial sets $\{\psi_i^\alpha\}$ and $\{\psi_i^\beta\}$ that overlap each other, $\int\psi_i^{\alpha*}\psi_j^\beta\,\mathrm d\mathbf r = S_{ij}\ne0$. Form $\chi_{2i-1} = \psi_i^\alpha\alpha$ and $\chi_{2i} = \psi_i^\beta\beta$.

    - **Same spin.** $\langle\chi_{2i-1}|\chi_{2j-1}\rangle = \langle\psi_i^\alpha|\psi_j^\alpha\rangle\langle\alpha|\alpha\rangle = \delta_{ij}$, and likewise for $\beta$.
    - **Opposite spin.** $\langle\chi_{2i-1}|\chi_{2j}\rangle = S_{ij}\,\langle\alpha|\beta\rangle = 0$.

    So the $2K$ spin orbitals are orthonormal even though the spatial sets are not mutually orthogonal: the spin integral does the work. These are the **unrestricted** spin orbitals used in UHF (see [[spin-adapted-configurations]]).

## The antisymmetry principle

Because the Hamiltonian ignores spin, merely letting the wave function depend on $\omega$ changes nothing. The physics of spin enters through an extra postulate. **A many-electron wave function must be antisymmetric under exchange of the full coordinates (space and spin) of any two electrons:**

$$
\Phi(\mathbf x_1,\dots,\mathbf x_i,\dots,\mathbf x_j,\dots,\mathbf x_N) = -\,\Phi(\mathbf x_1,\dots,\mathbf x_j,\dots,\mathbf x_i,\dots,\mathbf x_N).
$$

This is the general form of the Pauli exclusion principle. It is an independent postulate: the exact wave function must both solve the Schrödinger equation and obey it.

Two consequences:

- **Probability density.** $|\Phi|^2$ is unchanged by exchanging two electrons, so electrons are indistinguishable.
- **Exclusion.** If $\Phi$ is built from orbitals, two electrons cannot occupy the same spin orbital. [[slater-determinants]] build in both properties automatically.

## Source

Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996; reprint of the revised first edition, McGraw-Hill, 1989), Sec. 2.1.3 and 2.2.1, pp. 45-47, Eqs. (2.19)-(2.27), Ex. 2.1.
