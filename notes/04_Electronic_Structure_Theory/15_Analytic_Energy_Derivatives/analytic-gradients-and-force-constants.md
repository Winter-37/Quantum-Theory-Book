---
id: analytic-gradients-and-force-constants
title: Analytic molecular gradients and force constants - nuclear displacements as a perturbation, Hellmann-Feynman forces, orbital response and basis-set (Pulay) terms
summary: A nuclear displacement u changes the electronic Hamiltonian through the electron-nuclear attraction. Treated as a perturbation in the MCSCF response formalism, it gives E(u) = E₀ + Σ u·V₁ + Σ u·M·u, with Hellmann-Feynman forces V₁, field-gradient terms V₂ and orbital/CI response D in the force-constant matrix M = V₂ − D. This assumes a complete basis. With atom-centred basis functions, derivatives of the basis functions (Pulay forces) must be added, either by enlarging the basis or by differentiating integrals. Water calculations show the Hellmann-Feynman-only gradient is useless in small bases.
status: in-progress
kind: derivation
level: advanced
tags: [analytic-gradients, force-constants, hessian, hellmann-feynman, pulay-forces, integral-derivatives, nuclear-displacement]
prerequisites: [molecular-properties-and-response, mcscf-second-order-optimization, gaussian-basis-functions]
related: [geometry-optimization, born-oppenheimer-approximation, molecular-hamiltonian, scf-procedure, rhf-analytic-gradient, ci-analytic-gradient, rhf-analytic-hessian]
order: 20
date: 2026-11-03
---

## Nuclear displacement as a perturbation

**Expansion of the potential.** Move nucleus $A$ from $\mathbf R_A^0$ to $\mathbf R_A^0 + \mathbf u_A$. Only the electron-nuclear attraction depends explicitly on nuclear positions ([[molecular-hamiltonian]]). By Taylor expansion,

$$
|\mathbf r - \mathbf R_A^0 - \mathbf u_A|^{-1} = |\mathbf r - \mathbf R_A^0|^{-1} - (\mathbf u_A\cdot\nabla)|\mathbf r - \mathbf R_A^0|^{-1} + \tfrac12(\mathbf u_A\cdot\nabla)^2|\mathbf r - \mathbf R_A^0|^{-1} + O(u_A^3),
$$

with $\nabla$ acting on $\mathbf r$.

**First- and second-order operators.** Multiplying by $-Z_A$ and writing the result in second quantization:

$$
V_1 = \sum_A\sum_{rs}Z_A\big\langle\phi_r\big|(\mathbf u_A\cdot\nabla)|\mathbf r - \mathbf R_A^0|^{-1}\big|\phi_s\big\rangle r^\dagger s,
$$

$$
V_2 = -\tfrac12\sum_A\sum_{rs}Z_A\big\langle\phi_r\big|(\mathbf u_A\cdot\nabla)^2|\mathbf r - \mathbf R_A^0|^{-1}\big|\phi_s\big\rangle r^\dagger s .
$$

$V_1$ is the force exerted on the electrons by the displaced nuclei; $V_2$ contains electric-field-gradient integrals at the nuclei. (Nuclear repulsion is added classically.)

## Energy through second order

**Mapping onto the response formalism.** Identify $\alpha H_1\to V_1$ and $\alpha^2H_2\to V_2$ in the MCSCF result of [[molecular-properties-and-response]]. Then

$$
\langle0|V_1|0\rangle = \sum_A\mathbf u_A\cdot\mathbf V_{1A},\qquad V_{1A}^i = \sum_{rs}Z_A\langle\phi_r|\partial_i|\mathbf r - \mathbf R_A^0|^{-1}|\phi_s\rangle\langle0|r^\dagger s|0\rangle,
$$

the **Hellmann-Feynman force**: the one-electron density contracted with derivative integrals. The second-order expectation value gives a tensor $\mathbf V_{2A}$. The response term becomes $\sum_{AB}\mathbf u_A\cdot\mathbf D_{AB}\cdot\mathbf u_B$, with

$$
D_{AB}^{ij} = \big(\mathbf F_A^i\ \mathbf G_A^i\big)(\mathbf A - \mathbf B)^{-1}\begin{pmatrix}\mathbf F_B^j\\ \mathbf G_B^j\end{pmatrix},\qquad \mathbf F_A^i = \sum_{rs}Z_A\langle\phi_r|\partial_i|\mathbf r - \mathbf R_A^0|^{-1}|\phi_s\rangle\langle0|[\mathbf Q, r^\dagger s]|0\rangle,
$$

and $\mathbf G_A^i$ defined analogously with the state-rotation operators $\mathbf R$.

**Result (J-S Eqs. 5.51-5.52).**

$$
E(\mathbf u) = \langle0|H|0\rangle + \sum_A\mathbf u_A\cdot\mathbf V_{1A} + \sum_{AB}\mathbf u_A\cdot\mathbf M_{AB}\cdot\mathbf u_B,\qquad \mathbf M_{AB} = \mathbf V_{2A}\delta_{AB} - \mathbf D_{AB}.
$$

The force-constant matrix $\mathbf M$ (half the Cartesian Hessian) has three parts:

- **Field-gradient terms** in $\mathbf V_2$.
- **Response of the wave function** in $\mathbf D$: the change of MCSCF orbitals and CI coefficients with nuclear displacement, obtained from one linear solve with the MCSCF Hessian.
- **Hellmann-Feynman forces**, which give the gradient.

**Stationary points.** These satisfy $\langle0|V_1|0\rangle = 0$, i.e. vanishing Hellmann-Feynman forces. Locating them is the subject of [[geometry-optimization]].

## The basis moves with the nuclei

**The hidden assumption.** The derivation writes the Hamiltonian at $\mathbf R^0$ and at $\mathbf R^0 + \mathbf u$ in the **same** orbitals. That is exact only for a complete basis. Real calculations use atom-centred functions that move with the nuclei. Integrating $|\mathbf r - \mathbf R_A|^{-1}$ over a density that moves with $A$ is equivalent to expanding the density, $\rho(\mathbf r - \mathbf u_A)$, which brings in derivatives of the basis functions.

**J-S's two remedies.**

1. **Enlarge the basis** so that the first and second derivatives of the important functions lie in it. The derivative of a Cartesian Gaussian is a combination of Gaussians with angular momentum one higher and one lower ([[gaussian-basis-functions]]). Adding those functions makes the formalism above exact for the dominant orbitals.
2. **Differentiate the integrals** explicitly (Thomsen and Swanstrom, 1973, as cited by J-S). For CH₂ in an s, p basis, second derivatives of $(pp|pp)$ involve only integrals like $(pp|pf)$ and $(pp|dd)$, never $(dd|dd)$ or $(ff|ff)$. A basis enlarged with full d and f sets would need all of those.

J-S note that the second route had become the standard one. It is how all modern analytic gradient codes work; the extra contributions are now called **Pulay forces** (general knowledge).

!!! example "Hellmann-Feynman versus analytic RHF gradients, water (computed for this note)"
    Geometry: R(OH) = 1.95 bohr, HOH = 110°, deliberately away from equilibrium. "HF-only" contracts the converged density with derivatives of the nuclear-attraction operator (basis held fixed) and adds the nuclear-repulsion force.

    | Basis | Analytic $|\mathbf g|$ | HF-only $|\mathbf g|$ | Max Pulay component |
    |---|---:|---:|---:|
    | STO-3G | 0.08029 | 2.88198 | 2.894 |
    | 6-31G | 0.11993 | 1.86606 | 1.938 |
    | cc-pVTZ | 0.13840 | 0.33131 | 0.389 |

    - **STO-3G oxygen.** The z-force on O is −0.01256 analytically but 2.88183 from Hellmann-Feynman alone. The minimal basis cannot polarize the O 1s core to follow its moving nucleus.
    - **Trend.** The Pulay term shrinks with basis size but is still larger than the true gradient in cc-pVTZ. Hellmann-Feynman forces become accurate only near the complete-basis limit, or with floating or derivative-augmented bases (J-S's remedy 1).

## Source

Jørgensen and Simons, *Second Quantization-Based Methods in Quantum Chemistry* (Academic Press, New York, 1981), Ch. 5, Sec. G, pp. 113-116, Eqs. (5.38)-(5.52). The term "Pulay forces" and the remark on modern codes are general knowledge. Water gradients computed with PySCF 2.14.
