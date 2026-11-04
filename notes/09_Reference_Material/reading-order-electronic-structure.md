---
id: reading-order-electronic-structure
title: Reading order - a path through the electronic-structure notes, from linear algebra to coupled cluster, MCSCF and calibration
summary: A curated order for reading the notebook's electronic-structure notes, in nine stages. The core path is Szabo-Ostlund level; HJO deep dives are marked as optional second passes. Each entry says why it comes where it does, and each stage ends with a checkpoint for testing understanding before moving on.
status: in-progress
kind: reference
level: introductory
tags: [reading-guide, study-plan, curriculum, electronic-structure, overview]
prerequisites: []
related: [matrix-eigenvalue-problem, variational-principle, rhf, electron-correlation, full-ci, mp2, coupled-cluster-second-quantization, mcscf-and-gvb, standard-models-h2-and-water]
also: []
date: 2026-11-04
---

## How to use this guide

**Two passes.** Each stage has a **core** list, to be read in order, and an optional **deep** list. Core notes are mostly Szabo-Ostlund or Jørgensen-Simons level: first quantization, explicit determinants, small worked models. Deep notes follow Helgaker-Jørgensen-Olsen (HJO): second quantization, exponential parametrizations, Lagrangians and production algorithms.

**Suggested route.**

1. Read every core list from stage 1 to stage 9.
2. Go back for the deep lists. Their stage 0 (second quantization) is a prerequisite for almost every deep note.

**Checkpoints.** Each stage ends with something to reproduce. Most of these worked numbers already sit inside the notes, so the checkpoint is to rederive or recompute them before looking.

## Stage 1 - Mathematics

**Core.**

1. [[matrices-and-determinants]] - notation, determinants and inverses.
2. [[dirac-notation]] - bras, kets and projectors in finite spaces.
3. [[change-of-basis]] - unitary transformations, used for every orbital change later.
4. [[matrix-eigenvalue-problem]] - Hermitian diagonalization, the engine of HF and CI.
5. [[functions-of-matrices]] - $\mathbf S^{-1/2}$, $e^{\mathbf A}$ and spectral functions.
6. [[orthonormal-functions-and-operators]] - completeness, the delta function and operators in function space.

**Deep.**

- [[unitary-matrices-exponential-logarithm]] - the $e^{-\boldsymbol\kappa}$ parametrization behind orbital rotations.
- [[baker-campbell-hausdorff]] - commutator expansions, needed for orbital rotations and coupled cluster.

**Checkpoint.** Diagonalize a 2 × 2 Hermitian matrix by hand. Then build $\mathbf S^{-1/2}$ for a two-function overlap matrix.

## Stage 2 - Quantum-mechanical foundations

**Core.**

1. [[molecular-hamiltonian]] then [[born-oppenheimer-approximation]] - what we are solving.
2. [[atomic-units]] and [[integral-notation]] - the conventions used everywhere after this.
3. [[variational-principle]] then [[variation-method]] - the upper bound and how it is used.
4. [[linear-variation-method]] - the secular equation; it explains why HF and CI become eigenvalue problems.
5. [[spin-orbitals-and-antisymmetry]], [[spin-operators]], [[slater-determinants]] - building antisymmetric many-electron functions.

**Deep.**

- [[upper-bounds-and-interlacing]] - Hylleraas-Undheim; why excited CI roots are also bounds.
- [[hellmann-feynman-and-virial-theorems]] - properties as energy derivatives.
- [[exact-wave-function-properties-and-symmetry]] - what an approximate wave function should inherit from the exact one.
- [[rayleigh-schrodinger-perturbation-theory]] and [[greens-functions-single-particle]] - general quantum-mechanics tools reused in stages 6 and 9.

**Checkpoint.** Prove the variational bound by eigenfunction expansion. Show that a two-electron determinant changes sign under exchange.

## Stage 3 - Matrix elements and basis sets

**Core.**

1. [[excited-determinants]] - single, double and higher excitations; the FCI space.
2. [[slater-condon-rules]] - the matrix elements that every method below uses.
3. [[spin-orbital-to-spatial-orbital]] - integrating out spin.
4. [[spin-adapted-configurations]] - restricted, spin-adapted and unrestricted functions.
5. [[minimal-basis-h2-model]] - the model system used throughout Szabo.
6. [[gaussian-basis-functions]] then [[pople-basis-sets]] - contracted Gaussians.
7. [[basis-orthogonalization]] - symmetric and canonical orthogonalization.

**Deep.**

- [[genealogical-coupling]] - CSF counting and spin coupling.
- [[radial-basis-functions-slater-and-gaussian]], [[solid-harmonics-angular-basis]] and [[gaussian-basis-sets-and-convergence]] - HJO's account of basis-set design.
- [[gaussian-overlap-distributions-and-one-electron-integrals]], [[electron-repulsion-integrals-md-os-rys]] and [[multipole-methods-and-integral-screening]] - how integrals are actually computed.
- [[basis-set-superposition-error]].

**Checkpoint.** Derive $\langle\Psi_0|\hat H|\Psi_0\rangle$ for minimal-basis H₂ from the Slater-Condon rules.

## Stage 4 - Hartree-Fock

**Core.**

1. [[fock-operator]] - Coulomb and exchange operators.
2. [[hartree-fock-equations]] - the derivation by constrained minimization.
3. [[brillouin-theorem]] - why singles do not mix with HF; it reappears in MP2 and CC.
4. [[rhf]] - the Roothaan equations.
5. [[scf-procedure]] - the full SCF loop, worked for STO-3G HeH⁺.
6. [[heh-plus-minimal-basis-model]] - a second worked model.
7. [[population-analysis]] and [[koopmans-theorem]] - what to do with the orbitals.
8. [[uhf]] then [[h2-dissociation-rhf-uhf]] - the dissociation problem; this motivates stages 5-8.
9. [[hf-closed-shell-basis-set-trends]] - how HF numbers behave with basis size.

**Deep** (after the deep part of stage 0).

- [[orbital-rotations]] then [[scf-second-order-and-stability]].
- [[hartree-fock-csf-parametrization-and-canonical-conditions]] - HF in second quantization, redundancies and the generalized Brillouin theorem.
- [[generalized-fock-matrix-and-orbital-hessian]] - needed again for MCSCF.
- [[scf-convergence-diis-and-newton]] and [[density-based-hartree-fock]] - production SCF.
- [[rhf-instabilities-and-multiple-solutions]] - triplet and singlet instabilities and the allyl radical.

**Checkpoint.** Run the HeH⁺ SCF by hand for two iterations. Then explain why RHF H₂ dissociates to the wrong limit.

## Stage 0 (deep only) - Second quantization

Read this before any deep note.

1. [[creation-and-annihilation-operators]].
2. [[second-quantized-operators]] then [[second-quantization-in-a-finite-basis]].
3. [[spin-tensor-operators]] - singlet excitation operators $\hat E_{pq}$.
4. [[density-matrices-second-quantization]], [[one-particle-rdm]] and [[natural-orbitals]].
5. [[nonorthogonal-second-quantization]] - needed only for biorthogonal tricks (CI orbital transformation, nonorthogonal states).

**Checkpoint.** Derive $\hat H = \sum h_{pq}\hat E_{pq} + \tfrac12\sum g_{pqrs}\hat e_{pqrs}$ and evaluate $\langle\text{HF}|\hat H|\text{HF}\rangle$ in this language.

## Stage 5 - Electron correlation and configuration interaction

**Core.**

1. [[electron-correlation]] then [[h2-minimal-basis-correlation-analysis]] - what HF misses, static versus dynamic.
2. [[full-ci]] - the exact answer in a basis.
3. [[cisd]] then [[size-consistency]] - truncation and its central flaw.
4. [[natural-orbitals]] - occupation numbers as a diagnostic.
5. [[ci-in-practice]].

**Deep.**

- [[coulomb-cusp-and-helium-expansions]] - why correlation converges slowly with basis size.
- [[ci-size-extensivity-and-excitation-levels]], [[ci-optimization-newton-and-davidson]] and [[determinant-strings-and-direct-ci]] - HJO Ch. 11: CAS and RAS spaces, Davidson, direct CI.

**Checkpoint.** Show that CID for two noninteracting H₂ molecules is not twice the monomer value.

## Stage 6 - Many-body perturbation theory

**Core.**

1. [[mp2]] - the Møller-Plesset partitioning and the second-order energy.
2. [[mp3]] - third order and the first signs of oscillation.
3. [[orbital-perturbation-theory]] - one-particle perturbations.

**Deep.**

- [[perturbation-theory-second-quantization]] then [[linked-cluster-theorem]] - diagrams and size consistency (J-S).
- [[rspt-wigner-rule-and-hylleraas-functional]] - 2n + 1 rule and Hylleraas functional (HJO 14.1).
- [[moller-plesset-and-coupled-cluster-perturbation-theory]] - CCPT and MP4 (HJO 14.2-14.4).
- [[mp-convergence-intruders-analytic-continuation]] - when and why MP diverges (HJO 14.5).

**Checkpoint.** Derive the closed-shell MP2 formula from the spin-orbital one.

## Stage 7 - Coupled cluster

**Core.**

1. [[iepa]] then [[coupled-pair-approximations]] - the historical road from pairs to CC.
2. [[coupled-cluster-doubles]] - CCD derived from the CI hierarchy.
3. [[coupled-cluster-second-quantization]] - $e^{\hat T}$, the terminating BCH series and the projected equations.

**Deep** (HJO Ch. 13-14).

1. [[coupled-cluster-hierarchy-and-size-extensivity]].
2. [[coupled-cluster-optimization-and-lagrangian]] - DIIS, Λ equations and properties.
3. [[closed-shell-ccsd-t1-transformation]].
4. [[perturbative-triples-cc2-cc3]] - CCSD(T), the workhorse.
5. [[eom-ccsd-and-size-extensivity]] - excited states.
6. [[coupled-cluster-variants-brueckner-qcisd-open-shell]].

**Checkpoint.** Expand $e^{\hat T}$ to quadruples and identify each disconnected term. Explain why CCSD is exact for two electrons.

## Stage 8 - Multiconfigurational methods

**Core.**

1. [[mcscf-and-gvb]] - why multiple configurations are needed and what GVB and MCSCF do.
2. [[mcscf-second-order-optimization]] - Newton MCSCF and the H₂ CAS(2,2) example (J-S).

**Deep** (HJO Ch. 12 and 14.7).

1. [[mcscf-parametrization-gradient-and-hessian]].
2. [[mcscf-trust-region-and-augmented-hessian]].
3. [[state-averaged-mcscf-and-configuration-rotations]].
4. [[caspt2-and-caspt-series]] - adding dynamical correlation on top.

**Checkpoint.** Show that active-active rotations are redundant in a CAS but not in a general MCSCF.

## Stage 9 - Properties, response and calibration

**Core.**

1. [[standard-models-h2-and-water]] - every model above compared against FCI; read it as a review of stages 4-8.
2. [[geometry-optimization]].

**Deep.**

- [[molecular-properties-and-response]], [[analytic-gradients-and-force-constants]] and [[lagrangian-for-nonvariational-energies]] - derivatives of variational and nonvariational energies.
- [[propagators-and-superoperators]], [[one-particle-greens-function]], [[ionization-potentials-second-order-self-energy]] and [[polarization-propagator-rpa]] - the propagator view (J-S).
- [[hjo-calibration-structures-and-dipoles]] then [[hjo-calibration-energies-atomization-reactions-barriers]] - how accurate the methods really are (HJO Ch. 15). Read these last.

**Checkpoint.** Predict, before looking, the ordering of HF, MP2, CCSD and CCSD(T) bond lengths against experiment in a triple-zeta basis. Then check the calibration note.

## Source

Organizes the notebook's own notes. They are built mainly on Szabo and Ostlund, *Modern Quantum Chemistry*; Jørgensen and Simons, *Second Quantization-Based Methods in Quantum Chemistry*; and Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, Chichester, 2000). Each note cites its exact sections.
