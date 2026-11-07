---
id: caspt2-and-caspt-series
title: Multiconfigurational perturbation theory (HJO 14.7) - the CASSCF Fock operator, the block-diagonal zero-order CASPT Hamiltonian, why CASPT is not exactly size-extensive, internally contracted CASPT2, and the divergence of the CASPT series for stretched water
summary: CASPT takes a CASSCF state as zero order and builds H₀ from the CASSCF Fock operator, projected separately onto the CAS space orthogonal to |0⟩, the singles-and-doubles space outside the CAS, the triples-and-quadruples space and so on. This keeps every wave-function correction at a finite excitation level, and H₀ reduces to the Møller-Plesset H₀ for one closed-shell determinant. The projectors make H₀ non-separable, so CASPT is not exactly size-extensive. I implemented HJO's uncontracted (determinantal) CASPT in the full frozen-core space of water/cc-pVDZ and ran it to tenth order. At R_ref it converges, and CASPT2 recovers 93% of the correlation missing from CASSCF. At 2R_ref it diverges explosively, as in HJO Table 14.8 (order 10: 1.7 × 10⁵ E_h here, 1.3 × 10⁵ in HJO). My low orders differ from HJO's by about 1.4 mE_h at CASPT2, although my MPPT series in the same code reproduces HJO's MPPT columns.
status: in-progress
kind: theory
level: advanced
tags: [caspt2, multireference-perturbation-theory, casscf, zero-order-hamiltonian, size-extensivity, intruder-states, divergence, water]
prerequisites: [rspt-wigner-rule-and-hylleraas-functional, mcscf-parametrization-gradient-and-hessian, moller-plesset-and-coupled-cluster-perturbation-theory]
related: [mp-convergence-intruders-analytic-continuation, state-averaged-mcscf-and-configuration-rotations, standard-models-h2-and-water, generalized-fock-matrix-and-orbital-hessian]
order: 60
date: 2026-11-04
---

## Why a new zero-order Hamiltonian

**The problem (HJO Sec. 14.7).** When several configurations matter, MP theory has no unique reference determinant. Its low orders are poor and its high orders diverge. CASPT uses the CASSCF state $|0\rangle$ as zero order and generalizes the Fock operator.

**The CASSCF Fock operator (HJO Sec. 14.7.1).**

$$
\hat f = \sum_{pq}f_{pq}\hat E_{pq},\qquad f_{pq} = h_{pq} + \sum_{rs}D_{rs}\big(g_{pqrs} - \tfrac12g_{psrq}\big),
$$

where $\mathbf D$ is the CASSCF one-electron density.

- **Vanishing blocks.** Inactive-secondary elements vanish at convergence, because they are proportional to the orbital gradient.
- **Surviving blocks.** Inactive-active and active-secondary elements remain.
- **Canonical orbitals.** The inactive, active and secondary diagonal blocks can each be diagonalized by redundant rotations (HJO Fig. 14.11).

**Making $|0\rangle$ an eigenstate.** $\hat f|0\rangle$ is not proportional to $|0\rangle$. Take $\hat H_0 = \hat P\hat f\hat P + E^{(0)}|0\rangle\langle0|$ with $E^{(0)} = \langle0|\hat f|0\rangle$. For a closed-shell determinant this is exactly MP theory. But its resolvent would spread the first-order wave function over the whole FCI space.

**Block-diagonal CASPT $\hat H_0$.** HJO therefore use

$$
\hat H_0 = \hat P_K\hat f\hat P_K + \hat P_{SD}\hat f\hat P_{SD} + \hat P_{TQ}\hat f\hat P_{TQ} + \cdots + E^{(0)}|0\rangle\langle0| .
$$

The projectors are onto:

- the CAS space orthogonal to $|0\rangle$ ($K$);
- single and double excitations outside the CAS ($SD$);
- triples and quadruples ($TQ$), and so on.

Then $|0^{(1)}\rangle$ contains at most doubles, $|0^{(2)}\rangle$ at most quadruples, and so on (HJO Fig. 14.12).

## Size-extensivity

**Non-separability (HJO Sec. 14.7.2).** For noninteracting A and B with a product CASSCF state:

- $\hat f_{AB} = \hat f_A + \hat f_B$ and $E^{(0)}_{AB} = E^{(0)}_A + E^{(0)}_B$ are additive;
- but $\hat P_{AB}\hat f_{AB}\hat P_{AB} \ne \hat P_A\hat f_A\hat P_A + \hat P_B\hat f_B\hat P_B$, because cross terms like $(\hat f_A - E^{(0)}_A)|0_A\rangle\langle0_A|$ do not cancel.

These cross terms vanish only when $|0_A\rangle$ and $|0_B\rangle$ are eigenfunctions of their Fock operators, i.e. in the single-determinant limit. So CASPT is close to extensive for nearly single-configuration references and less so for strongly multiconfigurational ones.

## CASPT2 in practice

**Internally contracted CASPT1 (HJO Sec. 14.7.3).** The first-order function is expanded in contracted functions $\hat E_{pq}|0\rangle$ and $\hat e_{pqrs}|0\rangle$, excluding all-active excitations:

- **Equations.** The basis is nonorthogonal, so the first-order equations involve the overlap matrix $\mathbf S$ of these functions.
- **What drops out.** CAS-space components vanish because the CASSCF CI gradient is zero, and triples and higher drop out.
- **Cost.** The formalism needs up to the three-particle active density already for $E^{(2)}$.
- **Uncontracted alternative.** Use all determinants excited from the whole CAS space. It is simpler, costlier, and gives similar $E^{(2)}$.

**Water dissociation (HJO Fig. 14.13, quoted).** With the valence (3,0,1,2) CAS:

- **Near equilibrium.** CASPT2 is about as accurate as MP2.
- **Along the stretch.** It stays uniform while MP2 deteriorates.
- **Against CASSCF.** It is more than ten times closer to FCI than CASSCF itself.

## How far does the series go?

!!! example "HJO Table 14.8 recomputed: water/cc-pVDZ, CASPT and MPPT to tenth order, $E - E_{\text{FCI}}$ ($E_h$; computed for this note)"
    **Method.**

    - **Reference.** Valence CASSCF(8e, 6o; 3,0,1,2) on all electrons; then its $1a_1$ orbital is frozen.
    - **CASPT.** Fock blocks canonicalized per irrep. Uncontracted determinantal CASPT in the full frozen-core space: $7.8\times10^7$ determinants, $1.96\times10^7$ of $A_1$ symmetry. $\hat H_0$ is built exactly from the block definition above; levels are defined by the number of electrons in secondary orbitals.
    - **Recursion.** Exact RSPT, with PySCF σ-vectors for $\hat H$.
    - **MPPT.** Canonical HF, frozen HF $1a_1$.
    - **Errors.** Relative to HJO's FCI energies: −76.23875 and −75.95022 (CAS core); −76.23977 and −75.94992 (HF core).

    | Order | CASPT $R_{\text{ref}}$ (mine) | HJO | CASPT $2R_{\text{ref}}$ (mine) | HJO | MPPT $R_{\text{ref}}$ (mine) | HJO | MPPT $2R_{\text{ref}}$ (mine) | HJO |
    |---:|---:|---:|---:|---:|---:|---:|---:|---:|
    | 1 | 0.16091 | 0.16091 | 0.13212 | 0.13212 | 0.21573 | 0.21574 | 0.36221 | 0.36221 |
    | 2 | 0.01119 | 0.01262 | 0.00672 | 0.00798 | 0.01334 | 0.01335 | 0.05491 | 0.05491 |
    | 3 | 0.00557 | 0.00419 | 0.00452 | 0.00442 | 0.00645 | 0.00645 | 0.06908 | 0.06908 |
    | 4 | 0.00023 | 0.00019 | −0.00025 | −0.00084 | 0.00106 | 0.00107 | 0.01602 | 0.01602 |
    | 5 | 0.00065 | 0.00036 | 0.15214 | 0.11878 | 0.00051 | 0.00051 | 0.01665 | 0.01665 |
    | 6 | −0.00002 | 0.00001 | 1.57487 | 1.17522 | 0.00013 | 0.00013 | 0.00434 | 0.00434 |
    | 7 | 0.00012 | 0.00005 | 35.833 | 27.454 | 0.00006 | 0.00007 | 0.00060 | 0.00060 |
    | 8 | −0.00001 | 0.00000 | 546.18 | 416.57 | | 0.00001 | −0.00051 | −0.00051 |
    | 9 | 0.00003 | 0.00001 | 10 110 | 7 758 | | 0.00001 |  | −0.00208 |
    | 10 | 0.00000 | 0.00000 | 169 049 | 129 959 | | 0.00000 |  | −0.00168 |

    - **Same machinery, two outcomes.** My code reproduces both of HJO's MPPT columns to $\pm1\times10^{-5}$ wherever I have them (the MPPT runs ran out of memory after orders 7 and 8). It also reproduces the CASSCF first-order errors exactly.
    - **Low-order discrepancy.** My CASPT low orders differ from HJO's by up to 1.4 m$E_h$ (CASPT2 0.01119 against 0.01262). So HJO's determinantal $\hat H_0$ must differ in a detail they do not specify, e.g. the active-orbital basis or how $\hat f$ is restricted inside each block. I have not resolved this.
    - **What both show.**
      - At $R_{\text{ref}}$ the CASPT series converges about as well as MPPT, reaching $10^{-5}$ $E_h$ by order 10.
      - At $2R_{\text{ref}}$ CASPT2 is excellent (6.7 m$E_h$ here, 8.0 in HJO, i.e. 94-95% of the 0.132 $E_h$ that CASSCF misses). Yet from fifth order on the series explodes, growing by a factor of 10-23 per order. The higher orders have no physical meaning.
      - MPPT at $2R_{\text{ref}}$ looks convergent to tenth order, but HJO note it diverges beyond (compare HF at $2.5R_e$ in [[mp-convergence-intruders-analytic-continuation]]).

**HJO's verdict.** Convergence data for genuinely multiconfigurational states are scarce, but this behaviour seems typical of this simple $\hat H_0$. Good low orders (CASPT2) are a much weaker requirement than a convergent series.

## Source

Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, Chichester, 2000), Sec. 14.7, pp. 796-803, Eqs. (14.7.1)-(14.7.27), Figs. 14.11-14.13, Table 14.8. Recomputed for this note with PySCF 2.14 (CASSCF, `direct_spin1_symm` σ-vectors) and my own CASPT/MPPT recursion (`hjo/c14/caspt.py`).
