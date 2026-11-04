---
id: natural-orbitals
title: Natural orbitals
summary: Natural spin orbitals are the eigenvectors of the one-particle density matrix and their eigenvalues are occupation numbers. They give a more rapidly convergent CI expansion than canonical Hartree-Fock orbitals for short expansions. Two-electron natural expansion (K terms instead of K²), the iterative natural orbital idea, and an H2/6-31G** demonstration.
status: in-progress
kind: theory
level: intermediate
tags: [natural-orbitals, rdm, occupation-numbers, ci-convergence, lowdin]
prerequisites: [one-particle-rdm, full-ci]
related: [density-matrices-second-quantization, mcscf-and-gvb, cisd, change-of-basis, ci-in-practice]
also: []
date: 2026-11-03
---

## Definition

The 1-RDM in an orthonormal spin-orbital basis, $\gamma_{ij}$ ([[one-particle-rdm]]), is Hermitian. Rotate to another orthonormal basis, $\chi_i = \sum_k\eta_kU_{ki}^*$ ([[change-of-basis]]):

$$
\gamma(\mathbf x_1,\mathbf x_1') = \sum_{kl}\eta_k(\mathbf x_1)\,(\mathbf U^\dagger\boldsymbol\gamma\mathbf U)_{kl}\,\eta_l^*(\mathbf x_1').
$$

Choose $\mathbf U$ to diagonalize $\boldsymbol\gamma$, $\mathbf U^\dagger\boldsymbol\gamma\mathbf U = \boldsymbol\lambda$:

$$
\gamma(\mathbf x_1,\mathbf x_1') = \sum_i\lambda_i\,\eta_i(\mathbf x_1)\,\eta_i^*(\mathbf x_1').
$$

The $\eta_i$ are the **natural spin orbitals** (Löwdin) and the $\lambda_i$ their **occupation numbers**:

$$
0\le\lambda_i\le1,
\qquad
\sum_i\lambda_i = N .
$$

**Limiting cases.**

- **Hartree-Fock.** The occupied Hartree-Fock orbitals are natural orbitals with $\lambda = 1$, and every virtual has $\lambda = 0$.
- **Correlated.** Some occupations fall below 1 and some virtual-like natural orbitals become fractionally occupied. These are the orbitals that carry the correlation.

## Why they help

Natural orbitals give, in a precise sense, the **most rapidly convergent CI expansion**. To reach a given accuracy, fewer configurations are needed when they are built from natural orbitals than from any other orthonormal set. Orbitals with negligible occupation can be discarded with little loss.

Szabo illustrates this with Shavitt and co-workers' water study (39-STO basis, 4120 SDCI configurations, his Table 4.12):

- 60% of the SDCI correlation energy needs 50 natural-orbital configurations versus 146 canonical ones.
- The advantage fades for very long expansions (99%: 1652 vs 1760).

## Two electrons: the natural expansion (Szabo Ex. 4.8)

Write the full CI singlet of a two-electron system in spatial orbitals $\psi_i$, $i = 1,\dots,K$:

$$
|{}^1\Phi_0\rangle = \sum_{i=1}^{K}\sum_{j=1}^{K}C_{ij}\,|\psi_i\bar\psi_j\rangle,
\qquad
\mathbf C = \mathbf C^{\mathsf T}\ (\text{singlet}),
$$

which has $K^2$ terms.

1. **Natural orbitals from $\mathbf C$.** The spatial 1-RDM is $2\mathbf C\mathbf C^\dagger$. Diagonalizing $\mathbf C$ with a real orthogonal $\mathbf U$, $\mathbf U^{\mathsf T}\mathbf C\mathbf U = \mathbf d$, also diagonalizes $\mathbf C\mathbf C^\dagger$.
2. **The rotated orbitals are natural orbitals.** $\zeta_i = \sum_j\psi_jU_{ji}$ are the natural spatial orbitals, with occupation numbers $2d_i^2$.
3. **The wave function collapses.** In the natural orbitals,
$$
|{}^1\Phi_0\rangle = \sum_{i=1}^{K}d_i\,|\zeta_i\bar\zeta_i\rangle .
$$
Only **$K$ terms** remain, all closed-shell pairs, compared with $K^2$ in a general basis.

This is the two-electron case of the singular-value (Schmidt) decomposition of $\mathbf C$.

!!! example "H₂, 6-31G**, R = 1.4 bohr (full CI with PySCF 2.14)"
    **Occupations.** The spatial natural-orbital occupations (sum 2) are
    $$
    1.96965,\ 0.02017,\ 0.00636,\ 0.00158,\ 0.00158,\ 0.00024,\ \dots
    $$
    The coefficients $d_i$ = 0.99238, 0.10042, 0.05637, 0.02811, 0.02811 satisfy $2d_i^2$ = occupation, confirming the natural expansion.

    **Truncated full CI.** Full CI in the first $k$ orbitals, measured relative to the full-space Hartree-Fock energy (hartree; full basis value $-0.033869$):

    | $k$ | natural orbitals | canonical HF orbitals |
    |---:|---:|---:|
    | 2 | −0.018212 | −0.005101 |
    | 3 | −0.025508 | −0.011678 |
    | 4 | −0.028880 | −0.023655 |
    | 5 | −0.032194 | −0.027088 |

    With two orbitals, natural orbitals give 54% of the correlation energy against 15% for canonical orbitals.

    The $k=1$ natural-orbital value is +0.0002 hartree, slightly above Hartree-Fock. The first natural orbital is not the variationally best single orbital, so a one-determinant energy in it is a little worse than Hartree-Fock.

## Using natural orbitals in practice

**The catch.** Exact natural orbitals require the CI wave function you wanted to avoid computing.

**Approximate natural orbitals** are nearly as good. In the **iterative natural orbital** method (Bender and Davidson, as cited by Szabo):

1. Run a short CI with canonical orbitals.
2. Diagonalize its 1-RDM to get approximate natural orbitals.
3. Build the next short CI from the most occupied of these.
4. Repeat.

A few iterations help. Szabo cites a study showing the process can diverge if pushed further. The variational alternative is to optimize the orbitals together with the CI coefficients, which is MCSCF ([[mcscf-and-gvb]]).

**Two remarks from Jørgensen and Simons (Ch. 2, Sec. D.2).**

- **INOs are not MCSCF orbitals.** INOs diagonalize the 1-RDM of a fixed configuration list; MCSCF orbitals minimize the energy.
- **The list must contain configurations singly excited relative to each other.** If it holds only mutually doubly excited configurations, the 1-RDM is diagonal in any orbital set and every set is "natural". For Be, a list built on $1s^22s^2$ and $1s^22p^2$ needs $1s^22sns$ and $1s^22pnp$ as well. These mimic the orbital-rotation parameters an MCSCF would optimize ([[ci-in-practice]]).

## Source

Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996; reprint of the revised first edition, McGraw-Hill, 1989), Sec. 4.4, pp. 254-258, Eqs. (4.41)-(4.46), Table 4.12, Ex. 4.8; Szabo's references to Löwdin (Phys. Rev. 97, 1474, 1955) and Bender-Davidson (J. Phys. Chem. 70, 2675, 1966). H$_2$ numbers computed for this note.
