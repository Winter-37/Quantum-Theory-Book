---
id: propagators-and-superoperators
title: Propagators (many-body Green's functions) and the superoperator formalism
summary: Jørgensen and Simons' general framework. A propagator ⟨⟨A;B⟩⟩_E has poles at energy differences between the reference state and states with N or N±1 electrons, and residues that are transition amplitudes. It obeys an equation of motion; with the superoperator Ĥ X = [H, X], a binary product and complete operator manifolds, it becomes (B†|(E1̂+Ĥ)⁻¹|A), computed from a generalized eigenvalue problem. Truncation, order analysis, the hermiticity theorem and partitioning. The spectral form, sum rule and equation of motion checked on exact H2 states.
status: in-progress
kind: theory
level: advanced
tags: [propagator, greens-function, superoperator, equation-of-motion, spectral-representation, operator-manifold, response-function]
prerequisites: [greens-functions-single-particle, second-quantized-operators, baker-campbell-hausdorff]
related: [one-particle-greens-function, polarization-propagator-rpa, molecular-properties-and-response, mcscf-second-order-optimization]
also: [04_Electronic_Structure_Theory/08_Electronic_and_Molecular_Properties/08_Excitation_Energies, 04_Electronic_Structure_Theory/08_Electronic_and_Molecular_Properties/01_Electronic_Energies]
date: 2026-11-03
---

## Why propagators

Stationary-state methods compute two states and subtract their energies. Ionization and excitation energies are small differences of large numbers, and transition moments between separately optimized states involve nonorthogonal orbitals ([[molecular-properties-and-response]]). Propagators deliver energy **differences** and transition **amplitudes** directly, from a calculation built on one reference state.

## Definition and spectral form

**Time domain.** For operators $A$, $B$ and reference state $|0\rangle$ (J-S Eq. 6.1, $\hbar = 1$):

$$
\langle\langle A(t); B\rangle\rangle = -i\,\theta(t)\langle0|A(t)B|0\rangle \mp i\,\theta(-t)\langle0|BA(t)|0\rangle,
\qquad A(t) = e^{iHt}Ae^{-iHt}.
$$

The lower sign (+) is used when $A$, $B$ contain an odd number of creation/annihilation operators (e.g. $a_r$, $a_r^\dagger a_s^\dagger a_t$), the upper (−) when even (e.g. $a_r^\dagger a_s$). The overall sign conventions differ between texts; J-S's printed prefactors are only partly legible in the scan, so the form here follows the standard definition (general knowledge).

**Energy domain.** Insert a complete set of eigenstates $|n\rangle$ and Fourier transform with a convergence factor $e^{-\eta|t|}$:

$$
\langle\langle A; B\rangle\rangle_E = \lim_{\eta\to0^+}\sum_n\left[\frac{\langle0|A|n\rangle\langle n|B|0\rangle}{E - (E_n - E_0) + i\eta} \pm \frac{\langle0|B|n\rangle\langle n|A|0\rangle}{E + (E_n - E_0) - i\eta}\right].
$$

**What the poles mean.**

- **Number-conserving $A$, $B$** (e.g. $a_r^\dagger a_s$, the dipole operator): the states $|n\rangle$ have $N$ electrons. Poles at $\pm(E_n - E_0)$ are **excitation energies**; residues are transition amplitudes, e.g. $|\langle0|\mathbf r|n\rangle|^2$. This is the polarization propagator ([[polarization-propagator-rpa]]).
- **$A = a_r$, $B = a_s^\dagger$:** poles at $E_n^{N+1} - E_0$ (electron affinities) and $E_0 - E_n^{N-1}$ (minus ionization potentials). This is the electron propagator, the one-particle Green's function ([[one-particle-greens-function]]).

Because the second-quantized Hamiltonian does not depend on $N$ ([[second-quantized-operators]]), one $H$ describes the reference and the ions.

**Equation of motion.** Differentiating in time and using $i\,dA/dt = [A, H]$:

$$
E\,\langle\langle A; B\rangle\rangle_E = \langle0|[A, B]_\mp|0\rangle + \langle\langle[A, H]; B\rangle\rangle_E ,
$$

with the anticommutator for odd operators. Iterating it generates a hierarchy, the starting point for EOM methods. J-S note that the EOM and superoperator routes lead to the same working equations.

!!! example "Exact H₂ (STO-3G, R = 1.4 bohr), all 16 Fock-space states (computed for this note)"
    - **Poles.** The poles of $\langle\langle a_1; a_1^\dagger\rangle\rangle_E$ are at the exact IPs, 0.598765 (H₂⁺ ground state) and 1.375959 (excited H₂⁺). The EA poles are at 0.690829 and 1.490925. Koopmans' values are $-\varepsilon_1 = 0.578203$ and $\varepsilon_2 = 0.670268$.
    - **Pole strengths.** For the occupied orbital: 0.9873 at the main IP pole and 0.0127 at an electron-addition pole. Correlation puts a small amount of "empty" character into the occupied orbital.
    - **Sum rule.** The residues sum to $\langle0|\{a_r, a_r^\dagger\}|0\rangle = 1$ exactly.
    - **Equation of motion.** At $E = 0.37$, $E\,G_{11} = 0.372883735663$ and $\langle\{a_1, a_1^\dagger\}\rangle + \langle\langle[a_1, H]; a_1^\dagger\rangle\rangle = 0.372883735663$.

## Superoperators

**Superoperator Hamiltonian.** Define $\hat H X = [H, X]$ for any operator $X$, and the identity superoperator $\hat 1 X = X$. The Heisenberg operator is then $A(t) = e^{i\hat Ht}A$, by the nested-commutator series ([[baker-campbell-hausdorff]]).

**Binary product.** $(C|D) = \langle0|[C^\dagger, D]_\pm|0\rangle$, with the anticommutator for odd operators.

**Resolvent form.** The Fourier transform then gives

$$
\langle\langle A; B\rangle\rangle_E = (B^\dagger|(E\hat1 + \hat H)^{-1}|A),
$$

a "matrix element" of the superoperator resolvent, analogous to $\mathbf G = (E\mathbf 1 - \mathbf H)^{-1}$ ([[greens-functions-single-particle]]).

**Complete operator manifolds (Manne, Dalgaard).** Applied to a reference determinant, these operator sets generate complete sets of kets:

- $\{1, p^\dagger\alpha, p^\dagger q^\dagger\beta\alpha, \ldots\}$ for $N$ electrons;
- $\{r^\dagger, r^\dagger p^\dagger\alpha, \ldots\}$ for $N+1$;
- $\{\alpha, \alpha\beta r^\dagger, \ldots\}$ for $N-1$.

(Greek letters are occupied, Latin virtual.) This remains true for a multiconfigurational $|0\rangle$ not orthogonal to the determinant. In the binary product each operator contributes to both the $N+1$ and the $N-1$ space, e.g. $(r^\dagger|p^\dagger q^\dagger\alpha) = \delta_{rp}\langle0|q^\dagger\alpha|0\rangle - \delta_{rq}\langle0|p^\dagger\alpha|0\rangle$.

**Working equation.** Inserting the corresponding resolution of the identity, $\hat 1 = |\mathbf T^\dagger)(\mathbf T^\dagger|\mathbf T^\dagger)^{-1}(\mathbf T^\dagger|$, gives J-S's Eq. (6.32):

$$
\langle\langle A; B\rangle\rangle_E = (B^\dagger|\mathbf T^\dagger)\,(\mathbf T^\dagger|E\hat1 + \hat H|\mathbf T^\dagger)^{-1}\,(\mathbf T^\dagger|A).
$$

The overlap $(\mathbf T^\dagger|\mathbf T^\dagger)$ and the superoperator matrix $(\mathbf T^\dagger|\hat H|\mathbf T^\dagger)$ play the roles of the overlap and Hamiltonian matrices of CI.

**Poles and residues.** The poles are the roots of $\det(\mathbf T^\dagger|E\hat1 + \hat H|\mathbf T^\dagger) = 0$, i.e. of the generalized eigenvalue problem $\bar{\mathbf H}\mathbf U_j = -E_j\mathbf S\mathbf U_j$. When $\bar{\mathbf H}$ is Hermitian and $\mathbf S$ positive definite, transforming with $\mathbf S^{-1/2}$ gives

$$
\langle\langle A; B\rangle\rangle_E = (B^\dagger|\mathbf T^\dagger)\,\mathbf U(E\mathbf 1 - \mathbf E)^{-1}\mathbf U^\dagger\,(\mathbf T^\dagger|A),
\qquad
\text{residue at }E_j = \sum_{kl}(B^\dagger|T_k^\dagger)U_{kj}U_{lj}^*(T_l^\dagger|A).
$$

## Approximations

**Truncating the manifold.** In practice one chooses a reference $|0\rangle$ and a finite operator set:

- $A = a_j$ for primary ionizations;
- $A = a_i a_j a_k^\dagger$ for shake-up ionizations;
- $A = a_i^\dagger a_j$ for single excitations.

The symmetry of each operator must couple with that of $|0\rangle$ to give pure-symmetry states.

**Order analysis.** Expand $H = H^0 + V$ and $|0\rangle = |0^{(0)}\rangle + |0^{(1)}\rangle + \cdots$ by Rayleigh-Schrödinger theory. Keep each matrix element through the order needed for the poles (and residues) to be correct to a chosen order. Order is taken as a proxy for accuracy.

**Hermiticity theorem.** The difference $(T_k^\dagger|\hat H|T_l^\dagger) - (T_l^\dagger|\hat H|T_k^\dagger)^*$ is the expectation value $\langle0|[X_{kl}, H]|0\rangle$ of a commutator with $H$, where $X_{kl}$ is a commutator built from $T_k$ and $T_l$ (J-S Eq. 6.42; the exact operator order is not legible in the scan). It vanishes if $|0\rangle$ is an exact eigenstate. If $|0\rangle$ is correct through order $n$, the superoperator matrix is Hermitian through order $n$. One may therefore compute only the easier element of each pair (e.g. $(p^\dagger q^\dagger\alpha|\hat H|r^\dagger)$) and obtain its partner by Hermiticity.

**Partitioning.** Split the manifold into a primary block $a$ (e.g. single creators) and a secondary block $b$ (e.g. 2p1h, 2h1p). The primary block of the inverse is

$$
\big[(E\mathbf S + \bar{\mathbf H})^{-1}\big]_{aa} = \big[(E\mathbf S_{aa} + \bar{\mathbf H}_{aa}) - (E\mathbf S_{ab} + \bar{\mathbf H}_{ab})(E\mathbf S_{bb} + \bar{\mathbf H}_{bb})^{-1}(E\mathbf S_{ba} + \bar{\mathbf H}_{ba})\big]^{-1}.
$$

It has **all** poles of the full problem when treated exactly. If the coupling block is of first order and one searches away from the zeroth-order poles of the $bb$ block, the second term is a small, energy-dependent correction. This is the self-energy structure of the electron propagator.

**MCSCF references.** Perturbation theory fails for strongly multiconfigurational states (e.g. H₂ at large R). J-S describe MCSCF-based propagators with the operator set $\{r^\dagger s, s^\dagger r, |n\rangle\langle0|, |0\rangle\langle n|\}$: the same orbital and state-rotation operators as in MCSCF optimization ([[mcscf-second-order-optimization]]). The generalized Brillouin theorem makes parts of the superoperator matrix Hermitian. Without an order parameter, choosing and partitioning the manifold was an open problem when J-S wrote.

## Source

Jørgensen and Simons, *Second Quantization-Based Methods in Quantum Chemistry* (Academic Press, New York, 1981), Ch. 6, Secs. A-C, pp. 122-134, Eqs. (6.1)-(6.45). The sign conventions in the definition are standard (general knowledge) because the scanned equation is partly illegible. H₂ checks computed for this note.
