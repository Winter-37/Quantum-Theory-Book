---
id: wouters-2017-five-years-dmet
title: Wouters, Jiménez-Hoyos, Chan 2017 - Five years of density matrix embedding theory
summary: A book chapter reviewing DMET as of 2017 - the Schmidt decomposition, bath orbitals from a determinant, interacting and non-interacting bath Hamiltonians, energy expressions, self-consistency, and extensions to spectral functions via response-state baths.
kind: paper
status: in-progress
tags: [DMET, review, embedding, schmidt-decomposition, spectral-functions]
prerequisites: []
related: [schmidt-decomposition-and-dmet-bath, dmet-embedding-hamiltonian, dmet-self-consistency-and-correlation-potential, wouters-2016-practical-dmet]
order: 20
authors: S. Wouters, C. A. Jiménez-Hoyos, G. K.-L. Chan
journal: Chapter 8 in Fragmentation - Toward Accurate Calculations on Complex Molecular Systems, ed. M. S. Gordon (Wiley)
year: 2017
doi: to verify
date: 2026-11-08
---

## Research problem

Summarize what DMET had become five years after its introduction: its formal basis, the choices an implementation must make, and its extensions.

## Method

Review chapter. The core derivations (Eqs. 8.1-8.11 for the Schmidt decomposition and bath; Eqs. 8.19-8.24 for Hamiltonians and energies) follow the same line as [[wouters-2016-practical-dmet]].

## Contributions beyond the 2016 guide

- **Response formulation.** Ground-state baths miss excitations. Building the bath from the Schmidt decomposition of an approximate first-order response wave function gives accurate spectral functions. The chapter proves that the local density of states can be obtained with a Fock space of bath orbitals: it suffices to add one response orbital to the bath (two, for the real and imaginary parts, if real orbitals are wanted), Eq. 8.29 and the following discussion.
- **Applications.** Hubbard and hydrogen-chain benchmarks; with one atom per impurity, DMET beats DMFT against DMRG for the hydrogen chain, attributed to the interacting bath.
- **Context.** Places DMET between tensor-network states (entanglement of a fragment) and DMFT (self-consistent local Green's function).

## Relevance

A second source for Part 4, Chapter 19 ([[schmidt-decomposition-and-dmet-bath]], [[dmet-embedding-hamiltonian]]).
