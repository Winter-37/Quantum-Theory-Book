---
id: eom-ccsd-and-size-extensivity
title: Equation-of-motion coupled cluster (EOM-CC) - excited states as a biorthogonal CI with the similarity-transformed Hamiltonian, excitation energies as eigenvalues of the CC Jacobian, and which EOM energies are size-extensive
summary: EOM-CC expands excited states as Σ c_μ exp(T̂)τ̂_μ|HF⟩, with bra states ⟨HF|τ̂†_μ exp(−T̂) forming a biorthonormal set. This turns the problem into CI with the non-Hermitian H̄ = e^{−T}He^{T}. For an optimized ground state the first column of H̄ − E₀ vanishes, so excitation energies are the eigenvalues of the CC Jacobian. The ground-state left eigenvector is the Λ state of the CC Lagrangian. For noninteracting A + B the Jacobian is block diagonal: local excitations are exact sums, while simultaneous excitations A*B* are not size-extensive in a truncated model. Demonstrated for two H₂ molecules 100 bohr apart in cc-pVDZ. Local EOM-CCSD excitation energies equal the monomer values (and FCI) to 10⁻⁶. The triplet-triplet pair state, exactly 0.784814 E_h in FCI, comes out at 0.809416 in EOM-CCSD.
status: in-progress
kind: theory
level: advanced
tags: [eom-cc, eom-ccsd, excited-states, coupled-cluster-jacobian, biorthogonal, similarity-transformed-hamiltonian, size-extensivity, size-intensivity]
prerequisites: [coupled-cluster-optimization-and-lagrangian, coupled-cluster-hierarchy-and-size-extensivity]
related: [ci-size-extensivity-and-excitation-levels, closed-shell-ccsd-t1-transformation, ci-optimization-newton-and-davidson]
order: 60
date: 2026-11-04
---

## The model

**Why not separate CC calculations (HJO Sec. 13.6.1).**

- **References.** A good reference determinant for an excited state is often impossible to find.
- **Cost.** Each state costs a full CC calculation.
- **Orthogonality.** The resulting states are not orthogonal.

**EOM-CC instead.** Use a linear, CI-like expansion that contains the CC ground state as one term:

$$
|c\rangle = \sum_\mu c_\mu e^{\hat T}\hat\tau_\mu|\text{HF}\rangle,\qquad \hat\tau_0 = 1 .
$$

- **Division of labor.** The exponential carries the correlation common to all states; the linear coefficients describe how the state differs from the ground state.
- **Character of a state.** States are called singly or doubly dominated according to their leading coefficients.
- **Imperfection.** $\hat T$ is optimal only for the ground state, so the coefficients also absorb some excited-state correlation.

## The eigenvalue problem

**Biorthogonal basis (HJO Sec. 13.6.2).** Kets $|\bar\mu\rangle = e^{\hat T}|\mu\rangle$ and bras $\langle\bar\mu| = \langle\mu|e^{-\hat T}$ satisfy $\langle\bar\mu|\bar\nu\rangle = \delta_{\mu\nu}$. Making the pseudo-expectation value

$$
E(\bar c, c) = \frac{\langle\bar c|\hat H|c\rangle}{\langle\bar c|c\rangle} = \frac{\langle\bar c|e^{-\hat T}\hat He^{\hat T}|c\rangle}{\langle\bar c|c\rangle}
$$

stationary gives right and left eigenproblems $\bar{\mathbf H}\mathbf c = E\mathbf c$ and $\bar{\mathbf c}^{\mathsf T}\bar{\mathbf H} = E\bar{\mathbf c}^{\mathsf T}$. The matrix elements are $\bar H_{\mu\nu} = \langle\mu|e^{-\hat T}\hat He^{\hat T}|\nu\rangle$.

- **What it is.** CI with a similarity-transformed, non-Hermitian Hamiltonian.
- **No variational bound.** The eigenvalues are not upper bounds and could in principle be complex. They are real for any reasonable ground state.
- **Full limit.** A complete expansion recovers FCI.

**Structure (HJO Secs. 13.6.3-13.6.4).** For an optimized ground state, the first column of $\bar{\mathbf H}$ is $(E_0, \mathbf 0)$, because it holds the CC equations. With a resolution of the identity in a manifold closed under de-excitation,

$$
\bar{\mathbf H} - E_0\mathbf 1 = \begin{pmatrix}0 & \boldsymbol\eta^{\mathsf T}\\ \mathbf 0 & \mathbf A\end{pmatrix},\qquad \eta_\nu = \langle\text{HF}|[\hat H,\hat\tau_\nu]e^{\hat T}|\text{HF}\rangle .
$$

Here $\mathbf A$ is the CC Jacobian.

- **Ground state.** Its right eigenvector is $(1, \mathbf 0)$. Its left eigenvector $(1, \bar{\mathbf t})$ satisfies $\boldsymbol\eta^{\mathsf T} + \bar{\mathbf t}^{\mathsf T}\mathbf A = 0$, which are precisely the Λ equations of [[coupled-cluster-optimization-and-lagrangian]]. The CC Lagrangian *is* the EOM-CC ground-state expectation value.
- **Excited states.** The excitation energies are the eigenvalues of $\mathbf A$: $\mathbf A\mathbf t_K = \Delta E_K\mathbf t_K$. The reference coefficient is $s_K = \boldsymbol\eta^{\mathsf T}\mathbf t_K/\Delta E_K$.
- **Where it fails.** In models whose first column does not vanish, such as QCISD, EOM-CC cannot be applied. Response theory still can be.

## Size-extensivity of the excitation energies

**Block structure (HJO Sec. 13.6.5).** For noninteracting A and B, in a basis of A-only, B-only and mixed (AB) excitations, the Jacobian is block diagonal:

$$
\mathbf A = \begin{pmatrix}\mathbf A_{A,A} & 0 & 0\\ 0 & \mathbf A_{B,B} & 0\\ 0 & 0 & \mathbf A_{AB,AB}\end{pmatrix}.
$$

- **Local excitations.** The eigenvalues of $\mathbf A_{A,A}$ and $\mathbf A_{B,B}$ are exactly those of the separate systems. These excited-state energies are size-extensive, and the excitation energies size-intensive.
- **Simultaneous excitations.** $\mathbf A_{AB,AB}$ is a direct sum $\omega_A + \omega_B$ only in the full expansion. In a truncated EOM-CC model it is not, so those states are *not* size-extensive.
- **Consequences.** These states mix with local ones wherever they are nearly degenerate. In large systems they can contaminate even low-lying excitations.
- **Contrast with CI.** Truncated CI is not size-extensive even for the ground state ([[ci-size-extensivity-and-excitation-levels]]). EOM-CC shows that a well-chosen *linear* basis can give size-extensive energies.

!!! example "Two H₂ molecules (1.4 bohr, cc-pVDZ) 100 bohr apart: EOM-CCSD versus exact FCI ($E_h$; computed for this note)"
    **Setup.** For one H₂ (two electrons), CCSD and EOM-CCSD are exact. The dimer FCI has 36 100 determinants and was solved with PySCF's Davidson solver for 32 roots.

    | Excitation | Monomer (EOM = FCI) | Dimer FCI | Dimer EOM-CCSD |
    |---|---:|---:|---:|
    | local $^3\Sigma_u^+$ | 0.392407 | 0.392407 (×2) | 0.392407 (×2) |
    | local $^1\Sigma_u^+$ | 0.511369 | 0.511367, 0.511370 | 0.511367, 0.511370 |
    | local, next triplet | 0.646205 | 0.646205 (×2) | 0.646205 (×2) |
    | local, next singlet | 0.786275 | 0.786275 (×2) | 0.786275 (×2) |
    | ³A* ³B*, singlet/triplet/quintet coupled | $2\times0.392407$ | **0.784813** (×3) | **0.809416** (singlet and triplet) |
    | ¹A* ³B* | 0.903776 | **0.903775** | **0.955974** |

    - **Local states.** Every local excitation is reproduced to $10^{-6}$; the tiny splitting 0.511367/0.511370 is the residual coupling at 100 bohr.
    - **Simultaneous excitations.** The double-excitation states are $+24.6$ and $+52.2$ m$E_h$ too high. To describe "one correlated excitation on each molecule" CCSD would need excitation operators up to quadruples in $\mathbf A_{AB,AB}$.
    - **Charge-transfer states.** Both spectra also contain H₂⁺···H₂⁻ states (FCI 0.775642, EOM 0.776343). They are not products of monomer states.
    - **Minimal-basis contrast.** In STO-3G every monomer excited state is a single uncorrelated configuration, so EOM-CCSD is exact even for the pair states. A real test needs a basis in which the excited monomer is correlated.

**Response theory (HJO Sec. 13.6.6).** For standard CC models, the CC linear-response function gives the same excitation energies as EOM-CC. Its properties (for example polarizabilities) differ, and only the response ones are size-extensive. Response theory also covers QCISD and the CC2 and CC3 hierarchy (HJO Ch. 14).

## Source

Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, Chichester, 2000), Sec. 13.6, pp. 677-685, Eqs. (13.6.1)-(13.6.48). Recomputed for this note with PySCF 2.14 (`eom_rccsd` singlet and triplet, `fci.direct_spin1`) in `hjo/c13/eomsep3.py`; minimal-basis contrast in `eomsep2.py`.
