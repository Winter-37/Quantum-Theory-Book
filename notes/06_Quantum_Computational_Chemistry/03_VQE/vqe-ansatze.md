---
id: vqe-ansatze
title: VQE ansätze - hardware-efficient, unitary coupled cluster, symmetry-preserving and adaptive circuits
summary: The ansatz decides what VQE can represent and whether it can be trained. Hardware-efficient circuits are shallow and native to the device but conserve no symmetry and suffer barren plateaus. UCCSD is chemically motivated, conserves N and S_z and connects to CC, but is deep after Trotterization. Symmetry-preserving gates, the Hamiltonian variational ansatz, and adaptive constructions (ADAPT-VQE, iQCC) sit in between. On H2 a one-layer hardware-efficient circuit converges to a one-electron state; two layers or one UCCD parameter reach FCI.
status: in-progress
kind: comparison
level: intermediate
tags: [VQE, ansatz, UCCSD, hardware-efficient, ADAPT-VQE, barren-plateau, symmetry]
prerequisites: [variational-quantum-eigensolver, coupled-cluster-second-quantization]
related: [lucj-ansatz, baker-campbell-hausdorff]
order: 20
date: 2026-11-08
---

Notation: as in [[variational-quantum-eigensolver]]. $\hat T = \hat T_1 + \hat T_2$ the coupled-cluster excitation operator in spin orbitals; $M$ qubits.

## Fixed-structure ansätze

**Hardware-efficient ansatz (HEA)** (Tilly et al. 2022, Sec. 6.2.1). Layers of single-qubit rotations followed by entangling gates in the device's native pattern:

$$
U(\boldsymbol\theta) = \prod_{l=1}^{L}\Big[U_{\rm ent}\prod_{j}R_y(\theta_{lj})\Big].
$$

- **For.** Shallow, uses only native gates, few parameters per layer.
- **Against.** No particle-number or spin symmetry, so the optimizer can leave the target sector. Random-like circuits of growing depth have **barren plateaus** (gradients vanishing exponentially in $M$; Tilly et al., Sec. 6.1). No systematic improvability.

**Unitary coupled cluster (UCC)** (Sec. 6.2.2).

$$
|\psi\rangle = e^{\hat T(\boldsymbol\theta) - \hat T^\dagger(\boldsymbol\theta)}|\Phi_{\rm HF}\rangle .
$$

- **For.** Conserves $N$ and $S_z$; parameters have a meaning (amplitudes, initializable from MP2 or CCSD); variational, unlike CC.
- **Against.** Gate count. Each excitation operator becomes a Pauli-string exponential after Jordan-Wigner, the exponential of the sum must be Trotterized (which makes the result depend on operator ordering), and the number of doubles grows as $O(M^4)$.
- **Variants.** Generalized and paired forms (k-UpCCGSD) reduce depth.

**Symmetry-preserving ansätze** (Sec. 6.2.3). Gates such as particle-conserving two-qubit rotations keep $N$ (and sometimes $S^2$) by construction, removing the wrong-sector failure of the HEA.

**Hamiltonian variational ansatz** (Sec. 6.2.4). Alternate exponentials of the non-commuting parts of $\hat H$, in the spirit of adiabatic state preparation.

**Locality-restricted unitary cluster Jastrow (LUCJ).** Orbital rotations around density-density phases, with interactions restricted to the qubit connectivity. It is mostly used as a sampler rather than optimized ([[lucj-ansatz]]).

## Adaptive ansätze

- **ADAPT-VQE** (Sec. 6.3.1). Grow the circuit one operator at a time from a pool (fermionic excitations or qubit operators), each time adding the operator with the largest energy gradient $|\langle\psi|[\hat H,\hat A_k]|\psi\rangle|$, then re-optimize. Compact circuits, at the cost of many gradient measurements.
- **iQCC** (Sec. 6.3.2). Dress the Hamiltonian iteratively with qubit-coupled-cluster entanglers, keeping the circuit short and moving complexity into a growing Hamiltonian.

## Worked example

!!! example "H$_2$, STO-3G: HEA against UCCD"
    4 qubits, Jordan-Wigner Hamiltonian of [[jordan-wigner-mapping]], start $|1100\rangle$. HEA layer: $R_y$ on each qubit, then CNOTs $(0,1),(1,2),(2,3)$. BFGS from 20 random starts. Script: `hea.py`.

    | ansatz | parameters | $E-E_{\rm FCI}$ ($E_h$) | $\langle\hat N\rangle$ |
    |---|---|---|---|
    | UCCD | 1 | $4\times10^{-16}$ | 2 |
    | HEA, $L=1$ | 4 | $+0.601$ | 1.000 |
    | HEA, $L=2$ | 8 | $<10^{-15}$ | 2.000 |
    | HEA, $L=3$ | 12 | $<10^{-15}$ | 2.000 |

    - **Wrong sector.** With one layer the best state found is a one-electron state ($\langle\hat N\rangle = 1$, $\operatorname{Var}\hat N = 0$). It is the lowest energy that circuit can reach. Nothing in the HEA forbids it.
    - **Why no state below FCI.** Here the lowest eigenvalue of the full Fock-space Hamiltonian happens to be the two-electron ground state. For a molecule whose anion or cation is lower, an unconstrained HEA could converge below the neutral FCI energy; a penalty $\beta(\hat N-N)^2$ or symmetry-preserving gates prevent this.
    - **Parameter count.** UCCD needs one parameter because the ansatz is built from the physics.

## Source

- J. Tilly et al., *Phys. Rep.* **986**, 1 (2022), doi:10.1016/j.physrep.2022.08.003. Sec. 6.1 (barren plateaus), 6.2.1-6.2.4 (HEA, UCC and extensions, symmetry-preserving, HVA), 6.3 (ADAPT-VQE, iQCC, structure optimization), 6.4 (discussion).
- Numbers computed here.
