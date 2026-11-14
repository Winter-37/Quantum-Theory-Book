---
id: tilly-2022-vqe-review
title: Tilly et al. 2022 - The variational quantum eigensolver, a review of methods and best practices
summary: A 128-page review of every stage of VQE - Hamiltonians, fermion-to-qubit encodings, measurement and grouping, ansätze (hardware-efficient, UCC, symmetry-preserving, adaptive), optimizers and gradients, barren plateaus, error mitigation, excited states and embedding - with recommended practices and resource estimates.
kind: paper
status: in-progress
tags: [VQE, review, quantum-algorithms, ansatz, measurement, error-mitigation]
prerequisites: []
related: [variational-quantum-eigensolver, vqe-ansatze, jordan-wigner-mapping]
order: 10
authors: J. Tilly, H. Chen, S. Cao, D. Picozzi, K. Setia, Y. Li, E. Grant, L. Wossnig, I. Rungger, G. H. Booth, J. Tennyson
journal: Physics Reports 986, 1-128
year: 2022
doi: 10.1016/j.physrep.2022.08.003
date: 2026-11-08
---

## Research problem

VQE is the most studied near-term quantum algorithm for chemistry, but its literature is fragmented across encodings, ansätze, measurement schemes and optimizers, with little guidance on which choices scale.

## Method

A review, organized by the stages of the VQE pipeline, ending each part with an assessment of scaling and suggested best practices.

## Where to find things

- **Sec. 2.** Formal definition, pipeline, advantage argument and limitations, comparison with FCI, CC and QPE, resource estimates.
- **Sec. 3.** Electronic, lattice, vibrational and periodic Hamiltonians.
- **Sec. 4.** Encodings: Jordan-Wigner (4.1.1), parity, Bravyi-Kitaev, ternary trees; lattice-tailored encodings; qubit reduction (4.3).
- **Sec. 5.** Shot scaling (5.1, with the upper bound Eq. 85), measurement weighting, grouping and joint measurements (5.2), shadows.
- **Sec. 6.** Barren plateaus (6.1); fixed-structure ansätze (6.2); adaptive ansätze (6.3).
- **Sec. 7.** Gradient evaluation (parameter shift, 7.2.2), first- and second-order and gradient-free optimizers.
- **Sec. 8.** Error mitigation: symmetry verification, extrapolation, probabilistic cancellation, purification, readout.
- **Sec. 9.** Excited states; VQE as a solver for embedded subspaces (9.2).

## Results

- **Measurement wall.** Shot counts scale as $O(1/\epsilon^2)$ times a Hamiltonian-dependent prefactor; Sec. 5.1.1 quotes a conservative $O(10^{19})$ shots for Fe$_2$S$_2$ in STO-3G (112 spin orbitals).
- **Trainability.** Barren plateaus make generic deep circuits untrainable; problem-inspired and adaptive ansätze are the recommended route.

## Limitations

Written before sample-based methods (SQD) and before most hardware demonstrations beyond tens of qubits; its resource estimates are for VQE energy estimation, not for sampling-based workflows.

## Relevance

Background for Part 6, Chapter 3 ([[variational-quantum-eigensolver]], [[vqe-ansatze]]) and for the encodings in [[jordan-wigner-mapping]]. Sec. 9.2 is the starting point for VQE inside embedding ([[dmet-with-quantum-solvers]]).
