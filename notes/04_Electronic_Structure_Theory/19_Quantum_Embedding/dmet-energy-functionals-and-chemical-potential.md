---
id: dmet-energy-functionals-and-chemical-potential
title: DMET energy - democratic partitioning, the mean-field and correlated-density functionals, and the global chemical potential
summary: Embedding spaces of different fragments overlap, so fragment energies cannot simply be added. Democratic partitioning gives each fragment the share of every one- and two-body term that belongs to its impurity. Two functionals use these weights - one in which the environment acts through the Hartree-Fock density, one (Li et al. 2023) through a correlated density assembled from all fragments. Both are exact for an HF solver, neither is an expectation value, so DMET is not variational. A global μ fixes the electron count. H6 ring numbers show errors of either sign and the exact limit when the embedding space is the whole molecule.
status: in-progress
kind: theory
level: advanced
tags: [DMET, democratic-partitioning, energy-functional, chemical-potential, non-variational, one-shot]
prerequisites: [dmet-embedding-hamiltonian, density-matrices-second-quantization, full-ci]
related: [dmet-self-consistency-and-correlation-potential, dmet-analytic-nuclear-gradient, size-consistency]
order: 30
date: 2026-11-08
---

Notation: as in [[dmet-embedding-hamiltonian]]. The solver of fragment $I$ returns spin-summed RDMs $r_{1,pq} = \langle\hat E_{pq}\rangle$ and $r_{2,pqrt} = \langle a^\dagger_p a^\dagger_r a_t a_q\rangle$ (spin-summed, PySCF index order), so that $\langle\hat H\rangle = \sum h_{pq}r_{1,pq} + \tfrac12\sum(pq|rt)r_{2,pqrt}$.

## Democratic weights

**The problem.** The embedding space of fragment $I$ contains its impurity and a bath that overlaps other fragments' impurities. Adding the full embedded energies counts the bath regions several times.

**The rule.** Assign each term to the fragments that own its indices (Wouters et al. 2016, Eqs. 23-28; Li et al. 2023, Eqs. 5-7):

$$
(w_1)_{pq} = \begin{cases}1 & p,q\in I\\ \tfrac12 & \text{one of } p,q\in I\\ 0 & p,q\in\text{bath}\end{cases},
\qquad
(w_2)_{pqrt} = \tfrac14\,\#\{\text{indices among } p,q,r,t \text{ in } I\}.
$$

For symmetric RDMs this equals restricting the first index of every term to the impurity, which is how Wouters et al. write it.

## Two energy functionals

**Mean-field functional** (Wouters et al. 2016, Eq. 28). The environment acts on each fragment through the HF density:

$$
E = E_{\rm nuc} + \sum_I\Big[\sum_{pq}(w_1\circ h')_{pq}\,r_{1,pq} + \tfrac12\sum_{pqrt}(w_2\circ g)_{pqrt}\,r_{2,pqrt}\Big],
\qquad h' = \tfrac12\big(h_{\rm emb} + h_B\big),
$$

where $g$ are the embedding integrals and $h_B = h_{\rm emb}+v_{\rm core}$. The factor $\tfrac12$ on $v_{\rm core}$ is there because the interaction of an impurity electron with a core electron is shared between two fragments, as in $E_{\rm HF} = \tfrac12\operatorname{tr}[D(h+F)]$.

**Correlated-density functional** (Li et al. 2023, Eqs. 5-7). First assemble a global density from the fragments, $G = \sum_I C_I(w_1\circ r_{1,I})C_I^{\mathsf T}$ (spin-summed). Then replace the mean-field environment by $G$:

$$
E = E_{\rm nuc} + \operatorname{tr}(G h) + \tfrac12\operatorname{tr}\big(G\,v_s[G]\big)
- \tfrac12\sum_I\operatorname{tr}\big((w_1\circ r_{1,I})\,v_{s,{\rm emb},I}[r_{1,I}]\big)
+ \tfrac12\sum_I\sum_{pqrt}(w_2\circ g_I)_{pqrt}\,r_{2,I,pqrt},
$$

with $v_s[D] = J[D]-\tfrac12K[D]$ for a spin-summed $D$. The first three terms are the mean-field energy of $G$. The fourth removes each fragment's own mean-field pair energy, which its 2-RDM term already contains. This functional is quadratic in the fragment densities through $\operatorname{tr}(Gv_s[G])$, so it couples the fragments.

**Properties of both.**

- **Exact for an HF solver.** With complete baths, each fragment returns $r_1 = 2\gamma_{\rm emb}$ and the weighted terms tile the LO space. The mean-field functional then sums to $E_{\rm HF}$; for the correlated functional $G=2\gamma$ and the last two terms cancel for a single determinant.
- **Exact when the embedding space is the whole molecule.** If every fragment's embedding space spans all LOs and the solver is exact, all fragments hold the same RDMs, the weights sum to one, and both functionals return the full-system answer.
- **Not variational.** Neither functional is $\langle c_I|\hat H_I|c_I\rangle$, so there is no upper bound and the error can have either sign. For the same reason the Hellmann-Feynman theorem fails even for an exact solver, and a gradient needs the solver's response ([[dmet-analytic-nuclear-gradient]]).
- **Locality.** Democratic partitioning suits systems where correlation is spread evenly (rings, chains, crystals). For a chemical change confined to one fragment, Wouters et al. found that the democratic electron count is the largest source of error, and an active-space energy of that single fragment converged faster (SN2 study, Sec. 6.3).

## The global chemical potential

**Condition.** Each fragment is solved in its own embedding, so the impurity counts need not add to $N$. One global $\mu$, applied in the solver only ([[dmet-embedding-hamiltonian]]), is fitted so that

$$
N(\mu) = \sum_I \sum_{p\in I} r_{1,I,pp}(\mu) = N .
$$

- **Root finding.** $N(\mu)$ is non-decreasing, so the root is unique; Wouters et al. and Li et al. use a secant method.
- **Effect on derivatives.** At the fitted $\mu^*(R)$, the total derivative of $E(R,\mu^*(R))$ is $\partial_R E - z\,\partial_R N$ at fixed $\mu$, with $z = (\partial E/\partial\mu)/(\partial N/\partial\mu)$. This follows from differentiating $N(\mu^*(R),R)=N$ and is the scalar multiplier $z$ of the Lagrangian in [[dmet-analytic-nuclear-gradient]].

**One-shot DMET.** Everything above, with $\mu$ as the only self-consistent quantity, is one-shot DMET. Full self-consistency adds a correlation potential in the mean-field problem ([[dmet-self-consistency-and-correlation-potential]]).

## Worked example

!!! example "H$_6$ ring, STO-3G, 1.0 Å, FCI solver"
    Löwdin LOs, RHF $-3.157047$, FCI $-3.237477\ E_h$ (correlation energy $-80.4$ m$E_h$). Script: `dmet_mini.py`, μ converged to $|N-6| < 10^{-11}$.

    | fragments | $N(\mu=0)$ | $\mu^*$ | $E_{\rm DMET}$ | $E_{\rm DMET}-E_{\rm FCI}$ (m$E_h$) |
    |---|---|---|---|---|
    | 6 × H | 6.000786 | $-1.46\times10^{-4}$ | $-3.242562$ | $-5.08$ |
    | 3 × H$_2$ | 5.997334 | $+8.99\times10^{-4}$ | $-3.231060$ | $+6.42$ |
    | 2 × H$_3$ | 6.000000 | $\approx 0$ | $-3.237477$ | $1.5\times10^{-11}$ |

    - **Either sign.** One-atom fragments overshoot FCI, two-atom fragments undershoot: the energy is not bounded.
    - **Exact limit.** With three-atom fragments $n_I = n_E = 3$, every embedding space is the whole ring, and DMET reproduces FCI.
    - **HF solver.** With three H$_2$ fragments and an HF solver, both functionals give $-3.157047466625\ E_h$, equal to RHF to $3\times10^{-15}$, with $N = 6$ at $\mu=0$.
    - **The two functionals differ for a correlated solver.** For three H$_2$ fragments at $\mu=0$: mean-field functional $-3.228597$, correlated-density functional $-3.231560\ E_h$.
    - **μ coupling.** For three H$_2$ fragments, stretching every bond: $\partial E/\partial R|_\mu = 0.041029$, $z = -0.9238$, $\partial N/\partial R|_\mu = 1.723\times10^{-3}$ per Å. The chain rule gives $0.042620$; a finite difference at refitted $\mu$ gives $0.042620\ E_h$/Å (difference $1.3\times10^{-8}$). Refitting $\mu$ changes the force by 4%.

## Source

- Wouters et al., *J. Chem. Theory Comput.* **12**, 2706 (2016), doi:10.1021/acs.jctc.6b00316. Sec. 4 (Eqs. 21-28): democratic partitioning and the fragment energy; Sec. 5.1 (Eq. 36): secant fit of $\mu_{\rm glob}$; Sec. 6.3: SN2 reaction and the locality caveat.
- Li et al., *J. Chem. Phys.* **158**, 134105 (2023), doi:10.1063/5.0142961. Eqs. 5-7: correlated global density, updated one-electron part, total energy.
