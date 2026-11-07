---
id: creation-and-annihilation-operators
title: Creation and annihilation operators
summary: Second quantization in Szabo's convention. Creation and annihilation operators are defined by their action on Slater determinants, their anticommutation relations follow from determinant antisymmetry, determinants become strings of creation operators on the vacuum, and overlaps are evaluated by moving annihilators to the right.
status: in-progress
kind: derivation
level: intermediate
tags: [second-quantization, creation-operator, annihilation-operator, anticommutation, fock-space]
prerequisites: [slater-determinants]
related: [second-quantized-operators, nonorthogonal-second-quantization, second-quantization-in-a-finite-basis, excited-determinants, slater-condon-rules, baker-campbell-hausdorff, orbital-rotations]
order: 10
date: 2026-11-03
---

## Creation operators

For each spin orbital $\chi_i$ of an orthonormal set, define $a_i^\dagger$ by its action on any determinant. It **adds $\chi_i$ in the first column**:

$$
a_i^\dagger|\chi_k\cdots\chi_l\rangle = |\chi_i\chi_k\cdots\chi_l\rangle .
$$

**Order matters.**

$$
a_i^\dagger a_j^\dagger|\chi_k\cdots\chi_l\rangle = |\chi_i\chi_j\chi_k\cdots\chi_l\rangle,
\qquad
a_j^\dagger a_i^\dagger|\chi_k\cdots\chi_l\rangle = |\chi_j\chi_i\chi_k\cdots\chi_l\rangle = -|\chi_i\chi_j\chi_k\cdots\chi_l\rangle .
$$

Since the determinant is arbitrary, this is an operator identity:

$$
\{a_i^\dagger, a_j^\dagger\} = a_i^\dagger a_j^\dagger + a_j^\dagger a_i^\dagger = 0 .
$$

With $i = j$ it gives $a_i^\dagger a_i^\dagger = 0$: an electron cannot be created twice in one spin orbital (Pauli). More generally, $a_i^\dagger|\chi_k\cdots\chi_l\rangle = 0$ if $i\in\{k,\dots,l\}$, because the resulting determinant has two equal columns.

## Annihilation operators

Define $a_i \equiv (a_i^\dagger)^\dagger$. It **removes $\chi_i$ from the first column**:

$$
a_i|\chi_i\chi_k\cdots\chi_l\rangle = |\chi_k\cdots\chi_l\rangle .
$$

If $\chi_i$ is elsewhere, first move it to the front by column swaps, with a sign:

$$
a_i|\chi_k\chi_i\chi_l\rangle = -a_i|\chi_i\chi_k\chi_l\rangle = -|\chi_k\chi_l\rangle .
$$

**Why it is the adjoint.** With $|K\rangle = |\chi_i\chi_j\rangle = a_i^\dagger|\chi_j\rangle$, the adjoint equation is $\langle K| = \langle\chi_j|a_i$. Closing with $|K\rangle$: $1 = \langle K|K\rangle = \langle\chi_j|a_i|K\rangle$. This is consistent only if $a_i|\chi_i\chi_j\rangle = |\chi_j\rangle$, which is the definition above. Acting to the **left**, $a_i$ creates and $a_i^\dagger$ annihilates.

Taking the adjoint of the creator relation, using $(AB)^\dagger = B^\dagger A^\dagger$:

$$
\{a_i, a_j\} = 0,
\qquad
a_ia_i = 0 .
$$

An electron cannot be removed twice, and $a_i|\chi_k\cdots\chi_l\rangle = 0$ if $\chi_i$ is not occupied.

## Mixed anticommutator

Act with $a_ia_j^\dagger + a_j^\dagger a_i$ on an arbitrary determinant $|K\rangle$.

**Case $i = j$.**

- If $\chi_i$ is empty in $|K\rangle$: $a_i^\dagger a_i|K\rangle = 0$ and $a_ia_i^\dagger|K\rangle = |K\rangle$.
- If $\chi_i$ is occupied: $a_ia_i^\dagger|K\rangle = 0$, and $a_i^\dagger a_i$ removes $\chi_i$ and puts it back in the first column. Writing $|K\rangle$ with $\chi_i$ in front first, both sign changes cancel, so the result is $|K\rangle$.

Either way the sum is $|K\rangle$.

**Case $i\ne j$.** The result is nonzero only if $\chi_i$ is occupied and $\chi_j$ empty. Then, with $|K\rangle = |\chi_i\chi_k\cdots\rangle$:

$$
a_ia_j^\dagger|\chi_i\chi_k\cdots\rangle = a_i|\chi_j\chi_i\chi_k\cdots\rangle = -a_i|\chi_i\chi_j\chi_k\cdots\rangle = -|\chi_j\chi_k\cdots\rangle,
$$

$$
a_j^\dagger a_i|\chi_i\chi_k\cdots\rangle = a_j^\dagger|\chi_k\cdots\rangle = |\chi_j\chi_k\cdots\rangle,
$$

which sum to zero. Hence

$$
\{a_i, a_j^\dagger\} = \delta_{ij},
\qquad
a_ia_j^\dagger = -a_j^\dagger a_i\ (i\ne j),
\qquad
a_ia_i^\dagger = 1 - a_i^\dagger a_i .
$$

**These three anticommutators contain all properties of determinants.** From here on nothing else is needed.

## Vacuum and determinants as operator strings

The **vacuum** $|\,\rangle$ has no electrons, is normalized ($\langle\,|\,\rangle = 1$), and obeys

$$
a_i|\,\rangle = 0 = \langle\,|a_i^\dagger .
$$

Every determinant is a string of creators on the vacuum:

$$
|\chi_i\chi_j\cdots\chi_k\rangle = a_i^\dagger a_j^\dagger\cdots a_k^\dagger|\,\rangle,
\qquad
\langle\chi_i\chi_j\cdots\chi_k| = \langle\,|a_k\cdots a_j a_i .
$$

**Strategy for any matrix element:** move annihilators to the right with the anticommutators until each hits $|\,\rangle$ (giving zero) or is cancelled by a $\delta$.

!!! example "Overlap of two determinants, again (Szabo Eqs. 2.223-2.230)"
    $|K\rangle = a_i^\dagger a_j^\dagger|\,\rangle$ and $|L\rangle = a_k^\dagger a_l^\dagger|\,\rangle$, so $\langle K|L\rangle = \langle\,|a_ja_ia_k^\dagger a_l^\dagger|\,\rangle$.

    - **Move $a_i$ right.** Use $a_ia_k^\dagger = \delta_{ik} - a_k^\dagger a_i$:
    $$
    \langle K|L\rangle = \delta_{ik}\langle\,|a_ja_l^\dagger|\,\rangle - \langle\,|a_ja_k^\dagger a_ia_l^\dagger|\,\rangle .
    $$
    - **Continue in each term.** Repeat until every annihilator reaches the vacuum. The terms with $a|\,\rangle$ vanish, leaving
    $$
    \langle K|L\rangle = \delta_{ik}\delta_{jl} - \delta_{il}\delta_{jk},
    $$

    the same as expanding the determinants ([[slater-determinants]], Ex. 2.5).

## Useful identities with a reference determinant

Let $|\Psi_0\rangle = |\chi_1\cdots\chi_a\chi_b\cdots\chi_N\rangle$, with $a,b$ occupied and $r,s$ virtual (Szabo Ex. 2.27, 2.28).

- **Occupation number.** $a_i^\dagger a_j$ conserves particle number. For any determinant $|K\rangle$, $\langle K|a_i^\dagger a_j|K\rangle = \delta_{ij}$ if $\chi_i$ is occupied in $|K\rangle$ and $0$ otherwise. So $\hat n_i = a_i^\dagger a_i$ is the occupation-number operator.
- **Annihilation conditions.**
$$
a_r|\Psi_0\rangle = 0 = \langle\Psi_0|a_r^\dagger,
\qquad
a_a^\dagger|\Psi_0\rangle = 0 = \langle\Psi_0|a_a .
$$
- **Excitations as operator strings.**
$$
|\Psi_a^r\rangle = a_r^\dagger a_a|\Psi_0\rangle,
\qquad
\langle\Psi_a^r| = \langle\Psi_0|a_a^\dagger a_r,
$$
$$
|\Psi_{ab}^{rs}\rangle = a_s^\dagger a_b a_r^\dagger a_a|\Psi_0\rangle = a_r^\dagger a_s^\dagger a_b a_a|\Psi_0\rangle .
$$

The second form of the double follows by anticommuting: move $a_b$ past $a_r^\dagger$, then swap $a_s^\dagger a_r^\dagger$. That is two swaps, so the sign is $+1$, with no $\delta$ terms since all four indices differ. The order of $a_b a_a$ matters: it reproduces the "same column" convention of [[excited-determinants]].

!!! warning "Ordering conventions differ between books"
    Szabo's $a_i^\dagger$ inserts the new spin orbital in the **first** column. Other texts, including Helgaker-Jørgensen-Olsen, define occupation-number vectors with a fixed canonical orbital order and a phase from the number of occupied orbitals preceding $i$. Both satisfy the same anticommutators, but explicit phases of individual determinants can differ. Fix one convention before comparing CI vectors between codes.

## Helgaker, Jørgensen and Olsen: the Fock space of occupation-number vectors

**ON vectors.** In a basis of $M$ orthonormal spin orbitals, each determinant with spin orbitals in canonical order maps to an occupation-number vector $|\mathbf k\rangle = |k_1, k_2, \ldots, k_M\rangle$, $k_P\in\{0,1\}$. ON vectors are abstract basis vectors without spatial structure, with $\langle\mathbf k|\mathbf m\rangle = \prod_P\delta_{k_Pm_P}$, which is also defined (and zero) between different electron numbers.

**Fock space.** $F(M) = F(M,0)\oplus F(M,1)\oplus\cdots\oplus F(M,M)$ has dimension $2^M$, and the $N$-electron sector $F(M,N)$ has dimension $\binom MN$. $F(M,0)$ holds only the true vacuum $|\text{vac}\rangle = |0_1,\ldots,0_M\rangle$. The resolution of the identity runs over all ON vectors of all electron numbers.

**Phase convention.** Creation and annihilation carry the phase of the occupied spin orbitals **preceding** $P$ in the canonical order:

$$
a_P^\dagger|\mathbf k\rangle = \delta_{k_P0}\,\Gamma_P^{\mathbf k}\,|k_1,\ldots,1_P,\ldots,k_M\rangle,\qquad
a_P|\mathbf k\rangle = \delta_{k_P1}\,\Gamma_P^{\mathbf k}\,|k_1,\ldots,0_P,\ldots,k_M\rangle,\qquad
\Gamma_P^{\mathbf k} = \prod_{Q<P}(-1)^{k_Q} .
$$

This differs from Szabo's first-column convention (warning above), but the anticommutation relations are identical.

**Occupation-number operators.** $\hat N_P = a_P^\dagger a_P$ satisfies $\hat N_P|\mathbf k\rangle = k_P|\mathbf k\rangle$. The ON operators are Hermitian projectors ($\hat N_P^2 = \hat N_P$) that commute with each other, and $\hat N = \sum_P\hat N_P$ counts electrons. ON vectors are their simultaneous eigenvectors.

**Excitation operators (HJO Exercise 1.1).**

$$
a_P^\dagger a_Q|\mathbf k\rangle = \varepsilon_{PQ}\Gamma_P^{\mathbf k}\Gamma_Q^{\mathbf k}(1 - k_P + \delta_{PQ})k_Q\,|\mathbf k;\ k_Q\to0,\ k_P\to\delta_{PQ}\rangle,\qquad \varepsilon_{PQ} = \begin{cases}+1 & P\le Q\\ -1 & P>Q\end{cases}
$$

The sign $\varepsilon_{PQ}$ appears because, for $P>Q$, removing $Q$ first changes the parity seen by $P$.

!!! example "Check with Jordan-Wigner matrices (computed for this note)"
    $M = 5$, Fock space of dimension 32 with sectors of size 1, 5, 10, 10, 5, 1.

    - $\hat N_P^2 = \hat N_P$ and $[\hat N_P,\hat N_Q] = 0$ hold exactly.
    - The excitation formula above agrees with $a_P^\dagger a_Q$ applied to all 32 ON vectors, for all 25 index pairs, with no exceptions.

    The Jordan-Wigner construction with $Z$ strings on the spin orbitals **before** $P$ realizes exactly HJO's $\Gamma_P^{\mathbf k}$.

## The same algebra in Jørgensen and Simons

J-S (Ch. 1, Sec. A) start from the anticommutators rather than from determinants. A few of their statements are worth recording because later chapters rely on them.

**Kets and determinants are in correspondence, not equal.** J-S write

$$
r^\dagger s^\dagger\cdots t^\dagger|\text{vac}\rangle \leftrightarrow (N!)^{-1/2}\det|\phi_t\cdots\phi_s\phi_r| ,
$$

and stress that this is a one-to-one map, not an identity between functions and operator products. Note the **order**: the leftmost creator corresponds to the **last** column. This is the reverse of Szabo's $a_i^\dagger a_j^\dagger|\,\rangle = |\chi_i\chi_j\rangle$ (checked on the page image of J-S Eq. 1.1). The two conventions differ by the phase of reversing $N$ columns, $(-1)^{N(N-1)/2}$, the same for every determinant with $N$ electrons. Expectation values and energies are unaffected; individual CI coefficients and transition elements between states with different conventions are not.

**Nonorthogonal spin orbitals.** For a nonorthogonal set the mixed anticommutator becomes the overlap, $[r, s^\dagger]_+ = \langle\phi_r|\phi_s\rangle$, while $[r^\dagger, s^\dagger]_+ = [r, s]_+ = 0$ still hold. Most of the formalism assumes orthonormal orbitals for exactly this reason; the full treatment, with biorthogonal operators, is in [[nonorthogonal-second-quantization]].

**Number operators.** $\hat n_r = r^\dagger r$ has eigenvalue 1 on kets containing $\phi_r$ and 0 otherwise; $\hat N = \sum_r\hat n_r$ counts electrons. J-S's argument: with $r$ occupied, $r^\dagger r$ moves $r^\dagger$ to the front with sign $(-1)^{k_r}$, annihilates it, recreates it and moves it back with the same sign. With $r$ empty, $r^\dagger r$ gives zero.

**Replacement operators.** For $r\ne s$, $s^\dagger r$ acting on a ket containing $\phi_r$ (and not $\phi_s$) replaces $\phi_r$ by $\phi_s$ in the same position, with no sign: $s^\dagger r\,t^\dagger u^\dagger\cdots r^\dagger\cdots w^\dagger|\text{vac}\rangle = t^\dagger u^\dagger\cdots s^\dagger\cdots w^\dagger|\text{vac}\rangle$. This is the elementary step of orbital rotations ([[orbital-rotations]]) and of excitation operators.

**Density matrices replace determinant algebra.** Expectation values of one- and two-electron operators reduce to the one- and two-particle density matrices $\langle0|i^\dagger j|0\rangle$ and $\langle0|i^\dagger j^\dagger lk|0\rangle$. For a single determinant, anticommuting $u$ to the right and $t^\dagger$ to the left gives the second-quantized form of the one-electron Slater-Condon rule:

$$
\langle0|t^\dagger u|0\rangle = \delta_{tu}\,\nu_t ,
$$

with $\nu_t$ the occupation (1 or 0) of $\phi_t$ (J-S Eq. 1.14). For a multideterminant state the same matrix elements are computed from the expansion coefficients; this is how all of J-S's MCSCF and CI formulas are written ([[mcscf-second-order-optimization]]).

## Source

Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996; reprint of the revised first edition, McGraw-Hill, 1989), Sec. 2.4.1, pp. 89-95, Eqs. (2.190)-(2.230), Ex. 2.24-2.28. Jørgensen and Simons, *Second Quantization-Based Methods in Quantum Chemistry* (Academic Press, New York, 1981), Ch. 1, Sec. A, pp. 2-5, Eqs. (1.1)-(1.14). Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, Chichester, 2000), Secs. 1.1-1.3, pp. 1-9, Eqs. (1.1.1)-(1.3.18); Exercise 1.1.
