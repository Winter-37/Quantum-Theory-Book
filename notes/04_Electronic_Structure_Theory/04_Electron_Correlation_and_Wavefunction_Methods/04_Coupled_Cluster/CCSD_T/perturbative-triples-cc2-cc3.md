---
id: perturbative-triples-cc2-cc3
title: Perturbation analysis of the coupled-cluster hierarchy and the hybrid models CC2, CC3 and CCSD(T) (HJO 14.6)
summary: Counting orders in the fluctuation potential, a CC model truncated at excitation level N has a wave function correct to order N − 1 and an energy correct to order ⌊3N/2⌋. So CCSD is correct to third order and CCSDT to fourth. Hybrid models keep only the lowest-order terms of the next level. CC2 approximates the doubles (n⁵, iterative, energy correct to second order) and CC3 approximates the triples (n⁷ iterative, fourth order). CCSD(T) adds noniteratively the fourth-order triples energy plus a fifth-order singles-triples term, built from CCSD amplitudes with closed-shell bra amplitudes 2t_i^a and 4t_ij^ab − 2t_ij^ba. Recomputed for water/cc-pVDZ against HJO's FCI: MP2, CC2, MP3, CCSD, MP4, CCSD(T) and CCSDT errors (HJO Fig. 14.10; CC3 is not available in PySCF). Added from Crawford's ESQC 2026 lectures: the spin-orbital (T)/[T] working equations with batched triples, CCSD+T(4) versus CCSD[T] versus CCSD(T), the CCSDT-n/CC3/CCSDR(3) family, and a water/6-31G benchmark against FCI. At the 2R_e geometry, [T] overshoots by −6.3 mE_h and the positive E_ST pulls (T) back to −4.8.
status: in-progress
kind: comparison
level: advanced
tags: [ccsd-t, cc2, cc3, perturbative-triples, coupled-cluster, moller-plesset, order-analysis, water]
prerequisites: [moller-plesset-and-coupled-cluster-perturbation-theory, coupled-cluster-hierarchy-and-size-extensivity]
related: [ccsd-spin-orbital-equations, coupled-cluster-diagrams, closed-shell-ccsd-t1-transformation, standard-models-h2-and-water, eom-ccsd-and-size-extensivity, coupled-cluster-optimization-and-lagrangian]
also: []
date: 2026-11-04
---

## How accurate is each CC level?

**Order counting (HJO Sec. 14.6.1).** Compare the projected CC equations level by level.

- **CCSD to CCSDT.** Going up a level changes the singles and doubles projections only at third order. The new triples equations are second order.
- **CCSD.** Its singles and doubles are therefore correct to second order. Its wave function is correct only to first order, because the triples are missing at second. Its energy, built from singles and doubles, is correct to third order.
- **CCSDT.** Wave function correct to second order, energy to fourth.
- **General rule.** A level-$N$ CC wave function is correct to order $N-1$ and its energy to order $\lfloor3N/2\rfloor$. CCSDTQ is good to sixth order and CCSDTQ5 to seventh (HJO Table 14.5).

**Beyond order counting.** CCSD and MP3 are both correct to third order, but CCSD is much better. It also satisfies the projected Schrödinger equation in the singles and doubles space, and it is exact for two electrons, whereas MP3, like HF, is exact only for one.

HJO's water plots (Figs. 14.8 and 14.9) show the same thing. Near equilibrium CC and MP converge similarly, with CC uniformly ahead. At $2R_{\text{ref}}$ only CC converges smoothly; MP and CC agree only by sixth order.

## Iterative hybrids: CC2 and CC3

**CC2 (HJO Sec. 14.6.2).**

- **Equations.** Singles as in CCSD. Doubles only to first order, $\varepsilon_{\mu_2}t_{\mu_2} = -\langle\mu_2|\tilde H|\text{HF}\rangle$ with the $T_1$-transformed Hamiltonian ([[closed-shell-ccsd-t1-transformation]]).
- **Cost and accuracy.** $n^5$ per iteration; energy correct to second order, like MP2.
- **Why use it.** It is a proper CC response model, good for time-dependent properties and excitation energies.

**CC3.** Keep in the CCSDT triples equations only the second-order terms:

$$
\varepsilon_{\mu_3}t_{\mu_3} = -\langle\mu_3|[\tilde H,\hat T_2]|\text{HF}\rangle,
$$

and feed $\hat T_3$ back into the singles and doubles equations.

- **Accuracy.** Singles and doubles are correct to third order, triples to second, and the energy to fourth, as in CCSDT.
- **Cost.** $n^7$ per iteration.

## CCSD(T)

**Construction (HJO Sec. 14.6.3).** Instead of iterating CC3, evaluate its lowest-order energy terms once, using converged CCSD amplitudes:

- **Triples amplitudes.** $t^{abc}_{ijk}$ from $\langle\mu_3|[\hat\Phi,\hat T_2]|\text{HF}\rangle/\varepsilon_{\mu_3}$.
- **Fourth-order triples energy.** $\langle\bar t_2|[\hat\Phi,\hat T_3]|\text{HF}\rangle$, the MP4(T)-like term.
- **Fifth-order singles-triples term.** $\langle\bar t_1|[\hat\Phi,\hat T_3]|\text{HF}\rangle$, which has no MP4 counterpart.

In the closed-shell biorthogonal basis the bra amplitudes are $\bar t_i^a = 2t_i^a$ and $\bar t_{ij}^{ab} = 4t_{ij}^{ab} - 2t_{ij}^{ba}$. Without the singles term the method is CCSD[T].

**Cost and judgement.** The cost is $O^3V^4$, like MP4, but paid once. The energy is fourth-order correct and exact for two electrons. HJO call it the method of choice for energies and static properties, while CC3 is preferable for time-dependent properties.

**HJO Tables 14.6-14.7 in brief.**

| Model | MP2 | CC2 | MP3 | CCSD | MP4 | CCSD(T) | CC3 | CCSDT |
|---|---|---|---|---|---|---|---|---|
| Energy correct to order | 2 | 2 | 3 | 3 | 4 | 4 | 4 | 4 |
| Cost | $n^5$ | $n^5$ (iterative) | $n^6$ | $n^6$ (iterative) | $n^7$ | $n^7$ | $n^7$ (iterative) | $n^8$ (iterative) |
| Exact for $N$ electrons | 1 | | 1 | 2 | 1 | 2 | 2 | 3 |

!!! example "HJO Fig. 14.10 recomputed: water/cc-pVDZ, $E - E_{\text{FCI}}$ ($E_h$; HJO's FCI; computed for this note)"
    | Method | $R_{\text{ref}}$ (HF weight 0.941) | $2R_{\text{ref}}$ (HF weight 0.589) |
    |---|---:|---:|
    | MP2 | 0.013131 | 0.054730 |
    | CC2 | 0.012254 | 0.037153 |
    | MP3 | 0.006439 | 0.069096 |
    | CCSD | 0.003744 | 0.022032 |
    | MP4 | 0.001060 | 0.016046 |
    | CCSD(T) | 0.000658 | −0.003820 |
    | CC3 | not computed | not computed |
    | CCSDT | 0.000493 | −0.001405 |

    - **At $R_{\text{ref}}$.** The errors fall steadily along HJO's sequence. (T) recovers 95% of the full-triples correction.
    - **At $2R_{\text{ref}}$.** MP3 is worse than MP2, as HJO note. CCSD(T) overshoots below FCI by 3.8 m$E_h$, more than CCSDT's 1.4 m$E_h$. The perturbative triples become unreliable once the HF weight drops to 0.59.
    - **Tools.** MP3 and MP4 come from the λ-scaled-CCSD Taylor coefficients of [[moller-plesset-and-coupled-cluster-perturbation-theory]]. CC2 is PySCF's `rccsd` with `cc2 = True`; CCSDT is `rccsdt`.

## Spin-orbital (T) and [T], and the other approximate-triples models

**The perturbative chain.** In the language of [[ccsd-spin-orbital-equations]], triples first enter the energy at fourth order (MP4) through

$$
\hat T_2^{(1)}\ \xrightarrow{\ \langle\Phi_{ijk}^{abc}|\hat V_N\hat T_2^{(1)}|\Phi_0\rangle\ }\ \hat T_3^{(2)}\ \xrightarrow{\ \langle\Phi_{ij}^{ab}|\hat V_N\hat T_3^{(2)}|\Phi_0\rangle\ }\ \hat T_2^{(3)}\ \longrightarrow\ E_T^{(4)} = \langle\Phi_0|\hat V_N\hat T_2^{(3)}|\Phi_0\rangle .
$$

**Variants built on the chain.**

- **CCSD+T(4).** Evaluate this chain with first-order (MP1) doubles and add it to $E_{\text{CCSD}}$.
- **CCSD[T]** (Urban, Noga, Cole and Bartlett 1985). Use the converged CCSD $\hat T_2$ instead; this was earlier called CCSD+T(CCSD).
- **CCSD(T)** (Raghavachari, Trucks, Pople and Head-Gordon 1989). Add the fifth-order singles-triples term $E_{ST}^{(5)}$, evaluated with converged $\hat T_1$.

**Spin-orbital working equations.** Notation: $P(p/qr)f(pqr) = f(pqr)-f(qpr)-f(rqp)$ and $D_{ijk}^{abc} = f_{ii}+f_{jj}+f_{kk}-f_{aa}-f_{bb}-f_{cc}$ (canonical orbitals). The connected and disconnected triples are

$$
D_{ijk}^{abc}\,t_{ijk}^{abc}(\text{c}) = P(i/jk)P(a/bc)\Big[\sum_e t_{jk}^{ae}\langle ei||bc\rangle - \sum_m t_{im}^{bc}\langle ma||jk\rangle\Big],\qquad
D_{ijk}^{abc}\,t_{ijk}^{abc}(\text{d}) = P(i/jk)P(a/bc)\,t_i^a\langle jk||bc\rangle,
$$

and the energies are

$$
E_{[T]} = \tfrac1{36}\sum_{ijkabc}t_{ijk}^{abc}(\text{c})\,D_{ijk}^{abc}\,t_{ijk}^{abc}(\text{c}),\qquad
E_{ST} = \tfrac1{36}\sum_{ijkabc}t_{ijk}^{abc}(\text{c})\,D_{ijk}^{abc}\,t_{ijk}^{abc}(\text{d}),\qquad
E_{(T)} = E_{[T]} + E_{ST}.
$$

**Why it is affordable.**

- The triples are never stored. For a fixed batch $(i,j,k)$ all $t_{ijk}^{abc}$ are built ($v^3$ storage), contracted into the energy, and discarded. The cost is one noniterative $o^3v^4$ pass.
- $E_{[T]}$ evaluated with $t_i^a=0$ and MP1 doubles is the MP4 triples energy, i.e. CCSD+T(4).

**Iterative and noniterative relatives** (Crawford, part 3; references checked).

| Model | Idea | Iterative? | Reference |
|---|---|---|---|
| CCSDT-1a | lowest-order $\hat T_3$ equation, coupled back into $\hat T_1,\hat T_2$ | yes | Lee, Kucharski, Bartlett, *JCP* **81**, 5906 (1984) |
| CCSDT-1b | CCSDT-1a plus extra $\hat T_3\to\hat T_2$ couplings | yes | Urban, Noga, Cole, Bartlett, *JCP* **83**, 4041 (1985) |
| CCSDT-2, CCSDT-3 | add $\tfrac12\hat T_2^2$ terms (−2), then $\hat T_1$ terms (−3) to the $\hat T_3$ equation | yes | Noga, Bartlett, Urban, *CPL* **134**, 126 (1987) |
| CC3 | CCSDT-1-like, with $\hat T_1$ treated as zeroth order (via the $T_1$-transformed Hamiltonian) | yes | Koch, Christiansen, Jørgensen, Sánchez de Merás, Helgaker, *JCP* **106**, 1808 (1997) |
| CCSDR(3) | noniterative counterpart of CC3 | no | Christiansen, Koch, Jørgensen (reference to add) |
| CCSDT | full triples | yes, $o^3v^5$ | Noga and Bartlett, *JCP* **86**, 7041 (1987) |

All approximate models are $O(N^7)$ and none store the full $\hat T_3$.

!!! example "Water/6-31G, all electrons: CCSD+T(4), CCSD[T], CCSD(T) and CCSDT against FCI (computed for this note)"
    **Geometry.** $r_{\text{OH}} = 0.9572$ Å and 104.52°, and the same angle with both OH bonds doubled ($2R_e$). RHF reference.

    **Code check.** The spin-orbital $E_{(T)}$ from my code equals PySCF's `ccsd_t()` to $2\times10^{-13}\,E_h$ (at a slightly different equilibrium geometry; see [[ccsd-spin-orbital-equations]]). CCSDT is PySCF `rccsdt`; FCI is all-electron.

    | | $R_e$ | $2R_e$ |
    |---|---:|---:|
    | $E_{\text{FCI}}$ ($E_h$) | −76.120837 | −75.880535 |
    | max $\lvert t_i^a\rvert$ | 0.011 | 0.075 |
    | $E_T^{(4)}$[MP1 doubles] | −1.003 | −12.202 |
    | $E_{[T]}$ | −1.093 | −16.195 |
    | $E_{ST}$ | +0.099 | +1.424 |

    Triples energies in m$E_h$. Errors $E-E_{\text{FCI}}$ in m$E_h$:

    | Method | $R_e$ | $2R_e$ |
    |---|---:|---:|
    | CCSD | 1.518 | 9.942 |
    | CCSD+T(4) | 0.515 | −2.260 |
    | CCSD[T] | 0.425 | −6.254 |
    | CCSD(T) | 0.524 | −4.829 |
    | CCSDT | 0.441 | −1.359 |

    **At $R_e$.**

    - All three perturbative corrections land within 0.1 m$E_h$ of CCSDT.
    - [T] happens to be closest. $E_{ST}$ is positive, so (T) is slightly less negative than [T].
    - The remaining 0.44 m$E_h$ is mostly quadruples.

    **At $2R_e$.**

    - Every perturbative correction overshoots below FCI.
    - [T] is the worst, by 6.3 m$E_h$. The positive $E_{ST}$ ($+1.4$ m$E_h$) moves (T) about 30% of the way back toward CCSDT.
    - CCSD+T(4) looks best here only because its MP1 doubles underestimate the triples. That is a cancellation of errors, not a better method.

## Source

Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, Chichester, 2000), Sec. 14.6, pp. 783-796, Eqs. (14.6.1)-(14.6.63), Tables 14.5-14.7, Figs. 14.8-14.10. Recomputed for this note with PySCF 2.14 (`hjo/c14/fig1410.py`, `hjo/c14/mpn.py`, `hjo/c13/ccsdt.py`).

The spin-orbital triples section draws on T. D. Crawford, *Coupled Cluster Theory*, ESQC 2026 lecture slides, part 3 ("Higher excitations", "CCSD(T)", "Other approximate triples methods"), and on T. D. Crawford and H. F. Schaefer, *Rev. Comput. Chem.* **14**, 33 (2000), doi:10.1002/9780470125915.ch2. Original methods: K. Raghavachari, G. W. Trucks, J. A. Pople and M. Head-Gordon, *Chem. Phys. Lett.* **157**, 479 (1989); M. Urban, J. Noga, S. J. Cole and R. J. Bartlett, *J. Chem. Phys.* **83**, 4041 (1985). Water/6-31G numbers recomputed with PySCF 2.15 (`esqc/cc/ccsd_so.py`, `esqc/cc/triples_bench.py`).
