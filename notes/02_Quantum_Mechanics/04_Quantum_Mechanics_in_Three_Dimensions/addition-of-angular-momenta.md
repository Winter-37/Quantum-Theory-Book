---
id: addition-of-angular-momenta
title: Addition of angular momenta; singlet, triplet and Clebsch–Gordan coefficients
summary: Coupling two angular momenta. M = m₁ + m₂, and the total s runs from s₁+s₂ down to |s₁−s₂|. Derives the two-spin-½ triplet and singlet by lowering and checks them with S² = S₁² + S₂² + 2S₁·S₂. Clebsch–Gordan coefficients expand |s m⟩ in product states and back; worked table lookups, measurement probabilities on coupled states (spin-orbit for ψ₅₁₀ with spin down), why S₁z does not commute with S², and three spins ½ (one quartet, two doublets).
status: in-progress
kind: derivation
level: intermediate
tags: [angular-momentum-coupling, clebsch-gordan, singlet, triplet, total-spin, spin-orbit-coupling, tensor-product, griffiths]
prerequisites: [spin-one-half, orbital-angular-momentum]
related: [spin-operators, spin-adapted-configurations, genealogical-coupling, spin-orbitals-and-antisymmetry]
order: 60
date: 2026-11-04
---

## Setup

**Product states.** Two subsystems with angular momenta $\mathbf S^{(1)}$ (quantum numbers $s_1, m_1$) and $\mathbf S^{(2)}$ ($s_2, m_2$) live in the product space, with basis $|s_1s_2m_1m_2\rangle$. The operators of different subsystems commute.

**Total angular momentum.** $\mathbf S = \mathbf S^{(1)}+\mathbf S^{(2)}$. Its $z$ component simply adds:

$$
S_z|s_1s_2m_1m_2\rangle = \hbar(m_1+m_2)|s_1s_2m_1m_2\rangle,\qquad m = m_1+m_2 .
$$

The total quantum number $s$ is the subtle part.

## Two spins ½

**The puzzle.** The product basis $|{\uparrow\uparrow}\rangle, |{\uparrow\downarrow}\rangle, |{\downarrow\uparrow}\rangle, |{\downarrow\downarrow}\rangle$ has $m = 1,0,0,-1$. This is one $m=0$ too many for a single $s=1$ multiplet.

**Lowering.** Lower from $|{\uparrow\uparrow}\rangle$ with $S_- = S_-^{(1)}+S_-^{(2)}$:

$$
S_-|{\uparrow\uparrow}\rangle = \hbar(|{\downarrow\uparrow}\rangle+|{\uparrow\downarrow}\rangle).
$$

This gives the **triplet** ($s=1$):

$$
|1\,1\rangle = |{\uparrow\uparrow}\rangle,\qquad
|1\,0\rangle = \tfrac{1}{\sqrt2}(|{\uparrow\downarrow}\rangle+|{\downarrow\uparrow}\rangle),\qquad
|1\,{-1}\rangle = |{\downarrow\downarrow}\rangle .
$$

**The orthogonal $m=0$ state** is the **singlet** ($s=0$):

$$
|0\,0\rangle = \tfrac{1}{\sqrt2}(|{\uparrow\downarrow}\rangle-|{\downarrow\uparrow}\rangle).
$$

**Proof via $S^2$.**

$$
S^2 = (S^{(1)})^2+(S^{(2)})^2+2\mathbf S^{(1)}\cdot\mathbf S^{(2)} .
$$

Using the Pauli matrices, $\mathbf S^{(1)}\cdot\mathbf S^{(2)}|{\uparrow\downarrow}\rangle = \tfrac{\hbar^2}{4}(2|{\downarrow\uparrow}\rangle-|{\uparrow\downarrow}\rangle)$. Hence

$$
\mathbf S^{(1)}\cdot\mathbf S^{(2)}|1\,0\rangle = \tfrac{\hbar^2}{4}|1\,0\rangle,\qquad
\mathbf S^{(1)}\cdot\mathbf S^{(2)}|0\,0\rangle = -\tfrac{3\hbar^2}{4}|0\,0\rangle,
$$

$$
S^2|1\,0\rangle = \left(\tfrac34+\tfrac34+\tfrac12\right)\hbar^2|1\,0\rangle = 2\hbar^2|1\,0\rangle,\qquad S^2|0\,0\rangle = 0 .
$$

**Numerical check.** The eigenvalues of $\mathbf S^{(1)}\cdot\mathbf S^{(2)}$ on the 4-dimensional space are $\{-\tfrac34, \tfrac14, \tfrac14, \tfrac14\}\hbar^2$.

**Chemistry.** In a two-electron system the triplet spin functions are symmetric under exchange and the singlet is antisymmetric. Combined with the Pauli principle, this pairs spin symmetry with spatial symmetry ([[spin-orbitals-and-antisymmetry]], and Ch. 5).

## General rule and Clebsch–Gordan coefficients

**Allowed totals.** Combining $s_1$ and $s_2$ gives every total from the parallel to the antiparallel limit, in integer steps:

$$
s = s_1+s_2,\ s_1+s_2-1,\ \ldots,\ |s_1-s_2| .
$$

**Dimension check.** $\sum_s(2s+1) = (2s_1+1)(2s_2+1)$.

**Examples.**

- Spin $\tfrac32\otimes$ spin 2 gives $s = \tfrac72,\tfrac52,\tfrac32,\tfrac12$.
- An electron in $\psi_{n\ell m}$ has $j = \ell\pm\tfrac12$.
- Adding the proton spin gives $f = \ell+1, \ell, \ell, \ell-1$. The value $f = \ell$ appears twice.

**Clebsch–Gordan expansion.** The coupled states expand in the product states:

$$
|s\,m\rangle = \sum_{m_1+m_2=m}C^{s_1s_2s}_{m_1m_2m}\,|s_1s_2m_1m_2\rangle,
\qquad
|s_1s_2m_1m_2\rangle = \sum_sC^{s_1s_2s}_{m_1m_2m}\,|s\,m\rangle .
$$

The CG coefficients are real and form an orthogonal matrix. Columns are normalized for the first expansion and rows for the second.

**Group theory.** In group-theory language this is the decomposition of a direct product of two irreducible representations of the rotation group into a direct sum of irreducible ones.

## Worked examples

All coefficients below were computed with `sympy.physics.quantum.cg`, which uses the same Condon–Shortley convention as Griffiths Table 4.8.

!!! example "Reading the table (Griffiths text examples)"
    **$2\otimes1$, state $|3\,0\rangle$.**

    $$
    |3\,0\rangle = \tfrac{1}{\sqrt5}|2\,1\rangle|1\,{-1}\rangle + \sqrt{\tfrac35}|2\,0\rangle|1\,0\rangle + \tfrac{1}{\sqrt5}|2\,{-1}\rangle|1\,1\rangle .
    $$

    A measurement of $S_z^{(1)}$ gives $\hbar$, 0 or $-\hbar$ with probabilities $\tfrac15, \tfrac35, \tfrac15$.

    **$\tfrac32\otimes1$, product state $|\tfrac32\,\tfrac12\rangle|1\,0\rangle$.**

    $$
    |\tfrac32\,\tfrac12\rangle|1\,0\rangle = \sqrt{\tfrac35}\,|\tfrac52\,\tfrac12\rangle + \sqrt{\tfrac1{15}}\,|\tfrac32\,\tfrac12\rangle - \sqrt{\tfrac13}\,|\tfrac12\,\tfrac12\rangle .
    $$

    A total-spin measurement gives $s = \tfrac52, \tfrac32, \tfrac12$ with probabilities $\tfrac35, \tfrac1{15}, \tfrac13$.

!!! example "Problem 4.40"
    **(a) Spin 1 and spin 2 in $|3\,1\rangle$.** The probabilities for $m_2$ of the spin-2 particle are

    | $m_2$ | 2 | 1 | 0 |
    |---|---|---|---|
    | Probability | $1/15$ | $8/15$ | $2/5$ |

    $m_1 = 1-m_2$ must lie in $\{-1,0,1\}$, which excludes $m_2 = -1$.

    **(b) Electron in $\psi_{510}$ with spin down.** Couple $\ell=1$, $m_\ell=0$ with $s=\tfrac12$, $m_s=-\tfrac12$:

    $$
    |1\,0\rangle|\tfrac12\,{-\tfrac12}\rangle\ \to\ j = \tfrac32\ \text{with probability } \tfrac23,\qquad j = \tfrac12\ \text{with probability } \tfrac13 .
    $$

    So $J^2 = \tfrac{15}{4}\hbar^2$ or $\tfrac34\hbar^2$ with these probabilities. This is the spin–orbit coupled basis needed for fine structure.

**Why the coupled states mix product states** (Problem 4.41):

$$
[S^2,S_z^{(1)}] = 2i\hbar\,(\mathbf S^{(1)}\times\mathbf S^{(2)})_z\neq0,
$$

checked as a matrix identity. Eigenstates of $S^2$ therefore cannot also be eigenstates of $S_z^{(1)}$; the CG coefficients do the mixing. The sum $S_z = S_z^{(1)}+S_z^{(2)}$ does commute with $S^2$.

!!! example "Three spins ½ (Problem 4.65)"
    **Decomposition.** $\tfrac12\otimes\tfrac12\otimes\tfrac12 = \tfrac32\oplus\tfrac12\oplus\tfrac12$. Diagonalizing $S^2$ on the 8-dimensional space gives $\tfrac{15}{4}\hbar^2$ four times and $\tfrac34\hbar^2$ four times: one quartet and two doublets.

    **Quartet.** Start from $|{\uparrow\uparrow\uparrow}\rangle$ and lower.

    **Doublets.** A singlet on particles 1-2 times $|{\uparrow}\rangle_3$ is one doublet: $S^2 = \tfrac34\hbar^2$, $S_z = \tfrac12\hbar$. Any combination with the second, orthogonal doublet (from the $s_{12}=1$ triplet coupled down to $\tfrac12$) also has $s=\tfrac12$, so the doublets are not unique. This non-uniqueness is the origin of the several spin-adapted configuration functions (CSFs) for one open-shell configuration ([[spin-adapted-configurations]], [[genealogical-coupling]]).

## Source

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Sec. 4.4.3, Eqs. (4.171)-(4.185), Example 4.5, Table 4.8 (consulted; values recomputed rather than copied); Problems 4.37-4.41, 4.65. Page numbers are not given because the PDF used is an e-book rendering without print pagination. The links to CSFs and exchange symmetry are additions. Checks are in `griffiths/ch04_3d.py` (section F).
