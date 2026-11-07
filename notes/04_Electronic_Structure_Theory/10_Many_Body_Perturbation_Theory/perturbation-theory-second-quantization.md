---
id: perturbation-theory-second-quantization
title: Perturbation theory from the resolvent - Brillouin-Wigner versus Rayleigh-Schrödinger, size consistency of energies and wave functions, and the Møller-Plesset wave function
summary: Jørgensen and Simons' derivation of perturbation theory from one resolvent equation with a free energy parameter ℰ. ℰ = E_j gives Brillouin-Wigner theory, ℰ = E_j⁰ Rayleigh-Schrödinger. Only RS is size consistent: BW denominators contain the total energy, so the BW second-order correlation of n separated HeH⁺ ions falls to 0.3% of n times the monomer value at n = 1000. In RS third order the size-inconsistent renormalization term cancels against part of the main term, leaving a linked expression (J-S Eq. 3.43, checked for water). The first-order wave function is not product separable, yet the projected energy is extensive. The second-order MP wave function contains singles, doubles, triples and quadruples; its singles part is checked against an exact recursion.
status: in-progress
kind: derivation
level: advanced
tags: [perturbation-theory, brillouin-wigner, rayleigh-schrodinger, moller-plesset, size-consistency, resolvent, renormalization, wave-function-corrections]
prerequisites: [rayleigh-schrodinger-perturbation-theory, second-quantized-operators, greens-functions-single-particle]
related: [mp2, mp3, linked-cluster-theorem, size-consistency, iepa, heh-plus-minimal-basis-model, coupled-cluster-second-quantization, brillouin-theorem]
order: 40
date: 2026-11-03
---

## One equation, two theories

**Partition.** Write $H = H^0 + U$, where the eigenstates $H^0|k^0\rangle = E_k^0|k^0\rangle$ are known. In practice $H^0$ must be a one-electron operator, so that the $|k^0\rangle$ are determinants. Add and subtract a free parameter $\mathscr E$ in $H|j\rangle = E_j|j\rangle$:

$$
(\mathscr E - H^0)|j\rangle = (\mathscr E - E_j + U)|j\rangle .
$$

**Intermediate normalization.** Choose $\langle j^0|j\rangle = 1$ and split $|j\rangle = |j^0\rangle + Q|j\rangle$ with $Q = 1 - |j^0\rangle\langle j^0|$. Since $Q$ commutes with $H^0$, applying $Q$ and inverting gives the integral equation

$$
|j\rangle = |j^0\rangle + (\mathscr E - H^0)^{-1}Q(\mathscr E - E_j + U)|j\rangle .
$$

$Q$ keeps the resolvent away from its pole at $E_j^0$ ([[greens-functions-single-particle]]). For metals and other systems with many near-degenerate levels, other poles crowd in.

**Series.** Iterating gives the wave function, and projecting the Schrödinger equation on $\langle j^0|$ gives $E_j = E_j^0 + \langle j^0|U|j\rangle$, hence

$$
|j\rangle = \sum_{n=0}^\infty\big[(\mathscr E - H^0)^{-1}Q(\mathscr E - E_j + U)\big]^n|j^0\rangle,\qquad
E_j - E_j^0 = \sum_{n=0}^\infty\langle j^0|U\big[(\mathscr E - H^0)^{-1}Q(\mathscr E - E_j + U)\big]^n|j^0\rangle .
$$

- **$\mathscr E = E_j$** (exact energy): **Brillouin-Wigner** (BW). The factor $\mathscr E - E_j$ vanishes, but every denominator contains the unknown $E_j$, so the equations must be solved self-consistently.
- **$\mathscr E = E_j^0$**: **Rayleigh-Schrödinger** (RS). The denominators are known, and the $-E_j$ terms generate the renormalization terms of [[rayleigh-schrodinger-perturbation-theory]].

**In second quantization.** Take $H^0 = \sum_k\varepsilon_kk^\dagger k$ with $\varepsilon_k$ the eigenvalues of $h + V$ for some one-electron potential $V$. Then $U = \tfrac12\sum\langle ij|kl\rangle i^\dagger j^\dagger lk - \sum\langle i|V|j\rangle i^\dagger j$: the electron repulsion minus the potential already included in $H^0$. The first-order energy, the same in BW and RS, is

$$
E_j^{(1)} = \tfrac12\sum_{\mu\nu\in j^0}\langle\mu\nu||\mu\nu\rangle - \sum_{\mu\in j^0}\langle\mu|V|\mu\rangle .
$$

## Only Rayleigh-Schrödinger is size consistent

**Two noninteracting systems.** With $H = H_a^0 + U_a + H_b^0 + U_b$, the states are products, and the excited states are of three kinds: $|k_a^0j_b^0\rangle$, $|j_a^0k_b^0\rangle$ and $|k_a^0k_b^0\rangle$. The last kind has no matrix element with $|j_a^0j_b^0\rangle$, and the second-order energy reduces to

$$
E^{(2)} = \sum_{k_a}\frac{|\langle j_a^0|U_a|k_a^0\rangle|^2}{\mathscr E - E_{k_a}^0 - E_{j_b}^0} + \sum_{k_b}\frac{|\langle j_b^0|U_b|k_b^0\rangle|^2}{\mathscr E - E_{j_a}^0 - E_{k_b}^0} .
$$

- **RS.** With $\mathscr E = E_{j_a}^0 + E_{j_b}^0$, the spectator energy cancels from each denominator and $E^{(2)} = E_a^{(2)} + E_b^{(2)}$.
- **BW.** With $\mathscr E = E_j$, each denominator retains the total correlation (and first-order) energy of the **other** fragment. Fragment $a$'s energy then depends on whether $b$ exists, however far away.

!!! example "BW versus RS second order for n separated HeH⁺ ions (computed for this note)"
    J-S's minimal-basis HeH⁺ ([[heh-plus-minimal-basis-model]]), MP partitioning.

    - **Per ion.** $K = \langle11|22\rangle = 0.1262$, $\Delta_0 = 2(\varepsilon_2 - \varepsilon_1) = 2.8546$ and $E^{(1)} = -J_{11} = -0.9596$.
    - **RS.** $E^{(2)} = -K^2/\Delta_0 = -0.005576$ per ion, for any $n$.
    - **BW.** With $x = E_j - E_j^0$, second-order BW requires $x = nE^{(1)} + nK^2/(x - \Delta_0)$. The correlation part is $x - nE^{(1)}$.

    | $n$ | BW2 per ion | % of RS2 |
    |---:|---:|---:|
    | 1 | −0.004169 | 74.8 |
    | 2 | −0.003330 | 59.7 |
    | 10 | −0.001277 | 22.9 |
    | 100 | −0.000161 | 2.9 |
    | 1000 | −0.000017 | 0.3 |

    The per-ion BW energy falls roughly as $1/n$, faster than the $\sqrt n$ failure of doubles CI ([[size-consistency]]), because the extensive first-order energy sits in every denominator. (To infinite order BW is exact, and hence size consistent; the failure is one of truncation.)

## RS third order: cancelling the unlinked terms

**Structure.** The RS third-order energy is

$$
E_j^{(3)} = \sum_{k,l\ne j}\frac{\langle j^0|U|k^0\rangle\langle k^0|U|l^0\rangle\langle l^0|U|j^0\rangle}{(E_j^0 - E_k^0)(E_j^0 - E_l^0)} - E_j^{(1)}\sum_{k\ne j}\frac{|\langle j^0|U|k^0\rangle|^2}{(E_j^0 - E_k^0)^2} .
$$

The second term is a product of two extensive factors, so it grows as $n^2$ for $n$ copies. The $k = l$ part of the first term cancels it.

**The combined term.** Collect

$$
A = \sum_{k\ne j}\frac{|\langle j^0|U|k^0\rangle|^2}{(E_j^0 - E_k^0)^2}\big[\langle k^0|U|k^0\rangle - \langle j^0|U|j^0\rangle\big].
$$

For two fragments, $\langle j_a^0k_b^0|U|j_a^0k_b^0\rangle - \langle j_a^0j_b^0|U|j_a^0j_b^0\rangle = \langle k_b^0|U_b|k_b^0\rangle - \langle j_b^0|U_b|j_b^0\rangle$: fragment $a$ drops out of the bracket, and $A = A_a + A_b$.

**Møller-Plesset form.** With the HF potential, only doubles contribute (Brillouin's theorem, [[brillouin-theorem]]). The bracket reduces to integrals that all share indices with the numerator (J-S Eq. 3.43):

$$
A = \sum_{\substack{a<b\\ i<j}}\frac{|\langle ij||ab\rangle|^2}{(\varepsilon_i + \varepsilon_j - \varepsilon_a - \varepsilon_b)^2}\Big[\langle ab||ab\rangle + \langle ij||ij\rangle - \langle ai||ai\rangle - \langle aj||aj\rangle - \langle bi||bi\rangle - \langle bj||bj\rangle\Big]
$$

(occupied $i, j$; virtual $a, b$; J-S write the last four as $(1 + P_{ab})(1 + P_{ij})\langle ai||ai\rangle$). Written this way, the expression is **linked**: it cannot be split into independent sums. The rest of $E^{(3)}$ ($k\ne l$) is linked as well. MBPT builds on this: it never generates the unlinked pieces in the first place ([[linked-cluster-theorem]]).

!!! example "Water, STO-3G, Szabo's geometry (computed for this note)"
    $A$ from determinant sums over the FCI space, Eq. (3.39): −0.01194124. From the linked orbital formula above: −0.01194124.

## The perturbed wave function

**First order.** Since $Q|j^0\rangle = 0$,

$$
|j^{(1)}\rangle = (E_j^0 - H^0)^{-1}QU|j^0\rangle = \sum_{k\ne j}\frac{\langle k^0|U|j^0\rangle}{E_j^0 - E_k^0}|k^0\rangle .
$$

For two fragments it contains $|k_a^0j_b^0\rangle$ and $|j_a^0k_b^0\rangle$ but not $|k_a^0k_b^0\rangle$. It is **not** a product of fragment wave functions.

**Why the energy is still extensive.** RS evaluates the energy by projection, $E_j = \langle j^0|H|j\rangle$, and $\langle j_a^0j_b^0|H|k_a^0k_b^0\rangle = 0$, so the missing simultaneous excitations cannot matter at this order. Using the same $|j^0\rangle + |j^{(1)}\rangle$ in the expectation value $\langle j|H|j\rangle/\langle j|j\rangle$ would not be size consistent. A variational method (CI, MCSCF) must include $|k_a^0k_b^0\rangle$ explicitly, e.g. $1\sigma_g^{-2}1\sigma_u^2$ excitations on both of two H₂ molecules. This is the excitation-level problem of truncated CI ([[size-consistency]]).

## The Møller-Plesset wave function

**MP partitioning.** Take $V$ as the HF potential of the reference determinant, $V = \sum_{kl}\sum_{\mu\in j^0}\langle k\mu||l\mu\rangle k^\dagger l$. Then $H^0 = \sum_k\varepsilon_kk^\dagger k$ with HF orbital energies, $E^{(1)} = -\tfrac12\sum_{\mu\nu}\langle\mu\nu||\mu\nu\rangle$, and $E^{(2)}$ is [[mp2]].

**First order.** Only doubles, by Brillouin's theorem:

$$
|j^{(1)}\rangle = \sum_{i<j,\,a<b}\frac{\langle ab||ij\rangle}{\varepsilon_i + \varepsilon_j - \varepsilon_a - \varepsilon_b}\,a^\dagger b^\dagger j\,i\,|j^0\rangle .
$$

**Second order.** Singles, doubles, triples and quadruples (J-S Eq. 3.54). The singles are driven by the first-order doubles (spin orbitals; standard form, equivalent to J-S Eq. 3.55):

$$
t_i^{a(2)}(\varepsilon_i - \varepsilon_a) = \tfrac12\sum_{jbc}\langle aj||bc\rangle t_{ij}^{bc} - \tfrac12\sum_{jkb}\langle jk||ib\rangle t_{jk}^{ab},\qquad t_{ij}^{ab} = \frac{\langle ab||ij\rangle}{\varepsilon_i + \varepsilon_j - \varepsilon_a - \varepsilon_b} .
$$

The quadruples are the disconnected products of first-order doubles that $|j^{(1)}\rangle$ lacks (general knowledge; this is how the RS wave function catches up with the product form, order by order).

!!! example "Water, STO-3G: content of the MP wave function (computed for this note)"
    Exact RS recursion in the full determinant space (441 determinants), $|j^{(1)}\rangle = R\,U|j^0\rangle$ and $|j^{(2)}\rangle = R\,(U - E^{(1)})|j^{(1)}\rangle$ with $R = Q(E_j^0 - H^0)^{-1}$.

    | Excitation level | $\lVert j^{(1)}\rVert^2$ | $\lVert j^{(2)}\rVert^2$ |
    |---|---:|---:|
    | Singles | 0 | 8.586 × 10⁻⁵ |
    | Doubles | 1.312 × 10⁻² | 1.137 × 10⁻³ |
    | Triples | 0 | 1.211 × 10⁻⁵ |
    | Quadruples | 0 | 4.068 × 10⁻⁵ |

    - **Checks.** The singles formula above gives 8.585611 × 10⁻⁵ against 8.585611 × 10⁻⁵ from the recursion. $\langle j^0|U|j^{(1)}\rangle$ = −0.03549932, which equals PySCF's MP2. $\langle j^0|U|j^{(2)}\rangle$ = −0.00959218, the third-order energy.
    - **Consequence.** Singles, triples and quadruples first affect the energy in fourth order ($E^{(4)}$ needs $|j^{(2)}\rangle$). Fourth order is therefore the first with singles, triples and quadruples contributions, and doubles-only resummations such as D-MBPT(∞) are exact only through third order ([[linked-cluster-theorem]]).

## HeH⁺ (J-S Problem 3.1)

!!! example "Second-order RS for minimal-basis HeH⁺ (computed for this note; J-S in parentheses)"
    - **First order.** $|1\sigma^2\rangle^{(1)} = \frac{\langle22|11\rangle}{2(\varepsilon_1 - \varepsilon_2)}|2\sigma^2\rangle = -0.0442|2\sigma^2\rangle$ (same). $|1\sigma2\sigma\rangle$ is absent by Brillouin's theorem.
    - **Normalized.** $0.9990|1\sigma^2\rangle - 0.0442|2\sigma^2\rangle$ (J-S 0.9990, −0.0441). The two-configuration CI gives 0.9984 and −0.0556 (J-S Problem 2.3); first order underestimates the double-excitation coefficient by about 20%.
    - **Energies.** $E^{(2)} = -0.005576$ (−0.0056). Two-configuration CI −0.007030 (−0.0070); full CI −0.007245 (−0.0072).
    - **n ions.** Integrals between different ions vanish, so $E^{(2)}$ is a sum over ions.

## Limits

**Near degeneracy.** RS (and MBPT) fail when some $E_k^0$ approaches $E_j^0$ or when the fluctuation potential is not small, e.g. in bond breaking.

**Size consistency is not proper dissociation.** MBPT gives $n$ times the energy of $n$ separated LiH molecules at equilibrium. It still cannot dissociate one LiH from the $1\sigma^22\sigma^2$ reference, which goes to ionic fragments. The configuration needed for neutral atoms is present in the MBPT wave function, but its amplitude, which dominates at large $R$, is not obtained correctly at any low order. Proper dissociation needs the right configurations **and** a method that can make them dominant (J-S, Sec. G; see also [[h2-dissociation-rhf-uhf]]).

## Source

Jørgensen and Simons, *Second Quantization-Based Methods in Quantum Chemistry* (Academic Press, New York, 1981), Ch. 3, Secs. A-F and end of Sec. G, pp. 68-78, 84-85, Eqs. (3.1)-(3.55); Problem 3.1 with Solution, pp. 85-87. The singles formula is written in its standard spin-orbital form (J-S Eq. 3.55 is partly illegible in the scan). The remark on quadruples as products is general knowledge. All numbers computed for this note (water with PySCF 2.14).
