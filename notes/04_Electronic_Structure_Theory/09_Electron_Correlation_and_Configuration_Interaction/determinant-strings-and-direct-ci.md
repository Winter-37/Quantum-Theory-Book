---
id: determinant-strings-and-direct-ci
title: Determinants as products of alpha and beta strings - RAS string classes, graph addressing, sparsity of H, N-resolution and minimal-operation-count direct CI, M_S = 0 symmetry, CI orbital transformations, and symmetry-broken CI
summary: How large determinant CI programs work. A determinant is an alpha string times a beta string, so CI vectors are matrices C(Iα, Iβ). RAS restrictions become allowed pairs of string classes. A reverse-lexical graph turns occupations into addresses by summing arc weights. H is extremely sparse in the determinant basis, so σ = HC is built directly from integrals: the N-resolution method costs about n⁴N_det/4, the minimal-operation-count method one operation per nonzero element. M_S = 0 states have C(Iα,Iβ) = (−1)^S C(Iβ,Iα). A CI vector can be re-expressed in rotated or nonorthogonal orbitals by n one-index-like contractions using an LU factorization of the orbital transformation. All of these were checked numerically, including an N-resolution σ against PySCF and the sequential orbital transformation against PySCF's transform_ci.
status: in-progress
kind: algorithm
level: advanced
tags: [direct-ci, spin-strings, ras, string-addressing, sigma-vector, n-resolution, minimal-operation-count, time-reversal-symmetry, ci-orbital-transformation, lu-decomposition, symmetry-breaking]
prerequisites: [full-ci, second-quantized-operators, slater-condon-rules]
related: [ci-optimization-newton-and-davidson, ci-size-extensivity-and-excitation-levels, ci-in-practice, nonorthogonal-second-quantization, rhf-instabilities-and-multiple-solutions]
order: 90
date: 2026-11-04
---

## Alpha and beta strings

**Factorization (HJO Sec. 11.6).** With $N_\alpha = \tfrac12N + M$ and $N_\beta = \tfrac12N - M$, every determinant is $\hat\alpha_{I_\alpha}\hat\beta_{I_\beta}|\text{vac}\rangle$, an ordered product of α creation operators and then β ones.

- **CI vector as a matrix.** The vector becomes a matrix $C_{I_\alpha I_\beta}$ of dimension $\binom n{N_\alpha}\times\binom n{N_\beta}$, much smaller in each dimension than $N_{\text{det}}$.
- **Singlets.** The matrix is symmetric.

**RAS spaces.** Strings are sorted into classes by their RAS1 and RAS3 occupations, and only certain class pairs are allowed. The CI vector becomes a set of blocks.

!!! example "HJO Tables 11.5-11.7 (checked)"
    **Example.** Three electrons in five orbitals give 10 strings.

    - **Order.** In reverse lexical order they are 123, 124, 134, 234, 125, 135, 235, 145, 245, 345.
    - **RAS restriction.** RAS1 = {1, 2} with at least 3 electrons in total and RAS3 = {4, 5} with at most 2 electrons leaves **37** of the 100 determinants. This is HJO's count, obtained here by enumeration.

## Addressing strings with a graph

**Paths (HJO Sec. 11.8.2).** A string is a path from $(0,0)$ to $(n,N)$. A diagonal arc into $(k,m)$ means orbital $k$ is occupied, and a vertical arc means it is empty.

**Weights.**

- **Vertex weights** count paths: $W_{k,m} = W_{k-1,m} + W_{k-1,m-1}$, with $W_{0,0} = 1$ and forbidden vertices set to 0.
- **Arc weights.** In reverse lexical order a vertical arc has weight 0, and a diagonal arc ending at $(k,m)$ has weight $Y_{k,m} = W_{k-1,m}$.
- **Address.** $1 + \sum_{\text{occupied }k}Y_{k,m_k}$.

**Check.** My implementation returns addresses 1-10, in order, for the ten strings above.

## How sparse is H?

**Counting (HJO Sec. 11.7).** The nonzero elements of one- and two-electron operators per determinant come from single and double excitations:

$$
L_1 = N_{\text{det}}\big[1 + N_\alpha(n-N_\alpha) + N_\beta(n-N_\beta)\big],
$$

$$
L_2 = N_{\text{det}}\big[\cdots + N_\alpha N_\beta(n-N_\alpha)(n-N_\beta) + \tfrac14N_\alpha(N_\alpha-1)(n-N_\alpha)(n-N_\alpha-1) + \tfrac14N_\beta(N_\beta-1)(\cdots)\big].
$$

!!! example "12 electrons in 12 orbitals (computed for this note)"
    - **Size.** $N_{\text{det}}$ = 853 776, so the full matrix has $7.29\times10^{11}$ elements.
    - **One-electron operator.** $L_1 = 6.23\times10^7$ nonzero elements (HJO: same).
    - **Two-electron operator.** The exact count (11.7.15) gives $L_2 = 1.55\times10^9$. HJO's $1.66\times10^9$ is the leading-order formula (11.7.16), $N_{\text{det}}[N_\alpha N_\beta(n-N_\alpha)(n-N_\beta) + \tfrac14N_\alpha^2(n-N_\alpha)^2 + \tfrac14N_\beta^2(n-N_\beta)^2]$.
    - **Sparsity.** Either way there are about 470-500 zeros for every nonzero element. In the orbital basis the same operator needs only $12^4$ = 20 736 integrals.

## Direct CI: building σ = HC from integrals

**Rewriting the Hamiltonian (HJO Sec. 11.8.3).** With $k_{pq} = h_{pq} - \tfrac12\sum_rg_{prrq}$, $\hat H = \sum_{pq}k_{pq}\hat E_{pq} + \tfrac12\sum_{pqrs}g_{pqrs}\hat E_{pq}\hat E_{rs}$.

**N-resolution method.** Insert a resolution of the identity in the $N$-electron space and proceed in three steps:

$$
D_{rs,K} = \sum_J\langle K|\hat E_{rs}|J\rangle C_J,\qquad G_{pq,K} = \sum_{rs}g_{pqrs}D_{rs,K},\qquad \sigma_I = \sum_{pq}k_{pq}D_{pq,I} + \tfrac12\sum_{pq,K}\langle I|\hat E_{pq}|K\rangle G_{pq,K}.
$$

- **Cost.** The middle step is a dense matrix product, about $n^4N_{\text{det}}/4$ operations with permutational symmetry. That is 2-3 times the theoretical minimum for $N\approx n$, and worse otherwise.

**Minimal operation count (MOC) (HJO Sec. 11.8.4).** Split $\hat E_{pq} = \hat E^\alpha_{pq} + \hat E^\beta_{pq}$.

- **Same-spin terms.** The αα and ββ terms use sparse string-space matrices $k^\alpha$ and $G^{\alpha\alpha}$, applied row by row.
- **Mixed term.** The αβ term uses $D^{\beta}_{I_\alpha J_\beta}[pq] = \sum_{J_\alpha}\langle I_\alpha|\hat E^\alpha_{pq}|J_\alpha\rangle C_{J_\alpha J_\beta}$, restricted to the nonvanishing rows, and $G^{\beta}[pq] = \sum_{rs}g_{pqrs}\langle\cdot|\hat E^\beta_{rs}|\cdot\rangle$.
- **Cost.** To leading order this equals the number of nonzero elements, the lower bound.
- **Comparison.** The N-resolution/MOC cost ratio is 21, 4.7, 2.7, 4.7 and 21 for $N_\alpha/n$ = 0.1, 0.25, 0.5, 0.75 and 0.9 (HJO Table 11.8).

**RAS direct CI (HJO Sec. 11.8.5).**

- **String counts.** For CISD, strings number $1 + OV + \tfrac14O^2V^2$ per spin, comparable to the number of determinants.
- **Substrings.** HJO split strings further into occupied and virtual substrings. Then, for example, the $C^{02}$ block (one α string, many β strings) uses $V(V-1)/2$ virtual substrings, with matrix elements $g_{egfh} - g_{ehfg}$.

**$M_S = 0$ (HJO Sec. 11.8.6).** The spin-flip operator $\hat U_{\alpha\beta} = \exp[i\pi(\hat S_x - \tfrac12\hat N)]$ swaps α and β. A state of spin $S$ with $M_S = 0$ satisfies $C_{I_\alpha I_\beta} = (-1)^SC_{I_\beta I_\alpha}$. This halves the parameters and the cost of σ.

**Density matrices.** These cost the same as one σ for an operator of the same rank.

!!! example "A direct σ from α/β excitation lists (computed for this note)"
    **System.** Water, STO-3G: 7 orbitals, $(5\alpha, 5\beta)$, 21 × 21 strings.

    **Method.** I built the excitation lists with PySCF's `cistring` and implemented the three N-resolution steps with $k_{pq}$.

    **Result.** For a random CI matrix, σ agrees with PySCF's `direct_spin1.contract_2e` to $2\times10^{-13}$ (largest element 254).

## Re-expressing a CI vector in new orbitals

**The task (HJO Sec. 11.9).** Find $\mathbf c^{(n)}$ such that $\sum_iC_i^{(0)}|i^{(0)}\rangle = \sum_jC^{(n)}_j|j^{(n)}\rangle$ when $a^{(n)\dagger}_p = \sum_qa^{(0)\dagger}_qD_{qp}$, where $\mathbf D$ need not be unitary. HJO's alternative to reoptimizing is due to Malmqvist (their ref. 17).

**The method.** Replace one orbital at a time.

- **Step $k$.** It uses biorthogonal annihilators ([[nonorthogonal-second-quantization]]) and is a single σ-like contraction with one fixed index:

$$
\mathbf C^{(k)} = \mathbf C^{(k-1)} + \sum_p(t_{pk} - \delta_{pk})\,\hat E_{pk}\mathbf C^{(k-1)} .
$$

- **Coefficients.** They follow from $\mathbf D\mathbf t^U + \mathbf t^L = \mathbf 1$. With $\mathbf D = \mathbf L\mathbf U$ ($\mathbf L$ unit lower triangular, no pivoting), $\mathbf t^U = \mathbf U^{-1}$ and $\mathbf t^L = \mathbf 1 - \mathbf L$.
- **Spins.** Do the α orbitals first, then the β ones.
- **Cost.** One full one-electron contraction in all.
- **RAS spaces.** To stay inside a RAS space, $\mathbf D$ must be block upper triangular in the RAS1/RAS2/RAS3 ordering. That is too restrictive for a general transformation, e.g. to natural orbitals.

!!! example "Sequential orbital transformation (computed for this note)"
    **Setup.** Full CI ground state of water/STO-3G, and a random orthogonal $\mathbf D = \exp(0.3(\mathbf A - \mathbf A^{\mathsf T}))$, decomposed by Doolittle LU.

    - **Method.** Fourteen one-orbital updates (7 α, 7 β).
    - **Result.** The vector has norm 1.000000000000. Its energy with integrals transformed to the new orbitals is −84.2008938756 $E_h$, identical to the original. It equals PySCF's `fci.addons.transform_ci` to $9\times10^{-16}$.

## Symmetry-broken CI

**The question (HJO Sec. 11.10).** The allyl radical has a symmetric ROHF solution and a slightly lower symmetry-broken one ([[rhf-instabilities-and-multiple-solutions]]). Truncated CI built on each differs.

**HJO's finding.** CISD potential curves along the antisymmetric stretch keep the HF pattern: one symmetric curve and two unsymmetric minima, though shallower. Surprisingly, the CISD based on the symmetric (restricted) orbitals lies below the one based on the broken orbitals.

**The cure.** Not higher excitations but an MCSCF treatment (Ch. 12).

!!! example "Allyl at δ = 0.2 bohr, Δ = 0 (computed for this note)"
    **Setup.** cc-pVDZ, all electrons, UCISD built on each ROHF solution.

    | Orbitals | ROHF energy | CISD energy |
    |---|---:|---:|
    | symmetric (C₂ᵥ) | −116.434555 | −116.835605 |
    | symmetry-broken | −116.435872 | −116.833537 |

    - **Agreement with HJO.** The broken solution is 1.32 m$E_h$ lower at the HF level, but its CISD is 2.07 m$E_h$ higher. This confirms HJO's observation.
    - **Absolute energies.** My CISD energies are about 5 m$E_h$ below the range plotted in HJO's Fig. 11.8 (−116.828 to −116.831). The cause is unknown; possible reasons are frozen orbitals or a spin-adapted versus spin-orbital CISD.

## Source

Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, Chichester, 2000), Secs. 11.6-11.10, pp. 550-574, Eqs. (11.6.1)-(11.9.25), Tables 11.5-11.8, Figs. 11.5-11.8. Checks computed for this note (NumPy, SciPy, PySCF 2.14; `hjo/c11/strings.py`, `model.py`, `allylci.py`). Table 11.8 and the RAS substring algorithm are described from HJO, not re-implemented.
