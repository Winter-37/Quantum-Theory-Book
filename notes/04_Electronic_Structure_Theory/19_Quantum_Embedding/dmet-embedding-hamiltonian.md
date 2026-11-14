---
id: dmet-embedding-hamiltonian
title: The DMET embedding Hamiltonian - projecting onto fragment plus bath, with the core as a frozen mean field
summary: Projecting the full Hamiltonian onto determinants of the form (embedding-space determinant) × (core determinant) gives an active-space Hamiltonian whose one-body part carries the Coulomb and exchange field of the core electrons. The same operator can be written without the core density as C^T F C − v_emb[γ_emb] ("Form B"), which depends on the global density only explicitly and is the form to differentiate. Interacting versus non-interacting bath, where the chemical potential enters, and the exact mean-field limit; verified on an H6 ring.
status: in-progress
kind: theory
level: advanced
tags: [DMET, embedding-hamiltonian, active-space, core-potential, form-b, chemical-potential]
prerequisites: [schmidt-decomposition-and-dmet-bath, second-quantized-operators, fock-operator, integral-notation]
related: [dmet-energy-functionals-and-chemical-potential, ci-in-practice, mcscf-and-gvb]
order: 20
date: 2026-11-08
---

Notation: as in [[schmidt-decomposition-and-dmet-bath]]. LOs $i,j,k,l$; embedding orbitals of one fragment $p,q,r,t$; $C$ (LO × embedding) holds the impurity columns first, then the bath. Integrals in chemists' notation. For a per-spin density $D$ the closed-shell mean-field potential is $v[D] = 2J[D]-K[D]$, with $J[D]_{ij} = \sum_{kl}(ij|kl)D_{kl}$ and $K[D]_{ij} = \sum_{kl}(ik|jl)D_{kl}$. $v_{\rm emb}$ is the same operator built from the embedding integrals.

## The projected Hamiltonian

**The projection.** Each fragment's mean-field determinant factorizes as $|\Phi\rangle = |\Phi_{\rm emb}\rangle\otimes|{\rm core}\rangle$ ([[schmidt-decomposition-and-dmet-bath]]). DMET keeps the core determinant fixed and projects $\hat H$ onto all determinants (embedding-space determinant) × $|{\rm core}\rangle$ with $N_{\rm emb}$ electrons per spin in the embedding orbitals. By the Slater-Condon rules this is an ordinary frozen-core active-space Hamiltonian:

$$
\hat H_{\rm emb} = E_{\rm core} + \sum_{pq}\big(h_{\rm emb}+v_{\rm core}\big)_{pq}\,\hat E_{pq}
+ \tfrac12\sum_{pqrt}(pq|rt)\,\hat e_{pqrt},
$$

$$
h_{\rm emb} = C^{\mathsf T}h\,C,\qquad
v_{\rm core} = C^{\mathsf T}v[D_{\rm core}]\,C,\qquad
(pq|rt) = \sum_{ijkl}C_{ip}C_{jq}C_{kr}C_{lt}\,(ij|kl).
$$

$E_{\rm core}$ is a constant and is dropped in the solver. Wouters et al. 2016 (Eqs. 18-20) call this the **interacting-bath** formulation: the two-electron interaction acts on bath as well as impurity orbitals.

**Exact mean-field limit.** Hartree-Fock inside this space, started from anywhere, converges to $2\gamma_{\rm emb}$. The core energy plus the embedding HF energy plus $E_{\rm nuc}$ is the global RHF energy. This holds because the global determinant is a product of core and embedding determinants and the embedded density satisfies the embedded Brillouin condition. DMET therefore loses nothing at the mean-field level; every error comes from the correlated treatment.

## Form B: the core potential without the core density

**The identity.** Insert $D_{\rm core} = \gamma - C\gamma_{\rm emb}C^{\mathsf T}$ into $v_{\rm core}$. Because the embedding integrals are the transformed LO integrals, $C^{\mathsf T}v[CDC^{\mathsf T}]C = v_{\rm emb}[D]$ for any embedding-space $D$. Hence

$$
h_B \equiv h_{\rm emb} + v_{\rm core} = C^{\mathsf T}F\,C - v_{\rm emb}[\gamma_{\rm emb}],
\qquad F = h + v[\gamma].
$$

This is Eq. 4 of Li et al. 2023 ($h = F - V\gamma$ in their antisymmetrized notation).

- **Why it matters.** The two forms are equal at every density. Form B depends on the global density only through $F[\gamma]$ and $\gamma_{\rm emb} = C^{\mathsf T}\gamma C$, both explicitly. The core form needs $D_{\rm core}$, a projector built from an eigenproblem of $\gamma_{EE}$. For an analytic gradient Form B is the one to differentiate ([[dmet-analytic-nuclear-gradient]]).
- **Never build the core.** $D_{\rm core}$ and $E_{\rm core}$ are not needed for the DMET energy either: the fragment energy functionals use only $h_{\rm emb}$, $h_B$, the embedding integrals and the solver's density matrices ([[dmet-energy-functionals-and-chemical-potential]]).

## Chemical potential

Nothing forces the impurity electron counts of different fragments to add up to $N$. A single global shift on the impurity orbitals restores this:

$$
\hat H_I(\mu) = \hat H_{\rm emb} - \mu\sum_{p\in I}\hat E_{pp}.
$$

- **Only in the solver.** $\mu$ shifts impurity orbitals only, the same $\mu$ for every fragment, and it never appears in the energy expressions.
- **Uniqueness.** $\hat H_I(\mu)$ is linear in $\mu$, so each ground-state energy is concave in $\mu$ and each impurity electron count is non-decreasing. A monotone $N(\mu)$ has at most one root.

## Interacting versus non-interacting bath

- **Interacting bath** (above). Two-electron terms on all embedding orbitals. This is the natural choice for quantum-chemistry solvers (CI, CC, DMRG, SQD), and the one used in molecular DMET.
- **Non-interacting bath.** Two-electron terms on the impurity only; a fitted correlation potential on the bath mimics the rest (Wouters et al. 2016, Sec. 3.2). It converges to the exact result with fragment size and suits solvers that struggle with non-local interactions (lattice QMC). For CI or CC solvers the only gain is fewer integrals.

## Worked example

!!! example "H$_6$ ring, STO-3G, fragment = atoms 0, 1"
    Same system as [[schmidt-decomposition-and-dmet-bath]]: 4 embedding orbitals, 4 electrons. Script: `dmet_mini.py`.

    - **Form B.** $\max|h_{\rm emb}+v_{\rm core} - h_B| = 4\times10^{-16}$, with $h_B$ from $C^{\mathsf T}FC - v_{\rm emb}[\gamma_{\rm emb}]$.
    - **Embedding HF.** Started from a uniform density, HF in the 4-orbital space converges to $2\gamma_{\rm emb}$ (largest deviation $2.5\times10^{-10}$, set by the SCF threshold).
    - **Energy bookkeeping.** $E_{\rm core} + E_{\rm emb}^{\rm HF} + E_{\rm nuc} = -3.1570474666255$, against the global $E_{\rm RHF} = -3.1570474666255$ (difference $2\times10^{-15}$).

## Source

- Wouters et al., *J. Chem. Theory Comput.* **12**, 2706 (2016), doi:10.1021/acs.jctc.6b00316. Sec. 3 (Eqs. 13-20): low- and high-level Hamiltonians, interacting and non-interacting bath, global chemical potential.
- C. Li, J. Yang, X. Zhang, G. K.-L. Chan, "Multi-site reaction dynamics through multi-fragment density matrix embedding", *J. Chem. Phys.* **158**, 134105 (2023), doi:10.1063/5.0142961. Eqs. 3-4: the embedding Hamiltonian with $\mu$, and the Fock-matrix form of $h$.
- The name "Form B" is this notebook's own label for the Fock-matrix form (Li et al., Eq. 4).
