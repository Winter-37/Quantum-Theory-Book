---
id: free-electron-gas
title: The free electron gas; Fermi energy and degeneracy pressure
summary: Sommerfeld model of a metal. Free electrons in a box fill an octant of k-space up to k_F = (3π²ρ)^{1/3}. Derives the Fermi energy, total energy (mean 3/5 E_F per electron), the degeneracy pressure P = (2/3)E/V, and the bulk modulus B = (5/3)P. Numbers for copper (E_F = 7.05 eV, T_F ≈ 8×10⁴ K, B ≈ 6.4×10¹⁰ N/m² against 13.4×10¹⁰ measured), ³He, the 2D gas, and a brute-force state count that converges to the continuum formulas.
status: in-progress
kind: derivation
level: intermediate
tags: [free-electron-gas, fermi-energy, fermi-surface, degeneracy-pressure, bulk-modulus, density-of-states, metals, sommerfeld, griffiths]
prerequisites: [schrodinger-equation-in-three-dimensions, bosons-fermions-and-exchange-forces]
related: [band-structure-and-the-dirac-comb, exchange-symmetry-spin-and-symmetrization-principle]
also: []
date: 2026-11-05
---

## Model

**Assumptions.** Valence electrons move freely in a rectangular box $l_x\times l_y\times l_z$ with impenetrable walls. All forces are ignored except the walls: no ions and no electron–electron repulsion. Only the Pauli principle is kept.

**One-electron states.** Separating in Cartesian coordinates ([[schrodinger-equation-in-three-dimensions]]):

$$
\psi = \sqrt{\frac{8}{l_xl_yl_z}}\sin\frac{n_x\pi x}{l_x}\sin\frac{n_y\pi y}{l_y}\sin\frac{n_z\pi z}{l_z},\qquad
E = \frac{\hbar^2k^2}{2m},\qquad k_i = \frac{n_i\pi}{l_i},\ n_i = 1,2,\ldots
$$

**k-space volume.** Each state occupies a block of volume $\pi^3/V$ in $k$-space, where $V = l_xl_yl_z$.

## Fermi sphere

**Filling.** Bosons would all sit in $\psi_{111}$. Fermions fill states two at a time (spin), so $Nd$ electrons ($N$ atoms with $d$ free electrons each) fill one octant of a sphere of radius $k_F$:

$$
\frac18\cdot\frac43\pi k_F^3 = \frac{Nd}{2}\cdot\frac{\pi^3}{V}
\quad\Longrightarrow\quad
k_F = (3\pi^2\rho)^{1/3},\qquad \rho = \frac{Nd}{V}.
$$

**Fermi energy.** The boundary is the **Fermi surface**, and

$$
E_F = \frac{\hbar^2}{2m}(3\pi^2\rho)^{2/3}.
$$

**Total energy.** A shell of thickness $dk$ holds $(V/\pi^2)k^2dk$ electrons. Integrating $\hbar^2k^2/2m$ over the sphere:

$$
E_{\rm tot} = \frac{\hbar^2V}{2\pi^2m}\int_0^{k_F}k^4dk = \frac{\hbar^2(3\pi^2Nd)^{5/3}}{10\pi^2m}V^{-2/3},
\qquad
\frac{E_{\rm tot}}{Nd} = \frac35E_F \quad\text{(Problem 5.20)}.
$$

## Degeneracy pressure

**Pressure.** $E_{\rm tot}\propto V^{-2/3}$, so expanding the box lowers the energy. The gas pushes on the walls with

$$
P = -\frac{dE_{\rm tot}}{dV} = \frac23\frac{E_{\rm tot}}{V} = \frac{(3\pi^2)^{2/3}\hbar^2}{5m}\rho^{5/3}.
$$

**Origin.** This pressure exists at zero temperature and with no interactions. It comes purely from antisymmetry (Griffiths prefers "exclusion pressure"), and it is a partial answer to why cold solids do not collapse.

**Bulk modulus** (Problem 5.23). $B = -V\,dP/dV = \tfrac53P$.

## Worked examples

!!! example "Copper (Griffiths Problems 5.21, 5.23)"
    **Inputs.** Density 8.96 g/cm³, atomic weight 63.5 g/mol, $d = 1$:

    | Quantity | Value |
    |---|---|
    | $\rho$ | $8.497\times10^{28}$ m⁻³ |
    | $k_F$ | $1.360\times10^{10}$ m⁻¹ |
    | $E_F$ | **7.05 eV** |
    | $v_F$ from $E_F = \tfrac12mv^2$ | $1.57\times10^6$ m/s $= 0.0053\,c$ (non-relativistic) |
    | $T_F = E_F/k_B$ | $8.2\times10^4$ K |
    | $P$ | $3.84\times10^{10}$ N/m² |
    | $B = \tfrac53P$ | $6.40\times10^{10}$ N/m² |

    **Reading the results.**

    - $T_F$ is far above copper's melting point (1356 K), so the electron gas is always "cold": almost every electron sits in its ground-state level.
    - The observed bulk modulus (quoted by Griffiths) is $13.4\times10^{10}$ N/m². A model with no ions and no interactions is within a factor of 2, which is surprisingly close.

!!! example "Helium-3 and two dimensions (Problems 5.22, 5.30)"
    **Helium-3.** ³He is a spin-½ fermion. As a Fermi gas at 82 kg/m³, with one atom per "electron" and the ³He mass in place of $m_e$, it has $T_F = 4.96$ K.

    **Two dimensions.** Filling a quarter disc of $k$-space with $\sigma$ electrons per unit area gives

    $$
    E_F = \frac{\pi\hbar^2\sigma}{m},
    $$

    linear in the density.

!!! example "Brute-force counting in a cube"
    **Method.** Enumerate the states $n_x^2+n_y^2+n_z^2$ of a cube ($n_i\le60$), fill them with $N$ electrons, two per state, and compare with the continuum formulas. Energies are in units of $\pi^2\hbar^2/2mL^2$.

    | $N$ | $E_F$ enumerated | $E_F$ continuum, $(3N/\pi)^{2/3}$ | $\langle E\rangle/E_F$ |
    |---|---|---|---|
    | 2 000 | 173.0 | 153.9 | 0.619 |
    | 20 000 | 755.0 | 714.5 | 0.609 |
    | 200 000 | 3402.0 | 3316.4 | 0.604 |

    **Convergence.** Agreement improves slowly, as $N^{-1/3}$. Hard walls exclude the $n_i = 0$ planes, a surface correction to the continuum count. The ratio tends to 3/5. With periodic boundary conditions (Problem 5.39) the bulk results are the same.

## Limitations

The model has every solid conducting, since there are no gaps in its spectrum. The periodic ionic potential is what produces bands and gaps ([[band-structure-and-the-dirac-comb]]). Griffiths's further problems extend the model:

- unequal spin populations and Pauli paramagnetism (5.32-5.33);
- a crude exchange term giving the Stoner criterion for ferromagnetism (5.34);
- white dwarfs and the Chandrasekhar limit (5.35-5.36).

They are not worked here.

## Source

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Sec. 5.3.1, Eqs. (5.46)-(5.57), Figs. 5.2-5.3 (described); Problems 5.20-5.23, 5.30, 5.39 (mentioned). Page numbers are not given because the PDF used is an e-book rendering without print pagination. The observed bulk modulus is quoted from Griffiths. All other numbers are computed with SciPy CODATA constants in `griffiths/ch05_identical.py` (section F).
