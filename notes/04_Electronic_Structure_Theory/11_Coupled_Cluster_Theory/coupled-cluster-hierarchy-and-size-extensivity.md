---
id: coupled-cluster-hierarchy-and-size-extensivity
title: The coupled-cluster hierarchy (HJO Ch. 13.1-13.3) - pair clusters, connected and disconnected amplitudes, linked versus unlinked projected equations, rank rules for the BCH expansion, and size-extensivity, with water/cc-pVDZ excitation-level weights and the CCSD and CCSDT errors recomputed
summary: HJO build the CC state from pair clusters ∏(1 + t τ)|HF⟩ = exp(T̂)|HF⟩. Every determinant is reached by connected and disconnected (product) clusters. Projection replaces the intractable variational conditions. Linked and unlinked equations are equivalent when the projection manifold is closed under de-excitation; the linked form is quartic in T and size-extensive term by term. Rank rules show the doubles enter the CCSD equations only quadratically. Recomputed for water/cc-pVDZ: CCSD excitation-level weights (HJO Table 13.1, all printed CCSD digits), CCSD and CCSDT errors against HJO's FCI (HJO Table 5.11 / Fig. 13.3), and CCSD at R_ref and 2R_ref.
status: in-progress
kind: theory
level: advanced
tags: [coupled-cluster, ccsd, ccsdt, ccsdtq, exponential-ansatz, connected-clusters, disconnected-clusters, size-extensivity, linked-equations, bch-expansion]
prerequisites: [coupled-cluster-second-quantization, ci-size-extensivity-and-excitation-levels]
related: [coupled-cluster-optimization-and-lagrangian, closed-shell-ccsd-t1-transformation, eom-ccsd-and-size-extensivity, coupled-cluster-variants-brueckner-qcisd-open-shell, standard-models-h2-and-water, coupled-cluster-doubles, linked-cluster-theorem]
order: 50
date: 2026-11-04
---

## From pair clusters to exp(T)

**Pair clusters (HJO Sec. 13.1.1).** In the independent-particle model, a pair of electrons in spin orbitals $I, J$ never scatters. Correlation adds virtual excitations $IJ\to AB$, each with an amplitude:

$$
|\text{CCD}\rangle = \prod_{A>B,\,I>J}\big(1 + t^{AB}_{IJ}\hat\tau^{AB}_{IJ}\big)|\text{HF}\rangle,\qquad \hat\tau^{AB}_{IJ} = a^\dagger_Aa_Ia^\dagger_Ba_J .
$$

**General clusters (HJO Sec. 13.1.2).** Adding single, triple and higher clusters gives $|\text{CC}\rangle = \prod_\mu(1 + t_\mu\hat\tau_\mu)|\text{HF}\rangle$.

- **Commuting factors.** All $\hat\tau_\mu$ excite from occupied to virtual spin orbitals, so they commute and the order of the factors is irrelevant.
- **Exponential form.** $\hat\tau_\mu^2 = 0$, so $1 + t_\mu\hat\tau_\mu = \exp(t_\mu\hat\tau_\mu)$. Hence $|\text{CC}\rangle = \exp(\hat T)|\text{HF}\rangle$ with $\hat T = \sum_\mu t_\mu\hat\tau_\mu$ (HJO Sec. 13.2.1).

**Connected and disconnected (HJO Sec. 13.1.3).**

- **Several routes.** A determinant can be reached in several ways: one connected amplitude $t_{\mu\nu}$, or a product $t_\mu t_\nu$ of disconnected ones.
- **Excitation levels.** Collecting terms gives $\hat C_2 = \hat T_2 + \tfrac12\hat T_1^2$, $\hat C_3 = \hat T_3 + \hat T_1\hat T_2 + \tfrac16\hat T_1^3$ and $\hat C_4 = \hat T_4 + \hat T_1\hat T_3 + \tfrac12\hat T_2^2 + \tfrac12\hat T_1^2\hat T_2 + \tfrac1{24}\hat T_1^4$ (see [[coupled-cluster-second-quantization]]).
- **Truncation.** A truncated CC state still contains every FCI determinant, with products of the amplitudes as coefficients.
- **Untruncated.** The full CC and FCI states have the same number of parameters (one connected amplitude per determinant), so neither has an advantage. The exponential pays off only on truncation.

## Projection instead of variation

**Why not variational (HJO Sec. 13.1.4).** Minimizing $\langle\text{CC}|\hat H|\text{CC}\rangle/\langle\text{CC}|\text{CC}\rangle$ couples all FCI determinants and high powers of the amplitudes. Instead, project the Schrödinger equation onto the HF state and onto the determinants $\langle\mu|$ that carry connected amplitudes:

$$
\text{unlinked:}\quad \langle\mu|\hat H e^{\hat T}|\text{HF}\rangle = E\langle\mu|e^{\hat T}|\text{HF}\rangle;\qquad
\text{linked:}\quad \langle\mu|e^{-\hat T}\hat He^{\hat T}|\text{HF}\rangle = 0;\qquad
E = \langle\text{HF}|\hat He^{\hat T}|\text{HF}\rangle .
$$

- **Truncation is harmless.** $\hat H$ couples determinants that differ by at most a double excitation, so every projection terminates after a few terms.
- **The price.** The energy is no longer an upper bound. At $2R_{\text{ref}}$ CCSDT and CCSDTQ fall *below* FCI (table below). Partly converged CCSD energies can also undershoot the final one (HJO Table 13.2, [[coupled-cluster-optimization-and-lagrangian]]).
- **Expectation value instead.** HJO's Fig. 13.1 shows that $\langle\text{CC}|\hat H|\text{CC}\rangle/\langle\text{CC}|\text{CC}\rangle$, evaluated with the projected amplitudes, is barely different and always a little lower for water. Making it variational is not worth the cost.

**Equivalence of linked and unlinked forms (HJO Sec. 13.2.3).**

- **Matrices.** Define $(\mathbf T^\pm)_{\mu\nu} = \langle\mu|e^{\pm\hat T}|\nu\rangle$. Both are lower triangular with unit diagonal, hence nonsingular.
- **Argument.** Multiplying the linked equations by $\mathbf T^+$ and inserting a resolution of the identity over the projection manifold gives exactly the unlinked equations. This works whenever the manifold is closed under de-excitation: CCSD, CCSDT, …, CCD, and models with selected excitations at the top level only.
- **Why the linked form is preferred.**
  - It is at most quartic in $\hat T$ for any truncation.
  - It is size-extensive term by term.
  - It is the starting point for perturbation theory (Ch. 14), for EOM-CC ([[eom-ccsd-and-size-extensivity]]) and for the $T_1$ transformation ([[closed-shell-ccsd-t1-transformation]]).

**Energy (HJO Sec. 13.2.4).** $E = E_{\text{HF}} + \langle\text{HF}|\hat H(\hat T_2 + \tfrac12\hat T_1^2)|\text{HF}\rangle$, using Brillouin's theorem. Only singles and doubles enter the energy directly, at any truncation level.

## Rank rules: why the BCH series stops

**Ranks (HJO Secs. 13.2.5 and 13.2.8).** For a string of operators $A$, the up rank $s^+_A$ counts virtual creators and occupied annihilators, and the down rank $s^-_A$ counts occupied creators and virtual annihilators, each with weight ½.

- **Particle and excitation rank.** The particle rank is $m_A = s^+_A + s^-_A$ and the excitation rank $s_A = s^+_A - s^-_A$.
- **Effect of one commutator.** Each commutator with a cluster operator lowers the down rank by ½. So $k$ nested commutators vanish unless $2s^-_A\ge k$.
- **Termination.** $\hat H$ has down rank at most 2, so $e^{-\hat T}\hat He^{\hat T}$ stops after the fourfold commutator.

**Range of a nested commutator.** For an $m_O$-particle operator $\hat O$,

$$
\sum_in_i - m_O\ \le\ s\big([\ldots[\hat O,\hat T_{n_1}],\ldots,\hat T_{n_k}]|\text{HF}\rangle\big)\ \le\ \sum_in_i + m_O - k,\qquad k\le2m_O .
$$

- **CCSD singles equations.** These are quartic in $\hat T_1$.
- **CCSD doubles equations.** These contain $\hat T_2$ only quadratically.
- **Higher truncations.** Above the doubles, the highest excitation level appears only linearly in its own equations.

## Excitation-level weights: what disconnected clusters capture

!!! example "HJO Table 13.1 recomputed: weights of excitation levels in the normalized CCSD state of water/cc-pVDZ (computed for this note)"
    **Method.** Spin-orbital CCSD amplitudes, all electrons, HOH = 110.565°. I expanded $e^{\hat T}|\text{HF}\rangle$ exactly by enumerating every partition of each excitation into connected singles and doubles with the permutation sign. The norms $N_n = \|\hat C_n|\text{HF}\rangle\|^2$ were computed for $n\le4$.

    Table entries are $W_n = W_0N_n$, using HJO's $W_0$. FCI columns are quoted from HJO.

    | Level | CCSD, $R_{\text{ref}}$ (mine) | HJO CCSD | HJO FCI | CCSD, $2R_{\text{ref}}$ (mine) | HJO CCSD | HJO FCI |
    |---:|---:|---:|---:|---:|---:|---:|
    | 0 | (0.94410) | 0.94410 | 0.94100 | (0.65114) | 0.65114 | 0.58966 |
    | 1 | 0.00056 | 0.00056 | 0.00053 | 0.02494 | 0.02494 | 0.02680 |
    | 2 | 0.05413 | 0.05413 | 0.05650 | 0.28762 | 0.28762 | 0.33300 |
    | 3 | 0.00002 | 0.00002 | 0.00055 | 0.00371 | 0.00371 | 0.01040 |
    | 4 | 0.00115 | 0.00115 | 0.00137 | 0.03225 | 0.03225 | 0.03970 |

    - **Unnormalized norms.** $N_1, \ldots, N_4$ = 5.971e-4, 0.057335, 2.49e-5, 1.2152e-3 at $R_{\text{ref}}$, and 0.038297, 0.44171, 5.702e-3, 0.049535 at $2R_{\text{ref}}$.
    - **Normalization check.** At $2R_{\text{ref}}$, $1 - W_0\sum_{n\le4}N_n = 0.00034$, exactly HJO's $W_5 + W_6 = 0.00006 + 0.00028$.
    - **Quadruples.** Built entirely from disconnected products (mostly $\tfrac12\hat T_2^2$), they recover 84% of the FCI quadruples weight at $R_{\text{ref}}$ and 81% at $2R_{\text{ref}}$.
    - **Triples.** Only 4% at $R_{\text{ref}}$ (0.00002 versus 0.00055). The triples are *not* products of lower clusters. This is why connected $\hat T_3$ (or a perturbative estimate of it, Ch. 14) matters for accuracy.
    - **Doubles at $2R_{\text{ref}}$.** Underestimated by 14%, a sign of static correlation that CCSD cannot handle.

## The hierarchy converges uniformly

!!! example "Water/cc-pVDZ, $E - E_{\text{FCI}}$ ($E_h$), using HJO's FCI −76.241860 and −75.951665 (computed for this note)"
    | Model | $R_{\text{ref}}$ | $2R_{\text{ref}}$ | HJO (Table 5.11) |
    |---|---:|---:|---|
    | RHF | 0.217822 | 0.363954 | same |
    | CCSD (−76.238116 / −75.929633) | 0.003744 | 0.022032 | same |
    | CCSDT (−76.241367 / −75.953070) | 0.000493 | −0.001405 | same |
    | CCSDTQ (HJO, quoted) | | | 0.000019 / −0.000446 |

    - **CCSDT.** Took 5 s and 21 s with PySCF's `rccsdt` and reproduces HJO's numbers to the last digit, including the overshoot below FCI at $2R_{\text{ref}}$.
    - **CCSDTQ.** Not recomputed: PySCF's `rccsdtq` had not finished after 18 CPU-minutes on two cores and was stopped. HJO's values are quoted.
    - **Rate.** Each level cuts the error by a factor of roughly 6-26 at $R_{\text{ref}}$ (3.744 → 0.493 → 0.019 → 0.003 m$E_h$; HJO Fig. 13.3).
    - **Comparison with CI.** The CI hierarchy improves mainly at even levels. CCSD (3.7 m$E_h$) falls between CISDT and CISDTQ because $\tfrac12\hat T_2^2$ enters CI only at the quadruples level ([[standard-models-h2-and-water]]).

## Size-extensivity

**Linked form (HJO Secs. 13.3.1-13.3.2).** For noninteracting A and B, $\hat H = \hat H_A + \hat H_B$ and $\hat T = \hat T_A + \hat T_B$ with $[\hat T_A, \hat T_B] = 0$, so

$$
e^{-\hat T}\hat He^{\hat T} = e^{-\hat T_A}\hat H_Ae^{\hat T_A} + e^{-\hat T_B}\hat H_Be^{\hat T_B} .
$$

- **Projections.** Onto A-only, B-only and mixed excitations, these reduce to the separate equations, and mixed ones vanish identically. So $\hat T_A + \hat T_B$ solves the compound problem and $E = E_A + E_B$.
- **Term by term.** Each commutator term is separately extensive. Dropping any *complete* commutator (as in CC2, QCISD or CCPT) keeps extensivity.

**Unlinked form (HJO Sec. 13.3.3).** Here extensivity emerges only after unlinked terms ($E\langle\mu|e^{\hat T}|\text{HF}\rangle$) cancel among themselves. Truncating such terms individually can destroy it, as CISD does ([[ci-size-extensivity-and-excitation-levels]]).

**Numbers (HJO Sec. 13.3.4).**

- **Per monomer.** CCSD recovers −214.1 of −217.8 m$E_h$ (98%) of the correlation energy at $R_{\text{ref}}$, and −341.9 of −364.0 (94%) at $2R_{\text{ref}}$ (CCSD recomputed, FCI quoted). These fractions are the same for any number of noninteracting monomers.
- **Contrast with CISD.** It drops from −205.8 to −162.4 m$E_h$ per monomer for eight monomers.
- **Wave-function overlap.** The CCSD wave function is a product, so its overlap with FCI decays as $S^m$.
- **High even excitations.** These look *better* for many monomers only because independent pair excitations on different monomers dominate.

## Source

Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, Chichester, 2000), Secs. 13.1-13.3, pp. 648-670, Eqs. (13.1.1)-(13.3.32), Table 13.1, Figs. 13.1-13.4; Table 5.11 (p. 189). Recomputed for this note with PySCF 2.14 (RCCSD, `rccsdt`) and my own exact expansion of $e^{\hat T}$ by excitation level (`hjo/c13/t131.py`, `hjo/c13/ccsdt.py`). FCI energies and FCI weights are quoted from HJO.
