---
id: upper-bounds-and-interlacing
title: Upper bounds in the variation method - the electronic Hessian of a linear expansion, Cauchy interlacing, the Hylleraas-Undheim theorem and nonlinear wave functions
summary: For a linear expansion the stationary points of the energy are the eigenvectors of the Hamiltonian matrix, and the electronic Hessian at the Kth one has K−1 negative eigenvalues 2(E_M − E_K). Enlarging the variational space lowers every eigenvalue (Cauchy's interlace theorem); adding one function interlaces the old and new spectra (Hylleraas-Undheim). Computed for BH with truncated CI spaces. Nonlinearly optimized states bound only the ground state, unless they are recombined linearly.
status: in-progress
kind: theory
level: intermediate
tags: [variational-principle, upper-bound, hylleraas-undheim, cauchy-interlace, macdonald-theorem, electronic-hessian, excited-states]
prerequisites: [variational-principle, linear-variation-method]
related: [full-ci, cisd, ci-in-practice, scf-second-order-and-stability]
also: [04_Electronic_Structure_Theory/04_Electron_Correlation_and_Wavefunction_Methods/03_Configuration_Interaction]
date: 2026-11-04
---

## Stationary points of the energy functional

**Variation principle.** The energy functional $E[\tilde0] = \langle\tilde0|\hat H|\tilde0\rangle/\langle\tilde0|\tilde0\rangle$ is stationary exactly at the eigenstates of $\hat H$. Expanding around an eigenstate, $|\tilde0\rangle = |0\rangle + |\delta\rangle$:

- **No first-order term.** The first-order term vanishes.
- **Converse.** Every stationary point satisfies $\hat H|\tilde0\rangle = E[\tilde0]|\tilde0\rangle$.
- **Accuracy.** Near an eigenstate the energy error is quadratic in the wave-function error, so the energy is more accurate than the wave function. (HJO Exercise 4.1: the energy error can be estimated from the gradient and Hessian.)

## Linear expansions

**Setup.** For $|\mathbf C\rangle = \sum_iC_i|i\rangle$ with real coefficients and orthonormal $|i\rangle$, the energy $E(\mathbf C) = \mathbf C^{\mathsf T}\mathbf H\mathbf C/\mathbf C^{\mathsf T}\mathbf C$ has gradient and Hessian

$$
E_i^{(1)} = \frac{2}{\mathbf C^{\mathsf T}\mathbf C}\big[(\mathbf H\mathbf C)_i - E(\mathbf C)C_i\big],\qquad
E_{ij}^{(2)}\big|_{\text{stat}} = 2\big(H_{ij} - E\,\delta_{ij}\big)\quad(\mathbf C^{\mathsf T}\mathbf C = 1).
$$

**Stationary points.** $\mathbf E^{(1)} = 0$ gives $\mathbf H\mathbf C = E\mathbf C$: an $m$-dimensional space has exactly $m$ orthonormal solutions.

**Character of each solution.** In the eigenvector basis the Hessian at solution $K$ is diagonal with elements $2(E_M - E_K)$, i.e. twice the excitation energies. It is singular along $\mathbf C_K$ itself, and without degeneracies the $K$th state has exactly $K - 1$ negative eigenvalues:

- the ground state is a minimum;
- the first excited state is a first-order saddle point;
- and so on.

This is the same diagnostic used for SCF stability ([[scf-second-order-and-stability]]).

## Bounds when the space grows

**Lowest eigenvalue.** If $S'\subset S''$, the eigenvectors of $S'$ can be expanded in those of $S''$. This gives $E_1'' \le E_1'$: the lowest eigenvalue can only drop as the space is enlarged.

**Cauchy's interlace theorem (HJO Eq. 4.2.39; proof in Exercise 4.2).** With $\delta = \dim S'' - \dim S'$,

$$
E_K''\le E_K'\le E_{K+\delta}'' .
$$

**Every** eigenvalue drops. In particular, the $m$ lowest eigenvalues of any linear variational space are upper bounds to the $m$ lowest exact energies of the same symmetry (often called the Hylleraas-Undheim-MacDonald theorem; the name is general knowledge).

**Hylleraas-Undheim ($\delta = 1$).** The spectra interlace:

$$
E_1''\le E_1'\le E_2''\le E_2'\le\cdots\le E_m''\le E_m'\le E_{m+1}'' .
$$

**Larger steps.** For $\delta>1$ the second inequality allows $E_{K+1}''<E_K'$: an eigenvalue of the old space is then no longer a lower bound to the next eigenvalue of the new space.

!!! example "BH, 6-31G, R = 2.3289 bohr: five lowest singlet $^1A_1$ ($C_{2v}$) energies in nested CI spaces (computed for this note)"
    Hartree; determinant space restricted to $A_1$ symmetry; singlets selected by $\langle\hat S^2\rangle = 0$. The spaces contain all excitations up to the given level from the RHF determinant.

    | Space | Dimension | $E_1$ | $E_2$ | $E_3$ | $E_4$ | $E_5$ |
    |---|---:|---:|---:|---:|---:|---:|
    | S | 25 | −25.10897 | −24.70304 | −24.51307 | −24.45591 | −24.37682 |
    | SD | 289 | −25.16989 | −24.91229 | −24.86693 | −24.76065 | −24.64033 |
    | SDT | 1465 | −25.17089 | −24.92932 | −24.88454 | −24.77797 | −24.65781 |
    | SDTQ | 3961 | −25.17266 | −24.93853 | −24.89728 | −24.77935 | −24.66799 |
    | FCI | 7057 | −25.17266 | −24.93854 | −24.89730 | −24.77936 | −24.66801 |

    - **Interlacing.** Every $E_K$ drops (or stays) from one space to the next, as the interlace theorem requires.
    - **Large steps.** $E_3(\text{SD}) = -24.86693$ lies below $E_2(\text{S}) = -24.70304$: Hylleraas-Undheim interlacing does not hold for $\delta>1$. HJO's d-aug-cc-pVDZ calculation shows the same with $E_2(\text{S}) > E_3(\text{SD})$.
    - **Brillouin.** $E_1(\text{S})$ equals the RHF energy (−25.10897).
    - **Remark.** In $C_{2v}$, $A_1$ includes one component of any $\Delta$ states of the linear molecule; the interlacing argument needs only a space closed under the symmetry, which this is. HJO restrict to $^1\Sigma^+$.

## Nonlinear wave functions

**What still holds.** A nonlinearly optimized, normalized state $|c\rangle = \sum_KC_K|K\rangle$ (expanded in exact or Fock-space eigenstates) satisfies

$$
E_c - E_I = \sum_K|C_K|^2(E_K - E_I),
$$

so $E_c\ge E_1$ always. It is an upper bound to $E_I$ only if $|c\rangle$ is orthogonal to all lower states.

**Excited states are not bounded.** Separately optimized excited states of the same symmetry bound nothing but the ground state.

**Repair.** Use the nonlinear states as the basis of a small linear problem; its eigenvalues are again bounds by Cauchy's theorem.

**He example (HJO, t-aug-cc-pVTZ; quoted, not recomputed).**

| | $1s^2$ HF | $1s2s$ HF | Exact |
|---|---:|---:|---:|
| Separately optimized | −2.861627 | −2.169652 | −2.903724, −2.145974 |
| After the 2×2 nonorthogonal CI in the two HF states | −2.862332 | −2.096220 | |

- **Separate optimization.** Both HF energies lie **below** the exact first excited $^1S$ energy, so the $1s2s$ HF energy is not an upper bound to it.
- **After the 2×2 CI.** Both energies are rigorous upper bounds.
- **Diagnostic.** A nonlinear stationary point may be unphysical. Inspect the number of negative Hessian eigenvalues before accepting it.

## Source

Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, Chichester, 2000), Secs. 4.2.1-4.2.5, pp. 111-119, Eqs. (4.2.1)-(4.2.51), Fig. 4.1-4.2; Exercises 4.1-4.2. Equations (4.2.39)-(4.2.41) read from the page image. The BH 6-31G table was computed for this note with PySCF 2.14 (HJO's figure uses d-aug-cc-pVDZ). The He numbers are HJO's.
