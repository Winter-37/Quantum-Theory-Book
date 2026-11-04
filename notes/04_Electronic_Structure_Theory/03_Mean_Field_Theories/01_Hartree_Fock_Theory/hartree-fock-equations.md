---
id: hartree-fock-equations
title: Derivation of the Hartree-Fock equations
summary: Minimize the energy of a single determinant over its spin orbitals with orthonormality constraints (Lagrange multipliers ε_ba). Functional variation gives f|χ_a⟩ = Σ_b ε_ba|χ_b⟩; a unitary rotation of the occupied orbitals diagonalizes ε and gives the canonical equations f|χ_a⟩ = ε_a|χ_a⟩.
status: in-progress
kind: derivation
level: intermediate
tags: [hartree-fock, variational, lagrange-multipliers, functional-derivative, canonical-orbitals]
prerequisites: [fock-operator, slater-condon-rules, variational-principle]
related: [rhf, uhf, brillouin-theorem, change-of-basis]
also: []
date: 2026-11-03
---

## Problem

Find the single determinant $|\Psi_0\rangle = |\chi_1\cdots\chi_a\cdots\chi_N\rangle$ with the lowest energy

$$
E_0[\{\chi_a\}] = \langle\Psi_0|\hat H|\Psi_0\rangle = \sum_a^N\langle a|h|a\rangle + \tfrac12\sum_{a,b}^N\big([aa|bb] - [ab|ba]\big),
$$

subject to $\langle\chi_a|\chi_b\rangle = \delta_{ab}$. The energy expression assumes orthonormal spin orbitals ([[slater-condon-rules]]), so the constraint is needed for consistency. $E_0$ is a **functional**: a number that depends on functions.

## Functional variation

For a functional $E[\tilde\Phi]$, change the function by an arbitrary small amount, $\tilde\Phi\to\tilde\Phi + \delta\tilde\Phi$, and expand:

$$
E[\tilde\Phi + \delta\tilde\Phi] = E[\tilde\Phi] + \delta E + \mathcal O(\delta\tilde\Phi^2).
$$

$\delta E$, the part linear in $\delta\tilde\Phi$, is the first variation. A stationary point has $\delta E = 0$ for every allowed $\delta\tilde\Phi$.

**Linear-variation check.** With $\tilde\Phi = \sum_i c_i\Psi_i$ and $E = \langle\tilde\Phi|\hat H|\tilde\Phi\rangle - E(\langle\tilde\Phi|\tilde\Phi\rangle - 1)$, requiring $\delta E = 0$ for arbitrary $\delta c_i^*$ gives $\sum_j H_{ij}c_j = E c_i$, the [[linear-variation-method]].

## Lagrangian

Introduce one multiplier per constraint:

$$
\mathcal L[\{\chi_a\}] = E_0[\{\chi_a\}] - \sum_{a,b}^N\varepsilon_{ba}\big(\langle a|b\rangle - \delta_{ab}\big).
$$

$\mathcal L$ is real, and $\langle a|b\rangle^* = \langle b|a\rangle$. Taking the complex conjugate of the constraint sum therefore shows the multipliers form a Hermitian matrix, $\varepsilon_{ba} = \varepsilon_{ab}^*$ (Szabo Eq. 3.40, Ex. 3.2).

## First variation

Vary every occupied spin orbital, $\chi_a\to\chi_a + \delta\chi_a$, and keep first-order terms (Szabo Ex. 3.3):

$$
\delta\mathcal L = \sum_a^N\langle\delta\chi_a|h|\chi_a\rangle
+ \sum_{a,b}^N\big([\delta\chi_a\chi_a|\chi_b\chi_b] - [\delta\chi_a\chi_b|\chi_b\chi_a]\big)
- \sum_{a,b}^N\varepsilon_{ba}\langle\delta\chi_a|\chi_b\rangle
+ \text{c.c.} = 0 .
$$

The factor $\tfrac12$ of the two-electron term disappears because varying either orbital of a pair gives the same contribution. Rewrite the two-electron terms with the [[fock-operator]] pieces $\mathcal J_b$ and $\mathcal K_b$:

$$
\delta\mathcal L = \sum_a^N\int\mathrm d\mathbf x_1\ \delta\chi_a^*(1)\Big[h(1)\chi_a(1) + \sum_b^N\big(\mathcal J_b(1) - \mathcal K_b(1)\big)\chi_a(1) - \sum_b^N\varepsilon_{ba}\chi_b(1)\Big] + \text{c.c.} = 0 .
$$

$\delta\chi_a^*$ is arbitrary, so the bracket vanishes for each $a$:

$$
f(1)\,\chi_a(1) = \sum_b^N\varepsilon_{ba}\,\chi_b(1),
\qquad a = 1,\dots,N .
$$

## Canonical form

Rotate the occupied spin orbitals by a unitary $\mathbf U$:

$$
\chi_a' = \sum_b\chi_b U_{ba}.
$$

**The determinant is unchanged up to a phase.** Write the $N\times N$ matrix $\mathbf A$ with $A_{ia} = \chi_a(i)$. Then $\mathbf A' = \mathbf{AU}$ and $|\Psi_0'\rangle = \det(\mathbf U)\,|\Psi_0\rangle$ with $|\det\mathbf U| = 1$ ([[matrices-and-determinants]]).

**$f$ is unchanged.** $\sum_b\mathcal J_b$ and $\sum_b\mathcal K_b$ depend only on $\sum_b\chi_b(2)\chi_b^*(2')$, which is invariant under unitary mixing ([[change-of-basis]]).

**The multipliers transform as a matrix.** $\boldsymbol\varepsilon' = \mathbf U^\dagger\boldsymbol\varepsilon\mathbf U$. Because $\boldsymbol\varepsilon$ is Hermitian, $\mathbf U$ can be chosen to make it diagonal.

The **canonical spin orbitals** then satisfy

$$
f|\chi_a\rangle = \varepsilon_a|\chi_a\rangle .
$$

They are delocalized and have definite symmetry, and their eigenvalues have the Koopmans interpretation ([[koopmans-theorem]]). Other unitary choices, such as localized orbitals, give the same energy and wave function but no orbital energies.

## What has been obtained

- **Infinitely many eigenfunctions.** The canonical equation has infinitely many solutions in a complete space. The $N$ with lowest $\varepsilon$ are occupied, giving the lowest energy among single determinants in typical cases, though the aufbau choice is not guaranteed to be the global minimum. The rest are virtuals.
- **Stationary, not necessarily minimal.** The derivation gives a stationary point of $E_0$. Whether it is a minimum, and whether lower solutions exist when spin or spatial constraints are relaxed, is a stability question (see [[h2-dissociation-rhf-uhf]]).
- **Finite basis.** In a basis of $K$ spatial functions the equations become matrix equations: [[rhf]] (Roothaan) for closed shells and [[uhf]] (Pople-Nesbet) for unrestricted spin orbitals.
- **Hartree-Fock limit.** As the basis approaches completeness, the energy approaches the Hartree-Fock limit. This is still above the exact energy by the correlation energy.

## Source

Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996; reprint of the revised first edition, McGraw-Hill, 1989), Sec. 3.2, pp. 115-123, Eqs. (3.24)-(3.70), Ex. 3.2-3.3.
