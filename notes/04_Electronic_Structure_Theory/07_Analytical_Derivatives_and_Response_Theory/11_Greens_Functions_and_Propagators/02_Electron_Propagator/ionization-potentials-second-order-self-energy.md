---
id: ionization-potentials-second-order-self-energy
title: Ionization potentials from the second-order self-energy - orbital relaxation, pair relaxation and pair removal
summary: The simplest Green's-function correction to Koopmans' theorem, ε_c + Σ(2)_cc(ε_c), equals the difference of second-order energies of the N- and (N−1)-electron systems computed with N-electron Hartree-Fock orbitals. It splits into orbital relaxation (ORX), pair relaxation (PRX) and pair removal (PRM). Recomputed Szabo Tables 7.2-7.6 (H2, the ten-electron series, N2), the correct N2 ordering of 3σg and 1πu, and a cc-pVTZ comparison with the Dyson solution and EOM-IP-CCSD.
status: in-progress
kind: derivation
level: advanced
tags: [ionization-potential, self-energy, orbital-relaxation, pair-relaxation, pair-removal, koopmans, green-function, n2]
prerequisites: [one-particle-greens-function, mp2, koopmans-theorem]
related: [hf-closed-shell-basis-set-trends, propagators-and-superoperators, linked-cluster-theorem]
also: [04_Electronic_Structure_Theory/08_Electronic_and_Molecular_Properties/01_Electronic_Energies, 04_Electronic_Structure_Theory/15_Benchmarking_and_Validation/01_Energy_Benchmarks]
date: 2026-11-03
---

## The result

Write the simplest Green's-function estimate ([[one-particle-greens-function]]) for removing an electron from spin orbital $\chi_c$:

$$
-\text{IP}_c \approx \varepsilon_c + \Sigma_{cc}^{(2)}(\varepsilon_c)
= \varepsilon_c + \frac12\sum_{a,rs}\frac{|\langle rs||ca\rangle|^2}{\varepsilon_c + \varepsilon_a - \varepsilon_r - \varepsilon_s} + \frac12\sum_{ab,r}\frac{|\langle ab||cr\rangle|^2}{\varepsilon_c + \varepsilon_r - \varepsilon_a - \varepsilon_b} .
$$

**Theorem (Szabo Sec. 7.4, after Pickup and Goscinski).** This equals

$$
\varepsilon_c + \Sigma_{cc}^{(2)}(\varepsilon_c) = {}^NE^{(0+1+2)} - {}^{N-1}\tilde E^{(0+1+2)}(c),
$$

the difference of second-order energies. For $N$ electrons this is the ordinary MP partition ([[mp2]]). For $N-1$ electrons, $\mathscr H_0 = \sum_{i=1}^{N-1}\big(h(i) + v^{\text{HF},N}(i)\big)$ still contains the **$N$-electron** Hartree-Fock potential, so that $|{}^{N-1}\Psi_c\rangle = a_c|{}^N\Psi_0\rangle$ is its eigenfunction. Using the same orbitals for both systems lets common correlation terms cancel explicitly.

## Derivation in three classes of excitations

**Zeroth and first order.** ${}^NE^{(0)} - {}^{N-1}\tilde E^{(0)} = \varepsilon_c$ and the first-order energies are equal (Szabo Ex. 7.13), which is Koopmans' theorem. The correction is the difference of second-order energies.

**Second order of the ion: three kinds of intermediate states.**

1. **Singles $a\to r$** ($a\ne c$). Brillouin's theorem does not hold for the ion in $N$-electron orbitals, so singles contribute
$$
{}^{N-1}\tilde E^{(2)}_{\text{ORX}} = \sum_{a\ne c,\,r}\frac{|\langle ac||cr\rangle|^2}{\varepsilon_a - \varepsilon_r} < 0 .
$$
They relax the orbitals toward the ion's own Hartree-Fock orbitals.

2. **Doubles $ab\to rs$ with $a, b\ne c$.** They are common to both systems and cancel in the difference:
$$
{}^{N-1}\tilde E^{(2)}_{\text{doubles}} = {}^NE^{(2)} - \sum_{a,\,r<s}\frac{|\langle rs||ca\rangle|^2}{\varepsilon_c + \varepsilon_a - \varepsilon_r - \varepsilon_s} .
$$
The subtracted pairs involve $c$, which no longer exists in the ion.

3. **Doubles $ab\to cr$.** $\chi_c$ is empty in the ion, so it can serve as a virtual orbital:
$$
{}^{N-1}\tilde E^{(2)}_{\text{PRX}} = \frac12\sum_{a,b\ne c,\,r}\frac{|\langle ab||cr\rangle|^2}{\varepsilon_a + \varepsilon_b - \varepsilon_c - \varepsilon_r} < 0 .
$$

**Correction to Koopmans' IP.** Combining these gives $\text{IP} = \text{IP}_{\text{Koopmans}} + \Delta\text{IP}$ with

$$
\Delta\text{IP} = \underbrace{\sum_{a\ne c,\,r}\frac{|\langle ac||cr\rangle|^2}{\varepsilon_a - \varepsilon_r}}_{\text{ORX}<0}
+ \underbrace{\frac12\sum_{a,b\ne c,\,r}\frac{|\langle ab||cr\rangle|^2}{\varepsilon_a + \varepsilon_b - \varepsilon_c - \varepsilon_r}}_{\text{PRX}<0}
- \underbrace{\frac12\sum_{a,rs}\frac{|\langle rs||ca\rangle|^2}{\varepsilon_c + \varepsilon_a - \varepsilon_r - \varepsilon_s}}_{\text{PRM}>0} .
$$

| Excitation | In $N$ | In $N-1$ | Effect on Koopmans' IP | Name |
|---|---|---|---|---|
| $a\to r$ | no (Brillouin) | yes | lowers | orbital relaxation (ORX) |
| $ab\to rs$, $a,b\ne c$ | yes | yes | none (cancels) | |
| $ab\to cr$ | no ($c$ occupied) | yes | lowers | pair relaxation (PRX) |
| $ca\to rs$ | yes | no ($c$ empty) | raises | pair removal (PRM) |

**Interpretation.**

- **ORX.** The ion's orbitals contract around the hole.
- **PRX.** Pairs in the ion gain correlation from the newly vacant orbital $c$.
- **PRM.** The neutral has correlating pairs involving $c$ that the ion has lost.

J-S give the same three-term reading of the diagonal second-order propagator (their Eq. 6.80). The first two stabilize the ion and lower the IP; the third stabilizes the neutral and raises it. Koopmans' theorem works when these cancel. For a two-electron system PRX = 0 and PRM $= -{}^NE^{(2)}$ (Szabo Ex. 7.16).

## H₂: near cancellation

!!! example "H₂, R = 1.4 bohr (reproducing Szabo Tables 7.2-7.3; computed for this note)"
    | Basis | Koopmans | $\Sigma^{(2)}(\varepsilon)$ | Full CI | ORX | ORX exact | PRM | PRM exact |
    |---|---:|---:|---:|---:|---:|---:|---:|
    | STO-3G | 0.578 | 0.591 | 0.599 | 0.000 | 0.000 | 0.013 | 0.021 |
    | 4-31G | 0.596 | 0.593 | 0.595 | −0.020 | −0.026 | 0.017 | 0.025 |
    | 6-31G** | 0.595 | 0.598 | 0.600 | −0.023 | −0.029 | 0.026 | 0.034 |

    - **Agreement.** Every entry equals Szabo's.
    - **Exact references.** "Full CI" is $E(\text{H}_2^+) - E_{\text{FCI}}(\text{H}_2)$ in the basis. "ORX exact" is $E(\text{H}_2^+)$ minus its frozen-orbital energy ($h_{11} + V_{nn}$). "PRM exact" is $-E_{\text{corr}}(\text{H}_2)$. Experiment: 0.584.
    - **Near cancellation.** In the larger bases Koopmans is nearly exact because relaxation and pair removal cancel. The second-order terms are each about 75% of the exact ones, so their balance is reproduced.
    - **Dyson.** Iterating the diagonal Dyson equation changes these values by less than 0.001.

## The ten-electron series: overcorrection

!!! example "Lowest (HOMO) IPs in hartree (reproducing Szabo Table 7.4; computed for this note)"
    Koopmans / $\Sigma^{(2)}(\varepsilon)$ / iterated Dyson, Szabo geometries, Cartesian $d$ functions.

    | Molecule | STO-3G | 4-31G | 6-31G* | 6-31G** | Exp. |
    |---|---|---|---|---|---:|
    | CH₄ (1t₂) | .520/.495/.496 | .544/.503/.506 | .546/.508/.511 | .545/.512/.514 | 0.529 |
    | NH₃ (3a₁) | .353/.275/.279 | .414/.331/.338 | .421/.352/.358 | .421/.353/.359 | 0.400 |
    | H₂O (1b₁) | .391/.299/.304 | .500/.388/.398 | .498/.394/.404 | .497/.395/.405 | 0.463 |
    | FH (1π) | .464/.396/.399 | .628/.507/.517 | .629/.509/.520 | .627/.509/.519 | 0.581 |

    - **Agreement.** NH₃, H₂O and FH match Szabo's $\Sigma^{(2)}$ values to 0.001. CH₄ is 0.001-0.002 higher; its HOMO is triply degenerate, and any rotation within the degenerate set gives the same diagonal element here.
    - **Overcorrection.** Koopmans overestimates every IP, and the second-order correction overshoots by more: at 6-31G** the error moves from +0.02 to +0.05 hartree to −0.02 to −0.07. Iterating the Dyson equation recovers only 0.002-0.010 of this.

## N₂: the ordering is fixed by pair relaxation

**The problem.** Koopmans' theorem predicts the wrong order for N₂ in large bases. Experiment has 3σg (0.573) below 1πu (0.624); Koopmans has 3σg at 0.630 and 1πu at 0.612 in 6-31G*.

!!! example "N₂, R = 2.074 bohr (reproducing Szabo Tables 7.5-7.6; computed for this note)"
    | Basis | 3σg: KT | $\Sigma^{(2)}$ | ORX | PRX | PRM | 1πu: KT | $\Sigma^{(2)}$ | ORX | PRX | PRM |
    |---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
    | STO-3G | 0.539 | 0.463 | −0.005 | −0.091 | 0.020 | 0.573 | 0.620 | −0.001 | −0.008 | 0.056 |
    | 4-31G | 0.629 | 0.517 | −0.051 | −0.098 | 0.037 | 0.621 | 0.643 | −0.044 | −0.008 | 0.074 |
    | 6-31G* | 0.630 | 0.534 | −0.055 | −0.096 | 0.055 | 0.612 | 0.626 | −0.055 | −0.016 | 0.086 |

    - **Agreement.** These match Szabo to 0.001.
    - **Mechanism.** Orbital relaxation is about the same for both holes. The order is restored mainly by the much larger **pair relaxation** of the 3σg hole: double excitations that put an electron into the vacated 3σg orbital lower the ion's energy far more than for 1πu.

!!! example "Beyond Szabo: N₂ in cc-pVTZ (computed for this note)"
    | Method | 3σg | 1πu |
    |---|---:|---:|
    | Koopmans | 0.632 | 0.612 |
    | $\Sigma^{(2)}(\varepsilon)$ | 0.543 | 0.633 |
    | $\Sigma^{(2)}$, Dyson root (diagonal) | 0.553 | 0.631 |
    | EOM-IP-CCSD | 0.573 | 0.632 |
    | Experiment | 0.573 | 0.624 |

    **Szabo's comparison (Table 7.7; Cederbaum and Domcke, near-HF-limit Gaussian basis; literature values, not recomputed).** For 3σg / 1πu: Koopmans 0.635/0.615; $\Sigma^{(2)}(\varepsilon)$ 0.538/0.626; $\Sigma^{(2)}(E)$ 0.546/0.626; $\Sigma^{(2)}(E) + \Sigma^{(3)}(E)$ 0.584/0.613. The perturbation series in the self-energy oscillates; quantitative IPs need at least third order or a renormalized self-energy. EOM-IP-CCSD, a modern alternative (general knowledge), is within 0.01 hartree of experiment here.

## Code

```python
def sigma_ii(g, e, no, i, E):          # closed shell, chemists' g[p,q,r,s] = (pq|rs), spatial orbitals
    o, v = slice(0, no), slice(no, None); eo, ev = e[o], e[v]
    X = g[i, v, o, v]                  # (i r | a s): 2p1h
    t1 = np.einsum("ras,ras->", X, (2*X - X.transpose(2, 1, 0)) / (E + eo[None, :, None] - ev[:, None, None] - ev[None, None, :]))
    Y = g[i, o, v, o]                  # (i a | r b): 2h1p
    t2 = np.einsum("arb,arb->", Y, (2*Y - Y.transpose(2, 1, 0)) / (E + ev[None, :, None] - eo[:, None, None] - eo[None, None, :]))
    return t1 + t2
ip_koopmans = -e[i]; ip_2 = -(e[i] + sigma_ii(g, e, no, i, e[i]))
E = e[i]
for it in range(50): E = e[i] + sigma_ii(g, e, no, i, E)      # diagonal Dyson equation
```

The spatial-orbital code and an independent spin-orbital implementation (used for the ORX/PRX/PRM split) agree to all printed digits.

## Source

Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996; reprint of the revised first edition, McGraw-Hill, 1989), Sec. 7.4-7.5, pp. 398-409, Eqs. (7.69)-(7.87), Tables 7.1-7.7, Ex. 7.13-7.16. Jørgensen and Simons, *Second Quantization-Based Methods in Quantum Chemistry* (Academic Press, New York, 1981), Ch. 6, Sec. D.2b, pp. 138-139, Eq. (6.80). Experimental IPs and Table 7.7 quoted from Szabo; everything else computed for this note with PySCF 2.14.
