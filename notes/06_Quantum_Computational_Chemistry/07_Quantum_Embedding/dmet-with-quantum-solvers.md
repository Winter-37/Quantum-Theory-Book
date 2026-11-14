---
id: dmet-with-quantum-solvers
title: DMET with quantum solvers - fragment problems small enough for a device, and what changes for energies and geometries
summary: DMET replaces one large correlated problem by several fragment-plus-bath problems of twice the fragment size, which is what makes VQE or SQD solvers fit on current hardware. With SQD the device samples once per fragment and the chemical potential is fitted classically on the stored samples. For geometries the open questions are smoothness (a sampled determinant list changes with geometry) and the gradient (the DMET energy is not variational, so Hellmann-Feynman is not exact). Hao et al. (2026) co-optimize geometry and VQE parameters with a Hellmann-Feynman gradient; the analytic Lagrangian of Li et al. (2023) gives the exact derivative.
status: in-progress
kind: comparison
level: advanced
tags: [DMET, quantum-embedding, SQD, VQE, geometry-optimization, quantum-centric-supercomputing]
prerequisites: [dmet-energy-functionals-and-chemical-potential, sample-based-quantum-diagonalization, variational-quantum-eigensolver]
related: [dmet-analytic-nuclear-gradient, lucj-ansatz, geometry-optimization]
order: 10
date: 2026-11-08
---

Notation: fragment $I$ with $n_I$ impurity orbitals and $n_{\rm bath}\le n_I$ bath orbitals ([[schmidt-decomposition-and-dmet-bath]]); qubits per fragment $2(n_I+n_{\rm bath})$ under Jordan-Wigner, less if an active space is taken inside the embedding space.

## Why embedding suits near-term quantum solvers

- **Qubit count.** An embedding problem has at most $2n_I$ spatial orbitals. Shajan et al. ran H$_{18}$ (STO-3G) as H$_6$ fragments with (12e,12o) embedding problems on 27 qubits instead of 41; cyclohexane as CH$_2$ fragments with (14e,14o) problems on 32 qubits instead of 89.
- **Easier problems.** With a delocalized HOMO or LUMO, the single-particle gap of an embedding problem is larger than that of the whole molecule (Wouters et al. 2016, Sec. 6.2), so fewer determinants matter.
- **Parallel.** Fragments are independent at fixed $\mu$; only the electron count couples them.

## DMET-SQD (Shajan et al. 2025)

**Workflow.**

1. One-shot DMET (meta-Löwdin LOs, STO-3G, Tangelo + PySCF), embedding Hamiltonian as in [[dmet-embedding-hamiltonian]].
2. LUCJ circuit per symmetry-distinct fragment, parameters from embedding CCSD, run on ibm_cleveland with gate twirling and dynamical decoupling.
3. **Sample once, at $\mu=0$.** $\mu$ is then fitted by repeating S-CORE on the same samples for each trial $\mu$ (5 rounds before, 3 rounds during the fit). Total circuits: 3 for H$_{18}$/H$_6$, 6 for cyclohexane.

**Results.**

- **H$_{18}$ ring** (0.70-1.30 Å). Unfragmented RCCSD and CCSD(T) fall about 2 kcal/mol per atom below HCI at stretched bonds; unfragmented SQD lies about 2.5 kcal/mol per atom above. DMET-CCSD and DMET-SQD stay closer to HCI with much smaller non-parallelity, sub-kcal/mol per atom.
- **Cyclohexane conformers.** DMET-FCI against unfragmented CCSD(T): fragmentation error well below 1 kcal/mol. DMET-SQD with $|\tilde\chi_b|\ge 8\times10^3$ configurations per batch: within about 1 kcal/mol of DMET-FCI and correctly ordered. With $6\times10^3$ the order is wrong (twist-boat predicted most stable).
- **Sampling efficiency.** The fraction of retained configurations with $|c|^2\ge10^{-8}$ is higher in DMET-SQD than in unfragmented SQD: embedding problems are sampled more efficiently.

## Geometry optimization: two routes

**1. Nested loops.** Converge the fragment solvers (VQE or SQD, plus $\mu$) at each geometry, compute a gradient, step. The quantum cost is repeated at every geometry.

**2. Co-optimization** (Hao et al. 2026). Update nuclear coordinates $\vec x$ and circuit parameters $\vec\theta$ alternately inside one loop, with $\mu$ refitted in an outer loop:

$$
\vec x \leftarrow \vec x - \eta\,\nabla_{\vec x}\Big[\sum_I E_I(\vec\theta_I,\vec x) + E_{\rm nuc}(\vec x)\Big],\qquad
\vec\theta_I \leftarrow \vec\theta_I - \eta\,\nabla_{\vec\theta_I}\langle\psi(\vec\theta_I)|\hat H_{\rm emb}^I(\vec x)|\psi(\vec\theta_I)\rangle .
$$

- **Their gradient.** The nuclear gradient is taken from the Hellmann-Feynman theorem as $\langle\psi|\partial\hat H_{\rm emb}/\partial\vec x|\psi\rangle$ (their Eq. 23); the circuit gradient from the parameter-shift rule.
- **Tests.** H$_4$ (8 → 4 qubits), H$_2$O$_2$ (24 → 16), and glycolic acid (58 → 20), simulated in MindSpore Quantum. For glycolic acid only two rigid-rotation angles of the OH group were optimized, against a CCSD scan.
- **What is missing (my assessment).** The DMET energy is not an expectation value, and the bath, the Löwdin orbitals and the global HF density all depend on $\vec x$ ([[dmet-analytic-nuclear-gradient]]). A Hellmann-Feynman gradient therefore omits the solver, bath and orbital response terms. Near-zero forces at their converged geometries test stationarity of that approximate force, not of the DMET energy. The paper does not quantify the omitted terms.

## Source

- A. Shajan, D. Kaliakin, A. Mitra, J. Robledo Moreno, et al., "Toward quantum-centric simulations of extended molecules: sample-based quantum diagonalization enhanced with density matrix embedding theory", *J. Chem. Theory Comput.* **21**, 6801 (2025), doi:10.1021/acs.jctc.5c00114. Methods; Table 1; Figs. 1-5.
- Y. Hao, Q. Ding, X. Wang, X. Yuan, "Large-scale efficient molecule geometry optimization with hybrid quantum-classical computing", *J. Chem. Theory Comput.* **22**, 859 (2026), doi:10.1021/acs.jctc.5c01435. Eqs. 15-23; Table 1; Figs. 3-5.
- Li et al., *J. Chem. Phys.* **158**, 134105 (2023), doi:10.1063/5.0142961, for the exact gradient.
- Wouters et al., *J. Chem. Theory Comput.* **12**, 2706 (2016), Sec. 6.2, for the impurity-gap remark.
