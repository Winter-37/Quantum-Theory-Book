---
id: jordan-wigner-mapping
title: The Jordan-Wigner mapping - fermionic operators as Pauli strings, determinants as bit strings
summary: One qubit per spin orbital, |1⟩ = occupied. The annihilation operator becomes a lowering operator on its qubit times a string of Z on all lower qubits, which reproduces the fermionic sign and the anticommutation relations exactly. Every Slater determinant is a computational-basis state, which is why measuring a qubit register samples determinants (the basis of SQD). The molecular Hamiltonian becomes a weighted sum of O(M⁴) Pauli strings; for H2/STO-3G, 15 strings whose lowest two-electron eigenvalue is the FCI energy.
status: in-progress
kind: theory
level: intermediate
tags: [jordan-wigner, qubit-mapping, pauli-strings, second-quantization, bitstrings]
prerequisites: [creation-and-annihilation-operators, second-quantized-operators, slater-determinants]
related: [variational-quantum-eigensolver, sample-based-quantum-diagonalization]
order: 10
date: 2026-11-08
---

Notation: $M$ spin orbitals, labelled $j = 0,\dots,M-1$; qubit $j$ stores the occupation of spin orbital $j$. $X_j, Y_j, Z_j$ are Pauli matrices on qubit $j$; $\sigma^\pm_j = (X_j \mp iY_j)/2$ with $\sigma^-_j|1\rangle = |0\rangle$. Occupation-number vectors $|n_0 n_1\cdots n_{M-1}\rangle$ follow [[creation-and-annihilation-operators]].

## The mapping

**Fermionic signs.** In second quantization $a_j|n_0\cdots n_j\cdots\rangle = (-1)^{\sum_{k<j}n_k}\,\delta_{n_j1}\,|\cdots 0_j\cdots\rangle$. The phase counts the occupied orbitals below $j$.

**Jordan-Wigner** (Tilly et al. 2022, Sec. 4.1.1). Store $n_j$ in qubit $j$ and write the phase as a product of $Z$'s, since $Z_k|n_k\rangle = (-1)^{n_k}|n_k\rangle$:

$$
a_j = Z_0Z_1\cdots Z_{j-1}\,\sigma^-_j,\qquad a^\dagger_j = Z_0\cdots Z_{j-1}\,\sigma^+_j,\qquad
\hat n_j = a^\dagger_ja_j = \tfrac12(1 - Z_j).
$$

- **Anticommutation.** For $i<j$ the $Z_i$ in the string of $a_j$ anticommutes with $\sigma^\pm_i$, giving $\{a_i,a^\dagger_j\} = \delta_{ij}$ and $\{a_i,a_j\}=0$ exactly.
- **Locality cost.** A single fermionic operator acts on up to $M$ qubits. A hopping term $a^\dagger_pa_q$ becomes a Pauli string of weight up to $|p-q|+1$. The parity and Bravyi-Kitaev encodings trade this $O(M)$ weight for $O(\log M)$ (Tilly et al., Secs. 4.1.2-4.1.3).
- **Determinants are basis states.** A Slater determinant with occupied set $\{j\}$ is the computational-basis state with ones at those positions. Measuring all qubits in the $Z$ basis therefore returns determinants with probability $|c_D|^2$. This is the property that [[sample-based-quantum-diagonalization]] uses.

## The qubit Hamiltonian

Substituting into $\hat H = E_{\rm nuc} + \sum_{pq}h_{pq}a^\dagger_pa_q + \tfrac12\sum_{pqrs}(pq|rs)a^\dagger_pa^\dagger_ra_sa_q$ (spin-orbital integrals) and multiplying out the Pauli products gives

$$
\hat H = \sum_k c_k\,P_k,\qquad P_k\in\{I,X,Y,Z\}^{\otimes M},\quad c_k\in\mathbb R .
$$

- **Number of terms.** $O(M^4)$ strings in general, set by the number of distinct integrals.
- **Symmetries.** $\hat N = \sum_j\hat n_j$ and $\hat S_z$ commute with $\hat H$. The qubit Hamiltonian lives in all of Fock space ($2^M$ states), so the ground state of a given electron count is found within that sector; the global lowest eigenvalue can belong to another charge state.
- **Qubit reduction.** Conserved parities can be tapered off to remove qubits (Tilly et al., Sec. 4.3).

## Worked example

!!! example "H$_2$, STO-3G, 0.735 Å: 4 qubits"
    Spin orbitals ordered $(1\sigma_g\alpha, 1\sigma_g\beta, 1\sigma_u\alpha, 1\sigma_u\beta)$; operators built as $16\times16$ matrices from the definitions above. Script: `jw_vqe.py`.

    - **Anticommutators.** $\max|\{a_i,a^\dagger_j\}-\delta_{ij}| = 0$ exactly.
    - **Spectrum.** The lowest eigenvalue of the qubit Hamiltonian is $-1.137306035753\ E_h$, with $\langle\hat N\rangle = 2$, equal to PySCF's FCI energy to $10^{-16}$.
    - **Pauli decomposition** ($c_k = \operatorname{tr}(P_k\hat H)/16$): 15 nonzero strings including the identity. The largest are $-0.2258\,(Z_2+Z_3)$, $+0.1746\,Z_2Z_3$, $+0.1722\,(Z_0+Z_1)$, $+0.1689\,Z_0Z_1$. The only non-diagonal strings are $XXYY$-type, from the exchange integral.
    - **Hartree-Fock state.** $|1100\rangle$ gives $\langle H\rangle = -1.116998997$, the RHF energy.

## Source

- J. Tilly et al., "The variational quantum eigensolver: a review of methods and best practices", *Phys. Rep.* **986**, 1 (2022), doi:10.1016/j.physrep.2022.08.003. Sec. 4.1: generalized encodings (Jordan-Wigner, parity, Bravyi-Kitaev, ternary trees); Sec. 4.3: qubit reduction.
- The operator algebra above is standard; the H$_2$ numbers are computed here.
