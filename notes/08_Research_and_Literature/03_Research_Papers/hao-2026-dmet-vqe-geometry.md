---
id: hao-2026-dmet-vqe-geometry
title: Hao, Ding, Wang, Yuan 2026 - Large-scale efficient molecule geometry optimization with hybrid quantum-classical computing
summary: Proposes co-optimizing nuclear coordinates and VQE circuit parameters inside one loop for DMET-embedded fragments, instead of converging VQE at every geometry. Nuclear gradients from the Hellmann-Feynman theorem, circuit gradients from parameter shift. Simulated on H4, H2O2 and a two-angle OH rotation in glycolic acid.
kind: paper
status: in-progress
tags: [DMET, VQE, geometry-optimization, co-optimization, Hellmann-Feynman, UCCSD]
prerequisites: []
related: [dmet-with-quantum-solvers, variational-quantum-eigensolver, dmet-analytic-nuclear-gradient]
order: 50
authors: Y. Hao, Q. Ding, X. Wang, X. Yuan
journal: Journal of Chemical Theory and Computation 22, 859-868
year: 2026
doi: 10.1021/acs.jctc.5c01435
date: 2026-11-08
---

## Research problem

VQE geometry optimization is limited by qubit count and by nested loops (a full VQE at every geometry).

## Method

DMET fragments with UCCSD-VQE solvers. Alternate gradient steps in $\vec x$ and $\vec\theta$ (Eqs. 20-22) within a loop, refitting $\mu$ in an outer loop by Newton-Raphson. Nuclear gradient $\partial E/\partial x$ from Hellmann-Feynman, $\langle\psi|\partial\hat H_{\rm emb}/\partial x|\psi\rangle$ plus $\partial E_{\rm nuc}/\partial x$ (Eq. 23). Simulation in MindSpore Quantum; code at github.com/Yajie-Hao/DMET-VQE-MGO.

## Results

- **H$_4$** (8 → 4 qubits): from a linear chain to two separated H$_2$, in fewer iterations than the nested loop.
- **H$_2$O$_2$** (24 → 16 qubits), four internal parameters: converges to the basin of an FCI scan. Table 1 lists deviations of 0.018-0.079 (Å or rad) for its four parameters, as read from the extracted table (column mapping to verify against the PDF).
- **Glycolic acid** (58 → 20 qubits): two rigid-rotation angles of the OH group, against a CCSD energy scan; Table 1 deviations 0.002 and 0.162 rad.

## Limitations (my assessment)

- **The gradient is approximate.** DMET's energy is not an expectation value and its bath and LOs depend on $x$, so the Hellmann-Feynman term omits the solver, bath and orbital responses that Li et al. (2023) derive ([[dmet-analytic-nuclear-gradient]]). No comparison against finite differences of the DMET energy is shown.
- **Small optimization spaces.** The largest system optimizes two angles; no full Cartesian optimization of a molecule of that size.
- **Simulated, noiseless.** No hardware runs; shot noise in the circuit gradients is not analysed.

## Relevance

Summarized in [[dmet-with-quantum-solvers]] as the co-optimization route. Its Hellmann-Feynman force is compared there with the exact DMET gradient of [[dmet-analytic-nuclear-gradient]].
