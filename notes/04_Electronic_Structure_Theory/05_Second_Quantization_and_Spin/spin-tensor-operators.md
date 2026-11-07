---
id: spin-tensor-operators
title: Spin operators and spin tensor operators in second quantization
summary: S_z, S+ and S− as one-body second-quantized operators; commutators with creation operators show that a†_pα, a†_pβ form a spin doublet and illustrate how commutators lower particle rank. Coupling pairs of creation operators, or creation-annihilation pairs, gives singlet and triplet tensor operators, including the singlet excitation operator used for spin-adapted orbital rotations. All identities checked numerically.
status: in-progress
kind: theory
level: intermediate
tags: [second-quantization, spin, tensor-operators, singlet, triplet, excitation-operators, spin-adaptation]
prerequisites: [creation-and-annihilation-operators, second-quantized-operators, spin-operators]
related: [genealogical-coupling, density-matrices-second-quantization, spin-adapted-configurations, orbital-rotations, mcscf-second-order-optimization, baker-campbell-hausdorff]
order: 40
date: 2026-11-03
---

## Spin operators

Let $p,q,\ldots$ label spatial orbitals and $\sigma = \alpha,\beta$ the spin, with $a_{p\sigma}^\dagger$ creating an electron in $\phi_p\sigma$ (atomic units, $\hbar = 1$). Writing $S_z = \sum_{rs}\langle\phi_r|s_z|\phi_s\rangle a_r^\dagger a_s$ over spin orbitals and integrating over space with orthonormal $\phi_p$:

$$
\hat S_z = \tfrac12\sum_p\big(a_{p\alpha}^\dagger a_{p\alpha} - a_{p\beta}^\dagger a_{p\beta}\big),
\qquad
\hat S_+ = \sum_p a_{p\alpha}^\dagger a_{p\beta},
\qquad
\hat S_- = \sum_p a_{p\beta}^\dagger a_{p\alpha},
$$

and $\hat S^2 = \hat S_-\hat S_+ + \hat S_z^2 + \hat S_z$ ([[spin-operators]]). None of these refers to the number of electrons: the same operators act on every $N$-electron sector.

## Creation operators are a spin doublet

**Commutators.** Using $[a_r^\dagger a_s, a_t^\dagger] = \delta_{st}a_r^\dagger$:

$$
[\hat S_z, a_{p\alpha}^\dagger] = \tfrac12a_{p\alpha}^\dagger,
\qquad
[\hat S_+, a_{p\alpha}^\dagger] = 0,
\qquad
[\hat S_-, a_{p\alpha}^\dagger] = a_{p\beta}^\dagger ,
$$

and similarly $[\hat S_z, a_{p\beta}^\dagger] = -\tfrac12a_{p\beta}^\dagger$, $[\hat S_+, a_{p\beta}^\dagger] = a_{p\alpha}^\dagger$.

**Meaning.** These are the defining relations of a spherical tensor operator of rank $\tfrac12$: $a_{p\alpha}^\dagger$ is the $m = +\tfrac12$ component and $a_{p\beta}^\dagger$ the $m = -\tfrac12$ component. Acting on an $S_z$ eigenstate, $\hat S_z a_{p\alpha}^\dagger|0\rangle = (M_S + \tfrac12)a_{p\alpha}^\dagger|0\rangle$. (The corresponding annihilators, with a sign, form another doublet.)

**Rank reduction.** Each term inside $[\hat S_z, a^\dagger]$ has three operators, yet the result has one. A commutator of an $m$-body string with an $n$-body string has at most $m+n-1$ body rank. In second quantization this cancellation happens at the operator level, before any matrix element is taken; in first quantization it appears only after integrating determinantal matrix elements. The same mechanism makes the coupled-cluster commutator series terminate ([[coupled-cluster-second-quantization]]) and keeps MCSCF gradients and Hessians at two-body level ([[mcscf-second-order-optimization]]).

## Coupling to singlets and triplets

Combining two doublets with Clebsch-Gordan coefficients gives $S = 0$ and $S = 1$ operators.

**Pair creation operators (two electrons in orbitals $p$, $q$).**

$$
\hat P_{pq}^\dagger(0,0) = \tfrac1{\sqrt2}\big(a_{p\alpha}^\dagger a_{q\beta}^\dagger - a_{p\beta}^\dagger a_{q\alpha}^\dagger\big),
$$

$$
\hat P_{pq}^\dagger(1,1) = a_{p\alpha}^\dagger a_{q\alpha}^\dagger,\quad
\hat P_{pq}^\dagger(1,0) = \tfrac1{\sqrt2}\big(a_{p\alpha}^\dagger a_{q\beta}^\dagger + a_{p\beta}^\dagger a_{q\alpha}^\dagger\big),\quad
\hat P_{pq}^\dagger(1,-1) = a_{p\beta}^\dagger a_{q\beta}^\dagger .
$$

**Excitation (replacement) operators** from $q$ to $p$:

$$
\hat E_{pq} = a_{p\alpha}^\dagger a_{q\alpha} + a_{p\beta}^\dagger a_{q\beta}\quad(\text{singlet, up to the factor } 2^{-1/2}),
$$

$$
\hat T_{pq}(1,1) = -a_{p\alpha}^\dagger a_{q\beta},\quad
\hat T_{pq}(1,0) = \tfrac1{\sqrt2}\big(a_{p\alpha}^\dagger a_{q\alpha} - a_{p\beta}^\dagger a_{q\beta}\big),\quad
\hat T_{pq}(1,-1) = a_{p\beta}^\dagger a_{q\alpha}.
$$

These are exactly J-S's operators: their $q_{rs}^\dagger(0,0) = 2^{-1/2}\hat E_{rs}$, $q_{rs}^\dagger(1,1) = -a_{r\alpha}^\dagger a_{s\beta}$, $q_{rs}^\dagger(1,-1) = a_{r\beta}^\dagger a_{s\alpha}$ and $q_{rs}^\dagger(1,0) = 2^{-1/2}(a_{r\alpha}^\dagger a_{s\alpha} - a_{r\beta}^\dagger a_{s\beta})$ (Eq. 1.35, checked on the page image), and their pair operators of Eqs. (1.33)-(1.34). Other texts use other phases for the $M = \pm1$ components; these ones satisfy $[\hat S_+, \hat T(1,0)] = \sqrt2\,\hat T(1,1)$.

**Proving the tensor property (J-S Problem 1.3).** For the $M = 0$ component, using $[a_{j\alpha}^\dagger a_{j\beta}, a_{r\sigma}^\dagger a_{s\sigma'}] = \delta_{jr}\delta_{\beta\sigma}a_{j\alpha}^\dagger a_{s\sigma'} - \delta_{js}\delta_{\sigma'\alpha}a_{r\sigma}^\dagger a_{j\beta}$:

$$
[\hat S_z, q_{rs}^\dagger(1,0)] = 0,\qquad [\hat S_+, q_{rs}^\dagger(1,0)] = \sqrt2\,q_{rs}^\dagger(1,1),\qquad [\hat S_-, q_{rs}^\dagger(1,0)] = \sqrt2\,q_{rs}^\dagger(1,-1),
$$

which are the defining relations $[\hat J_\pm, T_M^L] = [L(L+1) - M(M\pm1)]^{1/2}T_{M\pm1}^L$ for $L = 1$, $M = 0$. The $M = \pm1$ components follow in the same way.

**Uses.**

- **Spin-free operators are singlets.** A spin-independent one-electron operator such as the electric dipole becomes $\sum_{pq}\langle\phi_p|\mathbf r|\phi_q\rangle\hat E_{pq}$, built from the singlet operator only. The Hamiltonian likewise contains only $\hat E_{pq}$ and products of them.
- **Spin-adapted orbital rotations.** For an RHF or spin-adapted MCSCF state, the orbital rotation operator must be totally symmetric, so it is built from $\hat E_{pq} - \hat E_{qp}$ ([[orbital-rotations]]). The triplet combinations $\hat T_{pq}(1,0) - \hat T_{qp}(1,0)$ generate the spin-symmetry-breaking rotations whose Hessian decides RHF→UHF stability ([[scf-second-order-and-stability]]).
- **Spin-adapted configurations.** $\hat E_{ai}|\Psi_0\rangle$ is the singlet singly excited configuration and $\hat T_{ai}(1,0)|\Psi_0\rangle$ the $M_S = 0$ triplet ([[spin-adapted-configurations]]).

!!! example "Numerical checks (computed for this note)"
    Two spatial orbitals (four spin orbitals), Jordan-Wigner matrices on the 16-dimensional Fock space:

    - $[\hat S_z, a_{1\alpha}^\dagger] - \tfrac12a_{1\alpha}^\dagger$, $[\hat S_+, a_{1\alpha}^\dagger]$ and $[\hat S_-, a_{1\alpha}^\dagger] - a_{1\beta}^\dagger$ all vanish exactly.
    - $[\hat S^2, \hat E_{21}] = 0$ and $[\hat S_+, \hat E_{21}] = 0$: the singlet excitation operator is a scalar.
    - $[\hat S_+, \hat T_{21}(1,0)] = \sqrt2\,\hat T_{21}(1,1)$ to $2\times10^{-16}$.
    - Acting on the closed shell $|1\alpha1\beta\rangle$: $\hat E_{21}$ gives $\langle\hat S^2\rangle = 0$ and $\hat T_{21}(1,0)$ gives $\langle\hat S^2\rangle = 2$. $\hat P_{21}^\dagger(0,0)|\text{vac}\rangle$ has $\langle\hat S^2\rangle = 0$.

## Example: the Fermi contact Hamiltonian (J-S Problem 1.4)

**First-quantized form.** For nuclei $a$ with spins $\mathbf I^a$,

$$
H_F = \sum_{i=1}^N\sum_a\frac{8\pi}{3}g\beta\gamma_a\,\mathbf S_i\cdot\mathbf I^a\,\delta(\mathbf r_i - \mathbf R_a),
$$

with $g$ the electron $g$ factor, $\beta$ the Bohr magneton and $\gamma_a$ the nuclear gyromagnetic factor.

**Second quantization.** This is a one-electron operator, so its matrix elements between spin orbitals give $\sum_{rs}\phi_r^*(\mathbf R_a)\phi_s(\mathbf R_a)\langle\sigma|\mathbf S|\sigma'\rangle\cdot\mathbf I^a\,a_{r\sigma}^\dagger a_{s\sigma'}$. Writing $\mathbf S\cdot\mathbf I = S_zI_z + \tfrac12(S_+I_- + S_-I_+)$ and collecting spin labels into the triplet operators:

$$
H_F = \sum_{a,r,s}\frac{4\pi}{3}g\beta\gamma_a\,\phi_r^*(\mathbf R_a)\phi_s(\mathbf R_a)\Big[-q_{rs}^\dagger(1,1)(I_x^a - iI_y^a) + q_{rs}^\dagger(1,-1)(I_x^a + iI_y^a) + \sqrt2\,q_{rs}^\dagger(1,0)I_z^a\Big].
$$

**Spin structure.** Only the triplet ($S = 1$) excitation operators appear, as they must for an operator that is a vector in electron spin. Its expectation value in a closed-shell singlet therefore vanishes; spin density at the nucleus is needed.

**Check (computed for this note).** For three spatial orbitals with random amplitudes $\phi_r(\mathbf R_a)$ and a random classical $\mathbf I^a$, the two forms agree as $64\times64$ Fock-space matrices to $1\times10^{-17}$.

## Helgaker, Jørgensen and Olsen's spin tensor operators

HJO use the same operators with a few differences in normalization and some additional relations.

**Annihilators.** The annihilators form a doublet after a sign and reordering: $\{-a_{p\beta}, a_{p\alpha}\}$ are the $m = +\tfrac12$ and $m = -\tfrac12$ components. $a_{p\beta}$ **raises** the projection, since it removes a $-\tfrac12$ electron.

**Excitation operators.**

- **Singlet:** $\hat S_{pq}^{0,0} = \tfrac1{\sqrt2}(a_{p\alpha}^\dagger a_{q\alpha} + a_{p\beta}^\dagger a_{q\beta}) = E_{pq}/\sqrt2$, so $E_{pq} = \sqrt2\,\hat S_{pq}^{0,0}$.
- **Triplet:** $\hat T_{pq}^{1,1} = -a_{p\alpha}^\dagger a_{q\beta}$, $\hat T_{pq}^{1,0} = \tfrac1{\sqrt2}(a_{p\alpha}^\dagger a_{q\alpha} - a_{p\beta}^\dagger a_{q\beta})$, $\hat T_{pq}^{1,-1} = a_{p\beta}^\dagger a_{q\alpha}$, identical to the $\hat T_{pq}(1,M)$ above.
- **No permutational symmetry in $p$, $q$.** Both are nonzero for $p = q$. Instead, conjugation reverses the excitation: $\hat S_{pq}^{0,0\dagger} = \hat S_{qp}^{0,0}$ and $\hat T_{pq}^{1,M\dagger} = (-1)^M\hat T_{qp}^{1,-M}$.
- **Cartesian triplets.** $\hat T_{pq}^x = \tfrac12(-\hat T_{pq}^{1,1} + \hat T_{pq}^{1,-1})$, $\hat T_{pq}^y = -\tfrac1{2i}(\hat T_{pq}^{1,1} + \hat T_{pq}^{1,-1})$, $\hat T_{pq}^z = \hat T_{pq}^{1,0}/\sqrt2$, with the simpler conjugation $\hat T_{pq}^{\mu\dagger} = \hat T_{qp}^\mu$ (HJO Eq. 2.3.27).

**Spin operators from triplet excitations.** $\hat S_+ = -\sum_p\hat T_{pp}^{1,1}$, $\hat S_z = \tfrac1{\sqrt2}\sum_p\hat T_{pp}^{1,0}$ and $\hat S_- = \sum_p\hat T_{pp}^{1,-1}$; equivalently $\sum_p\hat T_{pp}^\mu = \hat S_\mu$. The spin-orbit operator becomes $\hat V_{\mathrm{SO}} = \sum_{pq}(V_{pq}^+\hat T_{pq}^{1,-1} + \sqrt2V_{pq}^z\hat T_{pq}^{1,0} - V_{pq}^-\hat T_{pq}^{1,1})$, each term changing $M$ by a definite amount.

**Singlet excitations on a closed shell (HJO Eqs. 2.3.39-2.3.43).** With the singlet pair creator $\hat Q_{pq}^{0,0} = \hat P_{pq}^\dagger(0,0)$ and $[E_{pq},\hat Q_{rs}^{S,M}] = \hat Q_{ps}^{S,M}\delta_{qr} + \hat Q_{rp}^{S,M}\delta_{sq}$:

$$
\hat Q_{qq}^{0,0}|\text{vac}\rangle = \sqrt2\,a_{q\alpha}^\dagger a_{q\beta}^\dagger|\text{vac}\rangle\ \xrightarrow{E_{pq}}\ 2\hat Q_{pq}^{0,0}|\text{vac}\rangle\ \xrightarrow{E_{pq}}\ 2\hat Q_{pp}^{0,0}|\text{vac}\rangle\ \xrightarrow{E_{pq}}\ 0 .
$$

Repeated application of a singlet excitation takes a closed shell to the open-shell singlet, then to the doubly excited closed shell, and then stops.

!!! example "Checks (computed for this note)"
    Three spatial orbitals, 64-dimensional Fock space. All of the following hold to $2\times10^{-16}$ or exactly:

    - the annihilator-doublet relations;
    - $\hat T^{1,M\dagger}_{pq} = (-1)^M\hat T^{1,-M}_{qp}$ and $\hat T^{\mu\dagger}_{pq} = \hat T^\mu_{qp}$;
    - $\sum_p\hat T_{pp}^\mu = \hat S_\mu$ and the spherical forms of $\hat S_\pm$, $\hat S_z$;
    - the three-step $E_{pq}$ sequence.

    $\hat T_{pq}^x = \tfrac12(a_{p\alpha}^\dagger a_{q\beta} + a_{p\beta}^\dagger a_{q\alpha})$, as expected for $\hat S_x$-like excitations.

**Where spin tensors meet CSFs.** Coupling elementary operators into tensor strings is the basis of the genealogical construction of spin eigenfunctions ([[genealogical-coupling]]).

## Source

Jørgensen and Simons, *Second Quantization-Based Methods in Quantum Chemistry* (Academic Press, New York, 1981), Ch. 1, Sec. C "Tensor Operators", pp. 8-10, Eqs. (1.23)-(1.35); Problems and Solutions 1.3-1.4, pp. 14-17. The rank-reduction remark is from the same section; the uses in orbital rotations and stability analysis connect to J-S Ch. 2, Sec. B.8 (pp. 30-31), where the rotation operators are required to be totally symmetric tensor operators. Numerical checks computed for this note. Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, Chichester, 2000), Secs. 2.2-2.3, pp. 35-46, Eqs. (2.2.1)-(2.3.43); equations read from the page images.
