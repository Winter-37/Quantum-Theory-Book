---
id: sample-based-quantum-diagonalization
title: Sample-based quantum diagonalization (SQD) - the quantum computer proposes determinants, a classical computer diagonalizes
summary: Measuring a Jordan-Wigner register samples determinants. SQD collects the sampled bit strings, repairs those with wrong electron counts by self-consistent configuration recovery, closes the set under spin inversion, and diagonalizes the Hamiltonian in the product space of the sampled α and β strings. The energy is a variational upper bound and needs no energy measurement on the device; its quality depends entirely on whether the sampler hits the ground-state support. Water (8e,12o) shows the point: at equal subspace size, samples from the exact distribution beat uniform random strings by 10-100×, while a CCSD-initialized local LUCJ circuit is over-concentrated near Hartree-Fock.
status: in-progress
kind: algorithm
level: advanced
tags: [SQD, quantum-selected-CI, sampling, configuration-recovery, LUCJ, subspace-diagonalization, variational]
prerequisites: [jordan-wigner-mapping, full-ci, determinant-strings-and-direct-ci, ci-optimization-newton-and-davidson]
related: [selected-ci-analytic-gradient, lucj-ansatz, variational-quantum-eigensolver, dmet-with-quantum-solvers, natural-orbitals]
order: 10
date: 2026-11-08
---

Notation: $N_{\rm MO}$ spatial orbitals, $M = 2N_{\rm MO}$ qubits; a bit string $x = x_\downarrow x_\uparrow$ is a determinant ([[jordan-wigner-mapping]]). $\tilde{\mathcal X}$ is the multiset of measured strings, $\mathcal S$ a set of determinants, $\hat P_{\mathcal S} = \sum_{x\in\mathcal S}|x\rangle\langle x|$.

## The method

**Projection and diagonalization** (Robledo-Moreno et al. 2025, Eq. 3).

$$
\hat H_{\mathcal S} = \hat P_{\mathcal S}\hat H\hat P_{\mathcal S},\qquad
\hat H_{\mathcal S}|\psi_{\mathcal S}\rangle = E_{\mathcal S}|\psi_{\mathcal S}\rangle,\qquad E_{\mathcal S}\ge E_0 .
$$

- **Variational.** $|\psi_{\mathcal S}\rangle$ is a CI vector in a subspace, so $E_{\mathcal S}$ is an upper bound that decreases monotonically as $\mathcal S$ grows. It equals FCI when $\mathcal S$ is complete.
- **Classical work.** Matrix elements come from the Slater-Condon rules; the diagonalization is a Davidson solve, as in selected CI ([[ci-optimization-newton-and-davidson]]).
- **Quantum work.** The device only samples. It never estimates an energy, which removes the measurement cost that limits VQE ([[variational-quantum-eigensolver]]).
- **When it can work.** The ground state must be well approximated by a sparse vector, and the sampler must place its probability on that support.

**Spin closure** (Materials and Methods). Determinants are not $\hat S^2$ eigenfunctions, and a sampled set need not contain the partners needed to form one. Collect the unique half-strings $x_\uparrow$ and $x_\downarrow$ from the samples, take their union $\mathcal U$, and use the product space $\mathcal S = \mathcal U\times\mathcal U$. The set is then closed under exchange of $\alpha$ and $\beta$ strings, which restores $\hat S^2$ approximately. A product space is also what string-driven CI codes handle efficiently ([[determinant-strings-and-direct-ci]]).

## Self-consistent configuration recovery (S-CORE)

**The problem.** Noise broadens $P_\Psi(x) = |\langle x|\Psi\rangle|^2$ into some $\tilde P_\Psi$. Many strings come out with the wrong $N_\uparrow$ or $N_\downarrow$, and discarding them throws away most shots on current hardware.

**The fix** (Robledo-Moreno et al., Fig. 1, Eqs. 4, 17).

1. **Start.** Keep the shots with correct counts for both spins, form $K$ batches, diagonalize each, and average the occupations $n_{p\sigma} = K^{-1}\sum_k\langle\psi^{(k)}|\hat n_{p\sigma}|\psi^{(k)}\rangle$.
2. **Recover.** For each string with $N_{x\sigma}\neq N_\sigma$, flip $|N_{x\sigma}-N_\sigma|$ bits among the occupied (too many electrons) or empty (too few) orbitals of that spin. Choose them with probability proportional to $w(|x_{p\sigma}-n_{p\sigma}|)$, where $w$ is a modified ReLU that rarely flips bits already agreeing with the average occupation.
3. **Rediagonalize.** Draw new batches from the recovered set, diagonalize, update $n$.
4. **Repeat.** Usually converged within three rounds in their experiments; at most five to ten were used.

S-CORE treats the occupation vector as a cluster centre and pulls noisy strings toward it. It restores $N$ and $S_z$, not $S^2$.

**Experiments.** N$_2$ cc-pVDZ (10e,26o) on 58 qubits; [2Fe-2S] (30e,20o) on 45 qubits; [4Fe-4S] (54e,36o) on 77 qubits, with subspaces up to $d = 10^8$ diagonalized on Fugaku. For N$_2$ the dissociation curve lies within tens of m$E_h$ of HCI everywhere. Robledo-Moreno et al. also show that HCI itself does not find the optimal subspace for [2Fe-2S]: smaller subspaces give comparable energies, and the bottleneck is proposing good configurations, not diagonalizing.

## What the sampler must do

The energy in a given subspace is fixed by which determinants it holds, not by how often they were sampled. A fair test of a sampler therefore compares energies at **equal subspace size** against a classical null model (random strings). Without that control, a large enough random subspace of a small problem looks like quantum success.

## Nuclear gradients

For a given list of determinants, SQD is a selected CI: the energy is the lowest eigenvalue of $\mathbf H$ in that list, in the orbitals the bitstrings refer to. Its analytic gradient is therefore the selected-CI gradient ([[selected-ci-analytic-gradient]]), with the list held fixed while the geometry changes. A sampled list is not closed under occupied-occupied or virtual-virtual rotations, so the orbital response is needed for those pairs too, not only the occupied-virtual block a CISD gradient would use.

## Worked example

!!! example "Water, 6-31G, O 1s frozen: (8e,12o), FCI dimension 245 025"
    O-H 0.96 Å and 1.92 Å, angle 104.5°. Samplers: exact FCI distribution $|c_D|^2$; LUCJ with CCSD parameters, $L=2$, heavy-hex-style locality ([[lucj-ansatz]]); uniform random strings plus the HF string. $2\times10^5$ shots; the $k$ most frequent strings per spin, spin-closed; PySCF fixed-space CI. Scripts: `sqd_fixed_dim.py`, `sqd_demo.py`.

    $E_{\mathcal S}-E_{\rm FCI}$ in m$E_h$:

    | $r_{\rm OH}$ | $k$ (dim, % of FCI) | FCI samples | local LUCJ | uniform + HF |
    |---|---|---|---|---|
    | 0.96 | 30 (900, 0.37%) | 14.6 | 69.8 | 128.4 |
    | 0.96 | 60 (3600, 1.5%) | 3.13 | 40.4 (40 strings only) | 130.0 |
    | 0.96 | 120 (14 400, 5.9%) | 1.00 | — | 110.6 |
    | 1.92 | 30 (900) | 28.3 | 55.6 (27 strings only) | 287.1 |
    | 1.92 | 120 (14 400) | 2.14 | — | 269.6 |

    - **The sampler is what matters.** At 0.4% of the FCI space, ideal samples are within 15-28 m$E_h$, uniform strings 130-290 m$E_h$ away.
    - **Over-concentration.** The local LUCJ state has 99.6% weight on HF (exact: 95.5%), and $2\times10^5$ shots produce only 40 (0.96 Å) or 27 (1.92 Å) distinct strings per spin. More shots add little: the subspace is capped by what the circuit samples. Which rare strings appear depends on the random seed, so these LUCJ numbers move by several m$E_h$ between runs.
    - **A trap with noise.** Replace 90% or 98% of the $10^4$ LUCJ shots by uniform random bits and run S-CORE (qiskit-addon-sqd, 5 batches of 300): the error drops from 104 to 0.015-0.04 m$E_h$. But the subspace has grown to 138 000-150 000 determinants, 56-61% of FCI. The noise has covered the space; this is the null model succeeding, not the circuit. For a problem this small, any honest claim needs the equal-size comparison above.

## Source

- J. Robledo-Moreno, M. Motta, H. Haas, et al., "Chemistry beyond the scale of exact diagonalization on a quantum-centric supercomputer", *Sci. Adv.* **11**, eadu9991 (2025), doi:10.1126/sciadv.adu9991. Results (workflow, Fig. 1; configuration recovery, Fig. 2; LUCJ, Fig. 3; experiments, Fig. 4); Materials and Methods (projection, spin closure, recovery with the modified ReLU, Eq. 17; energy-variance analysis).
- A. Shajan, D. Kaliakin, A. Mitra, et al., *J. Chem. Theory Comput.* **21**, 6801 (2025), doi:10.1021/acs.jctc.5c00114. Methods: S-CORE as used inside DMET ([[dmet-with-quantum-solvers]]).
- Software: qiskit-addon-sqd 0.14.1, ffsim 0.0.86, PySCF 2.15.
