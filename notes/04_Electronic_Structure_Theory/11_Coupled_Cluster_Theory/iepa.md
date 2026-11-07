---
id: iepa
title: Independent electron pair approximation (IEPA), Epstein-Nesbet and first-order pairs
summary: The exact correlation energy is a sum of pair energies e_ab built from the doubles coefficients of full CI. IEPA computes each pair energy from a separate pair-at-a-time CI in which only that pair is excited. Neglecting couplings between doubles gives Epstein-Nesbet pairs, and replacing the diagonal by orbital-energy differences gives first-order pairs (= MP2). IEPA is size consistent but not invariant to unitary rotations of degenerate orbitals; computed H2-dimer and water results show both features.
status: in-progress
kind: theory
level: intermediate
tags: [iepa, pair-theory, epstein-nesbet, first-order-pairs, bethe-goldstone, invariance, size-consistency]
prerequisites: [full-ci, cisd, size-consistency]
related: [coupled-pair-approximations, mp2, minimal-basis-h2-model, linked-cluster-theorem]
order: 10
date: 2026-11-03
---

## Pair decomposition of the exact correlation energy

**Exact statement.** Write the full CI wave function in intermediate normalization, $|\Phi_0\rangle = |\Psi_0\rangle + \sum c_a^r|\Psi_a^r\rangle + \sum_{a<b,\,r<s} c_{ab}^{rs}|\Psi_{ab}^{rs}\rangle + \cdots$. Because $H$ has at most two-body terms and Hartree-Fock orbitals satisfy Brillouin's theorem ([[brillouin-theorem]]), only doubles contribute to the energy expression:

$$
E_{\text{corr}} = \sum_{a<b}\sum_{r<s} c_{ab}^{rs}\,\langle\Psi_0|H|\Psi_{ab}^{rs}\rangle = \sum_{a<b} e_{ab},
\qquad
e_{ab} = \sum_{r<s} c_{ab}^{rs}\,\langle ab||rs\rangle .
$$

$e_{ab}$ is the **pair correlation energy** of the electrons that occupy spin orbitals $\chi_a,\chi_b$ in Hartree-Fock.

**The catch.** The decomposition is exact but useless as it stands: the coefficients $c_{ab}^{rs}$ come from the full $N$-electron calculation. The question is whether each $e_{ab}$ can be estimated by a two-electron-sized calculation, turning one $N$-electron problem into $N(N-1)/2$ pair problems.

## IEPA: one pair at a time

**Pair function.** Leave the other $N-2$ electrons in their Hartree-Fock spin orbitals and let only the pair $ab$ be excited (singles ignored):

$$
|\Psi_{ab}\rangle = |\Psi_0\rangle + \sum_{r<s} c_{ab}^{rs}|\Psi_{ab}^{rs}\rangle ,
\qquad E_{ab} = E_0 + e_{ab}.
$$

**Pair equations.** Projecting $(H - E_0)|\Psi_{ab}\rangle = e_{ab}|\Psi_{ab}\rangle$ onto $\langle\Psi_0|$ and $\langle\Psi_{ab}^{rs}|$:

$$
\sum_{t<u}\langle\Psi_0|H|\Psi_{ab}^{tu}\rangle\,c_{ab}^{tu} = e_{ab},
$$

$$
\langle\Psi_{ab}^{rs}|H|\Psi_0\rangle + \sum_{t<u}\langle\Psi_{ab}^{rs}|H - E_0|\Psi_{ab}^{tu}\rangle\,c_{ab}^{tu} = e_{ab}\,c_{ab}^{rs}.
$$

This is a small CI eigenvalue problem in the space $\{\Psi_0, \Psi_{ab}^{rs}\}$, one for every occupied pair. The total is $E_{\text{corr}}(\text{IEPA}) = \sum_{a<b} e_{ab}$.

**What is left out.** Matrix elements $\langle\Psi_{ab}^{rs}|H|\Psi_{cd}^{tu}\rangle$ between different pairs never appear. Each pair is variational on its own, but the **sum** of pair energies is not an upper bound: IEPA can give more than 100% of the correlation energy.

**Names.** The scheme was introduced independently by Sinanoğlu (many-electron theory) and Nesbet (Bethe-Goldstone theory). It is also called "pair-at-a-time CI". Despite the name it is not an approximation to DCI: it is a different approximation to full CI, and unlike DCI it is size consistent ([[size-consistency]]).

## From IEPA to Epstein-Nesbet and first-order pairs

**Epstein-Nesbet (EN) pairs.** Drop the coupling between different doubles of the same pair (keep only $t=r$, $u=s$ in the sum). Solving the second equation for $c_{ab}^{rs}$ and inserting in the first gives

$$
e_{ab} = \sum_{r<s}\frac{|\langle ab||rs\rangle|^2}{\langle\Psi_0|H|\Psi_0\rangle - \langle\Psi_{ab}^{rs}|H|\Psi_{ab}^{rs}\rangle + e_{ab}}
\;\approx\;
e_{ab}^{\text{EN}} = \sum_{r<s}\frac{|\langle ab||rs\rangle|^2}{\langle\Psi_0|H - E_0|\Psi_0\rangle - \langle\Psi_{ab}^{rs}|H - E_0|\Psi_{ab}^{rs}\rangle},
$$

where in the second step the small $e_{ab}$ is dropped from the denominator. The EN denominator is the full diagonal energy of the doubly excited determinant.

**First-order pairs.** Replace the diagonal difference by orbital-energy differences, $\langle\Psi_{ab}^{rs}|H|\Psi_{ab}^{rs}\rangle - E_0 \approx \varepsilon_r + \varepsilon_s - \varepsilon_a - \varepsilon_b$:

$$
e_{ab}^{(1)} = \sum_{r<s}\frac{|\langle ab||rs\rangle|^2}{\varepsilon_a + \varepsilon_b - \varepsilon_r - \varepsilon_s},
\qquad
E_{\text{corr}}^{(1)} = \sum_{a<b}e_{ab}^{(1)} = E_0^{(2)} .
$$

The sum of first-order pair energies **is** the second-order Møller-Plesset energy ([[mp2]]). The simplest pair theory and the simplest perturbation theory coincide.

**Hierarchy of denominators.** IEPA → EN → first order is a sequence of cruder denominators. The same EN expression reappears in [[linked-cluster-theorem]] as the infinite-order sum of a class of diagrams.

!!! example "Minimal-basis H₂ (Szabo Ex. 5.1)"
    For a two-electron system IEPA is full CI, so $E_{\text{corr}}(\text{IEPA}) = \Delta - (\Delta^2 + K_{12}^2)^{1/2}$ with $2\Delta = 2(\varepsilon_2-\varepsilon_1) + J_{11} + J_{22} - 4J_{12} + 2K_{12}$ ([[full-ci]]).

    - **First-order pairs.** Summing over spin orbitals $a,b = 1,\bar1$ and $r,s = 2,\bar2$ gives $E^{(1)}_{\text{corr}} = K_{12}^2/\big(2(\varepsilon_1 - \varepsilon_2)\big)$.
    - **Check.** Replacing $\Delta$ by $\varepsilon_2 - \varepsilon_1$ in the exact result and expanding $(1+x)^{1/2}\approx 1 + x/2$ gives the same expression.
    - **Numbers (STO-3G, R = 1.4 bohr).** First-order pairs give −0.013158, the exact (= IEPA) value is −0.020562 hartree. Computed for this note.

## Invariance problem

**Statement.** IEPA (and EN) energies depend on which set of degenerate occupied orbitals is used. Full CI, DCI, MP2 and coupled cluster depend only on the occupied *space*. IEPA does not, because the decomposition into "pairs" changes when the occupied orbitals are mixed.

**Szabo's test case.** Two minimal-basis H$_2$ molecules infinitely far apart. Each monomer has a doubly occupied $1_i$ and an empty $2_i$.

- **Localized orbitals** ($1_1, 1_2, 2_1, 2_2$). Of the six spin-orbital pairs only $(1_1\bar1_1)$ and $(1_2\bar1_2)$ have nonzero pair energies. Each equals the exact monomer correlation energy, so IEPA is exact: $2(\Delta - (\Delta^2+K_{12}^2)^{1/2})$.
- **Delocalized orbitals** $1_\pm = 2^{-1/2}(1_1 \pm 1_2)$, $2_\pm = 2^{-1/2}(2_1 \pm 2_2)$. The Hartree-Fock determinant is identical, but the integrals among the new orbitals are halved and spread over more pairs. Now parallel-spin pairs and cross pairs contribute, and the sum differs from the exact answer.

**Size consistency survives.** For $N$ separated monomers the IEPA energy in delocalized orbitals is not $N$ times the monomer energy, but it still grows linearly in $N$, unlike DCI's $\sqrt N$. Szabo's working definition of size consistency is linear growth with $N$; equality to $N$ times the monomer additionally needs invariance.

!!! example "H₂ dimer, STO-3G, R = 1.4 bohr, monomers 100 bohr apart"
    Spin-orbital pairs; correlation energies in hartree. Computed for this note with the pair code below; "exact" is twice the monomer full CI, −0.041124.

    | Method | Localized | Delocalized |
    |---|---:|---:|
    | MP2 (first-order pairs) | −0.02632 | −0.02632 |
    | Epstein-Nesbet | −0.04166 | −0.03241 |
    | IEPA | −0.04112 | −0.02763 |
    | DCI | −0.04061 | −0.04061 |

    - **IEPA** is exact in localized orbitals and loses a third of the correlation energy in delocalized ones.
    - **Tails between the molecules.** The table uses a real dimer 100 bohr apart, so the intermolecular Coulomb tails are not exactly zero. In Szabo's idealized model, where every intermolecular integral is set to zero, delocalized spin-orbital IEPA gives −0.02746 (Szabo −0.0275).
    - **Spin-adapted pairs (Szabo Eqs. 5.40-5.45).** The aā and bb̄ pairs are already singlets (−0.006865 each). For the ab pair, four singlet functions arise from the ab → rs doubles; only one couples to $|\Psi_0\rangle$ (element $K_{12} = 0.181258$, $2\Delta'' = 2.723161$). The pair energy is −0.012012 with that one function and also with all four. Total spin-adapted IEPA: −0.02574 hartree, against Szabo's −0.0258. The 0.06 mHa difference is at rounding level for his tabulated integrals.
    - **EN** is likewise noninvariant (Szabo Ex. 5.9). In localized orbitals it equals $-K_{12}^2/\Delta$ for the dimer.
    - **MP2 and DCI** are invariant: same value in both bases.

## How good is IEPA?

**Atoms (literature values quoted by Szabo, checked against the page images of Table 5.1 and p. 285).**

- **Be.** Nesbet's large Slater-basis IEPA gives −0.0930 hartree against the exact −0.094, about 99%. The (1s,1s̄) and (2s,2s̄) opposite-spin pairs dominate (−0.0418 and −0.0454); parallel-spin pairs are tiny (−0.0008), because Hartree-Fock already builds in the Fermi hole for parallel spins.
- **Ne.** About 107% of the exact correlation energy in a large basis, estimated 110% at the basis-set limit.
- **N₂.** IEPA −0.412 hartree against an estimated full CI −0.35 in the same basis (18% too large); DCI gave −0.324.

**Molecules (Szabo Table 5.3, H₂O, 39-STO basis).** IEPA −0.3274 against the estimated full CI −0.296 ± 0.001 hartree. That is 10.6% too large. Szabo's text says 13%; the table on p. 296 confirms the numbers, so the 13% does not follow from them (it is close to the 12.6% excess over L-CCA, −0.2908). Comparing with the exact correlation energy (−0.37) instead of the basis-set full CI would wrongly suggest that IEPA is the best method.

!!! example "Water, Szabo geometry (R = 1.809 bohr, 104.52°), all electrons correlated"
    Computed for this note. "% FCI" is relative to full CI in the same basis.

    | Basis | MP2 | EN | IEPA | FCI |
    |---|---:|---:|---:|---:|
    | STO-3G | −0.035499 (71.7%) | −0.053812 (108.7%) | −0.051191 (103.4%) | −0.049486 |
    | 6-31G | −0.128803 (94.1%) | −0.170842 (124.8%) | −0.174935 (127.8%) | −0.136848 |

    Once the virtual space grows, the neglected pair-pair coupling matters: IEPA and EN overshoot by a quarter in 6-31G. The coupled-pair methods of [[coupled-pair-approximations]] fix this.

## Code

Spin-orbital pair code used for the tables. `A[p,q,r,s]` is $\langle pq||rs\rangle$ with occupied spin orbitals first; `D` is $\varepsilon_i + \varepsilon_j - \varepsilon_a - \varepsilon_b$. The linear doubles residual `R_lin` is the action of $H - E_0$ on a doubles vector plus the $\langle\Psi_{ij}^{ab}|H|\Psi_0\rangle$ term, written with $\langle ab||cd\rangle$, $\langle kl||ij\rangle$ and $\langle kb||cj\rangle$ blocks. Each IEPA pair is solved with all other amplitudes masked to zero.

```python
def iepa(d, tol=1e-12):
    no = d.no; e = np.zeros((no, no))
    for i in range(no):
        for j in range(i + 1, no):
            mask = np.zeros((no, no)); mask[i, j] = mask[j, i] = 1
            t = d.oovv / d.D * mask[:, :, None, None]          # start from first-order pair
            for it in range(500):
                eij = d.pair_e(t)[i, j]                          # e_ij = sum_ab <ij||ab> t_ij^ab / 2
                tn = (d.R_lin(t) - eij * t) * mask[:, :, None, None] / d.D
                if abs(tn - t).max() < tol: t = tn; break
                t = tn
            e[i, j] = d.pair_e(t)[i, j]
    return e.sum()

def epstein_nesbet(d):            # diag = <Phi_ij^ab| H - E0 |Phi_ij^ab>
    return 0.25 * np.sum(d.oovv ** 2 / -d.diag)
```

The code was validated against energies of a determinant-space Hamiltonian built with PySCF's full CI routines.

## Source

Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996; reprint of the revised first edition, McGraw-Hill, 1989), Sec. 5.1, pp. 272-285, Eqs. (5.1)-(5.19), Ex. 5.1, 5.9; Table 5.1 (Be pair energies, from Nesbet), Table 5.3, p. 296. Numerical tables computed for this note with PySCF 2.14.
