---
id: hf-solution-classification
title: Classification of Hartree-Fock solutions - the eight Fukutome / Stuber-Paldus classes by retained Ŝ², Ŝ_z, complex conjugation and time reversal
summary: Hartree-Fock determinants can be sorted by which of four symmetries they keep. Two are spin symmetries (Ŝ² and Ŝ_z). The other two are antiunitary: complex conjugation K̂ (real orbitals) and time reversal Θ̂ (Kramers-paired orbitals). The combinations allowed by the RHF, UHF and GHF coefficient structures give eight classes: real/complex RHF, real/paired/complex UHF and real/paired/complex GHF, with Fukutome's names TICS, CCW, ASDW, ASCW, ASW, TSDW, TSCW and TSW. Releasing one constraint at a time links them by eleven arrows. Lower energies can lie in larger classes, but a solution's class must be read off the solution, not inferred from the method used. The ⟨S_z⟩ variance Σ_ia |⟨a|ŝ_z|i⟩|² is a one-line test for broken Ŝ_z. Checked on equilateral H₃/STO-3G: the UHF solution is an ASDW (real UHF, Var S_z = 0) and the 120° GHF solution is a TSDW (real GHF, ⟨S_z⟩ = 0, Var S_z = 0.324). No complex GHF solution below it was found from six complex starting points.
status: in-progress
kind: reference
level: advanced
tags: [hartree-fock, ghf, symmetry-breaking, stability, time-reversal, complex-orbitals, classification]
prerequisites: [ghf, uhf]
related: [rhf-instabilities-and-multiple-solutions, scf-second-order-and-stability, h2-dissociation-rhf-uhf, exact-wave-function-properties-and-symmetry]
also: []
date: 2026-11-07
---

## The four symmetries

**Which symmetries.** Write the occupied spinors as columns of $\mathbf C = \begin{pmatrix}\mathbf C^{\alpha}\\ \mathbf C^{\beta}\end{pmatrix}$ ([[ghf]]). Four symmetries of the exact nonrelativistic Hamiltonian can be kept or broken by a single determinant:

| Symmetry | Operator | Kept when |
|---|---|---|
| Total spin | $\hat S^2$ | $\alpha$ and $\beta$ electrons occupy the same spatial orbitals (closed shell) |
| Spin projection | $\hat S_z$ | every orbital is purely $\alpha$ or purely $\beta$ |
| Complex conjugation | $\hat K$ | $\mathbf C$ can be chosen real |
| Time reversal | $\hat\Theta = -i\boldsymbol\sigma_y\hat K$ | the occupied set is closed under $\chi\mapsto\hat\Theta\chi$ (Kramers pairs) |

**How the antiunitary ones act.**

- **$\hat K$.** It conjugates the spatial parts and leaves the spin labels unchanged.
- **$\hat\Theta$ on one spinor.** It maps $\psi^\alpha\alpha+\psi^\beta\beta$ to $-\psi^{\beta*}\alpha+\psi^{\alpha*}\beta$, up to a phase convention.
- **Consequence.** A $\hat\Theta$-invariant determinant has its spinors in pairs $(\chi,\hat\Theta\chi)$. This is the "paired" structure in the table below.

$\hat K$ is not the exchange operator here.

## The eight classes

Constraints on $\mathbf C$ and the symmetries each class retains (Loos Table 2, after Henderson, Jiménez-Hoyos and Scuseria, Table I). $\sigma'$ is the spin opposite to $\sigma$.

| Family | Stuber-Paldus name | Fukutome name | Symmetries kept | Structure of $\mathbf C$ |
|---|---|---|---|---|
| RHF | real RHF | TICS | $\hat S^2,\hat S_z,\hat K,\hat\Theta$ | $\begin{pmatrix}\mathbf C_{\sigma\sigma}&0\\0&\mathbf C_{\sigma\sigma}\end{pmatrix}$, real |
| RHF | complex RHF | CCW | $\hat S^2,\hat S_z$ | same blocks, complex |
| UHF | paired UHF | ASCW | $\hat S_z,\hat\Theta$ | $\begin{pmatrix}\mathbf C_{\sigma\sigma}&0\\0&\mathbf C_{\sigma\sigma}^*\end{pmatrix}$ |
| UHF | real UHF | ASDW | $\hat S_z,\hat K$ | $\begin{pmatrix}\mathbf C_{\sigma\sigma}&0\\0&\mathbf C_{\sigma'\sigma'}\end{pmatrix}$, real |
| UHF | complex UHF | ASW | $\hat S_z$ | same blocks, complex |
| GHF | paired GHF | TSCW | $\hat\Theta$ | $\begin{pmatrix}\mathbf C_{\sigma\sigma}&\mathbf C_{\sigma\sigma'}\\-\mathbf C_{\sigma\sigma'}^*&\mathbf C_{\sigma\sigma}^*\end{pmatrix}$ |
| GHF | real GHF | TSDW | $\hat K$ | full $2\times2$ block, real |
| GHF | complex GHF | TSW | none | full $2\times2$ block, complex |

**Fukutome's acronyms.**

- **TICS.** Time-reversal-invariant closed shell.
- **CCW.** Charge current wave.
- **ASCW, ASDW, ASW.** Axial spin current wave, axial spin density wave, axial spin wave.
- **TSCW, TSDW, TSW.** Torsional spin current wave, torsional spin density wave, torsional spin wave.

"Axial" means one common spin axis (collinear). "Torsional" means the spin direction varies in space (non-collinear). "Current" classes have complex orbitals and can carry charge or spin currents.

**Releasing one constraint at a time** gives the eleven connections:

| From | To | Released |
|---|---|---|
| real RHF | complex RHF | $\hat\Theta,\hat K$ |
| real RHF | real UHF | $\hat S^2,\hat\Theta$ |
| real RHF | paired UHF | $\hat S^2,\hat K$ |
| complex RHF | complex UHF | $\hat S^2$ |
| real UHF | real GHF | $\hat S_z$ |
| real UHF | complex UHF | $\hat K$ |
| paired UHF | paired GHF | $\hat S_z$ |
| paired UHF | complex UHF | $\hat\Theta$ |
| complex UHF | complex GHF | $\hat S_z$ |
| real GHF | complex GHF | $\hat K$ |
| paired GHF | complex GHF | $\hat\Theta$ |

"Real" and "paired" are alternative constraints. An RHF determinant built from real orbitals satisfies both, which is why one real RHF class covers the corner of the diagram.

**How to use the table.**

- **Energy ordering.** Each arrow enlarges the variational space, so the lowest energy can only go down along it.
- **Stability.** A stability analysis in the larger space tells whether a given solution is still a minimum there. A negative eigenvalue in the corresponding block of the orbital Hessian is the signal; for RHF these are the singlet/triplet and real/complex instabilities ([[rhf-instabilities-and-multiple-solutions]]).
- **Labelling.** A solution produced by a GHF code need not be in a GHF class. Diagnose it: it may be collinear (Gram test in [[ghf]]), real, or Kramers-paired.

## Diagnostics

**$\hat S_z$.** For a single determinant and any one-body operator $\hat A$, the variance is

$$
\langle\hat A^2\rangle - \langle\hat A\rangle^2 = \sum_{i\in\text{occ}}\sum_{a\in\text{virt}}|\langle\chi_a|\hat a|\chi_i\rangle|^2,
$$

with $\hat A = \sum_k \hat a(k)$. This follows from Wick's theorem: only the occupied-virtual block survives ([[normal-ordering-and-wicks-theorem]]). For $\hat a = \hat s_z$ the variance vanishes exactly when $\hat S_z$ is a good quantum number.

**$\hat S^2$.** Use the standard single-determinant formula for $\langle S^2\rangle$ ([[uhf]], [[spin-operators]]). It equals $S(S+1)$ only for a spin eigenfunction.

**$\hat K$.** The coefficients are real up to a unitary transformation of the occupied space, i.e. $\mathbf P$ is real.

**$\hat\Theta$.** The spin density is odd under time reversal, so a $\hat\Theta$-invariant determinant has $m_k(\mathbf r)=0$ everywhere. The converse fails. A complex RHF determinant has no spin density, yet it breaks $\hat\Theta$ through its complex (current-carrying) orbitals. Vanishing magnetization is therefore necessary but not sufficient.

!!! example "Labelling the H₃/STO-3G solutions at side 1.5 Å (computed for this note)"
    | Solution | $E$ ($E_h$) | $\langle S_z\rangle$ | Var$(S_z)$ | $\langle S^2\rangle$ | max $\lvert\mathrm{Im}\,C\rvert$ | Class |
    |---|---:|---:|---:|---:|---:|---|
    | UHF (stable) | −1.391833 | +0.5000 | 0.0000 | 1.343 | 0 | real UHF (ASDW) |
    | non-collinear GHF | −1.398580 | 0.0000 | 0.3236 | 1.192 | 0 | real GHF (TSDW) |

    - **Starting points.** From six starting densities, each the real-GHF density plus a random Hermitian complex perturbation (amplitude 0.05), complex GHF always returned to the real solution (difference $4\times10^{-14}\,E_h$).
    - **What that shows.** No lower TSW solution was found. This is evidence, not proof: a complex-orbital Hessian analysis would be needed to show that the TSDW state is stable against $\hat K$-breaking rotations.
    - **No time-reversal symmetry.** Neither solution is $\hat\Theta$ invariant, which is impossible for an odd electron count anyway.

## Source

P.-F. Loos, *Many Electrons, One Determinant: Hartree-Fock Theory, Basis Sets, and Molecular Integrals*, ESQC 2026 lecture chapter (course notes; edition/publication details to add), Sec. 3.4, pp. 102-103, Table 2 and Fig. 19.

Primary sources as cited there:

- J. L. Stuber and J. Paldus, "Symmetry breaking in the independent particle model", in E. J. Brändas and E. S. Kryachko (eds.), *Fundamental World of Quantum Chemistry*, Vol. 1 (Kluwer, Dordrecht, 2003), pp. 67-139.
- H. Fukutome, *Int. J. Quantum Chem.* **20**, 955 (1981).
- T. M. Henderson, C. A. Jiménez-Hoyos and G. E. Scuseria, *J. Chem. Theory Comput.* **14**, 649 (2018).
- H. G. A. Burton, A. J. W. Thom and P.-F. Loos, *J. Chem. Theory Comput.* **15**, 4374 (2019).

The time-reversal convention $\hat\Theta = -i\boldsymbol\sigma_y\hat K$ and the variance formula are standard. They are stated in my own words and not taken from Loos. Numbers from `esqc/ghf/ghf_classes.py` (PySCF 2.15).
