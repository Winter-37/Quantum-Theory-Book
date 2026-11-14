---
id: schmidt-decomposition-and-dmet-bath
title: Schmidt decomposition and the DMET bath - why a fragment of n orbitals needs at most n bath orbitals
summary: Any state of fragment plus environment has a Schmidt decomposition with at most dim(fragment) environment states. For a Slater determinant those states are a Fock space of bath orbitals, read off from the SVD of the environment-impurity block of the one-particle density matrix. Idempotency gives the singular values σ = [n(1−n)]^{1/2}, pairs each entangled impurity natural orbital with one bath orbital and one electron, and makes the embedding space hold an integer number of electrons. Verified on an H6 ring.
status: in-progress
kind: theory
level: advanced
tags: [DMET, embedding, schmidt-decomposition, bath-orbitals, SVD, idempotency, entanglement]
prerequisites: [slater-determinants, one-particle-rdm, natural-orbitals, basis-orthogonalization]
related: [dmet-embedding-hamiltonian, dmet-energy-functionals-and-chemical-potential, rhf]
order: 10
date: 2026-11-08
---

Notation: per-spin quantities throughout; the closed-shell density is $2\gamma$. Orbitals $i,j$ are orthonormal localized orbitals (LOs). A fragment (impurity) $I$ is a set of $n_I$ LOs; the other $n_E$ LOs are its environment $E$. Block indices $II$, $EI$, $EE$ refer to this split.

## Schmidt decomposition of a many-body state

**The statement.** Expand a state of the whole system in product states of fragment ($|A_i\rangle$, $N_A$ of them) and environment ($|B_j\rangle$, $N_B$ of them), $|\Psi\rangle = \sum_{ij}\Psi_{ij}|A_i\rangle|B_j\rangle$. The SVD $\Psi = U\Lambda V^\dagger$ gives

$$
|\Psi\rangle = \sum_{\alpha=1}^{\min(N_A,N_B)} \lambda_\alpha\, |\tilde A_\alpha\rangle|\tilde B_\alpha\rangle ,
\qquad
|\tilde A_\alpha\rangle = \sum_i U_{i\alpha}|A_i\rangle,\quad |\tilde B_\alpha\rangle = \sum_j V^*_{j\alpha}|B_j\rangle .
$$

- **Consequence.** However large the environment, at most $N_A$ environment states (the bath) are entangled with the fragment.
- **Exact embedding.** With $\hat P = \sum_{\alpha\beta}|\tilde A_\alpha\tilde B_\beta\rangle\langle\tilde A_\alpha\tilde B_\beta|$, the state $|\Psi\rangle$ is an eigenstate of $\hat P\hat H\hat P$, a problem of dimension $N_A^2$ instead of $N_AN_B$ (Wouters et al. 2016, Eqs. 1-2).
- **The catch.** Building $|\tilde B_\alpha\rangle$ needs $|\Psi\rangle$. DMET breaks the circle by taking the Schmidt decomposition of a mean-field determinant $|\Phi\rangle$ instead.

## Bath orbitals from a determinant

For a Slater determinant the Schmidt states of the environment are spanned by orbitals, not by general many-body states (Wouters et al. 2016, Sec. 2.1).

**Occupied-orbital picture.** Write the occupied orbitals as $C_{k\mu}$ ($k$ an LO, $\mu$ occupied). Take the SVD of the fragment rows, $C_{I\mu} = \sum_p U_{kp}\lambda_p V^\dagger_{p\mu}$. Rotating the occupied orbitals by $V$ (which leaves $|\Phi\rangle$ unchanged) gives at most $n_I$ occupied orbitals with weight on the fragment and $N_{\rm occ}-n_I$ orbitals with none. The environment parts of the first set, normalized, are the bath orbitals.

**Density-matrix picture (used in practice).** Let $\gamma = C_{\rm occ}C_{\rm occ}^{\mathsf T}$ in the LO basis, so $\gamma^2=\gamma$. Partition it as

$$
\gamma = \begin{pmatrix}\gamma_{II} & \gamma_{IE}\\ \gamma_{EI} & \gamma_{EE}\end{pmatrix},
\qquad
\gamma_{EI} = U\Sigma V^{\mathsf T}.
$$

The bath orbitals are the left singular vectors $U$ with nonzero singular values. Equivalently they are the eigenvectors of $\gamma_{EE}$ with eigenvalues strictly between 0 and 1 (Wouters et al. 2016, Sec. 2.2, via MacDonald's theorem).

## Why the SVD works: three identities

Expand the blocks of $\gamma^2=\gamma$:

$$
\gamma_{II}^2 + \gamma_{IE}\gamma_{EI} = \gamma_{II},
\qquad
\gamma_{EI}\gamma_{II} + \gamma_{EE}\gamma_{EI} = \gamma_{EI}.
$$

1. **Singular values.** The first identity gives $\gamma_{IE}\gamma_{EI} = \gamma_{II}(1-\gamma_{II})$. Its eigenvalues are $\sigma_k^2$, so

    $$
    \sigma_k = \sqrt{n_k(1-n_k)},
    $$

    where $n_k$ are the eigenvalues of $\gamma_{II}$, the occupations of the impurity natural orbitals.
2. **Bath occupations.** Choose $V$ as the eigenvectors of $\gamma_{II}$, $\gamma_{II}v_k=n_kv_k$, and $u_k = \gamma_{EI}v_k/\sigma_k$. The second identity gives $\gamma_{EE}u_k = (1-n_k)u_k$: bath orbital $k$ has occupation $1-n_k$.
3. **One electron per pair.** Impurity natural orbital $k$ and bath orbital $u_k$ together hold $n_k+(1-n_k)=1$ electron of each spin. An impurity orbital with $n_k\in\{0,1\}$ has $\sigma_k=0$ and is entangled with nothing.

**Four kinds of orbitals.** Impurity orbitals and bath orbitals form the embedding space, an active space of $n_I+n_{\rm bath}$ orbitals. The remaining environment orbitals are the eigenvectors of $\gamma_{EE}$ with eigenvalue 1 (the **core**: doubly occupied, unentangled) or 0 (external virtuals).

**Embedding electron count.** With every nonzero $\sigma_k$ kept, the per-spin count in the embedding space is

$$
N_{\rm emb} = \operatorname{tr}\big(C^{\mathsf T}\gamma C\big) = n_{\rm bath} + \#\{k: n_k = 1\},
\qquad
C = \begin{pmatrix}\mathbb 1_{I} & 0\\ 0 & U_{\rm bath}\end{pmatrix},
$$

an integer, and the embedded density $C^{\mathsf T}\gamma C$ is itself idempotent. The core density $D_{\rm core} = \gamma - C\gamma_{\rm emb}C^{\mathsf T}$ is idempotent too, with $C^{\mathsf T}D_{\rm core}=0$, so $|\Phi\rangle$ factorizes exactly into a core determinant times a determinant in the embedding space.

## Practical points

- **Mixing occupied and virtual.** The LOs must mix occupied and virtual character, otherwise nothing is entangled. Löwdin orbitals (closest orthonormal orbitals to the AOs) or IAOs are the usual choices (Wouters et al. 2016, Sec. 2.2).
- **Near-zero singular values.** With large basis sets, or with core orbitals of neighbouring atoms, some $\sigma_k$ approach 0. A threshold decides which bath orbitals to keep, and a bath orbital that switches in or out along a reaction path makes the energy discontinuous. Wouters et al. recommend one bath orbital per broken bond, or IAO-based fragments that keep entanglement in the valence space.
- **Tall versus wide block.** If $n_E<n_I$ the rank is at most $n_E$. When it reaches $n_E$, the embedding space covers every LO, and DMET returns the solver's result for the whole molecule.
- **SVD versus diagonalizing $\gamma_{EE}$.** Both give the same bath. $\gamma_{EE}$ has large exactly degenerate eigenspaces (eigenvalues 0 and 1), so the SVD of $\gamma_{EI}$ is the better-conditioned route when the bath must be differentiated (see [[dmet-analytic-nuclear-gradient]]).

## Worked example

!!! example "H$_6$ ring, STO-3G, two-atom fragment"
    Regular hexagon, nearest-neighbour distance 1.0 Å, RHF ($E = -3.157047\ E_h$), Löwdin LOs, fragment = atoms 0 and 1. Script: `dmet_mini.py` (PySCF 2.15).

    - **Idempotency.** $\max|\gamma^2-\gamma| = 4\times10^{-16}$, $\operatorname{tr}\gamma = 3$.
    - **Impurity natural occupations.** $n = (0.166667,\ 0.833333)$.
    - **Singular values.** $\sigma = (0.372678,\ 0.372678)$; $\sqrt{n(1-n)} = 0.372678$ for both, as the first identity requires. The two values are equal because $n_2 = 1-n_1$ here.
    - **Electron count.** Two bath orbitals and no $n_k=1$, so $N_{\rm emb}=2$ per spin, 4 electrons in 4 embedding orbitals. $2\operatorname{tr}\gamma_{\rm emb} = 4.000000000000002$, and $\gamma_{\rm emb}$ is idempotent to $4\times10^{-16}$.
    - **Factorization.** $\max|C^{\mathsf T}D_{\rm core}| = 3\times10^{-16}$.

## Source

- S. Wouters, C. A. Jiménez-Hoyos, Q. Sun, G. K.-L. Chan, "A practical guide to density matrix embedding theory in quantum chemistry", *J. Chem. Theory Comput.* **12**, 2706 (2016), doi:10.1021/acs.jctc.6b00316. Sections 2.1-2.2: Schmidt decomposition, bath orbitals, the four orbital classes.
- S. Wouters, C. A. Jiménez-Hoyos, G. K.-L. Chan, "Five years of density matrix embedding theory", Chapter 8 in *Fragmentation: Toward Accurate Calculations on Complex Molecular Systems*, ed. M. S. Gordon (Wiley, 2017). Same construction, Eqs. 8.1-8.11.
- G. Knizia, G. K.-L. Chan, *Phys. Rev. Lett.* **109**, 186404 (2012), doi:10.1103/PhysRevLett.109.186404: the original DMET (cited by Wouters et al. 2016; not read directly here).
- The three idempotency identities are written out here in my own derivation; the SVD form of the bath follows Li et al., *J. Chem. Phys.* **158**, 134105 (2023), Eqs. 1-2.
