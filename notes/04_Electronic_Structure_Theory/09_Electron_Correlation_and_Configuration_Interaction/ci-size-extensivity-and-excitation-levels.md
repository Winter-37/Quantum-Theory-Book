---
id: ci-size-extensivity-and-excitation-levels
title: Truncated CI and size-extensivity - CAS and RAS spaces, the Davidson correction, noninteracting water molecules and the binomial distribution of excitation levels
summary: Full-CI expansions grow by about 16 per added electron pair, so practical CI truncates by classes of configurations (CAS for static correlation, then single and double excitations, RAS as the unifying scheme). Truncation destroys size-extensivity. For m noninteracting molecules the CISD correlation energy per molecule decays towards zero and the Hartree-Fock weight stays too large, because the important excitation level of the exact wave function grows linearly with m (binomially distributed). The Davidson correction repairs this only partly. Reproduced: HJO Table 11.1, all of Table 11.2 (CISD and CISD+Q for 1-8 waters at R_ref and 2R_ref), the minimal-basis H₂ model, and the ten-water excitation-level distribution.
status: in-progress
kind: theory
level: intermediate
tags: [configuration-interaction, cisd, size-extensivity, davidson-correction, cas, ras, excitation-levels, binomial-distribution, noninteracting-systems, water]
prerequisites: [cisd, full-ci, size-consistency]
related: [ci-optimization-newton-and-davidson, determinant-strings-and-direct-ci, coupled-cluster-doubles, standard-models-h2-and-water, hartree-fock-csf-parametrization-and-canonical-conditions]
order: 70
date: 2026-11-04
---

## How fast full CI grows

**Counting (HJO Sec. 11.1.2).** With $k$ α and $k$ β electrons in $n$ orbitals, $N_{\text{det}} = \binom nk^2$.

| $2k$ (electrons = orbitals) | 2 | 4 | 6 | 8 | 10 | 12 | 14 | 16 | 18 | 20 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| $N_{\text{det}}$ ($M_S = 0$) | 4 | 36 | 400 | 4 900 | 63 504 | 853 776 | 11 778 624 | 165 636 900 | 2 363 904 400 | 34 134 779 536 |

(HJO Table 11.1, recomputed.)

**Asymptotics.**

- **Electrons equal to orbitals.** Stirling's formula gives $N_{\text{det}}\approx16^k/(k\pi)$, so each new electron pair together with a new orbital pair multiplies the space by about 16.
- **Many orbitals.** For $n\gg k$, Stirling gives $N_{\text{det}}\approx(en/k)^{2k}/(2\pi k)$ (my derivation; the OCR of HJO's Eq. 11.1.8 is illegible), a power $n^{2k}$ of the basis size.

**Use.** Full CI is mostly a benchmark tool ([[full-ci]]).

## Truncating by classes: CAS and RAS

**Why classes.** Selecting individual configurations has been abandoned. A small hand-picked set cannot recover dynamical correlation, and the best selection changes across a potential surface.

**The modern scheme.**

1. **Reference space for static correlation.** A complete active space (CAS): inactive orbitals always doubly occupied, secondary orbitals always empty, and all distributions of the active electrons among the active orbitals.
2. **Dynamical correlation.** Add excitations out of the reference space (MRSDCI, or CISD for a single reference).

**Orbitals.**

- **Reference space.** Optimize its orbitals together with its configurations (MCSCF, HJO Ch. 12), so that no reference configuration is favoured.
- **Dynamical part.** HF or MCSCF orbitals are good enough, because only their nodal structure matters there.

**Restricted active space (RAS).** The active orbitals are split into RAS1, RAS2 and RAS3.

- **RAS1** has at least some minimum number of electrons (at most so many holes).
- **RAS3** has at most some maximum number of electrons.
- **RAS2** is unrestricted.

For example, a CAS-based MRSDCI is RAS1 = inactive orbitals with ≤ 2 holes, RAS2 = CAS, RAS3 = secondary orbitals with ≤ 2 electrons.

## Why truncated CI is not size-extensive

**Full CI is extensive.** For noninteracting A and B, the FCI state is the product $\hat\Psi_A\hat\Psi_B|\text{vac}\rangle$, whose correlation part contains $\hat\Psi_A^{\text{corr}}\hat\Psi_B^{\text{corr}}$. Expectation values of additively separable operators depend only on the fragment density matrices, so they never accumulate errors (compare [[hartree-fock-csf-parametrization-and-canonical-conditions]]).

**CID is not.** In CID the product term is a quadruple excitation and is missing from the compound space. HJO's Eq. (11.2.20) gives the compound correlation energy as

$$
E^{\text{corr}}_{AB} = \frac{\langle\Psi^{\text{CID}}_A|\hat H_A - E^{\text{HF}}_A|\Psi^{\text{CID}}_A\rangle + \langle\Psi^{\text{CID}}_B|\hat H_B - E^{\text{HF}}_B|\Psi^{\text{CID}}_B\rangle}{\langle\Psi^{\text{CID}}_A|\Psi^{\text{CID}}_A\rangle + \langle\Psi^{\text{CID}}_B|\Psi^{\text{CID}}_B\rangle - 1}.
$$

The numerator is additive but the normalization in the denominator couples the fragments.

**Davidson correction.** Setting the denominator to 1 makes the energy additive. Expressed in terms of $C_0$, the HF coefficient of the normalized CID vector, this gives (HJO 11.2.27)

$$
\Delta E_Q = (1 - C_0^2)\,E^{\text{CISD}}_{\text{corr}} .
$$

**Justification.** It is not rigorous: the compound-system amplitudes differ from the fragment ones. HJO stress that its real justification is empirical. Szabo's version of the argument is in [[cisd]].

## Noninteracting water molecules

**Reduction to one monomer.** For $m$ identical noninteracting monomers with canonical RHF orbitals, only the symmetric combination of each monomer's singles and doubles couples to the HF determinant, with coupling $\sqrt m\,\mathbf b$. Products of singles on different monomers and charge-transfer excitations decouple: they are reached only through Brillouin-vanishing or zero matrix elements. The $m$-monomer CISD problem is therefore the monomer CISD problem with $\mathbf b\to\sqrt m\,\mathbf b$, and it is solved exactly in the monomer space.

!!! example "HJO Table 11.2 recomputed: CISD correlation energy per monomer for $m$ noninteracting waters, cc-pVDZ (m$E_h$; computed for this note)"
    **Setup.** HOH = 110.565°, all electrons correlated. $E^{\text{HF}}$ = −76.0240 and −75.5877 $E_h$. FCI correlation (HJO) is −217.8 and −364.0 m$E_h$.

    | $m$ | CISD ($R_{\text{ref}}$) | CISD+Q | $W_{\text{HF}}$ | CISD ($2R_{\text{ref}}$) | CISD+Q | $W_{\text{HF}}$ |
    |---:|---:|---:|---:|---:|---:|---:|
    | 1 | −205.8 | −216.1 | 0.9499 | −291.9 | −353.2 | 0.7901 |
    | 2 | −196.5 | −213.4 | 0.9140 | −251.6 | −307.3 | 0.7786 |
    | 3 | −188.7 | −210.2 | 0.8863 | −229.5 | −283.1 | 0.7663 |
    | 4 | −182.1 | −206.8 | 0.8641 | −214.2 | −266.6 | 0.7556 |
    | 5 | −176.3 | −203.5 | 0.8456 | −202.6 | −254.1 | 0.7463 |
    | 6 | −171.1 | −200.2 | 0.8299 | −193.3 | −244.0 | 0.7380 |
    | 7 | −166.5 | −197.1 | 0.8164 | −185.6 | −235.6 | 0.7306 |
    | 8 | −162.4 | −194.1 | 0.8046 | −179.0 | −228.3 | 0.7240 |

    - **Agreement.** Every entry equals HJO's (last entry: 0.7240 against their 0.7241).
    - **At $R_{\text{ref}}$.** CISD falls from 94.5% to 74.6% of the FCI correlation per monomer. CISD+Q for four molecules is already no better than plain CISD for one.
    - **At $2R_{\text{ref}}$.** CISD falls from 80.2% to 49.2%.
    - **MP2 for comparison.** It recovers the same fraction (94%) for every $m$, because it is size-extensive.

**The HF weight.**

- **In FCI.** It is multiplicatively separable: $0.9411^m$ is 0.6153 at $m = 8$ ($R_{\text{ref}}$), and $0.5897^8$ = 0.0146 at $2R_{\text{ref}}$.
- **In CISD.** It stays much larger (0.80 and 0.72). CISD cannot describe simultaneous independent excitations.

## The minimal-basis H₂ model

**Setup (HJO Sec. 11.3).** Take $m$ noninteracting minimal-basis H₂ molecules. Let $K = g_{gugu}$ and $2\Delta = E^{\text{HF}}_u - E^{\text{HF}}$, where $E^{\text{HF}} = 2h_{gg} + g_{gggg}$ and $E^{\text{HF}}_u = 2h_{uu} + g_{uuuu}$. CID involves only $|\text{HF}\rangle$ and the normalized sum of the $m$ double excitations:

$$
E^{\text{CID}}_{\text{corr}}(m) = \Delta - \sqrt{\Delta^2 + mK^2},\qquad
C_D(m) = \frac{\Delta - \sqrt{\Delta^2 + mK^2}}{\sqrt mK},\qquad
E^{\text{FCI}}_{\text{corr}}(m) = m\big(\Delta - \sqrt{\Delta^2 + K^2}\big).
$$

**Behaviour.**

- **Large $m$.** The CID energy per molecule goes as $-K/\sqrt m\to0$.
- **Small $K/\Delta$.** The leading $-K^2/2\Delta$ terms of CID and FCI agree, but higher orders depend nonlinearly on $m$.
- **Davidson correction.** It removes the term linear in $m$ in the expansion: correct to fifth order in $K$ but only to first order in $m$, and wrong for a single molecule.
- **Density.** The CID density in each antibonding orbital is $2C_D^2/[m(1 + C_D^2)]$. It tends to the HF value 0 as $m$ grows, since $C_D\to-1$.

!!! example "H₂/STO-3G at R = 1.4 bohr ($K$ = 0.181258, $\Delta$ = 0.788645 $E_h$; computed for this note)"
    | $m$ | $E^{\text{CID}}/m$ | $E^{\text{CID+Q}}/m$ | $E^{\text{FCI}}/m$ | $C_D(m)$ |
    |---:|---:|---:|---:|---:|
    | 1 | −0.020562 | −0.020823 | −0.020562 | −0.113 |
    | 10 | −0.018629 | −0.020409 | −0.020562 | −0.325 |
    | 100 | −0.011881 | −0.015451 | −0.020562 | −0.656 |
    | 1000 | −0.004997 | −0.007155 | −0.020562 | −0.872 |

    - **Closed form.** It agrees with direct diagonalization of the $(m+1)$-dimensional CID matrix to all digits.
    - **Davidson correction.** It over-corrects the single molecule and helps for intermediate $m$, but cannot stop the collapse.

## The binomial distribution of excitation levels

**Derivation.** For $m$ noninteracting systems, each doubly excited with weight $W_D$ and unexcited with weight $W_{\text{HF}}$, the FCI weight of all $2k$-fold excitations is binomial:

$$
W_{2k}(m) = \binom mkW_{\text{HF}}^{m-k}W_D^k,\qquad \bar W = mW_D,\qquad \sigma_W = \sqrt{mW_{\text{HF}}W_D}.
$$

**Consequence.** The typical excitation level grows linearly with system size. Any expansion truncated at a fixed level degrades with system size; this is what coupled-cluster theory fixes ([[coupled-cluster-doubles]]).

!!! example "Ten noninteracting waters from HJO's monomer FCI weights (Exercise 11.1; computed for this note)"
    **Monomer weights (HJO Table 11E.1.1).** At $R_{\text{ref}}$: $W_0$ = 0.9410, $W_2$ = 0.0565, $W_4$ = 0.0014, $W_6$ = 0.000015.

    - **$R_{\text{ref}}$.** The tenth power of $\sum_kW_{2k}x^{2k}$ gives 0.544 (HF), 0.327 (doubles), 0.096 (quadruples) and 0.019 (sextuples). HJO quote 54.5%, 32.7%, 9.6% and 1.9%.
    - **$2R_{\text{ref}}$.** The tabulated even weights sum to only 0.963, so 3.7% lies in odd levels. With even levels alone, the eightfold excitations are the largest at 14.9%, against HJO's 15.9% from the full distribution. HF is down to 0.5%.

## Source

Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, Chichester, 2000), Secs. 11.1-11.3, pp. 523-540, Eqs. (11.1.1)-(11.3.36), Tables 11.1-11.2, Exercises 11.1-11.3. Recomputed for this note with PySCF 2.14 (GCISD contraction for the $\sqrt m$-scaled problem, `hjo/c11/table112.py`) and NumPy (`model.py`). FCI correlation energies and monomer FCI weights are quoted from HJO.
