---
id: uhf
title: Unrestricted Hartree-Fock and the Pople-Nesbet equations
summary: Different spatial orbitals for α and β electrons. The coupled α and β Fock operators, the Pople-Nesbet matrix equations F^α C^α = S C^α ε^α and F^β C^β = S C^β ε^β, total and spin density matrices, the UHF energy, and a CH3 radical example with spin contamination and spin density.
status: in-progress
kind: derivation
level: intermediate
tags: [hartree-fock, uhf, pople-nesbet, open-shell, spin-density, spin-contamination]
prerequisites: [rhf, spin-adapted-configurations]
related: [h2-dissociation-rhf-uhf, scf-procedure, fock-operator]
order: 100
date: 2026-11-03
---

## Unrestricted spin orbitals

Open-shell systems ($N^\alpha > N^\beta$) or stretched bonds need extra freedom. Unrestricted Hartree-Fock (UHF) uses separate orthonormal spatial sets for each spin ([[spin-adapted-configurations]]):

$$
\chi_j(\mathbf x) = \psi_j^\alpha(\mathbf r)\,\alpha(\omega)\quad\text{or}\quad\psi_j^\beta(\mathbf r)\,\beta(\omega),
\qquad
|\Psi_0^{\text{UHF}}\rangle = |\psi_1^\alpha\bar\psi_1^\beta\psi_2^\alpha\bar\psi_2^\beta\cdots\rangle .
$$

There are $N^\alpha$ occupied $\alpha$ and $N^\beta$ occupied $\beta$ spatial orbitals. Labels $a, b$ below refer to occupied orbitals of the indicated spin.

## Spatial Fock operators

Integrate the spin-orbital Fock operator ([[fock-operator]]) over spin, separately for $\alpha$ and $\beta$ (Szabo Ex. 3.33):

$$
f^\alpha(1) = h(1) + \sum_a^{N^\alpha}\big[J_a^\alpha(1) - K_a^\alpha(1)\big] + \sum_a^{N^\beta}J_a^\beta(1),
$$

$$
f^\beta(1) = h(1) + \sum_a^{N^\beta}\big[J_a^\beta(1) - K_a^\beta(1)\big] + \sum_a^{N^\alpha}J_a^\alpha(1),
$$

$$
f^\alpha\psi_j^\alpha = \varepsilon_j^\alpha\psi_j^\alpha,
\qquad
f^\beta\psi_j^\beta = \varepsilon_j^\beta\psi_j^\beta .
$$

**Coupling.**

- An $\alpha$ electron feels the Coulomb field of all electrons, but exchange only with other $\alpha$ electrons.
- The two equations are coupled through the Coulomb terms, so they must be solved together.
- When $N^\alpha\neq N^\beta$ the exchange fields differ, so $\psi^\alpha\ne\psi^\beta$ (spin polarization).

**Orbital energies (Szabo Ex. 3.35).**

$$
\varepsilon_i^\alpha = h_{ii}^{\alpha\alpha} + \sum_a^{N^\alpha}\big(J_{ia}^{\alpha\alpha} - K_{ia}^{\alpha\alpha}\big) + \sum_a^{N^\beta}J_{ia}^{\alpha\beta},
$$

and similarly for $\beta$. The superscripts say which spatial set each orbital index belongs to.

**Energy.**

$$
E_0 = \tfrac12\Big[\sum_a^{N^\alpha}\big(h_{aa}^{\alpha} + \varepsilon_a^\alpha\big) + \sum_a^{N^\beta}\big(h_{aa}^{\beta} + \varepsilon_a^\beta\big)\Big].
$$

**Example: Li (Szabo Ex. 3.34).** For $|\psi_1^\alpha\bar\psi_1^\beta\psi_2^\alpha\rangle$,

$$
E_0 = h_{11}^{\alpha} + h_{11}^{\beta} + h_{22}^{\alpha} + J_{11}^{\alpha\beta} + J_{12}^{\alpha\alpha} - K_{12}^{\alpha\alpha} + J_{12}^{\beta\alpha}.
$$

Here $J_{12}^{\beta\alpha}$ is the Coulomb integral between $\psi_1^\beta$ and $\psi_2^\alpha$. This is the pseudo-classical bookkeeping of [[spin-orbital-to-spatial-orbital]] with separate spatial orbitals per spin.

## Pople-Nesbet equations

Expand both sets in one basis $\{\phi_\mu\}$:

$$
\psi_i^\alpha = \sum_\mu C_{\mu i}^\alpha\phi_\mu,
\qquad
\psi_i^\beta = \sum_\mu C_{\mu i}^\beta\phi_\mu .
$$

$$
\mathbf F^\alpha\mathbf C^\alpha = \mathbf S\mathbf C^\alpha\boldsymbol\varepsilon^\alpha,
\qquad
\mathbf F^\beta\mathbf C^\beta = \mathbf S\mathbf C^\beta\boldsymbol\varepsilon^\beta .
$$

**Density matrices.**

$$
P_{\mu\nu}^\alpha = \sum_a^{N^\alpha}C_{\mu a}^\alpha C_{\nu a}^{\alpha*},
\qquad
P_{\mu\nu}^\beta = \sum_a^{N^\beta}C_{\mu a}^\beta C_{\nu a}^{\beta*},
\qquad
\mathbf P^T = \mathbf P^\alpha + \mathbf P^\beta,
\qquad
\mathbf P^S = \mathbf P^\alpha - \mathbf P^\beta .
$$

**Fock matrices.** With chemists' integrals ([[integral-notation]]):

$$
F_{\mu\nu}^\alpha = H_{\mu\nu}^{\text{core}} + \sum_{\lambda\sigma}\Big[P_{\lambda\sigma}^T(\mu\nu|\sigma\lambda) - P_{\lambda\sigma}^\alpha(\mu\lambda|\sigma\nu)\Big],
$$

$$
F_{\mu\nu}^\beta = H_{\mu\nu}^{\text{core}} + \sum_{\lambda\sigma}\Big[P_{\lambda\sigma}^T(\mu\nu|\sigma\lambda) - P_{\lambda\sigma}^\beta(\mu\lambda|\sigma\nu)\Big].
$$

**Energy (Szabo Ex. 3.40).**

$$
E_0 = \tfrac12\sum_{\mu\nu}\Big[P_{\nu\mu}^T H_{\mu\nu}^{\text{core}} + P_{\nu\mu}^\alpha F_{\mu\nu}^\alpha + P_{\nu\mu}^\beta F_{\mu\nu}^\beta\Big].
$$

**Iteration.** The SCF loop is that of [[scf-procedure]]: build both Fock matrices from $(\mathbf P^\alpha, \mathbf P^\beta)$, diagonalize each, occupy the $N^\alpha$ and $N^\beta$ lowest.

**Closed-shell reduction.** For $N^\alpha = N^\beta$ and $\mathbf P^\alpha = \mathbf P^\beta = \tfrac12\mathbf P$, both Fock matrices reduce to the RHF matrix ([[rhf]]). The RHF solution is always a solution of the UHF equations. Whether a lower, spin-broken solution exists depends on stability ([[h2-dissociation-rhf-uhf]]). An unrestricted calculation on a closed shell needs an asymmetric initial guess to find it.

## Densities and spin properties

**Charge density.** The total density is $\rho^T(\mathbf r) = \sum_{\mu\nu}P^T_{\mu\nu}\phi_\mu(\mathbf r)\phi_\nu^*(\mathbf r)$. Spin-free one-electron expectation values use only $\mathbf P^T$ (Szabo Ex. 3.38):

$$
\langle\sum_i o(i)\rangle = \sum_{\mu\nu}P^T_{\mu\nu}(\nu|o|\mu).
$$

**Spin density.** $\rho^S(\mathbf r) = \rho^\alpha(\mathbf r) - \rho^\beta(\mathbf r) = \sum_{\mu\nu}P^S_{\mu\nu}\phi_\mu(\mathbf r)\phi_\nu^*(\mathbf r)$. Its integral is (Szabo Ex. 3.36)

$$
\int\rho^S(\mathbf r)\,\mathrm d\mathbf r = N^\alpha - N^\beta = 2\langle\hat{\mathcal S}_z\rangle .
$$

**Spin-dependent operators (Szabo Ex. 3.39).** These need $\mathbf P^S$. For the Fermi-contact-type operator $\sum_i\delta(\mathbf r_i - \mathbf R)\,s_z(i)$, the expectation value is $\tfrac12\rho^S(\mathbf R)$. Its value at a nucleus determines isotropic hyperfine coupling constants in ESR.

**Spin contamination.** The UHF determinant is not an $\hat{\mathcal S}^2$ eigenfunction. Its $\langle\hat{\mathcal S}^2\rangle$ exceeds $S(S+1)$ by $N^\beta - \sum_{ij}|S_{ij}^{\alpha\beta}|^2$ ([[spin-adapted-configurations]]).

!!! example "Planar CH₃ radical (compare Szabo Sec. 3.8.6)"
    Planar D$_{3h}$ geometry, C-H = 1.079 Å, $N^\alpha = 5$, $N^\beta = 4$. PySCF 2.14, Cartesian $d$:

    | Basis | $E_{\text{UHF}}$ | $\langle\hat{\mathcal S}^2\rangle$ | $E_{\text{ROHF}}$ | $\rho^S(\mathbf R_{\text{C}})$ (au) |
    |---|---:|---:|---:|---:|
    | STO-3G | −39.076709 | 0.7652 | −39.072133 | +0.248 |
    | 6-31G* | −39.558902 | 0.7618 | −39.554587 | +0.199 |

    **Reading the table.**

    - **Spin contamination.** The pure doublet value is $\langle\hat{\mathcal S}^2\rangle = 0.75$, so the contamination is small.
    - **Energy.** UHF lies about 4.5 mHa below restricted open-shell HF (ROHF, not in Szabo; included for comparison).
    - **Spin density at carbon.** In ROHF the unpaired electron sits in the C 2p$_z$ orbital, which has a node in the molecular plane. Its spin density at the C nucleus is therefore exactly zero. UHF gives a **positive** value because the singly occupied $\alpha$ orbital polarizes the C 1s and 2s shells. This is the effect behind the observed $^{13}$C hyperfine coupling. Szabo's Table 3.26 makes the same point with 4-31G and larger calculations.

## Source

Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996; reprint of the revised first edition, McGraw-Hill, 1989), Sec. 3.8.1-3.8.6, pp. 205-221, Eqs. (3.297)-(3.354), Ex. 3.33-3.41. CH$_3$ numbers computed for this note.
