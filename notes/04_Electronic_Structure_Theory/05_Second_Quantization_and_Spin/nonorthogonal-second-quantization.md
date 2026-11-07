---
id: nonorthogonal-second-quantization
title: Second quantization for nonorthogonal spin orbitals - the overlap anticommutator and biorthogonal operators
summary: For nonorthogonal spin orbitals with overlap S, creation operators still anticommute among themselves, but {a_P, a†_Q} = S_PQ. Built from Löwdin-orthonormalized auxiliary operators, ON vectors have inner products det S_km, an annihilator removes an electron from every occupied orbital it overlaps, and one- and two-electron operators carry S⁻¹ on each index. Biorthogonal annihilators ā_P = Σ_Q [S⁻¹]_PQ a_Q restore {ā_P, a†_Q} = δ_PQ but are not adjoints of the creators. All relations checked with Fock-space matrices and against the first-quantization Löwdin rule.
status: in-progress
kind: derivation
level: advanced
tags: [second-quantization, nonorthogonal-orbitals, biorthogonal, overlap, lowdin-orthogonalization, valence-bond]
prerequisites: [creation-and-annihilation-operators, second-quantized-operators, basis-orthogonalization]
related: [second-quantization-in-a-finite-basis, mcscf-and-gvb, orbital-rotations, unitary-matrices-exponential-logarithm]
order: 80
date: 2026-11-04
---

## Fock space for nonorthogonal spin orbitals

**Inner product.** For spin orbitals with overlap $S_{PQ} = \int\phi_P^*(\mathbf x)\phi_Q(\mathbf x)\,\mathrm d\mathbf x$, the Fock space is built from ON vectors as before, but the inner product is the overlap of the corresponding determinants:

$$
\langle\mathbf k|\mathbf m\rangle = \delta_{N_k N_m}\det\mathbf S_{\mathbf k\mathbf m},
$$

where $\mathbf S_{\mathbf k\mathbf m}$ is the overlap matrix between the spin orbitals occupied in $|\mathbf k\rangle$ and in $|\mathbf m\rangle$.

**Auxiliary orthonormal operators.** Introduce the symmetrically orthonormalized spin orbitals $\tilde{\boldsymbol\phi} = \boldsymbol\phi\mathbf S^{-1/2}$ ([[basis-orthogonalization]]) with ordinary operators $\tilde a_P^\dagger$. Creation operators transform like the orbitals (as for any change of basis, [[orbital-rotations]]):

$$
a_P^\dagger = \sum_Q\tilde a_Q^\dagger[\mathbf S^{1/2}]_{QP},\qquad a_P = \sum_Q\tilde a_Q[\mathbf S^{1/2}]_{PQ}.
$$

## Anticommutation relations

$$
\{a_P^\dagger, a_Q^\dagger\} = 0,\qquad \{a_P, a_Q\} = 0,\qquad \{a_P, a_Q^\dagger\} = S_{PQ}.
$$

Nonorthogonality affects only the mixed anticommutator, which is nonzero for every overlapping pair.

**Annihilation.** Since $a_P$ is a combination of orthonormal annihilators, $a_P|\text{vac}\rangle = 0$. On an ON vector it removes an electron from **each** occupied spin orbital it overlaps (HJO Eq. 1.9.15):

$$
a_P|\mathbf k\rangle = \sum_Qk_Q\Gamma_Q^{\mathbf k}S_{PQ}\,|k_1,\ldots,0_Q,\ldots,k_M\rangle,\qquad \Gamma_Q^{\mathbf k} = \prod_{R<Q}(-1)^{k_R} .
$$

(Derived by writing $|\mathbf k\rangle$ as a creator string and expanding the commutator or anticommutator of $a_P$ with the string as a sum of elementary anticommutators.) The creation operator acts exactly as in the orthonormal case, because the creators still anticommute among themselves.

## One- and two-electron operators

Transforming from the auxiliary basis, the integrals pick up $\mathbf S^{-1}$ on every index:

$$
\hat f = \sum_{PQ}\big[\mathbf S^{-1}\mathbf f\mathbf S^{-1}\big]_{PQ}a_P^\dagger a_Q,\qquad
\hat g = \frac12\sum_{PQRS}\Big(\sum_{IJKL}[\mathbf S^{-1}]_{PI}[\mathbf S^{-1}]_{JQ}[\mathbf S^{-1}]_{RK}[\mathbf S^{-1}]_{LS}\,g_{IJKL}\Big)a_P^\dagger a_R^\dagger a_Sa_Q,
$$

with $f_{PQ}$ and $g_{IJKL}$ the integrals over the nonorthogonal spin orbitals (HJO's charge-distribution order; [[second-quantized-operators]]). Both reduce to the usual forms when $\mathbf S = \mathbf 1$.

## Biorthogonal annihilators

All complications come from $\{a_P, a_Q^\dagger\} = S_{PQ}$. Define

$$
\bar a_P = \sum_Q[\mathbf S^{-1}]_{PQ}a_Q\quad\Rightarrow\quad \{\bar a_P, a_Q^\dagger\} = \delta_{PQ}.
$$

- **Excitation operators.** $a_P^\dagger\bar a_Q$ acts on ON vectors exactly like an orthonormal excitation operator, phase factors included.
- **Simpler operators.** $\hat f = \sum_{PQ}[\mathbf S^{-1}\mathbf f]_{PQ}a_P^\dagger\bar a_Q$: one factor of $\mathbf S^{-1}$ has been absorbed into $\bar a_Q$. The integrals $[\mathbf S^{-1}\mathbf f]_{PQ}$ are not Hermitian.
- **Not adjoints.** $\bar a_P \ne (a_P^\dagger)^\dagger$. The pair $\{a_P^\dagger, \bar a_Q\}$ is biorthogonal, not conjugate. Expectation values must therefore be formed with the true adjoint states.

**Where this is used (general knowledge).** Valence-bond and GVB wave functions ([[mcscf-and-gvb]]), nonorthogonal CI, and the transformed (biorthogonal) Hamiltonians that appear in coupled-cluster theory and in nonunitary orbital transformations ([[unitary-matrices-exponential-logarithm]]).

!!! example "Numerical checks (computed for this note)"
    Four spin orbitals with a random overlap matrix (unit diagonal, eigenvalues 0.557-1.875). Operators $a_P^\dagger = \sum_Q\tilde a_Q^\dagger[\mathbf S^{1/2}]_{QP}$ built from Jordan-Wigner matrices on the 16-dimensional Fock space.

    | Relation | Largest deviation |
    |---|---:|
    | $\{a_P^\dagger, a_Q^\dagger\} = 0$ | $1\times10^{-16}$ |
    | $\{a_P, a_Q^\dagger\} = S_{PQ}$ | $2\times10^{-15}$ |
    | $\langle\mathbf k|\mathbf m\rangle = \det\mathbf S_{\mathbf k\mathbf m}$, all 36 two-electron pairs | $3\times10^{-15}$ |
    | $a_P|\mathbf k\rangle$ by the overlap-weighted removal formula | $4\times10^{-16}$ |
    | $\langle\mathbf k|\hat f|\mathbf m\rangle$ against the first-quantization Löwdin rule $\frac{\mathrm d}{\mathrm d\lambda}\det(\mathbf S_{\mathbf k\mathbf m} + \lambda\mathbf f_{\mathbf k\mathbf m})\big|_0$ | $8\times10^{-11}$ (finite difference) |
    | $\{\bar a_P, a_Q^\dagger\} = \delta_{PQ}$ | $2\times10^{-15}$ |
    | $\sum[\mathbf S^{-1}\mathbf f]_{PQ}a_P^\dagger\bar a_Q = \sum[\mathbf S^{-1}\mathbf f\mathbf S^{-1}]_{PQ}a_P^\dagger a_Q$ | $4\times10^{-15}$ |

    $\bar a_1$ differs from $a_1$ by up to 0.33 in matrix elements: the biorthogonal annihilator is a genuinely different operator.

## Source

Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, Chichester, 2000), Sec. 1.9, pp. 27-30, Eqs. (1.9.1)-(1.9.25). The list of applications and the Löwdin-rule comparison are general knowledge. Numerical checks computed for this note (NumPy, SciPy).
