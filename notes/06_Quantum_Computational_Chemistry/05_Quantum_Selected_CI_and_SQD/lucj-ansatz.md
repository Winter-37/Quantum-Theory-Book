---
id: lucj-ansatz
title: The local unitary cluster Jastrow (LUCJ) ansatz - orbital rotations around density-density phases, cut to the qubit connectivity
summary: A unitary cluster Jastrow operator is a product of layers U_k e^{iJ_k} U_k^†, with U_k orbital rotations and J_k diagonal (number-number) operators. Its parameters can be taken from a double factorization of CCSD t2 amplitudes, so no optimization is needed. LUCJ keeps only the J couplings between qubits that are adjacent on the device, which makes each layer shallow. On water the locality cut leaves the state 99.6% Hartree-Fock and spreads samples over few strings; keeping all couplings and more layers samples a far better SQD subspace.
status: in-progress
kind: theory
level: advanced
tags: [LUCJ, unitary-cluster-jastrow, double-factorization, CCSD, ansatz, SQD, hardware]
prerequisites: [sample-based-quantum-diagonalization, coupled-cluster-second-quantization, orbital-rotations]
related: [vqe-ansatze, jordan-wigner-mapping]
order: 20
date: 2026-11-08
---

Notation: $N_{\rm MO}$ spatial orbitals; $\hat n_{p\sigma}$ number operators; $\hat K = \sum_{pq,\sigma}K_{pq}a^\dagger_{p\sigma}a_{q\sigma}$ an anti-Hermitian one-body operator (real $K$ antisymmetric), so $e^{\hat K}$ is an orbital rotation ([[orbital-rotations]]).

## The ansatz

**Unitary cluster Jastrow (UCJ).**

$$
|\Psi\rangle = \prod_{k=1}^{L} e^{\hat K_k}\,e^{i\hat J_k}\,e^{-\hat K_k}\;|\Phi_{\rm HF}\rangle,
\qquad
\hat J_k = \tfrac12\sum_{pq}\sum_{\sigma\tau}J^{\sigma\tau}_{k,pq}\,\hat n_{p\sigma}\hat n_{q\tau}
$$

(Robledo-Moreno et al. 2025, Eq. 5). In the spin-balanced form $J^{\alpha\alpha} = J^{\beta\beta}$, $J^{\alpha\beta} = J^{\beta\alpha}$, and each $K_k$ acts identically on both spins.

- **Why this structure.** Each layer is a diagonal (Jastrow) correlator written in a rotated orbital basis. Orbital rotations compile to $O(N_{\rm MO}^2)$ Givens rotations in linear depth; $e^{i\hat J}$ is a product of commuting two-qubit $ZZ$-type phases.
- **Symmetries.** Both factors conserve $N_\uparrow$ and $N_\downarrow$, so a noiseless LUCJ circuit samples only correct-count strings.

**Parameters from CCSD.** A double factorization of the $t_2$ amplitudes writes $\hat T_2$ as a sum of rotated number-number terms. Each term supplies one $(K_k, J_k)$ layer, truncated to $L$ layers; $t_1$ can supply a final orbital rotation. No variational optimization is needed, which is how Robledo-Moreno et al. and Shajan et al. ran their experiments.

## The locality approximation

On a heavy-hex device a qubit has at most three neighbours. Jordan-Wigner places each spin's orbitals in a line, the $\alpha$ and $\beta$ lines side by side. LUCJ keeps only the $J$ couplings native to this layout:

- **Same spin.** Neighbouring orbitals $(p, p+1)$.
- **Opposite spin.** Same orbital $(p\alpha, p\beta)$, only where the $\alpha$ and $\beta$ lines are connected on the device: every fourth $p$ in the heavy-hex layouts of these papers, where the connection runs through an ancilla qubit.

The rest of $J_k$ is set to zero. Robledo-Moreno et al. also used a truncated circuit, $e^{-\hat K_2}e^{\hat K_1}e^{i\hat J_1}e^{-\hat K_1}|\Phi_{\rm HF}\rangle$ (one Jastrow layer, final rotation dropped), with up to 77 qubits.

**A known weakness.** When the CCSD-derived $J$ are small, $e^{\hat K_1}$ and $e^{-\hat K_1}$ nearly cancel and the state stays concentrated on HF (Robledo-Moreno et al., Results). Their remedy for [2Fe-2S] was to optimize the circuit: first to match a target distribution (Kullback-Leibler divergence), then on the SQD energy.

## Worked example

!!! example "Water, 6-31G, O 1s frozen (8e,12o): what the locality cut costs"
    Parameters from frozen-core CCSD via `ffsim.UCJOpSpinBalanced.from_t_amplitudes`. State vector simulated exactly; $2\times10^5$ shots; SQD over all distinct strings, spin-closed. Script: `lucj_check.py`.

    | $r_{\rm OH}$ | circuit | $\langle H\rangle - E_{\rm FCI}$ (m$E_h$) | weight on HF | strings/spin | $E_{\rm SQD}-E_{\rm FCI}$ (m$E_h$) |
    |---|---|---|---|---|---|
    | 0.96 | local, $L=2$ | 115.1 | 0.996 | 38 | 53.9 |
    | 0.96 | all pairs, $L=2$ | 45.2 | 0.955 | 93 | 18.4 |
    | 0.96 | all pairs, $L=4$ | 29.6 | 0.953 | 115 | 5.7 |
    | 1.92 | local, $L=2$ | 251.2 | 0.945 | 24 | 56.7 |
    | 1.92 | all pairs, $L=2$ | 236.4 | 0.625 | 65 | 26.9 |
    | 1.92 | all pairs, $L=4$ | 115.8 | 0.654 | 84 | 7.9 |

    Exact HF weights: 0.955 (0.96 Å), 0.623 (1.92 Å). $E_{\rm HF}-E_{\rm FCI} = 136.2$ and $292.2$ m$E_h$.

    - **Energy is not the point.** As a variational state LUCJ is poor; even the best circuit has $\langle H\rangle$ 30-116 m$E_h$ above FCI, worse than CCSD (1.5 and 9.8 m$E_h$). As a sampler, the same circuit yields an SQD subspace within 6-8 m$E_h$.
    - **The locality cut.** It pins the state to HF (0.996 against the exact 0.955) and cuts the number of distinct strings by a factor of 2.4-3.5. The SQD error grows from 18-27 to 54-57 m$E_h$ at $L=2$.
    - **Depth.** Going from $L=2$ to $L=4$ (all pairs) brings the SQD error from 18.4 to 5.7 m$E_h$ at equilibrium.

## Source

- J. Robledo-Moreno et al., *Sci. Adv.* **11**, eadu9991 (2025), doi:10.1126/sciadv.adu9991. Eq. 5 and Fig. 3 (LUCJ, heavy-hex compilation, truncated circuit); Results (initialization from CCSD, over-concentration near HF); Discussion and Fig. 5 (optimized LUCJ for [2Fe-2S]).
- The original LUCJ paper, cited as their ref. 34, was not read for this note; to verify before citing: M. Motta et al., *Chem. Sci.* (2023).
- ffsim 0.0.86 documentation of `UCJOpSpinBalanced` and `from_t_amplitudes` (double factorization of $t_2$).
