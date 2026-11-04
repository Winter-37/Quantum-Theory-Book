---
id: lagrangian-for-nonvariational-energies
title: Variational reformulation of nonvariational energies - the Lagrangian and its multipliers
summary: A nonvariational energy E(α, λ), whose parameters λ satisfy conditions f(α, λ) = 0 other than stationarity, can be made variational by the Lagrangian L = E + λ̄·f. Stationarity in λ fixes the multipliers by one linear equation independent of the perturbation; stationarity in λ̄ restores the original conditions. Then dE/dα = ∂E/∂α + λ̄·∂f/∂α, with no wave-function response. Demonstrated for the orbital-relaxed CISD dipole of water, where the Lagrangian reproduces the relaxed finite-field derivative to 10⁻⁶.
status: in-progress
kind: derivation
level: advanced
tags: [lagrangian, z-vector, lagrange-multipliers, nonvariational, relaxed-density, cisd, molecular-properties]
prerequisites: [molecular-properties-and-response, hellmann-feynman-and-virial-theorems, scf-second-order-and-stability]
related: [analytic-gradients-and-force-constants, cisd, coupled-cluster-second-quantization, mp2, orbital-rotations]
also: [04_Electronic_Structure_Theory/07_Analytical_Derivatives_and_Response_Theory/07_Z_Vector_Method, 04_Electronic_Structure_Theory/07_Analytical_Derivatives_and_Response_Theory/04_Orbital_Response]
date: 2026-11-04
---

## The problem

**Setup.** Let the energy $E(\alpha,\boldsymbol\lambda)$ depend on a perturbation strength $\alpha$ (a field, a geometry) and on wave-function parameters $\boldsymbol\lambda$ (orbitals, CI or cluster amplitudes). At each $\alpha$ the parameters are fixed by some equations:

$$
\mathbf f(\alpha,\boldsymbol\lambda^*) = \mathbf 0 .
$$

**Derivative.** By the chain rule,

$$
\frac{\mathrm dE}{\mathrm d\alpha} = \frac{\partial E}{\partial\alpha}\Big|_* + \frac{\partial E}{\partial\boldsymbol\lambda}\Big|_*\cdot\frac{\partial\boldsymbol\lambda^*}{\partial\alpha} .
$$

- **Variational wave functions.** $\mathbf f = \partial E/\partial\boldsymbol\lambda$, so the second term vanishes and $\mathrm dE/\mathrm d\alpha = \partial E/\partial\alpha$. For $E = \langle\hat H + \alpha\hat V\rangle$ this is Hellmann-Feynman ([[hellmann-feynman-and-virial-theorems]]).
- **Nonvariational wave functions** (coupled cluster, perturbation theory, CI with Hartree-Fock orbitals). The response $\partial\boldsymbol\lambda^*/\partial\alpha$ seems to be needed, one set of linear equations for **each** perturbation.

## The Lagrangian

**Definition.** Treat $\mathbf f = \mathbf 0$ as constraints and introduce multipliers $\bar{\boldsymbol\lambda}$:

$$
L(\alpha,\boldsymbol\lambda,\bar{\boldsymbol\lambda}) = E(\alpha,\boldsymbol\lambda) + \bar{\boldsymbol\lambda}\cdot\mathbf f(\alpha,\boldsymbol\lambda).
$$

**Stationarity conditions (HJO Eqs. 4.2.85-4.2.86).**

$$
\frac{\partial L}{\partial\boldsymbol\lambda} = \frac{\partial E}{\partial\boldsymbol\lambda} + \bar{\boldsymbol\lambda}^{\mathsf T}\frac{\partial\mathbf f}{\partial\boldsymbol\lambda} = \mathbf 0,\qquad
\frac{\partial L}{\partial\bar{\boldsymbol\lambda}} = \mathbf f(\alpha,\boldsymbol\lambda) = \mathbf 0 .
$$

- **Conditions on $\boldsymbol\lambda$** determine the multipliers. This is one linear system, solved once at $\alpha = 0$ for all perturbations: the "Z-vector" idea.
- **Conditions on $\bar{\boldsymbol\lambda}$** reproduce the original equations, and at the stationary point $L = E$.

**Result (HJO Eq. 4.2.87).**

$$
\frac{\mathrm dE}{\mathrm d\alpha} = \frac{\partial L}{\partial\alpha}\Big|_* = \frac{\partial E}{\partial\alpha}\Big|_* + \bar{\boldsymbol\lambda}^*\cdot\frac{\partial\mathbf f}{\partial\alpha}\Big|_* .
$$

No wave-function response appears.

**Properties.**

- **Saddle point.** $L$ is linear in $\bar{\boldsymbol\lambda}$, so its stationary points are saddle points, never minima, even for ground states.
- **Errors.** The error in $L$ is quadratic in the errors in $\boldsymbol\lambda$ and $\bar{\boldsymbol\lambda}$.
- **Later uses in HJO.** The variational formulation of coupled cluster (Sec. 13.5), perturbation theory (Secs. 14.1, 14.3) and time-dependent properties.
- **Cost.** It pays when obtaining the multipliers is cheaper than computing the perturbed wave functions. That is the usual case when there are many perturbations, e.g. $3N$ nuclear displacements.

## Example: orbital-relaxed CISD dipole

**Ingredients.** In CISD with Hartree-Fock orbitals:

- $\boldsymbol\lambda = \boldsymbol\kappa$ are the occupied-virtual orbital rotations ([[orbital-rotations]]);
- $\mathbf f$ is the HF condition $F_{ai}(\boldsymbol\kappa,\alpha) = 0$;
- the CI coefficients are variational and drop out.

**Lagrangian.** $L = E_{\text{CISD}}(\boldsymbol\kappa,\alpha) + \sum_{ai}\bar z_{ai}F_{ai}(\boldsymbol\kappa,\alpha)$, with multipliers from $\mathbf A^{\mathsf T}\bar{\mathbf z} = -\partial E_{\text{CISD}}/\partial\boldsymbol\kappa$, where $\mathbf A = \partial\mathbf F/\partial\boldsymbol\kappa$ is the HF orbital Hessian ([[scf-second-order-and-stability]]).

**Relaxed derivative.** The unrelaxed expectation value plus $\bar{\mathbf z}\cdot\partial\mathbf F/\partial\alpha$. The second term is the orbital-relaxation correction to the "relaxed density" ([[molecular-properties-and-response]]).

!!! example "Water, STO-3G, Szabo's geometry, field along the $C_2$ axis (computed for this note)"
    10 occupied-virtual rotation parameters. Derivatives by central differences (step $10^{-4}$); CISD with PySCF.

    | Quantity | Value (a.u.) |
    |---|---:|
    | $\lVert\partial E_{\text{CISD}}/\partial\boldsymbol\kappa\rVert$ at the HF orbitals | $2.20\times10^{-3}$ |
    | $\partial E/\partial F$ with orbitals frozen (CISD expectation value) | 1.577728 |
    | Relaxation term $\bar{\mathbf z}\cdot\partial\mathbf F/\partial F$ | −0.000767 |
    | Lagrangian $\mathrm dE/\mathrm dF$ | 1.576961 |
    | Finite field, HF re-optimized in the field, then CISD | 1.576961 |

    - **Not stationary.** The CISD energy is not stationary with respect to the orbitals (nonzero orbital gradient), so the unrelaxed value differs from the true derivative.
    - **Agreement.** The Lagrangian, built from quantities at zero field only, reproduces the relaxed finite-field derivative to $10^{-6}$.
    - **Sign.** $\mathrm dE/\mathrm dF$ with the perturbation $+F\hat z_{\text{el}}$ is minus the electronic dipole component.

## Source

Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, Chichester, 2000), Sec. 4.2.8, pp. 123-125, Eqs. (4.2.75)-(4.2.87); Sec. 4.2.9, pp. 125-126. Equations read from the page image. The CISD dipole example is my own, computed with PySCF 2.14; the term "Z-vector" is general knowledge.
