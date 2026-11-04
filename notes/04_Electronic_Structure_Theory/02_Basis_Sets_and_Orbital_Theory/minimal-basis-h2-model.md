---
id: minimal-basis-h2-model
title: The minimal-basis H2 model
summary: Szabo's running example. One 1s function per atom gives a bonding (g) and antibonding (u) MO, four spin orbitals, six two-electron determinants, and a 2x2 full CI between the ground and doubly excited determinants. All integrals and energies at R = 1.4 bohr (STO-3G) computed with PySCF.
status: in-progress
kind: reference
level: introductory
tags: [h2, minimal-basis, sto-3g, model-system, full-ci, lcao]
prerequisites: [slater-determinants]
related: [h2-minimal-basis-correlation-analysis, excited-determinants, slater-condon-rules, spin-orbital-to-spatial-orbital, spin-adapted-configurations]
also: []
date: 2026-11-03
---

## The model

Each hydrogen has one real, normalized 1s function, $\phi_1$ centred on $\mathbf R_1$ and $\phi_2$ on $\mathbf R_2$. They overlap,

$$
S_{12} = \int\mathrm d\mathbf r\ \phi_1^*(\mathbf r)\,\phi_2(\mathbf r),
$$

with $S_{12} = 1$ at $R_{12} = 0$ and $S_{12}\to 0$ as $R_{12}\to\infty$. Symmetry alone (inversion through the bond centre) fixes the molecular orbitals as the symmetric and antisymmetric combinations:

$$
\psi_1 = \frac{\phi_1 + \phi_2}{\sqrt{2(1+S_{12})}}\quad(\text{gerade, bonding}),
\qquad
\psi_2 = \frac{\phi_1 - \phi_2}{\sqrt{2(1-S_{12})}}\quad(\text{ungerade, antibonding}).
$$

They are orthonormal (Szabo Ex. 2.6):

- **Norm.** $\langle\psi_1|\psi_1\rangle = (1 + 2S_{12} + 1)/(2(1+S_{12})) = 1$, and likewise for $\psi_2$.
- **Overlap.** $\langle\psi_1|\psi_2\rangle \propto 1 - S_{12} + S_{12} - 1 = 0$.

Expanding MOs in fixed atom-centred functions like this is the LCAO idea. In general the coefficients must be found by solving the Roothaan equations, but here symmetry gives them.

**Spin orbitals.** Following Szabo,

$$
\chi_1 = \psi_1\alpha,\quad \chi_2 = \psi_1\beta,\quad \chi_3 = \psi_2\alpha,\quad \chi_4 = \psi_2\beta,
$$

written $1, \bar 1, 2, \bar 2$ in spatial-orbital notation (bar means $\beta$). The Hartree-Fock ground state is

$$
|\Psi_0\rangle = |\chi_1\chi_2\rangle = |1\bar 1\rangle = \psi_1(\mathbf r_1)\psi_1(\mathbf r_2)\cdot 2^{-1/2}\big[\alpha(1)\beta(2) - \beta(1)\alpha(2)\big],
$$

a closed-shell singlet.

## The determinant space

Two electrons in four spin orbitals give $\binom42 = 6$ determinants: $|\Psi_0\rangle$, four singly excited determinants and one doubly excited determinant,

$$
|\Psi_1^3\rangle = |2\bar1\rangle,\quad
|\Psi_1^4\rangle = |\bar2\bar1\rangle,\quad
|\Psi_2^3\rangle = |12\rangle,\quad
|\Psi_2^4\rangle = |1\bar2\rangle,
\qquad
|\Psi_{12}^{34}\rangle = |2\bar2\rangle .
$$

(Notation: $|\Psi_a^r\rangle$ replaces occupied $\chi_a$ by virtual $\chi_r$ in the same column; see [[excited-determinants]].)

**Only $|\Psi_{12}^{34}\rangle$ mixes with the ground state.**

- **Symmetry.** $\psi_1\psi_1$ and $\psi_2\psi_2$ are both gerade, while every single excitation puts one electron in $\psi_1$ and one in $\psi_2$, which is ungerade overall.
- **Spin.** $|\Psi_1^4\rangle$ and $|\Psi_2^3\rangle$ have $M_S = \mp1$, while $|\Psi_0\rangle$ has $M_S = 0$.

The full CI ground state is therefore

$$
|\Phi_0\rangle = c_0|\Psi_0\rangle + c_{12}^{34}|\Psi_{12}^{34}\rangle .
$$

## Full CI matrix

With the [[slater-condon-rules]] (Szabo Ex. 2.9, 2.12), in spin orbitals:

$$
\mathbf H =
\begin{pmatrix}
\langle1|h|1\rangle + \langle2|h|2\rangle + \langle12|12\rangle - \langle12|21\rangle & \langle12|34\rangle - \langle12|43\rangle\\
\langle34|12\rangle - \langle34|21\rangle & \langle3|h|3\rangle + \langle4|h|4\rangle + \langle34|34\rangle - \langle34|43\rangle
\end{pmatrix}.
$$

After integrating out spin ([[spin-orbital-to-spatial-orbital]], Szabo Ex. 2.17 and 2.21):

$$
\mathbf H =
\begin{pmatrix}
2h_{11} + J_{11} & K_{12}\\
K_{12} & 2h_{22} + J_{22}
\end{pmatrix},
$$

with $h_{ii} = (\psi_i|h|\psi_i)$, $J_{ij} = (ii|jj)$ and $K_{12} = (12|21)$ in chemists' notation ([[integral-notation]]). The lower eigenvalue is

$$
E_{\text{FCI}} = \tfrac12(H_{11}+H_{22}) - \sqrt{\tfrac14(H_{22}-H_{11})^2 + K_{12}^2},
$$

and the **correlation energy** is $E_{\text{corr}} = E_{\text{FCI}} - E_0$, with $E_0 = H_{11}$.

!!! example "Numbers at R = 1.4 bohr, STO-3G (ζ = 1.24)"
    Computed with PySCF 2.14 by transforming the AO integrals to $\psi_1$, $\psi_2$ above. All in hartree (electronic energies unless marked "total").

    | Quantity | Value |
    |---|---:|
    | $S_{12}$ | 0.659318 |
    | $h_{11}$ | −1.252797 |
    | $h_{22}$ | −0.475602 |
    | $J_{11}$ | 0.674594 |
    | $J_{22}$ | 0.697495 |
    | $J_{12}$ | 0.663564 |
    | $K_{12}$ | 0.181258 |
    | $E_0 = 2h_{11}+J_{11}$ | −1.831000 |
    | $2h_{22}+J_{22}$ | −0.253709 |
    | $E_{\text{FCI}}$ | −1.851562 |
    | $E_{\text{corr}}$ | −0.020562 |
    | $1/R$ | 0.714286 |
    | $E_0$ total (RHF) | −1.116714 |
    | $E_{\text{FCI}}$ total | −1.137276 |

    To four decimals these are the values Szabo uses for this model in Chapters 3 and 4 ($E_0 = -1.8310$, $E_{\text{corr}} = -0.0206$); check against the book's tables when those chapters are written up. The FCI eigenvector is $(c_0, c_{12}^{34}) = (0.99363, -0.11272)$. The double excitation enters with a small negative weight, which lowers the probability of both electrons sitting on the same atom. The total energies equal PySCF `scf.RHF` and `fci.FCI` to all digits shown. The orbital energies are $\varepsilon_1 = h_{11}+J_{11} = -0.578203$ and $\varepsilon_2 = h_{22}+2J_{12}-K_{12} = 0.670268$.

```python
import numpy as np
from pyscf import gto, ao2mo
mol = gto.M(atom="H 0 0 0; H 0 0 1.4", unit="Bohr", basis="sto-3g")
S12 = mol.intor("int1e_ovlp")[0, 1]
C = np.column_stack([np.array([1, 1]) / np.sqrt(2 * (1 + S12)),
                     np.array([1, -1]) / np.sqrt(2 * (1 - S12))])
h = C.T @ (mol.intor("int1e_kin") + mol.intor("int1e_nuc")) @ C
g = ao2mo.restore(1, ao2mo.kernel(mol, C), 2)       # chemists' (ij|kl)
J11, J22, J12, K12 = g[0,0,0,0], g[1,1,1,1], g[0,0,1,1], g[0,1,0,1]
H = np.array([[2*h[0,0] + J11, K12], [K12, 2*h[1,1] + J22]])
E0, Efci = H[0, 0], np.linalg.eigvalsh(H)[0]
print(E0, Efci, Efci - E0)        # -1.8310  -1.85156  -0.02056
```

## Why this model is useful

It is the smallest system in which every concept in the first chapters of Szabo appears with numbers small enough to check by hand: closed and open shells, singlet and triplet configurations, Brillouin's theorem, the Hartree-Fock dissociation error, and size-consistency failures of truncated CI (two separated H$_2$ molecules).

## Source

Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996; reprint of the revised first edition, McGraw-Hill, 1989), Sec. 2.2.5, 2.2.7 and 2.3.1, pp. 55-58 and 62-67, Ex. 2.6, 2.9, 2.12, 2.17, 2.21. Numerical values from PySCF 2.14 (computed for this note).
