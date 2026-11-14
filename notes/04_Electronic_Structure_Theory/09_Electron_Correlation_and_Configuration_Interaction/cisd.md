---
id: cisd
title: Truncated CI - doubly excited CI and CISD
summary: Truncating the CI expansion at double excitations (DCI) or singles and doubles (SDCI/CISD). The matrix form of the DCI equations, the iterative and perturbative estimates of the correlation energy and pair contributions, the Davidson correction, and what illustrative calculations show about singles, geometries, ionization potentials and dipole moments. Computed H2O example against full CI.
status: in-progress
kind: derivation
level: intermediate
tags: [ci, cisd, dci, truncated-ci, davidson-correction, pair-energies]
prerequisites: [full-ci]
related: [standard-models-h2-and-water, size-consistency, natural-orbitals, electron-correlation, coupled-pair-approximations, ci-in-practice]
order: 50
date: 2026-11-03
---

## Truncating the expansion

Full CI is out of reach except for tiny systems ([[full-ci]]). The systematic truncation keeps configurations that differ from $|\Psi_0\rangle$ by at most $m$ spin orbitals:

- **DCI** (CID): doubles only.
- **SDCI** (CISD): singles and doubles.
- **SDTQCI**, and so on, up to full CI at $m = N$.

The truncated energy is still variational. For small molecules SDCI recovers most of the correlation energy, but it deteriorates as the system grows ([[size-consistency]]).

**Singles.** They have little effect on the energy, but there are few of them, so they are usually included. They matter for one-electron properties.

## Matrix form of DCI

In intermediate normalization,

$$
|\Phi_{\text{DCI}}\rangle = |\Psi_0\rangle + \sum_{\substack{c<d\\ t<u}}c_{cd}^{tu}|\Psi_{cd}^{tu}\rangle .
$$

Project $(\hat H - E_0)|\Phi_{\text{DCI}}\rangle = E_{\text{corr}}|\Phi_{\text{DCI}}\rangle$ onto $\langle\Psi_0|$ and onto each $\langle\Psi_{ab}^{rs}|$. Define

$$
(\mathbf B)_{rasb} = \langle\Psi_{ab}^{rs}|\hat H|\Psi_0\rangle,
\qquad
(\mathbf D)_{rasb,tcud} = \langle\Psi_{ab}^{rs}|\hat H - E_0|\Psi_{cd}^{tu}\rangle,
\qquad
(\mathbf c)_{rasb} = c_{ab}^{rs}.
$$

The two projections become

$$
\mathbf B^\dagger\mathbf c = E_{\text{corr}},
\qquad
\mathbf B + \mathbf D\mathbf c = \mathbf c\,E_{\text{corr}},
\qquad\text{i.e.}\qquad
\begin{pmatrix}0 & \mathbf B^\dagger\\ \mathbf B & \mathbf D\end{pmatrix}\begin{pmatrix}1\\ \mathbf c\end{pmatrix} = E_{\text{corr}}\begin{pmatrix}1\\ \mathbf c\end{pmatrix}.
$$

This is the Hamiltonian in the basis $\{|\Psi_0\rangle, |\Psi_{ab}^{rs}\rangle\}$ with $E_0$ subtracted from the diagonal. $E_{\text{corr}}$ is its lowest eigenvalue. Minimal-basis H$_2$ is the $1\times1$ case of $\mathbf D$.

## Perturbative estimates and pair contributions

Eliminate $\mathbf c = -(\mathbf D - \mathbf 1E_{\text{corr}})^{-1}\mathbf B$:

$$
E_{\text{corr}} = -\mathbf B^\dagger\big(\mathbf D - \mathbf 1E_{\text{corr}}\big)^{-1}\mathbf B .
$$

**Iteration.** $E_{\text{corr}}$ appears on both sides, so this is solved iteratively. Starting from $E_{\text{corr}} = 0$ on the right gives the first estimate

$$
E_{\text{corr}}^{(1)} = -\mathbf B^\dagger\mathbf D^{-1}\mathbf B .
$$

This is no longer an upper bound, but unlike DCI it does not deteriorate with system size.

**Diagonal approximation.** If $\mathbf D$ is approximated by its diagonal,

$$
E_{\text{corr}} \approx \sum_{\substack{a<b\\ r<s}}\frac{|\langle\Psi_0|\hat H|\Psi_{ab}^{rs}\rangle|^2}{\langle\Psi_0|\hat H|\Psi_0\rangle - \langle\Psi_{ab}^{rs}|\hat H|\Psi_{ab}^{rs}\rangle} = \sum_{\substack{a<b\\ r<s}}e_{ab}^{rs}.
$$

Each term $e_{ab}^{rs}$ estimates one double's contribution. These estimates are cheap and are used to **select** the important configurations before a large CI. Replacing the diagonal elements of $\mathbf D$ by orbital-energy differences gives second-order perturbation theory (Szabo Ch. 6).

## The Davidson correction

A simple a-posteriori fix for the missing quadruples:

$$
E_{\text{corr}}(\text{SDCI}+Q) = E_{\text{corr}}(\text{SDCI}) + \Delta E_{\text{Davidson}},
\qquad
\Delta E_{\text{Davidson}} = (1 - c_0^2)\,E_{\text{corr}}(\text{SDCI}),
$$

where $c_0$ is the Hartree-Fock coefficient of the **normalized** SDCI wave function. It costs nothing extra.

**Why it works (Szabo Ex. 4.14).** For $N$ independent H$_2$ molecules ([[size-consistency]]):

- Expanding the DCI energy gives the exact $N$-linear term plus a spurious term $+N^2K_{12}^4/(8\Delta^3)$.
- $\Delta E_{\text{Davidson}}$ to leading order is $-N^2K_{12}^4/(8\Delta^3)$, which cancels it.
- Higher spurious powers remain. Also, for $N = 1$ DCI is already exact but the correction is not zero.

!!! example "H₂O, 6-31G, all electrons correlated (geometry of Szabo Table 3.10)"
    PySCF 2.14: `ci.CISD` and `fci.FCI`; 13 basis functions, 10 electrons. Correlation energies in hartree:

    | Method | $E_{\text{corr}}$ | % of full CI |
    |---|---:|---:|
    | CISD | −0.130068 | 95.0 |
    | CISD + Davidson ($c_0 = 0.98013$) | −0.135185 | 98.8 |
    | Full CI | −0.136848 | 100 |

    $E_{\text{HF}} = -75.983996$ hartree. With all electrons correlated, singles and doubles miss 5% of the basis-set correlation energy, and the Davidson estimate of the quadruples recovers most of it. This is a small-basis analogue of the Saxe-Schaefer-Handy double-zeta water benchmark that Szabo discusses; it is not the same calculation.

## What the illustrative calculations show (Szabo Sec. 4.3)

Szabo's Tables 4.2-4.11 collect CI results from the literature. The points they make:

- **H₂ (Tables 4.2-4.3).** SDCI is full CI for two electrons, and singles change the correlation energy by at most 0.15 mHa. The full CI bond lengths are longer than the SCF ones and closer to the exact 1.401 bohr. The 6-31G** SDCI value, −0.03387 hartree, agrees with the −0.033869 hartree computed in [[electron-correlation]].
- **BeH₂ (Tables 4.4-4.5).** Singles and doubles give about 98% of the full CI correlation energy for this six-electron molecule. In the double-zeta basis quadruples contribute more than triples.
- **H₂O, 39-STO basis (Tables 4.6-4.8, 4.11).**
  - **Energy.** SDCI recovers about 93% of the estimated basis-set correlation energy. Singles add only 0.6%.
  - **Geometry and force constants.** These move substantially from SCF towards experiment.
  - **Ionization potential.** The lowest IP from separate SDCI calculations on H₂O and H₂O⁺ is 0.452 hartree, against 0.507 (Koopmans) and 0.463 (experiment).
  - **Dipole moment.** SDCI halves the SCF error.
- **N₂ (Table 4.9).** SDCI on N₂ and N₂⁺ gives the correct ordering of the two lowest ionized states, which Koopmans' theorem gets wrong ([[koopmans-theorem]]).
- **CO dipole (Table 4.10).** Adding the 200 most important doubles to SCF lowers the energy more than 138 doubles plus 62 singles. However, only the calculation with singles gives the correct sign of the dipole moment. A better energy does not guarantee better one-electron properties, and singles are essential for the charge density ([[population-analysis]]).

## Source

Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996; reprint of the revised first edition, McGraw-Hill, 1989), Sec. 4.2-4.3, pp. 242-252, Eqs. (4.25)-(4.32), Tables 4.2-4.11; Ex. 4.14. Water numbers computed for this note.
