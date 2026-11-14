---
id: li-2023-dmet-gradient
title: Li, Yang, Zhang, Chan 2023 - Multi-site reaction dynamics through multi-fragment density matrix embedding
summary: Derives and implements the analytic nuclear gradient of one-shot multi-fragment DMET with Löwdin orbitals, through a Lagrangian with multipliers for the solver equations, the electron-number condition and the HF equations. Validated against HF and finite differences, then used for a Diels-Alder transition state and DMET-driven molecular dynamics of proton transport in a protonated water tetramer.
kind: paper
status: in-progress
tags: [DMET, analytic-gradients, lagrangian, molecular-dynamics, proton-transport, Diels-Alder]
prerequisites: []
related: [dmet-analytic-nuclear-gradient, dmet-energy-functionals-and-chemical-potential]
order: 20
authors: C. Li, J. Yang, X. Zhang, G. K.-L. Chan
journal: Journal of Chemical Physics 158, 134105
year: 2023
doi: 10.1063/5.0142961
date: 2026-11-08
---

## Research problem

Reactions in disordered settings (water, combustion, nanoreactors) happen at many sites at once, so no single active region can be chosen in advance. DMET with atom-sized fragments gives a continuous surface without choosing a reactive site, but molecular dynamics and optimizations need its gradient.

## Method

The energy uses a correlated global density assembled from all fragments (Eqs. 5-7). The gradient is $\partial\mathcal L/\partial A$ for $\mathcal L = E - z(N-N_{\rm elec}) - \lambda^\dagger X - \alpha^\dagger M$ (Eqs. 12-16), with auxiliary RDMs carrying the solver detail (Eq. 17). Appendices: HF and FCI solver responses (A), orbital-transformation gradient (B), CPHF contribution (C), overlap and integral terms (D). Code: github.com/MoleOrbitalHybridAnalyst/DMET-preview.

## Results

- **Validation.** Water trimer, HF solver: energy within $10^{-11}$ and gradient MAE below $10^{-8}$ a.u. of global HF. FCI solver: agreement with finite differences, with and without $\mu$. H$_{10}$ ring: integrated gradient reproduces energies to $10^{-6}\ E_h$.
- **Diels-Alder** (MVK + cyclopentadiene, 6-31G, FCI fragments): without $\mu$ fitting the electron number is off by about 0.7, so only fitted results are reported. With D3, the barrier is close to R-CCSD(T); imaginary frequency 562 cm$^{-1}$ against 581 (CCSD).
- **Proton transport** in H$^+$(H$_2$O)$_4$ by metadynamics-biased DMET MD: DMET follows CCSD(T) continuously where projection-based DFT embedding jumps when the proton changes partner.

## Limitations

Small bases (STO-3G for O in the MD), FCI solvers only; reaction energies (reactant against product) less accurate than barriers; the method relies on correlation being local.

## Relevance

Source for [[dmet-analytic-nuclear-gradient]], for the Fock-matrix form of the embedding Hamiltonian in [[dmet-embedding-hamiltonian]], and for the correlated-density functional in [[dmet-energy-functionals-and-chemical-potential]].
