---
id: shajan-2025-dmet-sqd
title: Shajan et al. 2025 - Toward quantum-centric simulations of extended molecules - SQD enhanced with DMET
summary: First DMET calculations with SQD as the fragment solver, run on ibm_cleveland. H18 ring (27 qubits per fragment instead of 41) and the four conformers of cyclohexane (32 instead of 89). DMET-SQD tracks HCI better than unfragmented SQD for H18 and orders the cyclohexane conformers correctly once at least 8000 configurations per batch are used.
kind: paper
status: in-progress
tags: [DMET, SQD, quantum-embedding, hydrogen-ring, cyclohexane, hardware]
prerequisites: []
related: [dmet-with-quantum-solvers, sample-based-quantum-diagonalization]
order: 40
authors: A. Shajan, D. Kaliakin, A. Mitra, J. Robledo Moreno, Z. Li, M. Motta, C. Johnson, A. A. Saki, S. Das, I. Sitdikov, A. Mezzacapo, K. M. Merz
journal: Journal of Chemical Theory and Computation 21, 6801-6810
year: 2025
doi: 10.1021/acs.jctc.5c00114
date: 2026-11-08
---

## Research problem

Near-term devices limit SQD to active spaces of a few tens of orbitals. Can embedding stretch that to extended molecules?

## Method

One-shot DMET in Tangelo (meta-Löwdin, STO-3G) with an in-house SQD solver; LUCJ from embedding CCSD, run with gate twirling and dynamical decoupling; samples taken at $\mu=0$ and reused for the $\mu$ fit (5 S-CORE rounds before, 3 during). Benchmarks: CCSD, CCSD(T), HCI (DICE), DMET-FCI.

## Results

- **H$_{18}$** (H$_6$ fragments, (12e,12o), 0.70-1.30 Å): unfragmented CCSD(T) about 2 kcal/mol per atom below HCI at stretch, unfragmented SQD about 2.5 above; DMET-SQD and DMET-CCSD closer to HCI with small non-parallelity.
- **Cyclohexane** (CH$_2$ fragments, (14e,14o)): DMET-FCI against CCSD(T) below 1 kcal/mol; DMET-SQD within ~1 kcal/mol of DMET-FCI and correctly ordered for $|\tilde\chi_b|\ge8\times10^3$; wrong order at $6\times10^3$.
- **Sampling efficiency** is higher for embedding problems than for the whole molecule.

## Limitations

Energies only, no gradients; minimal basis; geometries fixed (MP2 structures); random sampling makes results depend on batch size and seeds.

## Relevance

Source for the DMET-SQD workflow and results in [[dmet-with-quantum-solvers]].
