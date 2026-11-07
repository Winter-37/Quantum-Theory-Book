---
id: coupled-cluster-optimization-and-lagrangian
title: Solving the coupled-cluster equations and making them variational - Newton, the perturbation-based quasi-Newton step, DIIS, the CC Lagrangian, the Hellmann-Feynman theorem and Lagrangian density matrices
summary: The CC amplitude equations are solved by a quasi-Newton step in which the Jacobian is replaced by its orbital-energy diagonal, t ← t − Ω(t)/ε, accelerated by DIIS. Recomputed: HJO Table 13.2 for water CCSD/cc-pVDZ, digit for digit, including the 49-iteration crawl at 2R_ref without DIIS and the 13-15 iterations with DIIS. Because the CC energy is not variational, properties need a Lagrangian with multipliers t̄ that solve one linear system with the transposed Jacobian. The derivative is then a transition expectation value ⟨Λ|V|CC⟩. Checked for the water dipole: the Λ-density gives 1.365395 a.u. and the fixed-orbital finite-field derivative 1.365394, while the naive ⟨HF|e^{−T}z e^{T}|HF⟩ is off by 6 × 10⁻³.
status: in-progress
kind: algorithm
level: advanced
tags: [coupled-cluster, ccsd, quasi-newton, diis, jacobian, lagrangian, lambda-equations, hellmann-feynman, density-matrix, molecular-properties]
prerequisites: [coupled-cluster-hierarchy-and-size-extensivity, scf-convergence-diis-and-newton]
related: [eom-ccsd-and-size-extensivity, closed-shell-ccsd-t1-transformation, ci-optimization-newton-and-davidson, coupled-cluster-second-quantization]
order: 90
date: 2026-11-04
---

## Newton and quasi-Newton

**The vector function and its Jacobian (HJO Sec. 13.4.1).**

$$
\Omega_\mu(\mathbf t) = \langle\mu|e^{-\hat T}\hat He^{\hat T}|\text{HF}\rangle,\qquad
A_{\mu\nu} = \frac{\partial\Omega_\mu}{\partial t_\nu} = \langle\mu|e^{-\hat T}[\hat H,\hat\tau_\nu]e^{\hat T}|\text{HF}\rangle .
$$

- **Newton step.** $\mathbf A\,\Delta\mathbf t = -\boldsymbol\Omega$.
- **Cost.** Each step needs many Jacobian-vector products, which is too expensive for routine ground-state work. The same products are unavoidable in response theory and EOM-CC, though.

**Perturbation-based quasi-Newton (HJO Sec. 13.4.2).** In canonical orbitals $[\hat f, \hat\tau_\mu] = \varepsilon_\mu\hat\tau_\mu$, where $\varepsilon_\mu$ is the sum of virtual minus the sum of occupied orbital energies. So

$$
\Omega_\mu = \varepsilon_\mu t_\mu + \langle\mu|e^{-\hat T}\hat\Phi e^{\hat T}|\text{HF}\rangle,\qquad
A_{\mu\nu} = \varepsilon_\mu\delta_{\mu\nu} + \langle\mu|e^{-\hat T}[\hat\Phi,\hat\tau_\nu]e^{\hat T}|\text{HF}\rangle .
$$

- **Approximation.** $\hat\Phi$ (the fluctuation potential) is first order in Møller-Plesset theory, so drop it from $\mathbf A$: $\Delta t_\mu = -\Omega_\mu/\varepsilon_\mu$.
- **First iteration.** It starts from zero amplitudes and gives the MP1 amplitudes, so the first energy is MP2.
- **Typical cost.** 10-20 iterations for six decimals, up to 50 in hard cases.

**DIIS (HJO Sec. 13.4.3).**

- **Extrapolation.** $\mathbf t^{(n+1)} = \sum_kw_k(\mathbf t^{(k)} + \Delta\mathbf t^{(k)})$ with $\sum_kw_k = 1$.
- **Weights.** They minimize $\|\sum_kw_k\Delta\mathbf t^{(k)}\|$.
- **Not an optimizer itself.** DIIS only recombines the quasi-Newton steps already taken.

!!! example "HJO Table 13.2 recomputed: CCSD/cc-pVDZ water, energy error per iteration ($E_h$; computed for this note)"
    **Setup.** Iteration 1 is the energy of the MP1 amplitudes. Plain quasi-Newton is PySCF's `update_amps`. DIIS is my own: error vector $\Delta\mathbf t$, extrapolating from iteration 1 onwards, at most 8 vectors.

    | It. | QN, $R_{\text{ref}}$ | +DIIS | HJO +DIIS | QN, $2R_{\text{ref}}$ | +DIIS | HJO +DIIS |
    |---:|---:|---:|---:|---:|---:|---:|
    | 1 | 0.009388 | 0.009388 | 0.009387 | 0.032697 | 0.032697 | 0.032698 |
    | 2 | 0.004537 | 0.004537 | 0.004536 | 0.063687 | 0.063687 | 0.063687 |
    | 3 | 0.001233 | 0.000495 | 0.000495 | 0.019485 | 0.036548 | 0.036548 |
    | 4 | 0.000488 | 0.000015 | 0.000015 | 0.022513 | 0.008349 | 0.008349 |
    | 5 | 0.000188 | 0.000007 | 0.000006 | 0.010350 | 0.006522 | 0.006523 |
    | 6 | 0.000078 | −0.000004 | −0.000004 | 0.009594 | 0.001865 | 0.001866 |
    | 7 | 0.000033 | −0.000001 | −0.000001 | 0.005557 | 0.001044 | 0.001044 |
    | 8 | 0.000014 | 0.000000 | −0.000001 | 0.004722 | 0.000706 | 0.000706 |
    | 9 | 0.000006 | | 0.000000 | 0.003146 | −0.000023 | −0.000022 |
    | 10 | 0.000003 | | | 0.002590 | 0.000086 | 0.000073 |

    - **Plain quasi-Newton.** It matches HJO's QN columns to ±1 in the last digit throughout. At $2R_{\text{ref}}$ it needs 49 iterations to reach $10^{-6}$, exactly as in HJO. Converged energies: −76.238116 and −75.929633 $E_h$.
    - **DIIS.** It agrees through iteration 9. Beyond that the details depend on the subspace size.
    - **Undershoot.** Negative entries are energies *below* the converged CCSD energy, a visible sign that the CC energy is not variational.
    - **Why $2R_{\text{ref}}$ is slow.** The HF weight drops to 0.59, so $\hat\Phi$ is no longer small and the diagonal Jacobian is a poor model. That is where DIIS pays off most (49 → 13-15 iterations).

## The Lagrangian: making CC variational

**Construction (HJO Sec. 13.5.1).** With a perturbation $\alpha\hat V$:

$$
L(\alpha,\mathbf t,\bar{\mathbf t}) = \langle\text{HF}|(\hat H + \alpha\hat V)e^{\hat T}|\text{HF}\rangle + \sum_\mu\bar t_\mu\langle\mu|e^{-\hat T}(\hat H + \alpha\hat V)e^{\hat T}|\text{HF}\rangle .
$$

- **Stationary in $\bar{\mathbf t}$.** This is the amplitude equations.
- **Stationary in $\mathbf t$ (at $\alpha = 0$).** This gives one linear system for the multipliers, with the *transposed* Jacobian:

$$
\langle\text{HF}|[\hat H,\hat\tau_\nu]e^{\hat T}|\text{HF}\rangle + \sum_\mu\bar t_\mu A_{\mu\nu} = 0 .
$$

These are the "Λ equations".

**Hellmann-Feynman (HJO Sec. 13.5.2).** Because $L$ is stationary,

$$
\frac{dE}{d\alpha}\Big|_0 = \frac{\partial L}{\partial\alpha}\Big|_0 = \langle\Lambda|\hat V|\text{CC}\rangle,\qquad
\langle\Lambda| = \langle\text{HF}|e^{-\hat T} + \sum_\mu\bar t_\mu\langle\mu|e^{-\hat T} .
$$

- **No perturbed amplitudes.** The expression never needs the response of $\mathbf t$ to $\alpha$.
- **Size-extensive.** The first-order properties are size-extensive (HJO Exercise 13.1).
- **Real form.** For a manifestly real property, use $\tfrac12(\langle\Lambda|\hat V|\text{CC}\rangle + \text{c.c.})$.
- **Variational energy.** $E = \langle\Lambda|\hat H|\text{CC}\rangle$ is variational, so it is less sensitive to errors in $\mathbf t$ than $\langle\text{HF}|\hat H|\text{CC}\rangle$.

**Density matrices (HJO Sec. 13.5.3).**

- **Definition.** $D_{PQ} = \langle\Lambda|a^\dagger_Pa_Q|\text{CC}\rangle$ and $d_{PQRS}$ likewise.
- **Energy.** $E = \sum D_{PQ}h_{PQ} + \tfrac12\sum d_{PQRS}g_{PQRS}$.
- **Symmetry.** These matrices are not Hermitian. For Hermitian properties use the symmetric part, whose eigenvalues are real.

!!! example "Water CCSD/cc-pVDZ at $R_{\text{ref}}$: electronic $\langle z\rangle$ along the $C_2$ axis (bohr; computed for this note)"
    | Quantity | Value |
    |---|---:|
    | Hartree-Fock, $2\sum_iz_{ii}$ | 1.322184 |
    | Lagrangian, $\mathrm{Tr}(\mathbf D^\Lambda\mathbf z)$ from PySCF's Λ equations | **1.365395** |
    | Finite field, $dE_{\text{CCSD}}/dF$ with HF orbitals frozen (non-canonical CCSD at $F = \pm10^{-4}$) | **1.365394** |
    | Projected "expectation", $\langle\text{HF}|e^{-\hat T}\hat z e^{\hat T}|\text{HF}\rangle = z_{\text{HF}} + 4\sum_{ia}z_{ia}t_i^a$ | 1.359157 |
    | Finite field with orbitals relaxed | 1.363624 |

    - **Λ density.** It reproduces the true energy derivative at fixed orbitals to $10^{-6}$.
    - **Projected value.** Using $\hat T$ alone is wrong by $6\times10^{-3}$, more than half the size of the correlation correction itself.
    - **Orbital relaxation.** Allowing the orbitals to respond changes the derivative by another $1.8\times10^{-3}$. Analytic CC gradients therefore also need orbital-response multipliers (not treated in HJO Ch. 13).

## Source

Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, Chichester, 2000), Secs. 13.4-13.5, pp. 670-677, Eqs. (13.4.1)-(13.5.17), Table 13.2. Recomputed for this note with PySCF 2.14 (RCCSD, `solve_lambda`, `make_rdm1`), my own DIIS driver and finite-field runs (`hjo/c13/t132.py`, `hjo/c13/lagr.py`).
