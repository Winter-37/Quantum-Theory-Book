The variational quantum eigensolver: a parametrized circuit, a measured energy, a classical optimizer.

**Path.**

1. The algorithm and where its cost goes (shots, trainability, noise).
2. Ansätze: hardware-efficient, unitary coupled cluster, symmetry-preserving, adaptive.

**Needs.** Chapter 2; Part 4, Chapter 11 for UCC.

**Leads to.** Chapter 5 (SQD avoids the measurement cost) and Chapter 7 (VQE as a DMET solver).

**Core (first pass).** [[variational-quantum-eigensolver]], [[vqe-ansatze]].

**Checkpoint.** Show that one-parameter UCCD is exact for minimal-basis H$_2$. Estimate the shots needed for 1.6 m$E_h$ from $\sum_k|c_k|$.

**Planned sections:** Measurement grouping and classical shadows; Error mitigation; Excited-state VQE.
