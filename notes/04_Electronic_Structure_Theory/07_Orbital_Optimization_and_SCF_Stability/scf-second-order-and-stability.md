---
id: scf-second-order-and-stability
title: Hartree-Fock as an optimization problem - quadratic SCF, Brillouin-based Fock operators and stability
summary: The single-determinant case of second-order MCSCF. The quadratically convergent exp(κ) Newton scheme solves W = (A−B)κ with only occupied-virtual rotations; the Brillouin-theorem route instead builds a Fock potential whose occupied-virtual block is fixed by ⟨0|[H, r†s]|0⟩ = 0 and whose diagonal blocks are free, which is why orbital energies are a convention. The Hessian at convergence decides stability; for minimal-basis H2 the RHF→UHF instability appears at R = 2.18 bohr. Computed Newton versus Roothaan iterations for water.
status: in-progress
kind: algorithm
level: intermediate
tags: [hartree-fock, second-order-scf, newton-raphson, stability-analysis, brillouin, fock-potential, orbital-hessian, roothaan]
prerequisites: [orbital-rotations, scf-procedure, brillouin-theorem]
related: [mcscf-second-order-optimization, h2-dissociation-rhf-uhf, koopmans-theorem, uhf, spin-tensor-operators, heh-plus-minimal-basis-model, baker-campbell-hausdorff, polarization-propagator-rpa, molecular-properties-and-response]
order: 40
date: 2026-11-03
---

## Hartree-Fock as the one-configuration MCSCF

With a single configuration there are no state rotations ($\mathbf P$ and $\mathbf V$ disappear) and the second-order equations of [[mcscf-second-order-optimization]] reduce to

$$
\mathbf W = (\mathbf A_{11} - \mathbf B_{11})\,\boldsymbol\kappa,
\qquad
W_{rs} = \langle0|[a_s^\dagger a_r, \hat H]|0\rangle .
$$

Only rotations between occupied and unoccupied spin orbitals are nonredundant ([[orbital-rotations]]). Iterating this Newton step converges quadratically. Its drawback, as J-S note, is that each step needs a partial transformation of the two-electron integrals, and the procedure produces no orbital energies.

## The Brillouin-theorem route to a Fock operator

**Starting point.** Require only the first-order condition (Brillouin's theorem, [[brillouin-theorem]]):

$$
\langle0|[\hat H, a_r^\dagger a_s]|0\rangle = 0 .
$$

**Decomposition.** Split $\hat H = \hat F - \hat V + \hat W$, where $\hat W$ is the electron repulsion, $\hat F = \sum_{rs}(h_{rs} + V_{rs})a_r^\dagger a_s$ is a Fock operator that the chosen orbitals diagonalize, $h_{rs} + V_{rs} = \delta_{rs}\varepsilon_r$, and $\hat V = \sum V_{rs}a_r^\dagger a_s$ is a Fock potential still to be fixed.

**What the Brillouin condition determines.** Inserting this into the commutator, with a diagonal one-particle density matrix $\langle0|a_r^\dagger a_s|0\rangle = \delta_{rs}\nu_r$ (occupation numbers $\nu_r$, not necessarily 0 or 1 for a multi-determinant single configuration), gives

$$
V_{rs}(\nu_r - \nu_s) = \frac12\sum_{jkl}\Big(\langle sk||jl\rangle\langle0|a_r^\dagger a_k^\dagger a_l a_j|0\rangle + \langle lk||jr\rangle\langle0|a_l^\dagger a_k^\dagger a_j a_s|0\rangle\Big)
$$

(J-S Eq. 2.89 with the factor ½ restored; $\langle ij||kl\rangle = \langle ij|kl\rangle - \langle ij|lk\rangle$ as in their Eq. 2.87). The potential is **determined only where $\nu_r\ne\nu_s$**: between orbitals of different occupation.

!!! example "Correction to J-S Eq. (2.89): a missing factor ½ (checked for this note)"
    **Derivation.** With J-S's own two-electron operator $\hat W = \tfrac12\sum\langle rs|tu\rangle a_r^\dagger a_s^\dagger a_ua_t$ (their Eq. 1.16), expanding $\langle0|[a_r^\dagger a_s, \hat W]|0\rangle$ gives two pairs of equal terms. The result is $\tfrac12$ times the bracket printed in J-S Eqs. (2.86) and (2.89), where the factor is missing. The one-body terms of Eq. (2.86) give $V_{rs}(\nu_r - \nu_s)$ as stated, so the printed (2.89) is too large by a factor 2.

    **Numerical test.** Linear H$_4$ (STO-3G, 8 spin orbitals), Fock-space matrices, exact $\langle0|[a_r^\dagger a_s, \hat W]|0\rangle$ against the printed bracket $T_{rs}$:

    - **A closed-shell determinant in randomly rotated orbitals:** $\max|T - 2C| = 4\times10^{-16}$, while $T - C$ and $T + C$ are of order 0.15-0.45.
    - **An open-shell singlet CSF** with occupations ½: $\max|T - 2C| = 1\times10^{-15}$.
    - **Consistency with J-S Eq. (2.90).** For a determinant, $C_{rs} = (\nu_r - \nu_s)\sum_\gamma\langle r\gamma||s\gamma\rangle$ to $5\times10^{-16}$. J-S's own Eq. (2.90) therefore requires the factor ½ in (2.89).

**Closed-shell determinant.** For occupied $\gamma$ and unoccupied $m$, the condition fixes $V_{m\alpha} = \sum_\gamma\langle m\gamma||\alpha\gamma\rangle$, the usual Hartree-Fock potential in the occupied-virtual block. The occupied-occupied and virtual-virtual blocks are free.

**The free blocks are a choice.** Any choice of the undetermined blocks leads, at convergence, to the same stationary determinant: the free blocks only mix occupied orbitals among themselves and virtual orbitals among themselves, which leaves the determinant unchanged. They do change the orbitals and orbital energies.

- **Canonical choice.** Using the same formula in every block, $V_{rs} = \sum_\gamma\langle r\gamma||s\gamma\rangle$, gives canonical Hartree-Fock orbitals whose energies are Koopmans ionization energies and electron affinities ([[koopmans-theorem]]).
- **Other choices.** For example Kelly's $V^{N-1}$ potential for the virtual block, which makes virtual orbitals better suited to excitation energies. For open shells with doubly, singly and unoccupied orbitals there are three free diagonal blocks and many conventions (ROHF variants).

**Iteration.** Build $\mathbf F = \mathbf h + \mathbf V$ from the current orbitals, diagonalize, repeat: this is the Roothaan procedure ([[scf-procedure]]). It is first order (linearly convergent), but needs only a two-index transformation of the integrals.

!!! example "Water, STO-3G, from the core-Hamiltonian guess (computed for this note)"
    **Newton** on $E(\boldsymbol\kappa)$ with the 10 occupied-virtual rotations, numerical gradient and Hessian, level-shifted (augmented-Hessian) steps capped at 0.5:

    | Iteration | $E - E_{\text{SCF}}$ | Gradient norm | Lowest Hessian eigenvalue |
    |---:|---:|---:|---:|
    | 0 | 1.73 | 2.95 | −1.49 |
    | 1 | 0.430 | 2.12 | +0.68 |
    | 2 | 5.0e−3 | 0.235 | +2.16 |
    | 3 | 3.7e−7 | 1.5e−3 | +2.10 |
    | 4 | <1e−11 | 3.6e−7 | +2.10 |

    **Roothaan** (no damping, no DIIS) from the same guess: energy errors 1.73, 1.7e−2, 8.5e−4, 1.2e−4 after 0-3 iterations, 3.7e−6 after 5 and 8.5e−10 after 10, settling into a linear reduction by a factor of about 5.5 per iteration.

    - **Newton** needs fewer iterations once the Hessian is positive definite; its gradient roughly squares each step.
    - **Roothaan** iterations are much cheaper and, for an easy closed shell like this, converge quickly anyway. The core guess is a saddle point of $E(\boldsymbol\kappa)$ (negative Hessian eigenvalue), which a plain Newton step would not handle.

## Stability: what the Hessian says at convergence

**Statement.** A converged SCF solution satisfies $\mathbf W = 0$, but it is a minimum only if the Hessian $\mathbf A - \mathbf B$ is positive definite. Including in the Hessian rotations that break a constraint imposed on the wave function tests whether relaxing the constraint lowers the energy (general knowledge, consistent with J-S's discussion of symmetry-preserving tensor operators):

- **Real RHF → real UHF (triplet) instability:** rotations generated by triplet operators ([[spin-tensor-operators]]), which give the $\alpha$ and $\beta$ orbitals different shapes.
- **Real → complex instability:** rotations generated by the imaginary part of $\boldsymbol\lambda$.
- **Spatial symmetry breaking:** rotations between orbitals of different symmetry.

**Minimal-basis H₂.** The only triplet rotation mixes $\psi_1$ and $\psi_2$ with opposite angles for $\alpha$ and $\beta$ ([[h2-dissociation-rhf-uhf]]). The curvature of the energy at the RHF point is

$$
\frac{d^2E}{d\theta^2}\Big|_0 = 4\big(h_{22} - h_{11} - J_{11} + J_{12} - 2K_{12}\big) = 4\big(\varepsilon_2 - \varepsilon_1 - J_{12} - K_{12}\big),
$$

using $\varepsilon_1 = h_{11} + J_{11}$ and $\varepsilon_2 = h_{22} + 2J_{12} - K_{12}$. The second form is the triplet orbital-Hessian element: orbital-energy gap minus the particle-hole interaction.

!!! example "STO-3G H₂ (computed for this note)"
    | R (bohr) | $\varepsilon_2 - \varepsilon_1 - J_{12} - K_{12}$ (hartree) |
    |---:|---:|
    | 1.4 | +0.4036 |
    | 2.0 | +0.0737 |
    | 2.18 | −0.0001 |
    | 2.4 | −0.0797 |
    | 3.0 | −0.2505 |

    The root is $R_c = 2.1797$ bohr: beyond it RHF is a saddle point and a lower UHF solution exists. Szabo quotes "in the vicinity of 2.3 a.u." from his tabulated integrals; the analytic root with PySCF integrals is 2.180, matching the value in [[h2-dissociation-rhf-uhf]]. The two expressions for the curvature agree at every R (ratio exactly 4).

    The same quantity is the triplet $A + B$ of the RPA (TDHF) equations. As it passes through zero, the triplet excitation energy becomes imaginary: the instability shows up in the response calculation as well ([[polarization-propagator-rpa]]).

!!! example "HeH⁺ in a minimal Slater basis: J-S Problems 2.1-2.2 recomputed"
    **First order.** Roothaan SCF from the guess $\phi_1 = 1s_{\text{He}}$ converges linearly, with energy errors shrinking by a factor of about 6 per step in J-S's formula-(C) energies.

    **Second order.** The $e^{-\boldsymbol\kappa}$ Newton scheme uses the closed-shell matrices $W = -0.2882$, $A_{11} = 1.8716$, $B_{11} = -0.1532$ (J-S −0.2880, 1.8713, −0.1530). It converges quadratically: −2.80512857, −2.84313838, −2.84352780, −2.84352782.

    Explicit closed-shell formulas for $A_{11}$, $B_{11}$ and $W$, and all numbers, are in [[heh-plus-minimal-basis-model]].

**Why it matters.** At the instability point the RHF-based perturbation series begins to deteriorate ([[mp2]]), and for MCSCF the same Hessian analysis tells whether a solution is the intended state or a saddle point.

## Source

Jørgensen and Simons, *Second Quantization-Based Methods in Quantum Chemistry* (Academic Press, New York, 1981), Ch. 2, Sec. C "Single-Configuration Self-Consistent Field Methods", pp. 35-39, Eqs. (2.80)-(2.92); Problems 2.1-2.2, pp. 48-52; symmetry of rotation operators, Sec. B.8, pp. 30-31. Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996; reprint of the revised first edition, McGraw-Hill, 1989), Sec. 3.8.7, pp. 221-229, Ex. 3.42-3.43 (instability point). The stability classification is general knowledge. All numbers computed for this note with PySCF 2.14.
