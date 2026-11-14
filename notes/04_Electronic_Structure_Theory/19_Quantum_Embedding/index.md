Treating a fragment of a molecule with a correlated method while its environment is described by a mean field. This chapter covers density matrix embedding theory (DMET) in its molecular, one-shot form, up to its analytic nuclear gradient.

**Path.**

1. The Schmidt decomposition and the bath orbitals of a Slater determinant.
2. The embedding Hamiltonian: fragment plus bath, with the core as a frozen mean field, and Form B.
3. Combining fragments: democratic partitioning, two energy functionals, and the global chemical potential.
4. Self-consistency with a correlation potential, and when one-shot DMET is enough.
5. The analytic nuclear gradient as a Lagrangian.

**Needs.** Chapter 3 (RHF), Chapter 6 (density matrices and natural orbitals), Chapter 9 (FCI). Section 5 needs Chapter 15 (CPHF, Z-vector, CP-CI).

**Leads to.** Part 6, Chapter 7 (DMET with quantum solvers).

**Core (first pass).** [[schmidt-decomposition-and-dmet-bath]], [[dmet-embedding-hamiltonian]], [[dmet-energy-functionals-and-chemical-potential]].

**Deep (second pass).** [[dmet-self-consistency-and-correlation-potential]], [[dmet-analytic-nuclear-gradient]].

**Checkpoint.** For a two-atom fragment of an H$_6$ ring, show from $\gamma^2=\gamma$ that the bath singular values are $\sqrt{n(1-n)}$ and that the embedding space holds 4 electrons. Then explain why DMET with three-atom fragments reproduces FCI exactly.

**Planned sections:** Bootstrap embedding; Embedded wave function (EWF) and MP2 bath natural orbitals; DMFT; Projection-based wave-function-in-DFT embedding.
