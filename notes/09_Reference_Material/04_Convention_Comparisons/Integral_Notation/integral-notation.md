---
id: integral-notation
title: One- and two-electron integral notation
summary: Physicists' ⟨ij|kl⟩ versus chemists' [ij|kl] / (ij|kl) notation for spin and spatial orbitals, the antisymmetrized integral ⟨ij||kl⟩, permutational symmetries, and Coulomb and exchange integrals. Includes the PySCF index conventions.
status: in-progress
kind: reference
level: introductory
tags: [notation, integrals, eri, chemists-notation, physicists-notation, coulomb, exchange]
prerequisites: [spin-orbitals-and-antisymmetry]
related: [slater-condon-rules, spin-orbital-to-spatial-orbital, second-quantized-operators, electron-repulsion-integrals-md-os-rys]
also: []
date: 2026-11-03
---

## Definitions (Szabo Table 2.2)

Spin orbitals are $\chi$ with coordinate $\mathbf x = \{\mathbf r,\omega\}$, and spatial orbitals are $\psi$ with coordinate $\mathbf r$. The one-electron operator $h$ and $r_{12}^{-1}$ act as written.

| | Spin orbitals $\chi$ | Spatial orbitals $\psi$ |
|---|---|---|
| one-electron | $[i|h|j] = \langle i|h|j\rangle = \int\mathrm d\mathbf x_1\,\chi_i^*(1)\,h(1)\,\chi_j(1)$ | $(i|h|j) = h_{ij} = \int\mathrm d\mathbf r_1\,\psi_i^*(1)\,h(1)\,\psi_j(1)$ |
| chemists' | $[ij|kl] = \int\mathrm d\mathbf x_1\mathrm d\mathbf x_2\,\chi_i^*(1)\chi_j(1)\,r_{12}^{-1}\,\chi_k^*(2)\chi_l(2)$ | $(ij|kl) = \int\mathrm d\mathbf r_1\mathrm d\mathbf r_2\,\psi_i^*(1)\psi_j(1)\,r_{12}^{-1}\,\psi_k^*(2)\psi_l(2)$ |
| physicists' | $\langle ij|kl\rangle = \int\mathrm d\mathbf x_1\mathrm d\mathbf x_2\,\chi_i^*(1)\chi_j^*(2)\,r_{12}^{-1}\,\chi_k(1)\chi_l(2)$ | written the same way with $\psi$ and $\mathbf r$ |
| antisymmetrized | $\langle ij||kl\rangle = \langle ij|kl\rangle - \langle ij|lk\rangle$ | |

## How to read them

- **Chemists' (Mulliken).** Group by electron: $(ij|$ is the "charge distribution" $\psi_i^*\psi_j$ of electron 1, and $|kl)$ that of electron 2. Complex-conjugated functions come first in each pair.
- **Physicists' (Dirac).** Group by bra and ket: $\langle ij|$ holds electron 1 then electron 2 (conjugated), and $|kl\rangle$ holds electron 1 then electron 2. The conversion is

$$
\langle ij|kl\rangle = [ik|jl],
\qquad
[ij|kl] = \langle ik|jl\rangle .
$$

- **Antisymmetrized.** The exchange term swaps the two ket labels:

$$
\langle ij||kl\rangle = \langle ij|kl\rangle - \langle ij|lk\rangle = [ik|jl] - [il|jk].
$$

  It vanishes when $i = j$ or $k = l$, and satisfies $\langle ij||kl\rangle = -\langle ji||kl\rangle = -\langle ij||lk\rangle = \langle ji||lk\rangle$.

!!! warning "Same symbol, different meaning"
    $\langle ij|kl\rangle$ and $(ij|kl)$ with the same four labels are different integrals. Every expression must say which notation it uses. Szabo writes most general formulas in physicists' notation over spin orbitals and switches to chemists' notation over spatial orbitals for closed shells.

## Permutational symmetry

Both integrals are real for real orbitals. In general:

- **Interchange of electron labels.** $\langle ij|kl\rangle = \langle ji|lk\rangle$ and $[ij|kl] = [kl|ij]$.
- **Hermiticity.** $\langle ij|kl\rangle = \langle kl|ij\rangle^*$ and $[ij|kl] = [ji|lk]^*$.
- **Real orbitals.** Additionally $(ij|kl) = (ji|kl) = (ij|lk) = (ji|lk)$, giving the full **8-fold** symmetry of chemists' integrals:
$$
(ij|kl) = (ji|kl) = (ij|lk) = (ji|lk) = (kl|ij) = (lk|ij) = (kl|ji) = (lk|ji).
$$

## Coulomb and exchange integrals

For spatial orbitals,

$$
J_{ij} = (ii|jj) = \langle ij|ij\rangle,
\qquad
K_{ij} = (ij|ji) = \langle ij|ji\rangle .
$$

**Meaning.**

- $J_{ij}$ is the classical Coulomb repulsion between the charge clouds $|\psi_i(\mathbf r_1)|^2$ and $|\psi_j(\mathbf r_2)|^2$.
- $K_{ij}$ has no classical analogue. It arises only from antisymmetry.

**Properties (Szabo Ex. 2.19, 2.20).**

- $J_{ii} = K_{ii}$.
- $J_{ij}^* = J_{ij}$ and $K_{ij}^* = K_{ij}$: both are real.
- $J_{ij} = J_{ji}$ and $K_{ij} = K_{ji}$.
- $J_{ij} > 0$ and $K_{ij} > 0$: $K_{ij}$ is the self-repulsion of the charge distribution $\psi_i^*\psi_j$, and the Coulomb kernel is positive definite.
- For real orbitals, $K_{ij} = (ij|ji) = (ij|ij) = \langle ij|ji\rangle = \langle ii|jj\rangle$.

## In code (PySCF)

`mol.intor("int2e")` and `ao2mo` return **chemists'** integrals over spatial functions, `eri[p,q,r,s] = (pq|rs)`. Convert to physicists' order with `eri.transpose(0,2,1,3)`, which gives `g[p,q,r,s] = <pq|rs>`. Check the convention before contracting with an RDM, since $\Gamma$ in one notation pairs with integrals in the other.

```python
from pyscf import gto, ao2mo
mol = gto.M(atom="H 0 0 0; H 0 0 0.74", basis="sto-3g")
eri = ao2mo.restore(1, mol.intor("int2e", aosym="s8"), mol.nao)   # (pq|rs)
phys = eri.transpose(0, 2, 1, 3)                                   # <pq|rs>
assert abs(phys[0, 1, 0, 1] - eri[0, 0, 1, 1]) < 1e-14            # <01|01> = (00|11) = J
```

## Source

Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996; reprint of the revised first edition, McGraw-Hill, 1989), Sec. 2.3.2 and 2.3.6, pp. 67-68 and 85-86, Table 2.2, Eqs. (2.179)-(2.185), Ex. 2.19-2.20. PySCF conventions from the PySCF documentation and checked in code.
