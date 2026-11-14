---
id: ghf
title: Generalized Hartree-Fock - two-component spinor orbitals, the spinor Fock matrix, charge and magnetization densities, and the non-collinear 120° solution of equilateral H₃
summary: GHF lets every occupied orbital be a two-component spinor ψ^α α + ψ^β β, so the determinant is no longer an eigenfunction of Ŝ² or Ŝ_z and has no common spin axis. In a K-function AO basis the coefficient matrix is 2K × N. The Roothaan-Hall problem becomes F C = S C ε in a 2K space. In the Fock matrix the diagonal blocks are the familiar UHF ones, and the off-diagonal blocks −K[P^αβ] are the only new terms; they let the spin direction rotate. The spinor density splits into a charge part and three magnetization matrices (M_x, M_y, M_z). A determinant is collinear exactly when the 3 × 3 Gram matrix of the magnetizations has rank 1. Because the variational spaces are nested, the global minima satisfy E_GHF ≤ E_UHF ≤ E_RHF, but that says nothing about individual stationary points. Checked for equilateral H₃/STO-3G (doublet). The GHF Fock matrix and energy formulas reproduce PySCF to 10⁻¹⁶. A coplanar 120° spin arrangement lies up to 6.75 mE_h below the stable UHF solution (side 1.5 Å). The UHF solution is itself a local minimum in GHF space, so the GHF state is a separate, lower minimum, not an instability of UHF.
status: in-progress
kind: theory
level: advanced
tags: [hartree-fock, ghf, spin-symmetry-breaking, non-collinear, spinors, symmetry-breaking, h3]
prerequisites: [uhf, rhf, spin-operators]
related: [hf-solution-classification, rhf-instabilities-and-multiple-solutions, scf-second-order-and-stability, h2-dissociation-rhf-uhf, hartree-fock-equations]
order: 120
date: 2026-11-07
---

## The ansatz

**Notation.** $K$ spatial AOs $\phi_\mu$ (real), $N$ electrons, spin functions $\alpha(\omega)$ and $\beta(\omega)$, and $\mathbf x = (\mathbf r,\omega)$. Atomic units throughout.

The three Hartree-Fock families differ only in how much freedom each occupied spin orbital has:

| Ansatz | Occupied orbital $\chi_i(\mathbf x)$ | Good quantum numbers of the determinant |
|---|---|---|
| RHF (closed shell) | $\psi_i(\mathbf r)\alpha$ and $\psi_i(\mathbf r)\beta$, same $\psi_i$ | $\hat S^2$, $\hat S_z$ |
| UHF | $\psi_i^\alpha(\mathbf r)\alpha$ or $\psi_i^\beta(\mathbf r)\beta$ | $\hat S_z$ |
| GHF | $\psi_i^\alpha(\mathbf r)\alpha(\omega) + \psi_i^\beta(\mathbf r)\beta(\omega)$ | none in general |

A GHF orbital is a **two-component spinor**. Both components use the same spatial basis,

$$
\psi_i^\sigma(\mathbf r) = \sum_{\mu=1}^K C^\sigma_{\mu i}\phi_\mu(\mathbf r),\qquad
\mathbf C = \begin{pmatrix}\mathbf C^\alpha\\ \mathbf C^\beta\end{pmatrix}\in\mathbb C^{2K\times N}.
$$

**What changes.**

- The number of electrons of each spin is no longer fixed, so $N^\alpha$ and $N^\beta$ are not separately defined.
- No single spin-quantization axis is shared by all orbitals.
- RHF and UHF are the special cases in which every column of $\mathbf C$ has a zero $\beta$ block or a zero $\alpha$ block.
- A **global** spin rotation of a UHF determinant gives a GHF-looking coefficient matrix that is physically the same collinear state. The collinearity test below separates the two.

## Density matrix, charge and magnetization

**Spinor density matrix.** With $P^{\sigma\sigma'}_{\mu\nu} = \sum_{i=1}^N C^\sigma_{\mu i}C^{\sigma'*}_{\nu i}$,

$$
\mathbf P = \begin{pmatrix}\mathbf P^{\alpha\alpha} & \mathbf P^{\alpha\beta}\\ \mathbf P^{\beta\alpha} & \mathbf P^{\beta\beta}\end{pmatrix}.
$$

The off-diagonal blocks measure the coherence between the $\alpha$ and $\beta$ components of the same orbitals. They vanish for a UHF determinant written in its own spin axis.

**Charge and magnetization blocks** (Loos Eqs. 3.42-3.44):

$$
\mathbf P_{\!c} = \tfrac12(\mathbf P^{\alpha\alpha}+\mathbf P^{\beta\beta}),\quad
\mathbf M_z = \tfrac12(\mathbf P^{\alpha\alpha}-\mathbf P^{\beta\beta}),\quad
\mathbf M_x = \tfrac12(\mathbf P^{\beta\alpha}+\mathbf P^{\alpha\beta}),\quad
\mathbf M_y = \tfrac1{2i}(\mathbf P^{\beta\alpha}-\mathbf P^{\alpha\beta}),
$$

so that

$$
\mathbf P = \mathbb 1_{\text{spin}}\otimes\mathbf P_{\!c} + \sum_{k=x,y,z}\boldsymbol\sigma_k\otimes\mathbf M_k ,
$$

with $\boldsymbol\sigma_k$ the Pauli matrices. Here $\mathbf P_{\!c}$ is *half* the total charge-density matrix. The real-space spin density is $m_k(\mathbf r) = \sum_{\mu\nu}(\mathbf M_k)_{\mu\nu}\phi_\mu(\mathbf r)\phi_\nu(\mathbf r)$ (expectation of $\hat s_k$ density with $\hat s_k = \tfrac12\boldsymbol\sigma_k$). For real AOs only the symmetric part of each $\mathbf M_k$ contributes to $m_k(\mathbf r)$.

!!! warning "Index order of the density"
    With $P_{\lambda\sigma} = \sum_i C_{\lambda i}C^*_{\sigma i}$, complex orbitals make $\mathbf P^{\alpha\beta}$ and $\mathbf P^{\beta\alpha}$ different matrices, and the exchange contraction below must use them exactly as written. Swapping $\lambda$ and $\sigma$ in the integral without also transposing the density is wrong for complex orbitals.

## The GHF Roothaan-Hall equations

**Metric.** The spinor overlap is block diagonal, $\mathbf S_2 = \mathrm{diag}(\mathbf S,\mathbf S)$, and the orbitals satisfy $\mathbf C^\dagger\mathbf S_2\mathbf C = \mathbb 1$.

**Fock matrix** (Loos Eq. 3.49). With chemists' integrals $(\mu\nu|\lambda\sigma)$ and

$$
J_{\mu\nu}[\mathbf D] = \sum_{\lambda\sigma}D_{\lambda\sigma}(\mu\nu|\lambda\sigma),\qquad
K_{\mu\nu}[\mathbf D] = \sum_{\lambda\sigma}D_{\lambda\sigma}(\mu\lambda|\sigma\nu),
$$

$$
\mathbf F = \begin{pmatrix}
\mathbf H + \mathbf J[\mathbf P^{\alpha\alpha}] + \mathbf J[\mathbf P^{\beta\beta}] - \mathbf K[\mathbf P^{\alpha\alpha}] & -\mathbf K[\mathbf P^{\alpha\beta}]\\
-\mathbf K[\mathbf P^{\beta\alpha}] & \mathbf H + \mathbf J[\mathbf P^{\alpha\alpha}] + \mathbf J[\mathbf P^{\beta\beta}] - \mathbf K[\mathbf P^{\beta\beta}]
\end{pmatrix}.
$$

- **Coulomb.** The Coulomb potential depends only on the total charge, so it appears identically in both diagonal blocks.
- **Exchange.** It acts only between components of equal spin label, so $\alpha\beta$ density produces an $\alpha\beta$ exchange block.
- **The new physics.** The off-diagonal blocks $-\mathbf K[\mathbf P^{\alpha\beta}]$ are the only terms absent from UHF. They let each orbital tilt its spin away from the common axis.

**Equations to solve.**

$$
\mathbf F\mathbf C = \mathbf S_2\mathbf C\boldsymbol\varepsilon,\qquad
E_{\text{GHF}} = \tfrac12\mathrm{Tr}\big[(\mathbf H_2 + \mathbf F)\mathbf P\big] + V_{nn},\qquad \mathbf H_2 = \mathrm{diag}(\mathbf H,\mathbf H).
$$

**SCF cycle.** Build all four density blocks, then all four Fock blocks. Solve the $2K\times2K$ generalized eigenproblem and occupy the $N$ lowest spinors. Repeat to self-consistency.

**Cost.** Each iteration needs four Coulomb-type and four exchange-type contractions with the same integrals, plus diagonalization of a $2K$ matrix. That is a constant factor over UHF, with no change in scaling.

## Variational hierarchy and what it does not say

**Nested spaces.** For the global minima in one basis,

$$
\{\Phi_{\text{RHF}}\}\subset\{\Phi_{\text{UHF}}\}\subset\{\Phi_{\text{GHF}}\}\ \Longrightarrow\ E^{\min}_{\text{GHF}}\le E^{\min}_{\text{UHF}}\le E^{\min}_{\text{RHF}} .
$$

**Limits of the inequality.**

- It compares minima only. A converged GHF solution need not lie below every UHF or RHF stationary point.
- Whether a given solution is a local minimum is decided by the orbital Hessian in the larger space ([[scf-second-order-and-stability]], [[rhf-instabilities-and-multiple-solutions]]).
- A negative eigenvalue in the UHF→GHF block (rotations that mix $\alpha$ and $\beta$) means a lower GHF solution lies downhill.
- A lower GHF solution can also exist when the UHF point is a local minimum in GHF space. The H₃ example below is such a case.

**Symmetry.**

- UHF may break $\hat S^2$.
- GHF may also break $\hat S_z$.
- Complex GHF can in addition break time reversal; [[hf-solution-classification]] sorts all eight possibilities.
- None of this adds correlation. GHF is still one determinant, and its energy lowering comes from trading spin symmetry for a better mean field.

## Collinearity test

**Criterion.** A determinant is *collinear* if one global spin rotation brings it to UHF form, i.e. if there is a unit vector $\mathbf n$ with $\mathbf M_k = n_k\mathbf M$ for all $k$. Then the real symmetric Gram matrix

$$
G_{kl} = \mathrm{Tr}\big(\mathbf M_k^{\text{sym}}\,\mathbf S\,\mathbf M_l^{\text{sym}}\,\mathbf S\big),\qquad k,l\in\{x,y,z\},
$$

equals $\mathbf n\mathbf n^{\mathsf T}\,\mathrm{Tr}(\mathbf M\mathbf S\mathbf M\mathbf S)$ and has rank 1.

**Interpretation.**

- **Rank 2.** The spin density is coplanar but non-collinear.
- **Rank 3.** It is non-coplanar.
- **Tilted axis alone.** A tilted spin axis is not evidence of non-collinearity: a globally rotated UHF determinant still gives rank 1.

!!! example "Equilateral H₃, STO-3G, doublet: ROHF, UHF and non-collinear GHF (computed for this note)"
    **Setup.** Three H atoms on an equilateral triangle with side $R$, one 1s function each, $N = 3$.

    - **UHF.** It is followed through its own stability analysis to a stable solution. That solution breaks the $D_{3h}$ symmetry (two parallel spins and one antiparallel spin).
    - **GHF.** It is started from three localized 1s spinors whose spins point at 0°, 120° and 240° in the $xz$ plane (real coefficients).

    | $R$ (Å) | $E_{\text{ROHF}}$ | $E_{\text{UHF}}$ | $\langle S^2\rangle_{\text{UHF}}$ | $E_{\text{GHF}}$ | $E_{\text{GHF}}-E_{\text{UHF}}$ (m$E_h$) | $\langle S^2\rangle_{\text{GHF}}$ | Gram eigenvalues (GHF) |
    |---:|---:|---:|---:|---:|---:|---:|---|
    | 0.8 | −1.204330 | −1.212055 | 0.779 | −1.214351 | −2.295 | 0.785 | 0, 0.137, 0.137 |
    | 1.0 | −1.328176 | −1.335980 | 0.838 | −1.340440 | −4.460 | 0.841 | 0, 0.155, 0.155 |
    | 1.5 | −1.332014 | −1.391833 | 1.343 | −1.398580 | −6.747 | 1.192 | 0, 0.272, 0.272 |
    | 2.0 | −1.209204 | −1.397910 | 1.658 | −1.400272 | −2.362 | 1.425 | 0, 0.350, 0.350 |
    | 2.5 | −1.168738 | −1.399517 | 1.733 | −1.400021 | −0.504 | 1.486 | 0, 0.370, 0.370 |
    | 3.0 | −1.122628 | −1.399753 | 1.747 | −1.399837 | −0.084 | 1.498 | 0, 0.374, 0.374 |

    Energies in $E_h$, including nuclear repulsion.

    **Detail at $R = 1.5$ Å.**

    - **Fock matrix and energy.** The blocked Fock matrix above reproduces PySCF's GHF Fock matrix to $3\times10^{-16}$. $\tfrac12\mathrm{Tr}[(\mathbf H_2+\mathbf F)\mathbf P]+V_{nn}$ equals the SCF energy exactly.
    - **Local moments.** Mulliken-partitioned spin moments are $(0,0,0.439)$, $(0.380,0,-0.219)$ and $(-0.380,0,-0.219)$. All have length 0.439, are 120° apart, and sum to zero: the classic frustrated triangle.
    - **Gram test.** The Gram matrix has rank 2 (coplanar, non-collinear), while the UHF determinant embedded in GHF form gives rank 1 (eigenvalues 0, 0, 0.546).
    - **Spatial symmetry.** The occupied GHF spinor energies are $-0.5279$ (twice) and $-0.3084$. The pair degeneracy is consistent with the 120° state keeping the triangle's symmetry when each spatial rotation is combined with a matching spin rotation, which UHF cannot do (my interpretation, not checked group-theoretically).

    **What the numbers say.**

    - **Ordering.** $E_{\text{GHF}}<E_{\text{UHF}}<E_{\text{ROHF}}$ at every $R$ studied.
    - **Energy gain.** The GHF lowering peaks near $R=1.5$ Å and goes to zero at dissociation. There all three spins are localized, $|\mathbf m_A|\to\tfrac12$, and the 120° and up-down-up arrangements become degenerate.
    - **Spin contamination.** It is not a figure of merit. $\langle S^2\rangle$ of the GHF determinant (1.19 at 1.5 Å) is *smaller* than that of UHF (1.34), yet GHF is not an $\hat S_z$ eigenfunction: $\langle S_z\rangle=0$ with variance 0.32 ([[hf-solution-classification]]).
    - **Two separate minima.** The real-GHF stability analysis of the UHF determinant finds no negative eigenvalue (lowest 0.596). The UHF state is a local minimum in GHF space, and the non-collinear state is a separate, lower minimum. It is found from a non-collinear guess, not by following an instability. Eight GHF runs per geometry started from the UHF density plus random real perturbations (amplitude 0.1) all fell back to UHF.

## Practical points

- **Guesses.** GHF has many stationary points. Guesses built from the expected spin texture, and a stability analysis afterwards, matter more than for UHF.
- **Diagnostics.** Report $\langle S^2\rangle$, $\langle S_z\rangle$, the Gram rank and the local moments, not just the energy.
- **Particle number.** GHF is the most general Hartree-Fock determinant that conserves particle number. Breaking particle-number symmetry as well leads to Hartree-Fock-Bogoliubov theory (Loos Sec. 3.3, refs. [48, 49] there).
- **Spin-orbit coupling.** Two-component relativistic Hamiltonians need the GHF structure anyway, because $\hat S_z$ is not conserved there. That use is outside this note.

## Source

P.-F. Loos, *Many Electrons, One Determinant: Hartree-Fock Theory, Basis Sets, and Molecular Integrals*, ESQC 2026 lecture chapter (course notes; edition/publication details to add), Sec. 3.3, pp. 99-102, Eqs. (3.38)-(3.51), Fig. 18. The stability references cited there are D. J. Thouless, *Nucl. Phys.* **21**, 225 (1960) and R. Seeger and J. A. Pople, *J. Chem. Phys.* **66**, 3045 (1977).

The collinearity criterion via the Gram matrix of the magnetization blocks is my own formulation of Loos's "single global spin axis" test. Numbers recomputed with PySCF 2.15 (`esqc/ghf/ghf_h3.py`).
