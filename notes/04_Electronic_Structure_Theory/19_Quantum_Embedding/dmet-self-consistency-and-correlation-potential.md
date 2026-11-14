---
id: dmet-self-consistency-and-correlation-potential
title: DMET self-consistency - the correlation potential, cost functions, and when one-shot DMET is enough
summary: Full DMET feeds the fragment solutions back into the mean field. A one-body correlation potential u is added to the low-level Hamiltonian and fitted so that fragment density matrices of the mean field match those of the correlated solvers. The cost functions in use, the Lieb-type dual that removes indeterminacy, the algorithm, and the evidence (H rings, Be rings) on when self-consistency matters. One-shot DMET, with only a global μ, is what molecular gradient work uses.
status: in-progress
kind: theory
level: advanced
tags: [DMET, self-consistency, correlation-potential, cost-function, one-shot, v-representability]
prerequisites: [dmet-energy-functionals-and-chemical-potential]
related: [dmet-analytic-nuclear-gradient, rhf]
order: 40
date: 2026-11-08
---

Notation: $D^x$ is the 1-RDM of the correlated solution of fragment $x$, $D^{\rm mf}(u)$ the 1-RDM of the mean-field determinant of the low-level Hamiltonian $\hat h' = \hat h + \hat C$. Indices $r,s$ run over the orbitals named under each sum.

## The correlation potential

**Low-level Hamiltonian.** The global determinant $|\Phi\rangle$ is the ground state of a one-particle Hamiltonian

$$
\hat h' = \hat h + \sum_x \hat C_x,\qquad \hat C_x = \sum_{kl\in A_x} u^x_{kl}\,a^\dagger_k a_l ,
$$

with $\hat h$ usually the Fock operator of the initial RHF. The potential $u$ acts on each fragment's orbitals only. It changes $|\Phi\rangle$, hence the bath and core orbitals, hence the embedding problems. In the interacting-bath formulation $u$ does not appear in the embedding Hamiltonian itself, which would double count (Wouters et al. 2016, Sec. 3.1).

**Self-consistency loop** (Wouters et al. 2016, Algorithm 1, Sec. 5.1).

1. Solve the mean field of $\hat h'(u)$ and build $\gamma$.
2. For each fragment build the bath and the embedding Hamiltonian.
3. Solve each embedding problem with $\mu_{\rm glob}$; fit $\mu_{\rm glob}$ to the electron count.
4. Fit $u$ by minimizing a cost function at fixed correlated densities; go to 1.

## Cost functions

Each choice defines a different DMET functional (Wouters et al. 2016, Eqs. 29-32):

| name | what is matched | $u$ |
|---|---|---|
| fragment plus bath | $\sum_x\sum_{rs\in A_x\cup B_x}(D^x_{rs}-D^{\rm mf}_{rs})^2$ | on fragments |
| fragment only | $\sum_x\sum_{rs\in A_x}(D^x_{rs}-D^{\rm mf}_{rs})^2$ | on fragments |
| fragment diagonal | $\sum_x\sum_{r\in A_x}(D^x_{rr}-D^{\rm mf}_{rr})^2$ | diagonal |
| electron number | $(\sum_x\sum_{r\in A_x}D^x_{rr}-N)^2$ | none, only $\mu_{\rm glob}$ (one-shot) |

- **Not always reachable.** $D^{\rm mf}$ is idempotent and $D^x$ is not, so a correlated density need not be representable by any determinant (the DMET analogue of non-interacting $v$-representability). The fragment-plus-bath cost never reaches zero.
- **Indeterminacy and its cure.** When no exact match exists, many $u$ give the same cost. Wouters et al. replace the least-squares fit by the dual problem (following Lieb): maximize over $u$

    $$
    \min_\Phi\Big[\langle\Phi|\hat h|\Phi\rangle + \sum_x\sum_{rs\in A_x}u^x_{sr}\big(D^{\rm mf}_{rs}(\Phi)-D^x_{rs}\big)\Big],
    $$

    whose energy term breaks the degeneracy. When an exact match exists the two are equivalent.
- **Optimize all fragments together.** Fitting each fragment's $u^x$ separately is prone to limit cycles. Wouters et al. fit all at once, at fixed correlated densities, with analytic gradients of the cost.

## When it matters

- **H$_{10}$ and H$_{90}$ rings** (STO-6G, FCI solver). Self-consistency improves small-fragment results, but the difference from one-shot DMET shrinks as fragments grow (Wouters et al. 2016, Sec. 6.1).
- **Be$_{30}$ ring.** Near the crossing of two RHF solutions of different character, self-consistency largely removes the dependence on the starting determinant, and the jump in the curve shrinks (Sec. 6.2).
- **Molecular gradients.** Li et al. 2023 and most molecular DMET work use one-shot DMET (only $\mu$). One-shot DMET keeps the gradient theory to one global Z-vector solve, since the mean field is then the plain RHF of the molecule ([[dmet-analytic-nuclear-gradient]]).

## Source

- Wouters et al., *J. Chem. Theory Comput.* **12**, 2706 (2016), doi:10.1021/acs.jctc.6b00316. Sec. 3 (Eqs. 14-15), Sec. 5 (Eqs. 29-36, Algorithm 1), Sec. 6 (applications).
- No worked example here: the notebook's DMET code (`dmet_mini.py`) is one-shot only.
