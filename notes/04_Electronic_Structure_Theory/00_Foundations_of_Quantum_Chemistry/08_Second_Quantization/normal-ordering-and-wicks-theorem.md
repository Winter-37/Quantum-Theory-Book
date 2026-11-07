---
id: normal-ordering-and-wicks-theorem
title: Normal ordering relative to the Fermi vacuum, contractions, Wick's theorem, and the normal-ordered Hamiltonian H = E_HF + F_N + V_N
summary: With the Hartree-Fock determinant as the Fermi vacuum, aᵢ (occupied) and aₐ† (virtual) create quasiparticles, and a normal-ordered string {…} has all quasi-annihilators to the right, so its vacuum expectation value is zero. Only two contractions are nonzero: aᵢ†aⱼ = δᵢⱼ and aₐaᵦ† = δₐᵦ. Wick's theorem writes any string as its normal-ordered form plus all contractions, with a sign (−1) per crossing. For products of normal-ordered strings only contractions between different strings survive. Applied to the Hamiltonian it gives H = E_HF + Σ f_pq{p†q} + ¼Σ⟨pq||rs⟩{p†q†sr}, with E_HF = Σhᵢᵢ + ½Σ⟨ij||ij⟩ and f_pq = h_pq + Σᵢ⟨pi||qi⟩. A corollary is the single-determinant variance of a one-body operator, Σ_{ia}|A_ai|². Everything was checked as exact operator identities in the full 4096-dimensional Fock space of LiH/STO-3G (12 spin orbitals): H − E_HF − F_N − V_N vanishes to 7 × 10⁻¹⁵, and Wick's theorem holds exactly for every tested a†a†aa string.
status: in-progress
kind: derivation
level: intermediate
tags: [second-quantization, normal-ordering, wick-theorem, fermi-vacuum, contractions, coupled-cluster, many-body]
prerequisites: [creation-and-annihilation-operators, second-quantized-operators]
related: [coupled-cluster-second-quantization, ccsd-spin-orbital-equations, coupled-cluster-diagrams, linked-cluster-theorem, perturbation-theory-second-quantization, brillouin-theorem, fock-operator]
also: []
date: 2026-11-07
---

## Conventions

- **Basis.** Real orthonormal spin orbitals $\{\chi_p\}$, with $a_p^\dagger$ and $a_p$ obeying $\{a_p,a_q^\dagger\}=\delta_{pq}$ and all other anticommutators zero ([[creation-and-annihilation-operators]]).
- **Reference.** $|\Phi_0\rangle = a_1^\dagger\cdots a_N^\dagger|\text{vac}\rangle$. Occupied indices $i,j,k,l,m,n$; virtual $a,b,c,d,e,f$; general $p,q,r,s$.
- **Integrals.** Physicists' antisymmetrized integrals, $\langle pq||rs\rangle = \langle pq|rs\rangle - \langle pq|sr\rangle$ ([[integral-notation]]).
- **Hamiltonian.**

$$
\hat H = \sum_{pq}h_{pq}\,a_p^\dagger a_q + \tfrac14\sum_{pqrs}\langle pq||rs\rangle\,a_p^\dagger a_q^\dagger a_s a_r .
$$

## Quasiparticles and normal order

**Two ways to annihilate the reference.** Relative to $|\Phi_0\rangle$,

$$
a_a|\Phi_0\rangle = 0,\qquad a_i^\dagger|\Phi_0\rangle = 0 .
$$

So $a_a$ (virtual) and $a_i^\dagger$ (occupied) are **quasi-annihilators**. Their partners $a_a^\dagger$ (create a particle) and $a_i$ (create a hole) are **quasi-creators**.

**Normal order.** A string is *normal ordered relative to $\Phi_0$*, written $\{ABC\cdots\}$, when it has been rearranged so that every quasi-creator stands to the left of every quasi-annihilator. The sign is that of the permutation, as if all operators anticommuted. Two consequences:

$$
\langle\Phi_0|\{ABC\cdots\}|\Phi_0\rangle = 0\quad\text{(nonempty string)},\qquad \{\cdots AB\cdots\} = -\{\cdots BA\cdots\}.
$$

**Example.**

- In $a_i^\dagger a_j$ the quasi-annihilator $a_i^\dagger$ stands left of the quasi-creator $a_j$, so normal ordering swaps them: $\{a_i^\dagger a_j\} = -a_j a_i^\dagger$.
- $a_a^\dagger a_b$ is already normal ordered: $\{a_a^\dagger a_b\} = a_a^\dagger a_b$.
- $a_a^\dagger a_i$ (a quasi-creator times a quasi-creator) is normal ordered, and $\{a_i^\dagger a_a\} = a_i^\dagger a_a$ (two quasi-annihilators).

## Contractions

**Definition.** The contraction of two operators is what remains after normal ordering,

$$
\overline{AB} \equiv AB - \{AB\} = \langle\Phi_0|AB|\Phi_0\rangle .
$$

Only two are nonzero:

$$
\overline{a_i^\dagger a_j} = \delta_{ij},\qquad \overline{a_a a_b^\dagger} = \delta_{ab}.
$$

**Proof sketch.** $a_i^\dagger a_j = -a_j a_i^\dagger + \delta_{ij} = \{a_i^\dagger a_j\} + \delta_{ij}$. Similarly $a_a a_b^\dagger = -a_b^\dagger a_a + \delta_{ab}$. Every other ordered pair is either already normal ordered or anticommutes to a normal-ordered pair with no remainder.

**Two consequences.**

- A contraction always pairs a $\dagger$ with a non-$\dagger$, and both must be occupied (dagger on the left) or both virtual (dagger on the right).
- A contraction of the form $\overline{a_p^\dagger a_q}$ with $p,q$ general therefore means $\delta_{pq}$ restricted to occupied $p$. I write it $\delta_{pq}^{\text{o}}$.

## Wick's theorem

**Statement.** For a string $A_1A_2\cdots A_n$ of creation and annihilation operators,

$$
A_1\cdots A_n = \{A_1\cdots A_n\} + \sum_{\text{singles}}\{\overline{A_\mu\cdots A_\nu}\cdots\} + \sum_{\text{doubles}}\{\overline{A\cdots A}\,\overline{A\cdots A}\cdots\} + \cdots ,
$$

where each term contracts one, two, ... disjoint pairs in all possible ways and leaves the rest normal ordered.

**Sign.** It is $(-1)^{c}$ with $c$ the number of crossings when all contraction lines are drawn above the string. Equivalently, it is the parity of the permutation that brings each contracted pair together.

**Corollaries.**

- **Expectation values.** $\langle\Phi_0|A_1\cdots A_n|\Phi_0\rangle$ is the sum of the *fully* contracted terms only.
- **Generalized Wick theorem.** For a product of strings that are each already normal ordered, $\{A\cdots\}\{B\cdots\}\cdots$, contractions inside one string are absent. Only contractions *between* different strings appear. This is what makes coupled-cluster algebra (with $\hat H_N$ and $\hat T$ both normal ordered) manageable.
- **Connected terms.** Because the cluster operators contain only quasi-creators, $\hat T$ strings can contract only with $\hat H_N$ and never with each other.

!!! example "The two-body string"
    For $a_p^\dagger a_q^\dagger a_s a_r$ (positions 1-4), the nonzero single contractions are (1,3), (1,4), (2,3) and (2,4). Their signs are $(-1)^{\text{operators between}}$: $-,+,+,-$. The full contractions are (14)(23), with sign $+$, and (13)(24), with sign $-$. Hence

    $$
    \begin{aligned}
    a_p^\dagger a_q^\dagger a_s a_r ={}& \{a_p^\dagger a_q^\dagger a_s a_r\}
    + \delta^{\text o}_{qs}\{a_p^\dagger a_r\} - \delta^{\text o}_{qr}\{a_p^\dagger a_s\}
    - \delta^{\text o}_{ps}\{a_q^\dagger a_r\} + \delta^{\text o}_{pr}\{a_q^\dagger a_s\}\\
    &+ \delta^{\text o}_{pr}\delta^{\text o}_{qs} - \delta^{\text o}_{ps}\delta^{\text o}_{qr} .
    \end{aligned}
    $$

## The normal-ordered Hamiltonian

**One-body part.** $a_p^\dagger a_q = \{a_p^\dagger a_q\} + \delta^{\text o}_{pq}$.

**Two-body part.** Insert the two-body string into $\tfrac14\sum\langle pq||rs\rangle\cdots$ and use the antisymmetry of $\langle pq||rs\rangle$ in each index pair.

- The four single-contraction terms are equal and add to $\sum_{pq}\sum_i\langle pi||qi\rangle\{a_p^\dagger a_q\}$.
- The two full contractions give $\tfrac14\big(\sum_{ij}\langle ij||ij\rangle - \sum_{ij}\langle ij||ji\rangle\big) = \tfrac12\sum_{ij}\langle ij||ij\rangle$.

Collecting terms:

$$
\boxed{\hat H = E_{\text{HF}} + \underbrace{\sum_{pq}f_{pq}\{a_p^\dagger a_q\}}_{\hat F_N} + \underbrace{\tfrac14\sum_{pqrs}\langle pq||rs\rangle\{a_p^\dagger a_q^\dagger a_s a_r\}}_{\hat V_N}}
$$

with

$$
E_{\text{HF}} = \langle\Phi_0|\hat H|\Phi_0\rangle = \sum_i h_{ii} + \tfrac12\sum_{ij}\langle ij||ij\rangle,\qquad
f_{pq} = h_{pq} + \sum_i\langle pi||qi\rangle .
$$

**Remarks.**

- $\hat H_N \equiv \hat H - E_{\text{HF}} = \hat F_N + \hat V_N$ has zero reference expectation value. It is the Hamiltonian used in CC and MBPT ([[coupled-cluster-second-quantization]], [[ccsd-spin-orbital-equations]]).
- $f_{pq}$ is the Fock matrix of the reference ([[fock-operator]]). It appears here from the algebra alone, without minimizing anything, so the decomposition holds for *any* reference determinant.
- **Canonical HF.** For canonical Hartree-Fock orbitals, $f_{ia}=0$ (Brillouin, [[brillouin-theorem]]) and $f_{pq}=\varepsilon_p\delta_{pq}$.
- **Partitioning.** $\hat F_N$ (diagonal part) is the Møller-Plesset $\hat H_0 - \langle\hat H_0\rangle$ and $\hat V_N$ is the fluctuation potential.

**Variance of a one-body operator.** For $\hat A = \sum_{pq}A_{pq}a_p^\dagger a_q = \langle\hat A\rangle + \sum A_{pq}\{a_p^\dagger a_q\}$, the generalized Wick theorem gives $\langle\Phi_0|\{a_p^\dagger a_q\}\{a_r^\dagger a_s\}|\Phi_0\rangle = \delta_{ps}^{\text o}\,\delta_{qr}^{\text v}$. Hence

$$
\langle\hat A^2\rangle - \langle\hat A\rangle^2 = \sum_{i\in\text{occ}}\sum_{a\in\text{virt}}A_{ia}A_{ai} = \sum_{ia}|A_{ai}|^2 .
$$

This is the $\hat S_z$ test used in [[hf-solution-classification]].

!!! example "Operator identities in the full Fock space of LiH/STO-3G (computed for this note)"
    **Setup.** LiH at 1.6 Å with STO-3G: 6 spatial orbitals, 12 spin orbitals, 4 electrons, RHF reference. All operators are $4096\times4096$ sparse matrices built with the Jordan-Wigner representation.

    - **Normal ordering.** Each $\{\cdots\}$ is built *independently of Wick's theorem*. The string is reordered with quasi-creators first, and the sign comes from the permutation parity.
    - **Hartree-Fock energy.** $\langle\Phi_0|\hat H|\Phi_0\rangle + V_{nn} = -7.861864770\,E_h$, equal to PySCF's RHF energy. It also equals $\sum h_{ii} + \tfrac12\sum\langle ij||ij\rangle$ to $4\times10^{-15}$.
    - **Normal-ordered Hamiltonian.** $\max|\hat H - E_{\text{HF}} - \hat F_N - \hat V_N| = 6.9\times10^{-15}$ over the *whole* Fock space, all particle numbers. So the boxed identity is an operator identity, not just an $N$-electron statement.
    - **Wick's theorem.** For 37 random strings $a_p^\dagger a_q^\dagger a_s a_r$ with at least one nonzero contraction, the expansion in the example above matches the operator product exactly. Dropping the contraction terms gives errors of order 1.
    - **Variance formula.** For a random real symmetric one-body operator, $\langle A^2\rangle-\langle A\rangle^2 = 61.343462141900$ exactly and by $\sum_{ia}A_{ai}^2$.

## Source

T. D. Crawford, *Coupled Cluster Theory*, ESQC 2026 lecture slides, part 1 (sections "Normal ordering", "Operator contractions", "Wick's theorem", "The normal-ordered Hamiltonian").

T. D. Crawford and H. F. Schaefer, "An Introduction to Coupled Cluster Theory for Computational Chemists", *Rev. Comput. Chem.* **14**, 33-136 (2000), doi:10.1002/9780470125915.ch2.

I. Shavitt and R. J. Bartlett, *Many-Body Methods in Chemistry and Physics* (Cambridge University Press, 2009): chapter on second quantization and Wick's theorem (chapter/page numbers to add).

Derivations restated in my own notation. Numerical checks: `esqc/cc/wick_check.py` with `esqc/cc/fermi.py` (PySCF 2.15).
