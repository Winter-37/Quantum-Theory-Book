---
id: coupled-cluster-variants-brueckner-qcisd-open-shell
title: Variants of coupled-cluster theory - orbital-optimized and Brueckner CC, quadratic CI (QCISD) as truncated CCSD, and spin-restricted high-spin open-shell CC
summary: In OCC the singles are replaced by variational orbital rotations, exp(−κ̂)exp(T̂₀)|RHF⟩, optimized through a Lagrangian. In Brueckner CC the orbitals are instead chosen so that the singles projections vanish. Both remove Hartree-Fock-instability problems, but for ordinary molecules they differ little from CCSD; BCCD for water/cc-pVDZ is within 0.13 mE_h of CCSD. QCISD drops some commutators from CCSD, is size-extensive, costs the same, and is no better (water: 0.144/0.053 mE_h below CCSD). It cannot be used with EOM-CC. Spin-restricted open-shell CC solves the S² equations in the full projection manifold but the Schrödinger equation only on CSFs of the right spin. This keeps ⟨S²⟩ exact through the Lagrangian. For comparison, UCCSD removes most of UHF's spin contamination in CN (UHF ⟨S²⟩ 1.149 → UCCSD 0.753).
status: in-progress
kind: comparison
level: advanced
tags: [coupled-cluster, brueckner, orbital-optimized-cc, qcisd, quadratic-ci, open-shell, spin-restricted-cc, spin-contamination, uccsd]
prerequisites: [coupled-cluster-hierarchy-and-size-extensivity, coupled-cluster-optimization-and-lagrangian]
related: [closed-shell-ccsd-t1-transformation, eom-ccsd-and-size-extensivity, rhf-instabilities-and-multiple-solutions, mcscf-parametrization-gradient-and-hessian, coupled-pair-approximations]
order: 50
date: 2026-11-04
---

## Orbital-optimized and Brueckner CC

**Two ways to treat single excitations (HJO Sec. 13.8.1).** $e^{\hat T_1}$ and the orbital rotation $e^{-\hat\kappa}$ (with $\kappa_{AI}$ nonredundant occupied-virtual parameters) generate the same state to first order.

- **$e^{\hat T_1}$.** It changes only the occupied orbitals, nonunitarily.
- **$e^{-\hat\kappa}$.** It rotates occupied and virtual orbitals together, unitarily.

**Orbital-optimized CC (OCC).**

$$
|\text{OCC}\rangle = e^{-\hat\kappa}e^{\hat T_0}|\text{RHF}\rangle,\qquad \hat T_0 = \hat T_2 + \hat T_3 + \cdots \ \text{(no singles)} .
$$

- **Amplitudes.** Fixed by projection onto the $\hat T_0$ manifold.
- **Orbitals.** Optimized variationally through a Lagrangian with multipliers $\bar t_{\mu_0}$.
- **Stationarity conditions.** They form a generalized Brillouin theorem $\langle\Lambda|[\hat H, a^\dagger_Ia_A - a^\dagger_Aa_I]|\text{OCC}\rangle = 0$, as in MCSCF ([[mcscf-parametrization-gradient-and-hessian]]).
- **Redundancies.** Occupied-occupied and virtual-virtual rotations are automatically satisfied, so the redundancies are those of the single determinant.

**Brueckner CC (BCC).** Keep the singles projections $\langle\mu_1|e^{-\hat T_0}\tilde H e^{\hat T_0}|\text{RHF}\rangle = 0$, but satisfy them by rotating orbitals until $\hat T_1 = 0$. No multipliers are needed.

**When it matters.** Both choose orbitals together with the correlation treatment, in an MCSCF-like way. For ordinary molecules they hardly change the energy: HJO's Fig. 13.5 shows no systematic gain of OCCD over CCSD for water. But where RHF has a singlet instability, as in the allyl radical ([[rhf-instabilities-and-multiple-solutions]]), standard CC inherits the problem and OCC/BCC do not.

## Quadratic CI

**Definition (HJO Sec. 13.8.2).** Start from the linked CCSD equations and drop:

- every commutator quadratic or higher in $\hat T_1$;
- additionally, from the doubles equations, $[[\hat H, \hat T_1], \hat T_2]$.

What remains is

$$
\langle\mu_1|\hat H + [\hat H,\hat T_1] + [\hat H,\hat T_2] + [[\hat H,\hat T_1],\hat T_2]|\text{HF}\rangle = 0,\qquad
\langle\mu_2|\hat H + [\hat H,\hat T_2] + \tfrac12[[\hat H,\hat T_2],\hat T_2]|\text{HF}\rangle = 0 .
$$

- **Perturbative justification.** Singles are second order and doubles first order, so QCISD keeps everything through fourth order in the energy and singles equations, and through third order in the doubles equations.
- **Size-extensivity.** Whole commutators are dropped, so QCISD stays extensive term by term.

**Unlinked form.** Written as energy-dependent equations, QCISD is CISD plus the quadratic terms $\hat T_1\hat T_2$ and $\tfrac12\hat T_2^2$:

$$
\langle\mu_1|\hat H(1 + \hat T_1 + \hat T_2 + \hat T_1\hat T_2)|\text{HF}\rangle = E\,t_{\mu_1},\qquad
\langle\mu_2|\hat H(1 + \hat T_1 + \hat T_2 + \tfrac12\hat T_2^2)|\text{HF}\rangle = E\,t_{\mu_2} .
$$

Dropping the quadratic terms gives CISD and loses extensivity. That history explains the name.

**Verdict (HJO).** QCISD costs the same as CCSD and gives similar energies, slightly worse when singles are large. Its CC Jacobian does not have the EOM structure, so EOM-CC cannot be built on it ([[eom-ccsd-and-size-extensivity]]). HJO see "few compelling reasons" to keep it.

!!! example "Water/cc-pVDZ, $E - E_{\text{FCI}}$ ($E_h$; HJO FCI; computed for this note)"
    | | $R_{\text{ref}}$ | $2R_{\text{ref}}$ |
    |---|---:|---:|
    | CCSD | 0.003744 | 0.022032 |
    | QCISD | 0.003600 | 0.021979 |
    | BCCD (Brueckner, $\max|t_1| < 4\times10^{-8}$) | 0.003872 | 0.022120 |
    | max $|t_i^a|$ in CCSD | 0.008 | 0.106 |

    - **Spread.** All three lie within 0.3 m$E_h$ of each other at both geometries, even at $2R_{\text{ref}}$ where the CCSD singles are sizeable. This is consistent with HJO's statement that the variants mostly coincide unless the reference is unstable.
    - **OCCD.** PySCF has no OCCD, so HJO's Fig. 13.5 itself was not reproduced. BCCD is the closely related Brueckner variant.

## Spin-restricted open-shell CC

**The problem (HJO Sec. 13.9.1).** A truncated CC state cannot satisfy the Schrödinger equation and both spin equations in the full projection manifold. There are $3N_D$ equations for $N_D$ amplitudes.

- **Spin-unrestricted CC.** Solves the $N_D$ Schrödinger projections and ignores spin, so it is spin-contaminated.
- **Spin-restricted CC.** Starts from a high-spin RHF (ROHF) reference.
  - **$\hat S_z$.** Satisfied automatically by using only $M_S$-conserving excitations.
  - **Partition.** Diagonalizing $\hat S^2$ in the projection manifold splits it into CSFs $|{}^S\mu\rangle$ of the right spin ($N_S$ of them) and the rest $|{}^Q\mu\rangle$ ($N_Q$).
  - **Equations.** Solve the $N_Q$ spin equations $\langle{}^Q\mu|[\hat S^2]^{\hat T}|\text{RHF}\rangle = 0$ together with the $N_S$ Schrödinger projections onto $|{}^S\mu\rangle$. The Schrödinger projections onto $|{}^Q\mu\rangle$ are not satisfied.

**Total spin (HJO Sec. 13.9.2).** The resulting wave function is not an $\hat S^2$ eigenfunction. But its Lagrangian expectation value is exactly $S(S+1)$, by a Hellmann-Feynman argument with $\alpha\hat S^2$ as the perturbation.

**Cost.** In the spin-orbital form it is no cheaper than unrestricted CC. Savings require exploiting the spin equations to remove parameters (HJO Sec. 13.9.4, spin-adapted CCSD).

!!! example "Spin contamination in CN radical, cc-pVDZ, $R$ = 2.214 bohr (computed for this note)"
    | Method | $E$ ($E_h$) | $\langle\hat S^2\rangle$ (exact 0.75) |
    |---|---:|---:|
    | UHF | | 1.1489 |
    | UCCSD on UHF, Λ-based $\langle\hat S^2\rangle$ | −92.480253 | 0.7532 |
    | UCCSD on ROHF (unrestricted amplitudes) | −92.480319 | 0.7511 |

    - **What UCCSD does.** It removes almost all of UHF's large contamination, since $e^{\hat T}$ partly undoes the spin polarization. A small residue remains.
    - **What this is not.** It is a comparison point, not HJO's spin-restricted CC, which PySCF does not implement in this form.

## Source

Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, Chichester, 2000), Secs. 13.8-13.9, pp. 698-712, Eqs. (13.8.1)-(13.9.59), Fig. 13.5. Recomputed for this note with PySCF 2.14 (`qcisd`, `bccd`, UCCSD with `spin_square`) in `hjo/c13/misc.py` and `hjo/c13/spincc.py`. HJO's FCI energies are quoted.
