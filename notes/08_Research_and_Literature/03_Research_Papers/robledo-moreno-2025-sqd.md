---
id: robledo-moreno-2025-sqd
title: Robledo-Moreno et al. 2025 - Chemistry beyond the scale of exact diagonalization on a quantum-centric supercomputer
summary: Introduces sample-based quantum diagonalization at scale. An LUCJ circuit initialized from CCSD is sampled on IBM Heron processors, the noisy determinants are repaired by self-consistent configuration recovery, and the Hamiltonian is diagonalized in the sampled subspace on up to 6400 Fugaku nodes. N2 dissociation (cc-pVDZ, 58 qubits), [2Fe-2S] (45 qubits) and [4Fe-4S] (77 qubits).
kind: paper
status: in-progress
tags: [SQD, quantum-centric-supercomputing, LUCJ, configuration-recovery, iron-sulfur, N2]
prerequisites: []
related: [sample-based-quantum-diagonalization, lucj-ansatz, jordan-wigner-mapping]
order: 30
authors: J. Robledo-Moreno, M. Motta, H. Haas, A. Javadi-Abhari, P. Jurcevic, W. Kirby, S. Martiel, K. Sharma, S. Sharma, T. Shirakawa, I. Sitdikov, R.-Y. Sun, K. J. Sung, M. Takita, M. C. Tran, S. Yunoki, A. Mezzacapo
journal: Science Advances 11, eadu9991
year: 2025
doi: 10.1126/sciadv.adu9991
date: 2026-11-08
---

## Research problem

VQE energy estimation needs too many measurements, and chemically motivated circuits are too deep for current devices. Can a quantum processor contribute to electronic structure beyond exact diagonalization without estimating energies?

## Method

Sample determinants from a truncated LUCJ circuit (Eq. 5, Fig. 3); restore $N$ and $S_z$ by self-consistent configuration recovery with a modified-ReLU flip probability (Eq. 17); close the sampled strings under spin inversion; diagonalize in $K$ batches of subspaces (Eq. 3) with Davidson (PySCF) or DICE; update the occupations (Eq. 4) and repeat.

## Results

- **Noise robustness** (simulated N$_2$/6-31G, global depolarizing noise): with recovery, about 2% signal suffices for errors below 10 m$E_h$, against about 20% without (Fig. 2).
- **N$_2$/cc-pVDZ**, (10e,26o), 58 qubits, $d = 16\times10^6$, 10 recovery rounds: curve within tens of m$E_h$ of HCI; CCSD fails at dissociation.
- **[2Fe-2S]** (30e,20o) and **[4Fe-4S]** (54e,36o): subspaces up to $10^8$ determinants on Fugaku; energy-variance analysis. For [2Fe-2S] HCI does not find the optimal subspace; an LUCJ optimized against a target distribution and then the SQD energy samples near-optimal subspaces (Fig. 5).

## Limitations

The CCSD-initialized LUCJ is over-concentrated near HF when $J$ is small; $S^2$ is only approximately restored; accuracy depends on sampling the ground-state support, which the paper argues is where quantum advantage could appear but does not prove.

## Relevance

Source for [[sample-based-quantum-diagonalization]] and [[lucj-ansatz]], where the over-concentration near Hartree-Fock and the comparison against classical null models are checked.
