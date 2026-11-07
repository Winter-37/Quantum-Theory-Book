---
id: pople-basis-sets
title: Pople basis sets - STO-3G, 4-31G, 6-31G*, 6-31G**
summary: Construction and notation of the standard Pople basis sets used in Szabo. A minimal STO-3G basis with shared sp exponents and standard Slater exponents, the split-valence 4-31G and 6-31G, and polarization functions (*, **). Function counts, contraction notation, and the reasons for each step.
status: in-progress
kind: reference
level: introductory
tags: [basis-sets, pople, sto-3g, 4-31g, 6-31g, polarization, split-valence]
prerequisites: [gaussian-basis-functions]
related: [hf-closed-shell-basis-set-trends, rhf, gaussian-basis-sets-and-convergence]
order: 20
date: 2026-11-03
---

## Notation

$(n_s s\,n_p p\,n_d d/\dots)$ counts **primitive** Gaussians and $[\dots]$ counts **contracted** functions. For example, 4-31G for first-row atom/hydrogen is $(8s4p/4s)/[3s2p/2s]$.

## Minimal basis: STO-3G

One contracted function per occupied atomic orbital (H: 1s; Li-Ne: 1s, 2s, 2p$_{x,y,z}$). Each is a 3-primitive least-squares fit to a Slater function ([[gaussian-basis-functions]]). In the 2s and 2p functions:

- They **share exponents** (an "sp shell"), which halves the integral work.
- The fit is to $\zeta = 1$ Slater functions. The exponents are then scaled by $\zeta^2$ with **standard molecular Slater exponents** (Szabo Table 3.8), chosen as averages of exponents optimized in small molecules.

| Atom | H | Li | Be | B | C | N | O | F |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| $\zeta_{1s}$ | 1.24 | 2.69 | 3.68 | 4.68 | 5.67 | 6.67 | 7.66 | 8.65 |
| $\zeta_{2sp}$ | | 0.75 | 1.10 | 1.45 | 1.72 | 1.95 | 2.25 | 2.55 |
The H value 1.24 is larger than the free-atom 1.0: bonded hydrogens are contracted. For H$_2$ the optimum at 1.4 bohr is 1.19 ([[rhf]]).

**Limitations.**

- **Rigid shape.** Each atomic orbital has a fixed size, so it cannot expand or contract with the molecular environment.
- **Isotropic p shell.** All three p functions have the same radial extent, so the basis cannot describe anisotropic environments.

## Split valence: 4-31G and 6-31G

**Double zeta.** A true double-zeta basis uses two functions per minimal-basis function, one tighter and one more diffuse. The SCF can then change the effective orbital size by mixing them **linearly**, instead of re-optimizing nonlinear exponents. Differently oriented p orbitals can also have different effective sizes.

**4-31G** splits only the valence shell (a split-valence basis):

| Part | Contraction |
|---|---|
| inner shell (1s of Li-F) | one function, 4 primitives |
| inner valence (2s, 2p) | 3 primitives |
| outer valence (2s, 2p) | 1 primitive, uncontracted |
| hydrogen | 1s inner (3 primitives) + 1s outer (1 primitive) |

**Counts.** 2 functions for H and He, 9 for Li-Ne, 13 for Na-Ar. Notation: $(8s4p/4s)/[3s2p/2s]$.

**Fitting.** Unlike STO-3G, the parameters were not fitted to Slater functions but **optimized in atomic SCF calculations** with the contraction pattern fixed in advance. The valence exponents are then scaled by standard factors for molecules (Szabo Table 3.9; only H differs much from 1: inner 1.20, outer 1.15).

**6-31G** is the same scheme with a 6-primitive core function. It is reoptimized from scratch: lower total energies, nearly the same valence properties.

!!! example "A 4-31G-type He basis (Szabo Ex. 3.30)"
    Huzinaga's 4-primitive He 1s orbital has exponents (coefficients) 0.298073 (0.51380), 1.242567 (0.46954), 5.782948 (0.15457), 38.47497 (0.02373).

    - **Outer function.** Keep the most diffuse primitive, $\alpha = 0.298073$, uncontracted.
    - **Inner function.** Contract the three tight primitives with their coefficients, renormalized with the Gaussian overlap $S_{pq} = [2\sqrt{\alpha_p\alpha_q}/(\alpha_p+\alpha_q)]^{3/2}$. The renormalized coefficients are
    $$
    d = 0.79330\ (1.242567),\quad 0.26115\ (5.782948),\quad 0.04009\ (38.47497).
    $$

    Computed for this note.

## Polarization functions: 6-31G* and 6-31G**

**Why angular momentum must be raised.** Adding more s and p functions alone does not give a balanced basis. In the s,p limit NH$_3$ is predicted planar (Szabo).

**Polarization.** The next step adds functions of **higher angular momentum** than any occupied atomic orbital. A hydrogen atom in a field polarizes by mixing 1s with p. A bonded atom feels a similar nonuniform field, so p on H and d on Li-F let the charge distribution distort.

| Basis | Added functions | Standard exponent | Contraction (first row / H) | Functions (first row / H) |
|---|---|---|---|---|
| 6-31G* | one uncontracted set of six Cartesian $d$ on Li-F | 0.8 (C, N, O, F) | $(11s4p1d/4s)/[4s2p1d/2s]$ | 15 / 2 |
| 6-31G** | also one uncontracted $p$ set on each H | 1.1 | | 15 / 5 |

The six Cartesian $d$ functions ($x^2, y^2, z^2, xy, xz, yz$) equal the five spherical $d$ plus one extra s-type function $x^2+y^2+z^2$. Polarization on heavy atoms matters more than on hydrogen.

**Basis sizes for benzene (Szabo Ex. 3.31).** C$_6$H$_6$, Cartesian $d$, checked with PySCF:

| Basis | Count | Functions |
|---|---|---:|
| STO-3G | $6\times5 + 6\times1$ | 36 |
| 4-31G | $6\times9 + 6\times2$ | 66 |
| 6-31G* | $6\times15 + 6\times2$ | 102 |
| 6-31G** | $6\times15 + 6\times5$ | 120 |

## Beyond Szabo

Szabo stops at 6-31G**. The same logic leads to:

- triple-zeta valence (6-311G),
- multiple and higher polarization (2df),
- diffuse functions for anions and weak interactions (6-31+G*),
- correlation-consistent families (cc-pVXZ), designed for systematic convergence of correlated energies.

PySCF uses spherical $d$ by default. Set `cart=True` to reproduce the original Cartesian 6-31G* numbers.

## Source

Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996; reprint of the revised first edition, McGraw-Hill, 1989), Sec. 3.6.2-3.6.4, pp. 184-190, Tables 3.7-3.9, Ex. 3.30-3.31.
