---
id: mp3
title: Third-order Møller-Plesset energy (MP3) and the convergence of the MP series
summary: The third-order energy has three terms (particle-particle ladder, hole-hole ladder and ring) built entirely from first-order doubles amplitudes. The H2 minimal-basis result K12²(J11+J22−4J12+2K12)/4(ε1−ε2)², an order-by-order check against an exact RS recursion for water through seventh order, the identity between MP2+MP3 and the second iteration of linear coupled cluster, and Szabo's large-basis water results.
status: in-progress
kind: derivation
level: intermediate
tags: [mp3, moller-plesset, mbpt, third-order, ladder-diagrams, ring-diagrams, convergence]
prerequisites: [mp2, rayleigh-schrodinger-perturbation-theory]
related: [linked-cluster-theorem, coupled-pair-approximations, coupled-cluster-second-quantization, ionization-potentials-second-order-self-energy]
order: 20
date: 2026-11-03
---

## The formula

**General RS third order** ([[rayleigh-schrodinger-perturbation-theory]]): $E^{(3)} = \sum_{nm}{}'V_{0n}V_{nm}V_{m0}/(\Delta_n\Delta_m) - V_{00}\sum_n{}'|V_{0n}|^2/\Delta_n^2$, with $\Delta_n = E_0^{(0)} - E_n^{(0)}$. With the Møller-Plesset partition ([[mp2]]) only doubles appear as intermediate states, and after a lengthy evaluation of $\langle\Psi_{ab}^{rs}|\mathscr V|\Psi_{cd}^{tu}\rangle$ the renormalization term cancels. Szabo's result (Eq. 6.75), in spin orbitals:

$$
\begin{aligned}
E_0^{(3)} ={}& \frac18\sum_{abcdrs}\frac{\langle ab||rs\rangle\langle cd||ab\rangle\langle rs||cd\rangle}{(\varepsilon_a + \varepsilon_b - \varepsilon_r - \varepsilon_s)(\varepsilon_c + \varepsilon_d - \varepsilon_r - \varepsilon_s)}\\
&+ \frac18\sum_{abrstu}\frac{\langle ab||rs\rangle\langle rs||tu\rangle\langle tu||ab\rangle}{(\varepsilon_a + \varepsilon_b - \varepsilon_r - \varepsilon_s)(\varepsilon_a + \varepsilon_b - \varepsilon_t - \varepsilon_u)}\\
&+ \sum_{abcrst}\frac{\langle ab||rs\rangle\langle cs||tb\rangle\langle rt||ac\rangle}{(\varepsilon_a + \varepsilon_b - \varepsilon_r - \varepsilon_s)(\varepsilon_a + \varepsilon_c - \varepsilon_r - \varepsilon_t)} .
\end{aligned}
$$

**Reading the terms.** With $t_{ab}^{rs} = \langle rs||ab\rangle/(\varepsilon_a + \varepsilon_b - \varepsilon_r - \varepsilon_s)$, the first-order amplitudes,

- **hole-hole ladder:** $\tfrac18\sum t_{ab}^{rs}\langle cd||ab\rangle t_{cd}^{rs}$ (two holes scatter),
- **particle-particle ladder:** $\tfrac18\sum t_{ab}^{rs}\langle rs||tu\rangle t_{ab}^{tu}$ (two particles scatter),
- **ring:** the particle-hole term, with the sign fixed by the Goldstone rules ([[linked-cluster-theorem]]).

$E^{(3)}$ needs only first-order amplitudes, as the $(2n+1)$ rule promises: $E^{(3)} = \langle\Psi^{(1)}|\mathscr V - E^{(1)}|\Psi^{(1)}\rangle$. Its cost is dominated by the particle-particle ladder, $o^2v^4$, one power more than MP2's $o^2v^3$ integral transformation.

```python
# spin-orbital MP3, A = <pq||rs> with occupied first; t1 = first-order amplitudes t_ij^ab
t1 = A[o, o, v, v] / D                      # D = e_i + e_j - e_a - e_b
e3 = (0.125 * np.einsum("ijab,abcd,ijcd", t1, A[v, v, v, v], t1)
      + 0.125 * np.einsum("ijab,klij,klab", t1, A[o, o, o, o], t1)
      + np.einsum("ijab,kbcj,ikac", t1, A[o, v, v, o], t1))
```

## Minimal-basis H₂

**Expansion of the exact result.** Expanding $E_{\text{corr}} = \Delta - (\Delta^2 + K_{12}^2)^{1/2}$ in powers of the two-electron integrals (Szabo Ex. 6.9), with $2\Delta = 2(\varepsilon_2 - \varepsilon_1) + J_{11} + J_{22} - 4J_{12} + 2K_{12}$ and orbital energies regarded as zeroth order:

$$
E_0^{(2)} = \frac{K_{12}^2}{2(\varepsilon_1 - \varepsilon_2)},
\qquad
E_0^{(3)} = \frac{K_{12}^2\,(J_{11} + J_{22} - 4J_{12} + 2K_{12})}{4(\varepsilon_1 - \varepsilon_2)^2}.
$$

The general formula above reduces to the same result (Szabo shows this with Goldstone diagrams in Sec. 6.7.2).

**Numbers (STO-3G, R = 1.4 bohr, computed for this note).** $E^{(2)} = -0.013158$, $E^{(3)} = -0.004846$, sum $-0.018004$ hartree, against exact $-0.020562$. Third order is still large (37% of second order) in this basis.

## Order-by-order check for water

The spin-orbital formula was checked against an exact RS recursion in the full determinant space, with $\mathscr H_0$ the diagonal sum of orbital energies.

!!! example "H₂O, STO-3G, R = 1.809 bohr, 104.52° (computed for this note)"
    Full CI correlation energy −0.049486 hartree.

    | $n$ | $E^{(n)}$ | Sum through $n$ | % of full CI |
    |---:|---:|---:|---:|
    | 2 | −0.03549931 | −0.035499 | 71.7 |
    | 3 | −0.00959219 | −0.045091 | 91.1 |
    | 4 | −0.00290737 | −0.047999 | 97.0 |
    | 5 | −0.00095439 | −0.048953 | 98.9 |
    | 6 | −0.00033449 | −0.049288 | 99.6 |
    | 7 | −0.00012285 | −0.049410 | 99.8 |

    - **Formula check.** The three-term $E^{(3)}$ above gives −0.00959219, identical to the recursion.
    - **Recursion check.** $E^{(0)} + E^{(1)}$ plus the nuclear repulsion reproduces the SCF energy, as it must.
    - **Convergence.** Monotonic and roughly geometric, with successive ratios 0.27, 0.30, 0.33, 0.35, 0.37. This is a well-behaved closed shell near equilibrium; MP series can converge slowly, oscillate, or diverge for stretched bonds and diffuse basis sets (general knowledge, not from Szabo).

## MP3 is what linear coupled cluster gets right

**Second iteration.** Iterating the doubles amplitude equations from $t = 0$: the first iteration gives the MP2 amplitudes and energy. A second iteration with only the **linear** terms gives an energy that equals $E^{(2)} + E^{(3)}$ exactly. For STO-3G water, −0.0450914856 in both cases (computed for this note; see [[coupled-cluster-second-quantization]]).

**Consequence.** L-CCD (D-MBPT(∞)), CEPA and CCD are all exact through third order ([[coupled-pair-approximations]]). They first differ from full MBPT at fourth order, where singles, triples and quadruples enter.

**Szabo's large-basis water (39-STO basis; literature values, Table 6.8, checked against the page image).** $E^{(2)} = -0.2818$, $E^{(2)} + E^{(3)} = -0.2850$, $E^{(2)} + E^{(3)} + E^{(4)} = -0.2960$ against the estimated full CI $-0.296\pm0.001$ hartree. Third order adds only 1% here; fourth order (with singles, triples and quadruples) adds another 3.7%. For the geometry the series oscillates (see [[mp2]]).

## Source

Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996; reprint of the revised first edition, McGraw-Hill, 1989), Sec. 6.5, pp. 353-354, Eqs. (6.75)-(6.78), Ex. 6.9; Sec. 6.7.2 (Goldstone evaluation of $E^{(3)}$), pp. 362-368; Table 6.8, p. 373. Water numbers computed for this note with PySCF 2.14 integrals and a determinant-space recursion.
