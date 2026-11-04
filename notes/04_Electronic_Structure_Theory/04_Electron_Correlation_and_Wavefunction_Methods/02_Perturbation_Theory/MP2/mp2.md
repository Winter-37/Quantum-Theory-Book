---
id: mp2
title: Møller-Plesset partitioning and the second-order energy (MP2)
summary: With the Hartree-Fock Hamiltonian as H0, E(0)+E(1) is the Hartree-Fock energy and correlation starts at second order. E(2) in spin-orbital, physicists'-integral and closed-shell spatial forms; its identity with first-order pairs; the minimal-basis H2 result K12²/2(ε1−ε2); computed basis-set and bond-length trends for H2 reproducing Szabo Tables 6.3-6.4; why RHF-based MP2 diverges when H2 dissociates while UHF-based MP2 does not; and Szabo's literature results for geometries and dipole moments.
status: in-progress
kind: derivation
level: intermediate
tags: [mp2, moller-plesset, mbpt, perturbation-theory, correlation-energy, dissociation, finite-field]
prerequisites: [rayleigh-schrodinger-perturbation-theory, brillouin-theorem, integral-notation]
related: [standard-models-h2-and-water, perturbation-theory-second-quantization, mp3, iepa, linked-cluster-theorem, h2-dissociation-rhf-uhf, minimal-basis-h2-model, spin-orbital-to-spatial-orbital, ionization-potentials-second-order-self-energy]
also: [04_Electronic_Structure_Theory/15_Benchmarking_and_Validation/05_Basis_Set_Effects]
date: 2026-11-03
---

## The Møller-Plesset partition

**Zeroth-order Hamiltonian.** The sum of Fock operators ([[brillouin-theorem]]):

$$
\mathscr H_0 = \sum_i f(i) = \sum_i\big[h(i) + v^{\text{HF}}(i)\big],
\qquad
\mathscr V = \sum_{i<j}r_{ij}^{-1} - \sum_i v^{\text{HF}}(i).
$$

$\mathscr V$ is the **fluctuation potential**: the true electron repulsion minus its Hartree-Fock average. RS perturbation theory ([[rayleigh-schrodinger-perturbation-theory]]) with this partition is Møller-Plesset perturbation theory (MPPT), also called many-body perturbation theory (MBPT).

**Notation.** Physicists' integrals $\langle ij|kl\rangle = \int\chi_i^*(1)\chi_j^*(2)r_{12}^{-1}\chi_k(1)\chi_l(2)$ and $\langle ij||kl\rangle = \langle ij|kl\rangle - \langle ij|lk\rangle$ ([[integral-notation]]). In this notation $v^{\text{HF}}_{ij} = \sum_b\langle ib||jb\rangle$.

**Zeroth and first order.** Every determinant built from Hartree-Fock spin orbitals is an eigenfunction of $\mathscr H_0$ with eigenvalue equal to the sum of its occupied orbital energies. Hence

$$
E_0^{(0)} = \sum_a\varepsilon_a,
\qquad
E_0^{(1)} = \langle\Psi_0|\mathscr V|\Psi_0\rangle = \tfrac12\sum_{ab}\langle ab||ab\rangle - \sum_{ab}\langle ab||ab\rangle = -\tfrac12\sum_{ab}\langle ab||ab\rangle,
$$

so $E_0^{(0)} + E_0^{(1)} = E_{\text{HF}}$. The first correction to Hartree-Fock is second order.

## Second order

**Which states contribute.** In $E_0^{(2)} = \sum_n{}'|\langle\Psi_0|\mathscr V|n\rangle|^2/(E_0^{(0)} - E_n^{(0)})$:

- **Singles** give $\langle\Psi_a^r|\mathscr V|\Psi_0\rangle = \langle\Psi_a^r|\mathscr H|\Psi_0\rangle - \langle\Psi_a^r|\mathscr H_0|\Psi_0\rangle = f_{ra} - 0 = 0$, by Brillouin's theorem and because $\Psi_0$ is an eigenfunction of $\mathscr H_0$.
- **Triples and higher** do not couple through a two-body operator.
- **Doubles** give $\langle\Psi_{ab}^{rs}|\mathscr V|\Psi_0\rangle = \langle rs||ab\rangle$ and $E_0^{(0)} - E^{(0)}_{ab,rs} = \varepsilon_a + \varepsilon_b - \varepsilon_r - \varepsilon_s$.

**Spin-orbital forms.**

$$
E_0^{(2)} = \sum_{a<b}\sum_{r<s}\frac{|\langle ab||rs\rangle|^2}{\varepsilon_a + \varepsilon_b - \varepsilon_r - \varepsilon_s}
= \frac14\sum_{abrs}\frac{|\langle ab||rs\rangle|^2}{\varepsilon_a + \varepsilon_b - \varepsilon_r - \varepsilon_s}
= \frac12\sum_{abrs}\frac{\langle ab|rs\rangle\langle rs|ab\rangle}{\varepsilon_a + \varepsilon_b - \varepsilon_r - \varepsilon_s} - \frac12\sum_{abrs}\frac{\langle ab|rs\rangle\langle rs|ba\rangle}{\varepsilon_a + \varepsilon_b - \varepsilon_r - \varepsilon_s}.
$$

The second form uses the antisymmetry of $\langle ab||rs\rangle$ in $ab$ and in $rs$, and the fact that terms with $a=b$ or $r=s$ vanish.

**Closed shell.** Summing over spin ([[spin-orbital-to-spatial-orbital]]), with $a,b$ now doubly occupied spatial orbitals and $r,s$ virtual spatial orbitals:

$$
E_0^{(2)} = 2\sum_{abrs}^{N/2}\frac{\langle ab|rs\rangle\langle rs|ab\rangle}{\varepsilon_a + \varepsilon_b - \varepsilon_r - \varepsilon_s} - \sum_{abrs}^{N/2}\frac{\langle ab|rs\rangle\langle rs|ba\rangle}{\varepsilon_a + \varepsilon_b - \varepsilon_r - \varepsilon_s}.
$$

The first term is the opposite-spin plus same-spin "direct" part, the second the same-spin exchange part.

**Pair form.** $E_0^{(2)} = \sum_{a<b}e_{ab}^{(1)}$, where $e_{ab}^{(1)}$ are the first-order pair energies of [[iepa]]. MP2 is the simplest pair theory.

**Wave function.** The first-order wave function is $|\Psi_0^{(1)}\rangle = \sum_{a<b,r<s}t_{ab}^{rs}|\Psi_{ab}^{rs}\rangle$ with $t_{ab}^{rs} = \langle rs||ab\rangle/(\varepsilon_a + \varepsilon_b - \varepsilon_r - \varepsilon_s)$. These are exactly the first-iteration coupled-cluster amplitudes ([[coupled-cluster-second-quantization]]).

```python
# closed-shell MP2 from MO-basis chemists' integrals g[p,q,r,s] = (pq|rs) = <pr|qs>
o, v = slice(0, nocc), slice(nocc, None)
ovov = g[o, v, o, v]                                      # (ar|bs) = <ab|rs>
D = e[o, None, None, None] - e[None, v, None, None] + e[None, None, o, None] - e[None, None, None, v]
e2 = np.sum(ovov * (2 * ovov - ovov.transpose(0, 3, 2, 1)) / D)
```

## Minimal-basis H₂

**Exact correlation energy** ([[full-ci]]): $E_{\text{corr}} = \Delta - (\Delta^2 + K_{12}^2)^{1/2}$ with $2\Delta = 2(\varepsilon_2 - \varepsilon_1) + J_{11} + J_{22} - 4J_{12} + 2K_{12}$.

**Perturbation theory.** With $a = b = 1$, $r = s = 2$ and $\langle11|22\rangle = K_{12}$, the closed-shell formula gives

$$
E_0^{(2)} = \frac{2K_{12}^2 - K_{12}^2}{2(\varepsilon_1 - \varepsilon_2)} = \frac{K_{12}^2}{2(\varepsilon_1 - \varepsilon_2)} .
$$

Expanding the exact result in powers of the two-electron integrals reproduces this and also gives the third-order term of [[mp3]].

**Numbers (STO-3G, R = 1.4 bohr, computed for this note).** $E^{(2)} = -0.013158$ hartree, 64% of the exact −0.020562.

## Basis-set dependence

!!! example "H₂ at R = 1.4 bohr (reproducing Szabo Table 6.3; computed for this note)"
    Correlation energies in hartree; percent of full CI in the same basis.

    | Basis | $E^{(2)}$ | $E^{(2)} + E^{(3)}$ | Full CI |
    |---|---:|---:|---:|
    | STO-3G | −0.0132 (64%) | −0.0180 (88%) | −0.0206 |
    | 4-31G | −0.0174 (70%) | −0.0226 (91%) | −0.0249 |
    | 6-31G** | −0.0263 (78%) | −0.0319 (94%) | −0.0339 |
    | cc-pVTZ | −0.0317 (80%) | −0.0373 (95%) | −0.0394 |

    - **Agreement with Szabo.** The first three rows match his table; Szabo lists 87% for STO-3G $E^{(2)}+E^{(3)}$, and −0.0180/−0.0206 = 87.6%. For H, 4-31G and 6-31G are the same basis.
    - **Last row.** Szabo's large basis is a (10s,5p,1d) set from the literature (−0.0321, 81%; −0.0376, 95%; full CI −0.0397). cc-pVTZ is used here instead and behaves the same way. The exact nonrelativistic value is −0.0409.
    - **Trend.** The fraction recovered at second order grows with the basis. Judging MP2 from minimal-basis numbers underrates it.

!!! example "H₂ equilibrium bond length in bohr (reproducing Szabo Table 6.4; computed for this note)"
    | Basis | SCF | MP2 | Full CI |
    |---|---:|---:|---:|
    | STO-3G | 1.346 | 1.368 | 1.389 |
    | 4-31G | 1.379 | 1.394 | 1.410 |
    | 6-31G** | 1.384 | 1.387 | 1.395 |

    Szabo: 1.346/1.368/1.389, 1.380/1.394/1.410, 1.385/1.387/1.396. The 0.001-bohr differences are at the level of rounding and integral accuracy. Exact: 1.401. Correlation lengthens the bond; MP2 moves the SCF value in the right direction but by too little in the polarized basis.

**Other molecules (Szabo Tables 6.5-6.10; literature values, checked against the page images).**

- **X-H bonds (CH₄, NH₃, H₂O, HF).** At 6-31G** the largest SCF bond-length error is 0.03 bohr, and MP2 reduces every error below 0.01 bohr. MP2 roughly halves the SCF error in the bond angles of NH₃ and H₂O.
- **Multiple bonds.** For N₂ and CO (6-31G*), SCF is about 0.03 bohr too short and MP2 overcorrects (N₂: SCF 2.039, MP2 2.133, MP2+MP3 2.109, experiment 2.074). The third-order term partly undoes the overshoot.
- **H₂O near-HF-limit basis (39-STO).** MP2 gives R = 1.811 bohr and 104.4° against experiment 1.809 and 104.5°; adding third order makes the geometry worse (1.803), adding fourth order better again (1.813). The correlation energy itself converges monotonically: −0.2818, −0.2850, −0.2960 (estimated full CI −0.296).
- **Dipole moments by finite field.** Solve Hartree-Fock in a small field $\mathbf F$, add $E^{(2)}$ with the field-dependent orbitals, and differentiate: $\mu_i = -\partial E/\partial F_i$. Correlation changes the dipole moments of NH₃, H₂O and HF in the right direction but cannot repair basis-set deficiencies (Table 6.10).

## Dissociation: RHF-MP2 diverges, UHF-MP2 does not

**Why RHF-MP2 fails.** As $R\to\infty$ in minimal-basis H$_2$, every two-electron integral tends to $\tfrac12(\phi\phi|\phi\phi)$ and $\varepsilon_1 = h_{11} + J_{11}$, $\varepsilon_2 = h_{22} + 2J_{12} - K_{12}$ approach the same limit. So $\varepsilon_2 - \varepsilon_1\to0$ while $K_{12}$ stays finite, and $E^{(2)} = K_{12}^2/2(\varepsilon_1 - \varepsilon_2)\to-\infty$. Perturbation theory on a qualitatively wrong reference makes things worse, not better ([[h2-dissociation-rhf-uhf]]).

**UHF reference.** Use unrestricted spin orbitals and orbital energies in the spin-orbital formulas. The UHF determinant dissociates correctly, and the perturbation series stays finite.

!!! example "H₂, STO-3G, total energies in hartree (computed for this note)"
    | R (bohr) | RHF | RMP2 | UHF | UMP2 | Full CI | $\varepsilon_2 - \varepsilon_1$ |
    |---:|---:|---:|---:|---:|---:|---:|
    | 1.4 | −1.116714 | −1.129872 | = RHF | = RMP2 | −1.137276 | 1.2485 |
    | 2.0 | −1.049171 | −1.071827 | = RHF | = RMP2 | −1.088496 | 0.8874 |
    | 3.0 | −0.885275 | −0.936859 | −0.951018 | −0.952630 | −0.985157 | 0.5358 |
    | 4.0 | −0.761082 | −0.862710 | −0.935842 | −0.935889 | −0.943778 | 0.3458 |
    | 6.0 | −0.645077 | −0.898081 | −0.933227 | −0.933227 | −0.933402 | 0.1827 |
    | 10 | −0.595971 | −1.164213 | −0.933164 | −0.933164 | −0.933164 | 0.1001 |

    - **RMP2** turns over and plunges as the gap $\varepsilon_2 - \varepsilon_1$ (RHF orbital energies) closes: at 10 bohr it is 0.23 hartree *below* the exact energy.
    - **UMP2** is correct at both ends but recovers almost nothing at intermediate R (at 4 bohr, 0.05 mHa of the 7.9 mHa UHF-to-FCI gap). Szabo's point: the UHF function $|\phi_1\bar\phi_2|$ has the wrong form; the exact singlet is $2^{-1/2}(|\phi_1\bar\phi_2| + |\phi_2\bar\phi_1|)$. Fixing the long-range region needs a multiconfigurational zeroth order.
    - **The UHF solution** appears at R ≈ 2.18 bohr in this basis ([[scf-second-order-and-stability]]).

## Source

Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996; reprint of the revised first edition, McGraw-Hill, 1989), Sec. 6.5, pp. 350-354, Eqs. (6.58)-(6.77), Ex. 6.8-6.9; Sec. 6.8, pp. 370-378, Tables 6.3-6.10, Eqs. (6.96)-(6.101), Figs. 6.2-6.3. Tables marked "computed" were computed for this note with PySCF 2.14; the others quote Szabo's literature values.
