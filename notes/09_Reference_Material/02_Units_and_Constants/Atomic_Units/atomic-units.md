---
id: atomic-units
title: Atomic units
summary: How the Bohr radius and the hartree arise from making the hydrogen Schrödinger equation dimensionless, and a table of atomic-unit conversion factors (CODATA 2022) plus common non-SI conversions.
status: in-progress
kind: reference
level: introductory
tags: [units, atomic-units, hartree, bohr, constants]
prerequisites: []
related: [molecular-hamiltonian]
also: []
date: 2026-11-03
---

## Origin

In SI units the hydrogen-atom Schrödinger equation is

$$
\left[-\frac{\hbar^2}{2m_e}\nabla^2 - \frac{e^2}{4\pi\varepsilon_0 r}\right]\phi = \mathcal E\phi .
$$

Scale lengths, $x = \lambda x'$ (and likewise $y$, $z$, $r$), so that $\nabla^2 = \lambda^{-2}\nabla'^2$:

$$
\left[-\frac{\hbar^2}{2m_e\lambda^2}\nabla'^2 - \frac{e^2}{4\pi\varepsilon_0\lambda r'}\right]\phi = \mathcal E\phi .
$$

Choose $\lambda$ so that the two prefactors are equal, and call their common value $E_h$:

$$
\frac{\hbar^2}{m_e\lambda^2} = \frac{e^2}{4\pi\varepsilon_0\lambda} = E_h
\quad\Longrightarrow\quad
\lambda = \frac{4\pi\varepsilon_0\hbar^2}{m_e e^2} = a_0 .
$$

So $\lambda$ is the Bohr radius $a_0$ (unit of length, the **bohr**), and $E_h$ is the **hartree** (unit of energy). Dividing by $E_h$ and writing $\mathcal E' = \mathcal E/E_h$ gives the dimensionless equation

$$
\left[-\tfrac12\nabla'^2 - \frac{1}{r'}\right]\phi = \mathcal E'\phi ,
$$

whose ground state is $\mathcal E' = -\tfrac12$, i.e. $-0.5\,E_h$.

Equivalently, atomic units set $\hbar = m_e = e = 4\pi\varepsilon_0 = 1$. A quantity $Q'$ in atomic units has SI value $Q = XQ'$, with $X$ from the table. From here on primes are dropped.

## Conversion table

Values are CODATA 2022 as provided by `scipy.constants` (SciPy 1.18), rounded. Szabo's Table 2.1 lists older values that agree to the digits shown there.

| Quantity | Atomic unit $X$ | SI value |
|---|---|---|
| length | $a_0$ | $5.29177211\times10^{-11}$ m |
| mass | $m_e$ | $9.10938371\times10^{-31}$ kg |
| charge | $e$ | $1.602176634\times10^{-19}$ C (exact) |
| energy | $E_h$ | $4.35974472\times10^{-18}$ J |
| angular momentum | $\hbar$ | $1.05457182\times10^{-34}$ J s |
| electric dipole moment | $ea_0$ | $8.47835362\times10^{-30}$ C m |
| electric polarizability | $e^2a_0^2/E_h$ | $1.64877727\times10^{-41}$ C$^2$ m$^2$ J$^{-1}$ |
| electric field | $E_h/(ea_0)$ | $5.14220675\times10^{11}$ V m$^{-1}$ |
| wave function (3D) | $a_0^{-3/2}$ | $2.59775567\times10^{15}$ m$^{-3/2}$ |

## Non-SI conversions used in the literature

| From | To |
|---|---|
| 1 bohr | 0.529177211 Å |
| 1 hartree | 27.2113862 eV |
| 1 hartree | 627.509474 kcal/mol |
| 1 hartree | 2625.49964 kJ/mol |
| 1 hartree | 219474.631 cm$^{-1}$ |
| 1 $ea_0$ | 2.54174647 D |
| proton mass | 1836.15267 $m_e$ |

The molar values use the Avogadro constant and 1 kcal = 4.184 kJ (thermochemical calorie). The debye is $10^{-21}/c$ C m.

## Source

Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996; reprint of the revised first edition, McGraw-Hill, 1989), Sec. 2.1.1, pp. 41-43, Eqs. (2.3)-(2.9), Table 2.1. Numerical values: CODATA 2022 via `scipy.constants`.
