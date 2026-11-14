---
id: selected-ci-analytic-gradient
title: The selected-CI analytic gradient - a truncated list is not invariant, so every orbital pair responds
summary: A CI in a fixed, truncated list of determinants is not invariant to occupied-occupied or virtual-virtual rotations, because each determinant names specific orbitals. Its gradient therefore needs the canonical-orbital response U^x_pq for those pairs as well, at a cost of 1/(ε_q − ε_p) per pair. Following Coe (2023), the extra pairs fold into one modified Z-vector solve. Pairs in different irreducible representations of an abelian group never contribute, so symmetry-required degeneracies are harmless. Verified on water (STO-3G) to 1×10⁻⁸ E_h/bohr against finite differences. Dropping the oo/vv response gives errors up to 6×10⁻² E_h/bohr and a net torque, but no net force.
status: in-progress
kind: derivation
level: advanced
tags: [analytic-gradients, selected-CI, configuration-interaction, orbital-response, canonical-orbitals, z-vector, cphf, symmetry]
prerequisites: [ci-analytic-gradient, z-vector-method, cphf-closed-shell, derivative-integrals-and-u-matrices]
related: [coe-2023-sci-gradient, sample-based-quantum-diagonalization, generalized-fock-matrix-and-orbital-hessian, cpci-and-ci-hessian]
order: 85
date: 2026-11-09
---

Notation as in [[ci-analytic-gradient]]: RHF canonical orbitals with energies $\varepsilon_p$; $i,j,k,l$ occupied, $a,b$ virtual, $p,q,r,s,m$ general; $x$ a nuclear coordinate. $U^x_{pq}$ is the coefficient of $\phi_p$ in $\partial\phi_q/\partial x$; $S^x$, $h^x$, $(pq|rs)^x$ are skeleton (AO-derivative) integrals in the MO basis; $X_{pq} = F_{qp}$ is the CI Lagrangian (the transposed generalized Fock matrix); $\mathbf M\mathbf U^x_{\rm vo} = \mathbf B^x$ is the CPHF system of [[cphf-closed-shell]]. Coe's $\Delta F_{pq} = F_{pq}-F_{qp}$ equals $X_{qp}-X_{pq}$ here.

## Why a truncated list breaks the invariance

**Selected CI.** The wave function is $\Psi = \sum_{I\in\mathcal S}c_I\Phi_I$, with $\mathcal S$ a list of determinants chosen by some criterion (perturbative, stochastic, sampled from a quantum device) and $c$ the lowest eigenvector of $\mathbf H$ restricted to $\mathcal S$. For a gradient, $\mathcal S$ is fixed: at every geometry the same occupation strings are used, read in that geometry's canonical orbitals.

**What the bits name.** A determinant is a list of occupied orbitals. A rotation between two occupied orbitals $i$ and $j$ maps a determinant containing $i$ but not $j$ onto a combination of itself and the determinant with $j$ instead of $i$. If that partner is missing from $\mathcal S$, the rotated span differs from the original and the energy changes. The energy is invariant to a rotation only when $\mathcal S$ is closed under it.

| CI space | oo rotations | vv rotations | ov rotations |
|---|---|---|---|
| FCI, no frozen orbitals | invariant | invariant | invariant |
| CISD (or any excitation-level truncation), all electrons | invariant | invariant | not invariant |
| frozen-core CI or CASCI | core-valence not invariant | active-frozen not invariant | not invariant |
| selected CI | not invariant | not invariant | not invariant |

**Consequence.** As in [[ci-analytic-gradient]], the orbital response enters through the antisymmetric part of $\mathbf X$:

$$
2\sum_{pq}U^x_{pq}X_{pq} = 2\sum_{p>q}K^x_{pq}\,(X_{pq}-X_{qp}) - \sum_{pq}S^x_{pq}W_{pq},
\qquad K^x = U^x + \tfrac12S^x,\quad W = \tfrac12(\mathbf X+\mathbf X^{\mathsf T}).
$$

Each pair with $X_{pq}\neq X_{qp}$ needs its own $U^x_{pq}$. For selected CI these include oo and vv pairs, and there the "symmetric choice" $U^x_{pq} = -\tfrac12S^x_{pq}$ allowed for invariant energies is no longer valid. The orbitals the list is written in are the canonical ones, so $U^x$ must be the response that keeps them canonical.

## The gradient

**Coe, Eqs. 7 and 11.** With the nuclear repulsion added,

$$
\frac{\mathrm dE}{\mathrm dx} = \sum_{pq}D_{pq}h^x_{pq} + \frac12\sum_{pqrs}d_{pqrs}(pq|rs)^x + 2\sum_{pq}U^x_{pq}X_{pq} + \frac{\partial V_{\rm nn}}{\partial x}.
$$

The CI coefficients still drop out, because $c$ is variational in $\mathcal S$; the RDMs $D$, $d$ depend only on $c$ and the occupation strings.

**The canonical-orbital response for oo and vv pairs.** The orbitals satisfy $F_{pq}(x) = 0$ for $p\neq q$ at every geometry. Differentiate with the total Fock derivative of [[derivative-integrals-and-u-matrices]]:

$$
\frac{\mathrm dF_{pq}}{\mathrm dx} = F^x_{pq} + U^x_{qp}\varepsilon_q + U^x_{pq}\varepsilon_p + \sum_{k}\sum_{l\in\rm occ}U^x_{kl}A_{pq,kl} = 0,
\qquad A_{pq,kl} = 4(pq|kl) - (pk|ql) - (pl|qk),
$$

with $F^x$ the skeleton Fock derivative. Orthonormality gives $U^x_{qp} = -U^x_{pq} - S^x_{pq}$. For $p\neq q$ both occupied or both virtual:

$$
U^x_{pq} = \frac{F^x_{pq} - \varepsilon_qS^x_{pq} + \sum_k\sum_{l\in\rm occ}U^x_{kl}A_{pq,kl}}{\varepsilon_q-\varepsilon_p},
$$

which is Coe's Eq. 13. The sum on the right needs only $U^x_{\rm vo}$ (from CPHF) and the symmetric part of $U^x_{\rm oo}$, which is $-\tfrac12S^x_{\rm oo}$, so the oo/vv elements are explicit once CPHF is solved. Diagonal elements are $U^x_{pp} = -\tfrac12S^x_{pp}$.

## One solve for all coordinates

**The term is linear in $U^x_{\rm vo}$.** Collect the response term as $T^x = T^x_0 + \sum_{ai}l'_{ai}U^x_{ai}$. Here $T^x_0$ is the response term with $U^x_{\rm vo}$ set to zero (it contains $S^x$ and the explicit part of the oo/vv elements), and

$$
l'_{ai} = 2(X_{ai}-X_{ia}) + 2\sum_{\substack{p>q\\ \text{oo or vv}}}\frac{X_{pq}-X_{qp}}{\varepsilon_q-\varepsilon_p}\,A_{pq,ai}.
$$

The first term is the ordinary CI Lagrangian of [[z-vector-method]]. The second is new: an oo or vv pair reaches the vo block because its $U^x_{pq}$ contains $\sum A\,U^x_{\rm vo}$.

**Z vector (Coe, Eqs. 15-16).** With $\mathbf U^x_{\rm vo} = \mathbf M^{-1}\mathbf B^x$ and $\mathbf M$ symmetric,

$$
\mathbf M\mathbf z' = \mathbf l',\qquad
\frac{\mathrm dE}{\mathrm dx} = \sum_{pq}D_{pq}h^x_{pq} + \frac12\sum_{pqrs}d_{pqrs}(pq|rs)^x + T^x_0 + \mathbf z'\cdot\mathbf B^x + \frac{\partial V_{\rm nn}}{\partial x}.
$$

One CPHF-sized solve serves all $3N$ coordinates, exactly as for CISD; only the right-hand side changes. Coe's $\Delta F'$ is $\mathbf l'$ up to sign and factor conventions. Every remaining term is a contraction of skeleton integrals, so the cost per coordinate is $O(M^4)$ once the 2-RDM is back-transformed to the AO basis (Coe, Eqs. 9 and 17).

## When the denominators are dangerous

**The factor $1/(\varepsilon_q-\varepsilon_p)$.** It multiplies $X_{pq}-X_{qp}$, so a small gap matters only for a pair the list is not invariant to.

**Pairs in different irreducible representations do not contribute (Coe, Sec. 2.4).**

- **The claim.** Take an abelian point group in which every canonical orbital has a definite irrep and $\Psi$ has a definite irrep.
    - **One-body term.** $\gamma_{pq}$ is nonzero only if $p$ and $q$ share an irrep, and $h_{tq}$ only if $t$ and $q$ do. So $\sum_q\gamma_{pq}h_{tq}$ vanishes unless $t$ and $p$ share an irrep.
    - **Two-body term.** The same direct-product argument applies to $\sum_{qrs}\Gamma_{prsq}(tr|qs)$.
- **The consequence.** $F_{tp} = F_{pt} = 0$, and the pair drops out whatever its gap.
- **Exact degeneracies.** In the molecules Coe tested (CO, NH$_3$, square H$_4$, hexagonal H$_6$, CH$_4$), every degeneracy forced by the full point group split into different irreps of the largest abelian subgroup. Exact degeneracies therefore never produced a zero denominator.
- **A caveat for some groups.** This is a property of those groups and their subgroup chains, not a general theorem. A pair of degenerate orbitals that falls into one abelian irrep would still need care.

**Near-degeneracies within one irrep.** These do enter with a small denominator. Coe's tests:

- **NH$_3$.** Distorting it by $10^{-3}$ Å from the planar structure left pairs $1.3\times10^{-4}$ $E_h$ apart. The analytic gradient still agreed with the seminumerical one, but the seminumerical step had to drop to about $10^{-6}$ bohr ($10^{-5}$ bohr gave only qualitative agreement).
- **Scale of the term.** Without the CPHF contribution, that hydrogen gradient component came out about 4.4 times too small.

The analytic result is the exact derivative of the fixed-list surface. A small gap means that surface itself changes quickly. That is a statement about the surface, not a numerical failure of the formula.

## The seminumerical check

**Coe, Eq. 5.** With $D$ and $d$ fixed at the reference geometry,

$$
\frac{\mathrm dE}{\mathrm dx} = \sum_{pq}D_{pq}\frac{\mathrm dh_{pq}}{\mathrm dx} + \frac12\sum_{pqrs}d_{pqrs}\frac{\mathrm d(pq|rs)}{\mathrm dx} + \frac{\partial V_{\rm nn}}{\partial x},
$$

where the total MO-integral derivatives are taken by finite differences of RHF calculations at displaced geometries (canonical orbitals, phases aligned to the reference).

- **Why it is exact up to the step.** At fixed $c$ the energy is $\sum Dh + \tfrac12\sum dg$ in the orbitals of that geometry. Because $c$ is variational, its derivative at fixed $c$ is the full gradient.
- **What it costs.** It needs only one CI calculation, so stochastic selection does no harm. It does need $3N$ (or $6N$, central) SCF runs and integral transformations, $O(3NM^5)$, plus a step size.
- **Its use.** An independent check of an analytic implementation, which is how Coe uses it.

**Hellmann-Feynman is not enough.** The operator-only force $\langle\Psi|\partial\hat H/\partial x|\Psi\rangle$ misses the basis-function and orbital terms. Coe reports it far from the analytic gradient for CO in cc-pVTZ, and it is useless in a minimal basis (table below).

## Worked example

!!! example "Water, STO-3G, R(OH) = 1.95 bohr, HOH = 110° (computed for this note)"
    **Setup.**

    - **Reference.** $E_{\rm RHF} = -74.9570541297$, $E_{\rm FCI} = -75.0160501121$ $E_h$, 441 determinants.
    - **Lists.** Determinants with $|c^{\rm FCI}_I| > \tau$ at this geometry, then frozen by orbital index.
    - **Canonical MOs.** 1a$_1$, 2a$_1$, 1b$_2$, 3a$_1$, 1b$_1$ occupied; 4a$_1$, 2b$_2$ virtual.

    **Antisymmetric part of $\mathbf X$.**

    | $\tau$ | dets | $E-E_{\rm FCI}$ ($E_h$) | max oo | max vv | max vo | pairs in different irreps |
    |---|---:|---:|---:|---:|---:|---:|
    | 0.05 | 6 | $2.6\times10^{-2}$ | $1.8\times10^{-2}$ | $7\times10^{-16}$ | $2.0\times10^{-2}$ | $7\times10^{-15}$ |
    | 0.02 | 17 | $3.6\times10^{-3}$ | $9.3\times10^{-4}$ | $1\times10^{-15}$ | $2.3\times10^{-2}$ | $3\times10^{-15}$ |
    | 0 (FCI) | 441 | 0 | $2\times10^{-15}$ | $1\times10^{-18}$ | $6\times10^{-15}$ | $6\times10^{-15}$ |

    - **Symmetry.** The vv block vanishes because the two virtuals are in different irreps. The nonzero oo elements are between a$_1$ orbitals; the smallest such gap is 0.797 $E_h$ (2a$_1$-3a$_1$).
    - **Complete list.** Every block vanishes, as it must for FCI.

    **Gradient, $\tau = 0.05$ ($E_h$/bohr; O$_z$, H1$_y$, H1$_z$).**

    | Method | O$_z$ | H1$_y$ | H1$_z$ | max dev. from FD |
    |---|---:|---:|---:|---:|
    | Central finite differences of the fixed-list energy (step $10^{-4}$) | 0.033601 | 0.033578 | −0.016801 | — |
    | Explicit $U^x$ for all pairs (9 CPHF solves) | 0.033601 | 0.033578 | −0.016801 | $1.3\times10^{-8}$ |
    | Modified Z vector, one solve | 0.033601 | 0.033578 | −0.016801 | $1.3\times10^{-8}$ |
    | Seminumerical, fixed RDMs | 0.033601 | 0.033578 | −0.016801 | $4\times10^{-10}$ |
    | vo response only (list treated as invariant) | 0.029423 | 0.038667 | −0.014712 | $5.1\times10^{-3}$ |
    | No orbital response at all ($-\sum WS^x$ kept) | 0.010776 | 0.044060 | −0.005388 | $2.3\times10^{-2}$ |
    | Hellmann-Feynman force only | 2.829 | −0.026 | 0.000 | 2.8 |

    - **The oo/vv response.** At $\tau = 0.02$ the vo-only error drops to $2.6\times10^{-4}$, because the oo elements of $\mathbf X - \mathbf X^{\mathsf T}$ shrink with the list's incompleteness. For FCI all variants coincide (to $2\times10^{-9}$).

    **Sum rules at a geometry with no symmetry.**

    - **Geometry.** O at the origin, H at (0.25, 1.55, 1.25) and (−0.15, −1.80, 1.05) bohr.
    - **The lists.** 8 and 19 determinants.
    - **Full gradient.** Agrees with finite differences to $3\times10^{-8}$.
    - **vo-only gradient.** Off by $3.2\times10^{-2}$ and $6.5\times10^{-2}$ $E_h$/bohr.
    - **What the sum rules detect.**
        - **Net force.** $\sum_A\nabla_AE$ is zero to $10^{-15}$ in every variant. Under a rigid translation the canonical MO coefficients do not change, so $\sum_AU^{A}=0$ and $\sum_AS^{A}=0$ in every block, and the omitted term cancels.
        - **Net torque.** $\sum_A\mathbf R_A\times\nabla_AE$ is $10^{-12}$ for the full gradient but $9\times10^{-4}$ and $4\times10^{-3}$ $E_h$ without the oo/vv response.
    - **Which test to use.** The translational sum rule cannot detect a missing oo/vv term; the rotational one can.

## Source

- J. P. Coe, "Analytic gradients for selected configuration interaction", *J. Chem. Theory Comput.* **19**, 874 (2023), doi:10.1021/acs.jctc.2c01062.
    - Sec. 2.1: seminumerical derivatives, Eq. 5.
    - Sec. 2.2: Eqs. 6-18, the gradient, CPHF for all pairs and the modified Z vector.
    - Sec. 2.4: degeneracies, Eqs. 20-21.
    - Sec. 3: tests.
    - Equations read from the page images. Summary: [[coe-2023-sci-gradient]].
- The linear form of $\mathbf l'$ and the sum-rule test are my restatement in the notebook's conventions, checked numerically.
- Z-vector: N. C. Handy and H. F. Schaefer III, *J. Chem. Phys.* **81**, 5031 (1984), doi:10.1063/1.447489.
- Computations: PySCF 2.15, `gradients/sci_grad.py` and `gradients/sci_grad_asym.py`, built on the CISD code of [[ci-analytic-gradient]].
