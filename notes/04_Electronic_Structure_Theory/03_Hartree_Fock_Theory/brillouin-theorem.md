---
id: brillouin-theorem
title: Brillouin's theorem and the Hartree-Fock Hamiltonian
summary: Singly excited determinants do not mix with the Hartree-Fock ground state because ⟨Ψ0|H|Ψ_a^r⟩ = f_ar = 0. The Hartree-Fock Hamiltonian H0 = Σ f(i) has every determinant as an eigenfunction with eigenvalue equal to a sum of orbital energies; the fluctuation potential V = H − H0 corrects the double counting.
status: in-progress
kind: derivation
level: intermediate
tags: [hartree-fock, brillouin, single-excitations, zeroth-order-hamiltonian, perturbation-theory]
prerequisites: [fock-operator, slater-condon-rules, excited-determinants]
related: [hartree-fock-equations, koopmans-theorem, spin-orbital-to-spatial-orbital, mp2, scf-second-order-and-stability]
order: 30
date: 2026-11-03
---

## Brillouin's theorem

For the Hartree-Fock determinant $|\Psi_0\rangle$ and any single excitation $|\Psi_a^r\rangle$, the Case 2 [[slater-condon-rules]] give

$$
\langle\Psi_0|\hat H|\Psi_a^r\rangle = \langle a|h|r\rangle + \sum_b^N\langle ab||rb\rangle = \langle\chi_a|f|\chi_r\rangle .
$$

Since $f|\chi_r\rangle = \varepsilon_r|\chi_r\rangle$ and $\langle\chi_a|\chi_r\rangle = 0$,

$$
\langle\Psi_0|\hat H|\Psi_a^r\rangle = 0 .
$$

**Singly excited determinants do not interact directly with the Hartree-Fock reference.**

**It is a stationarity condition.** Brillouin's theorem only needs the occupied-virtual block $f_{ar}$ to vanish, not $f$ to be diagonal. Read the other way, it characterizes the Hartree-Fock solution: rotating occupied into virtual orbitals, $\chi_a\to\chi_a + \kappa\chi_r$, changes the energy to first order by $2\,\mathrm{Re}\,\kappa\langle\Psi_0|\hat H|\Psi_a^r\rangle$. Stationarity of $E_0$ under all such rotations is the same as $f_{ar} = 0$. Gradient-based SCF solvers drive exactly this quantity to zero.

**Consequences.**

- **Truncated CI.** In CI on top of Hartree-Fock (Szabo Ch. 4), singles enter the ground state only indirectly, through doubles. CISD has small singles amplitudes, and CIS gives no correlation to the ground state.
- **Second-order energy.** In MP2, the second-order energy contains only doubles.
- **One-particle properties.** For one-electron properties, singles matter more than their energy contribution suggests.

!!! example "Minimal-basis H₂"
    The only single excitations are ungerade or have $M_S\ne0$, so they vanish by symmetry anyway ([[minimal-basis-h2-model]]). Brillouin's theorem is the general statement that does not need symmetry.

## The Hartree-Fock Hamiltonian

Define the **Hartree-Fock (zeroth-order) Hamiltonian** as a sum of Fock operators:

$$
\hat H_0 = \sum_{i=1}^N f(i) = \sum_i\big[h(i) + v^{\text{HF}}(i)\big].
$$

**Every determinant is an eigenfunction (Szabo Ex. 3.7).** $\hat H_0$ is a sum of one-electron operators that is symmetric under permutation of electron labels, so it commutes with antisymmetrization. Acting on each Hartree product of canonical spin orbitals gives the sum of their orbital energies:

$$
\hat H_0|\Psi_0\rangle = \Big(\sum_a\varepsilon_a\Big)|\Psi_0\rangle,
\qquad
\hat H_0|\Psi_{ab}^{rs}\rangle = \Big(\sum_c\varepsilon_c - \varepsilon_a - \varepsilon_b + \varepsilon_r + \varepsilon_s\Big)|\Psi_{ab}^{rs}\rangle .
$$

**The eigenvalue is not the Hartree-Fock energy.** As in [[fock-operator]], $\sum_a\varepsilon_a$ counts each electron pair twice.

## The fluctuation potential

Split the full Hamiltonian as

$$
\hat H = \hat H_0 + \hat V,
\qquad
\hat V = \sum_{i<j}r_{ij}^{-1} - \sum_i v^{\text{HF}}(i).
$$

$\hat V$ is the difference between the true instantaneous electron repulsion and its mean-field average.

**Expectation value (Szabo Ex. 3.8).** With the rules for one- and two-electron operators,

$$
\langle\Psi_0|\hat V|\Psi_0\rangle = \tfrac12\sum_{ab}\langle ab||ab\rangle - \sum_{ab}\langle ab||ab\rangle = -\tfrac12\sum_{ab}\langle ab||ab\rangle .
$$

**Hartree-Fock energy.** Combining the two pieces,

$$
E_0 = \langle\Psi_0|\hat H_0|\Psi_0\rangle + \langle\Psi_0|\hat V|\Psi_0\rangle = \sum_a\varepsilon_a - \tfrac12\sum_{ab}\langle ab||ab\rangle .
$$

In perturbation language, $E_0^{(0)} = \sum_a\varepsilon_a$ and $E_0^{(1)} = -\tfrac12\sum_{ab}\langle ab||ab\rangle$. The Hartree-Fock energy is correct through first order. Correlation starts at second order. This partition defines Møller-Plesset perturbation theory (Szabo Ch. 6).

## Source

Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996; reprint of the revised first edition, McGraw-Hill, 1989), Sec. 3.3.2-3.3.3, pp. 128-131, Eqs. (3.98)-(3.111), Ex. 3.7-3.8.
