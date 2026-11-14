---
id: genealogical-coupling
title: Spin of determinants and configuration state functions - counting CSFs and the genealogical coupling scheme
summary: Determinants are always S_z eigenfunctions but S² eigenfunctions only for closed shells and high-spin cases, because spin-orbital occupation operators do not commute with S². Orbital occupation operators do, so spin eigenfunctions (CSFs) are combinations of the determinants of one orbital configuration. For N open shells there are C(N, N/2−S) − C(N, N/2−S−1) CSFs of spin S, and S_high+1 determinants per singlet CSF. The genealogical scheme couples electrons one at a time; each determinant coefficient is a product of Clebsch-Gordan-type factors. HJO's three-electron example reproduced, and orthonormality, S² and counts checked for up to eight open shells.
status: in-progress
kind: derivation
level: intermediate
tags: [csf, spin-adaptation, genealogical-coupling, branching-diagram, spin-eigenfunctions, determinants, clebsch-gordan]
prerequisites: [spin-operators, spin-adapted-configurations, spin-tensor-operators]
related: [slater-determinants, full-ci, ci-in-practice, uhf, density-matrices-second-quantization]
order: 50
date: 2026-11-04
---

## Spin properties of determinants

**Exact states.** The nonrelativistic Hamiltonian is a singlet operator, so it commutes with $\hat S^2$ and $\hat S_z$, and exact states can be taken as spin eigenfunctions $|S, M\rangle$. Approximate wave functions should share this property.

**$\hat S_z$.** $\hat S_z = \tfrac12\sum_p(\hat N_{p\alpha} - \hat N_{p\beta})$ is a combination of spin-orbital occupation (ON) operators, which commute among themselves. Every determinant is therefore an $\hat S_z$ eigenfunction, with $M = \tfrac12(n_\alpha - n_\beta)$ counting the unpaired electrons.

**$\hat S^2$.** The ON operators do not commute with $\hat S_\pm$, so in general determinants are not $\hat S^2$ eigenfunctions. Writing a determinant as core string × alpha string × beta string (doubly occupied orbitals first) and applying $\hat S^2 = \hat S_-\hat S_+ + \hat S_z(\hat S_z + 1)$, the unwanted terms involve $[\hat S_-, \text{alpha string}]$ and $[\hat S_+, \text{beta string}]$, which flip two spins. They vanish in two cases:

- **closed shells**, where both open strings are empty: $S = 0$;
- **high spin**, where all unpaired spins are parallel: $S = |M| = n_{\text{open}}/2$.

(Detailed algebra: HJO Eqs. 2.4.13-2.4.39; see also [[spin-adapted-configurations]].)

## Configuration state functions

**Orbital configurations.** The orbital ON operators $\hat N_p = \hat N_{p\alpha} + \hat N_{p\beta}$ are singlet operators and commute with $\hat S^2$ and $\hat S_z$. Simultaneous eigenfunctions of all $\hat N_p$, $\hat S^2$ and $\hat S_z$ exist: these are the **configuration state functions** (CSFs). All determinants with the same orbital occupations (0, 1 or 2 per orbital) but different spin assignments of the singly occupied orbitals form an **orbital configuration**. $\hat S^2$ never couples determinants of different configurations, so CSFs are combinations within one configuration.

**Counting.** Let $N$ be the number of singly occupied orbitals.

- **Determinants with projection $M$:** $\binom{N}{N/2 - M}$; $2^N$ in total.
- **CSFs with spin $S$** (and any one $M$ with $|M|\le S$): subtract the number of determinants with projection $S + 1$ from those with projection $S$,

$$
N_{\text{CSF}}(N, S) = \binom{N}{N/2 - S} - \binom{N}{N/2 - S - 1},
$$

  with binomials of negative or half-integer arguments set to zero.
- **Singlets:** for $N = 2k$, $\binom{2k}{k}/N_{\text{CSF}} = k + 1 = S_{\text{high}} + 1$ determinants per CSF.

| Open shells $N$ | 2 | 4 | 6 | 8 | 10 | 12 |
|---|---:|---:|---:|---:|---:|---:|
| Determinants, $M = 0$ | 2 | 6 | 20 | 70 | 252 | 924 |
| Singlet CSFs | 1 | 2 | 5 | 14 | 42 | 132 |

**Trade-off.** Determinants are simpler and give longer expansions that may break spin symmetry. CSFs are combinations of determinants but impose the correct spin and are shorter.

## The genealogical coupling scheme

**Idea.** Couple the open-shell electrons one at a time. The first gives a doublet; adding the second gives a singlet or a triplet; adding the third to these gives two doublets and one quartet; and so on. The core (doubly occupied orbitals) is a singlet and is ignored.

**Labels.**

- **CSF:** a path $\mathbf T = (T_1, \ldots, T_N)$ of intermediate total spins ($T_N = S$), or equivalently the sequence of steps $\pm$. Example: the three-electron doublets are $|\tfrac12, 1, \tfrac12\rangle^{\mathrm c} = |{+}{+}{-}\rangle^{\mathrm c}$ and $|\tfrac12, 0, \tfrac12\rangle^{\mathrm c} = |{+}{-}{+}\rangle^{\mathrm c}$.
- **Determinant:** a path $\mathbf P = (P_1, \ldots, P_N)$ of intermediate spin projections, or the individual projections $\pm\tfrac12$.

The **branching diagram** draws all paths in the $(N, S)$ plane. The number of paths ending at $(N, S)$ equals $N_{\text{CSF}}(N, S)$ above.

**Recursion.** Write the CSF as a spin tensor operator $\hat O_N^{S,M}(\mathbf t)$ acting on the closed-shell core. Each step adds one creator to an $(N-1)$-electron tensor operator:

$$
\hat O_N^{S,M}(\mathbf t) = \sum_{\sigma=\pm1/2}C_{t_N,\sigma}^{S,M}\,a_{N\sigma}^\dagger\,\hat O_{N-1}^{S - t_N,\,M - \sigma}(\mathbf t),
$$

where $t_N = T_N - T_{N-1} = \pm\tfrac12$. The coupling coefficients are Clebsch-Gordan coefficients for coupling spin $S - t_N$ with $\tfrac12$ (HJO Eqs. 2.6.5-2.6.6):

$$
C_{1/2,\sigma}^{S,M} = \sqrt{\frac{S + 2\sigma M}{2S}},\qquad
C_{-1/2,\sigma}^{S,M} = -2\sigma\sqrt{\frac{S + 1 - 2\sigma M}{2(S + 1)}} .
$$

They do not depend on the number of electrons.

**Coefficient of a determinant.** Projecting onto a determinant, the creator $a_{N\sigma}^\dagger$ must match spin orbital $N$ of the determinant, which fixes $\sigma = p_N$. Repeating $N$ times gives (HJO Eq. 2.6.10)

$$
{}^{\mathrm d}\langle\mathbf p|\mathbf t\rangle^{\mathrm c} = \prod_{n=1}^NC_{t_n,p_n}^{T_n,P_n},
$$

with the rule that the coefficient vanishes unless $|P_n|\le T_n$ at every step.

!!! example "Three electrons in three orbitals, $M = \tfrac12$ (HJO Sec. 2.6.4; computed for this note)"
    Determinants with $M = \tfrac12$: $|{+}{+}{-}\rangle$, $|{+}{-}{+}\rangle$, $|{-}{+}{+}\rangle$.

    | CSF | $|{+}{+}{-}\rangle$ | $|{+}{-}{+}\rangle$ | $|{-}{+}{+}\rangle$ |
    |---|---:|---:|---:|
    | Doublet $|\tfrac12, 1, \tfrac12\rangle^{\mathrm c}$ | $\sqrt{2/3} = 0.816497$ | $-1/\sqrt6 = -0.408248$ | $-1/\sqrt6 = -0.408248$ |
    | Doublet $|\tfrac12, 0, \tfrac12\rangle^{\mathrm c}$ | 0 | $1/\sqrt2 = 0.707107$ | $-1/\sqrt2 = -0.707107$ |
    | Quartet $|\tfrac12, 1, \tfrac32\rangle^{\mathrm c}$, $M = \tfrac32$ | $|{+}{+}{+}\rangle$: 1 | | |

    - **First doublet.** For example, $\langle{+}{+}{-}|\tfrac12,1,\tfrac12\rangle = C_{1/2,1/2}^{1/2,1/2}C_{1/2,1/2}^{1,1}C_{-1/2,-1/2}^{1/2,1/2} = 1\times1\times\sqrt{2/3}$.
    - **Second doublet.** $|{+}{+}{-}\rangle$ cannot contribute: after two electrons the projection 1 would exceed the intermediate spin 0.
    - **Agreement.** Both doublets agree with HJO Eqs. (2.6.14)-(2.6.15).

**Completeness and orthonormality.** The genealogical CSFs of a configuration form a complete orthonormal set: their number equals $N_{\text{CSF}}$, and orthonormality follows by induction on $N$ (HJO Sec. 2.6.5).

!!! example "Genealogical CSFs for up to eight open shells (computed for this note)"
    For every $N\le8$ and every allowed $S$, I built all genealogical CSFs from the product formula (with $M = S$) and checked them against explicit $\hat S^2$ and $\hat S_z$ matrices on the $2^N$ spin strings.

    - **Counts** equal $N_{\text{CSF}}(N, S)$ in every case, e.g. 14, 28, 20, 7, 1 for $N = 8$ and $S = 0, \ldots, 4$.
    - **Orthonormality** holds to $2\times10^{-15}$.
    - **Spin.** $\hat S^2\Psi = S(S+1)\Psi$ and $\hat S_z\Psi = S\Psi$ to $4\times10^{-15}$.

**In practice (general knowledge).** CSF-based CI codes evaluate Hamiltonian matrix elements through coupling coefficients of the operators $E_{pq}$ between CSFs. Determinant-based direct CI instead works with alpha and beta strings and imposes spin symmetry afterwards ([[ci-in-practice]]).

## Source

Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, Chichester, 2000), Secs. 2.4-2.6, pp. 46-61, Eqs. (2.4.1)-(2.6.16), Fig. 2.1. The coupling coefficients and the three-electron expansions were read from the page images. All numbers computed for this note.
