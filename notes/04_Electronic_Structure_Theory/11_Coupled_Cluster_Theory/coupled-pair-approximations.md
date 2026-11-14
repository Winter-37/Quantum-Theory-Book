---
id: coupled-pair-approximations
title: Coupled-pair approximations - DCI, linear CCA (L-CCD), CEPA and CCA as truncations of full CI
summary: The full CI hierarchy links the doubles to the quadruples. Setting the quadruples to zero gives DCI; approximating them by products of doubles gives CCA (CCD); dropping the product term after the energy cancellation gives linear CCA (= L-CCD = D-MBPT(∞)); keeping only its same-pair part gives CEPA. All four share one doubles equation with a different term X on the right. Size consistency, invariance and computed results for the H2 dimer and water.
status: in-progress
kind: comparison
level: intermediate
tags: [cepa, l-ccd, linear-cca, d-mbpt, dci, ccd, coupled-pair, size-consistency, invariance]
prerequisites: [iepa, cisd, size-consistency]
related: [coupled-cluster-doubles, mp3, linked-cluster-theorem, one-particle-hamiltonian-models, coupled-cluster-second-quantization]
order: 20
date: 2026-11-03
---

## The full CI hierarchy

Ignore singles, triples and other odd excitations for simplicity. Inserting the intermediate-normalized full CI wave function

$$
|\Phi_0\rangle = |\Psi_0\rangle + \sum_{\substack{a<b\\ r<s}} c_{ab}^{rs}|\Psi_{ab}^{rs}\rangle + \sum_{\substack{a<b<c<d\\ r<s<t<u}} c_{abcd}^{rstu}|\Psi_{abcd}^{rstu}\rangle + \cdots
$$

into $(H - E_0)|\Phi_0\rangle = E_{\text{corr}}|\Phi_0\rangle$ and projecting on $\langle\Psi_0|$ and $\langle\Psi_{ab}^{rs}|$ gives

$$
\sum_{c<d,\,t<u}\langle\Psi_0|H|\Psi_{cd}^{tu}\rangle\,c_{cd}^{tu} = E_{\text{corr}},
$$

$$
\langle\Psi_{ab}^{rs}|H|\Psi_0\rangle + \sum_{c<d,\,t<u}\langle\Psi_{ab}^{rs}|H - E_0|\Psi_{cd}^{tu}\rangle\,c_{cd}^{tu} + \sum_{c<d,\,t<u}\langle\Psi_0|H|\Psi_{cd}^{tu}\rangle\,c_{abcd}^{rstu} = E_{\text{corr}}\,c_{ab}^{rs}.
$$

The doubles equation contains the quadruples, the quadruples equation contains the hextuples, and so on. A pair theory is a recipe for closing this hierarchy. The doubles-quadruples matrix element $\langle\Psi_{ab}^{rs}|H|\Psi_{abcd}^{rstu}\rangle$ has been replaced by $\langle\Psi_0|H|\Psi_{cd}^{tu}\rangle$, because the two determinants differ only in $cd\to tu$.

**Closure 1: DCI.** Set $c_{abcd}^{rstu} = 0$. The result is exactly the DCI eigenvalue problem ([[cisd]]). It is variational and not size consistent ([[size-consistency]]).

## Closure 2: quadruples as products of doubles (CCA)

**Motivation.** For two infinitely separated H$_2$ molecules the exact quadruple coefficient is the product of the doubles coefficients ([[size-consistency]]). For a real system pairs are not independent, but IEPA works reasonably ([[iepa]]), which suggests approximating every quadruple coefficient by products of doubles.

**Sign bookkeeping.** The same quadruple $abcd\to rstu$ can be built from two disjoint double excitations in 18 distinct ways (which hole pairs and which particle pairs are combined). Each product carries the sign of the permutation that brings the determinant to the standard order. Szabo writes the sum as

$$
c_{abcd}^{rstu} \approx c_{ab}^{rs}*c_{cd}^{tu}
= c_{ab}^{rs}c_{cd}^{tu} - c_{ac}^{rs}c_{bd}^{tu} + c_{ad}^{rs}c_{bc}^{tu} - \cdots \quad(18\text{ terms}).
$$

**The cancellation.** Insert this into the doubles equation and use the energy equation for $E_{\text{corr}}$. The right-hand side $E_{\text{corr}}c_{ab}^{rs}$ contains the products $c_{ab}^{rs}c_{cd}^{tu}\langle\Psi_0|H|\Psi_{cd}^{tu}\rangle$. These cancel exactly against the first term of $c_{ab}^{rs}*c_{cd}^{tu}$ on the left. What remains is

$$
\langle\Psi_{ab}^{rs}|H|\Psi_0\rangle + \sum_{c<d,\,t<u}\langle\Psi_{ab}^{rs}|H - E_0|\Psi_{cd}^{tu}\rangle c_{cd}^{tu}
= \sum_{c<d,\,t<u}\langle\Psi_0|H|\Psi_{cd}^{tu}\rangle\,\big\langle c_{ab}^{rs}*c_{cd}^{tu}\big\rangle ,
$$

where $\langle c_{ab}^{rs}*c_{cd}^{tu}\rangle = c_{ab}^{rs}c_{cd}^{tu} - c_{ab}^{rs}*c_{cd}^{tu}$ collects the 17 remaining products.

**Properties.**

- The equation does not contain $E_{\text{corr}}$ and is quadratic in the amplitudes. It cannot be solved by diagonalization; it is solved iteratively.
- This is coupled-pair many-electron theory (CPMET) of Čížek and Paldus, also called the coupled-cluster approximation (CCA). With doubles only it is CCD ([[coupled-cluster-doubles]]).
- CCA couples different pairs like DCI, is size consistent like IEPA, and is invariant to rotations of degenerate orbitals. It is not variational.

## Closure 3: linear CCA

**Definition.** Drop the product term $\langle c*c\rangle$ **after** the cancellation:

$$
\langle\Psi_{ab}^{rs}|H|\Psi_0\rangle + \sum_{c<d,\,t<u}\langle\Psi_{ab}^{rs}|H - E_0|\Psi_{cd}^{tu}\rangle c_{cd}^{tu} = 0,
\qquad E_{\text{corr}} = \mathbf b^\dagger\mathbf c .
$$

With $(\mathbf b)_{rs,ab} = \langle\Psi_{ab}^{rs}|H|\Psi_0\rangle$ and $(\mathbf D)_{rsab,tucd} = \langle\Psi_{ab}^{rs}|H - E_0|\Psi_{cd}^{tu}\rangle$,

$$
E_{\text{corr}}(\text{L-CCA}) = -\mathbf b^\dagger\mathbf D^{-1}\mathbf b,
\qquad
E_{\text{corr}}(\text{DCI}) = -\mathbf b^\dagger(\mathbf D - E_{\text{corr}}\mathbf 1)^{-1}\mathbf b .
$$

**Not an approximation to DCI.** The two formulas look alike: L-CCA is DCI with $E_{\text{corr}}$ set to zero in the denominator. But dropping the products *before* the cancellation would have given DCI. The term $-E_{\text{corr}}c_{ab}^{rs}$ in DCI is exactly the unlinked piece that destroys size consistency, so L-CCA is size consistent and DCI is not.

**Other names.** L-CCA is the same as linearized CCD (L-CCD), and the same as the doubles-only infinite-order many-body perturbation theory D-MBPT(∞) of Bartlett and coworkers, obtained by summing all doubles diagrams ([[linked-cluster-theorem]]). It is exact through third order ([[mp3]]). Replacing $\mathbf D$ by its diagonal gives Epstein-Nesbet pairs (Szabo Ex. 5.12a). L-CCA is invariant to unitary transformations of degenerate orbitals (Ex. 5.12b).

## Closure 4: CEPA

**Definition (Meyer).** In the product term keep only $cd = ab$. Since amplitudes are antisymmetric, $\langle c_{ab}^{rs}*c_{ab}^{tu}\rangle = c_{ab}^{rs}c_{ab}^{tu}$ and the right-hand side becomes $c_{ab}^{rs}\sum_{t<u}\langle\Psi_0|H|\Psi_{ab}^{tu}\rangle c_{ab}^{tu} = e_{ab}\,c_{ab}^{rs}$:

$$
\langle\Psi_{ab}^{rs}|H|\Psi_0\rangle + \sum_{c<d,\,t<u}\langle\Psi_{ab}^{rs}|H - E_0|\Psi_{cd}^{tu}\rangle c_{cd}^{tu} = e_{ab}\,c_{ab}^{rs},
\qquad E_{\text{corr}} = \sum_{a<b} e_{ab}.
$$

**Relation to IEPA and DCI.** Replacing $e_{ab}$ by $E_{\text{corr}}$ gives DCI. Restricting the sum to $cd = ab$ gives IEPA. CEPA couples pairs and stays size consistent, and is computationally as simple as DCI. It is not exactly invariant, but much closer to invariant than IEPA.

**Caution on the name.** Several CEPA variants exist in the literature, differing in which pair energies are subtracted. Szabo's form, with the pair's own energy $e_{ab}$, is the one usually labelled CEPA(2) (general knowledge, not from Szabo).

## One equation, four methods

All four theories share

$$
E_{\text{corr}} = \sum_{a<b} e_{ab}, \qquad e_{ab} = \sum_{r<s}\langle\Psi_0|H|\Psi_{ab}^{rs}\rangle c_{ab}^{rs},
$$

$$
\langle\Psi_{ab}^{rs}|H|\Psi_0\rangle + \sum_{c<d,\,t<u}\langle\Psi_{ab}^{rs}|H - E_0|\Psi_{cd}^{tu}\rangle c_{cd}^{tu} = X ,
$$

and differ only in $X$ (Szabo Table 5.2):

| Method | $X$ | Variational | Size consistent | Invariant |
|---|---|---|---|---|
| DCI | $E_{\text{corr}}\,c_{ab}^{rs}$ | yes | no | yes |
| L-CCA (L-CCD) | $0$ | no | yes | yes |
| CEPA | $e_{ab}\,c_{ab}^{rs}$ | no | yes | nearly |
| CCA (CCD) | $\sum_{c<d,t<u}\langle\Psi_0|H|\Psi_{cd}^{tu}\rangle\langle c_{ab}^{rs}*c_{cd}^{tu}\rangle$ | no | yes | yes |

The last three columns are from Szabo's discussion; IEPA (not in the table) is size consistent and not invariant. That one method follows from another by setting something to zero says nothing about which is more accurate.

## H₂ dimer: CEPA in delocalized orbitals

**Analytic result (Szabo Eqs. 5.69-5.71).** In delocalized orbitals the dimer DCI matrix of Ex. 5.7 has four equal pair energies $e$. Replacing $E_{\text{corr}}$ by $e$ gives $e^2 - 2\Delta e - K_{12}^2/2 = 0$ and

$$
{}^2E_{\text{corr}}(\text{CEPA, delocalized}) = 4\Big(\Delta - \big(\Delta^2 + K_{12}^2/2\big)^{1/2}\Big),
$$

against the exact $2\big(\Delta - (\Delta^2 + K_{12}^2)^{1/2}\big)$. In localized orbitals there is no coupling between pairs, so CEPA = IEPA = exact.

!!! example "H₂ dimer, STO-3G, R = 1.4 bohr, 100 bohr apart"
    Correlation energies in hartree, computed for this note; the exact value is −0.041124.

    | Method | Localized | Delocalized |
    |---|---:|---:|
    | DCI | −0.04061 | −0.04061 |
    | L-CCD | −0.04166 | −0.04166 |
    | CEPA | −0.04112 | −0.04139 |
    | CCD | −0.04112 | −0.04112 |
    | IEPA | −0.04112 | −0.02763 |

    - **CEPA** changes by only 0.27 mHa between bases (Szabo: −0.0414 delocalized). The analytic formula above with $\Delta = 0.788645$, $K_{12} = 0.181258$ gives −0.041389, matching the iterative code.
    - **CCD** is exact and basis independent.
    - **L-CCD** is basis independent but overshoots; for the dimer it equals the localized Epstein-Nesbet value $-K_{12}^2/\Delta$.
    - **DCI** is invariant but not size consistent.

## Water: all methods in one basis

!!! example "H₂O at R = 1.809 bohr, 104.52°, all electrons correlated (computed for this note)"
    $E_{\text{HF}} = -74.962940$ (STO-3G) and $-75.983996$ hartree (6-31G). Correlation energies in hartree; percent of full CI in parentheses. CISD and CCSD include singles and are given for reference.

    | Method | STO-3G | 6-31G |
    |---|---:|---:|
    | MP2 | −0.035499 (71.7) | −0.128803 (94.1) |
    | MP2 + MP3 | −0.045091 (91.1) | −0.130383 (95.3) |
    | DCI | −0.048541 (98.1) | −0.129413 (94.6) |
    | CISD | −0.048783 (98.6) | −0.130068 (95.0) |
    | L-CCD | −0.049811 (100.7) | −0.134824 (98.5) |
    | CEPA | −0.049607 (100.2) | −0.134456 (98.3) |
    | CCD | −0.049122 (99.3) | −0.134648 (98.4) |
    | CCSD | −0.049369 (99.8) | −0.135330 (98.9) |
    | IEPA | −0.051191 (103.4) | −0.174935 (127.8) |
    | Epstein-Nesbet | −0.053812 (108.7) | −0.170842 (124.8) |
    | Full CI | −0.049486 | −0.136848 |

    **Pattern.** The three coupled-pair methods agree to within 0.4 mHa in 6-31G and recover about 98.4% of full CI. DCI recovers 94.6%. The uncoupled pair theories (IEPA, EN) overshoot badly once the basis has more than a minimal virtual space.

**Szabo's large-basis results (Tables 5.3-5.4, H₂O, 39-STO basis; literature values checked against the page images).** SDCI −0.2756, L-CCA −0.2908, CCA −0.2862 against estimated full CI −0.296 hartree. Equilibrium bond length (bohr) and angle: SCF 1.776, 106.1°; SDCI 1.800, 104.9°; L-CCA 1.810, 104.6°; CCA 1.806, 104.7°; experiment 1.809, 104.5°. L-CCA is closer to experiment than CCA here; Szabo warns that this may reflect cancellation with the missing singles and triples rather than a better theory.

## Code

The residual for all four methods. `R_lin(t)` is the left-hand side of the common equation, divided by nothing; the update is `t_new = R/D` with $D = \varepsilon_i + \varepsilon_j - \varepsilon_a - \varepsilon_b$, because `R_lin` contains the diagonal Fock part only through `D`. For CCD the quadratic terms are built with the usual intermediates (see [[coupled-cluster-doubles]]).

```python
def residual(d, t, kind):
    if kind == "DCI":  return d.R_lin(t) - d.E(t) * t                      # X = E_corr c
    if kind == "LCCD": return d.R_lin(t)                                   # X = 0
    if kind == "CEPA": return d.R_lin(t) - d.pair_e(t)[:, :, None, None] * t   # X = e_ab c
    if kind == "CCD":  return d.R_ccd(t)                                   # X = product terms
# R_lin(t) = <ij||ab> + 1/2 <ab||cd> t_ij^cd + 1/2 <kl||ij> t_kl^ab + P(ij)P(ab) <kb||cj> t_ik^ac
```

## Source

Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996; reprint of the revised first edition, McGraw-Hill, 1989), Sec. 5.2, pp. 286-297, Eqs. (5.47)-(5.71), Table 5.2 (p. 295), Tables 5.3-5.4 (pp. 296-297), Ex. 5.12. All tables except the 39-STO literature values computed for this note with PySCF 2.14; CCD checked against PySCF's CCD (−0.049122 for STO-3G water).
