---
id: wouters-2016-practical-dmet
title: Wouters et al. 2016 - A practical guide to density matrix embedding theory in quantum chemistry
summary: The explicit implementation-level description of molecular DMET - bath orbitals from the mean-field 1-RDM, interacting and non-interacting bath Hamiltonians, democratic energy evaluation, the global chemical potential, and correlation-potential self-consistency - tested on H10 and H90 rings, a Be30 ring and an SN2 reaction, with the QC-DMET code.
kind: paper
status: in-progress
tags: [DMET, embedding, tutorial, self-consistency, chemical-potential, SN2]
prerequisites: []
related: [schmidt-decomposition-and-dmet-bath, dmet-embedding-hamiltonian, dmet-energy-functionals-and-chemical-potential, dmet-self-consistency-and-correlation-potential]
order: 10
authors: S. Wouters, C. A. Jiménez-Hoyos, Q. Sun, G. K.-L. Chan
journal: Journal of Chemical Theory and Computation 12, 2706-2719
year: 2016
doi: 10.1021/acs.jctc.6b00316
date: 2026-11-08
---

## Research problem

The original DMET papers were short; implementers lacked an explicit account of the bath construction, the Hamiltonians, the energy and the self-consistency for chemical systems.

## Method

- **Sec. 2.** Bath from the SVD of the fragment block of the occupied orbitals, or equivalently from the environment block of the 1-RDM (MacDonald's theorem); orbital truncation and IAO-based fragments.
- **Sec. 3.** Low-level Hamiltonian with correlation potential; interacting and non-interacting bath high-level Hamiltonians; global chemical potential.
- **Sec. 4.** Democratic partitioning of expectation values and the fragment energy (Eq. 28).
- **Sec. 5.** Cost functions (Eqs. 29-32), the Lieb-type dual (Eq. 35), the full algorithm with secant fit of $\mu_{\rm glob}$ (Eq. 36).

## Results

- **H$_{10}$ ring** (STO-6G, FCI solver): DMET follows FCI along the dissociation; self-consistency helps small fragments.
- **H$_{90}$ ring**: larger fragments within a few tenths of m$E_h$ per atom of DMRG beyond 1.0 Å; convergence with fragment size is non-monotonic.
- **Be$_{30}$ ring** (CCSD solver): within ~4 m$E_h$ per atom of full CCSD with one-atom fragments, ~1 m$E_h$ with 5-6 atoms; near the RHF crossing DMET is smoother than full CCSD, and self-consistency removes most of the dependence on the starting determinant.
- **SN2 reaction** (cc-pVDZ, CCSD solver): democratic DMET gives a qualitatively wrong profile; the active-space energy of the reacting fragment with one bath orbital per broken bond converges fastest. The democratic electron count is the largest error.

## Limitations

Democratic partitioning is poor for chemical changes localized in one fragment; bath truncation by eigenvalue threshold causes discontinuities along reaction paths.

## Relevance

Primary source for Part 4, Chapter 19. The SN2 finding is a warning for any DMET geometry work on localized reactions: check the bath selection and the electron-count error, not only the total energy.
