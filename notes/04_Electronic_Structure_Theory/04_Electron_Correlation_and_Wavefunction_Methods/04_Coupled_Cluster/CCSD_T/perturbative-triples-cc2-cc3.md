---
id: perturbative-triples-cc2-cc3
title: Perturbation analysis of the coupled-cluster hierarchy and the hybrid models CC2, CC3 and CCSD(T) (HJO 14.6)
summary: Counting orders in the fluctuation potential, a CC model truncated at excitation level N has a wave function correct to order N − 1 and an energy correct to order ⌊3N/2⌋. So CCSD is correct to third order and CCSDT to fourth. Hybrid models keep only the lowest-order terms of the next level. CC2 approximates the doubles (n⁵, iterative, energy correct to second order) and CC3 approximates the triples (n⁷ iterative, fourth order). CCSD(T) adds noniteratively the fourth-order triples energy plus a fifth-order singles-triples term, built from CCSD amplitudes with closed-shell bra amplitudes 2t_i^a and 4t_ij^ab − 2t_ij^ba. Recomputed for water/cc-pVDZ against HJO's FCI: MP2, CC2, MP3, CCSD, MP4, CCSD(T) and CCSDT errors (HJO Fig. 14.10; CC3 is not available in PySCF).
status: in-progress
kind: comparison
level: advanced
tags: [ccsd-t, cc2, cc3, perturbative-triples, coupled-cluster, moller-plesset, order-analysis, water]
prerequisites: [moller-plesset-and-coupled-cluster-perturbation-theory, coupled-cluster-hierarchy-and-size-extensivity]
related: [closed-shell-ccsd-t1-transformation, standard-models-h2-and-water, eom-ccsd-and-size-extensivity, coupled-cluster-optimization-and-lagrangian]
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

## Source

Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, Chichester, 2000), Sec. 14.6, pp. 783-796, Eqs. (14.6.1)-(14.6.63), Tables 14.5-14.7, Figs. 14.8-14.10. Recomputed for this note with PySCF 2.14 (`hjo/c14/fig1410.py`, `hjo/c14/mpn.py`, `hjo/c13/ccsdt.py`).
