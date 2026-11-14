---
id: variational-quantum-eigensolver
title: The variational quantum eigensolver (VQE) - a parametrized circuit, a measured energy, a classical optimizer
summary: VQE minimizes E(θ) = ⟨ψ(θ)|H|ψ(θ)⟩ over the parameters of a quantum circuit, estimating E by measuring the Pauli terms of the qubit Hamiltonian and updating θ classically. It is variational (an upper bound for any θ), needs only short circuits, and is limited by the number of measurements (shots scale as (Σ|c_k|/ε)² for a naive estimator), by the expressivity and trainability of the ansatz, and by noise. One-parameter UCCD on H2 reproduces FCI exactly.
status: in-progress
kind: algorithm
level: intermediate
tags: [VQE, variational-principle, quantum-algorithms, measurement, shot-noise, parameter-shift]
prerequisites: [jordan-wigner-mapping, variational-principle, full-ci]
related: [vqe-ansatze, sample-based-quantum-diagonalization, coupled-cluster-second-quantization]
order: 10
date: 2026-11-08
---

Notation: qubit Hamiltonian $\hat H = \sum_k c_kP_k$ from [[jordan-wigner-mapping]]; $|\psi(\boldsymbol\theta)\rangle = U(\boldsymbol\theta)|\psi_0\rangle$ with $|\psi_0\rangle$ usually the HF determinant; $\epsilon$ the target precision of the energy.

## The algorithm

**Definition** (Tilly et al. 2022, Sec. 2.1).

$$
E_{\rm VQE} = \min_{\boldsymbol\theta}\ \langle\psi_0|U^\dagger(\boldsymbol\theta)\,\hat H\,U(\boldsymbol\theta)|\psi_0\rangle \;\ge\; E_0 .
$$

The bound holds for every $\boldsymbol\theta$ by the [[variational-principle]], so VQE energies are upper bounds whatever the ansatz.

**Pipeline** (Sec. 2.2).

1. **Hamiltonian.** Integrals classically, then a fermion-to-qubit mapping.
2. **Ansatz.** Choose $U(\boldsymbol\theta)$ ([[vqe-ansatze]]).
3. **Measurement.** For each $P_k$, rotate each qubit into the eigenbasis of its Pauli factor, measure in $Z$, average the $\pm1$ parities. Commuting strings can be measured together.
4. **Optimization.** A classical optimizer updates $\boldsymbol\theta$ from estimated energies (and gradients); repeat until converged.

**Gradients.** For gates $e^{-i\theta P/2}$ with $P$ a Pauli string, the **parameter-shift rule** gives an exact derivative from two energy evaluations, $\partial_\theta E = \tfrac12[E(\theta+\pi/2) - E(\theta-\pi/2)]$ (Tilly et al., Sec. 7.2.2).

## Where the cost goes

- **Shots.** An energy estimate is an average of random outcomes. Sampling one term at a time with probability $|c_k|/\lambda$, $\lambda=\sum_k|c_k|$, gives a variance of at most $\lambda^2$, so

    $$
    N_{\rm shots} \lesssim (\lambda/\epsilon)^2 .
    $$

    $\lambda$ grows with system size. Tilly et al. (Sec. 5.1.1) quote a conservative estimate of $O(10^{19})$ shots for the energy of the Fe$_2$S$_2$ ferredoxin cluster in STO-3G (112 spin orbitals), and note that optimization needs gradient differences, which are smaller still. Grouping commuting terms, measuring in rotated bases and classical shadows reduce the constant (Tilly et al., Sec. 5). Robledo-Moreno et al. (2025) cite this measurement wall as one reason to sample determinants instead ([[sample-based-quantum-diagonalization]]).
- **Expressivity versus trainability.** Deep, generic circuits can represent more states but suffer **barren plateaus**: gradients that vanish exponentially in the number of qubits (Tilly et al., Sec. 6.1.3).
- **Noise.** Gate errors bias $E(\boldsymbol\theta)$ and can break the variational bound in practice. Error mitigation (zero-noise extrapolation, symmetry verification, probabilistic error cancellation) trades more shots for less bias (Tilly et al., Sec. 8).
- **Nested loops.** Inside a geometry optimization, a full VQE at every geometry is the dominant cost. Hao et al. (2026) instead update geometry and circuit parameters together ([[dmet-with-quantum-solvers]]).

## Relation to classical methods

- **UCC.** The unitary coupled-cluster ansatz $e^{\hat T-\hat T^\dagger}$ is variational (exact for minimal-basis H$_2$, worked example below) but, because $\hat T-\hat T^\dagger$ contains de-excitations, its Baker-Campbell-Hausdorff expansion does not terminate, so classical UCC must be truncated. A circuit implements the exponential directly, after Trotterization (Tilly et al., Sec. 6.2.2).
- **QPE.** Quantum phase estimation projects onto an eigenstate and needs fault tolerance; VQE trades that for many short circuits and a classical optimization (Sec. 2.5).

## Worked example

!!! example "H$_2$, STO-3G, 0.735 Å: one-parameter UCCD"
    Qubit Hamiltonian from [[jordan-wigner-mapping]] (15 Pauli strings). Script: `jw_vqe.py`.

    - **Ansatz.** $|\psi(\theta)\rangle = e^{\theta(\hat\tau-\hat\tau^\dagger)}|1100\rangle$ with $\hat\tau = a^\dagger_{2}a^\dagger_{3}a_{1}a_{0}$, the only double excitation. Since $(\hat\tau-\hat\tau^\dagger)^2 = -1$ on the two-determinant space, $|\psi\rangle = \cos\theta|1100\rangle + \sin\theta\,\hat\tau|1100\rangle$ exactly.
    - **Optimum.** $\theta^* = -0.1117685$, $E = -1.137306035753\ E_h$, equal to FCI ($|\Delta E| = 4\times10^{-16}$). Symmetry leaves only this one determinant to mix with HF, so UCCD is exact here.
    - **Variance.** $\operatorname{Var}(\hat H) = 0$ in the optimum, since it is an eigenstate. Shot noise then comes only from the term-by-term estimator.
    - **Shot budget.** $\lambda = \sum_{k\neq I}|c_k| = 1.894$, so the importance-sampling bound for $\epsilon = 1.6$ m$E_h$ is $(\lambda/\epsilon)^2 \approx 1.4\times10^6$ shots per energy, for a 4-qubit problem.

## Source

- J. Tilly et al., *Phys. Rep.* **986**, 1 (2022), doi:10.1016/j.physrep.2022.08.003. Sec. 2 (definition, pipeline, comparison with FCI, CC and QPE); Sec. 5 (measurement); Sec. 6.1.3 (barren plateaus); Sec. 7 (optimizers, parameter shift); Sec. 8 (error mitigation).
- J. Robledo-Moreno et al., *Sci. Adv.* **11**, eadu9991 (2025), doi:10.1126/sciadv.adu9991, Discussion: measurement cost of VQE estimators for large active spaces.
- The importance-sampling variance bound is standard; shot scaling is discussed in Tilly et al., Sec. 5.1 (Eq. 85 for the upper bound).
