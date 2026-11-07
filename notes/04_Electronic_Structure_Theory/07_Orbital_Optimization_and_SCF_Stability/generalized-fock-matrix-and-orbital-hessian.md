---
id: generalized-fock-matrix-and-orbital-hessian
title: The generalized Fock matrix, inactive and active Fock matrices, and the orbital Hessian - gradient, Hessian and Hessian-vector products for single-configuration wave functions
summary: For any wave function, the orbital gradient is twice the antisymmetric part of the generalized Fock matrix F_mn = Σ D_mq h_nq + Σ d_mqrs g_nqrs. Splitting the orbitals into inactive, active and virtual reduces F to inactive and active Fock matrices plus a Q matrix that needs only active two-electron densities. The orbital Hessian follows as a similar contraction. Its closed-shell form 4(δ_ij F_ab − δ_ab F_ij + 4g_aibj − g_abij − g_ajib) is diagonally dominant in canonical orbitals, and Hessian-vector products are built from one-index-transformed integrals or AO Fock-like matrices at n⁴ cost. Verified for high-spin O₂ (generalized-Fock gradient against finite differences, 8×10⁻⁹) and closed-shell water (Hessian against finite differences).
status: in-progress
kind: derivation
level: advanced
tags: [generalized-fock-matrix, inactive-fock, active-fock, orbital-hessian, orbital-gradient, one-index-transformation, operation-count, hartree-fock, high-spin]
prerequisites: [hartree-fock-csf-parametrization-and-canonical-conditions, density-matrices-second-quantization, orbital-rotations]
related: [scf-convergence-diis-and-newton, mcscf-second-order-optimization, scf-second-order-and-stability, density-based-hartree-fock, molecular-properties-and-response]
order: 30
date: 2026-11-04
---

## Gradient from the generalized Fock matrix

**Definition (HJO Sec. 10.8.3).** For a real state with densities $D_{pq} = \langle\hat E_{pq}\rangle$ and $d_{pqrs} = \langle\hat e_{pqrs}\rangle$,

$$
F_{mn} = \sum_\sigma\langle a^\dagger_{m\sigma}[a_{n\sigma},\hat H]\rangle = \sum_qD_{mq}h_{nq} + \sum_{qrs}d_{mqrs}g_{nqrs},\qquad
E^{(1)}_{mn} = 2(F_{mn} - F_{nm}).
$$

**Properties.**

- **Stationarity.** A symmetric $\mathbf F$ is sufficient for a stationary state.
- **Energy.** $E = \tfrac12\sum_{pq}(D_{pq}h_{pq} + \delta_{pq}F_{pq}) + h_{\text{nuc}}$. The energy is not $\mathrm{Tr}\,\mathbf F$, because one- and two-electron parts carry different weights.
- **Generality.** The same matrix drives MCSCF optimization ([[mcscf-second-order-optimization]]).

## Inactive, active and Q matrices

**Simplification (HJO Sec. 10.8.4).** Densities with a virtual index vanish, and those with an inactive index reduce to lower-rank densities ($D_{iq} = 2\delta_{iq}$, $d_{pqis} = 2\delta_{is}D_{pq} - \delta_{iq}D_{ps}$). The generalized Fock matrix then needs only

$$
{}^{\text I}F_{mn} = h_{mn} + \sum_i(2g_{mnii} - g_{miin}),\qquad
{}^{\text A}F_{mn} = \sum_{vw}D_{vw}\big(g_{mnvw} - \tfrac12g_{mwvn}\big),\qquad
Q_{vm} = \sum_{wxy}d_{vwxy}g_{mwxy},
$$

combined as follows:

$$
F_{in} = 2({}^{\text I}F_{ni} + {}^{\text A}F_{ni}),\qquad F_{vn} = \sum_w{}^{\text I}F_{nw}D_{vw} + Q_{vn},\qquad F_{an} = 0 .
$$

**Special cases.**

- **Closed shell.** $\mathbf F$ has only inactive rows, $2\,{}^{\text I}\mathbf F$. The gradient is $E^{(1)}_{ai} = 4\,{}^{\text I}F_{ai}$, the familiar Fock matrix.
- **High spin.** $D_{vw} = \delta_{vw}$ and $d_{vwxy} = \delta_{vw}\delta_{xy} - \delta_{vy}\delta_{wx}$. So $Q_{vm} = \sum_w(g_{mvww} - g_{mwwv})$, a Fock-like matrix with equal Coulomb and exchange weights, and $\mathbf Q = \mathbf 0$ for a doublet.

**Operation counts (HJO Sec. 10.8.5).** Here $n$ counts all orbitals, $O$ occupied, $V$ virtual, $I$ inactive and $A$ active.

| Quantity | Cost (multiplications) |
|---|---|
| $\mathbf F$ directly from (10.8.23) | $nO^4$ (a fifth-order process) |
| via ${}^{\text I}\mathbf F$, ${}^{\text A}\mathbf F$, $\mathbf Q$ | $\max(n^2I,\ n^2A^2,\ nA^4)$ |
| closed-shell gradient elements only | $I^2V$ |
| AO-basis Fock build | $n^4$, or less with screening |
| MO integral transformation | $n^5$ |

**Units of "order".** Doubling the system multiplies an $nO^4$ cost by 32. Doubling only the basis (fixed $N$) multiplies it by just 2. Cost statements should therefore track the orbital types.

## The Hessian

**General form (HJO Sec. 10.8.6).** Using the Jacobi identity, the Hessian becomes

$$
E^{(2)}_{pq,rs} = (1 - P_{pq})(1 - P_{rs})\big[2D_{pr}h_{qs} - (F_{pr} + F_{rp})\delta_{qs} + 2Y_{pqrs}\big],\qquad
Y_{pqrs} = \sum_{mn}\big[(d_{pmrn} + d_{pmnr})g_{qmns} + d_{prmn}g_{qsmn}\big].
$$

Building $\mathbf Y$ costs $n^2O^4$, a sixth-order process. The gradient is fifth order and the energy fourth order.

**Closed-shell form.**

$$
E^{(2)}_{ai,bj} = 4\big(\delta_{ij}F_{ab} - \delta_{ab}F_{ij} + 4g_{aibj} - g_{abij} - g_{ajib}\big)
\ \xrightarrow{\text{canonical}}\
4\big[\delta_{ab}\delta_{ij}(\varepsilon_a - \varepsilon_i) + 4g_{aibj} - g_{abij} - g_{ajib}\big].
$$

- **Diagonal dominance.** The orbital-energy differences, the Møller-Plesset denominators, are usually larger than the integrals. This is why iterative solvers converge quickly.
- **Triplet rotations.** Subtracting $16g_{aibj}$ gives the triplet Hessian used in [[rhf-instabilities-and-multiple-solutions]].

## Hessian-vector products without the Hessian

**One-index transformation (HJO Sec. 10.8.7).** The commutator $\hat H^\kappa = [\hat\kappa,\hat H]$ is a Hamiltonian whose integrals are one-index transformed:

$$
h^\kappa_{pq} = \sum_m(\kappa_{pm}h_{mq} + \kappa_{qm}h_{pm}),\qquad
g^\kappa_{pqrs} = \sum_m(\kappa_{pm}g_{mqrs} + \kappa_{qm}g_{pmrs} + \kappa_{rm}g_{pqms} + \kappa_{sm}g_{pqrm}).
$$

The transformed vector is then a gradient built from $\hat H^\kappa$, plus $\boldsymbol\kappa$ times the ordinary gradient (10.8.61). This costs $n^2O^3$ per vector, compared with $n^2O^4$ to build the Hessian.

**AO formulation (HJO Sec. 10.8.8).** For closed-shell and high-spin states, ${}^{\text I}\mathbf F^\kappa$ (and ${}^{\text A}\mathbf F^\kappa$, $\mathbf Q^\kappa$) are AO Fock builds with a modified density $P_{\rho\sigma} = 4\sum_{iq}\kappa_{iq}C_{\rho i}C_{\sigma q}$. Each trial vector costs about one SCF iteration ($n^4$). Newton iterations remain dearer because each one transforms several trial vectors. My closed-shell version is in [[scf-convergence-diis-and-newton]].

!!! example "Checks (computed for this note)"
    - **High-spin generalized Fock matrix, ³Σ⁻ O₂ in 6-31G** at $R$ = 2.28 bohr.
        - **Setup.** 7 inactive and 2 active orbitals, perturbed away from the ROHF solution by a random rotation. I built ${}^{\text I}\mathbf F$, ${}^{\text A}\mathbf F$ and $\mathbf Q^{\text{high-spin}}$ from MO integrals and assembled $\mathbf F$ as above.
        - **Gradient.** For all 95 nonredundant inactive-active, inactive-virtual and active-virtual rotations, $2(F_{pq} - F_{qp})$ equals the finite-difference energy derivative to $8\times10^{-9}$ (largest component 6.5). The sign follows the rotation convention: positive for HJO's $\exp(-\hat\kappa)$.
        - **Energy.** $\tfrac12\sum(D_{pq}h_{pq} + \delta_{pq}F_{pq}) + h_{\text{nuc}}$ reproduces the energy, −148.14940276 $E_h$.
        - **Converged ROHF.** The nonredundant block of $\mathbf F - \mathbf F^{\mathsf T}$ is $6\times10^{-8}$.
    - **Closed-shell Hessian, water/STO-3G at $1.3R_{\text{ref}}$.** The canonical-basis formula matches a central-difference Hessian of $E(\boldsymbol\kappa)$ to $8\times10^{-5}$, the finite-difference noise for elements up to 80 $E_h$.
    - **Not verified.** The one-index-transformed form (10.8.61) and the AO expressions (10.8.62)-(10.8.65) are described from HJO but were not coded separately. My Hessian-vector product uses the equivalent $\mathbf J$/$\mathbf K$ form.

## Source

Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, Chichester, 2000), Secs. 10.8.3-10.8.8, pp. 481-490, Eqs. (10.8.16)-(10.8.65). Checks computed for this note with NumPy, SciPy and PySCF 2.14 (`hjo/c10/genfock.py`, `fdcheck.py`).
