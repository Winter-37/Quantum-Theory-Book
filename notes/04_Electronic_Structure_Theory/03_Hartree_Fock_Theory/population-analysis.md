---
id: population-analysis
title: Expectation values, population analysis, and dipole moments
summary: One-electron expectation values of a single determinant from the density matrix, ⟨O⟩ = Σ P_μν (ν|o|μ). Mulliken (PS) and Löwdin (S^½PS^½) populations and atomic charges, why they are basis dependent, and the SCF dipole moment. Worked HeH+ charges and computed dipoles for small molecules.
status: in-progress
kind: theory
level: intermediate
tags: [population-analysis, mulliken, lowdin, dipole-moment, density-matrix, properties]
prerequisites: [rhf, basis-orthogonalization]
related: [scf-procedure, hf-closed-shell-basis-set-trends]
order: 90
date: 2026-11-03
---

## One-electron expectation values

For a sum of spin-free one-electron operators $\hat O_1 = \sum_i o(i)$ and a closed-shell determinant, the Case 1 rule ([[slater-condon-rules]]) gives $2\sum_a(\psi_a|o|\psi_a)$. Expanding the MOs in the basis ([[rhf]]):

$$
\langle\Psi_0|\hat O_1|\Psi_0\rangle = \sum_{\mu\nu}P_{\mu\nu}\,(\nu|o|\mu) = \operatorname{tr}(\mathbf P\mathbf o),
\qquad
(\nu|o|\mu) = \int\mathrm d\mathbf r\ \phi_\nu^*(\mathbf r)\,o(\mathbf r)\,\phi_\mu(\mathbf r).
$$

All one-electron properties of a determinant follow from $\mathbf P$.

## Dipole moment

The dipole operator is $\hat{\boldsymbol\mu} = -\sum_i\mathbf r_i + \sum_A Z_A\mathbf R_A$ (atomic units; electrons carry charge $-1$). Hence

$$
\boldsymbol\mu = -\sum_{\mu\nu}P_{\mu\nu}\,(\nu|\mathbf r|\mu) + \sum_A Z_A\mathbf R_A .
$$

For a neutral molecule this does not depend on the origin, because $\operatorname{tr}(\mathbf{PS}) = \sum_A Z_A$. 1 au $= ea_0 = 2.5417$ D ([[atomic-units]]).

## Population analysis

The number of electrons is $N = \operatorname{tr}(\mathbf{PS}) = \sum_\mu(\mathbf{PS})_{\mu\mu}$. Any way of splitting this trace into basis-function contributions gives a population analysis. For any $0\le\alpha\le1$,

$$
N = \sum_\mu\big(\mathbf S^{\alpha}\mathbf P\mathbf S^{1-\alpha}\big)_{\mu\mu}.
$$

**Mulliken ($\alpha = 0$ or 1).** Population of function $\mu$: $(\mathbf{PS})_{\mu\mu}$. The overlap population $P_{\mu\nu}S_{\nu\mu}$ between functions on two atoms is shared equally between them.

**Löwdin ($\alpha = \tfrac12$).** $(\mathbf S^{1/2}\mathbf P\mathbf S^{1/2})_{\mu\mu}$. These are the diagonal elements of the density matrix in the symmetrically orthogonalized basis, $\mathbf P' = \mathbf X^{-1}\mathbf P\mathbf X^{-\dagger}$ with $\mathbf X = \mathbf S^{-1/2}$ (Szabo Ex. 3.18, [[basis-orthogonalization]]). They are always between 0 and 2.

**Atomic charge.**

$$
q_A = Z_A - \sum_{\mu\in A}(\text{population of }\mu).
$$

!!! warning "Populations are not observables"
    No population scheme is unique. The numbers depend strongly on the basis set and only make sense when comparing molecules in the same, **balanced** basis.

    Szabo's illustration: in a complete basis placed on one centre, every electron would be assigned to that atom.

    Mulliken populations can even be negative or exceed 2 in diffuse basis sets. For physically motivated charges use methods based on the density or electrostatic potential instead (Hirshfeld, natural population analysis, ESP fitting); these are beyond Szabo.

!!! example "STO-3G HeH⁺ (Szabo Sec. 3.5.3)"
    From the converged $\mathbf P$ and $\mathbf S$ of [[scf-procedure]]:

    | | He | H |
    |---|---:|---:|
    | Mulliken population | 1.5296 | 0.4704 |
    | Mulliken charge | +0.470 | +0.530 |
    | Löwdin population | 1.4728 | 0.5272 |
    | Löwdin charge | +0.527 | +0.473 |

    Both schemes split the +1 charge roughly equally. The ordering of the two charges reverses between schemes, which shows how little meaning a 0.05 difference carries.

!!! example "SCF dipole moments (au) at Szabo's standard geometries"
    PySCF 2.14 RHF, Cartesian $d$ functions, geometries of Szabo Table 3.10:

    | Molecule | STO-3G | 4-31G | 6-31G* | 6-31G** |
    |---|---:|---:|---:|---:|
    | CO (signed, + = C$^-$O$^+$) | +0.066 | −0.237 | −0.131 | −0.131 |
    | NH$_3$ | 0.703 | 0.905 | 0.767 | 0.744 |
    | H$_2$O | 0.679 | 1.026 | 0.875 | 0.859 |
    | FH | 0.507 | 0.897 | 0.780 | 0.776 |

    The polyatomic entries are magnitudes. The CO entries are signed, positive meaning C$^-$O$^+$. Experimentally carbon is the negative end, $\mu = +0.044$ au. Szabo (Table 3.24) notes that the minimal STO-3G basis gives the right sign. Every basis of double-zeta quality or better gives the wrong sign at the Hartree-Fock level (near-HF-limit value −0.110 au): a small dipole from two large, opposite contributions (O more negative vs the carbon lone pair), which correlation corrects. Split-valence 4-31G exaggerates polarity, and polarization functions bring the values down towards experiment. Compare Szabo Tables 3.24-3.25.

## Source

Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996; reprint of the revised first edition, McGraw-Hill, 1989), Sec. 3.4.7, pp. 149-152, Eqs. (3.186)-(3.198), Ex. 3.18; Sec. 3.5.3, p. 177; Sec. 3.7.4, pp. 203-205. Numbers recomputed for this note.
