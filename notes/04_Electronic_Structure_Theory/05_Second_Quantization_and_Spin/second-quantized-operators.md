---
id: second-quantized-operators
title: Second-quantized one- and two-electron operators
summary: The one- and two-electron operators written with creation and annihilation operators, independent of electron number. The Hartree-Fock energy derived by anticommutation alone, and a numerical check that the second-quantized Hamiltonian of minimal-basis H2 reproduces the full CI spectrum.
status: in-progress
kind: derivation
level: intermediate
tags: [second-quantization, hamiltonian, matrix-elements, fock-space]
prerequisites: [creation-and-annihilation-operators, integral-notation]
related: [second-quantization-in-a-finite-basis, density-matrices-second-quantization, slater-condon-rules, molecular-hamiltonian, minimal-basis-h2-model, spin-tensor-operators, orbital-rotations, baker-campbell-hausdorff]
order: 20
date: 2026-11-03
---

## The operators

Sums run over all spin orbitals of the orthonormal set, occupied or not. Integrals are in physicists' notation over spin orbitals ([[integral-notation]]).

$$
\hat{\mathcal O}_1 = \sum_{ij}\langle i|h|j\rangle\,a_i^\dagger a_j,
\qquad
\hat{\mathcal O}_2 = \frac12\sum_{ijkl}\langle ij|kl\rangle\,a_i^\dagger a_j^\dagger a_l a_k .
$$

**Index order.** Note $a_la_k$, not $a_ka_l$. Creators carry the bra labels in order $i, j$, and annihilators carry the ket labels in **reverse** order, $l, k$. Reversing them flips the sign of the operator.

The electronic Hamiltonian is $\hat H = \hat{\mathcal O}_1 + \hat{\mathcal O}_2$ with $h$ the core Hamiltonian ([[molecular-hamiltonian]]).

These forms are justified because they give the same matrix elements between determinants as the first-quantized operators $\sum_i h(i)$ and $\sum_{i<j}r_{ij}^{-1}$, i.e. the [[slater-condon-rules]].

**Properties.**

- The particle number does not appear. One operator acts on every $N$-electron sector of Fock space, which is convenient for ionized states and infinite systems.
- The integrals enter explicitly.
- All antisymmetry is carried by the operator algebra.

Using $\{a_k,a_l\} = 0$ one can also write $\hat{\mathcal O}_2 = \frac14\sum_{ijkl}\langle ij||kl\rangle\,a_i^\dagger a_j^\dagger a_la_k$.

## Hartree-Fock energy by operator algebra

Take $|\Psi_0\rangle = |\chi_1\cdots\chi_N\rangle$ with occupied labels $a, b, c, d$.

**One-electron part.** In $\langle\Psi_0|a_i^\dagger a_j|\Psi_0\rangle$ both operators destroy an occupied electron (one to the left, one to the right), so $i, j$ must be occupied:

$$
\langle\Psi_0|\hat{\mathcal O}_1|\Psi_0\rangle = \sum_{ab}\langle a|h|b\rangle\langle\Psi_0|a_a^\dagger a_b|\Psi_0\rangle .
$$

Use $a_a^\dagger a_b = \delta_{ab} - a_ba_a^\dagger$. The second term vanishes because $a_a^\dagger|\Psi_0\rangle = 0$, so

$$
\langle\Psi_0|\hat{\mathcal O}_1|\Psi_0\rangle = \sum_a\langle a|h|a\rangle .
$$

**Two-electron part.** By the same argument all indices are occupied:

$$
\langle\Psi_0|\hat{\mathcal O}_2|\Psi_0\rangle = \tfrac12\sum_{abcd}\langle ab|cd\rangle\,\langle\Psi_0|a_a^\dagger a_b^\dagger a_da_c|\Psi_0\rangle .
$$

Move $a_d$ and $a_c$ to the left through the creators, each step producing a $\delta$ and a sign. Every leftover term has an $a^\dagger_{\text{occ}}$ acting on $|\Psi_0\rangle$ and vanishes, giving

$$
\langle\Psi_0|a_a^\dagger a_b^\dagger a_da_c|\Psi_0\rangle = \delta_{ac}\delta_{bd} - \delta_{ad}\delta_{bc},
$$

$$
\langle\Psi_0|\hat{\mathcal O}_2|\Psi_0\rangle = \tfrac12\sum_{ab}\big(\langle ab|ab\rangle - \langle ab|ba\rangle\big) = \tfrac12\sum_{ab}\langle ab||ab\rangle ,
$$

as in the Case 1 Slater-Condon rule.

!!! example "Matrix elements with excited determinants (Szabo Ex. 2.29-2.31)"
    **H₂ one-electron energy.** For minimal-basis H$_2$, $|\Psi_0\rangle = a_1^\dagger a_2^\dagger|\,\rangle$ gives $\langle\Psi_0|\hat{\mathcal O}_1|\Psi_0\rangle = \langle1|h|1\rangle + \langle2|h|2\rangle$.

    **Singles.** Write $\langle\Psi_a^r| = \langle\Psi_0|a_a^\dagger a_r$ and move $a_r$ and $a_i^\dagger$ through with anticommutators:
    $$
    \langle\Psi_a^r|\hat{\mathcal O}_1|\Psi_0\rangle = \sum_{ij}\langle i|h|j\rangle\langle\Psi_0|a_a^\dagger a_ra_i^\dagger a_j|\Psi_0\rangle = \langle r|h|a\rangle .
    $$

    **Doubles.**
    $$
    \langle\Psi_{ab}^{rs}|\hat{\mathcal O}_2|\Psi_0\rangle = \langle rs||ab\rangle ,
    $$
    the complex conjugate of the Case 3 rule $\langle\Psi_0|\hat{\mathcal O}_2|\Psi_{ab}^{rs}\rangle = \langle ab||rs\rangle$.

## Numerical check

For minimal-basis H$_2$ ($R = 1.4$ bohr, STO-3G; [[minimal-basis-h2-model]]):

1. Build $4\times4$-mode fermionic operators as $16\times16$ matrices with Jordan-Wigner strings, and confirm the canonical anticommutators.
2. Assemble $\hat H$ exactly as written above.
3. Diagonalize the $N = 2$ block.

The six eigenvalues (hartree, electronic) are:

| Eigenvalue | Degeneracy | Identified as |
|---:|---:|---|
| −1.851562 | 1 | full CI ground state $^1\Sigma_g^+$ |
| −1.246093 | 3 | triplet $^3\Sigma_u^+$, $h_{11}+h_{22}+J_{12}-K_{12}$ |
| −0.883577 | 1 | open-shell singlet $^1\Sigma_u^+$, $h_{11}+h_{22}+J_{12}+K_{12}$ |
| −0.233148 | 1 | second $^1\Sigma_g^+$ root of the 2x2 CI |

The ground state matches the determinant-based full CI. The open-shell energies match the spin-adapted formulas of [[spin-adapted-configurations]].

```python
import numpy as np
from functools import reduce
# h[i,j] = <i|h|j>, g[i,j,k,l] = <ij|kl> over 4 spin orbitals (see minimal-basis-h2-model)
n, Z, I2, a1 = 4, np.diag([1., -1.]), np.eye(2), np.array([[0., 1.], [0., 0.]])
A = [reduce(np.kron, [Z]*p + [a1] + [I2]*(n - p - 1)) for p in range(n)]   # annihilators
Ad = [x.T for x in A]
H = sum(h[i, j] * Ad[i] @ A[j] for i in range(n) for j in range(n))
H += 0.5 * sum(g[i, j, k, l] * Ad[i] @ Ad[j] @ A[l] @ A[k]
               for i in range(n) for j in range(n) for k in range(n) for l in range(n))
Nop = np.diag(sum(Ad[i] @ A[i] for i in range(n))).round()
idx = np.where(Nop == 2)[0]
print(np.linalg.eigvalsh(H[np.ix_(idx, idx)]))
```

## Jørgensen and Simons on the same operators

**Definition by matching.** J-S (Ch. 1, Sec. B) define the second-quantized operator as the one whose matrix elements between kets $\prod r^\dagger|\text{vac}\rangle$ equal those of the first-quantized operator between the corresponding determinants. They arrive at the same forms,

$$
\sum_{rs}\langle\phi_r|f|\phi_s\rangle r^\dagger s \leftrightarrow \sum_{i=1}^N f(\mathbf r_i),
\qquad
\frac12\sum_{rstu}\langle\phi_r\phi_s|g|\phi_t\phi_u\rangle r^\dagger s^\dagger ut \leftrightarrow \frac12\sum_{i\ne j}g(\mathbf r_i, \mathbf r_j),
$$

and stress that the operator order $r^\dagger s^\dagger ut$ is required for the correct signs.

**No N anywhere.** The operators do not refer to the electron number. The kinetic-energy operator of Be is identical to that of Be⁺ and Be⁻; nuclear charges appear only through the integrals. All $N$-dependence sits in the state vectors. J-S point out that this is what lets a single Hamiltonian describe neutral and ionized states at once, which is essential for Green's-function (propagator) methods.

**Selection rules built in.** $r^\dagger s$ can replace at most one spin orbital, so a one-electron operator connects kets differing by at most one label; $r^\dagger s^\dagger ut$ connects kets differing by at most two. These are the Slater-Condon rules, now properties of the operators.

!!! example "J-S's worked example: three electrons (Eqs. 1.19-1.22)"
    **The task.** Evaluate $\langle\hat{\mathcal O}_2\rangle$ for $|0\rangle = 2s_\alpha^\dagger1s_\beta^\dagger1s_\alpha^\dagger|\text{vac}\rangle$. The Slater-Condon rules give $J_{1s,1s} + 2J_{1s,2s} - K_{1s,2s}$, with $J_{ij} = \langle ij|ij\rangle$ and $K_{ij} = \langle ij|ji\rangle$.

    **Second-quantized route.** Write $\langle\hat{\mathcal O}_2\rangle = \tfrac12\sum\langle rs|tu\rangle\langle0|r^\dagger s^\dagger ut|0\rangle$. Anticommute $u$ and $t$ to the right, using $rs^\dagger = \delta_{rs} - s^\dagger r$, until they hit $|\text{vac}\rangle$. Do the same for $r^\dagger s^\dagger$ to the left. The surviving products of Kronecker deltas form the two-particle density matrix of the determinant. Summed against the integrals they give $J_{11} + 2J_{12} - K_{12}$: the $1s_\alpha1s_\beta$ pair contributes $J_{11}$, the two pairs with $2s_\alpha$ give $2J_{12}$, and the same-spin pair $1s_\alpha2s_\alpha$ gives the exchange term.

    **Check (computed for this note).** With random real two-orbital integrals and the operator built as a $16\times16$ Fock-space matrix, $\langle0|\hat{\mathcal O}_2|0\rangle$ equals $J_{11} + 2J_{12} - K_{12}$ to $10^{-10}$.

## Helgaker, Jørgensen and Olsen's conventions and the spin-free form

**Index order.** HJO write two-electron integrals in the charge-distribution order (chemists' notation),

$$
g_{PQRS} = \iint\phi_P^*(\mathbf x_1)\phi_R^*(\mathbf x_2)\,r_{12}^{-1}\,\phi_Q(\mathbf x_1)\phi_S(\mathbf x_2)\,\mathrm d\mathbf x_1\mathrm d\mathbf x_2 = (PQ|RS) = \langle PR|QS\rangle,
\qquad
\hat g = \tfrac12\sum_{PQRS}g_{PQRS}\,a_P^\dagger a_R^\dagger a_Sa_Q .
$$

This is the same operator as $\tfrac12\sum\langle ij|kl\rangle a_i^\dagger a_j^\dagger a_la_k$ above, relabelled.

**Spin-free operators.** For spin orbitals $\phi_p\sigma$ and spin-free $h$ and $g$, the spin integrations collapse the sums onto the singlet excitation operators $E_{pq} = a_{p\alpha}^\dagger a_{q\alpha} + a_{p\beta}^\dagger a_{q\beta}$ and the two-electron excitation operators $e_{pqrs}$:

$$
\hat H = \sum_{pq}h_{pq}E_{pq} + \tfrac12\sum_{pqrs}g_{pqrs}\,e_{pqrs} + h_{\text{nuc}},\qquad
e_{pqrs} = E_{pq}E_{rs} - \delta_{qr}E_{ps} = \sum_{\sigma\tau}a_{p\sigma}^\dagger a_{r\tau}^\dagger a_{s\tau}a_{q\sigma},
$$

with orbital integrals $h_{pq}$ and $g_{pqrs} = (pq|rs)$. For real orbitals $g_{pqrs}$ has eightfold symmetry. $e_{pqrs} = e_{rspq}$ has only that one, because spin integration ties index $p$ to $q$ and $r$ to $s$.

**Commutator toolkit.**

- **Rank-reduction rule.** The rank of a string is half its number of elementary operators. **Anticommute** two strings that both have half-integral rank; **commute** all other pairs. The result then has lower rank than the two strings combined (HJO Sec. 1.8, Exercise 1.2).
- **Expansions.** $[\hat A,\hat B_1\hat B_2] = [\hat A,\hat B_1]\hat B_2 + \hat B_1[\hat A,\hat B_2] = [\hat A,\hat B_1]_+\hat B_2 - \hat B_1[\hat A,\hat B_2]_+$, and their $n$-fold generalizations. Choose the form that produces rank reduction.
- **Elementary results.**

$$
[a_P^\dagger, a_Q^\dagger a_R] = -\delta_{PR}a_Q^\dagger,\qquad [a_P, a_Q^\dagger a_R] = \delta_{PQ}a_R,\qquad
[a_P^\dagger a_Q, a_R^\dagger a_S] = \delta_{QR}a_P^\dagger a_S - \delta_{PS}a_R^\dagger a_Q,
$$

$$
[E_{mn}, E_{pq}] = \delta_{pn}E_{mq} - \delta_{mq}E_{pn},\qquad [E_{mn}, a_{p\sigma}^\dagger] = \delta_{np}a_{m\sigma}^\dagger .
$$

  The singlet excitation operators obey the same algebra as the $n\times n$ matrix units: they generate the unitary group.
- **Nested.** $[a_P^\dagger a_Q,[a_R^\dagger a_S, a_M^\dagger a_N]] = \delta_{SM}\delta_{QR}a_P^\dagger a_N - \delta_{SM}\delta_{PN}a_R^\dagger a_Q - \delta_{RN}\delta_{QM}a_P^\dagger a_S + \delta_{RN}\delta_{PS}a_M^\dagger a_Q$ (rank reduced by 2). The Jacobi identity relates nested commutators of the same rank.
- **One-electron operators close under commutation (HJO Exercise 1.4).** $[\hat K,\hat F] = \sum_{PQ}(\mathbf K\mathbf F - \mathbf F\mathbf K)_{PQ}a_P^\dagger a_Q$. This is why orbital rotations act on operators through matrix algebra ([[orbital-rotations]]).

!!! example "Checks with Jordan-Wigner matrices (computed for this note)"
    - **Spin-orbital identities.** All of the above, for 5 spin orbitals and every index combination (3 orbitals for the nested commutator), hold exactly (deviation 0). Exercise 1.4 with random $\mathbf K$, $\mathbf F$ holds to $4\times10^{-15}$.
    - **Singlet identities.** $[E_{mn},E_{pq}]$ and $[E_{mn}, a_{p\sigma}^\dagger]$ hold exactly for 3 orbitals.
    - **Spin-free energy.** The full-CI water energy is reproduced from $h_{pq}$, $g_{pqrs}$ and the densities $\langle E_{pq}\rangle$, $\langle e_{pqrs}\rangle$ ([[density-matrices-second-quantization]]).

**Finite basis.** The operators are projections onto the spin-orbital basis. Products and commutators of projected operators differ from those of the exact operators unless the basis is complete ([[second-quantization-in-a-finite-basis]]).

## Source

Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996; reprint of the revised first edition, McGraw-Hill, 1989), Sec. 2.4.2, pp. 95-97, Eqs. (2.231)-(2.239), Ex. 2.29-2.31. Jørgensen and Simons, *Second Quantization-Based Methods in Quantum Chemistry* (Academic Press, New York, 1981), Ch. 1, Sec. B, pp. 5-8, Eqs. (1.15)-(1.22). Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, Chichester, 2000), Sec. 1.4, pp. 9-14; Sec. 1.8, pp. 25-27, Eqs. (1.8.1)-(1.8.17); Sec. 2.2.1, pp. 36-37, Eqs. (2.2.6)-(2.2.17); Sec. 2.3.5, p. 46, Eqs. (2.3.35)-(2.3.38); Exercises 1.2-1.4. Numerical checks computed for this note (PySCF 2.14 integrals, NumPy).
