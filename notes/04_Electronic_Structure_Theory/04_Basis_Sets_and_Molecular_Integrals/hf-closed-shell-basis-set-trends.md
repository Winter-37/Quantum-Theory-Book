---
id: hf-closed-shell-basis-set-trends
title: Hartree-Fock basis-set trends for small closed-shell molecules
summary: RHF total energies, Koopmans ionization potentials, dipole moments, and hydrogenation energies for H2, N2, CO, CH4, NH3, H2O, FH with STO-3G, 4-31G, 6-31G*, 6-31G**, recomputed with PySCF at Szabo's standard geometries and compared with his tables and Hartree-Fock limits.
status: in-progress
kind: reference
level: intermediate
tags: [benchmark, hartree-fock, basis-sets, total-energy, reaction-energy, pyscf]
prerequisites: [rhf, pople-basis-sets]
related: [koopmans-theorem, population-analysis, gaussian-basis-sets-and-convergence, basis-set-superposition-error]
order: 60
date: 2026-11-03
---

## Setup

**Calculations.** RHF in PySCF 2.14 with Cartesian $d$ functions (as in the original Pople 6-31G* definition). The geometries are Szabo Table 3.10 (bohr):

| Molecule | $R$ (bohr) | Angle |
|---|---|---|
| H$_2$ | 1.400 | |
| CO | 2.132 | |
| N$_2$ | 2.074 | |
| CH$_4$ | 2.050 | tetrahedral |
| NH$_3$ | 1.913 | HNH 106.67° |
| H$_2$O | 1.809 | HOH 104.52° |
| FH | 1.733 | |

**Purpose.** This reproduces Szabo Sec. 3.7 with a modern code, so the numbers can be regenerated and extended to other basis sets.

## Total energies (hartree)

| Molecule | STO-3G | 4-31G | 6-31G* | 6-31G** | HF limit (Szabo) |
|---|---:|---:|---:|---:|---:|
| H$_2$ | −1.117 | −1.127 | −1.127 | −1.131 | −1.134 |
| N$_2$ | −107.496 | −108.754 | −108.943 | −108.943 | −108.997 |
| CO | −111.225 | −112.552 | −112.737 | −112.737 | −112.791 |
| CH$_4$ | −39.727 | −40.140 | −40.195 | −40.202 | −40.225 |
| NH$_3$ | −55.454 | −56.102 | −56.184 | −56.195 | −56.225 |
| H$_2$O | −74.963 | −75.907 | −76.011 | −76.023 | −76.065 |
| FH | −98.571 | −99.887 | −100.003 | −100.011 | −100.071 |

**Agreement with Szabo.** Every entry agrees with Szabo Tables 3.11-3.13 to the three decimals printed. The one exception is N$_2$/6-31G*: −108.943 here vs −108.942 printed, a last-digit rounding difference.

**Duplicate columns.** Two pairs of columns are identical by construction:

- H$_2$ 6-31G* = 4-31G: no heavy atoms to polarize, and no core for the 6-primitive contraction to improve.
- N$_2$, CO 6-31G** = 6-31G*: no hydrogens.

The Hartree-Fock-limit column is quoted from Szabo's tables (Schulman-Kaufman 1970; Hariharan-Pople 1973) and was not recomputed.

## Koopmans ionization potentials and dipoles

See [[koopmans-theorem]] (first IPs) and [[population-analysis]] (dipoles) for the same calculations.

## Reaction energies

Hydrogenation energies $\Delta E$ (electronic, no zero-point or thermal corrections), kcal/mol, using 1 hartree = 627.5095 kcal/mol (Szabo Ex. 3.32):

| Reaction | STO-3G | 4-31G | 6-31G* | 6-31G** | HF limit |
|---|---:|---:|---:|---:|---:|
| CO + 3H$_2\to$ CH$_4$ + H$_2$O | −72.2 | −71.9 | −55.3 | −58.8 | −60.9 |
| N$_2$ + 3H$_2\to$ 2NH$_3$ | −39.0 | −44.5 | −28.4 | −33.8 | −32.0 |

The HF-limit column uses Szabo's tabulated limit energies.

**Comparison with experiment.** The experimental 0 K reaction enthalpies are −45.894 (CO) and −18.604 (N$_2$) kcal/mol (as quoted in Szabo). These include zero-point energy, which must be added to $\Delta E$ before comparing. Hartree-Fock predicts both reactions exothermic, with errors that change size and even ordering with the basis. Small basis sets give right-looking numbers partly through error cancellation. Converging the basis does not converge to experiment, because the correlation contribution to bond-breaking reaction energies is large.

## Code

```python
import numpy as np
from pyscf import gto, scf
geom = {"H2O": [("O", [0, 0, 0]),
                ("H", [ 1.809*np.sin(np.radians(52.26)), 0, 1.809*np.cos(np.radians(52.26))]),
                ("H", [-1.809*np.sin(np.radians(52.26)), 0, 1.809*np.cos(np.radians(52.26))])]}
for basis in ["sto-3g", "4-31g", "6-31g*", "6-31g**"]:
    mol = gto.M(atom=geom["H2O"], unit="Bohr", basis=basis, cart=True, verbose=0)
    mf = scf.RHF(mol).run()
    print(basis, round(mf.e_tot, 3), round(-mf.mo_energy[mol.nelectron//2 - 1], 3))
```

## Source

Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996; reprint of the revised first edition, McGraw-Hill, 1989), Sec. 3.7, pp. 190-205, Tables 3.10-3.13, Ex. 3.32. All values in the first four columns computed for this note.
