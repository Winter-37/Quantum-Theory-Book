---
id: slater-condon-rules
title: Slater-Condon rules for matrix elements between determinants
summary: Matrix elements of one- and two-electron operators between Slater determinants of orthonormal spin orbitals depend only on how many spin orbitals differ (0, 1, 2, or more). Maximum coincidence, the three cases, the energy of a determinant, Koopmans-type ionization energy, an outline of the derivation, and a code check against PySCF full CI.
status: in-progress
kind: derivation
level: intermediate
tags: [slater-condon, matrix-elements, determinants, ci, hamiltonian-matrix]
prerequisites: [slater-determinants, integral-notation, molecular-hamiltonian]
related: [excited-determinants, minimal-basis-h2-model, spin-orbital-to-spatial-orbital, second-quantized-operators]
also: []
date: 2026-11-03
---

## Operators

Quantum chemistry needs two kinds of $N$-electron operators (see [[molecular-hamiltonian]]):

$$
\hat{\mathcal O}_1 = \sum_{i=1}^{N} h(i),
\qquad
\hat{\mathcal O}_2 = \sum_{i=1}^{N}\sum_{j>i}^{N} r_{ij}^{-1}.
$$

$\hat H = \hat{\mathcal O}_1 + \hat{\mathcal O}_2$ with $h$ the core Hamiltonian. All spin orbitals below come from one orthonormal set, and integrals are in physicists' notation over spin orbitals ([[integral-notation]]).

## Maximum coincidence

Before applying the rules, reorder the columns of one determinant so that as many identical spin orbitals as possible sit in the same columns as in the other. Each column swap multiplies by $-1$ ([[slater-determinants]]).

**Example.** $|K\rangle = |abcd\rangle$ and $|L\rangle = |crds\rangle$ share $c$ and $d$. Swapping columns,

$$
|crds\rangle = -|crsd\rangle = |srcd\rangle ,
$$

so after two swaps $|L\rangle = |srcd\rangle$, which differs from $|K\rangle$ by $a\to s$, $b\to r$ with sign $+1$.

The determinants are then classified by the number of differing spin orbitals:

- **Case 1:** $|K\rangle = |\cdots mn\cdots\rangle$ with $|L\rangle = |K\rangle$.
- **Case 2:** one difference, $m\to p$: $|L\rangle = |\cdots pn\cdots\rangle$.
- **Case 3:** two differences, $m\to p$ and $n\to q$: $|L\rangle = |\cdots pq\cdots\rangle$.
- **Three or more differences:** both matrix elements vanish.

## The rules (Szabo Tables 2.3 and 2.4)

Sums over $m, n$ run over the spin orbitals occupied in $|K\rangle$.

| Case | $\langle K|\hat{\mathcal O}_1|L\rangle$ | $\langle K|\hat{\mathcal O}_2|L\rangle$ |
|---|---|---|
| 1 (identical) | $\sum_m^N\langle m|h|m\rangle$ | $\tfrac12\sum_m^N\sum_n^N\langle mn||mn\rangle$ |
| 2 ($m\to p$) | $\langle m|h|p\rangle$ | $\sum_n^N\langle mn||pn\rangle$ |
| 3 ($m\to p$, $n\to q$) | $0$ | $\langle mn||pq\rangle$ |
| $\ge3$ differences | $0$ | $0$ |

In Case 1 the double sum can be written with the factor removed, $\sum_m\sum_{n>m}\langle mn||mn\rangle$, because $\langle mm||mm\rangle = 0$ and $\langle mn||mn\rangle = \langle nm||nm\rangle$.

**Why the cut-offs.**

- A one-electron operator can change at most one electron's orbital.
- A two-electron operator can change at most two.
- Any further difference leaves an overlap $\langle\chi_x|\chi_y\rangle = 0$ in every term.

## Ground state and excited determinants

Applied to $|\Psi_0\rangle = |\chi_1\cdots\chi_N\rangle$ ([[excited-determinants]]):

$$
E_0 = \langle\Psi_0|\hat H|\Psi_0\rangle = \sum_a^N\langle a|h|a\rangle + \tfrac12\sum_a^N\sum_b^N\langle ab||ab\rangle ,
$$

$$
\langle\Psi_0|\hat H|\Psi_a^r\rangle = \langle a|h|r\rangle + \sum_b^N\langle ab||rb\rangle ,
\qquad
\langle\Psi_0|\hat H|\Psi_{ab}^{rs}\rangle = \langle ab||rs\rangle ,
$$

and the ground state does not couple to triples and higher. The single-excitation element is the occupied-virtual Fock matrix element $f_{ar}$, which vanishes for Hartree-Fock orbitals (Brillouin's theorem, Szabo Ch. 3).

**Reading energies off a picture.** Each occupied spin orbital contributes $\langle m|h|m\rangle$, and each distinct pair contributes $\langle mn||mn\rangle = \langle mn|mn\rangle - \langle mn|nm\rangle$. Example (Szabo Ex. 2.11):

$$
\langle\chi_1\chi_2\chi_3|\hat H|\chi_1\chi_2\chi_3\rangle
= \sum_{m=1}^{3}\langle m|h|m\rangle + \langle12||12\rangle + \langle13||13\rangle + \langle23||23\rangle .
$$

!!! example "One-electron operator between singles (Szabo Ex. 2.13)"
    Both determinants are singles relative to the same $|\Psi_0\rangle$. Bring them into maximum coincidence first.
    $$
    \langle\Psi_a^r|\hat{\mathcal O}_1|\Psi_b^s\rangle =
    \begin{cases}
    0 & a\ne b,\ r\ne s\ \ (\text{two differences})\\
    \langle r|h|s\rangle & a = b,\ r\ne s\\
    -\langle b|h|a\rangle & a\ne b,\ r = s\\
    \sum_c^N\langle c|h|c\rangle - \langle a|h|a\rangle + \langle r|h|r\rangle & a = b,\ r = s
    \end{cases}
    $$
    The minus sign in the third line comes from the reordering. Write $|\Psi_a^r\rangle = |\cdots r\cdots b\cdots\rangle$ and $|\Psi_b^r\rangle = |\cdots a\cdots r\cdots\rangle$. Moving $r$ to the same column in both costs one swap, and the remaining difference is $b\to a$.

!!! example "Ionization energy from the rules (Szabo Ex. 2.14)"
    Remove an electron from $\chi_a$: $|{}^{N-1}\Psi_a\rangle$ has all orbitals of $|\Psi_0\rangle$ except $\chi_a$, with the same orbitals (no relaxation). With the Case 1 rule for both energies, the difference is every term that contains $a$:
    $$
    {}^{N}E_0 - {}^{N-1}E_a = \langle a|h|a\rangle + \sum_{b}^{N}\langle ab||ab\rangle .
    $$
    Here $\tfrac12\sum_{mn}$ loses the terms $m=a$ and $n=a$, which are equal, giving $\sum_b\langle ab||ab\rangle$ (and $\langle aa||aa\rangle = 0$). The right side is the Hartree-Fock orbital energy $\varepsilon_a$, so the frozen-orbital ionization energy is ${}^{N-1}E_a - {}^NE_0 = -\varepsilon_a$. This is Koopmans' theorem, derived in Szabo Ch. 3.

## Outline of the derivation

Write a determinant as an antisymmetrized Hartree product,

$$
|K\rangle = (N!)^{-1/2}\sum_{n=1}^{N!}(-1)^{p_n}\,\mathscr P_n\{\chi_m(1)\chi_n(2)\cdots\chi_k(N)\},
$$

where $\mathscr P_n$ permutes electron labels and $p_n$ is its parity. Three steps then give all the rules:

1. **Overlap.** Each product in $\langle K|$ pairs with each product in $|L\rangle$. The integrals factor into one-electron overlaps, so a term survives only if every electron is in the same spin orbital on both sides. This gives $\langle K|L\rangle = 1$ for identical determinants and $0$ otherwise.
2. **Reduce to one electron or one pair.** $\hat{\mathcal O}_1$ and $\hat{\mathcal O}_2$ are symmetric in the electron labels, so they commute with every $\mathscr P_n$. One can use $\langle K|\hat{\mathcal O}_1|L\rangle = N\langle K|h(1)|L\rangle$ and $\langle K|\hat{\mathcal O}_2|L\rangle = \tfrac{N(N-1)}{2}\langle K|r_{12}^{-1}|L\rangle$.
3. **Count surviving terms.** In $\langle K|h(1)|L\rangle$ electrons $2,\dots,N$ must match exactly, which leaves the electron-1 integrals. In $\langle K|r_{12}^{-1}|L\rangle$ electrons $3,\dots,N$ must match, which leaves "direct" and "exchange" assignments of electrons 1 and 2. That is the origin of $\langle mn|pq\rangle - \langle mn|qp\rangle$. Counting the $(N-1)!$ or $(N-2)!$ permutations of the spectator electrons cancels the prefactors.

Szabo works through each case explicitly (Sec. 2.3.4). The second-quantized route ([[second-quantized-operators]]) is shorter.

**Independent-electron check (Szabo Ex. 2.15).** If $h\chi_i = \varepsilon_i\chi_i$, then $\sum_i h(i)$ commutes with every permutation and acts on each Hartree product as $\sum_{i\in\text{occ}}\varepsilon_i$. A determinant of eigen-spin-orbitals is therefore an eigenfunction with eigenvalue $\varepsilon_i + \varepsilon_j + \cdots + \varepsilon_k$.

## Verification in code

The script below builds the full determinant-space Hamiltonian of LiH (STO-3G, 12 spin orbitals, 4 electrons, $\binom{12}{4} = 495$ determinants) from the table above alone. It applies maximum coincidence with explicit permutation signs.

Results:

- The lowest eigenvalue plus $V_{nn}$ is −7.882324378884 hartree, identical to PySCF `fci.FCI` to $10^{-12}$.
- The Case 1 element for the reference determinant reproduces the RHF energy, −7.861864769809 hartree.

```python
import numpy as np, itertools
from pyscf import gto, scf, ao2mo, fci

mol = gto.M(atom="Li 0 0 0; H 0 0 1.6", basis="sto-3g", verbose=0)
mf = scf.RHF(mol).run()
K, C, N = mol.nao, mf.mo_coeff, mol.nelectron
hs = C.T @ mf.get_hcore() @ C
gs = ao2mo.restore(1, ao2mo.kernel(mol, C), K)                 # (pq|rs), spatial
sp, sg = np.arange(2*K) // 2, np.arange(2*K) % 2               # spatial index, spin
h = hs[np.ix_(sp, sp)] * (sg[:, None] == sg[None, :])
g = gs[np.ix_(sp, sp, sp, sp)].transpose(0, 2, 1, 3)           # <pq|rs>
g = g * ((sg[:, None, None, None] == sg[None, None, :, None]) &
         (sg[None, :, None, None] == sg[None, None, None, :]))
A = g - g.transpose(0, 1, 3, 2)                                # <pq||rs>

def element(Kd, Ld):
    Kd, Ld = list(Kd), list(Ld)
    dK = [p for p in Kd if p not in Ld]; dL = [p for p in Ld if p not in Kd]
    if len(dK) > 2: return 0.0
    Lm = Ld.copy()
    for m, p in zip(dK, dL): Lm[Lm.index(p)] = m               # maximum coincidence
    sign = round(np.linalg.det(np.eye(N)[[Kd.index(x) for x in Lm]]))
    if not dK:
        return sum(h[m, m] for m in Kd) + 0.5 * sum(A[m, n, m, n] for m in Kd for n in Kd)
    if len(dK) == 1:
        m, p = dK[0], dL[0]
        return sign * (h[m, p] + sum(A[m, n, p, n] for n in Kd))
    (m, n), (p, q) = dK, dL
    return sign * A[m, n, p, q]

dets = list(itertools.combinations(range(2*K), N))
H = np.array([[element(a, b) for b in dets] for a in dets])
print(np.linalg.eigvalsh(H)[0] + mol.energy_nuc(), fci.FCI(mf).kernel()[0])
```

## Source

Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996; reprint of the revised first edition, McGraw-Hill, 1989), Sec. 2.3.3-2.3.4, pp. 68-81, Tables 2.3-2.6, Eqs. (2.95)-(2.158), Ex. 2.11-2.16.
