---
id: coupled-cluster-diagrams
title: Coupled-cluster diagrams - operator vertices, interpretation rules (labels, ½ per equivalent line pair, 1/n! per equivalent vertex set, P(pq) per inequivalent external pair), the Kucharski-Bartlett sign sequence, topology names, linked versus unlinked, and cost from line counts
summary: CC diagrams turn each term of ⟨Φ₀|, ⟨Φ_i^a| or ⟨Φ_ij^ab| (Ĥ_N e^T)_c|Φ₀⟩ into a picture. F_N and V_N are dashed interaction lines and T_n are solid ones. Upward lines are particles, downward lines are holes, and the picture is read bottom to top for right to left in the matrix element. The algebra follows from a short rule list: label lines; sum over internal lines; read integrals as ⟨left-out right-out||left-in right-in⟩ and amplitudes as t_in^out; the sign is (−1)^{h+l}; ½ for each pair of equivalent lines; 1/n! for n equivalent T vertices; P(pq) for each pair of inequivalent external lines. The Kucharski-Bartlett sign sequence enumerates the distinct connections without double counting. For ½V_N T₁² T₂ in the doubles equation it gives five diagrams, which I confirmed by brute-force enumeration. The rules reproduce the three CCSD energy terms with their ¼ and ½ factors. The cost of a term is o^{n_h} v^{n_p}, with n_h and n_p the distinct hole and particle labels on the diagram, so the particle-particle ladder is o²v⁴. Unlinked diagrams appear in CI, from the E_corr·c terms, but never in CC, which is the diagrammatic statement of CC size-extensivity.
status: in-progress
kind: reference
level: advanced
tags: [coupled-cluster, diagrams, hugenholtz, goldstone, size-extensivity, ccsd, cost]
prerequisites: [normal-ordering-and-wicks-theorem, ccsd-spin-orbital-equations]
related: [linked-cluster-theorem, coupled-cluster-hierarchy-and-size-extensivity, ci-size-extensivity-and-excitation-levels, perturbative-triples-cc2-cc3, coupled-cluster-second-quantization]
also: []
date: 2026-11-07
---

## What a diagram represents

**What is drawn.** Every term of a CC equation is a fully contracted matrix element:

$$
\langle\Phi_0|(\hat H_N e^{\hat T})_c|\Phi_0\rangle,\qquad
\langle\Phi_i^a|(\hat H_N e^{\hat T})_c|\Phi_0\rangle,\qquad
\langle\Phi_{ij}^{ab}|(\hat H_N e^{\hat T})_c|\Phi_0\rangle,
$$

where the subscript $c$ means connected. The generalized Wick theorem ([[normal-ordering-and-wicks-theorem]]) decides which contractions exist. A diagram is a picture of one such pattern of contractions.

**Ingredients** (Crawford, ESQC 2026, part 2):

- **Lines.** Hole lines (occupied, $i,j,\dots$) point down and particle lines (virtual, $a,b,\dots$) point up. A line is a contraction, or an uncontracted external index.
- **Interaction lines.** $\hat F_N$ is a dashed line with one vertex and $\hat V_N$ a dashed line with two vertices, or one Hugenholtz dot in the antisymmetrized form. $\hat T_n$ is a solid line with $n$ particle-hole pairs leaving it upward. Every line of $\hat T_n$ points out of it, because $\hat T$ contains only quasi-creators.
- **Excitation level.** For an operator component, it is half the number of lines above the interaction line minus the number below. $\hat V_N$ has components from $-2$ to $+2$, $\hat F_N$ from $-1$ to $+1$, and $\hat T_n$ has $+n$.
- **Reading order.** Bottom to top in the diagram is right to left in the matrix element. The $\hat T$ vertices sit at the bottom, $\hat H_N$ above them, and a bra $\langle\Phi_{ij\dots}^{ab\dots}|$ leaves its lines open at the top.

## Interpretation rules

**Rules 1-3: labels, summations, matrix elements.**

1. **Labels.** Label every line with a hole or particle index.
2. **Summation.** Sum over every *internal* line, i.e. a line that starts and ends on interaction lines. External lines carry the indices of the bra.
3. **Matrix elements.**
    - $\hat F_N$ vertex: $f_{\text{out},\text{in}}$.
    - $\hat V_N$ vertex: $\langle\text{left-out}\;\text{right-out}||\text{left-in}\;\text{right-in}\rangle$.
    - $\hat T_n$ vertex: $t_{\text{in}\cdots}^{\text{out}\cdots}$ read left to right, holes as subscripts and particles as superscripts.

**Rules 4-7: sign and weight factors.**

4. **Sign** $(-1)^{h+l}$, with $h$ the number of internal hole lines and $l$ the number of closed loops. Loops are counted on a Goldstone (non-antisymmetrized) representative of the Hugenholtz diagram. For *open* diagrams the external lines must be paired into quasi-loops before counting. The convention for that is in Shavitt-Bartlett (chapter to add). Here I check signs against the algebraic equations of [[ccsd-spin-orbital-equations]] instead of relying on it.
5. **Equivalent lines.** Two lines that leave the same interaction line and end together on another, in the same direction, contribute a factor $\tfrac12$.
6. **Equivalent vertices.** $n$ identical $\hat T$ operators that connect to $\hat H_N$ in exactly the same way contribute $1/n!$. This absorbs the $1/n!$ of $e^{\hat T}$.
7. **Permutations.** Each pair of external lines of the same kind (two holes or two particles) that end on *different* interaction lines introduces $P(pq)$, with $P(pq)X_{pq}=X_{pq}-X_{qp}$. This restores the antisymmetry of $t_{ij}^{ab}$.

!!! example "The three CCSD energy diagrams"
    | Diagram | Lines | Rules applied | Term |
    |---|---|---|---|
    | $\hat F_N$ over $\hat T_1$ | $i$ (hole) and $a$ (particle), both internal | $h=1$, $l=1$ gives $+$; no equivalences | $\sum f_{ia}t_i^a$ |
    | $\hat V_N$ over $\hat T_2$ | $i,j$ and $a,b$, all running from $\hat T_2$ to $\hat V_N$ | two equivalent pairs give $\tfrac12\cdot\tfrac12$; $h=2$, $l=2$ gives $+$ | $\tfrac14\sum\langle ij||ab\rangle t_{ij}^{ab}$ |
    | $\hat V_N$ over $\hat T_1\hat T_1$ | $(i,a)$ to one $\hat T_1$, $(j,b)$ to the other | no equivalent lines; two equivalent vertices give $\tfrac1{2!}$; $h=2$, $l=2$ gives $+$ | $\tfrac12\sum\langle ij||ab\rangle t_i^at_j^b$ |

    These are exactly the three terms of the CCSD energy, $E_{\text{CC}} = \sum f_{ia}t_i^a + \tfrac14\sum\langle ij||ab\rangle t_{ij}^{ab} + \tfrac12\sum\langle ij||ab\rangle t_i^at_j^b$.

## Enumerating distinct diagrams: the sign sequence

**The problem.** For a product such as $\tfrac12\hat V_N\hat T_1^2\hat T_2$ projected on $\langle\Phi_{ij}^{ab}|$, it is easy to draw the same diagram twice or miss one.

**Kucharski and Bartlett's bookkeeping.**

- **Required component of $\hat H_N$.** The $\hat T$'s give excitation level $1+1+2=4$ and the bra needs 2, so only the $-2$ component of $\hat V_N$ can contribute. It has four lines below its vertex, two particle (+) and two hole (−).
- **Labels on the $\hat T$ lines.** Mark every line leaving a $\hat T$ as + (particle) or − (hole). $\hat T_1$ has $(+,-)$ and $\hat T_2$ has $(+,+,-,-)$.
- **Choices.** Choose which lines of each $\hat T$ go up to $\hat V_N$: two + and two − in total, **at least one line from every $\hat T$** (connectedness), and count the two $\hat T_1$'s as interchangeable.

!!! example "½ V_N T₁² T₂ into the doubles equation: how many diagrams? (computed for this note)"
    Brute-force enumeration of (lines from $T_1$, lines from $T_1'$, lines from $T_2$), each as (particles, holes), unordered in the two $T_1$:

    | $T_1$ | $T_1'$ | $T_2$ |
    |---|---|---|
    | $(0,1)$ | $(0,1)$ | $(2,0)$ |
    | $(0,1)$ | $(1,0)$ | $(1,1)$ |
    | $(0,1)$ | $(1,1)$ | $(1,0)$ |
    | $(1,0)$ | $(1,0)$ | $(0,2)$ |
    | $(1,0)$ | $(1,1)$ | $(0,1)$ |

    There are **five** distinct diagrams, in agreement with Crawford's count. Lines not sent to $\hat V_N$ become the external $i,j,a,b$: each row leaves two particle and two hole lines open, as it must.

## Names of the common topologies

Linear $\hat T_2$ terms of the doubles equation, as they appear in [[ccsd-spin-orbital-equations]]. Signs and factors are taken from the verified algebraic equations.

| Name | Term | Distinct labels | Cost |
|---|---|---|---|
| particle-particle ladder | $\tfrac12\sum_{ef}\langle ab||ef\rangle t_{ij}^{ef}$ | $i,j$; $a,b,e,f$ | $o^2v^4$ |
| hole-hole ladder | $\tfrac12\sum_{mn}\langle mn||ij\rangle t_{mn}^{ab}$ | $i,j,m,n$; $a,b$ | $o^4v^2$ |
| ring (particle-hole) | $P(ij)P(ab)\sum_{me}\langle mb||ej\rangle t_{im}^{ae}$ | $i,j,m$; $a,b,e$ | $o^3v^3$ |
| Fock insertions | $P(ab)\sum_e f_{be}t_{ij}^{ae}$, $-P(ij)\sum_m f_{mj}t_{im}^{ab}$ | five labels | $o^2v^3$, $o^3v^2$ |

**Cost rule.** A term costs $o^{n_h}v^{n_p}$, with $n_h$ and $n_p$ the numbers of *distinct* hole and particle labels in its diagram. Factorization through intermediates means splitting a diagram into pieces with fewer distinct labels each.

**Example.** The quadratic term $\tfrac14\sum\langle mn||ef\rangle t_{ij}^{ef}t_{mn}^{ab}$ has 8 labels ($o^4v^4$). It is evaluated as $\sum_{mn}t_{mn}^{ab}\big[\sum_{ef}\langle mn||ef\rangle t_{ij}^{ef}\big]$, two steps with 6 labels each ($o^4v^2$).

## Terminology, and why CC is size-extensive

**Terminology.**

- **Open / closed.** With or without external lines.
- **Connected / disconnected.** Whether all parts are joined by directed lines.
- **Linked / unlinked.** Whether the diagram contains a *closed* part not connected to the rest.

**CI versus CC.**

- **CI.** The amplitude equations are $E_{\text{corr}}c_{ij}^{ab} = \langle\Phi_{ij}^{ab}|\hat H_N(1+\hat C)|\Phi_0\rangle$. The left side is a closed piece, the energy, multiplied by an open piece, the coefficient. That is an **unlinked** diagram. The closed part scales with system size independently of the open part, so truncated CI energies do not scale linearly with the number of non-interacting fragments ([[ci-size-extensivity-and-excitation-levels]]).
- **CC.** The equations $0 = \langle\Phi_{ij}^{ab}|(\hat H_N e^{\hat T})_c|\Phi_0\rangle$ contain only connected, hence linked, diagrams. Truncated CC is therefore size-extensive at every level ([[coupled-cluster-hierarchy-and-size-extensivity]]).
- **Relation to MBPT.** This is the same mechanism as Goldstone's linked-cluster theorem ([[linked-cluster-theorem]]).

## Not done here

**Figures.** No drawings are included yet. The rules and tables stand alone, but the vertex pictures are in Crawford's slides and in Shavitt-Bartlett.

**Open-diagram sign rule.** It is stated only by reference (rule 4).

## Source

T. D. Crawford, *Coupled Cluster Theory*, ESQC 2026 lecture slides, part 2 (sections "Diagrams: the basics", "matrix elements", "the CC energy", "the CC amplitude equations", "Common diagram terminology", "Size extensivity", "Computational cost").

T. D. Crawford and H. F. Schaefer, *Rev. Comput. Chem.* **14**, 33-136 (2000), doi:10.1002/9780470125915.ch2.

I. Shavitt and R. J. Bartlett, *Many-Body Methods in Chemistry and Physics* (Cambridge University Press, 2009): chapters on diagrammatic CC (chapter/page numbers to add).

The sign-sequence bookkeeping is due to S. A. Kucharski and R. J. Bartlett (original reference to add; it is cited in Crawford-Schaefer).

Enumeration: `esqc/cc/sign_sequence.py`.
