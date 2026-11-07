---
id: scf-procedure
title: The SCF procedure, with a worked STO-3G HeH+ calculation
summary: The Roothaan self-consistent field algorithm step by step (integrals, orthogonalization, guess, build F(P), diagonalize, new P, convergence), the variational energy at each iteration, and Szabo's HeH+ example reproduced iteration by iteration with a short Python implementation.
status: in-progress
kind: algorithm
level: intermediate
tags: [scf, hartree-fock, roothaan, algorithm, heh+, sto-3g, convergence]
prerequisites: [rhf, basis-orthogonalization]
related: [gaussian-basis-functions, population-analysis, koopmans-theorem]
order: 70
date: 2026-11-03
---

## Algorithm

The Roothaan equations $\mathbf F(\mathbf P)\mathbf C = \mathbf{SC}\boldsymbol\varepsilon$ ([[rhf]]) are nonlinear in $\mathbf C$. The SCF procedure solves them by fixed-point iteration.

1. **Specify the system.** Nuclear coordinates $\{\mathbf R_A\}$, charges $\{Z_A\}$, number of electrons $N$ (even, closed shell), and basis $\{\phi_\mu\}$.
2. **Compute integrals once.** $S_{\mu\nu}$, $H^{\text{core}}_{\mu\nu}$, and $(\mu\nu|\lambda\sigma)$.
3. **Orthogonalize.** Diagonalize $\mathbf S$ and form $\mathbf X$, symmetric or canonical ([[basis-orthogonalization]]).
4. **Guess $\mathbf P$.** $\mathbf P = \mathbf 0$ means $\mathbf F = \mathbf H^{\text{core}}$ in the first iteration, i.e. electron repulsion is ignored. Better guesses (superposition of atomic densities, extended Hückel) reduce iterations.
5. **Build $\mathbf G(\mathbf P)$** from $\mathbf P$ and the two-electron integrals, then $\mathbf F = \mathbf H^{\text{core}} + \mathbf G$.
6. **Energy.** $E_0 = \tfrac12\sum P_{\nu\mu}(H_{\mu\nu}+F_{\mu\nu})$ with the **same** $\mathbf P$ used to build $\mathbf F$.
7. **Transform.** $\mathbf F' = \mathbf X^\dagger\mathbf{FX}$.
8. **Diagonalize.** Solve $\mathbf F'\mathbf C' = \mathbf C'\boldsymbol\varepsilon$.
9. **Back-transform.** $\mathbf C = \mathbf{XC}'$.
10. **New density.** $P_{\mu\nu} = 2\sum_a^{N/2}C_{\mu a}C_{\nu a}^*$ from the $N/2$ lowest MOs (aufbau).
11. **Test convergence.** Stop if $\mathbf P$ (and $E_0$) changed by less than a threshold. Otherwise return to step 5.

After convergence, $\mathbf C$, $\boldsymbol\varepsilon$ and $\mathbf P$ give properties: the energy, Koopmans IPs ([[koopmans-theorem]]), populations and dipole moments ([[population-analysis]]).

**Variational energy at each step (Szabo Eq. 3.274).** $E_0$ from step 6 is the expectation value of $\hat H$ for the determinant that produced $\mathbf P$. It is therefore an upper bound at every iteration and usually converges monotonically from above. If $E_0$ is instead evaluated with the new $\mathbf P$ and the old $\mathbf F$, it is no longer a variational quantity.

**Practice.** Plain iteration can oscillate or diverge. Production codes add:

- **DIIS extrapolation**, which drives $\mathbf{FPS} - \mathbf{SPF}\to0$. This is the matrix form of Brillouin's theorem ([[brillouin-theorem]]).
- **Damping or level shifting.**
- **Second-order orbital optimization.**
- **Incremental Fock builds and integral screening.**

Convergence to the aufbau solution does not guarantee a minimum. Check stability (see [[h2-dissociation-rhf-uhf]]).

## Worked example: STO-3G HeH⁺ (Szabo Sec. 3.5.3)

**System.** He ($\zeta = 2.0925$) at the origin, H ($\zeta = 1.24$) at $R = 1.4632$ bohr, two electrons, one STO-3G 1s function per atom (contractions in [[gaussian-basis-functions]]). Both atoms are scaled 1s STO-3G functions, unlike the standard He basis.

**Integrals.** $S_{12} = 0.4508$, and

$$
\mathbf H^{\text{core}} = \begin{pmatrix}-2.6527 & -1.3472\\ -1.3472 & -1.7318\end{pmatrix}.
$$

**Iterations** from $\mathbf P = \mathbf 0$ (core-Hamiltonian guess). Each row shows the density from that iteration's diagonalization and the electronic energy evaluated with it:

| Iteration | $P_{11}$ | $P_{12}$ | $P_{22}$ | $E_0$ (hartree) |
|---:|---:|---:|---:|---:|
| 1 | 1.7266 | 0.2599 | 0.0391 | −4.141860 |
| 2 | 1.3342 | 0.5166 | 0.2000 | −4.226488 |
| 3 | 1.2899 | 0.5384 | 0.2247 | −4.227519 |
| 4 | 1.2864 | 0.5400 | 0.2267 | −4.227526 |
| 5 | 1.2862 | 0.5402 | 0.2269 | −4.227526 |
| 6 | 1.2861 | 0.5402 | 0.2269 | −4.227526 |

Charge flows from He to H as the repulsion is switched on, and the energy decreases monotonically.

**Converged results.**

$$
\mathbf C = \begin{pmatrix}0.8019 & -0.7823\\ 0.3368 & 1.0684\end{pmatrix}
\ \ (\text{column signs arbitrary}),
\qquad
\varepsilon_1 = -1.5975,\quad \varepsilon_2 = -0.0617 .
$$

- The occupied MO is bonding (same signs) and mostly He 1s.
- The virtual MO is antibonding and weighted towards H.
- $E_{\text{tot}} = E_0 + 2/R = -2.860659$ hartree.
- The calculated equilibrium bond length is $R_e = 1.3782$ bohr.

**Fragments in the same basis.**

| Species | Expression | Energy (hartree) |
|---|---|---:|
| H | $T_{22} + V_{22}^{\text{H}}$ | −0.466582 |
| He$^+$ | $T_{11} + V_{11}^{\text{He}}$ | −1.975512 |
| He | $2(T_{11} + V_{11}^{\text{He}}) + (11|11)$ | −2.643876 |

**Dissociation energies.**

- HeH$^+\to$ He + H$^+$: 0.2168 hartree (5.90 eV). The exact value is 2.04 eV; the He exponent 2.0925 suits the molecule, not the free atom (optimum 1.6875).
- HeH$^+\to$ He$^+$ + H: 0.4186 hartree.

The closed-shell products are correctly predicted to be lower. As $R\to\infty$ the RHF energy goes to that of He, $2(T_{11}+V_{11}) + (11|11)$ (Szabo Ex. 3.29), because both electrons end up on He.

!!! note "Agreement with Szabo"
    PySCF integrals reproduce every printed density matrix element and Szabo's $R_e$. The energies differ by about $3\times10^{-6}$ hartree (Szabo: −4.227529 and −2.860662) because of integral precision in the 1980s program.

    Eq. (3.279) in the book prints 0.4168 hartree for HeH$^+\to$ He$^+$ + H. Szabo's own Table 3.6 energies give $-1.975514 - 0.466582 + 2.860662 = 0.4186$, so the printed value has transposed digits.

## Implementation

A complete restricted SCF in about 30 lines, using PySCF only for integrals. It is Szabo's Appendix B program in NumPy.

```python
import numpy as np
from pyscf import gto

A3 = [0.109818, 0.405771, 2.22766]          # STO-3G 1s exponents for zeta = 1
D3 = [0.444635, 0.535328, 0.154329]
def sto3g_1s(zeta):
    return [[0] + [[a * zeta**2, d] for a, d in zip(A3, D3)]]

mol = gto.M(atom="He 0 0 0; H 0 0 1.4632", unit="Bohr", charge=1,
            basis={"He": sto3g_1s(2.0925), "H": sto3g_1s(1.24)}, verbose=0)
S = mol.intor("int1e_ovlp")
H = mol.intor("int1e_kin") + mol.intor("int1e_nuc")
eri = mol.intor("int2e")                     # (mu nu | lam sig)

s, U = np.linalg.eigh(S)
X = U @ np.diag(s**-0.5) @ U.T               # symmetric orthogonalization
P = np.zeros_like(S)
nocc = mol.nelectron // 2
for it in range(1, 50):
    G = np.einsum("ls,mnsl->mn", P, eri) - 0.5 * np.einsum("ls,mlsn->mn", P, eri)
    F = H + G
    E = 0.5 * np.sum(P * (H + F))            # variational energy with the P that built F
    e, Cp = np.linalg.eigh(X.T @ F @ X)
    C = X @ Cp
    Pnew = 2 * C[:, :nocc] @ C[:, :nocc].T
    if np.abs(Pnew - P).max() < 1e-8:
        break
    P = Pnew
print(E, E + mol.energy_nuc(), e)            # -4.227526  -2.860659  [-1.5975 -0.0617]
```

The index pattern implements $G_{\mu\nu} = \sum_{\lambda\sigma}P_{\lambda\sigma}[(\mu\nu|\sigma\lambda) - \tfrac12(\mu\lambda|\sigma\nu)]$. Swapping the indices of the exchange term silently gives a wrong but converging SCF, so check against a reference value.

## Source

Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996; reprint of the revised first edition, McGraw-Hill, 1989), Sec. 3.4.6, pp. 145-149, Eqs. (3.181)-(3.185), Ex. 3.17; Sec. 3.5.3, pp. 168-180, Table 3.5-3.6, Eqs. (3.268)-(3.281), Ex. 3.28-3.29; Appendix B. All numbers recomputed for this note.
