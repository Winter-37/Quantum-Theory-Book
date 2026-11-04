---
id: linked-cluster-theorem
title: Size consistency of Møller-Plesset theory, Hugenholtz and Goldstone diagrams, and the linked-cluster theorem
summary: For N noninteracting H2 molecules the third-order RS energy contains a renormalization term growing as N², cancelled exactly by part of the other term (Brueckner's cancellation, verified numerically). Goldstone's linked-cluster theorem guarantees this in every order: only linked diagrams survive. Rules for Hugenholtz and Goldstone diagrams, how the second- and third-order energies follow from them, and the infinite-order sums that give the Epstein-Nesbet and D-MBPT(∞) = L-CCD energies. Jørgensen and Simons' Brandow-diagram rules with a general one-electron potential, the cancellation of Hartree-Fock potential diagrams, wave-function diagrams, and the third-order diagrams for HeH⁺.
status: in-progress
kind: theory
level: advanced
tags: [linked-cluster-theorem, size-consistency, goldstone-diagrams, hugenholtz-diagrams, mbpt, resummation, d-mbpt, brandow-diagrams]
prerequisites: [mp2, mp3, size-consistency]
related: [rayleigh-schrodinger-perturbation-theory, coupled-pair-approximations, iepa, coupled-cluster-second-quantization, orbital-perturbation-theory, perturbation-theory-second-quantization, mp2, mp3]
also: []
date: 2026-11-03
---

## Brueckner's problem

**History (as told by Szabo).** Brueckner, working on infinite nuclear matter, noticed that the RS energy expressions contain terms proportional to the square of the number of particles and showed that these cancel through sixth order. Goldstone, using Feynman-style diagrams, proved the cancellation in all orders: the linked-cluster theorem. Kelly first applied these diagrammatic methods to atoms, summing selected diagram classes to infinite order.

## The cancellation in the N-H₂ model

**Model.** $N$ minimal-basis H$_2$ molecules, all intermolecular integrals zero ([[size-consistency]]), Møller-Plesset partition ([[mp2]]).

**First and second order.** $E^{(0)} = 2N\varepsilon_1$, $E^{(1)} = -NJ_{11}$, and only the $N$ local doubles contribute to second order:

$$
E^{(2)} = \frac{NK_{12}^2}{2(\varepsilon_1 - \varepsilon_2)} .
$$

Both are $N$ times the monomer values.

**Third order.** $E^{(3)} = A^{(3)} + B^{(3)}$ ([[rayleigh-schrodinger-perturbation-theory]]).

- **The renormalization term grows as $N^2$:**

$$
B^{(3)} = -E^{(1)}\sum_n{}'\frac{|V_{0n}|^2}{(E_0^{(0)} - E_n^{(0)})^2} = NJ_{11}\cdot\frac{NK_{12}^2}{4(\varepsilon_1 - \varepsilon_2)^2} .
$$

- **The other term contains a compensating piece.** Only diagonal elements between local doubles survive, and

$$
\langle\Psi_{1_i\bar1_i}^{2_i\bar2_i}|\mathscr V|\Psi_{1_i\bar1_i}^{2_i\bar2_i}\rangle = -NJ_{11} + J_{11} + J_{22} - 4J_{12} + 2K_{12},
$$

because the doubly excited determinant still "sees" the Hartree-Fock potential of all other molecules. Hence

$$
A^{(3)} = -\frac{N^2J_{11}K_{12}^2}{4(\varepsilon_1 - \varepsilon_2)^2} + \frac{NK_{12}^2(J_{11} + J_{22} - 4J_{12} + 2K_{12})}{4(\varepsilon_1 - \varepsilon_2)^2}.
$$

- **Sum.** The $N^2$ terms cancel and $E^{(3)}$ is $N$ times the monomer third-order energy of [[mp3]].

!!! example "Separated H₂ molecules, STO-3G, R = 1.4 bohr, molecules 100 bohr apart (computed for this note)"
    Hartree; $B^{(3)}$ evaluated as $-E^{(1)}\cdot\tfrac14\sum|\langle ab||rs\rangle|^2/D^2$, $A^{(3)} = E^{(3)} - B^{(3)}$.

    | $N$ | $E^{(2)}$ | $E^{(3)}$ | $B^{(3)}$ | $A^{(3)}$ |
    |---:|---:|---:|---:|---:|
    | 1 | −0.013158 | −0.004846 | 0.003555 | −0.008401 |
    | 2 | −0.026316 | −0.009692 | 0.014641 | −0.024333 |
    | 3 | −0.039474 | −0.014539 | 0.033574 | −0.048113 |
    | 4 | −0.052631 | −0.019385 | 0.060531 | −0.079916 |

    - **$E^{(2)}$ and $E^{(3)}$** are exactly linear in $N$.
    - **$B^{(3)}$** grows roughly as $N^2$ (ratios 4.1, 9.4, 17.0 against 4, 9, 16). The small excess comes from the Coulomb tails between molecules 100 bohr apart, which make $E^{(1)}$ slightly more negative than $-NJ_{11}$.
    - **$A^{(3)}$** contains the same superlinear growth with opposite sign.

## Hugenholtz diagrams

**Construction (Szabo Sec. 6.7.1).** With a two-body perturbation each dot carries four lines (two in, two out). For order $n$, connect $n$ vertically ordered dots so that each diagram is linked and distinct, and, because of Brillouin's theorem, no line starts and ends on the same dot when there is more than one dot. There is one second-order diagram, three third-order diagrams and twelve fourth-order skeletons.

**Translation rules.**

1. Each dot gives $\langle\text{in}_1\,\text{in}_2||\text{out}_1\,\text{out}_2\rangle$ (the order within the pair is arbitrary).
2. Each gap between adjacent dots gives $\sum\varepsilon_{\text{holes}} - \sum\varepsilon_{\text{particles}}$ over the lines crossing it.
3. Sign $(-1)^{h+l}$: $h$ hole lines, $l$ closed loops. Here $l$ is found from the written string of integrals: follow a label from a bra position to the matching ket position ($i\to k$, $j\to l$ in $\langle ij||kl\rangle$) until it returns; $l$ is the number of such cycles needed to use up all labels.
4. Sum over all labels.
5. Multiply by $2^{-k}$, $k$ = number of pairs of equivalent lines (same start, same end, same direction).

**Second order.** Two hole lines, two pairs of equivalent lines ($r,s$ and $a,b$), and $l=2$ for the string $\langle ab||rs\rangle\langle rs||ab\rangle$: the result is $\tfrac14\sum|\langle ab||rs\rangle|^2/(\varepsilon_a + \varepsilon_b - \varepsilon_r - \varepsilon_s)$, which is [[mp2]]. Writing the string as $\langle ab||rs\rangle\langle sr||ab\rangle$ instead gives $l = 1$ and an opposite sign that compensates $\langle sr||ab\rangle = -\langle rs||ab\rangle$.

**Third order.** The three diagrams give the hole ladder ($l = 2$), particle ladder ($l = 2$) and ring ($l = 3$) terms of [[mp3]], with weights $\tfrac18$, $\tfrac18$ and 1.

## Goldstone diagrams

**Construction (Szabo Sec. 6.7.2).** Pull each Hugenholtz dot apart into a dashed interaction line with one line in and one out at each end. Matrix elements become ordinary integrals $\langle\text{left in, right in}|\text{left out, right out}\rangle$, and the number of closed loops can be read off the picture. There are more Goldstone diagrams than Hugenholtz diagrams: two at second order (direct and exchange) and twelve at third order (Szabo Table 6.2).

**Rules.** Same denominators and sign $(-1)^{h+l}$, sum over labels, a factor $\tfrac12$ for diagrams with a mirror plane perpendicular to the page, and for closed shells $\sum_{\text{spin orbitals}} = 2^l\sum_{\text{spatial}}$. The direct second-order diagram has $h = 2$, $l = 2$ and weight $\tfrac12$; the exchange diagram $h = 2$, $l = 1$, weight $\tfrac12$. Together they give the two terms of the closed-shell MP2 formula.

## The linked-cluster theorem

**Statement.** Algebraic terms that grow as $N^2$ (or faster) correspond to **unlinked** diagrams, made of disconnected pieces. Goldstone proved, with time-dependent techniques, that unlinked diagrams cancel in every order. The $n$th-order energy is the sum of linked diagrams only. Each linked diagram is a connected cluster of interactions, and for separated fragments its value is a sum over fragments. Therefore every finite order of MBPT is size consistent.

**What "size consistent" means here.** Szabo uses the term for energies that grow linearly with the number of particles. A supermolecule energy equals $N$ times the monomer energy only when the method is also invariant to rotations of degenerate orbitals; MBPT is ([[iepa]] for a counterexample).

**Connection to coupled cluster (general knowledge, consistent with J-S Ch. 4).** The similarity-transformed form $e^{-\hat T}He^{\hat T}$ produces only connected (linked) terms, which is why coupled cluster is size consistent ([[coupled-cluster-second-quantization]]).

## Summing diagram classes to infinite order

**Epstein-Nesbet.** Start from the second-order direct and exchange diagrams and insert interactions that leave the labels on each crossed line unchanged (diagonal insertions: hole-hole, particle-particle, hole-particle). The values form a geometric series, exactly as in the two-state problem of [[rayleigh-schrodinger-perturbation-theory]]:

$$
\frac{|\langle ab||rs\rangle|^2}{\varepsilon_a + \varepsilon_b - \varepsilon_r - \varepsilon_s}\to
\frac{|\langle ab||rs\rangle|^2}{\langle\Psi_0|H|\Psi_0\rangle - \langle\Psi_{ab}^{rs}|H|\Psi_{ab}^{rs}\rangle},
\qquad
E_{\text{corr}}(\text{EN}) = \sum_{a<b,\,r<s}\frac{|\langle ab||rs\rangle|^2}{E_0 - \langle\Psi_{ab}^{rs}|H|\Psi_{ab}^{rs}\rangle} .
$$

This is the Epstein-Nesbet pair energy of [[iepa]]: a resummation that is equivalent to second order with a repartitioned $\mathscr H_0$.

**D-MBPT(∞).** Sum all diagrams in which every horizontal cut crosses exactly two holes and two particles (doubles-only intermediate states). The result is Bartlett's D-MBPT(∞):

$$
E_{\text{corr}}(\text{D-MBPT}(\infty)) = -\mathbf b^\dagger\mathbf D^{-1}\mathbf b,
\qquad (\mathbf b)_{rs,ab} = \langle\Psi_{ab}^{rs}|H|\Psi_0\rangle,\ \ (\mathbf D)_{rsab,tucd} = \langle\Psi_{ab}^{rs}|H - E_0|\Psi_{cd}^{tu}\rangle,
$$

identical to linear CCA (L-CCD) of [[coupled-pair-approximations]]. Keeping only the diagonal of $\mathbf D$ gives EN back. Unlike EN, D-MBPT(∞) is exact through third order; at fourth order it lacks the singles, triples and quadruples contributions. CCD restores the quadruples (as products of doubles); singles and triples need $\hat T_1$ and $\hat T_3$.

!!! example "Water, STO-3G and 6-31G (computed for this note)"
    | Method | STO-3G | 6-31G |
    |---|---:|---:|
    | MP2 + MP3 | −0.045091 | −0.130383 |
    | EN (diagonal sum) | −0.053812 | −0.170842 |
    | D-MBPT(∞) = L-CCD | −0.049811 | −0.134824 |
    | CCD | −0.049122 | −0.134648 |
    | Full CI | −0.049486 | −0.136848 |

    The diagonal (EN) resummation overshoots badly; the full doubles resummation is close to CCD.

## Jørgensen and Simons' version: Brandow diagrams

**Two kinds of vertex.** J-S keep a general one-electron potential, $U = W - V$ ([[perturbation-theory-second-quantization]]). A Hugenholtz diagram then has dots for $W$ (two lines in, two out) and one-ended solid lines for $-V$ (one line in, one out). For order $n$, draw $m$ dots and $n - m$ potential vertices, $m = 0, \ldots, n$, in all time orders, and connect them in all distinct **linked** ways.

**Evaluation via Brandow diagrams.** To evaluate a Hugenholtz diagram, stretch each dot into a dashed line with one line in and one out at each end. Brandow diagrams are antisymmetrized Goldstone diagrams: every Brandow form of a Hugenholtz diagram has the same value. J-S's Table II:

1. Label down-going lines as holes, up-going lines as particles. A line that starts and ends at the same interaction is a hole.
2. Numerator: $\langle\text{out}|{-V}|\text{in}\rangle$ for each potential vertex and $\langle\text{left out, right out}||\text{left in, right in}\rangle$ for each interaction.
3. Denominator: for each of the $n - 1$ gaps between successive vertices, $\sum\varepsilon_{\text{holes}} - \sum\varepsilon_{\text{particles}}$ over the lines crossing it.
4. Factor $(\tfrac12)^k$ for $k$ equivalent pairs of lines.
5. Sign $(-1)^{h+l}$, with $h$ hole lines and $l$ closed loops (traced along the arrows without crossing a dashed line).
6. Sum over all labels.

Two Brandow forms of one third-order Hugenholtz diagram (J-S Fig. 3.2 A and E) differ in loop count by one. They give the same value because interchanging two labels in one antisymmetrized integral supplies the compensating sign.

**Unlinked diagrams.** J-S Fig. 3.3A, a first-order potential diagram multiplied by a disjoint first-order interaction loop, is a product of two independent sums. For $n$ fragments each sum is proportional to $n$, so the product is not size consistent: unlinked diagrams are exactly the unlinked terms of RS theory.

**Hartree-Fock potential.** With $V = V^{\mathrm{HF}}$, $\langle p|V^{\mathrm{HF}}|q\rangle = \sum_\mu\langle p\mu||q\mu\rangle$. A $-V$ vertex then cancels a $W$ vertex closed on itself with a hole loop in the same position (J-S Fig. 3.3B, C). This holds in every order beyond first, so with HF orbitals:

- **Energy.** Only the two first-order diagrams ($W$ loop and $-V$ loop, together $-\tfrac12\sum_{\mu\nu}\langle\mu\nu||\mu\nu\rangle$) and the single second-order diagram survive through second order. The latter gives [[mp2]].
- **Wave function.** The first-order singles diagrams cancel the same way. This is Brillouin's theorem in diagram language.

**Wave-function diagrams.** Same rules, except that external (open) lines do not count in $h$. Each external line carries its creation or annihilation operator. The last denominator carries the orbital energies of the open lines.

**A geometric series (J-S Fig. 3.4).** Insert repeated hole-hole interactions $\langle\alpha\beta||\alpha\beta\rangle$ between the two holes of the second-order diagram. Each insertion multiplies by $\langle\alpha\beta||\alpha\beta\rangle/(\varepsilon_\alpha + \varepsilon_\beta - \varepsilon_r - \varepsilon_s)$, and the sum is a shifted denominator:

$$
\tfrac14\sum_{\alpha\beta rs}\frac{|\langle\alpha\beta||rs\rangle|^2}{\varepsilon_\alpha + \varepsilon_\beta - \varepsilon_r - \varepsilon_s - \langle\alpha\beta||\alpha\beta\rangle} .
$$

This is part of the Epstein-Nesbet shift above. For HeH⁺, its third-order term is the whole hole-hole ladder (0.001875, below), and the resummed value is −0.004174.

!!! example "Third-order MBPT for minimal-basis HeH⁺ (J-S Problem 3.2; computed for this note, J-S in parentheses)"
    With HF orbitals, the only surviving third-order Brandow diagrams are the particle ladder, the hole ladder and the ring (J-S Fig. 3.7). In the two-orbital model:

    | Diagram | Closed-shell value | Hartree |
    |---|---|---:|
    | Particle ladder | $K_{12}^2J_{22}/4(\varepsilon_1 - \varepsilon_2)^2$ | 0.001203 (0.0012) |
    | Hole ladder | $K_{12}^2J_{11}/4(\varepsilon_1 - \varepsilon_2)^2$ | 0.001875 (0.0019) |
    | Ring | $K_{12}^2(2K_{12} - 4J_{12})/4(\varepsilon_1 - \varepsilon_2)^2$ | −0.004245 (−0.0042) |
    | $E^{(3)}$ | $K_{12}^2(J_{11} + J_{22} - 4J_{12} + 2K_{12})/4(\varepsilon_1 - \varepsilon_2)^2$ | −0.001167 (−0.0011) |

    - **Totals.** $E^{(2)} + E^{(3)} = -0.006743$ (−0.0067), against full CI −0.007245 (−0.0072). The third order recovers 70% of what second order misses.
    - **Formula.** The total is the same closed form as for H₂ in [[mp3]].

**Size consistency is not proper dissociation.** MBPT is size consistent order by order but, built on one determinant, it can still dissociate a single molecule wrongly (J-S's LiH example; [[perturbation-theory-second-quantization]]).

## Source

Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996; reprint of the revised first edition, McGraw-Hill, 1989), Chapter 6 introduction, pp. 320-322; Sec. 6.6, pp. 354-356, Eqs. (6.79)-(6.92); Sec. 6.7, pp. 356-370, Hugenholtz rules H1-H5, Goldstone rules G1-G6, Table 6.2, Eqs. (6.93)-(6.95), Ex. 6.11-6.13. The coupled-cluster remark is general knowledge (consistent with Jørgensen and Simons, Ch. 4, p. 94). Jørgensen and Simons, *Second Quantization-Based Methods in Quantum Chemistry* (Academic Press, New York, 1981), Ch. 3, Sec. G, pp. 78-85, Eqs. (3.56)-(3.71), Tables I-II, Figs. 3.1-3.7; Problem 3.2 with Solution, pp. 86-89. Numbers computed for this note.
